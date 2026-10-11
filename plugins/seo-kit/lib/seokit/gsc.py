"""Google Search Console "Performance" export loader (zip or folder of CSV files).

Each CSV's role (queries, pages, countries, devices, dates, search_appearance,
filters) is detected from the shape of its data first (URLs, dates, device names,
two text columns), then from the first header cell and the file name in English,
Italian, German, Spanish, Portuguese or French. Metric columns are matched by
header pattern, falling back to position. Compare exports (two columns per metric)
yield a "previous" period alongside "current".
"""
from __future__ import annotations

import csv
import io
import re
import unicodedata
import zipfile
from pathlib import Path
from typing import Optional

ROLES = ("queries", "pages", "countries", "devices", "dates", "search_appearance", "filters")
METRICS = ("clicks", "impressions", "ctr", "position")

# File-name hints (secondary signal), folded (lower case, no accents).
NAME_HINTS = {
    "queries": ["queries", "query", "suchanfragen", "consultas", "requetes"],
    "pages": ["pages", "pagine", "seiten", "paginas"],
    "countries": ["countries", "paesi", "lander", "laender", "paises", "pays"],
    "devices": ["devices", "dispositivi", "gerate", "geraete", "dispositivos", "appareils"],
    "dates": ["dates", "date", "chart", "grafico", "daten", "diagramm", "fechas", "datas", "graphique"],
    "search_appearance": ["search appearance", "aspetto nella ricerca", "darstellung in der suche",
                          "aspecto en los resultados de busqueda", "aparencia na pesquisa",
                          "apparence dans les resultats de recherche"],
    "filters": ["filters", "filtri", "filter", "filtros", "filtres"],
}
# First-header-cell hints, folded; checked in this order.
HEADER_HINTS = [
    ("filters", ["filter", "filtro", "filtre"]),
    ("search_appearance", ["appearance", "aspetto", "darstellung", "aspecto", "aparencia", "apparence"]),
    ("devices", ["device", "dispositiv", "gerat", "appareil"]),
    ("countries", ["country", "paese", "land", "pais", "pays"]),
    ("pages", ["page", "pagin", "seite"]),
    ("queries", ["quer", "suchanfrage", "consulta", "requete"]),
    ("dates", ["date", "data", "datum", "fecha"]),
]
METRIC_PATTERNS = {
    "clicks": re.compile(r"clic|click|klick|clique"),
    "impressions": re.compile(r"impres"),
    "ctr": re.compile(r"ctr"),
    "position": re.compile(r"posi"),
}
PREVIOUS_HINTS = ("previous", "precedent", "vorherig", "anterior", "prior", "vorperiode")
SEARCH_TYPE_NAMES = {"search type", "tipo di ricerca", "suchtyp", "suchtyp ", "tipo de busqueda",
                     "tipo de pesquisa", "type de recherche"}
DATE_FILTER_NAMES = {"date", "data", "datum", "fecha", "dates"}
DEVICE_WORDS = ("tablet", "desktop", "mobile", "computer", "cellulare", "mobil", "movil", "celular",
                "ordinateur")
_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_LOCAL_DATE = re.compile(r"^(\d{1,2})[./-](\d{1,2})[./-](\d{2,4})$")
MAX_ROW_WARNINGS = 5


class GscError(ValueError):
    """The path is not a readable Search Console export."""


def fold(text: str) -> str:
    """Lower case, accents removed (NFD + strip combining marks)."""
    return "".join(c for c in unicodedata.normalize("NFD", text or "")
                   if not unicodedata.combining(c)).lower().strip()


_SPACES = re.compile(r"[\s   ']")


def parse_number(value, decimal: bool = False) -> Optional[float]:
    """Parse '1,234' '1.234' '1 234' '1.234,56' '1,234.56' '12,5 %' '12.5%' '<0.1%'.

    A single separator followed by exactly three digits (and a non-zero integer
    part) is a thousands separator; otherwise it is the decimal mark. With
    decimal=True (CTR and position columns, never >= 1000) a single separator is
    always the decimal mark. '<0.1%' returns its bound (0.1). Empty or unparsable
    values return None.
    """
    if value is None:
        return None
    s = _SPACES.sub("", str(value)).replace("%", "").lstrip("<>~+≈").strip()
    if s in ("", "-", "—", "–", "n/a", "N/A"):
        return None
    negative = s.startswith("-")
    if negative:
        s = s[1:]
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s or "." in s:
        sep = "," if "," in s else "."
        parts = s.split(sep)
        if len(parts) > 2:
            s = "".join(parts)
        else:
            whole, frac = parts
            if not decimal and len(frac) == 3 and whole not in ("", "0") and whole.isdigit():
                s = whole + frac
            else:
                s = whole + "." + frac
    try:
        number = float(s)
    except ValueError:
        return None
    return -number if negative else number


def _decode(data: bytes) -> str:
    if data.startswith(b"\xef\xbb\xbf"):
        return data[3:].decode("utf-8", "replace")
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16", "replace")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        try:
            return data.decode("cp1252")  # Excel re-save on Windows
        except UnicodeDecodeError:
            return data.decode("latin-1")


def _zip_name(info: zipfile.ZipInfo) -> str:
    """Entry name: UTF-8 when flagged; otherwise try UTF-8 bytes read as cp437."""
    if info.flag_bits & 0x800:
        return info.filename
    try:
        return info.filename.encode("cp437").decode("utf-8")
    except UnicodeError:
        return info.filename


def _read_files(path) -> list:
    p = Path(path)
    if not p.exists():
        raise GscError(f"{path}: file or folder not found")
    files = []
    if p.is_dir():
        for f in sorted(p.iterdir()):
            if f.is_file() and f.suffix.lower() == ".csv":
                files.append((f.name, f.read_bytes()))
    elif zipfile.is_zipfile(p):
        with zipfile.ZipFile(p) as z:
            for info in z.infolist():
                name = _zip_name(info)
                if not info.is_dir() and name.lower().endswith(".csv"):
                    files.append((Path(name).name, z.read(info)))
    elif p.suffix.lower() == ".csv":
        files.append((p.name, p.read_bytes()))
    else:
        raise GscError(f"{path}: expected a .zip export, a folder or a .csv file")
    if not files:
        raise GscError(f"{path}: no CSV files found")
    return files


def sniff_delimiter(text: str) -> str:
    """csv.Sniffer restricted to , ; and tab, checked against column consistency."""
    sample = text[:8192]
    lines = [ln for ln in sample.splitlines() if ln.strip()][:30]
    scores = {}
    for delim in (",", ";", "\t"):
        rows = list(csv.reader(lines, delimiter=delim))
        if not rows or len(rows[0]) < 2:
            scores[delim] = (0.0, 0)
            continue
        width = len(rows[0])
        same = sum(1 for r in rows if len(r) == width) / len(rows)
        scores[delim] = (same, width)
    try:
        sniffed = csv.Sniffer().sniff(sample, delimiters=",;\t").delimiter
    except csv.Error:
        sniffed = None
    best = max(scores, key=lambda d: scores[d])
    if sniffed in scores and scores[sniffed] == scores[best]:
        return sniffed
    return best if scores[best][1] else ","


def _is_date(value: str) -> bool:
    return bool(_ISO_DATE.match(value) or _LOCAL_DATE.match(value))


def normalize_date(value: str) -> str:
    """ISO dates unchanged; d/m/y (or m/d/y when the day is > 12) to YYYY-MM-DD."""
    value = value.strip()
    if _ISO_DATE.match(value):
        return value
    m = _LOCAL_DATE.match(value)
    if not m:
        return value
    a, b, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if year < 100:
        year += 2000
    day, month = (a, b) if b <= 12 else (b, a)
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return value
    return f"{year:04d}-{month:02d}-{day:02d}"


def _frac(values, predicate) -> float:
    values = [v for v in values if v]
    if not values:
        return 0.0
    return sum(1 for v in values if predicate(v)) / len(values)


def classify(header: list, rows: list, filename: str = "") -> str:
    """Role of a table: shape first, then first header cell, then file name."""
    keys = [r[0].strip() for r in rows if r and r[0].strip()]
    if len(header) == 2 and rows:
        numeric = _frac([r[1] for r in rows if len(r) > 1], lambda v: parse_number(v) is not None)
        if numeric < 0.5:
            return "filters"
    if keys and _frac(keys, _is_date) >= 0.8:
        return "dates"
    if keys and _frac(keys, lambda k: k.lower().startswith(("http://", "https://"))) >= 0.8:
        return "pages"
    if 0 < len(keys) <= 3 and any(any(w in fold(k) for w in DEVICE_WORDS) for k in keys) \
            and any("tablet" in fold(k) for k in keys):
        return "devices"
    words = re.findall(r"\w+", fold(header[0])) if header else []
    for role, hints in HEADER_HINTS:
        if any(w.startswith(h) for w in words for h in hints):
            return role
    stem = fold(Path(filename).stem)
    for role, hints in NAME_HINTS.items():
        if stem in hints or any(stem.startswith(h) for h in hints if " " in h):
            return role
    return "unknown"


def metric_columns(header: list) -> dict:
    """{"current": {metric: index}, "previous": {metric: index} or None}."""
    found: dict = {m: [] for m in METRICS}
    for i, cell in enumerate(header[1:], start=1):
        f = fold(cell)
        for metric, rx in METRIC_PATTERNS.items():
            if rx.search(f):
                found[metric].append(i)
                break
    if not any(found.values()):  # unknown language: rely on position
        n = len(header) - 1
        if n >= 8:
            return {"current": {m: 1 + 2 * k for k, m in enumerate(METRICS)},
                    "previous": {m: 2 + 2 * k for k, m in enumerate(METRICS)}}
        return {"current": {m: 1 + k for k, m in enumerate(METRICS) if 1 + k < len(header)},
                "previous": None}
    current, previous = {}, {}
    for metric, cols in found.items():
        if not cols:
            continue
        if len(cols) >= 2:
            prev = [c for c in cols if any(h in fold(header[c]) for h in PREVIOUS_HINTS)]
            prev_col = prev[0] if prev else cols[1]
            cur_col = next(c for c in cols if c != prev_col)
            current[metric], previous[metric] = cur_col, prev_col
        else:
            current[metric] = cols[0]
    return {"current": current, "previous": previous or None}


def _row_values(row: list, cols: dict) -> dict:
    out = {}
    for metric in METRICS:
        idx = cols.get(metric)
        value = None
        if idx is not None and idx < len(row):
            value = parse_number(row[idx], decimal=metric in ("ctr", "position"))
        out[metric] = value if value is not None else 0.0
    return out


def parse_filters(rows: list) -> dict:
    out = {"search_type": None, "date_range": None, "dimensions": [], "raw": []}
    for r in rows:
        if not r or not r[0].strip():
            continue
        name, value = r[0].strip(), (r[1].strip() if len(r) > 1 else "")
        out["raw"].append([name, value])
        f = fold(name)
        if f in SEARCH_TYPE_NAMES:
            out["search_type"] = value
        elif f in DATE_FILTER_NAMES:
            out["date_range"] = value
        else:
            out["dimensions"].append({"name": name, "value": value})
    return out


def load_export(path) -> dict:
    """Load a Search Console export.

    Returns {"source", "current": {role: [rows]}, "previous": {role: [rows]} or None,
    "meta": {"filters", "compare", "files": {name: role}, "columns": {role: header},
    "delimiters": {name: delim}}, "warnings": [...]}. Rows are
    {"key", "clicks", "impressions", "ctr" (percent), "position"}.
    Raises GscError when the path holds no usable CSV.
    """
    files = _read_files(path)
    result = {"source": str(path), "current": {}, "previous": None,
              "meta": {"filters": None, "compare": False, "files": {}, "columns": {}, "delimiters": {}},
              "warnings": []}
    previous: dict = {}
    for name, data in files:
        text = _decode(data)
        delim = sniff_delimiter(text)
        rows = list(csv.reader(io.StringIO(text), delimiter=delim))
        rows = [r for r in rows if any(c.strip() for c in r)]
        if not rows:
            result["warnings"].append(f"{name}: empty file skipped")
            continue
        header, body = rows[0], rows[1:]
        role = classify(header, body, name)
        result["meta"]["files"][name] = role
        result["meta"]["delimiters"][name] = delim
        if role == "unknown":
            result["warnings"].append(f"{name}: could not tell what this table contains; skipped")
            continue
        if role == "filters":
            result["meta"]["filters"] = parse_filters(body)
            continue
        if role in result["current"]:
            result["warnings"].append(f"{name}: a second {role} table was ignored")
            continue
        cols = metric_columns(header)
        result["meta"]["columns"][role] = header
        width = len(header)
        cur_rows, prev_rows, skipped = [], [], 0
        for line_no, r in enumerate(body, start=2):
            if len(r) < width or not r[0].strip():
                skipped += 1
                if skipped <= MAX_ROW_WARNINGS:
                    result["warnings"].append(
                        f"{name}: line {line_no} has {len(r)} of {width} columns; skipped")
                continue
            key = r[0].strip()
            if role == "dates":
                key = normalize_date(key)
            cur_rows.append({"key": key, **_row_values(r, cols["current"])})
            if cols["previous"]:
                prev_rows.append({"key": key, **_row_values(r, cols["previous"])})
        if skipped > MAX_ROW_WARNINGS:
            result["warnings"].append(f"{name}: {skipped} short or malformed lines skipped in total")
        if cols["previous"]:
            # A compare export lists the union of both periods: a row with no
            # clicks and no impressions in one period did not exist in it.
            def present(row):
                return row["clicks"] or row["impressions"]
            cur_rows = [r for r in cur_rows if present(r)]
            previous[role] = [r for r in prev_rows if present(r)]
            result["meta"]["compare"] = True
        result["current"][role] = cur_rows
    if not result["current"]:
        raise GscError(f"{path}: no Search Console performance table recognised")
    if previous:
        result["previous"] = previous
    return result


def totals(tables: dict) -> dict:
    """Clicks, impressions, CTR and impression-weighted position.

    Uses the dates table when present (the only complete total); falls back to
    queries, which exclude anonymised queries and therefore under-count.
    """
    if tables.get("dates"):
        src, source = tables["dates"], "dates"
    else:
        src, source = tables.get("queries") or [], "queries (anonymised queries excluded: under-counts)"
    clicks = sum(r["clicks"] for r in src)
    impressions = sum(r["impressions"] for r in src)
    weighted = sum(r["position"] * r["impressions"] for r in src)
    days = sorted(r["key"] for r in tables.get("dates") or [])
    return {
        "clicks": clicks, "impressions": impressions,
        "ctr_pct": round(100 * clicks / impressions, 2) if impressions else 0.0,
        "avg_position": round(weighted / impressions, 1) if impressions else None,
        "from": days[0] if days else None, "to": days[-1] if days else None,
        "days": len(days), "source": source,
    }
