"""DNS lookups without third-party packages.

Addresses come from ``socket``. NS and TXT records need an external resolver tool:
``dig`` or ``nslookup`` is used when present; otherwise the result says
{"available": False, "reason": ...} instead of failing.
"""
from __future__ import annotations

import ipaddress
import re
import shutil
import socket
import subprocess

from . import urls

# Second-level public suffixes under which the registrable domain has three labels.
TWO_LEVEL_SUFFIXES = {
    "co.uk", "org.uk", "ac.uk", "gov.uk", "ltd.uk", "plc.uk", "me.uk", "net.uk", "sch.uk",
    "com.au", "net.au", "org.au", "edu.au", "gov.au", "co.nz", "org.nz", "net.nz",
    "co.jp", "ne.jp", "or.jp", "ac.jp", "co.za", "org.za", "com.br", "net.br", "org.br",
    "com.mx", "com.ar", "com.tr", "co.in", "net.in", "org.in", "co.kr", "or.kr",
    "com.cn", "net.cn", "org.cn", "com.sg", "com.hk", "co.il", "com.tw", "co.id",
    "com.my", "com.ph", "com.pl", "co.at", "or.at", "com.es", "com.pt", "co.th",
}
TIMEOUT = 15
_DOMAIN_RE = re.compile(r"^[a-z0-9](?:[a-z0-9.\-]*[a-z0-9])?$")


def _is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host.strip("[]"))
        return True
    except ValueError:
        return False


def registrable_domain(host: str) -> str:
    """Strip subdomains: last two labels, or three under a co.uk-style suffix."""
    host = (host or "").strip().lower().rstrip(".")
    if host.startswith("[") or _is_ip(host):
        return host
    host = host.split(":")[0]
    try:
        host = urls.idna_host(host)
    except urls.InvalidURL:
        return host
    labels = host.split(".")
    if len(labels) <= 2:
        return host
    if ".".join(labels[-2:]) in TWO_LEVEL_SUFFIXES:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])


def _tool():
    for name in ("dig", "nslookup"):
        path = shutil.which(name)
        if path:
            return name, path
    return None, None


def _unavailable(host: str):
    domain = registrable_domain(host)
    if _is_ip(domain) or domain in ("localhost", "") or "." not in domain:
        return domain, {"available": False, "domain": domain, "reason": "not a public domain name"}
    if not _DOMAIN_RE.match(domain):
        return domain, {"available": False, "domain": domain, "reason": "invalid domain name"}
    name, _path = _tool()
    if not name:
        return domain, {"available": False, "domain": domain,
                        "reason": "neither dig nor nslookup is installed"}
    return domain, None


def _run(args) -> str:
    res = subprocess.run(args, capture_output=True, text=True, timeout=TIMEOUT,
                         encoding="utf-8", errors="replace")
    return res.stdout or ""


def _query(host: str, rtype: str):
    domain, problem = _unavailable(host)
    if problem:
        return domain, None, problem
    name, path = _tool()
    try:
        if name == "dig":
            out = _run([path, "+short", rtype, domain])
        else:
            out = _run([path, f"-type={rtype}", domain])
    except (OSError, subprocess.SubprocessError) as exc:
        return domain, None, {"available": True, "domain": domain, "tool": name,
                              "error": f"{type(exc).__name__}: {exc}"}
    return domain, (name, out), None


def nameservers(host: str) -> dict:
    """NS records of the registrable domain of `host`."""
    domain, result, problem = _query(host, "NS")
    if problem:
        problem.setdefault("nameservers", [])
        return problem
    name, out = result
    if name == "dig":
        found = [line.strip().rstrip(".") for line in out.splitlines()
                 if line.strip() and not line.startswith(";")]
    else:
        found = [n.rstrip(".") for n in re.findall(r"nameserver\s*=\s*(\S+)", out, re.I)]
    return {"available": True, "domain": domain, "tool": name,
            "nameservers": sorted({n.lower() for n in found})}


def txt(host: str) -> dict:
    """TXT records of the registrable domain of `host`."""
    domain, result, problem = _query(host, "TXT")
    if problem:
        problem.setdefault("records", [])
        return problem
    name, out = result
    records = []
    for line in out.splitlines():
        parts = re.findall(r'"((?:[^"\\]|\\.)*)"', line)
        if parts:
            records.append("".join(parts))
    return {"available": True, "domain": domain, "tool": name, "records": records}


def addresses(host: str) -> dict:
    """A/AAAA addresses through the system resolver (socket)."""
    host = (host or "").split(":")[0] if not host.startswith("[") else host.strip("[]")
    try:
        infos = socket.getaddrinfo(urls.idna_host(host), None)
    except (OSError, UnicodeError, urls.InvalidURL) as exc:
        return {"available": True, "addresses": [], "error": f"{type(exc).__name__}: {exc}"}
    return {"available": True, "addresses": sorted({i[4][0] for i in infos})}


def summary(host: str) -> dict:
    """DNS facts useful for an audit: provider (e.g. Cloudflare) and verification records."""
    ns = nameservers(host)
    records = txt(host)
    out = {"domain": registrable_domain(host), "nameservers": ns, "txt": records}
    if ns.get("available") and not ns.get("error"):
        out["cloudflare_dns"] = any("cloudflare" in n for n in ns.get("nameservers", []))
    else:
        out["cloudflare_dns"] = None
    if records.get("available") and not records.get("error"):
        recs = records.get("records", [])
        out["txt_verifications"] = sorted({r.split("=")[0] for r in recs if "verification" in r.lower()})
        out["google_domain_property_likely"] = any(r.startswith("google-site-verification") for r in recs)
    else:
        out["txt_verifications"] = None
        out["google_domain_property_likely"] = None
    return out
