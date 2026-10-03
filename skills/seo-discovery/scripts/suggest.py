#!/usr/bin/env python3
"""Suggerimenti di completamento automatico di Google per una lista di ricerche.

Indizio gratuito di come le persone formulano le ricerche: NON dà volumi e non
garantisce che una ricerca porti traffico. L'endpoint non è un'API documentata e
può cambiare o limitare le richieste: usalo con moderazione (pausa tra le query).

Uso:
  python suggest.py "orientamento verona" "career coach" --hl it --gl it
  python suggest.py "elia raguso" --expand        # aggiunge varianti "query a", "query b", ...
"""
import argparse
import json
import sys
import time
import urllib.parse
import urllib.request

URL = "https://suggestqueries.google.com/complete/search?client=firefox&hl={hl}&gl={gl}&q={q}"


def suggest(q, hl, gl):
    req = urllib.request.Request(URL.format(hl=hl, gl=gl, q=urllib.parse.quote(q)),
                                 headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8", "replace"))
        return data[1] if len(data) > 1 else []
    except Exception as e:  # noqa: BLE001
        return [f"ERRORE: {type(e).__name__}: {e}"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("queries", nargs="+")
    ap.add_argument("--hl", default="it", help="lingua (default it)")
    ap.add_argument("--gl", default="it", help="paese (default it)")
    ap.add_argument("--expand", action="store_true", help="prova anche 'query + lettera' (a-z)")
    ap.add_argument("--pause", type=float, default=1.0, help="secondi tra le richieste")
    args = ap.parse_args()

    out = {}
    for q in args.queries:
        variants = [q] + ([f"{q} {c}" for c in "abcdefghilmnopqrstuvz"] if args.expand else [])
        found = []
        for v in variants:
            for s in suggest(v, args.hl, args.gl):
                if s not in found:
                    found.append(s)
            time.sleep(args.pause)
        out[q] = found
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
