"""XML sitemap loader: sitemap indexes, gzip, namespace-agnostic parsing.

load(url, fetch) never raises: errors of a single sitemap are collected and the
other sitemaps are still read.
"""
from __future__ import annotations

import xml.etree.ElementTree as ET
import zlib
from typing import Callable

from . import urls

STANDARD_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
MAX_URLS_PER_FILE = 50_000
MAX_UNCOMPRESSED = 50 * 1024 * 1024
GZIP_MAGIC = b"\x1f\x8b"
FEED_CHUNK = 1 << 16
MAX_HOST_MISMATCH_SAMPLES = 50


def _local(tag) -> str:
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def _ns(tag) -> str:
    return tag[1:].split("}", 1)[0] if isinstance(tag, str) and tag.startswith("{") else ""


def _child_text(elem, name: str):
    for child in elem:
        if _local(child.tag) == name:
            return (child.text or "").strip() or None
    return None


def gunzip(data: bytes, limit: int = MAX_UNCOMPRESSED):
    """Decompress gzip data up to limit+1 bytes. Returns (data, over_limit)."""
    out = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(data, limit + 1)
    return out[:limit], len(out) > limit


def parse_xml(body: bytes) -> dict:
    """Parse sitemap XML incrementally (tolerates truncated documents).

    Returns {"root": local name, "namespace": ns, "urls": [...], "sitemaps": [...],
    "error": str or None}.
    """
    parser = ET.XMLPullParser(events=("start", "end"))
    out = {"root": None, "namespace": None, "urls": [], "sitemaps": [], "error": None}
    depth = 0
    try:
        for i in range(0, max(len(body), 1), FEED_CHUNK):
            parser.feed(body[i:i + FEED_CHUNK])
            depth = _drain(parser, out, depth)
        parser.close()
        _drain(parser, out, depth)
    except ET.ParseError as exc:
        _drain(parser, out, depth)
        out["error"] = f"XML parse error: {exc}"
    return out


def _drain(parser, out: dict, depth: int) -> int:
    for event, elem in parser.read_events():
        if event == "start":
            depth += 1
            if depth == 1:
                out["root"], out["namespace"] = _local(elem.tag), _ns(elem.tag)
            continue
        depth -= 1
        if depth != 1:
            continue
        name = _local(elem.tag)
        if name == "url":
            alternates, images, videos = [], 0, 0
            for child in elem:
                cname = _local(child.tag)
                if cname == "link" and (child.get("rel") or "").lower() == "alternate":
                    alternates.append({"hreflang": child.get("hreflang"), "href": child.get("href")})
                elif cname == "image":
                    images += 1
                elif cname == "video":
                    videos += 1
            loc = _child_text(elem, "loc")
            if loc:
                out["urls"].append({"loc": loc, "lastmod": _child_text(elem, "lastmod"),
                                    "alternates": alternates, "images": images, "videos": videos})
            elem.clear()
        elif name == "sitemap":
            loc = _child_text(elem, "loc")
            if loc:
                out["sitemaps"].append({"loc": loc, "lastmod": _child_text(elem, "lastmod")})
            elem.clear()
    return depth


def load(url: str, fetch: Callable, *, max_depth: int = 3, max_sitemaps: int = 50,
         max_urls: int = 100_000) -> dict:
    """Read a sitemap (or sitemap index) and its children.

    fetch: callable(url) -> object with status, body (bytes), error, truncated
    (seokit.http.fetch or a Throttle). Returns a summary dict; see docs/page-schema.md.
    """
    state = {
        "url": url, "sitemaps": [], "urls": [], "errors": [], "warnings": [], "truncated": False,
        "host_mismatch": [], "host_mismatch_count": 0, "_seen": set(),
        "_site": urls.site_key(urls.safe_normalize(url) or url),
        "_limits": (max_depth, max_sitemaps, max_urls),
    }
    _load_one(url, fetch, 0, state)
    state.pop("_seen")
    state.pop("_site")
    state.pop("_limits")
    state["url_count"] = len(state["urls"])
    return state


def _load_one(url: str, fetch: Callable, depth: int, state: dict) -> None:
    max_depth, max_sitemaps, max_urls = state["_limits"]
    norm = urls.safe_normalize(url)
    info = {"url": url, "depth": depth, "status": None, "type": None, "url_count": 0,
            "children": 0, "gzipped": False, "lastmod_count": 0, "error": None}
    if norm is None:
        info["error"] = "invalid URL"
        state["sitemaps"].append(info)
        state["errors"].append({"url": url, "error": info["error"]})
        return
    if norm in state["_seen"]:
        return
    if len(state["sitemaps"]) >= max_sitemaps:
        state["truncated"] = True
        msg = f"stopped after {max_sitemaps} sitemap files"
        if msg not in state["warnings"]:
            state["warnings"].append(msg)
        return
    state["_seen"].add(norm)
    state["sitemaps"].append(info)

    def fail(message):
        info["error"] = message
        state["errors"].append({"url": url, "error": message})

    try:
        resp = fetch(norm)
    except Exception as exc:  # noqa: BLE001 - a bad child never aborts its siblings
        fail(f"{type(exc).__name__}: {exc}")
        return
    info["status"] = getattr(resp, "status", None)
    if getattr(resp, "error", None):
        fail(resp.error)
        return
    if info["status"] != 200:
        fail(f"HTTP {info['status']}")
        return
    body = resp.body or b""
    if getattr(resp, "truncated", False):
        state["truncated"] = True
        state["warnings"].append(f"{url}: download stopped at the size limit")
    if body[:2] == GZIP_MAGIC:  # detected by magic bytes, whatever the headers say
        info["gzipped"] = True
        try:
            body, over = gunzip(body)
        except zlib.error as exc:
            fail(f"gzip data could not be decompressed: {exc}")
            return
        if over:
            state["truncated"] = True
            state["warnings"].append(f"{url}: more than 50 MB uncompressed (limit); only the first 50 MB read")
    elif len(body) > MAX_UNCOMPRESSED:
        state["warnings"].append(f"{url}: more than 50 MB uncompressed (limit)")

    parsed = parse_xml(body)
    root = parsed["root"]
    if root not in ("urlset", "sitemapindex"):
        if parsed["error"] and root is None:
            fail(parsed["error"])
        else:
            fail(f"not a sitemap (root element <{root}>)")
        return
    if parsed["namespace"] != STANDARD_NS:
        state["warnings"].append(
            f"{url}: namespace {parsed['namespace'] or '(none)'!r} is not {STANDARD_NS!r}")
    if parsed["error"]:
        state["warnings"].append(f"{url}: {parsed['error']} (entries before the error were kept)")
        info["error"] = parsed["error"]

    if root == "urlset":
        info["type"] = "urlset"
        entries = parsed["urls"]
        info["url_count"] = len(entries)
        info["lastmod_count"] = sum(1 for e in entries if e["lastmod"])
        if len(entries) > MAX_URLS_PER_FILE:
            state["warnings"].append(f"{url}: {len(entries)} URLs, more than the 50,000 allowed per file")
        room = max_urls - len(state["urls"])
        if len(entries) > room:
            entries = entries[:room]
            state["truncated"] = True
            msg = f"stopped collecting after {max_urls} URLs"
            if msg not in state["warnings"]:
                state["warnings"].append(msg)
        for e in entries:
            if urls.site_key(urls.safe_normalize(e["loc"]) or e["loc"]) != state["_site"]:
                state["host_mismatch_count"] += 1
                if len(state["host_mismatch"]) < MAX_HOST_MISMATCH_SAMPLES:
                    state["host_mismatch"].append(e["loc"])
        state["urls"].extend(entries)
        return

    info["type"] = "sitemapindex"
    children = parsed["sitemaps"]
    info["children"] = len(children)
    info["lastmod_count"] = sum(1 for c in children if c["lastmod"])
    if depth + 1 > max_depth:
        state["truncated"] = True
        state["warnings"].append(f"{url}: nested sitemap indexes deeper than {max_depth} levels not read")
        return
    for child in children:
        _load_one(child["loc"], fetch, depth + 1, state)
