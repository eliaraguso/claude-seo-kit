#!/usr/bin/env python3
"""Collect SEO facts from a live site, standard library only.

Reads the raw HTML returned by the server (what a crawler that does not run
JavaScript sees) and the site files (robots.txt, sitemaps). JavaScript is not
executed: compare with the rendered DOM (extract_dom.js in a browser) or with the
URL Inspection tool in Search Console.

Usage:
  python seo_fetch.py https://northwind-physio.example                  # home page + site checks
  python seo_fetch.py https://northwind-physio.example --sitemap 30     # plus up to 30 sitemap URLs
  python seo_fetch.py https://northwind-physio.example/a https://northwind-physio.example/b --no-site
  python seo_fetch.py https://northwind-physio.example --lang en --terms "physio oslo;back pain" --json out.json

Crawler user agents are simulated: a firewall that verifies crawler IP addresses
may treat the real crawlers differently, so the user-agent comparison is a hint,
not proof.

Exit codes: 0 done (findings are in the output) · 2 invalid URL or site unreachable.
"""
import argparse
import os
import re
import sys
import urllib.parse
import uuid


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

from seokit import __version__  # noqa: E402
from seokit import bots, dns, report, robots, sitemap, typos, urls  # noqa: E402
from seokit import html as seohtml  # noqa: E402
from seokit import http as seohttp  # noqa: E402

GOOGLE_HTML_LIMIT = 2 * 1024 * 1024       # Googlebot reads the first 2 MB of an HTML file
ROBOTS_LIMIT = 500 * 1024                  # Google reads the first 500 KiB of robots.txt
VISIBLE_TEXT_PREVIEW = 1500
CHALLENGE_MARKERS = ("cf-challenge", "_cf_chl_opt", "captcha-delivery", "Just a moment", "Access denied",
                     "Request unsuccessful", "datadome")
# Plain phrases that also occur in ordinary copy: only counted on an error status or a small page.
CHALLENGE_PHRASES = ("Just a moment", "Access denied", "Request unsuccessful")
CHALLENGE_SMALL_PAGE = 20_000
CDN_HEADERS = (("cf-ray", "cloudflare"), ("x-vercel-id", "vercel"), ("x-nf-request-id", "netlify"),
               ("x-amz-cf-id", "cloudfront"), ("x-served-by", "fastly"), ("x-akamai-transformed", "akamai"))
LOCAL_HOSTS = ("localhost", "127.0.0.1", "::1", "[::1]")


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="+", help="one or more page URLs (http:// or https://); the first sets the site")
    ap.add_argument("--sitemap", type=int, default=0, metavar="N", help="also analyse up to N URLs from the sitemaps")
    ap.add_argument("--max-pages", type=int, default=None, metavar="N", help="never analyse more than N pages in total")
    ap.add_argument("--no-site", action="store_true", help="skip robots.txt, sitemaps, host variants, 404 probe, DNS")
    ap.add_argument("--no-ua", action="store_true", help="skip the user-agent comparison (same as --ua-set none)")
    ap.add_argument("--ua-set", choices=sorted(bots.UA_SETS), default="default",
                    help="user agents compared on the first page (default: browser + main search and AI crawlers)")
    ap.add_argument("--lang", metavar="xx", help="site language: sent as Accept-Language by the browser UA and "
                    "used to pick the typo pack; crawler UAs never send Accept-Language")
    ap.add_argument("--terms", help="terms separated by ';' to look for in titles, headings and text")
    ap.add_argument("--delay", type=float, default=1.0, metavar="SECONDS", help="pause between requests (default 1.0)")
    ap.add_argument("--timeout", type=float, default=20, metavar="SECONDS", help="timeout per request (default 20)")
    ap.add_argument("--full-text", action="store_true", help="keep the whole visible text in the output")
    ap.add_argument("--json", metavar="PATH", help="write the full result to this file instead of stdout")
    ap.add_argument("--version", action="version", version=f"seo-kit {__version__}")
    return ap


# -- helpers -------------------------------------------------------------------

def _hops(resp):
    return max(len(resp.chain) - 1, 0)


def _cdn(headers):
    found = [name for header, name in CDN_HEADERS if header in headers]
    server = (headers.get("Server") or "").lower()
    for name in ("cloudflare", "vercel", "netlify", "akamai"):
        if name in server and name not in found:
            found.append(name)
    return found


def _is_html(resp):
    ctype = resp.content_type.lower()
    if "html" in ctype:
        return True
    return not ctype and "<html" in resp.text[:2048].lower()


def term_regex(term):
    words = [re.escape(w.casefold()) for w in term.split()]
    return re.compile(r"(?<!\w)" + r"\s+".join(words) + r"(?!\w)")


def term_coverage(page, terms):
    """Word-boundary, case-insensitive (casefold) matches of each term."""
    out = {}
    fields = {
        "in_title": " ".join(page.get("title") or []),
        "in_description": " ".join(page.get("meta_description") or []),
        "in_h1": " ".join(page.get("h1") or []),
        "in_headings": " ".join(h["text"] for h in page.get("headings") or []),
    }
    text = (page.get("visible_text") or "").casefold()
    for term in terms:
        rx = term_regex(term)
        entry = {name: bool(rx.search(value.casefold())) for name, value in fields.items()}
        entry["text_count"] = len(rx.findall(text))
        out[term] = entry
    return out


def _covers(entry):
    return entry["text_count"] > 0 or any(v for k, v in entry.items() if k.startswith("in_"))


# -- site checks ----------------------------------------------------------------

def check_robots(origin, fetch):
    resp = fetch(origin + "/robots.txt", max_bytes=4 * ROBOTS_LIMIT)
    status = None if resp.error else resp.status
    info = {
        "url": origin + "/robots.txt", "status": resp.status, "final_url": resp.final_url or None,
        "error": resp.error, "status_semantics": robots.status_semantics(status),
        "content_type": resp.content_type or None, "bytes": len(resp.body),
        "over_500kib": len(resp.body) > ROBOTS_LIMIT, "html_suspect": False,
        "groups": [], "sitemaps": [], "invalid_lines": [], "verdicts_root": None, "note": None,
    }
    parsed = None
    if info["status_semantics"] == "parse":
        parsed = robots.parse(resp.body[:ROBOTS_LIMIT])
        info.update(groups=parsed["groups"], sitemaps=robots.sitemaps(parsed),
                    invalid_lines=parsed["invalid_lines"], html_suspect=parsed["html_suspect"])
        if parsed["html_suspect"]:
            info["note"] = "robots.txt returns an HTML page (SPA fallback?): no rules can be read from it"
        info["verdicts_root"] = {t: robots.is_allowed(parsed, t, "/") for t in bots.TOKENS}
    elif info["status_semantics"] == "allow_all":
        info["note"] = f"HTTP {resp.status}: Google treats the site as having no robots.txt (everything allowed)"
        info["verdicts_root"] = {t: True for t in bots.TOKENS}
    else:
        info["note"] = ("robots.txt unavailable (5xx, 429 or no response): Google stops crawling the site "
                        "while this lasts")
    return info, parsed


def check_sitemaps(origin, declared, fetch):
    candidates = declared or [origin + "/sitemap.xml"]
    out, all_locs = [], []

    def fetch_xml(u):
        return fetch(u, max_bytes=sitemap.MAX_UNCOMPRESSED + 1,
                     accept="application/xml,text/xml;q=0.9,*/*;q=0.8")

    for url in candidates:
        res = sitemap.load(url, fetch_xml)
        all_locs.extend(e["loc"] for e in res["urls"])
        out.append({
            "url": url, "declared_in_robots": bool(declared), "url_count": res["url_count"],
            "files": res["sitemaps"], "errors": res["errors"], "warnings": res["warnings"],
            "truncated": res["truncated"], "host_mismatch_count": res["host_mismatch_count"],
            "host_mismatch_sample": res["host_mismatch"][:10],
            "with_lastmod": sum(1 for e in res["urls"] if e["lastmod"]),
            "with_alternates": sum(1 for e in res["urls"] if e["alternates"]),
            "sample_urls": [e["loc"] for e in res["urls"][:20]],
        })
    return {"sitemaps": out, "total_urls": len(all_locs)}, all_locs


def check_host_variants(origin, fetch):
    parts = urllib.parse.urlsplit(origin)
    host = parts.hostname or ""
    port = f":{parts.port}" if parts.port else ""
    if host in LOCAL_HOSTS or host.endswith(".localhost") or dns._is_ip(host):
        names = [host]
    else:
        bare = host[4:] if host.startswith("www.") else host
        # www. variants only for the registrable domain: www.shop.<domain> usually does not exist.
        names = [bare, "www." + bare] if bare == dns.registrable_domain(bare) else [host]
    variants = []
    for name in names:
        for scheme in ("https", "http"):
            variants.append(f"{scheme}://{name}{port}/")
    rows = []
    for v in variants:
        r = fetch(v, max_bytes=65536, retries=0)
        rows.append({"url": v, "status": r.status, "hops": _hops(r), "final_url": r.final_url or None,
                     "chain": [h["status"] for h in r.chain], "error": r.error})
    finals = {urls.compare_key(r["final_url"]) for r in rows if not r["error"] and r["status"]}
    return {
        "variants": rows,
        "all_reach_same_final_url": len(finals) == 1 and all(not r["error"] for r in rows),
        "final_urls": sorted(finals),
        "multi_hop": [r["url"] for r in rows if r["hops"] > 1],
    }


def check_not_found(origin, fetch):
    probe = f"{origin}/seo-kit-404-check-{uuid.uuid4().hex[:8]}"
    r = fetch(probe, max_bytes=262144, retries=0)
    status = r.status
    if r.error or status is None:
        verdict = "error"
    elif status in (404, 410):
        verdict = "ok"
    elif 200 <= status < 300:
        home = urls.compare_key(origin + "/")
        verdict = "soft_404_redirect_to_home" if urls.compare_key(r.final_url) == home else "soft_404"
    elif status >= 500:
        verdict = "server_error"
    else:
        verdict = "other"
    return {"url": probe, "status": status, "final_url": r.final_url or None, "hops": _hops(r),
            "verdict": verdict, "error": r.error}


def ua_comparison(url, fetch, names, lang):
    results = {}
    for name in names:
        r = fetch(url, ua=name, lang=lang if name == "browser" else None, retries=0)
        head = r.text[:200_000].lower()
        suspicious = r.status is None or not 200 <= r.status < 300 or len(r.body) < CHALLENGE_SMALL_PAGE
        markers = [m for m in CHALLENGE_MARKERS if m.lower() in head and (suspicious or m not in CHALLENGE_PHRASES)]
        title, main_chars = None, None
        if r.status is not None and r.text:
            parsed = seohtml.parse_page(r.text, r.final_url or url)
            title = (parsed["title"] or [None])[0]
            main_chars = parsed["main_text_chars"]
        results[name] = {"status": r.status, "final_url": r.final_url or None, "hops": _hops(r),
                         "bytes": len(r.body), "title": title, "main_text_chars": main_chars,
                         "challenge_markers": markers, "error": r.error}
    differences = []
    base_name = "browser" if "browser" in results else next(iter(results), None)
    base = results.get(base_name) or {}
    for name, res in results.items():
        if res["challenge_markers"]:
            differences.append(f"{name}: challenge or block page markers {res['challenge_markers']}")
        if name == base_name:
            continue
        if res["status"] != base.get("status"):
            differences.append(f"{name}: HTTP {res['status']} (vs {base.get('status')} for {base_name})")
        if base.get("bytes") and res["bytes"] and not (0.5 <= res["bytes"] / base["bytes"] <= 2):
            differences.append(f"{name}: {res['bytes']} bytes (vs {base['bytes']} for {base_name})")
        if res["title"] != base.get("title"):
            differences.append(f"{name}: title {res['title']!r} (vs {base.get('title')!r})")
    return {"url": url, "results": results, "differences": differences,
            "note": "Crawler user agents are simulated; real crawlers may be verified by IP."}


# -- pages --------------------------------------------------------------------------

def apply_robots(page, robots_info, robots_parsed):
    """Per-crawler robots.txt verdicts for the page (None when robots.txt is unknown)."""
    if page.get("status") is None:
        return
    semantics = (robots_info or {}).get("status_semantics")
    if robots_parsed is not None and semantics == "parse":
        verdicts = {t: robots.is_allowed(robots_parsed, t, page["final_url"]) for t in bots.TOKENS}
    elif semantics == "allow_all":
        verdicts = {t: True for t in bots.TOKENS}
    else:
        verdicts = None
    page["robots_txt_allowed"] = verdicts
    if verdicts is not None and not verdicts["Googlebot"] and page.get("indexable"):
        page["indexable"]["value"] = False
        page["indexable"]["reasons"].append("blocked by robots.txt for Googlebot (content cannot be crawled)")

def analyze_page(url, fetch, *, lang=None, robots_info=None, robots_parsed=None, terms=None):
    r = fetch(url)
    page = {
        "url": url, "final_url": r.final_url or url, "status": r.status, "chain": r.chain,
        "content_type": r.content_type or None, "bytes": len(r.body), "transfer_bytes": r.transfer_bytes,
        "over_2mb": len(r.body) > GOOGLE_HTML_LIMIT, "elapsed_ms": r.elapsed_ms, "encoding": r.encoding,
        "encoding_source": r.encoding_source, "truncated": r.truncated, "error": r.error,
        "fetch_warnings": r.warnings, "server": r.headers.get("Server"), "cdn": _cdn(r.headers),
        "link_header": r.headers.get_all("Link"),
    }
    if r.status is None:
        return page
    if _is_html(r):
        page.update(seohtml.parse_page(r.text, page["final_url"], r.headers, r.status))
    else:
        page["not_html"] = True
        page["x_robots_tag"] = r.headers.get_all("X-Robots-Tag")
        page["indexable"] = seohtml.indexability({}, page["x_robots_tag"], r.status)
    apply_robots(page, robots_info, robots_parsed)
    found = typos.find(page, lang or page.get("lang")) if not page.get("not_html") else None
    if found is not None:
        page["typo_suspects"] = found
    if terms:
        page["term_coverage"] = term_coverage(page, terms)
    page.pop("text_blocks", None)
    return page


def duplicates(pages):
    """Duplicate titles/descriptions among indexable fetched pages, keyed by final URL."""
    seen, titles, descriptions = set(), {}, {}
    for p in pages:
        status = p.get("status")
        if p.get("error") or status is None or not 200 <= status < 300 or p.get("not_html"):
            continue
        reasons = (p.get("indexable") or {}).get("reasons") or []
        if any("noindex" in r for r in reasons):
            continue
        key = urls.compare_key(p["final_url"])
        if key in seen:
            continue
        seen.add(key)
        for t in p.get("title") or []:
            if t:
                titles.setdefault(t, []).append(p["final_url"])
        for d in p.get("meta_description") or []:
            if d:
                descriptions.setdefault(d, []).append(p["final_url"])
    return {"title": {k: v for k, v in titles.items() if len(v) > 1},
            "meta_description": {k: v for k, v in descriptions.items() if len(v) > 1}}


def main(argv=None):
    report.setup_stdout()
    args = build_parser().parse_args(argv)
    try:
        targets = list(dict.fromkeys(urls.normalize_url(u) for u in args.urls))
    except urls.InvalidURL as exc:
        report.eprint(f"error: {exc}")
        return 2
    if args.max_pages is not None and args.max_pages < 1:
        report.eprint("error: --max-pages must be at least 1")
        return 2
    terms = [t.strip() for t in (args.terms or "").split(";") if t.strip()]
    origin = urls.origin_of(targets[0])
    fetch = seohttp.Throttle(delay=args.delay, lang=args.lang, timeout=args.timeout)
    out = {"tool": "seo_fetch", "version": __version__, "origin": origin, "lang": args.lang,
           "requested_urls": args.urls, "site": {}, "pages": [], "warnings": []}

    first = analyze_page(targets[0], fetch, lang=args.lang, terms=terms)
    unreachable = first["status"] is None
    robots_info, robots_parsed, sitemap_locs = None, None, []
    if unreachable:
        out["warnings"].append(f"{targets[0]} could not be fetched: {first['error']}")
    elif not args.no_site:
        robots_info, robots_parsed = check_robots(origin, fetch)
        out["site"]["robots"] = robots_info
        out["site"]["sitemaps"], sitemap_locs = check_sitemaps(origin, robots_info["sitemaps"], fetch)
        out["site"]["host_variants"] = check_host_variants(origin, fetch)
        out["site"]["not_found_probe"] = check_not_found(origin, fetch)
        out["site"]["dns"] = dns.summary(urllib.parse.urlsplit(origin).hostname or "")
    if not unreachable and not args.no_ua:
        names = bots.UA_SETS[args.ua_set]
        if names:
            out["site"]["ua_comparison"] = ua_comparison(targets[0], fetch, names, args.lang)

    page_urls = list(targets)
    if args.sitemap and sitemap_locs:
        added = 0
        for loc in sitemap_locs:
            norm = urls.safe_normalize(loc)
            if norm and norm not in page_urls:
                page_urls.append(norm)
                added += 1
                if added >= args.sitemap:
                    break
    elif args.sitemap and not args.no_site and not unreachable:
        out["warnings"].append("--sitemap: no URLs found in the sitemaps")
    if args.max_pages is not None and len(page_urls) > args.max_pages:
        out["warnings"].append(f"--max-pages {args.max_pages}: {len(page_urls) - args.max_pages} URLs not analysed")
        page_urls = page_urls[:args.max_pages]

    # The first page was fetched before robots.txt was read: add its verdicts now.
    apply_robots(first, robots_info, robots_parsed)
    pages = [first]
    if not unreachable:
        for u in page_urls[1:]:
            pages.append(analyze_page(u, fetch, lang=args.lang, robots_info=robots_info,
                                      robots_parsed=robots_parsed, terms=terms))

    out["pages"] = pages
    out["duplicates"] = duplicates(pages)
    out["hreflang_return_issues"] = seohtml.hreflang_return_issues(
        [p for p in pages if p.get("hreflang")])
    if terms:
        out["term_coverage"] = {
            t: [p["final_url"] for p in pages if p.get("term_coverage") and _covers(p["term_coverage"][t])]
            for t in terms}
    for p in pages:
        text = p.get("visible_text") or ""
        if not args.full_text and len(text) > VISIBLE_TEXT_PREVIEW:
            p["visible_text"] = text[:VISIBLE_TEXT_PREVIEW] + " [...]"
            p["visible_text_truncated"] = True

    if args.json:
        report.write_json(args.json, out)
        errors = sum(1 for p in pages if p.get("error"))
        print(f"Wrote {args.json}: {len(pages)} page(s), {errors} with errors")
    else:
        report.print_json(out)
    if unreachable:
        report.eprint(f"error: {targets[0]} is unreachable: {first['error']}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
