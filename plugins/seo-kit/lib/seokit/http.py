"""HTTP fetching with a recorded redirect chain, never raising on network errors.

Note: this module is ``seokit.http``; it does not shadow the standard ``http``
package because it is only importable through the ``seokit`` package.
"""
from __future__ import annotations

import codecs
import email.utils
import http.client
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from . import urls
from .bots import user_agent

REDIRECT_CODES = (301, 302, 303, 307, 308)
RETRY_CODES = (429, 503)
MAX_REDIRECTS = 10
MAX_RETRY_WAIT = 30.0
DEFAULT_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
META_SCAN_BYTES = 4096

# Patched by tests to avoid real waiting.
_sleep = time.sleep


class Headers:
    """Case-insensitive, multi-value response headers."""

    def __init__(self, items=None):
        self._items = [(str(k), str(v)) for k, v in (items or [])]

    def get(self, name: str, default=None):
        """First value of a header, or default."""
        values = self.get_all(name)
        return values[0] if values else default

    def get_all(self, name: str) -> List[str]:
        """Every value of a header, in the order received."""
        key = name.lower()
        return [v for k, v in self._items if k.lower() == key]

    def items(self):
        return list(self._items)

    def __contains__(self, name) -> bool:
        return bool(self.get_all(name))

    def __len__(self) -> int:
        return len(self._items)

    def to_dict(self) -> Dict[str, List[str]]:
        out: Dict[str, List[str]] = {}
        for k, v in self._items:
            out.setdefault(k.lower(), []).append(v)
        return out


@dataclass
class Response:
    url: str
    final_url: str = ""
    status: Optional[int] = None
    chain: list = field(default_factory=list)
    headers: Headers = field(default_factory=Headers)
    body: bytes = b""
    text: str = ""
    encoding: Optional[str] = None
    encoding_source: Optional[str] = None  # header | meta | bom | fallback
    elapsed_ms: int = 0
    transfer_bytes: int = 0
    truncated: bool = False
    error: Optional[str] = None
    warnings: list = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.error is None and self.status is not None and 200 <= self.status < 300

    @property
    def content_type(self) -> str:
        return self.headers.get("Content-Type", "") or ""

    def to_dict(self, include_text: bool = False) -> dict:
        out = {
            "url": self.url, "final_url": self.final_url, "status": self.status, "chain": self.chain,
            "content_type": self.content_type, "bytes": len(self.body),
            "transfer_bytes": self.transfer_bytes, "encoding": self.encoding,
            "encoding_source": self.encoding_source, "elapsed_ms": self.elapsed_ms,
            "truncated": self.truncated, "error": self.error, "warnings": self.warnings,
        }
        if include_text:
            out["text"] = self.text
        return out


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def accept_language(lang: str) -> str:
    lang = lang.strip()
    primary = re.split(r"[-_]", lang)[0]
    if primary and primary.lower() != lang.lower():
        return f"{lang},{primary};q=0.9"
    return lang


def _error_text(exc: BaseException) -> str:
    reason = getattr(exc, "reason", None)
    if reason is not None and not isinstance(exc, urllib.error.HTTPError):
        return f"{type(exc).__name__}: {reason}"
    return f"{type(exc).__name__}: {exc}"


def _request_once(url: str, headers: dict, timeout: float, max_bytes: int):
    """One GET without following redirects. Returns (status, Headers, raw, truncated, error)."""
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        resp = _opener.open(req, timeout=timeout)
    except urllib.error.HTTPError as exc:  # 4xx/5xx and unfollowed 3xx
        resp = exc
    except Exception as exc:  # noqa: BLE001 - DNS, TLS, refused, timeout...
        return None, Headers(), b"", False, _error_text(exc)
    status = getattr(resp, "status", None) or getattr(resp, "code", None)
    hdrs = Headers(resp.headers.items() if getattr(resp, "headers", None) is not None else [])
    raw, truncated, error = b"", False, None
    try:
        raw = resp.read(max_bytes + 1)
    except http.client.IncompleteRead as exc:
        raw = exc.partial
    except Exception as exc:  # noqa: BLE001
        error = f"read failed: {_error_text(exc)}"
    finally:
        try:
            resp.close()
        except Exception:  # noqa: BLE001
            pass
    if len(raw) > max_bytes:
        raw, truncated = raw[:max_bytes], True
    return status, hdrs, raw, truncated, error


def _retry_wait(value: Optional[str], attempt: int) -> float:
    if value:
        value = value.strip()
        if value.isdigit():
            return min(float(value), MAX_RETRY_WAIT)
        try:
            when = email.utils.parsedate_to_datetime(value)
            return max(0.0, min(when.timestamp() - time.time(), MAX_RETRY_WAIT))
        except (TypeError, ValueError, IndexError, OverflowError):
            pass
    return float(2 ** attempt)


def _inflate(data: bytes, wbits: int, limit: int) -> bytes:
    return zlib.decompressobj(wbits).decompress(data, limit + 1)


def decode_content(raw: bytes, content_encoding: str, max_bytes: int):
    """Undo gzip/deflate. Returns (body, truncated, warnings)."""
    warnings: list = []
    truncated = False
    codings = [c.strip().lower() for c in (content_encoding or "").split(",") if c.strip()]
    body = raw
    for coding in reversed(codings):
        if coding == "identity":
            continue
        try:
            if coding in ("gzip", "x-gzip"):
                body = _inflate(body, 16 + zlib.MAX_WBITS, max_bytes)
            elif coding == "deflate":
                try:  # RFC 9110: zlib wrapper; many servers send raw deflate instead
                    body = _inflate(body, zlib.MAX_WBITS, max_bytes)
                except zlib.error:
                    body = _inflate(body, -zlib.MAX_WBITS, max_bytes)
            else:
                warnings.append(f"unsupported Content-Encoding {coding!r}; body left as received")
                break
        except zlib.error as exc:
            warnings.append(f"could not decode Content-Encoding {coding!r}: {exc}")
            break
        if len(body) > max_bytes:
            body, truncated = body[:max_bytes], True
    return body, truncated, warnings


def _codec(name: Optional[str]) -> Optional[str]:
    if not name:
        return None
    try:
        return codecs.lookup(name.strip().strip("'\"")).name
    except (LookupError, ValueError):
        return None


_CT_CHARSET = re.compile(r"""charset\s*=\s*["']?([^"';,\s]+)""", re.I)
_META_CHARSET = re.compile(rb"""<meta[^>]+?charset\s*=\s*["']?\s*([A-Za-z0-9_\-:.]+)""", re.I)


def decode_text(body: bytes, content_type: str = ""):
    """Decode a body: header charset -> <meta> -> BOM -> utf-8 -> latin-1.

    Returns (text, encoding, source, warnings). Never raises on unknown charsets.
    """
    warnings: list = []
    m = _CT_CHARSET.search(content_type or "")
    if m:
        enc = _codec(m.group(1))
        if enc:
            return body.decode(enc, "replace").lstrip("﻿"), enc, "header", warnings
        warnings.append(f"unknown charset {m.group(1)!r} in Content-Type; ignored")
    m = _META_CHARSET.search(body[:META_SCAN_BYTES])
    if m:
        declared = m.group(1).decode("ascii", "replace")
        enc = _codec(declared)
        if enc:
            return body.decode(enc, "replace").lstrip("﻿"), enc, "meta", warnings
        warnings.append(f"unknown charset {declared!r} in <meta>; ignored")
    for bom, enc in ((codecs.BOM_UTF8, "utf-8"), (codecs.BOM_UTF16_LE, "utf-16-le"),
                     (codecs.BOM_UTF16_BE, "utf-16-be")):
        if body.startswith(bom):
            return body[len(bom):].decode(enc, "replace"), enc, "bom", warnings
    try:
        return body.decode("utf-8"), "utf-8", "fallback", warnings
    except UnicodeDecodeError:
        warnings.append("no charset declared and the body is not valid UTF-8; decoded as latin-1")
        return body.decode("latin-1"), "latin-1", "fallback", warnings


def fetch(url: str, *, ua: str = "browser", lang: Optional[str] = None, timeout: float = 20,
          max_bytes: int = 8_000_000, retries: int = 2, follow_redirects: bool = True,
          accept: Optional[str] = None) -> Response:
    """GET a URL following redirects by hand so that each hop is recorded.

    ua: a short name from bots.USER_AGENTS or a full UA string.
    lang: when given, sent as Accept-Language (crawlers such as Googlebot send none).
    Network problems never raise: they are reported in Response.error.
    """
    started = time.monotonic()
    resp = Response(url=url)
    try:
        current = urls.normalize_url(url)
    except urls.InvalidURL as exc:
        resp.error = f"invalid URL: {exc}"
        return resp
    headers = {
        "User-Agent": user_agent(ua),
        "Accept": accept or DEFAULT_ACCEPT,
        "Accept-Encoding": "gzip, deflate",
    }
    if lang:
        headers["Accept-Language"] = accept_language(lang)

    finished = False
    for _hop in range(MAX_REDIRECTS + 1):
        for attempt in range(retries + 1):
            status, hdrs, raw, truncated, error = _request_once(current, headers, timeout, max_bytes)
            if status in RETRY_CODES and attempt < retries:
                _sleep(_retry_wait(hdrs.get("Retry-After"), attempt))
                continue
            break
        resp.final_url = current
        if status is None:
            resp.error = error or "no response"
            finished = True
            break
        location = hdrs.get("Location")
        hop = {"url": current, "status": status, "location": None}
        if status in REDIRECT_CODES and location:
            try:
                target = urls.normalize_url(
                    urllib.parse.urljoin(current, urls.fix_header_text(location)))
            except urls.InvalidURL as exc:
                hop["location"] = location
                resp.chain.append(hop)
                resp.status, resp.headers = status, hdrs
                resp.error = f"invalid redirect target: {exc}"
                finished = True
                break
            hop["location"] = target
            resp.chain.append(hop)
            if follow_redirects:
                current = target
                continue
        else:
            resp.chain.append(hop)
        resp.status, resp.headers, resp.transfer_bytes = status, hdrs, len(raw)
        body, trunc2, warns = decode_content(raw, hdrs.get("Content-Encoding", ""), max_bytes)
        resp.body = body
        resp.truncated = truncated or trunc2
        resp.warnings.extend(warns)
        if error:
            resp.warnings.append(error)
        text, enc, source, warns = decode_text(body, resp.content_type)
        resp.text, resp.encoding, resp.encoding_source = text, enc, source
        resp.warnings.extend(warns)
        finished = True
        break
    if not finished:
        resp.error = f"too many redirects (more than {MAX_REDIRECTS})"
    resp.elapsed_ms = int((time.monotonic() - started) * 1000)
    return resp


class Throttle:
    """Callable wrapper around fetch() keeping requests at least `delay` seconds apart."""

    def __init__(self, delay: float = 1.0, **defaults):
        self.delay = max(0.0, float(delay or 0))
        self.defaults = defaults
        self._last = None
        self.count = 0

    def __call__(self, url: str, **kwargs) -> Response:
        if self._last is not None and self.delay:
            wait = self.delay - (time.monotonic() - self._last)
            if wait > 0:
                _sleep(wait)
        opts = dict(self.defaults)
        opts.update(kwargs)
        try:
            return fetch(url, **opts)
        finally:
            self._last = time.monotonic()
            self.count += 1
