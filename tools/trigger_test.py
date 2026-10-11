#!/usr/bin/env python3
"""Trigger test for the seo-kit skills: which skill does Claude pick for a request?

For every query in the queries file, and for every run, it starts `claude -p` in a new
empty temporary folder with the plugin loaded through `--plugin-dir`, reads the
stream-json output and records the first skill Claude invokes (or none). The child
process is stopped as soon as the answer is known (first Skill call, a few other tool
calls, or the final result) and its whole process tree is killed on timeout, so each
run costs as little as possible. The temporary folder is removed after each run.

User settings are skipped (`--setting-sources project,local`) so that a seo-kit
installed from a marketplace does not answer in place of the copy under test; pass
--keep-user-settings to load them anyway.

Usage:
  python tools/trigger_test.py --dry-run
  python tools/trigger_test.py --runs 2 --workers 4
  python tools/trigger_test.py --only seo-content,none --runs 3 --model sonnet

Queries file: a JSON list of {"query": str, "expected": "<skill>" or null, "lang": "en"}
(null = the request should trigger no seo-kit skill).

A run whose session fails (a `result` event with is_error or an error subtype, or a
non-zero exit code when the tool did not stop the child itself: auth, rate limit,
rejected flag...) is recorded with status "error", listed in the summary and kept out
of the accuracy totals, so a broken environment does not look like "no skill invoked".

Output: a Markdown summary on stdout and the full results as JSON in
tools/trigger-runs/<timestamp>.json (git-ignored). Each real run is a billable Claude
Code session; use --dry-run first.

Exit codes: 0 done, 2 usage error (missing queries file, plugin dir or claude executable).
"""
import argparse
import datetime as _dt
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REPO = TOOLS_DIR.parent
DEFAULT_PLUGIN_DIR = REPO / "plugins" / "seo-kit"
DEFAULT_QUERIES = TOOLS_DIR / "trigger-queries.json"
DEFAULT_OUT_DIR = TOOLS_DIR / "trigger-runs"
PLUGIN_NAME = "seo-kit"
MAX_OTHER_TOOLS = 3
IS_WINDOWS = os.name == "nt"


# --------------------------------------------------------------------------- command

def build_command(claude, query, plugin_dir, model=None, max_budget_usd=None, keep_user_settings=False):
    """The argv of one `claude -p` run (the query is passed as one argument, never via a shell)."""
    cmd = [claude, "-p", query,
           "--plugin-dir", str(plugin_dir),
           "--output-format", "stream-json", "--verbose", "--include-partial-messages",
           "--no-session-persistence",
           "--strict-mcp-config"]
    if not keep_user_settings:
        cmd += ["--setting-sources", "project,local"]
    if model:
        cmd += ["--model", model]
    if max_budget_usd:
        cmd += ["--max-budget-usd", str(max_budget_usd)]
    return cmd


def child_env():
    env = dict(os.environ)
    env.pop("CLAUDECODE", None)  # allow a nested session when launched from Claude Code
    return env


# --------------------------------------------------------------------------- process tree

def popen_kwargs():
    if IS_WINDOWS:
        return {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
    return {"start_new_session": True}


def kill_tree(proc):
    """Kill the child and everything it started (Windows: taskkill /T; POSIX: process group)."""
    if proc.poll() is not None:
        return
    try:
        if IS_WINDOWS:
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        else:
            os.killpg(proc.pid, signal.SIGKILL)
    except (OSError, ProcessLookupError):
        pass
    try:
        proc.kill()
    except OSError:
        pass


def remove_dir(path, attempts=10):
    """rmtree with retries: on Windows a just-killed process can hold the folder for a moment."""
    for _ in range(attempts):
        shutil.rmtree(path, ignore_errors=True)
        if not os.path.exists(path):
            return True
        time.sleep(0.3)
    return not os.path.exists(path)


# --------------------------------------------------------------------------- stream parsing

class StreamState:
    """Incremental reader of `claude -p --output-format stream-json` events."""

    def __init__(self, max_other_tools=MAX_OTHER_TOOLS):
        self.skill = None
        self.tools = []
        self.done = False
        self.ended_by_result = False
        self.error = None  # set from a `result` event with is_error / an error subtype
        self.max_other_tools = max_other_tools
        self._current = None
        self._partial = ""

    def _tool(self, name, tool_input):
        if self.done:
            return
        if name == "Skill":
            skill = None
            if isinstance(tool_input, dict):
                skill = tool_input.get("skill")
            elif isinstance(tool_input, str):
                try:
                    skill = json.loads(tool_input).get("skill")
                except (ValueError, AttributeError):
                    skill = tool_input[:80] or None
            self.skill = skill or "?"
            self.done = True
            return
        self.tools.append(name)
        if len(self.tools) >= self.max_other_tools:
            self.done = True

    def feed(self, line):
        """Process one output line; returns True once the outcome is known."""
        line = line.strip()
        if not line or self.done:
            return self.done
        try:
            ev = json.loads(line)
        except ValueError:
            return False
        if not isinstance(ev, dict):
            return False
        kind = ev.get("type")
        if kind == "stream_event":
            se = ev.get("event") or {}
            t = se.get("type")
            block = se.get("content_block") or {}
            if t == "content_block_start" and block.get("type") == "tool_use":
                self._current, self._partial = block.get("name"), ""
            elif t == "content_block_delta" and self._current:
                self._partial += (se.get("delta") or {}).get("partial_json", "")
            elif t == "content_block_stop" and self._current:
                name, self._current = self._current, None
                self._tool(name, self._partial)
        elif kind == "assistant":
            # Complete messages (also emitted without --include-partial-messages).
            if self._current is None:
                for block in (ev.get("message") or {}).get("content") or []:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        self._tool(block.get("name"), block.get("input"))
                        if self.done:
                            break
        elif kind == "result":
            self.done = True
            self.ended_by_result = True
            subtype = str(ev.get("subtype") or "")
            if ev.get("is_error") or subtype.startswith("error"):
                detail = ev.get("result") or ev.get("error") or ""
                if not isinstance(detail, str):
                    detail = json.dumps(detail, ensure_ascii=False)
                self.error = ("%s: %s" % (subtype or "error", detail)).strip(": ")[:300]
        return self.done


def short(skill):
    """'seo-kit:seo-audit' -> 'seo-audit'; another plugin's skill -> 'other:<name>'; None -> None."""
    if not skill:
        return None
    if skill.startswith(PLUGIN_NAME + ":"):
        return skill.split(":", 1)[1]
    if skill.startswith("seo-") and ":" not in skill:
        return skill
    return "other:" + skill


# --------------------------------------------------------------------------- one run

def run_query(claude, query, plugin_dir, timeout, model=None, max_budget_usd=None, keep_user_settings=False):
    cwd = tempfile.mkdtemp(prefix="seo-kit-trigger-")
    cmd = build_command(claude, query, plugin_dir, model, max_budget_usd, keep_user_settings)
    state = StreamState()
    result = {"status": "ok", "skill": None, "tools": state.tools, "timeout": False, "error": None,
              "exit_code": None, "cwd_removed": False, "seconds": None}
    t0 = time.time()
    timed_out = threading.Event()
    killed = False  # True when we stopped the child, so its exit code says nothing about the session
    proc = None
    stderr_file = tempfile.TemporaryFile()
    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                stderr=stderr_file, cwd=cwd, env=child_env(), **popen_kwargs())

        def on_timeout():
            timed_out.set()
            kill_tree(proc)

        timer = threading.Timer(timeout, on_timeout)
        timer.daemon = True
        timer.start()
        try:
            for raw in proc.stdout:
                if state.feed(raw.decode("utf-8", "replace")):
                    break
            if state.ended_by_result or not state.done:
                # Final result or end of output: let the child exit by itself to read its exit code.
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    pass
        finally:
            timer.cancel()
            if proc.poll() is None:
                killed = True
                kill_tree(proc)
            try:
                proc.stdout.close()
            except OSError:
                pass
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
        killed = killed or timed_out.is_set()
        result["exit_code"] = proc.returncode
    except OSError as exc:
        result["error"] = "%s: %s" % (type(exc).__name__, exc)
    finally:
        result["cwd_removed"] = remove_dir(cwd)
    result["skill"] = state.skill
    result["timeout"] = timed_out.is_set() and not state.skill
    result["seconds"] = round(time.time() - t0, 1)
    if not state.skill and not result["error"]:
        if state.error:
            result["error"] = state.error
        elif not killed and proc is not None and proc.returncode not in (0, None):
            result["error"] = "exit code %s: %s" % (proc.returncode, stderr_tail(stderr_file) or "no output")
    try:
        stderr_file.close()
    except OSError:
        pass
    if result["error"]:
        result["status"] = "error"
    elif result["timeout"]:
        result["status"] = "timeout"
    return result


def stderr_tail(fh, limit=300):
    try:
        fh.seek(0)
        text = fh.read().decode("utf-8", "replace").strip()
    except (OSError, ValueError):
        return ""
    return " ".join(text.split())[-limit:]


# --------------------------------------------------------------------------- summary

def summarise(items, got):
    rows, confusion = [], Counter()
    for i, it in enumerate(items):
        exp = it.get("expected")
        # Failed sessions (auth, rate limit, rejected flag...) say nothing about triggering:
        # they are listed but kept out of the accuracy totals.
        valid = [r for r in got[i] if r.get("status") != "error" and not r.get("error")]
        res = [short(r.get("skill")) for r in valid]
        ok = sum(1 for s in res if s == exp)
        rows.append({"query": it["query"], "expected": exp, "lang": it.get("lang"), "got": res, "ok": ok,
                     "runs": len(res), "timeouts": sum(1 for r in valid if r.get("timeout")),
                     "errors": [r.get("error") or "error" for r in got[i]
                                if r.get("status") == "error" or r.get("error")],
                     "statuses": [r.get("status", "ok") for r in got[i]],
                     "other_tools": [r.get("tools", []) for r in valid]})
        for s in res:
            confusion[(exp or "none", s or "none")] += 1
    return rows, confusion


def markdown(rows, confusion, seconds, meta):
    total_ok = sum(r["ok"] for r in rows)
    total = sum(r["runs"] for r in rows) or 1
    out = ["# Trigger test", "",
           "- Plugin: `%s`" % meta["plugin_dir"],
           "- Queries: %d · runs per query: %d · model: %s · %.0fs"
           % (len(rows), meta["runs"], meta.get("model") or "default", seconds),
           "- **Correct: %d/%d (%.0f%%)**" % (total_ok, sum(r["runs"] for r in rows),
                                              100.0 * total_ok / total)]
    errors = [(r, e) for r in rows for e in r["errors"]]
    out.append("- Errors: %d run(s) failed and are excluded from the totals" % len(errors))
    out.append("")
    by = defaultdict(lambda: [0, 0])
    by_lang = defaultdict(lambda: [0, 0])
    for r in rows:
        key = r["expected"] or "none"
        by[key][0] += r["ok"]
        by[key][1] += r["runs"]
        by_lang[r.get("lang") or "?"][0] += r["ok"]
        by_lang[r.get("lang") or "?"][1] += r["runs"]
    out += ["| Expected | Correct | Runs | % |", "|---|---|---|---|"]
    for k, (a, b) in sorted(by.items()):
        out.append("| %s | %d | %d | %.0f%% |" % (k, a, b, 100.0 * a / (b or 1)))
    out += ["", "| Language | Correct | Runs | % |", "|---|---|---|---|"]
    for k, (a, b) in sorted(by_lang.items()):
        out.append("| %s | %d | %d | %.0f%% |" % (k, a, b, 100.0 * a / (b or 1)))
    wrong = [(k, n) for k, n in sorted(confusion.items()) if k[0] != k[1]]
    if wrong:
        out += ["", "## Confusions", "", "| Expected | Got | Count |", "|---|---|---|"]
        out += ["| %s | %s | %d |" % (e, g, n) for (e, g), n in wrong]
    misses = [r for r in rows if r["ok"] < r["runs"]]
    if misses:
        out += ["", "## Misses", ""]
        for r in misses:
            got = ", ".join(s or "none" for s in r["got"])
            extra = " (timeouts: %d)" % r["timeouts"] if r["timeouts"] else ""
            out.append("- expected **%s**, got %s%s: %s" % (r["expected"] or "none", got, extra, r["query"][:120]))
    if errors:
        out += ["", "## Errors (excluded from the totals)", ""]
        for r, e in errors:
            out.append("- %s: %s" % (r["query"][:80], e))
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- main

def load_items(path, only):
    items = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(items, list) or not all(isinstance(i, dict) and "query" in i for i in items):
        raise ValueError("queries file must be a JSON list of objects with a 'query' key")
    if only:
        keep = {s.strip() for s in only.split(",") if s.strip()}
        items = [i for i in items if (i.get("expected") or "none") in keep]
    return items


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", default=str(DEFAULT_QUERIES), help="queries JSON (default: tools/trigger-queries.json)")
    ap.add_argument("--plugin-dir", default=str(DEFAULT_PLUGIN_DIR), help="plugin under test (default: plugins/seo-kit)")
    ap.add_argument("--runs", type=int, default=2, help="runs per query (default 2)")
    ap.add_argument("--workers", type=int, default=4, help="parallel runs (default 4)")
    ap.add_argument("--timeout", type=float, default=120, help="seconds per run before the process tree is killed")
    ap.add_argument("--max-budget-usd", type=float, help="per-run spending cap passed to claude (default: none)")
    ap.add_argument("--model", help="model for the runs (default: Claude Code's default)")
    ap.add_argument("--only", help="keep queries expected for these skills, comma separated ('none' = negatives)")
    ap.add_argument("--claude", default="claude", help="claude executable (default: 'claude' on PATH)")
    ap.add_argument("--keep-user-settings", action="store_true", help="also load user settings and plugins")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="where the JSON results go (default: tools/trigger-runs/, git-ignored)")
    ap.add_argument("--dry-run", action="store_true", help="print what would run, start nothing")
    args = ap.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (OSError, ValueError):
            pass

    try:
        items = load_items(args.queries, args.only)
    except (OSError, ValueError) as exc:
        print("error: cannot read queries file %s: %s" % (args.queries, exc), file=sys.stderr)
        return 2
    plugin_dir = Path(args.plugin_dir).resolve()
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest.is_file():
        print("error: %s is not a plugin directory (no .claude-plugin/plugin.json)" % plugin_dir, file=sys.stderr)
        return 2
    if args.runs < 1 or args.workers < 1:
        print("error: --runs and --workers must be at least 1", file=sys.stderr)
        return 2

    jobs = [(i, r) for i in range(len(items)) for r in range(args.runs)]
    if args.dry_run:
        print("# Trigger test (dry run)\n")
        print("- Plugin: `%s`" % plugin_dir)
        print("- Queries: %d (%s) · runs per query: %d · total runs: %d · workers: %d · timeout: %ss"
              % (len(items), args.queries, args.runs, len(jobs), args.workers, args.timeout))
        print("- Each run: a new empty temporary folder as cwd, removed afterwards; results would go to %s\n"
              % args.out_dir)
        for i, it in enumerate(items):
            cmd = build_command(args.claude, it["query"], plugin_dir, args.model, args.max_budget_usd,
                                args.keep_user_settings)
            print("%3d. expected %-18s %s" % (i + 1, it.get("expected") or "none", subprocess.list2cmdline(cmd)))
        return 0

    claude = shutil.which(args.claude)
    if not claude:
        print("error: '%s' not found on PATH" % args.claude, file=sys.stderr)
        return 2

    got = defaultdict(list)
    t0 = time.time()
    with ThreadPoolExecutor(args.workers) as ex:
        futs = {ex.submit(run_query, claude, items[i]["query"], plugin_dir, args.timeout, args.model,
                          args.max_budget_usd, args.keep_user_settings): i for i, _ in jobs}
        for n, fut in enumerate(as_completed(futs), 1):
            i = futs[fut]
            try:
                got[i].append(fut.result())
            except Exception as exc:  # noqa: BLE001 - one broken run must not stop the batch
                got[i].append({"status": "error", "skill": None, "tools": [], "timeout": False, "error": str(exc)})
            print("\r%d/%d" % (n, len(jobs)), end="", file=sys.stderr, flush=True)
    print(file=sys.stderr)
    seconds = time.time() - t0

    rows, confusion = summarise(items, got)
    meta = {"plugin_dir": str(plugin_dir), "queries": str(args.queries), "runs": args.runs,
            "model": args.model, "max_budget_usd": args.max_budget_usd, "timeout": args.timeout,
            "keep_user_settings": args.keep_user_settings,
            "started": _dt.datetime.fromtimestamp(t0).isoformat(timespec="seconds"),
            "seconds": round(seconds, 1)}
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (_dt.datetime.fromtimestamp(t0).strftime("%Y%m%d-%H%M%S") + ".json")
    out.write_text(json.dumps({"meta": meta, "rows": rows,
                               "confusion": {"%s -> %s" % k: n for k, n in sorted(confusion.items())}},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    sys.stdout.write(markdown(rows, confusion, seconds, meta))
    print("\nJSON: %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
