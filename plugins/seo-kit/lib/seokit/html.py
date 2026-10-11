"""Raw-HTML page parser producing the shared page schema (docs/page-schema.md).

Rules worth knowing:
- ``<svg>``/``<math>`` subtrees never contribute to title, H1 or headings.
- ``<script>``, ``<style>``, ``<noscript>`` and ``<template>`` contents never count
  as text, links, images or head violations (JSON-LD scripts are read separately).
- ``<base href>`` is honoured when resolving relative URLs.
- Internal links share the page host, ignoring ``www.`` and the default port.
"""
from __future__ import annotations

import json
import re
import urllib.parse
from html.parser import HTMLParser
from typing import Optional

from . import urls

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param",
        "source", "track", "wbr", "keygen", "frame"}
HEAD_ALLOWED = {"title", "meta", "link", "script", "style", "base", "noscript", "template"}
NON_TEXT = {"script", "style", "noscript", "template"}
FOREIGN = {"svg", "math"}
NON_MAIN = {"nav", "header", "footer", "aside"}
SPA_ROOT_IDS = {"root", "app", "__next", "___gatsby", "__nuxt", "svelte", "q-app"}
SPA_ROOT_TAGS = {"app-root", "app"}
SPA_MAIN_TEXT_LIMIT = 300
SPA_MAX_CHILDREN = 3
ROBOTS_META_NAMES = ("robots", "googlebot", "bingbot", "googlebot-news")
LAZY_ATTRS = ("data-src", "data-lazy-src", "data-original", "data-srcset", "data-lazy")
DOC_RE = re.compile(r"\.(pdf|docx?|pptx?|xlsx?|odt|ods|odp|rtf)$", re.I)
HREFLANG_RE = re.compile(r"^(x-default|[a-z]{2,3}(-[a-z]{4})?(-([a-z]{2}|\d{3}))?)$", re.I)
# Frequent mistakes: valid-looking codes that are not ISO 639-1 / ISO 3166-1.
HREFLANG_LANG_MISTAKES = {"jp": "ja", "cn": "zh", "gr": "el", "dk": "da", "cz": "cs", "kr": "ko", "ua": "uk"}
HREFLANG_REGION_MISTAKES = {"uk": "gb", "eu": None}
X_ROBOTS_DIRECTIVE_KEYS = {"unavailable_after", "max-snippet", "max-image-preview", "max-video-preview"}


def _clean(text: str) -> str:
    return " ".join(text.split())


def parse_jsonld(raw: str):
    """Parse a JSON-LD block leniently.

    Returns (data, error, recovered). `error` is None for valid JSON; when the block
    only parses after relaxing (literal control characters, trailing commas, HTML
    comment/CDATA wrappers) `recovered` is True and `error` explains the problem.
    """
    s = (raw or "").strip()
    wrapped = False
    m = re.match(r"^(<!--|(//\s*)?<!\[CDATA\[)", s)
    if m:
        s, wrapped = s[m.end():], True
    m = re.search(r"(-->|(//\s*)?\]\]>)\s*$", s)
    if m:
        s, wrapped = s[:m.start()], True
    s = s.strip()
    if not s:
        return None, "empty JSON-LD block", False
    try:
        data = json.loads(s)
        return data, ("wrapped in an HTML comment or CDATA section" if wrapped else None), wrapped
    except ValueError as exc:
        first = f"{exc}"
    try:
        return json.loads(s, strict=False), f"invalid JSON (control character inside a string): {first}", True
    except ValueError:
        pass
    relaxed = re.sub(r",(\s*[}\]])", r"\1", s)
    try:
        return json.loads(relaxed, strict=False), f"invalid JSON (trailing comma): {first}", True
    except ValueError:
        return None, f"invalid JSON: {first}", False


def jsonld_types(node) -> list:
    """Every @type in a JSON-LD structure, at any depth (order kept, no duplicates)."""
    found: list = []

    def walk(n):
        if isinstance(n, list):
            for item in n:
                walk(item)
        elif isinstance(n, dict):
            t = n.get("@type")
            for value in (t if isinstance(t, list) else [t]):
                if isinstance(value, str) and value and value not in found:
                    found.append(value)
            for key, value in n.items():
                if key != "@type":
                    walk(value)

    walk(node)
    return found


def parse_robots_directives(values, *, header: bool = False) -> dict:
    """Map crawler name ('*' for all) -> set of directives, for meta robots or X-Robots-Tag."""
    out: dict = {}
    for value in values or []:
        target = "*"
        text = value or ""
        if header:
            m = re.match(r"^\s*([A-Za-z][\w\-]*)\s*:\s*(.*)$", text)
            if m and m.group(1).lower() not in X_ROBOTS_DIRECTIVE_KEYS:
                target, text = m.group(1).lower(), m.group(2)
        for part in text.split(","):
            directive = part.strip().lower()
            if directive:
                out.setdefault(target, set()).add(directive.split(":")[0].strip())
    return out


class PageParser(HTMLParser):
    """Collects the page schema. Use parse_page() unless you need the raw parser."""

    def __init__(self, url: str):
        super().__init__(convert_charrefs=True)
        self.url = url
        self.base = url
        self.base_href: Optional[str] = None
        self.stack: list = []
        self.in_head = False
        self.body_started = False
        self.title_buf: Optional[list] = None
        self.heading: Optional[dict] = None
        self.anchor: Optional[dict] = None
        self.jsonld_buf: Optional[list] = None
        self.jsonld_count = 0
        self.title_depth = -1
        self.text: list = []
        self.main_text: list = []
        self.spa_root: Optional[dict] = None
        self.page_site = urls.site_key(url)
        self.d = {
            "title": [], "meta_description": [], "robots_meta": {}, "canonicals": [],
            "hreflang": [], "lang": None, "viewport": None, "og": {}, "twitter": {},
            "h1": [], "headings": [], "internal_links": [], "external_links": [],
            "other_links": {}, "anchors_without_href": 0, "images": [], "documents": [],
            "jsonld": [], "jsonld_errors": [], "microdata_present": False, "rdfa_present": False,
            "head_invalid_tags": [], "icons": [], "meta_refresh": None,
        }

    # -- context helpers -------------------------------------------------
    def _inside(self, names) -> bool:
        return any(t in names for t in self.stack)

    def _resolve(self, href: str) -> str:
        href = (href or "").strip()
        try:
            joined = urllib.parse.urljoin(self.base, href)
        except ValueError:  # malformed href such as "http://[::1"
            return href
        return urls.safe_normalize(joined) or joined

    # -- tag handling ----------------------------------------------------
    def handle_starttag(self, tag, attrs):
        self._start(tag.lower(), attrs, self_closing=False)

    def handle_startendtag(self, tag, attrs):
        self._start(tag.lower(), attrs, self_closing=True)

    def _start(self, tag, attrs, self_closing):
        a = {}
        for k, v in attrs:
            a.setdefault(k.lower(), v if v is not None else "")
        foreign = self._inside(FOREIGN)
        nontext = self._inside(NON_TEXT)

        if "itemscope" in a or "itemtype" in a:
            self.d["microdata_present"] = True
        if "vocab" in a or "typeof" in a:
            self.d["rdfa_present"] = True

        # SPA root container: count its direct element children.
        if self.spa_root is not None and not self.spa_root["closed"] \
                and len(self.stack) == self.spa_root["depth"] + 1:
            self.spa_root["children"] += 1

        if tag == "html" and self.d["lang"] is None and a.get("lang"):
            self.d["lang"] = a.get("lang").strip()
        elif tag == "head":
            self.in_head = True
        elif tag == "body":
            self.in_head = False
            self.body_started = True
        elif self.in_head and tag not in HEAD_ALLOWED \
                and tag not in ("html", "head") and not nontext and not foreign:
            # Per the HTML parsing rules this element closes <head>: later meta/link
            # tags end up in <body> and Google may ignore them.
            if tag not in self.d["head_invalid_tags"]:
                self.d["head_invalid_tags"].append(tag)
            self.body_started = True
        elif not self.in_head and not self.body_started and tag not in HEAD_ALLOWED \
                and tag not in ("html", "head"):
            self.body_started = True

        if not foreign and not nontext:
            self._collect(tag, a)

        if tag == "script" and "ld+json" in (a.get("type") or "").lower() and not nontext:
            self.jsonld_buf = []

        if self_closing or tag in VOID:
            return
        if self.spa_root is None and not foreign and not nontext and (
                tag in SPA_ROOT_TAGS or (a.get("id") or "").strip() in SPA_ROOT_IDS):
            ident = (a.get("id") or "").strip()
            self.spa_root = {"selector": f"{tag}#{ident}" if ident else tag,
                             "depth": len(self.stack), "children": 0, "closed": False}
        depth = len(self.stack)
        self.stack.append(tag)
        if foreign or nontext:
            return
        if tag == "title":
            self.title_buf = []
            self.title_depth = depth
        elif re.fullmatch(r"h[1-6]", tag):
            self.heading = {"level": int(tag[1]), "buf": [], "depth": depth}
        elif tag == "a" and self.anchor is not None:
            self.anchor["depth"] = depth

    def _collect(self, tag, a):
        d = self.d
        if tag == "meta":
            name = (a.get("name") or a.get("property") or "").strip().lower()
            content = a.get("content", "")
            if name == "description":
                d["meta_description"].append(_clean(content))
            elif name in ROBOTS_META_NAMES:
                d["robots_meta"].setdefault(name, []).append(content.strip())
            elif name == "viewport" and d["viewport"] is None:
                d["viewport"] = content.strip()
            elif name.startswith("og:"):
                d["og"].setdefault(name, content.strip())
            elif name.startswith("twitter:"):
                d["twitter"].setdefault(name, content.strip())
            if (a.get("http-equiv") or "").lower() == "refresh" and d["meta_refresh"] is None:
                d["meta_refresh"] = content.strip()
        elif tag == "base" and self.base_href is None and a.get("href"):
            self.base_href = self._resolve(a["href"])
            self.base = self.base_href
        elif tag == "link":
            rel = (a.get("rel") or "").lower().split()
            href = a.get("href") or ""
            if "canonical" in rel:
                d["canonicals"].append({"href": href, "in_body": self.body_started})
            if "alternate" in rel and a.get("hreflang"):
                d["hreflang"].append({"lang": a["hreflang"].strip(), "href": href,
                                      "resolved": self._resolve(href) if href else None})
            if "icon" in rel:
                d["icons"].append({"rel": " ".join(rel), "sizes": a.get("sizes") or None,
                                   "href": self._resolve(href) if href else None})
        elif tag == "a":
            if self.anchor is not None:  # a new <a> implicitly closes the previous one
                self._finish_anchor()
            self.anchor = {"href": a.get("href"), "rel": (a.get("rel") or "").lower().split(),
                           "buf": [], "img_alt": [], "depth": None}
        elif tag == "img":
            alt = a.get("alt") if "alt" in a else None
            src = a.get("src") or ""
            lazy = next((a[k] for k in LAZY_ATTRS if a.get(k)), None)
            d["images"].append({
                "src": src, "resolved": self._resolve(src) if src else None,
                "alt": alt, "alt_empty": alt is not None and not alt.strip(),
                "width": a.get("width"), "height": a.get("height"),
                "loading": a.get("loading"), "lazy_attr": lazy,
            })
            if self.anchor is not None and alt:
                self.anchor["img_alt"].append(alt)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "head":
            self.in_head = False
        if tag not in self.stack:
            return
        while self.stack:
            open_tag = self.stack.pop()
            self._close(open_tag)
            if open_tag == tag:
                break

    def _close(self, tag):
        if self.spa_root is not None and not self.spa_root["closed"] \
                and len(self.stack) == self.spa_root["depth"]:
            self.spa_root["closed"] = True
        if tag == "script" and self.jsonld_buf is not None:
            self._finish_jsonld()
        elif tag == "title" and self.title_buf is not None and len(self.stack) == self.title_depth:
            self.d["title"].append(_clean("".join(self.title_buf)))
            self.title_buf = None
        elif re.fullmatch(r"h[1-6]", tag) and self.heading is not None \
                and len(self.stack) == self.heading["depth"]:
            text = _clean("".join(self.heading["buf"]))
            self.d["headings"].append({"level": self.heading["level"], "text": text})
            if self.heading["level"] == 1:
                self.d["h1"].append(text)
            self.heading = None
        elif tag == "a" and self.anchor is not None and len(self.stack) == self.anchor["depth"]:
            self._finish_anchor()

    def _finish_jsonld(self):
        raw = "".join(self.jsonld_buf or [])
        self.jsonld_buf = None
        index = self.jsonld_count
        self.jsonld_count += 1
        data, error, recovered = parse_jsonld(raw)
        if data is not None:
            self.d["jsonld"].append(data)
        if error:
            self.d["jsonld_errors"].append({"index": index, "error": error[:300], "recovered": recovered})

    def _finish_anchor(self):
        anc, self.anchor = self.anchor, None
        href = anc["href"]
        if href is None or not href.strip():
            self.d["anchors_without_href"] += 1
            return
        href = href.strip()
        text = _clean("".join(anc["buf"])) or _clean(" ".join(anc["img_alt"]))
        if href.startswith("#"):
            key = "fragment"
        else:
            key = urls.scheme_of(href)
        if key == "fragment" or (key and key not in ("http", "https")):
            self.d["other_links"][key] = self.d["other_links"].get(key, 0) + 1
            return
        resolved = self._resolve(href)
        link = {"href": href, "resolved": resolved, "text": text, "rel": anc["rel"],
                "nofollow": "nofollow" in anc["rel"]}
        try:
            path = urllib.parse.urlsplit(resolved).path
        except ValueError:
            path = ""
        if DOC_RE.search(path) and resolved not in self.d["documents"]:
            self.d["documents"].append(resolved)
        if urls.site_key(resolved) == self.page_site:
            self.d["internal_links"].append(link)
        else:
            self.d["external_links"].append(link)

    def handle_data(self, data):
        if self.jsonld_buf is not None:
            self.jsonld_buf.append(data)
            return
        foreign = self._inside(FOREIGN)
        if self.title_buf is not None:
            if not foreign:
                self.title_buf.append(data)
            return
        if foreign or self._inside(NON_TEXT):
            return
        if self.heading is not None:
            self.heading["buf"].append(data)
        if self.anchor is not None:
            self.anchor["buf"].append(data)
        if self.in_head and not self.body_started:
            return
        chunk = _clean(data)
        if chunk:
            self.text.append(chunk)
            if not self._inside(NON_MAIN):
                self.main_text.append(chunk)

    # -- result ----------------------------------------------------------
    def result(self) -> dict:
        while self.stack:  # close anything left open (unterminated documents)
            self._close(self.stack.pop())
        if self.anchor is not None:
            self._finish_anchor()
        d = dict(self.d)
        canonicals = d.pop("canonicals")
        head_canon = [c for c in canonicals if not c["in_body"]]
        chosen = (head_canon or canonicals or [None])[0]
        canonical = {"href": None, "resolved": None, "self_referencing": None,
                     "in_body": bool(canonicals) and not head_canon, "count": len(canonicals),
                     "all": [c["href"] for c in canonicals]}
        if chosen is not None:
            canonical["href"] = chosen["href"]
            if chosen["href"].strip():
                canonical["resolved"] = self._resolve(chosen["href"])
                canonical["self_referencing"] = urls.compare_key(canonical["resolved"]) == urls.compare_key(self.url)
        d["canonical"] = canonical
        for h in d["hreflang"]:
            h["valid_code"] = _hreflang_valid(h["lang"])
        d["hreflang_issues"] = hreflang_issues(d["hreflang"], self.url)
        skips, prev = [], 0
        for h in d["headings"]:
            if prev and h["level"] > prev + 1:
                skips.append({"from": f"h{prev}", "to": f"h{h['level']}", "text": h["text"][:100]})
            prev = h["level"]
        d["heading_skips"] = skips
        d["images_without_alt"] = sum(1 for i in d["images"] if i["alt"] is None)
        types: list = []
        for block in d["jsonld"]:
            for t in jsonld_types(block):
                if t not in types:
                    types.append(t)
        d["jsonld_types"] = types
        visible = " ".join(self.text)
        d["visible_text"] = visible
        d["text_blocks"] = list(self.text)
        d["visible_text_chars"] = len(visible)
        d["main_text_chars"] = len(" ".join(self.main_text))
        root = self.spa_root
        d["spa_root"] = root["selector"] if root else None
        d["spa_shell_suspect"] = bool(root and root["children"] <= SPA_MAX_CHILDREN
                                      and d["main_text_chars"] < SPA_MAIN_TEXT_LIMIT)
        d["base_href"] = self.base_href
        return d


def _hreflang_valid(code: str) -> bool:
    code = (code or "").strip()
    if not HREFLANG_RE.match(code):
        return False
    if code.lower() == "x-default":
        return True
    parts = code.lower().split("-")
    if parts[0] in HREFLANG_LANG_MISTAKES:
        return False
    region = parts[-1] if len(parts) > 1 and len(parts[-1]) == 2 else None
    return region not in HREFLANG_REGION_MISTAKES


def hreflang_issues(entries: list, page_url: str) -> list:
    """Problems visible on one page: invalid codes, conflicting duplicates, no self-reference."""
    issues = []
    seen: dict = {}
    for h in entries:
        code = (h.get("lang") or "").strip()
        if not h.get("valid_code", _hreflang_valid(code)):
            parts = code.lower().split("-")
            hint = ""
            if parts and parts[0] in HREFLANG_LANG_MISTAKES:
                hint = f" (language code is {HREFLANG_LANG_MISTAKES[parts[0]]!r})"
            elif len(parts) > 1 and parts[-1] in HREFLANG_REGION_MISTAKES:
                fix = HREFLANG_REGION_MISTAKES[parts[-1]]
                hint = f" (region code is {fix.upper()!r})" if fix else " (not a country code)"
            issues.append({"issue": "invalid_code", "detail": f"{code!r}{hint}"})
        key = code.lower()
        target = urls.compare_key(h.get("resolved") or "")
        if key in seen and seen[key] != target:
            issues.append({"issue": "duplicate_code", "detail": f"{code!r} points to more than one URL"})
        seen.setdefault(key, target)
    if entries:
        own = urls.compare_key(page_url)
        if not any(urls.compare_key(h.get("resolved") or "") == own for h in entries):
            issues.append({"issue": "missing_self_reference",
                           "detail": "the hreflang set does not include this page"})
    return issues


def hreflang_return_issues(pages: list) -> list:
    """Cross-page check: every alternate fetched in the same run must link back."""
    by_key = {}
    for p in pages:
        if p.get("final_url"):
            by_key[urls.compare_key(p["final_url"])] = p
    out = []
    for p in pages:
        own = urls.compare_key(p.get("final_url") or "")
        for h in p.get("hreflang") or []:
            target = urls.compare_key(h.get("resolved") or "")
            if not target or target == own or target not in by_key:
                continue
            back = by_key[target].get("hreflang") or []
            if not any(urls.compare_key(b.get("resolved") or "") == own for b in back):
                out.append({"page": p["final_url"], "alternate": h.get("resolved"), "lang": h.get("lang"),
                            "issue": "missing_return_link"})
    return out


def indexability(page: dict, x_robots: list, status: Optional[int]) -> dict:
    """{"value": bool, "reasons": [...]} from status, meta robots and X-Robots-Tag (Google's view)."""
    reasons = []
    if status is not None and not (200 <= status < 300):
        reasons.append(f"HTTP status {status}")
    meta = page.get("robots_meta") or {}
    for name in ("robots", "googlebot"):
        directives = parse_robots_directives(meta.get(name, [])).get("*", set())
        if directives & {"noindex", "none"}:
            reasons.append(f"noindex in <meta name=\"{name}\">")
    header = parse_robots_directives(x_robots, header=True)
    for target in ("*", "googlebot"):
        if header.get(target, set()) & {"noindex", "none"}:
            who = "" if target == "*" else f" for {target}"
            reasons.append(f"noindex in X-Robots-Tag{who}")
    return {"value": not reasons, "reasons": reasons}


def parse_page(html_text: str, url: str, headers=None, status: Optional[int] = None) -> dict:
    """Parse raw HTML into the page schema.

    headers: a seokit.http.Headers (or anything with get_all) for X-Robots-Tag.
    The result also holds ``text_blocks`` (visible text per text node) for the typo
    check; scripts drop it from their output.
    """
    parser = PageParser(url)
    parse_error = None
    try:
        parser.feed(html_text or "")
        parser.close()
    except Exception as exc:  # noqa: BLE001 - malformed markup must not stop a run
        parse_error = f"{type(exc).__name__}: {exc}"
    page = parser.result()
    page["x_robots_tag"] = list(headers.get_all("X-Robots-Tag")) if headers is not None else []
    page["indexable"] = indexability(page, page["x_robots_tag"], status)
    if parse_error:
        page["parse_error"] = parse_error
    return page
