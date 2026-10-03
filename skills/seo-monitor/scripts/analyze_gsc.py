#!/usr/bin/env python3
"""Analisi di un export del report Rendimento di Google Search Console (CSV o .zip).

Search Console -> Rendimento -> Esporta -> "Scarica CSV" produce uno .zip con un CSV per
dimensione (query, pagine, paesi, dispositivi, date...). Lo script accetta lo .zip o la
cartella estratta, in italiano o in inglese, e opzionalmente un secondo export del periodo
precedente per il confronto.

Uso:
  python analyze_gsc.py export-ottobre.zip
  python analyze_gsc.py export-ottobre.zip --previous export-settembre.zip --brand "raguso|eliaraguso"
  python analyze_gsc.py cartella-export --json gsc.json

Note: le query anonimizzate da Google non compaiono nel file Query, quindi la somma dei clic
per query è inferiore al totale (il totale affidabile è nel file Date/Grafico).
"""
import argparse
import csv
import io
import json
import re
import sys
import zipfile
from pathlib import Path

DIMENSIONS = {
    "query": ["query", "queries", "domande"],
    "pages": ["pagine", "pages", "pagina"],
    "countries": ["paesi", "countries"],
    "devices": ["dispositivi", "devices"],
    "dates": ["date", "dates", "grafico", "chart"],
    "appearance": ["aspetto", "appearance"],
}


def _num(v):
    v = (v or "").strip().replace("%", "").replace(" ", "")
    if not v:
        return 0.0
    if "," in v and "." in v:
        v = v.replace(".", "").replace(",", ".")
    elif "," in v:
        v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return 0.0


def _col(header, *keys):
    for i, h in enumerate(header):
        hl = h.strip().lower()
        if any(k in hl for k in keys):
            return i
    return None


def read_table(text):
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        return []
    h = rows[0]
    ic, ii = _col(h, "clic", "click"), _col(h, "impress")
    ir, ip = _col(h, "ctr"), _col(h, "posiz", "position")
    out = []
    for r in rows[1:]:
        if not r or not r[0].strip():
            continue
        out.append({"key": r[0].strip(),
                    "clicks": _num(r[ic]) if ic is not None else 0,
                    "impressions": _num(r[ii]) if ii is not None else 0,
                    "ctr": _num(r[ir]) if ir is not None else 0,
                    "position": _num(r[ip]) if ip is not None else 0})
    return out


def load_export(path):
    p = Path(path)
    files = {}
    if p.suffix.lower() == ".zip":
        with zipfile.ZipFile(p) as z:
            for n in z.namelist():
                if n.lower().endswith(".csv"):
                    files[Path(n).stem] = z.read(n).decode("utf-8-sig", "replace")
    elif p.is_dir():
        for f in p.glob("*.csv"):
            files[f.stem] = f.read_text(encoding="utf-8-sig", errors="replace")
    else:
        files[p.stem] = p.read_text(encoding="utf-8-sig", errors="replace")
    data = {}
    for stem, text in files.items():
        s = stem.lower()
        for dim, names in DIMENSIONS.items():
            if any(s.startswith(n) for n in names):
                data[dim] = read_table(text)
    return data


def totals(data):
    src = data.get("dates") or data.get("query") or []
    c = sum(r["clicks"] for r in src)
    i = sum(r["impressions"] for r in src)
    pos = (sum(r["position"] * r["impressions"] for r in src) / i) if i else 0
    days = [r["key"] for r in data.get("dates", [])]
    return {"clicks": c, "impressions": i, "ctr_pct": round(100 * c / i, 2) if i else 0,
            "avg_position": round(pos, 1), "from": min(days) if days else None, "to": max(days) if days else None,
            "source": "date" if data.get("dates") else "query (sottostima: query anonime escluse)"}


def brand_split(rows, brand_re):
    rx = re.compile(brand_re, re.I)
    b = [r for r in rows if rx.search(r["key"])]
    nb = [r for r in rows if not rx.search(r["key"])]
    agg = lambda rs: {"queries": len(rs), "clicks": sum(r["clicks"] for r in rs),
                      "impressions": sum(r["impressions"] for r in rs)}
    return {"brand": agg(b), "non_brand": agg(nb)}


def compare(cur, prev, top=15):
    pc = {r["key"]: r for r in prev}
    cc = {r["key"]: r for r in cur}
    new = sorted([r for k, r in cc.items() if k not in pc], key=lambda r: -r["impressions"])[:top]
    lost = sorted([r for k, r in pc.items() if k not in cc], key=lambda r: -r["impressions"])[:top]
    movers = []
    for k, r in cc.items():
        if k in pc:
            movers.append({"key": k, "d_clicks": r["clicks"] - pc[k]["clicks"],
                           "d_impressions": r["impressions"] - pc[k]["impressions"],
                           "position": r["position"], "d_position": round(r["position"] - pc[k]["position"], 1)})
    up = sorted([m for m in movers if m["d_impressions"] > 0 or m["d_clicks"] > 0],
                key=lambda m: (-m["d_clicks"], -m["d_impressions"]))[:top]
    down = sorted([m for m in movers if m["d_impressions"] < 0 or m["d_clicks"] < 0],
                  key=lambda m: (m["d_clicks"], m["d_impressions"]))[:top]
    return {"new": new, "lost": lost, "up": up, "down": down}


def _fmt(v):
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() else f"{v:g}"
    return str(v)


def check_urls(urls, timeout=15):
    """Stato HTTP attuale degli URL presenti nell'export (redirect seguiti a mano)."""
    import urllib.error
    import urllib.request

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None

    opener = urllib.request.build_opener(NoRedirect)
    out = []
    for u in urls:
        if not u.startswith("http"):
            continue
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}, method="GET")
        try:
            r = opener.open(req, timeout=timeout)
            out.append({"key": u, "status": r.status, "location": ""})
        except urllib.error.HTTPError as e:
            out.append({"key": u, "status": e.code, "location": e.headers.get("Location") or ""})
        except Exception as e:  # noqa: BLE001
            out.append({"key": u, "status": "errore", "location": f"{type(e).__name__}"})
    return out


def warnings(cur, prev):
    """Avvisi sulla confrontabilita' dei dati."""
    w = []
    t = totals(cur)
    pages_sum = sum(r["clicks"] for r in cur.get("pages", []))
    if cur.get("dates") and cur.get("pages") and abs(pages_sum - t["clicks"]) > max(2, 0.05 * t["clicks"]):
        w.append(f"La somma dei clic per pagina ({pages_sum:.0f}) è diversa dal totale per data ({t['clicks']:.0f}): "
                 "Search Console conta i clic per pagina in modo diverso e l'export include solo le prime righe.")
    if prev is not None:
        dc, dp = len(cur.get("dates", [])), len(prev.get("dates", []))
        if dc and dp and dc != dp:
            w.append(f"I due periodi hanno lunghezza diversa ({dc} giorni contro {dp}): confronta le medie giornaliere.")
    if t["clicks"] < 100:
        w.append("Volumi piccoli: con meno di un centinaio di clic le variazioni percentuali possono essere rumore.")
    return w


def md_table(rows, cols):
    if not rows:
        return "_nessun dato_\n"
    out = "| " + " | ".join(c[1] for c in cols) + " |\n|" + "---|" * len(cols) + "\n"
    for r in rows:
        out += "| " + " | ".join(_fmt(r.get(c[0], "")) for c in cols) + " |\n"
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", help=".zip o cartella dell'export Rendimento")
    ap.add_argument("--previous", help="export del periodo precedente, per il confronto")
    ap.add_argument("--brand", help="regex delle query col proprio nome/marchio (es. 'raguso|eliaraguso')")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--check-urls", action="store_true",
                    help="verifica lo stato HTTP attuale delle pagine presenti negli export (404, redirect)")
    ap.add_argument("--json", help="scrive anche il risultato in JSON")
    args = ap.parse_args()

    cur = load_export(args.export)
    res = {"current": {"totals": totals(cur)}}
    q = cur.get("query", [])
    res["current"]["top_queries"] = sorted(q, key=lambda r: (-r["clicks"], -r["impressions"]))[:args.top]
    res["current"]["top_impressions_low_ctr"] = sorted(
        [r for r in q if r["impressions"] >= 20 and r["ctr"] < 2], key=lambda r: -r["impressions"])[:args.top]
    res["current"]["top_pages"] = sorted(cur.get("pages", []), key=lambda r: (-r["clicks"], -r["impressions"]))[:args.top]
    res["current"]["devices"] = cur.get("devices", [])
    if args.brand:
        res["current"]["brand_split"] = brand_split(q, args.brand)
    if args.previous:
        prev = load_export(args.previous)
        res["previous"] = {"totals": totals(prev)}
        if args.brand:
            res["previous"]["brand_split"] = brand_split(prev.get("query", []), args.brand)
        res["compare_queries"] = compare(q, prev.get("query", []), args.top)
        res["compare_pages"] = compare(cur.get("pages", []), prev.get("pages", []), args.top)
    else:
        prev = None
    res["warnings"] = warnings(cur, prev)
    if args.check_urls:
        urls = {r["key"] for r in cur.get("pages", [])} | ({r["key"] for r in prev.get("pages", [])} if prev else set())
        res["url_status"] = check_urls(sorted(urls))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)

    sys.stdout.reconfigure(encoding="utf-8")
    t = res["current"]["totals"]
    print(f"## Periodo attuale ({t['from']} → {t['to']})\n")
    print(f"Clic {t['clicks']:.0f} · Impressioni {t['impressions']:.0f} · CTR {t['ctr_pct']}% · "
          f"Posizione media {t['avg_position']} (fonte: {t['source']})\n")
    if "previous" in res:
        p = res["previous"]["totals"]
        print(f"Periodo precedente ({p['from']} → {p['to']}): clic {p['clicks']:.0f} · impressioni "
              f"{p['impressions']:.0f} · CTR {p['ctr_pct']}% · posizione {p['avg_position']}\n")
    if args.brand:
        for label, part in (("attuale", res["current"]), ("precedente", res.get("previous"))):
            if part and "brand_split" in part:
                b = part["brand_split"]
                print(f"Periodo {label} — query col nome: {b['brand']['clicks']:.0f} clic / "
                      f"{b['brand']['impressions']:.0f} impressioni · altre query: {b['non_brand']['clicks']:.0f} clic / "
                      f"{b['non_brand']['impressions']:.0f} impressioni\n")
    for w in res["warnings"]:
        print(f"> Attenzione: {w}\n")
    if "url_status" in res:
        print("### Stato attuale delle pagine presenti nei dati\n"
              + md_table(res["url_status"], [("key", "Pagina"), ("status", "Stato HTTP"), ("location", "Redirect verso")]))
    cols = [("key", "Query"), ("clicks", "Clic"), ("impressions", "Impr."), ("ctr", "CTR %"), ("position", "Pos.")]
    print("### Query principali\n" + md_table(res["current"]["top_queries"], cols))
    print("### Molte impressioni, pochi clic (title/description da rivedere?)\n"
          + md_table(res["current"]["top_impressions_low_ctr"], cols))
    print("### Pagine principali\n" + md_table(res["current"]["top_pages"], [("key", "Pagina")] + cols[1:]))
    if "compare_queries" in res:
        c = res["compare_queries"]
        print("### Query nuove\n" + md_table(c["new"], cols))
        print("### Query sparite\n" + md_table(c["lost"], cols))
        mc = [("key", "Query"), ("d_clicks", "Δ clic"), ("d_impressions", "Δ impr."), ("position", "Pos."),
              ("d_position", "Δ pos.")]
        print("### In crescita\n" + md_table(c["up"], mc))
        print("### In calo\n" + md_table(c["down"], mc))
        cp = res["compare_pages"]
        pcols = [("key", "Pagina")] + cols[1:]
        print("### Pagine nuove nei risultati\n" + md_table(cp["new"], pcols))
        print("### Pagine sparite dai risultati\n" + md_table(cp["lost"], pcols))
        pm = [("key", "Pagina")] + mc[1:]
        print("### Pagine in crescita\n" + md_table(cp["up"], pm))
        print("### Pagine in calo\n" + md_table(cp["down"], pm))


if __name__ == "__main__":
    main()
