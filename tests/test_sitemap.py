import gzip
import os
import tempfile
import unittest
from unittest import mock

from helpers import FixtureServer, fixture

from seokit import http as seohttp
from seokit import sitemap

XML = "application/xml"


def serve_fixtures(srv):
    for name in ("child_ok.xml", "child_broken.xml", "old_namespace.xml", "with_xhtml_links.xml"):
        srv.add(f"/{name}", fixture("sitemaps", name).read_bytes(), content_type=XML)
    index = fixture("sitemaps", "index.xml").read_text(encoding="utf-8").replace("{base}", srv.url("").rstrip("/"))
    srv.add("/index.xml", index, content_type=XML)
    # urlset.xml.gz is generated here from urlset.xml and served WITHOUT Content-Encoding.
    with tempfile.TemporaryDirectory() as tmp:
        gz_path = os.path.join(tmp, "urlset.xml.gz")
        with gzip.open(gz_path, "wb") as fh:
            fh.write(fixture("sitemaps", "urlset.xml").read_bytes())
        with open(gz_path, "rb") as fh:
            srv.add("/urlset.xml.gz", fh.read(), content_type="application/octet-stream")


class SitemapTests(unittest.TestCase):
    def test_index_children_and_errors(self):  # bug 16
        with FixtureServer() as srv:
            serve_fixtures(srv)
            res = sitemap.load(srv.url("/index.xml"), seohttp.fetch)
        locs = [u["loc"] for u in res["urls"]]
        # gzip detected by magic bytes, siblings read despite the broken and missing children
        for loc in ("https://acme-widgets.example/gz-1", "https://acme-widgets.example/widgets/blue",
                    "https://acme-widgets.example/old", "https://acme-widgets.example/en/",
                    "https://acme-widgets.example/broken-1"):
            self.assertIn(loc, locs)
        by_url = {s["url"].rsplit("/", 1)[-1]: s for s in res["sitemaps"]}
        self.assertEqual(by_url["index.xml"]["type"], "sitemapindex")
        self.assertEqual(by_url["index.xml"]["children"], 6)
        self.assertTrue(by_url["urlset.xml.gz"]["gzipped"])
        self.assertEqual(by_url["missing.xml"]["error"], "HTTP 404")
        self.assertTrue(by_url["child_broken.xml"]["error"].startswith("XML parse error"))
        self.assertEqual({e["url"].rsplit("/", 1)[-1] for e in res["errors"]}, {"missing.xml"})
        self.assertTrue(any("0.84" in w for w in res["warnings"]))
        self.assertFalse(res["truncated"])
        self.assertEqual(res["url_count"], len(res["urls"]))

    def test_details_extracted(self):
        with FixtureServer() as srv:
            serve_fixtures(srv)
            res = sitemap.load(srv.url("/child_ok.xml"), seohttp.fetch)
            alt = sitemap.load(srv.url("/with_xhtml_links.xml"), seohttp.fetch)
        blue = [u for u in res["urls"] if u["loc"].endswith("/blue")][0]
        self.assertEqual((blue["images"], blue["videos"]), (2, 1))
        self.assertEqual(res["urls"][0]["lastmod"], "2026-10-01")
        # the sitemap is served from 127.0.0.1, so every acme URL is a host mismatch
        self.assertEqual(res["host_mismatch_count"], 3)
        en = alt["urls"][0]
        self.assertEqual([a["hreflang"] for a in en["alternates"]], ["en", "de"])
        self.assertEqual(alt["urls"][1]["loc"], "https://acme-widgets.example/de/ü-straße")

    def test_host_mismatch_ignores_www(self):
        body = (b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                b"<url><loc>https://www.acme-widgets.example/a</loc></url>"
                b"<url><loc>https://other.example/b</loc></url></urlset>")
        fake = mock.Mock(return_value=mock.Mock(status=200, body=body, error=None, truncated=False))
        res = sitemap.load("https://acme-widgets.example/sitemap.xml", fake)
        self.assertEqual(res["host_mismatch"], ["https://other.example/b"])

    def test_limits_set_truncated(self):
        with FixtureServer() as srv:
            serve_fixtures(srv)
            res = sitemap.load(srv.url("/index.xml"), seohttp.fetch, max_sitemaps=3)
            res_urls = sitemap.load(srv.url("/child_ok.xml"), seohttp.fetch, max_urls=1)
            res_depth = sitemap.load(srv.url("/index.xml"), seohttp.fetch, max_depth=0)
        self.assertTrue(res["truncated"])
        self.assertEqual(len(res["sitemaps"]), 3)
        self.assertTrue(res_urls["truncated"])
        self.assertEqual(res_urls["url_count"], 1)
        self.assertTrue(res_depth["truncated"])
        self.assertEqual(res_depth["url_count"], 0)

    def test_fetch_exception_does_not_abort(self):
        def boom(url):
            raise RuntimeError("socket exploded")
        res = sitemap.load("https://acme-widgets.example/sitemap.xml", boom)
        self.assertIn("socket exploded", res["errors"][0]["error"])

    def test_too_many_urls_warning(self):
        entries = b"".join(b"<url><loc>https://a.example/%d</loc></url>" % i for i in range(50_001))
        body = b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + entries + b"</urlset>"
        fake = mock.Mock(return_value=mock.Mock(status=200, body=body, error=None, truncated=False))
        res = sitemap.load("https://a.example/sitemap.xml", fake)
        self.assertTrue(any("50,000" in w for w in res["warnings"]))

    def test_not_a_sitemap(self):
        fake = mock.Mock(return_value=mock.Mock(status=200, body=b"<html><body>hi</body></html>",
                                                error=None, truncated=False))
        res = sitemap.load("https://a.example/sitemap.xml", fake)
        self.assertIn("not a sitemap", res["errors"][0]["error"])


if __name__ == "__main__":
    unittest.main()
