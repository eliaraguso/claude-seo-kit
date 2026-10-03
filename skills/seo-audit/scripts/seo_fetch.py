#!/usr/bin/env python3
"""Raccolta dati SEO da un sito online, senza dipendenze esterne.

Legge l'HTML grezzo restituito dal server (cio' che vede un bot che non esegue
JavaScript) e i file di sito (robots.txt, sitemap). Non esegue JavaScript: per il
DOM renderizzato serve un browser (Chrome DevTools) o il Controllo URL di Search Console.

Uso:
  python seo_fetch.py https://example.com                 # home + controlli di sito
  python seo_fetch.py https://example.com --sitemap 30    # anche fino a 30 URL dalla sitemap
  python seo_fetch.py https://example.com/a https://example.com/b --no-site
  python seo_fetch.py https://example.com --json out.json

Lo user agent dei bot e' simulato: un WAF che verifica l'IP puo' trattare i bot veri
in modo diverso. Il confronto tra user agent e' quindi un indizio, non una prova.
"""
import argparse
import gzip
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET
import zlib
from html.parser import HTMLParser

UA = {
    "browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36",
    "googlebot": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "bingbot": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "oai-searchbot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot",
    "perplexitybot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
    "claude-searchbot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-SearchBot/1.0; +https://www.anthropic.com)",
}
BOT_TOKENS = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot",
              "Claude-SearchBot", "PerplexityBot", "Google-Extended", "CCBot", "*"]
GOOGLE_HTML_LIMIT = 2 * 1024 * 1024  # Googlebot legge i primi 2 MB non compressi
TIMEOUT = 20


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


_opener = urllib.request.build_opener(NoRedirect)


def http_get(url, ua="browser", max_hops=10):
    """GET seguendo i redirect a mano per registrare la catena."""
    chain = []
    current = url
    for _ in range(max_hops):
        req = urllib.request.Request(current, headers={
            "User-Agent": UA.get(ua, ua), "Accept": "text/html,application/xhtml+xml,*/*",
            "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en;q=0.5"})
        try:
            resp = _opener.open(req, timeout=TIMEOUT)
            status, headers, raw = resp.status, resp.headers, resp.read()
        except urllib.error.HTTPError as e:
            status, headers, raw = e.code, e.headers, e.read() if e.fp else b""
        except Exception as e:  # noqa: BLE001 - errore di rete/DNS/TLS da riportare
            return {"url": url, "error": f"{type(e).__name__}: {e}", "chain": chain}
        chain.append({"url": current, "status": status})
        if status in (301, 302, 303, 307, 308) and headers.get("Location"):
            current = urllib.parse.urljoin(current, headers["Location"])
            continue
        enc = (headers.get("Content-Encoding") or "").lower()
        try:
            if "gzip" in enc:
                raw = gzip.decompress(raw)
            elif "deflate" in enc:
                raw = zlib.decompress(raw)
        except Exception:  # noqa: BLE001
            pass
        ctype = headers.get("Content-Type") or ""
        m = re.search(r"charset=([\w-]+)", ctype)
        text = raw.decode(m.group(1) if m else "utf-8", "replace")
        return {"url": url, "final_url": current, "status": status, "chain": chain,
                "content_type": ctype, "bytes": len(raw), "x_robots_tag": headers.get("X-Robots-Tag"),
                "link_header": headers.get("Link"), "server": headers.get("Server"),
                "cf_ray": bool(headers.get("CF-Ray")), "text": text}
    return {"url": url, "error": "troppi redirect", "chain": chain}


class PageParser(HTMLParser):
    VOID_SKIP = {"script", "style", "noscript", "template", "svg"}

    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.d = {"title": [], "meta": {}, "canonical": [], "hreflang": [], "robots": [],
                  "h1": [], "headings": {}, "jsonld": [], "links_internal": set(), "links_external": 0,
                  "a_without_href": 0, "img": 0, "img_no_alt": 0, "lang": None, "icons": [],
                  "head_invalid_tags": [], "text_chars": 0, "outline": [], "documents": set(),
                  "text": []}
        self._stack_skip = 0
        self._in = None
        self._buf = []
        self._in_head = False
        self._script_ld = False

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "html":
            self.d["lang"] = a.get("lang")
        if tag == "head":
            self._in_head = True
        if tag == "body":
            self._in_head = False
        if self._in_head and tag in ("img", "iframe", "div", "p", "span"):
            self.d["head_invalid_tags"].append(tag)  # Google smette di leggere i meta dopo questi
        if tag == "meta":
            name = (a.get("name") or a.get("property") or "").lower()
            if name:
                self.d["meta"].setdefault(name, []).append(a.get("content", ""))
            if name in ("robots", "googlebot"):
                self.d["robots"].append(f"{name}: {a.get('content', '')}")
        elif tag == "link":
            rel = a.get("rel", "").lower().split()
            href = a.get("href", "")
            if "canonical" in rel:
                self.d["canonical"].append(href)
            if "alternate" in rel and a.get("hreflang"):
                self.d["hreflang"].append(f"{a['hreflang']} -> {href}")
            if "icon" in rel:
                self.d["icons"].append(f"{' '.join(rel)} {a.get('sizes', '')} {href}".strip())
        elif tag == "a":
            href = a.get("href")
            if not href:
                self.d["a_without_href"] += 1
            elif not href.startswith(("#", "mailto:", "tel:", "javascript:")):
                full = urllib.parse.urljoin(self.base, href)
                if re.search(r"\.(pdf|docx?|pptx?|xlsx?|odt)(\?|$)", full, re.I):
                    self.d["documents"].add(full)
                if urllib.parse.urlparse(full).netloc == urllib.parse.urlparse(self.base).netloc:
                    self.d["links_internal"].add(full.split("#")[0])
                else:
                    self.d["links_external"] += 1
        elif tag == "img":
            self.d["img"] += 1
            if "alt" not in a:
                self.d["img_no_alt"] += 1
        if tag == "script" and "ld+json" in a.get("type", ""):
            self._script_ld = True
            self._buf = []
        elif tag in self.VOID_SKIP:
            self._stack_skip += 1
        if tag in ("title", "h1", "h2", "h3", "h4", "h5", "h6"):
            self._in = tag
            self._buf = []
            if tag.startswith("h"):
                self.d["headings"][tag] = self.d["headings"].get(tag, 0) + 1

    def handle_endtag(self, tag):
        if tag == "script" and self._script_ld:
            self._script_ld = False
            raw = "".join(self._buf).strip()
            try:
                data = json.loads(raw)
                self.d["jsonld"].append({"ok": True, "types": _ld_types(data)})
            except Exception as e:  # noqa: BLE001
                self.d["jsonld"].append({"ok": False, "error": str(e)[:120]})
            return
        if tag in self.VOID_SKIP:
            self._stack_skip = max(0, self._stack_skip - 1)
        if tag == self._in:
            text = " ".join("".join(self._buf).split())
            if tag == "title":
                self.d["title"].append(text)
            else:
                self.d["outline"].append(f"{tag}: {text[:100]}")
                if tag == "h1":
                    self.d["h1"].append(text)
            self._in = None
        if tag == "head":
            self._in_head = False

    def handle_data(self, data):
        if self._script_ld or self._in:
            self._buf.append(data)
        if not self._stack_skip and not self._in_head and not self._script_ld:
            chunk = " ".join(data.split())
            self.d["text_chars"] += len(chunk)
            if chunk:
                self.d["text"].append(chunk)


def _ld_types(node):
    out = []
    if isinstance(node, list):
        for n in node:
            out += _ld_types(n)
    elif isinstance(node, dict):
        t = node.get("@type")
        if t:
            out += t if isinstance(t, list) else [t]
        for k in ("@graph", "mainEntity", "author", "publisher", "itemListElement"):
            if k in node:
                out += _ld_types(node[k])
    return out


def analyze_page(url, ua="browser"):
    r = http_get(url, ua)
    if "error" in r:
        return r
    p = PageParser(r["final_url"])
    try:
        p.feed(r["text"])
    except Exception as e:  # noqa: BLE001
        r["parse_error"] = str(e)
    d = p.d
    meta = d["meta"]
    out = {k: v for k, v in r.items() if k != "text"}
    out.update({
        "over_2mb": r["bytes"] > GOOGLE_HTML_LIMIT,
        "lang": d["lang"],
        "title": d["title"], "title_len": [len(t) for t in d["title"]],
        "meta_description": meta.get("description", []),
        "robots_meta": d["robots"],
        "canonical": d["canonical"],
        "hreflang": d["hreflang"],
        "h1": d["h1"], "headings": d["headings"], "outline": d["outline"],
        "heading_skips": _heading_skips(d["outline"]),
        "documents": sorted(d["documents"]),
        "og": {k: v for k, v in meta.items() if k.startswith("og:")},
        "twitter_card": meta.get("twitter:card"),
        "jsonld": d["jsonld"],
        "icons": d["icons"],
        "links_internal": len(d["links_internal"]), "links_external": d["links_external"],
        "a_without_href": d["a_without_href"],
        "img": d["img"], "img_no_alt": d["img_no_alt"],
        "visible_text_chars": d["text_chars"],
        "head_invalid_tags": sorted(set(d["head_invalid_tags"])),
        "spa_shell_suspect": d["text_chars"] < 300 and bool(re.search(
            r"<(app-root|div id=\"(root|app|__next|__nuxt)\")[^>]*>\s*</", r["text"])),
        "internal_links": sorted(d["links_internal"]),
        "visible_text": " ".join(d["text"]),
    })
    return out


# Errori di accento frequenti in italiano (euristica: da confermare leggendo il contesto).
IT_TYPO_PATTERNS = [
    (re.compile(r"(?<![\w'])é(?![\w'])"), "'é' isolato: il verbo essere si scrive 'è'"),
    (re.compile(r"\b(cos|com|dov|quand)'é\b", re.I), "'é' dopo apostrofo: si scrive 'è' (es. cos'è)"),
    (re.compile(r"\b(perchè|poichè|affinchè|finchè|benchè|sicchè|nè|sè|ventitrè|trentatrè)\b", re.I),
     "accento grave dove va l'acuto (perché, né, sé, ...)"),
    (re.compile(r"\bpò\b", re.I), "'pò' si scrive 'po''"),
    (re.compile(r"\bqual'è\b", re.I), "'qual'è' si scrive 'qual è'"),
    (re.compile(r"\bE'\s"), "\"E'\" con apostrofo al posto di 'È'"),
]


def typo_suspects(page):
    """Cerca errori di accento frequenti in title, description, intestazioni e testo (solo pagine in italiano)."""
    if not (page.get("lang") or "it").lower().startswith("it"):
        return []
    fields = {"title": page.get("title") or [], "description": page.get("meta_description") or [],
              "headings": page.get("outline") or [], "text": [page.get("visible_text") or ""]}
    found = []
    for field, values in fields.items():
        for v in values:
            for pat, why in IT_TYPO_PATTERNS:
                for m in pat.finditer(v):
                    ctx = " ".join(v[max(0, m.start() - 40):m.end() + 40].split())
                    found.append({"field": field, "match": m.group(0), "why": why, "context": ctx})
    return found


def _heading_skips(outline):
    """Salti di livello (es. h1 -> h3): non incidono sul ranking, ma su chiarezza e accessibilita'."""
    skips, prev = [], 0
    for item in outline:
        lvl = int(item[1])
        if prev and lvl > prev + 1:
            skips.append(f"h{prev} -> {item}")
        prev = lvl
    return skips


def _norm(s):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def term_coverage(pages, terms):
    """Per ogni termine, le pagine il cui testo visibile, title, description o H1 lo contengono."""
    out = {}
    for t in terms:
        nt = _norm(t)
        hits = []
        for p in pages:
            blob = " ".join([p.get("visible_text") or "", *(p.get("title") or []),
                             *(p.get("meta_description") or []), *(p.get("h1") or [])])
            if nt in _norm(blob):
                hits.append(p.get("final_url") or p.get("url"))
        out[t] = hits
    return out


def nameservers(host):
    """Nameserver e record TXT del dominio.

    Cloudflare in modalita' solo DNS non appare negli header HTTP; un record TXT
    google-site-verification indica una proprieta' Search Console di tipo Dominio.
    """
    import subprocess
    domain = host[4:] if host.startswith("www.") else host
    out = {"domain": domain}
    try:
        res = subprocess.run(["nslookup", "-type=NS", domain], capture_output=True, text=True, timeout=15)
        ns = sorted(set(re.findall(r"nameserver\s*=\s*(\S+)", res.stdout, re.I)))
        out.update({"ns": ns, "cloudflare_dns": any("cloudflare" in n.lower() for n in ns)})
        res = subprocess.run(["nslookup", "-type=TXT", domain], capture_output=True, text=True, timeout=15)
        txt = re.findall(r'"([^"]*)"', res.stdout)
        out["txt_verifications"] = sorted({t.split("=")[0] for t in txt if "verification" in t.lower()})
        out["google_domain_property_likely"] = any(t.startswith("google-site-verification") for t in txt)
    except Exception as e:  # noqa: BLE001
        out["error"] = f"{type(e).__name__}: {e}"
    return out


def parse_robots(text):
    groups, cur, sitemaps = {}, [], []
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        k, v = (x.strip() for x in line.split(":", 1))
        k = k.lower()
        if k == "user-agent":
            if cur and cur[-1][1]:
                cur = []
            cur.append([v, []])
            groups.setdefault(v.lower(), [])
        elif k in ("allow", "disallow") and cur:
            for g in cur:
                g[1].append(f"{k}: {v}")
                groups[g[0].lower()].append(f"{k}: {v}")
        elif k == "sitemap":
            sitemaps.append(v)
    return groups, sitemaps


def site_checks(origin):
    res = {}
    rb = http_get(origin + "/robots.txt")
    res["robots_txt"] = {k: rb.get(k) for k in ("status", "content_type", "bytes", "error")}
    res["dns"] = nameservers(urllib.parse.urlparse(origin).netloc)
    sitemaps = []
    if rb.get("status") == 200:
        if "<html" in rb["text"][:500].lower():
            res["robots_txt"]["warning"] = "robots.txt restituisce HTML (fallback SPA?)"
        groups, sitemaps = parse_robots(rb["text"])
        res["robots_txt"]["sitemaps"] = sitemaps
        res["robots_txt"]["groups"] = {ua: rules for ua, rules in groups.items()
                                      if ua in [t.lower() for t in BOT_TOKENS] or ua == "*"}
        res["robots_txt"]["all_user_agents"] = sorted(groups)
        res["robots_txt"]["bytes_over_500KiB"] = rb["bytes"] > 500 * 1024
    # Varianti http/www: devono arrivare all'URL canonico con un solo redirect.
    u = urllib.parse.urlparse(origin)
    host = u.netloc
    alt_host = host[4:] if host.startswith("www.") else "www." + host
    res["variants"] = {}
    for v in {f"http://{host}/", f"http://{alt_host}/", f"https://{alt_host}/"}:
        r = http_get(v)
        res["variants"][v] = {"chain": r.get("chain"), "final": r.get("final_url"), "error": r.get("error")}
    # Un URL inesistente deve rispondere 404/410 (non 200 = soft 404).
    probe = f"{origin}/seo-check-{uuid.uuid4().hex[:8]}"
    r404 = http_get(probe)
    res["not_found_probe"] = {"url": probe, "status": r404.get("status"), "final": r404.get("final_url")}
    # Sitemap
    sm_urls, sm_info = [], []
    for sm in (sitemaps or [origin + "/sitemap.xml"])[:5]:
        r = http_get(sm)
        info = {"url": sm, "status": r.get("status"), "error": r.get("error")}
        if r.get("status") == 200:
            try:
                root = ET.fromstring(r["text"].encode("utf-8"))
                ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = [e.text.strip() for e in root.findall(".//s:loc", ns) if e.text]
                info.update({"type": root.tag.split("}")[-1], "loc_count": len(locs),
                             "with_lastmod": len(root.findall(".//s:lastmod", ns))})
                if root.tag.endswith("sitemapindex"):
                    for child in locs[:5]:
                        rc = http_get(child)
                        if rc.get("status") == 200:
                            croot = ET.fromstring(rc["text"].encode("utf-8"))
                            sm_urls += [e.text.strip() for e in croot.findall(".//s:loc", ns) if e.text]
                else:
                    sm_urls += locs
            except ET.ParseError as e:
                info["parse_error"] = str(e)
        sm_info.append(info)
    res["sitemaps"] = sm_info
    res["sitemap_urls"] = sm_urls
    return res


def ua_comparison(url):
    """Stessa pagina con user agent diversi: differenze di stato o dimensione = possibile blocco WAF/CDN."""
    out = {}
    for name in UA:
        r = http_get(url, name)
        out[name] = {"status": r.get("status"), "bytes": r.get("bytes"), "final": r.get("final_url"),
                     "error": r.get("error"),
                     "challenge_suspect": bool(r.get("text") and re.search(
                         r"(cf-challenge|captcha|are you a robot|verify you are human|just a moment)",
                         r["text"][:20000], re.I))}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--sitemap", type=int, default=0, help="analizza fino a N URL presi dalla sitemap")
    ap.add_argument("--no-site", action="store_true", help="salta robots/sitemap/varianti/404")
    ap.add_argument("--no-ua", action="store_true", help="salta il confronto tra user agent")
    ap.add_argument("--terms", help="termini separati da ';' da cercare nei testi (copertura del vocabolario)")
    ap.add_argument("--full-text", action="store_true", help="include il testo visibile completo nel JSON")
    ap.add_argument("--json", help="scrive il risultato completo in questo file")
    args = ap.parse_args()

    first = urllib.parse.urlparse(args.urls[0])
    origin = f"{first.scheme}://{first.netloc}"
    report = {"origin": origin}
    if not args.no_site:
        report["site"] = site_checks(origin)
    targets = list(dict.fromkeys(args.urls))
    if args.sitemap and report.get("site"):
        for u in report["site"]["sitemap_urls"]:
            if len(targets) >= args.sitemap + len(args.urls):
                break
            if u not in targets:
                targets.append(u)
    report["pages"] = [analyze_page(u) for u in targets]
    if not args.no_ua:
        report["ua_comparison"] = ua_comparison(args.urls[0])

    # Duplicati di title/description tra le pagine analizzate
    seen_t, seen_d = {}, {}
    for p in report["pages"]:
        for t in p.get("title") or []:
            seen_t.setdefault(t, []).append(p["url"])
        for d in p.get("meta_description") or []:
            seen_d.setdefault(d, []).append(p["url"])
    report["duplicates"] = {"title": {k: v for k, v in seen_t.items() if len(v) > 1},
                            "meta_description": {k: v for k, v in seen_d.items() if len(v) > 1}}

    for p in report["pages"]:
        if "error" not in p:
            p["typo_suspects"] = typo_suspects(p)
    if args.terms:
        report["term_coverage"] = term_coverage(report["pages"], [t.strip() for t in args.terms.split(";") if t.strip()])
    for p in report["pages"]:
        vt = p.get("visible_text") or ""
        if not args.full_text and len(vt) > 1500:
            p["visible_text"] = vt[:1500] + " [...] (usa --full-text per il testo completo)"

    text = json.dumps(report, ensure_ascii=False, indent=2, default=list)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Scritto {args.json} ({len(report['pages'])} pagine)")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
