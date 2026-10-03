#!/usr/bin/env python3
"""Test di attivazione delle skill seo-kit (compatibile con Windows).

Per ogni richiesta lancia `claude -p` in una cartella vuota, con il plugin installato,
e registra quale skill viene invocata (o nessuna). Interrompe il processo appena
vede la prima invocazione di una skill, o dopo alcune chiamate ad altri strumenti,
per consumare il meno possibile.

Uso:
  python trigger_test.py trigger-queries.json --runs 2 --workers 4 --out results.json
  python trigger_test.py trigger-queries.json --only seo-content,seo-build
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_OTHER_TOOLS = 3


def run_query(query, cwd, timeout, model=None):
    cmd = ["claude", "-p", query, "--output-format", "stream-json", "--verbose", "--include-partial-messages"]
    if model:
        cmd += ["--model", model]
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=cwd, env=env,
                            shell=(os.name == "nt"))
    timer = threading.Timer(timeout, proc.kill)
    timer.start()
    tools, current, partial = [], None, ""
    result = {"skill": None, "tools": tools, "timeout": False}
    try:
        for raw in proc.stdout:
            line = raw.decode("utf-8", "replace").strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "stream_event":
                se = ev.get("event", {})
                t = se.get("type")
                if t == "content_block_start" and se.get("content_block", {}).get("type") == "tool_use":
                    current, partial = se["content_block"].get("name"), ""
                elif t == "content_block_delta" and current:
                    partial += se.get("delta", {}).get("partial_json", "")
                elif t == "content_block_stop" and current:
                    if current == "Skill":
                        try:
                            result["skill"] = json.loads(partial).get("skill")
                        except json.JSONDecodeError:
                            result["skill"] = partial[:80]
                        return result
                    tools.append(current)
                    current = None
                    if len(tools) >= MAX_OTHER_TOOLS:
                        return result
            elif ev.get("type") == "result":
                return result
        return result
    finally:
        timer.cancel()
        if proc.poll() is None:
            proc.kill()
        result["timeout"] = proc.returncode is not None and proc.returncode < 0 and not result["skill"]


def short(skill):
    if not skill:
        return None
    return skill.split(":", 1)[1] if skill.startswith("seo-kit:") else f"altro:{skill}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("queries")
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--model")
    ap.add_argument("--only", help="limita alle richieste attese per queste skill (separate da virgola; 'none' per i negativi)")
    ap.add_argument("--out", default="trigger-results.json")
    args = ap.parse_args()

    items = json.load(open(args.queries, encoding="utf-8"))
    if args.only:
        keep = set(args.only.split(","))
        items = [i for i in items if (i["expected"] or "none") in keep]
    workdir = tempfile.mkdtemp(prefix="seo-kit-trigger-")
    jobs = [(i, r) for i in range(len(items)) for r in range(args.runs)]
    got = defaultdict(list)
    t0 = time.time()
    with ThreadPoolExecutor(args.workers) as ex:
        futs = {ex.submit(run_query, items[i]["query"], workdir, args.timeout, args.model): i for i, _ in jobs}
        for n, f in enumerate(as_completed(futs), 1):
            i = futs[f]
            try:
                got[i].append(f.result())
            except Exception as e:  # noqa: BLE001
                got[i].append({"skill": None, "tools": [], "error": str(e)})
            print(f"\r{n}/{len(jobs)}", end="", file=sys.stderr, flush=True)
    print(file=sys.stderr)

    rows, conf = [], Counter()
    for i, it in enumerate(items):
        exp = it["expected"]
        res = [short(r["skill"]) for r in got[i]]
        ok = sum(1 for s in res if s == exp)
        rows.append({"query": it["query"], "expected": exp, "got": res, "ok": ok, "runs": len(res),
                     "other_tools": [r["tools"] for r in got[i]]})
        for s in res:
            conf[(exp or "nessuna", s or "nessuna")] += 1

    total_ok = sum(r["ok"] for r in rows)
    total = sum(r["runs"] for r in rows)
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Corretti: {total_ok}/{total} ({100 * total_ok / total:.0f}%) in {time.time() - t0:.0f}s\n")
    by = defaultdict(lambda: [0, 0])
    for r in rows:
        by[r["expected"] or "nessuna"][0] += r["ok"]
        by[r["expected"] or "nessuna"][1] += r["runs"]
    for k, (a, b) in sorted(by.items()):
        print(f"  {k:18s} {a}/{b}")
    print("\nErrori:")
    for r in rows:
        if r["ok"] < r["runs"]:
            print(f"  atteso {r['expected'] or 'nessuna'} -> {r['got']} | {r['query'][:90]}")
    json.dump({"rows": rows, "confusion": {f"{a} -> {b}": n for (a, b), n in conf.items()}},
              open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
