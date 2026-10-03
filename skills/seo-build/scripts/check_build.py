#!/usr/bin/env python3
"""Controllo SEO dei file HTML generati dalla build (prerender/SSG/sito statico), prima del deploy.

Legge ogni .html nella cartella di output e segnala: title/description mancanti o duplicati,
canonical assente o multiplo, H1 mancante o multiplo, noindex, lang assente, JSON-LD non valido,
salti di intestazione, possibili errori di accento, documenti collegati, pagine quasi vuote.
Riusa il parser di seo-audit/scripts/seo_fetch.py.

Uso:
  python check_build.py dist/browser                 # report leggibile
  python check_build.py dist --base https://dominio.it --json build-check.json
"""
import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

_FETCH = Path(__file__).resolve().parents[2] / "seo-audit" / "scripts" / "seo_fetch.py"
_spec = importlib.util.spec_from_file_location("seo_fetch", _FETCH)
seo_fetch = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(seo_fetch)

SKIP_DIRS = {"node_modules", ".git", "assets", "media"}
# File di servizio dei framework: non sono pagine indicizzabili (es. guscio CSR di Angular).
SHELL_FILES = {"index.csr.html", "200.html", "_fallback.html", "fallback.html"}


def page_url(base, root, path):
    rel = path.relative_to(root).as_posix()
    if rel.endswith("index.html"):
        rel = rel[: -len("index.html")]
    return base.rstrip("/") + "/" + rel


def analyze(path, url):
    text = path.read_text(encoding="utf-8", errors="replace")
    p = seo_fetch.PageParser(url)
    p.feed(text)
    d = p.d
    page = {"url": url, "file": str(path), "lang": d["lang"], "title": d["title"],
            "meta_description": d["meta"].get("description", []), "canonical": d["canonical"],
            "robots_meta": d["robots"], "h1": d["h1"], "outline": d["outline"],
            "jsonld": d["jsonld"], "documents": sorted(d["documents"]),
            "visible_text": " ".join(d["text"]), "bytes": len(text.encode("utf-8"))}
    issues = []
    noindex = any("noindex" in r.lower() for r in page["robots_meta"])
    page["noindex"] = noindex
    if path.name in SHELL_FILES:
        page["shell"] = True
        page["issues"] = [{"gravita": "info", "problema": "file di fallback del framework (guscio CSR): "
                           "non deve essere servito per URL indicizzabili"}]
        page.pop("visible_text")
        return page
    if noindex:
        issues.append(("info", "pagina in noindex (verifica che sia voluto, es. 404 o privacy)"))
        page["issues"] = [{"gravita": g, "problema": m} for g, m in issues]
        page.pop("visible_text")
        return page
    if not page["title"] or not page["title"][0].strip():
        issues.append(("alta", "title mancante o vuoto"))
    if not page["meta_description"]:
        issues.append(("media", "meta description mancante"))
    if len(page["canonical"]) != 1:
        issues.append(("alta", f"canonical: {len(page['canonical'])} trovati (serve esattamente 1)"))
    if len(page["h1"]) != 1:
        issues.append(("media", f"H1: {len(page['h1'])} trovati"))
    if not page["lang"]:
        issues.append(("bassa", "attributo lang mancante su <html>"))
    for j in page["jsonld"]:
        if not j.get("ok"):
            issues.append(("alta", f"JSON-LD non valido: {j.get('error')}"))
    for s in seo_fetch._heading_skips(page["outline"]):
        issues.append(("bassa", f"salto di intestazione {s}"))
    for t in seo_fetch.typo_suspects(page):
        issues.append(("media", f"possibile errore in {t['field']}: '{t['match']}' ({t['why']}) - {t['context']}"))
    if len(" ".join(page["visible_text"].split())) < 300:
        issues.append(("alta", "pochissimo testo nell'HTML: pagina non prerenderizzata o guscio vuoto?"))
    if page["bytes"] > seo_fetch.GOOGLE_HTML_LIMIT:
        issues.append(("critica", "HTML oltre 2 MB: Googlebot legge solo i primi 2 MB"))
    page["issues"] = [{"gravita": g, "problema": m} for g, m in issues]
    page.pop("visible_text")
    return page


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dir", help="cartella di output della build")
    ap.add_argument("--base", default="https://example.com", help="URL di produzione, per risolvere i link")
    ap.add_argument("--json", help="scrive il risultato completo in questo file")
    args = ap.parse_args()

    root = Path(args.dir).resolve()
    # Angular: dist/<progetto>/browser contiene le pagine prerenderizzate
    browser = [b for b in root.rglob("browser") if (b / "index.html").exists()]
    if browser and not (root / "index.html").exists():
        root = browser[0]
    files = [p for p in root.rglob("*.html") if not (SKIP_DIRS & set(p.relative_to(root).parts))]
    pages = [analyze(p, page_url(args.base, root, p)) for p in sorted(files)]

    dup = {}
    for key in ("title", "meta_description"):
        seen = {}
        for p in pages:
            if p.get("noindex") or p.get("shell"):
                continue
            for v in p[key]:
                seen.setdefault(v, []).append(p["url"])
        dup[key] = {k: v for k, v in seen.items() if len(v) > 1}

    report = {"dir": str(root), "pages": pages, "duplicates": dup}
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"{len(pages)} pagine HTML in {root}")
    for p in pages:
        if p["issues"]:
            print(f"\n{p['url']}  ({os.path.relpath(p['file'], root)})")
            for i in p["issues"]:
                print(f"  [{i['gravita']}] {i['problema']}")
    for key, items in dup.items():
        for v, urls in items.items():
            print(f"\n[media] {key} duplicato su {len(urls)} pagine: \"{v[:80]}\"")
    if not any(p["issues"] for p in pages) and not any(dup.values()):
        print("Nessun problema trovato.")


if __name__ == "__main__":
    main()
