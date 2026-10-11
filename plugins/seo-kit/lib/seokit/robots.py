"""robots.txt parsing and evaluation with Google's documented semantics.

- Groups: consecutive user-agent lines share the rules that follow them; groups
  naming the same crawler are merged.
- The crawler obeys only the most specific group that names it (falling back to
  documented parents such as Googlebot-Image -> Googlebot, then to ``*``).
- Within the group the longest matching rule wins; on equal length ``allow`` wins.
- ``*`` matches any sequence, ``$`` anchors the end of the URL path.
- HTTP status: 4xx (except 429) = no restrictions; 5xx and 429 = site unavailable.
"""
from __future__ import annotations

import re
import urllib.parse
from typing import Optional

from .bots import ROBOTS_FALLBACK

_UA_KEYS = {"user-agent", "useragent", "user agent", "user_agent"}
_RULE_KEYS = {
    "allow": "allow",
    "disallow": "disallow",
    # Misspellings Google's open-source parser accepts.
    "dissallow": "disallow", "dissalow": "disallow", "disalow": "disallow",
    "diasllow": "disallow", "disallaw": "disallow",
}
_SITEMAP_KEYS = {"sitemap", "site-map"}
_LINE_RE = re.compile(r"^\s*([A-Za-z][A-Za-z _-]*?)\s*:\s*(.*?)\s*$")
_TOKEN_RE = re.compile(r"[A-Za-z_*\-]+")
_PATH_SAFE = "/%:@!$&'()*+,;=~?"
MAX_INVALID_LINES = 20


def _product_token(value: str) -> str:
    m = _TOKEN_RE.match(value.strip())
    return m.group(0).lower() if m else ""


def parse(text) -> dict:
    """Parse robots.txt text (str or bytes).

    Returns {"groups": [{"user_agents": [...], "rules": [{"type", "path", "line"}],
    "other": [...]}], "sitemaps": [...], "invalid_lines": [...], "html_suspect": bool}.
    """
    if isinstance(text, bytes):
        text = text.decode("utf-8", "replace")
    text = (text or "").lstrip("\ufeff")
    head = text[:1024].lstrip().lower()
    result = {
        "groups": [], "sitemaps": [], "invalid_lines": [],
        "html_suspect": head.startswith("<!doctype") or head.startswith("<html") or "<html" in head,
    }
    current = None
    last_was_ua = False
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.split("#", 1)[0].replace("\ufeff", "").strip()
        if not line:
            continue
        m = _LINE_RE.match(line)
        if not m:
            if len(result["invalid_lines"]) < MAX_INVALID_LINES:
                result["invalid_lines"].append({"line": lineno, "text": raw.strip()[:200]})
            continue
        key = " ".join(m.group(1).lower().split())
        value = m.group(2)
        if key in _UA_KEYS:
            if current is None or not last_was_ua:
                current = {"user_agents": [], "rules": [], "other": []}
                result["groups"].append(current)
            current["user_agents"].append(value)
            last_was_ua = True
        elif key in _RULE_KEYS:
            last_was_ua = False
            if current is None:
                if len(result["invalid_lines"]) < MAX_INVALID_LINES:
                    result["invalid_lines"].append(
                        {"line": lineno, "text": raw.strip()[:200], "reason": "rule before any user-agent"})
                continue
            current["rules"].append({"type": _RULE_KEYS[key], "path": value, "line": lineno})
        elif key in _SITEMAP_KEYS:
            if value:
                result["sitemaps"].append(value)
        else:
            # crawl-delay, host, noindex...: ignored by Google; kept for the report.
            if current is not None:
                current["other"].append({"key": key, "value": value, "line": lineno})
    return result


def _groups(parsed):
    if isinstance(parsed, dict):
        return parsed.get("groups", [])
    return parsed or []


def sitemaps(parsed) -> list:
    """Sitemap URLs declared in robots.txt (in file order, without duplicates)."""
    if isinstance(parsed, dict):
        return list(dict.fromkeys(parsed.get("sitemaps", [])))
    return []


def select_group(parsed, ua: str):
    """Return (token_matched, rules) for the group a crawler obeys, or (None, [])."""
    groups = _groups(parsed)
    token = _product_token(ua)
    for candidate in [token] + ROBOTS_FALLBACK.get(token, []):
        matched = [g for g in groups if candidate in {_product_token(u) for u in g["user_agents"]}]
        if matched:
            return candidate, [r for g in matched for r in g["rules"]]
    star = [g for g in groups if "*" in {_product_token(u) for u in g["user_agents"]}]
    if star:
        return "*", [r for g in star for r in g["rules"]]
    return None, []


def _encode(s: str) -> str:
    return urllib.parse.quote(s, safe=_PATH_SAFE + "*$")


def _pattern_regex(pattern: str):
    anchored = pattern.endswith("$")
    if anchored:
        pattern = pattern[:-1]
    body = "".join(".*" if ch == "*" else re.escape(ch) for ch in _encode(pattern))
    return re.compile("^" + body + ("$" if anchored else ""), re.DOTALL)


def _target_path(path_or_url: str) -> str:
    if re.match(r"^[A-Za-z][A-Za-z0-9+.\-]*://", path_or_url or ""):
        parts = urllib.parse.urlsplit(path_or_url)
        path = parts.path or "/"
        if parts.query:
            path += "?" + parts.query
    else:
        path = path_or_url or "/"
    if not path.startswith("/"):
        path = "/" + path
    return _encode(path)


def evaluate(parsed, ua: str, path: str) -> dict:
    """Decide whether `ua` may crawl `path` (a path or a full URL).

    Returns {"allowed": bool, "group": token or None, "rule": "disallow: /x" or None}.
    """
    target = _target_path(path)
    if target == "/robots.txt":
        return {"allowed": True, "group": None, "rule": None}
    group, rules = select_group(parsed, ua)
    best = None  # (length, is_allow, rule)
    for rule in rules:
        pattern = rule["path"]
        if not pattern:  # an empty value matches nothing
            continue
        if _pattern_regex(pattern).match(target):
            candidate = (len(pattern), rule["type"] == "allow", rule)
            if best is None or candidate[:2] > best[:2]:
                best = candidate
    if best is None:
        return {"allowed": True, "group": group, "rule": None}
    rule = best[2]
    return {"allowed": rule["type"] == "allow", "group": group, "rule": f"{rule['type']}: {rule['path']}"}


def is_allowed(parsed, ua: str, path: str) -> bool:
    return evaluate(parsed, ua, path)["allowed"]


def status_semantics(status: Optional[int]) -> str:
    """How Google treats the robots.txt HTTP status.

    parse (2xx) · allow_all (4xx except 429: as if there were no robots.txt) ·
    unavailable (5xx, 429 or no response: Google pauses crawling of the site).
    """
    if status is None:
        return "unavailable"
    if 200 <= status < 300:
        return "parse"
    if status == 429 or 500 <= status < 600:
        return "unavailable"
    return "allow_all"
