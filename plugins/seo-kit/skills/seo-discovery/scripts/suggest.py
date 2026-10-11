#!/usr/bin/env python3
"""Google autocomplete suggestions for a list of searches.

A free hint of how people phrase their searches. It gives NO volumes and does not
promise that a search brings traffic. The endpoint is not a documented API: it can
change or rate-limit requests, so use it sparingly (there is a pause between requests).

Usage:
  python suggest.py "physio oslo" "back pain exercises" --lang en
  python suggest.py "studio ferri" --lang it --expand        # adds "query a".."query z", "query 0".."9", "come query"...
  python suggest.py "acme widgets" --hl de --gl at --json

--hl/--gl default from --lang: en -> en/us, it -> it/it, de -> de/de, es -> es/es,
fr -> fr/fr, pt -> pt/br; any other language -> hl=<lang>, gl=us.

Exit codes: 0 done · 2 usage error · 3 stopped by Google rate limiting (HTTP 429).
"""
import argparse
import json
import os
import re
import string
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


def _bootstrap():
    """Put <plugin>/lib on sys.path (walks up from this file to find lib/seokit)."""
    here = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(here, "lib", "seokit")):
            sys.path.insert(0, os.path.join(here, "lib"))
            return
        parent = os.path.dirname(here)
        if parent == here:
            sys.stderr.write("seo-kit: cannot find the lib/seokit folder of the plugin\n")
            sys.exit(2)
        here = parent


_bootstrap()

from seokit import __version__, report  # noqa: E402
from seokit.bots import USER_AGENTS  # noqa: E402

ENDPOINT = "https://suggestqueries.google.com/complete/search"
PAUSE = 0.5
TIMEOUT = 15
LANG_DEFAULTS = {"en": ("en", "us"), "it": ("it", "it"), "de": ("de", "de"), "es": ("es", "es"),
                 "fr": ("fr", "fr"), "pt": ("pt", "br")}
LATIN = string.ascii_lowercase  # a-z, j k w x y included
ALPHABETS = {"en": LATIN, "it": LATIN, "de": LATIN, "es": LATIN, "fr": LATIN, "pt": LATIN}
DIGITS = string.digits
QUESTION_WORDS = {
    "en": ["how", "what", "why", "where", "when", "which", "who"],
    "it": ["come", "cosa", "perché", "dove", "quando", "quale", "chi"],
    "de": ["wie", "was", "warum", "wo", "wann", "welche", "wer"],
    "es": ["cómo", "qué", "por qué", "dónde", "cuándo", "cuál", "quién"],
    "fr": ["comment", "quoi", "pourquoi", "où", "quand", "quel", "qui"],
    "pt": ["como", "o que", "por que", "onde", "quando", "qual", "quem"],
}

_sleep = time.sleep  # patched by tests


class RateLimited(Exception):
    """Google answered HTTP 429."""


def locale_for(lang, hl=None, gl=None):
    lang = (lang or "en").lower()
    primary = re.split(r"[-_]", lang)[0]
    d_hl, d_gl = LANG_DEFAULTS.get(primary, (primary, "us"))
    return hl or d_hl, gl or d_gl


def variants(query, lang, expand):
    """The query itself, plus with --expand: query + letter/digit and question word + query."""
    out = [query]
    if expand:
        primary = re.split(r"[-_]", (lang or "en").lower())[0]
        out += [f"{query} {c}" for c in ALPHABETS.get(primary, LATIN) + DIGITS]
        out += [f"{w} {query}" for w in QUESTION_WORDS.get(primary, [])]
    return out


def fetch_suggestions(q, hl, gl):
    params = urllib.parse.urlencode({"client": "firefox", "hl": hl, "gl": gl, "ie": "utf-8", "oe": "utf-8", "q": q})
    req = urllib.request.Request(f"{ENDPOINT}?{params}", headers={"User-Agent": USER_AGENTS["browser"]})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read()
            charset = resp.headers.get_content_charset() if hasattr(resp.headers, "get_content_charset") else None
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            raise RateLimited("HTTP 429 Too Many Requests") from None
        raise
    data = json.loads(raw.decode(charset or "utf-8", "replace"))
    if not isinstance(data, list) or len(data) < 2 or not isinstance(data[1], list):
        raise ValueError("unexpected response format")
    return [s for s in data[1] if isinstance(s, str)]


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("queries", nargs="+", help="searches to complete")
    ap.add_argument("--lang", default="en", help="language of the searches (default en)")
    ap.add_argument("--hl", help="interface language sent to Google (default from --lang)")
    ap.add_argument("--gl", help="country sent to Google (default from --lang)")
    ap.add_argument("--expand", action="store_true",
                    help="also try 'query a'..'query z', 'query 0'..'query 9' and the language's question words")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a list")
    ap.add_argument("--version", action="version", version=f"seo-kit {__version__}")
    return ap


def main(argv=None):
    report.setup_stdout()
    args = build_parser().parse_args(argv)
    queries = [q.strip() for q in args.queries if q.strip()]
    if not queries:
        report.eprint("error: give at least one non-empty query")
        return 2
    hl, gl = locale_for(args.lang, args.hl, args.gl)
    results, errors = {}, []
    rate_limited = False
    first = True
    for query in queries:
        found = []
        for v in variants(query, args.lang, args.expand):
            if not first:
                _sleep(PAUSE)
            first = False
            try:
                for s in fetch_suggestions(v, hl, gl):
                    if s not in found:
                        found.append(s)
            except RateLimited as exc:
                errors.append({"query": v, "error": str(exc)})
                report.eprint(f"error: {v!r}: {exc}; stopping (try again later)")
                rate_limited = True
                break
            except Exception as exc:  # noqa: BLE001 - network or format problem for one request
                errors.append({"query": v, "error": f"{type(exc).__name__}: {exc}"})
                report.eprint(f"error: {v!r}: {type(exc).__name__}: {exc}")
        results[query] = found
        if rate_limited:
            break

    if args.json:
        report.print_json({"hl": hl, "gl": gl, "expand": args.expand, "results": results, "errors": errors,
                           "rate_limited": rate_limited,
                           "note": "Autocomplete suggestions: no search volumes."})
    else:
        print(f"Autocomplete suggestions (hl={hl}, gl={gl}); no search volumes.")
        for query, found in results.items():
            print(f"\n## {query}")
            for s in found:
                print(f"- {s}")
            if not found:
                print("- (no suggestions)")
        if errors:
            print(f"\n{len(errors)} request(s) failed; see stderr.")
    return 3 if rate_limited else 0


if __name__ == "__main__":
    sys.exit(main())
