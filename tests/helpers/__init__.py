"""Shared test helpers: paths, a local fixture HTTP server, script runner."""
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PLUGIN = REPO / "plugins" / "seo-kit"
LIB = PLUGIN / "lib"
FIXTURES = REPO / "tests" / "fixtures"
SCRIPTS = {
    "seo_fetch": PLUGIN / "skills" / "seo-audit" / "scripts" / "seo_fetch.py",
    "extract_dom": PLUGIN / "skills" / "seo-audit" / "scripts" / "extract_dom.js",
    "check_build": PLUGIN / "skills" / "seo-build" / "scripts" / "check_build.py",
    "suggest": PLUGIN / "skills" / "seo-discovery" / "scripts" / "suggest.py",
    "analyze_gsc": PLUGIN / "skills" / "seo-monitor" / "scripts" / "analyze_gsc.py",
}

if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))


def fixture(*parts) -> Path:
    return FIXTURES.joinpath(*parts)


def fixture_text(*parts) -> str:
    return fixture(*parts).read_text(encoding="utf-8")


def load_script(name):
    """Import a CLI script as a module (without running main)."""
    import importlib.util
    path = SCRIPTS[name]
    spec = importlib.util.spec_from_file_location(f"seokit_script_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_script(name, *args, timeout=180, cwd=None):
    """Run a CLI script with the current interpreter; returns CompletedProcess (text)."""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    return subprocess.run(
        [sys.executable, str(SCRIPTS[name]), *[str(a) for a in args]],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        timeout=timeout, env=env, cwd=cwd,
    )


class FixtureServer:
    """Threaded HTTP server on 127.0.0.1 with a random port.

    routes: {path_with_query: (status, [(header, value)], body_bytes)} or a callable
    taking the handler and returning that tuple. Unknown paths answer 404.
    Header values that are bytes are written raw (to send non-ASCII Location headers).
    """

    def __init__(self, routes=None):
        self.routes = dict(routes or {})
        self.requests = []

    def add(self, path, body=b"", status=200, headers=None, content_type="text/html; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        hdrs = list(headers or [])
        if content_type and not any(k.lower() == "content-type" for k, _ in hdrs):
            hdrs.insert(0, ("Content-Type", content_type))
        self.routes[path] = (status, hdrs, body)

    def url(self, path="/"):
        return f"http://127.0.0.1:{self.port}{path}"

    def __enter__(self):
        server = self

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.0"

            def log_message(self, *args):  # silence
                pass

            def do_GET(self):
                server.requests.append({"path": self.path, "headers": dict(self.headers.items())})
                route = server.routes.get(self.path)
                if callable(route):
                    route = route(self)
                if route is None:
                    route = (404, [("Content-Type", "text/html")], b"<h1>Not found</h1>")
                status, headers, body = route
                self.send_response_only(status)
                for key, value in headers:
                    if isinstance(value, bytes):
                        self._headers_buffer.append(key.encode("latin-1") + b": " + value + b"\r\n")
                    else:
                        self.send_header(key, value)
                if not any(k.lower() == "content-length" for k, _ in headers):
                    self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.httpd.daemon_threads = True
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.httpd.shutdown()
        self.httpd.server_close()
        return False
