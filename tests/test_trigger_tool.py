"""Tests for tools/trigger_test.py without calling the real Claude: stream parsing, the
dry run, and end-to-end runs against a fake `claude` executable put first on PATH.

Run:  python -m unittest tests.test_trigger_tool -v
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TOOL = REPO / "tools" / "trigger_test.py"
sys.path.insert(0, str(REPO / "tools"))

import trigger_test as tt  # noqa: E402

FAKE_CLAUDE = textwrap.dedent(r'''
    import json, os, subprocess, sys, time

    argv = sys.argv[1:]
    query = argv[argv.index("-p") + 1] if "-p" in argv else ""
    entry = {"argv": argv, "cwd": os.getcwd()}
    if "hang" in query:
        child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
        entry["grandchild"] = child.pid
    # One file per process: concurrent appends to one file can lose lines on Windows.
    log_file = os.path.join(os.environ["FAKE_CLAUDE_LOG"], "%d.json" % os.getpid())
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(entry, f)

    def emit(ev):
        print(json.dumps(ev), flush=True)

    emit({"type": "system", "subtype": "init"})
    if "audit" in query:
        emit({"type": "stream_event", "event": {"type": "content_block_start", "index": 0,
              "content_block": {"type": "tool_use", "name": "Skill", "input": {}}}})
        for part in ['{"skill": "seo-kit:', 'seo-audit"}']:
            emit({"type": "stream_event", "event": {"type": "content_block_delta", "index": 0,
                  "delta": {"type": "input_json_delta", "partial_json": part}}})
        emit({"type": "stream_event", "event": {"type": "content_block_stop", "index": 0}})
        time.sleep(30)  # the tool must stop us as soon as it has seen the Skill call
    elif "content" in query:
        emit({"type": "assistant", "message": {"content": [
            {"type": "tool_use", "name": "Skill", "input": {"skill": "seo-kit:seo-content"}}]}})
        time.sleep(30)
    elif "hang" in query:
        time.sleep(60)
    elif "badkey" in query:
        emit({"type": "result", "subtype": "success", "is_error": True, "result": "Invalid API key"})
        sys.exit(1)
    elif "crash" in query:
        sys.stderr.write("error: unknown option '--bogus'\n")
        sys.exit(2)
    else:
        emit({"type": "result", "subtype": "success", "result": "Nothing to do with SEO."})
''')


def install_fake_claude(bin_dir):
    script = bin_dir / "fake_claude.py"
    script.write_text(FAKE_CLAUDE, encoding="utf-8")
    if os.name == "nt":
        (bin_dir / "claude.cmd").write_text(
            '@echo off\r\n"%s" "%s" %%*\r\n' % (sys.executable, script), encoding="utf-8")
    else:
        exe = bin_dir / "claude"
        exe.write_text("#!%s\n%s" % (sys.executable, FAKE_CLAUDE), encoding="utf-8")
        exe.chmod(0o755)


def alive(pid):
    if os.name == "nt":
        out = subprocess.run(["tasklist", "/FI", "PID eq %d" % pid, "/NH"],
                             capture_output=True, text=True).stdout
        return str(pid) in out
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    stat = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return bool(stat) and not stat.startswith("Z")


class StreamParsing(unittest.TestCase):
    def feed(self, events):
        st = tt.StreamState()
        for ev in events:
            if st.feed(json.dumps(ev) + "\n"):
                break
        return st

    def test_partial_messages_skill(self):
        st = self.feed([
            {"type": "stream_event", "event": {"type": "content_block_start",
                                               "content_block": {"type": "tool_use", "name": "Skill"}}},
            {"type": "stream_event", "event": {"type": "content_block_delta",
                                               "delta": {"partial_json": '{"skill": "seo-kit:seo-build"}'}}},
            {"type": "stream_event", "event": {"type": "content_block_stop"}},
        ])
        self.assertTrue(st.done)
        self.assertEqual(st.skill, "seo-kit:seo-build")

    def test_full_assistant_message_skill(self):
        st = self.feed([{"type": "assistant", "message": {"content": [
            {"type": "text", "text": "Let me check."},
            {"type": "tool_use", "name": "Skill", "input": {"skill": "seo-kit:seo-monitor"}}]}}])
        self.assertEqual(st.skill, "seo-kit:seo-monitor")

    def test_other_tools_stop_after_limit(self):
        events = []
        for name in ["Read", "Glob", "Grep", "Read"]:
            events.append({"type": "assistant", "message": {"content": [
                {"type": "tool_use", "name": name, "input": {}}]}})
        st = self.feed(events)
        self.assertTrue(st.done)
        self.assertIsNone(st.skill)
        self.assertEqual(st.tools, ["Read", "Glob", "Grep"])

    def test_result_ends_and_garbage_is_ignored(self):
        st = tt.StreamState()
        self.assertFalse(st.feed("not json\n"))
        self.assertFalse(st.feed("[1, 2]\n"))
        self.assertTrue(st.feed(json.dumps({"type": "result"})))
        self.assertIsNone(st.skill)

    def test_error_result_is_recorded(self):
        st = tt.StreamState()
        self.assertTrue(st.feed(json.dumps({"type": "result", "subtype": "success", "is_error": True,
                                            "result": "Invalid API key"})))
        self.assertIn("Invalid API key", st.error)
        st = tt.StreamState()
        st.feed(json.dumps({"type": "result", "subtype": "error_max_turns"}))
        self.assertTrue(st.error.startswith("error_max_turns"))
        st = tt.StreamState()
        st.feed(json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": "ok"}))
        self.assertIsNone(st.error)

    def test_short(self):
        self.assertEqual(tt.short("seo-kit:seo-audit"), "seo-audit")
        self.assertEqual(tt.short("seo-content"), "seo-content")
        self.assertEqual(tt.short("other-plugin:thing"), "other:other-plugin:thing")
        self.assertIsNone(tt.short(None))

    def test_build_command(self):
        cmd = tt.build_command("claude", "why is my site not on Google", Path("/p/seo-kit"), model="sonnet")
        self.assertEqual(cmd[:3], ["claude", "-p", "why is my site not on Google"])
        self.assertEqual(cmd[cmd.index("--plugin-dir") + 1], str(Path("/p/seo-kit")))
        self.assertIn("stream-json", cmd)
        self.assertEqual(cmd[cmd.index("--setting-sources") + 1], "project,local")
        self.assertEqual(cmd[cmd.index("--model") + 1], "sonnet")
        keep = tt.build_command("claude", "q", Path("/p"), keep_user_settings=True, max_budget_usd=0.5)
        self.assertNotIn("--setting-sources", keep)
        self.assertEqual(keep[keep.index("--max-budget-usd") + 1], "0.5")

    def test_cmd_shim_unsafe_queries(self):
        qs = ["why is my site not on Google", "50% off & free", 'say "hi"']
        self.assertEqual(tt.cmd_shim_unsafe("C:/npm/claude.CMD", qs), qs[1:])
        self.assertEqual(tt.cmd_shim_unsafe("C:/npm/claude.bat", qs[:1]), [])
        self.assertEqual(tt.cmd_shim_unsafe("/usr/local/bin/claude", qs), [])
        self.assertEqual(tt.cmd_shim_unsafe("C:/bin/claude.exe", qs), [])


class Cli(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="trigger-tool-test-"))
        self.queries = self.tmp / "queries.json"
        self.queries.write_text(json.dumps([
            {"query": "please audit my site", "expected": "seo-audit", "lang": "en"},
            {"query": "write the content of the page", "expected": "seo-content", "lang": "en"},
            {"query": "fix the login bug", "expected": None, "lang": "en"},
            {"query": "hang forever", "expected": "seo-monitor", "lang": "en"},
        ]), encoding="utf-8")
        self.out_dir = self.tmp / "runs"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_tool(self, *args, env=None, timeout=120):
        return subprocess.run([sys.executable, str(TOOL), "--queries", str(self.queries),
                               "--out-dir", str(self.out_dir), *args],
                              capture_output=True, text=True, encoding="utf-8", env=env, timeout=timeout)

    def test_dry_run_starts_nothing(self):
        res = self.run_tool("--dry-run", "--runs", "2")
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("total runs: 8", res.stdout)
        self.assertIn("--plugin-dir", res.stdout)
        self.assertIn(str(REPO / "plugins" / "seo-kit"), res.stdout)
        self.assertIn("please audit my site", res.stdout)
        self.assertFalse(self.out_dir.exists())

    def test_usage_errors(self):
        res = self.run_tool("--plugin-dir", str(self.tmp))
        self.assertEqual(res.returncode, 2)
        self.assertIn("not a plugin directory", res.stderr)
        res = subprocess.run([sys.executable, str(TOOL), "--queries", str(self.tmp / "missing.json"), "--dry-run"],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 2)

    def fake_env(self):
        bin_dir = self.tmp / "bin"
        bin_dir.mkdir()
        install_fake_claude(bin_dir)
        log = self.tmp / "fake-claude-log"
        log.mkdir()
        env = dict(os.environ)
        env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
        env["FAKE_CLAUDE_LOG"] = str(log)
        return env, log

    def test_failed_sessions_are_errors_not_misses(self):
        self.queries.write_text(json.dumps([
            {"query": "please audit my site", "expected": "seo-audit", "lang": "en"},
            {"query": "badkey session", "expected": None, "lang": "en"},
            {"query": "crash on start", "expected": "seo-build", "lang": "en"},
        ]), encoding="utf-8")
        env, _ = self.fake_env()
        res = self.run_tool("--runs", "1", "--timeout", "10", env=env)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        # Only the audit run counts; the two failed sessions are excluded and listed.
        self.assertIn("Correct: 1/1", res.stdout)
        self.assertIn("Errors: 2 run(s) failed", res.stdout)
        self.assertIn("Invalid API key", res.stdout)
        self.assertIn("exit code 2", res.stdout)
        self.assertIn("unknown option", res.stdout)
        data = json.loads(next(self.out_dir.glob("*.json")).read_text(encoding="utf-8"))
        by_query = {r["query"]: r for r in data["rows"]}
        self.assertEqual(by_query["badkey session"]["statuses"], ["error"])
        self.assertEqual(by_query["badkey session"]["runs"], 0)
        self.assertEqual(by_query["badkey session"]["ok"], 0)
        self.assertEqual(by_query["crash on start"]["statuses"], ["error"])
        self.assertEqual(by_query["please audit my site"]["statuses"], ["ok"])

    def test_runs_against_fake_claude(self):
        env, log = self.fake_env()
        t0 = time.time()
        res = self.run_tool("--runs", "1", "--workers", "4", "--timeout", "4", env=env)
        elapsed = time.time() - t0
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertLess(elapsed, 25, "runs were not stopped early")

        # Markdown summary on stdout, JSON results in the out dir.
        self.assertIn("# Trigger test", res.stdout)
        self.assertIn("Correct: 3/4", res.stdout)
        files = list(self.out_dir.glob("*.json"))
        self.assertEqual(len(files), 1)
        data = json.loads(files[0].read_text(encoding="utf-8"))
        by_query = {r["query"]: r for r in data["rows"]}
        self.assertEqual(by_query["please audit my site"]["got"], ["seo-audit"])
        self.assertEqual(by_query["write the content of the page"]["got"], ["seo-content"])
        self.assertEqual(by_query["fix the login bug"]["got"], [None])
        self.assertEqual(by_query["fix the login bug"]["ok"], 1)
        self.assertEqual(by_query["hang forever"]["got"], [None])
        self.assertEqual(by_query["hang forever"]["timeouts"], 1)

        # Every run got --plugin-dir and its own temporary cwd, removed afterwards.
        entries = [json.loads(f.read_text(encoding="utf-8")) for f in sorted(log.glob("*.json"))]
        self.assertEqual(len(entries), 4)
        cwds = {e["cwd"] for e in entries}
        self.assertEqual(len(cwds), 4)
        for e in entries:
            argv = e["argv"]
            self.assertEqual(Path(argv[argv.index("--plugin-dir") + 1]), (REPO / "plugins" / "seo-kit").resolve())
            self.assertFalse(os.path.exists(e["cwd"]), "temporary cwd not removed: %s" % e["cwd"])

        # The timeout killed the whole process tree, grandchild included.
        grandchild = next(e["grandchild"] for e in entries if "grandchild" in e)
        deadline = time.time() + 10
        while alive(grandchild) and time.time() < deadline:
            time.sleep(0.2)
        self.assertFalse(alive(grandchild), "grandchild %d survived the timeout" % grandchild)


if __name__ == "__main__":
    unittest.main()
