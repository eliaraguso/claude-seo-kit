import gzip
import json
import socket
import unittest
import zlib
from unittest import mock

from helpers import FixtureServer, fixture

from seokit import html as seohtml
from seokit import http as seohttp
from seokit import urls


def _closed_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


class UrlTests(unittest.TestCase):
    def test_scheme_required(self):
        with self.assertRaises(urls.InvalidURL) as ctx:
            urls.normalize_url("example.com")
        self.assertIn("http://", str(ctx.exception))
        self.assertIn("https://example.com", str(ctx.exception))

    def test_non_ascii_url_is_encoded(self):  # bug 7
        out = urls.normalize_url("https://bücher.example/über uns/?q=niño#frag")
        self.assertEqual(out, "https://xn--bcher-kva.example/%C3%BCber%20uns/?q=ni%C3%B1o")
        out.encode("ascii")

    def test_existing_escapes_kept(self):
        self.assertEqual(urls.normalize_url("http://a.example/a%20b"), "http://a.example/a%20b")

    def test_compare_key(self):
        self.assertEqual(urls.compare_key("https://A.example:443/x/"), urls.compare_key("https://a.example/x"))
        self.assertEqual(urls.compare_key("https://a.example/"), urls.compare_key("https://a.example"))
        self.assertNotEqual(urls.compare_key("http://a.example/"), urls.compare_key("https://a.example/"))

    def test_site_key(self):
        self.assertEqual(urls.site_key("https://www.a.example/"), urls.site_key("http://a.example:80/x"))
        self.assertNotEqual(urls.site_key("https://blog.a.example/"), urls.site_key("https://a.example/"))


class FetchTests(unittest.TestCase):
    def setUp(self):
        self.sleeps = []
        patcher = mock.patch.object(seohttp, "_sleep", side_effect=self.sleeps.append)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_invalid_url_never_raises(self):
        r = seohttp.fetch("example.com")
        self.assertIsNone(r.status)
        self.assertIn("http://", r.error)

    def test_network_error_never_raises(self):
        r = seohttp.fetch(f"http://127.0.0.1:{_closed_port()}/", timeout=5, retries=0)
        self.assertIsNone(r.status)
        self.assertTrue(r.error)

    def test_redirect_chain_records_location(self):
        with FixtureServer() as srv:
            srv.add("/a", status=301, headers=[("Location", "/b")])
            srv.add("/b", status=302, headers=[("Location", srv.url("/c"))])
            srv.add("/c", "<p>done</p>")
            r = seohttp.fetch(srv.url("/a"))
        self.assertEqual(r.status, 200)
        self.assertEqual(r.final_url, srv.url("/c"))
        self.assertEqual([h["status"] for h in r.chain], [301, 302, 200])
        self.assertEqual(r.chain[0]["location"], srv.url("/b"))
        self.assertIsNone(r.chain[-1]["location"])

    def test_redirect_cap(self):
        with FixtureServer() as srv:
            for i in range(15):
                srv.add(f"/r{i}", status=302, headers=[("Location", f"/r{i + 1}")])
            r = seohttp.fetch(srv.url("/r0"))
        self.assertIn("too many redirects", r.error)
        self.assertEqual(len(r.chain), 11)

    def test_non_ascii_location_header(self):  # bug 7
        with FixtureServer() as srv:
            srv.add("/old", status=301, headers=[("Location", "/über/".encode("utf-8"))])
            srv.add("/%C3%BCber/", "<p>ok</p>")
            r = seohttp.fetch(srv.url("/old"))
        self.assertIsNone(r.error)
        self.assertEqual(r.status, 200)
        self.assertTrue(r.final_url.endswith("/%C3%BCber/"))

    def test_non_ascii_request_url(self):  # bug 7
        with FixtureServer() as srv:
            srv.add("/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/?q=%C3%B1", "<p>ok</p>")
            r = seohttp.fetch(srv.url("/контакты/?q=ñ"))
        self.assertEqual(r.status, 200, r.error)

    def test_gzip(self):
        with FixtureServer() as srv:
            srv.add("/", gzip.compress(b"<p>zipped</p>"), headers=[("Content-Encoding", "gzip")])
            r = seohttp.fetch(srv.url("/"))
        self.assertEqual(r.text, "<p>zipped</p>")
        self.assertLess(r.transfer_bytes, 40)

    def test_deflate_raw_and_zlib(self):  # bug 8
        raw = zlib.compressobj(wbits=-15)
        raw_body = raw.compress(b"<p>raw deflate</p>") + raw.flush()
        with FixtureServer() as srv:
            srv.add("/raw", raw_body, headers=[("Content-Encoding", "deflate")])
            srv.add("/zlib", zlib.compress(b"<p>zlib deflate</p>"), headers=[("Content-Encoding", "deflate")])
            r1 = seohttp.fetch(srv.url("/raw"))
            r2 = seohttp.fetch(srv.url("/zlib"))
        self.assertEqual(r1.text, "<p>raw deflate</p>")
        self.assertEqual(r2.text, "<p>zlib deflate</p>")

    def test_unknown_charset_does_not_raise(self):  # bug 6
        with FixtureServer() as srv:
            srv.add("/", "<p>caffè</p>", content_type="text/html; charset=x-klingon")
            r = seohttp.fetch(srv.url("/"))
        self.assertIsNone(r.error)
        self.assertEqual(r.text, "<p>caffè</p>")
        self.assertEqual(r.encoding_source, "fallback")
        self.assertTrue(any("x-klingon" in w for w in r.warnings))

    def test_charset_from_meta(self):
        body = fixture("html", "charset_meta_latin1.html").read_bytes()
        with FixtureServer() as srv:
            srv.add("/", body, content_type="text/html")
            r = seohttp.fetch(srv.url("/"))
        self.assertEqual(r.encoding_source, "meta")
        self.assertIn("perché", r.text)
        self.assertIn("Città", r.text)

    def test_charset_order(self):
        text, enc, src, _ = seohttp.decode_text("é".encode("utf-8"), "text/html; charset=utf-8")
        self.assertEqual((text, src), ("é", "header"))
        text, enc, src, _ = seohttp.decode_text(b"\xef\xbb\xbfhello", "text/html")
        self.assertEqual((text, src), ("hello", "bom"))
        text, enc, src, warns = seohttp.decode_text("é".encode("latin-1"), "")
        self.assertEqual((text, enc, src), ("é", "latin-1", "fallback"))
        self.assertTrue(warns)

    def test_max_bytes_truncates(self):
        with FixtureServer() as srv:
            srv.add("/", b"x" * 5000)
            r = seohttp.fetch(srv.url("/"), max_bytes=1000)
        self.assertTrue(r.truncated)
        self.assertEqual(len(r.body), 1000)

    def test_retry_after_honoured(self):
        calls = {"n": 0}

        def flaky(handler):
            calls["n"] += 1
            if calls["n"] == 1:
                return 429, [("Retry-After", "3")], b"slow down"
            return 200, [("Content-Type", "text/plain")], b"ok"

        with FixtureServer({"/": flaky}) as srv:
            r = seohttp.fetch(srv.url("/"))
        self.assertEqual(r.status, 200)
        self.assertEqual(calls["n"], 2)
        self.assertEqual(self.sleeps, [3.0])

    def test_retries_exhausted_returns_last_status(self):
        with FixtureServer() as srv:
            srv.add("/", "busy", status=503)
            r = seohttp.fetch(srv.url("/"), retries=2)
        self.assertEqual(r.status, 503)
        self.assertEqual(len(self.sleeps), 2)

    def test_accept_language_only_when_lang_given(self):  # bug 18
        with FixtureServer() as srv:
            srv.add("/", "<p>x</p>")
            seohttp.fetch(srv.url("/"), ua="googlebot")
            seohttp.fetch(srv.url("/"), ua="browser", lang="de-AT")
            first, second = srv.requests
        self.assertNotIn("Accept-Language", first["headers"])
        self.assertIn("Googlebot", first["headers"]["User-Agent"])
        self.assertEqual(second["headers"]["Accept-Language"], "de-AT,de;q=0.9")

    def test_multiple_x_robots_tag_headers(self):  # bug 9
        spec = json.loads(fixture("headers", "multi_x_robots.json").read_text(encoding="utf-8"))
        with FixtureServer() as srv:
            srv.add("/", "<title>x</title>", status=spec["status"], headers=[tuple(h) for h in spec["headers"]])
            r = seohttp.fetch(srv.url("/"))
        values = r.headers.get_all("x-robots-tag")
        self.assertEqual(len(values), 3)
        page = seohtml.parse_page(r.text, r.final_url, r.headers, r.status)
        self.assertEqual(page["x_robots_tag"], values)
        self.assertFalse(page["indexable"]["value"])
        self.assertIn("noindex in X-Robots-Tag for googlebot", page["indexable"]["reasons"])

    def test_throttle_waits_between_requests(self):
        with FixtureServer() as srv:
            srv.add("/", "ok")
            t = seohttp.Throttle(delay=5)
            t(srv.url("/"))
            t(srv.url("/"))
        self.assertEqual(len(self.sleeps), 1)
        self.assertGreater(self.sleeps[0], 4)


if __name__ == "__main__":
    unittest.main()
