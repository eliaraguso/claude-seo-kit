"""URL helpers: validation, IDNA and percent-encoding, comparison keys."""
from __future__ import annotations

import re
import urllib.parse

DEFAULT_PORTS = {"http": 80, "https": 443}
# Link schemes that are neither internal nor external pages.
OTHER_SCHEMES = ("mailto", "tel", "sms", "whatsapp", "javascript", "data", "ftp")

# Characters left as they are when percent-encoding (RFC 3986 reserved + "%").
_PATH_SAFE = "/%:@!$&'()*+,;=~"
_QUERY_SAFE = _PATH_SAFE + "?"
_SCHEME_RE = re.compile(r"^([A-Za-z][A-Za-z0-9+.\-]*):")


class InvalidURL(ValueError):
    """Raised for URLs that cannot be fetched (bad scheme, no host, bad host)."""


def scheme_of(href: str) -> str:
    """Lower-case scheme of an href, or '' when it is relative."""
    m = _SCHEME_RE.match((href or "").strip())
    return m.group(1).lower() if m else ""


def idna_host(host: str) -> str:
    """Return the ASCII (punycode) form of a host name, lower-cased."""
    host = (host or "").strip().rstrip(".")
    try:
        host.encode("ascii")
        return host.lower()
    except UnicodeEncodeError:
        pass
    try:
        return host.encode("idna").decode("ascii").lower()
    except UnicodeError as exc:
        raise InvalidURL(f"host {host!r} cannot be converted to IDNA: {exc}") from None


def fix_header_text(value: str) -> str:
    """Headers are decoded as latin-1 by http.client; recover raw UTF-8 bytes."""
    try:
        value.encode("ascii")
        return value
    except UnicodeEncodeError:
        pass
    try:
        return value.encode("latin-1").decode("utf-8")
    except UnicodeError:
        return value


def normalize_url(url: str, *, header_value: bool = False) -> str:
    """Validate an http(s) URL and return it in fetchable ASCII form.

    Non-ASCII hosts become IDNA; non-ASCII characters and spaces in the path and
    query are percent-encoded (existing escapes are kept). The fragment is dropped.
    Raise InvalidURL with a readable message when the URL cannot be fetched.
    """
    if url is None or not str(url).strip():
        raise InvalidURL("empty URL")
    url = str(url).strip()
    if header_value:
        url = fix_header_text(url)
    try:  # urllib raises ValueError for e.g. "http://[::1" (unbalanced IPv6 bracket)
        parts = urllib.parse.urlsplit(url)
        hostname = parts.hostname
    except ValueError as exc:
        raise InvalidURL(f"{exc}: {url!r}") from None
    scheme = parts.scheme.lower()
    if scheme not in ("http", "https"):
        hint = ""
        if not parts.scheme or "." in parts.scheme or not parts.netloc:
            hint = f" - did you mean https://{url.split('://')[-1]}?"
        raise InvalidURL(f"URL must start with http:// or https:// (got {url!r}){hint}")
    if not hostname:
        raise InvalidURL(f"URL has no host name: {url!r}")
    host = idna_host(hostname)
    if ":" in host:  # IPv6 literal
        host = f"[{host}]"
    try:
        port = parts.port
    except ValueError:
        raise InvalidURL(f"URL has an invalid port: {url!r}") from None
    netloc = host
    if port is not None and port != DEFAULT_PORTS.get(scheme):
        netloc = f"{host}:{port}"
    if parts.username:
        userinfo = urllib.parse.quote(parts.username, safe="%")
        if parts.password:
            userinfo += ":" + urllib.parse.quote(parts.password, safe="%")
        netloc = f"{userinfo}@{netloc}"
    path = urllib.parse.quote(parts.path, safe=_PATH_SAFE) or "/"
    query = urllib.parse.quote(parts.query, safe=_QUERY_SAFE)
    return urllib.parse.urlunsplit((scheme, netloc, path, query, ""))


def safe_normalize(url: str):
    """normalize_url that returns None instead of raising."""
    try:
        return normalize_url(url)
    except (InvalidURL, ValueError):
        return None


def site_key(url: str) -> str:
    """Host used to decide internal vs external: no 'www.', no default port."""
    try:
        parts = urllib.parse.urlsplit(url)
        host = idna_host(parts.hostname or "")
        port = parts.port
    except (InvalidURL, ValueError):
        return ""
    if host.startswith("www."):
        host = host[4:]
    scheme = parts.scheme.lower()
    if port is not None and port != DEFAULT_PORTS.get(scheme):
        host = f"{host}:{port}"
    return host


def compare_key(url: str) -> str:
    """Key for comparing two URLs: scheme/host lower-cased, default port and
    trailing slash removed, fragment dropped, non-ASCII percent-encoded."""
    norm = safe_normalize(url)
    if norm is None:
        return (url or "").strip()
    parts = urllib.parse.urlsplit(norm)
    path = parts.path
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/") or "/"
    if path == "/":
        path = ""
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc.lower(), path, parts.query, ""))


def origin_of(url: str) -> str:
    parts = urllib.parse.urlsplit(normalize_url(url))
    return f"{parts.scheme}://{parts.netloc}"


def path_and_query(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    out = parts.path or "/"
    if parts.query:
        out += "?" + parts.query
    return out
