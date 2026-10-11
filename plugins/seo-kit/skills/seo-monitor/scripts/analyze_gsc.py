#!/usr/bin/env python3
"""Analyse a Google Search Console Performance export (zip or folder of CSV files).

Search Console > Performance > Export > "Download CSV" gives a .zip with one CSV
per dimension (queries, pages, countries, devices, dates, search appearance,
filters). Exports in English, Italian, German, Spanish, Portuguese or French are
recognised; comma, semicolon or tab separated (Excel re-saves included). A
"Compare" export (two columns per metric) provides the previous period by itself;
otherwise pass the previous period's export with --previous.

Usage:
  python analyze_gsc.py current.zip
  python analyze_gsc.py current.zip --previous previous.zip --brand "northwind|physio"
  python analyze_gsc.py export-folder --check-urls --json gsc.json

--brand is a regular expression matched case-insensitively and accent-insensitively
against each query, e.g. "northwind|physio".

Note: anonymised queries are not listed in the queries table, so the sum of clicks
by query is lower than the total; the reliable total is the dates table.

Exit codes: 0 done · 2 usage error (unreadable export, invalid --brand regex).
"""
import argparse
import os
import re
import sys
import time
import unicodedata


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

from seokit import __version__, gsc, report  # noqa: E402
from seokit import http as seohttp  # noqa: E402

TINY_CLICKS = 50
CHECK_DELAY = 1.0
_sleep = time.sleep  # patched by tests


def strip_accents(text):
    """NFD + drop combining marks; case is left alone (regex escapes like \\D stay valid)."""
    return "".join(c for c in unicodedata.normalize("NFD", text or "") if not unicodedata.combining(c))


def compile_brand(pattern):
    return re.compile(strip_accents(pattern), re.IGNORECASE)


def brand_split(rows, rx):
    def agg(rs):
        return {"queries": len(rs), "clicks": sum(r["clicks"] for r in rs),
                "impressions": sum(r["impressions"] for r in rs)}
    brand = [r for r in rows if rx.search(strip_accents(r["key"]))]
    other = [r for r in rows if not rx.search(strip_accents(r["key"]))]
    return {"brand": agg(brand), "non_brand": agg(other)}


def top(rows, n):
    return sorted(rows, key=lambda r: (-r["clicks"], -r["impressions"], r["key"]))[:n]


def opportunities(rows, min_impressions, max_ctr, n):
    picked = [r for r in rows if r["impressions"] >= min_impressions and r["ctr"] < max_ctr]
    return sorted(picked, key=lambda r: (-r["impressions"], r["key"]))[:n]


def compare(cur, prev, n):
    pc = {r["key"]: r for r in prev}
    cc = {r["key"]: r for r in cur}
    new = sorted((r for k, r in cc.items() if k not in pc), key=lambda r: (-r["impressions"], r["key"]))[:n]
    lost = sorted((r for k, r in pc.items() if k not in cc), key=lambda r: (-r["impressions"], r["key"]))[:n]
    movers = []
    for k, r in cc.items():
        if k in pc:
            movers.append({"key": k, "clicks": r["clicks"], "d_clicks": r["clicks"] - pc[k]["clicks"],
                           "impressions": r["impressions"], "d_impressions": r["impressions"] - pc[k]["impressions"],
                           "position": r["position"], "d_position": round(r["position"] - pc[k]["position"], 1)})
    up = sorted((m for m in movers if m["d_clicks"] > 0 or (m["d_clicks"] == 0 and m["d_impressions"] > 0)),
                key=lambda m: (-m["d_clicks"], -m["d_impressions"], m["key"]))[:n]
    down = sorted((m for m in movers if m["d_clicks"] < 0 or (m["d_clicks"] == 0 and m["d_impressions"] < 0)),
                  key=lambda m: (m["d_clicks"], m["d_impressions"], m["key"]))[:n]
    return {"new": new, "lost": lost, "up": up, "down": down}


def check_urls(page_urls, fetch=None):
    """Current HTTP status of the pages in the export (1 s between requests)."""
    fetch = fetch or seohttp.fetch
    out = []
    for i, u in enumerate(page_urls):
        if not u.lower().startswith(("http://", "https://")):
            continue
        if i:
            _sleep(CHECK_DELAY)
        r = fetch(u, max_bytes=65536, retries=0, timeout=15)
        first = r.chain[0] if r.chain else {}
        out.append({"key": u, "status": first.get("status"), "location": first.get("location") or "",
                    "final_status": r.status, "final_url": r.final_url or "", "error": r.error or ""})
    return out


def filters_signature(filters):
    if not filters:
        return None
    return (filters.get("search_type"), tuple(sorted((d["name"], d["value"]) for d in filters.get("dimensions", []))))


def data_warnings(cur, prev, cur_tot, prev_tot, prev_source):
    w = list(cur["warnings"])
    if prev is not None:
        w += [f"previous: {x}" for x in prev["warnings"]]
    if cur_tot["source"] != "dates":
        w.append("No dates table: totals come from the queries table and miss anonymised queries.")
    if cur_tot["clicks"] < TINY_CLICKS:
        w.append(f"Small numbers: {cur_tot['clicks']:.0f} clicks in the current period. Below about "
                 f"{TINY_CLICKS} clicks, percentage changes are mostly noise.")
    if prev_tot is not None:
        if cur_tot["days"] and prev_tot["days"] and cur_tot["days"] != prev_tot["days"]:
            w.append(f"The periods have different lengths ({cur_tot['days']} days vs {prev_tot['days']}): "
                     "compare daily averages, not totals.")
        cur_f = filters_signature(cur["meta"]["filters"])
        prev_f = filters_signature((prev or cur)["meta"]["filters"]) if prev_source == "file" else cur_f
        if cur_f != prev_f:
            w.append(f"The exports use different filters ({cur_f} vs {prev_f}): the periods are not comparable.")
    pages_sum = sum(r["clicks"] for r in cur["current"].get("pages", []))
    if cur["current"].get("dates") and cur["current"].get("pages") \
            and abs(pages_sum - cur_tot["clicks"]) > max(2, 0.05 * cur_tot["clicks"]):
        w.append(f"Clicks by page ({pages_sum:.0f}) differ from the total by date ({cur_tot['clicks']:.0f}): "
                 "Search Console counts by page differently and exports only the top rows.")
    w.append("Exports list at most 1,000 rows per table and omit anonymised queries.")
    return w


# -- Markdown --------------------------------------------------------------------

def fmt(v):
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() else f"{v:.2f}".rstrip("0").rstrip(".")
    return "" if v is None else str(v)


def md_table(rows, cols):
    if not rows:
        return "_No data._\n"
    out = "| " + " | ".join(label for _, label in cols) + " |\n|" + "---|" * len(cols) + "\n"
    for r in rows:
        out += "| " + " | ".join(fmt(r.get(key, "")).replace("|", "\\|") for key, _ in cols) + " |\n"
    return out


def change(cur, prev, kind):
    if prev is None:
        return ""
    if kind == "pct_points":
        return f"{cur - prev:+.2f} pt"
    if kind == "position":
        if cur is None or prev is None:
            return ""
        return f"{cur - prev:+.1f}"
    delta = cur - prev
    pct = f" ({100 * delta / prev:+.0f}%)" if prev else ""
    return f"{delta:+.0f}{pct}"


def render(res, args):
    cur_t = res["current"]["totals"]
    prev = res.get("previous")
    prev_t = prev["totals"] if prev else None
    q_cols = [("key", "Query"), ("clicks", "Clicks"), ("impressions", "Impressions"), ("ctr", "CTR %"),
              ("position", "Position")]
    p_cols = [("key", "Page")] + q_cols[1:]
    m_cols = [("key", "Query"), ("clicks", "Clicks"), ("d_clicks", "Δ clicks"), ("impressions", "Impressions"),
              ("d_impressions", "Δ impressions"), ("position", "Position"), ("d_position", "Δ position")]
    lines = ["# Search Console report", ""]
    lines.append(f"Source: `{res['source']}`" + (f" · previous: `{prev['source']}`" if prev else ""))
    lines += ["", "## Summary", ""]
    period = f"{cur_t['from']} → {cur_t['to']} ({cur_t['days']} days)" if cur_t["from"] else "dates not in the export"
    lines.append(f"- Current period: {period}.")
    lines.append(f"- {fmt(cur_t['clicks'])} clicks, {fmt(cur_t['impressions'])} impressions, CTR {cur_t['ctr_pct']}%, "
                 f"average position {fmt(cur_t['avg_position'])} (totals from {cur_t['source']}).")
    if prev_t:
        lines.append(f"- Previous period: {fmt(prev_t['clicks'])} clicks, {fmt(prev_t['impressions'])} impressions; "
                     f"clicks {change(cur_t['clicks'], prev_t['clicks'], 'abs')}, impressions "
                     f"{change(cur_t['impressions'], prev_t['impressions'], 'abs')}.")
    if res["warnings"]:
        lines.append(f"- {len(res['warnings'])} data note(s): see Data limits.")
    lines += ["", "## Key numbers", ""]
    rows = [("Clicks", "clicks", "abs"), ("Impressions", "impressions", "abs"), ("CTR %", "ctr_pct", "pct_points"),
            ("Average position", "avg_position", "position")]
    lines.append("| Metric | Current | Previous | Change |\n|---|---|---|---|")
    for label, key, kind in rows:
        p = prev_t[key] if prev_t else None
        lines.append(f"| {label} | {fmt(cur_t[key])} | {fmt(p) if prev_t else '-'} | "
                     f"{change(cur_t[key], p, kind) if prev_t else '-'} |")
    lines += ["", "## Brand vs non-brand", ""]
    if "brand_split" in res["current"]:
        lines.append(f"Brand regex: `{args.brand}` (case- and accent-insensitive).\n")
        lines.append("| Period | Brand queries | Brand clicks | Brand impressions | Other queries | Other clicks | "
                     "Other impressions |\n|---|---|---|---|---|---|---|")
        for label, part in (("Current", res["current"]), ("Previous", prev)):
            if part and "brand_split" in part:
                b, nb = part["brand_split"]["brand"], part["brand_split"]["non_brand"]
                lines.append(f"| {label} | {b['queries']} | {fmt(b['clicks'])} | {fmt(b['impressions'])} | "
                             f"{nb['queries']} | {fmt(nb['clicks'])} | {fmt(nb['impressions'])} |")
    else:
        lines.append("_Pass --brand REGEX to split queries that contain the brand or person name._")
    lines += ["", "## Top queries", "", md_table(res["current"]["top_queries"], q_cols)]
    lines += ["## Top pages", "", md_table(res["current"]["top_pages"], p_cols)]
    if "url_status" in res:
        lines += ["### Current HTTP status of the pages", "",
                  md_table(res["url_status"], [("key", "Page"), ("status", "Status"), ("location", "Redirects to"),
                                               ("final_status", "Final status"), ("error", "Error")])]
    lines += ["## Opportunities (high impressions, low CTR)", "",
              f"Queries with at least {fmt(args.min_impressions)} impressions and CTR below {fmt(args.max_ctr)}%: "
              "review the title and description of the page that ranks.", "",
              md_table(res["current"]["opportunities"], q_cols)]
    lines += ["## New and lost queries", ""]
    if "compare_queries" in res:
        c = res["compare_queries"]
        lines += ["### New queries", "", md_table(c["new"], q_cols), "### Lost queries", "", md_table(c["lost"], q_cols)]
    else:
        lines.append("_No previous period: pass --previous or use a Compare export._\n")
    lines += ["## Changes vs previous period", ""]
    if "compare_queries" in res:
        c, cp = res["compare_queries"], res["compare_pages"]
        page_m = [("key", "Page")] + m_cols[1:]
        lines += ["### Queries up", "", md_table(c["up"], m_cols), "### Queries down", "", md_table(c["down"], m_cols),
                  "### Pages up", "", md_table(cp["up"], page_m), "### Pages down", "", md_table(cp["down"], page_m),
                  "### Pages new in results", "", md_table(cp["new"], p_cols),
                  "### Pages gone from results", "", md_table(cp["lost"], p_cols)]
    else:
        lines.append("_No previous period: pass --previous or use a Compare export._\n")
    lines += ["## Data limits", ""]
    lines += [f"- {w}" for w in res["warnings"]]
    return "\n".join(lines).rstrip() + "\n"


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", help=".zip or folder of the Performance export (current period)")
    ap.add_argument("--previous", help="export of the previous period, for the comparison")
    ap.add_argument("--brand", help='regex of queries containing the brand or person name, e.g. "northwind|physio"')
    ap.add_argument("--top", type=int, default=15, help="rows per table (default 15)")
    ap.add_argument("--min-impressions", type=float, default=20, help="opportunities: minimum impressions (default 20)")
    ap.add_argument("--max-ctr", type=float, default=2.0, help="opportunities: CTR below this percent (default 2.0)")
    ap.add_argument("--check-urls", action="store_true",
                    help="fetch the pages listed in the exports and report their current HTTP status")
    ap.add_argument("--json", metavar="PATH", help="also write the result as JSON")
    ap.add_argument("--version", action="version", version=f"seo-kit {__version__}")
    return ap


def main(argv=None):
    report.setup_stdout()
    args = build_parser().parse_args(argv)
    brand_rx = None
    if args.brand:
        try:
            brand_rx = compile_brand(args.brand)
        except re.error as exc:
            report.eprint(f"error: --brand is not a valid regular expression: {exc}")
            return 2
    try:
        cur = gsc.load_export(args.export)
        prev_file = gsc.load_export(args.previous) if args.previous else None
    except gsc.GscError as exc:
        report.eprint(f"error: {exc}")
        return 2

    if prev_file is not None:
        prev_tables, prev_source = prev_file["current"], "file"
        if cur["previous"]:
            cur["warnings"].append("The current export is a Compare export; its previous-period columns were "
                                   "ignored because --previous was given.")
    elif cur["previous"]:
        prev_tables, prev_source = cur["previous"], "compare"
    else:
        prev_tables, prev_source = None, None

    q = cur["current"].get("queries", [])
    res = {"tool": "analyze_gsc", "version": __version__, "source": args.export,
           "meta": cur["meta"], "current": {"totals": gsc.totals(cur["current"])}}
    res["current"]["top_queries"] = top(q, args.top)
    res["current"]["top_pages"] = top(cur["current"].get("pages", []), args.top)
    res["current"]["opportunities"] = opportunities(q, args.min_impressions, args.max_ctr, args.top)
    res["current"]["devices"] = cur["current"].get("devices", [])
    res["current"]["countries"] = top(cur["current"].get("countries", []), args.top)
    if brand_rx:
        res["current"]["brand_split"] = brand_split(q, brand_rx)
    prev_tot = None
    if prev_tables is not None:
        prev_tot = gsc.totals(prev_tables)
        if prev_source == "compare":
            prev_tot["from"] = prev_tot["to"] = None  # rows are aligned to current-period dates
        res["previous"] = {"source": args.previous if prev_source == "file" else "compare columns of the same export",
                           "totals": prev_tot}
        if brand_rx:
            res["previous"]["brand_split"] = brand_split(prev_tables.get("queries", []), brand_rx)
        res["compare_queries"] = compare(q, prev_tables.get("queries", []), args.top)
        res["compare_pages"] = compare(cur["current"].get("pages", []), prev_tables.get("pages", []), args.top)
    res["warnings"] = data_warnings(cur, prev_file, res["current"]["totals"], prev_tot, prev_source)
    if args.check_urls:
        pages = [r["key"] for r in cur["current"].get("pages", [])]
        if prev_tables:
            pages += [r["key"] for r in prev_tables.get("pages", [])]
        res["url_status"] = check_urls(list(dict.fromkeys(pages)))

    if args.json:
        report.write_json(args.json, res)
    print(render(res, args), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
