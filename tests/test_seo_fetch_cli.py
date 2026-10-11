import json
import os
import socket
import tempfile
import unittest

from helpers import FixtureServer, load_script, run_script

from seokit import http as seohttp

FILLER = ("Northwind Physio is a physiotherapy clinic in Oslo. We treat back pain and sports injuries "
          "with exercise plans built for each patient. ") * 4

HOME = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Physiotherapy in Oslo | Northwind Physio</title>
<meta name="description" content="Physiotherapy in Oslo.">
<link rel="canonical" href="/">
<script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head><body><h1>Physio Oslo clinic</h1><p>{FILLER} See teh prices.</p>
<div class="g-recaptcha" data-sitekey="x"></div>
<a href="/about/">About</a><a href="/private/page">Private</a></body></html>"""

ABOUT = f"""<html lang="en"><head><title>Same title</title><meta name="description" content="About us">
</head><body><h1>About</h1><p>{FILLER}</p></body></html>"""
DUP = ABOUT.replace("About us", "Duplicate page")
NOINDEX = """<html lang="en"><head><title>Same title</title><meta name="robots" content="noindex"></head>
<body><h1>Hidden</h1></body></html>"""
NO_LANG = "<html><head><title>No language</title></head><body><p>Perchè no? Un pò.</p></body></html>"


def closed_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def site(srv, challenge_for_googlebot=False):
    def home(handler):
        ua = handler.headers.get("User-Agent", "")
        if challenge_for_googlebot and "Googlebot" in ua:
            return 403, [("Content-Type", "text/html")], b"<title>Just a moment...</title><div id=cf-challenge></div>"
        return 200, [("Content-Type", "text/html; charset=utf-8")], HOME.encode("utf-8")

    srv.routes["/"] = home
    srv.add("/about/", ABOUT)
    srv.add("/dup/", DUP)
    srv.add("/noindex/", NOINDEX)
    srv.add("/nolang/", NO_LANG)
    srv.add("/private/page", ABOUT.replace("Same title", "Private"))
    srv.add("/robots.txt", "\ufeffUser-agent: *\nDisallow: /private/\n\nUser-agent: GPTBot\nDisallow: /\n\n"
                           f"Sitemap: {srv.url('/sitemap.xml')}\n", content_type="text/plain")
    locs = "".join(f"<url><loc>{srv.url(p)}</loc></url>" for p in ("/", "/about/", "/dup/", "/noindex/",
                                                                     "/private/page"))
    srv.add("/sitemap.xml", f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{locs}</urlset>',
            content_type="application/xml")


class SeoFetchCliTests(unittest.TestCase):
    def run_json(self, *args):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "out.json")
            proc = run_script("seo_fetch", *args, "--delay", "0", "--timeout", "5", "--json", path)
            data = None
            if os.path.exists(path):
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
        return proc, data

    def test_invalid_url_exit_2(self):
        proc = run_script("seo_fetch", "northwind-physio.example")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("http://", proc.stderr)

    def test_malformed_url_exit_2(self):  # review fix: was a traceback with exit 1
        proc = run_script("seo_fetch", "http://[::1")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("Invalid IPv6 URL", proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)

    def test_unreachable_exit_2(self):
        proc, data = self.run_json(f"http://127.0.0.1:{closed_port()}/")
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertIn("unreachable", proc.stderr)
        self.assertIsNotNone(data["pages"][0]["error"])

    def test_full_run(self):
        with FixtureServer() as srv:
            site(srv)
            proc, data = self.run_json(srv.url("/"), "--sitemap", "10", "--max-pages", "4",
                                       "--terms", "physio oslo;Back Pain;therapy", "--lang", "de")
            requests = list(srv.requests)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        site_data = data["site"]
        # robots: BOM handled, rules evaluated per crawler and per page (bugs 3, 14)
        robots_info = site_data["robots"]
        self.assertEqual(robots_info["status_semantics"], "parse")
        self.assertEqual(len(robots_info["groups"]), 2)
        self.assertTrue(robots_info["verdicts_root"]["Googlebot"])
        self.assertFalse(robots_info["verdicts_root"]["GPTBot"])
        # sitemap
        self.assertEqual(site_data["sitemaps"]["total_urls"], 5)
        self.assertTrue(site_data["sitemaps"]["sitemaps"][0]["declared_in_robots"])
        # host variants include https://host (bug 15)
        variant_urls = [v["url"] for v in site_data["host_variants"]["variants"]]
        self.assertIn(srv.url("/").replace("http://", "https://"), variant_urls)
        # 404 probe
        self.assertEqual(site_data["not_found_probe"]["verdict"], "ok")
        self.assertFalse(site_data["dns"]["nameservers"]["available"])
        # UA comparison: g-recaptcha is not a challenge page (bug 17)
        ua = site_data["ua_comparison"]
        self.assertEqual(set(ua["results"]), {"browser", "googlebot", "bingbot", "oai-searchbot",
                                              "claude-searchbot", "perplexitybot"})
        self.assertTrue(all(not r["challenge_markers"] for r in ua["results"].values()))
        self.assertEqual(ua["differences"], [])
        # pages: max-pages respected, sitemap URLs appended
        finals = [p["final_url"] for p in data["pages"]]
        self.assertEqual(finals, [srv.url("/"), srv.url("/about/"), srv.url("/dup/"), srv.url("/noindex/")])
        self.assertTrue(any("--max-pages" in w for w in data["warnings"]))
        home = data["pages"][0]
        self.assertTrue(home["canonical"]["self_referencing"])
        self.assertTrue(home["robots_txt_allowed"]["Googlebot"])
        self.assertFalse(home["robots_txt_allowed"]["GPTBot"])
        # --lang de: no German pack, so no typo check even if the page is English (bug 4)
        self.assertNotIn("typo_suspects", home)
        cov = home["term_coverage"]
        self.assertTrue(cov["physio oslo"]["in_h1"])
        self.assertEqual(cov["Back Pain"]["text_count"], 4)  # FILLER repeated 4 times
        self.assertEqual(cov["therapy"]["text_count"], 0)  # inside "physiotherapy": not a word match
        self.assertEqual(data["term_coverage"]["physio oslo"], [srv.url("/")])
        # duplicates exclude noindex pages
        self.assertEqual(data["duplicates"]["title"], {"Same title": [srv.url("/about/"), srv.url("/dup/")]})
        # Accept-Language only for the browser UA (bug 18)
        for req in requests:
            ua_header = req["headers"].get("User-Agent", "")
            if "Googlebot" in ua_header or "bingbot" in ua_header:
                self.assertNotIn("Accept-Language", req["headers"])
        self.assertTrue(any(r["headers"].get("Accept-Language") == "de" for r in requests))

    def test_robots_blocked_page_and_typos(self):
        with FixtureServer() as srv:
            site(srv)
            proc, data = self.run_json(srv.url("/private/page"), srv.url("/nolang/"), srv.url("/"),
                                       "--no-ua", "--full-text")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        private, nolang, home = data["pages"]
        self.assertFalse(private["robots_txt_allowed"]["Googlebot"])
        self.assertFalse(private["indexable"]["value"])
        self.assertNotIn("typo_suspects", nolang)  # no lang and no --lang: no pack applies
        self.assertEqual([t["match"] for t in home["typo_suspects"]], ["teh"])
        self.assertNotIn("ua_comparison", data["site"])

    def test_challenge_page_detected(self):
        with FixtureServer() as srv:
            site(srv, challenge_for_googlebot=True)
            proc, data = self.run_json(srv.url("/"), "--no-site")
        ua = data["site"]["ua_comparison"]
        self.assertEqual(ua["results"]["googlebot"]["status"], 403)
        self.assertIn("cf-challenge", ua["results"]["googlebot"]["challenge_markers"])
        self.assertTrue(any(d.startswith("googlebot: HTTP 403") for d in ua["differences"]))
        self.assertNotIn("robots", data["site"])

    def test_stdout_json_and_lang_it(self):
        with FixtureServer() as srv:
            site(srv)
            proc = run_script("seo_fetch", srv.url("/nolang/"), "--no-site", "--no-ua", "--lang", "it",
                              "--delay", "0")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        matches = sorted(t["match"] for t in data["pages"][0]["typo_suspects"])
        self.assertEqual(matches, ["Perchè", "pò"])


class HostVariantTests(unittest.TestCase):
    def test_four_variants_for_a_domain(self):  # bug 15
        mod = load_script("seo_fetch")
        seen = []

        def fake_fetch(url, **kw):
            seen.append(url)
            r = seohttp.Response(url=url, final_url="https://northwind-physio.example/", status=200)
            r.chain = [{"url": url, "status": 301, "location": "https://northwind-physio.example/"},
                       {"url": "https://northwind-physio.example/", "status": 200, "location": None}]
            if url == "https://northwind-physio.example/":
                r.chain = r.chain[1:]
            return r

        res = mod.check_host_variants("https://www.northwind-physio.example", fake_fetch)
        self.assertEqual(seen, ["https://northwind-physio.example/", "http://northwind-physio.example/",
                                "https://www.northwind-physio.example/", "http://www.northwind-physio.example/"])
        self.assertTrue(res["all_reach_same_final_url"])
        self.assertEqual(res["variants"][0]["hops"], 0)
        self.assertEqual(res["variants"][1]["hops"], 1)


    def test_subdomain_gets_no_www_variants(self):  # review minor
        mod = load_script("seo_fetch")
        seen = []

        def fake_fetch(url, **kw):
            seen.append(url)
            return seohttp.Response(url=url, final_url=url, status=200)

        mod.check_host_variants("https://shop.northwind-physio.example", fake_fetch)
        self.assertEqual(seen, ["https://shop.northwind-physio.example/", "http://shop.northwind-physio.example/"])


class ChallengeMarkerTests(unittest.TestCase):
    def test_phrase_in_ordinary_copy_not_flagged(self):  # review minor
        mod = load_script("seo_fetch")
        big = "<title>FAQ</title><p>What if I see Access denied on the portal?</p>" + "<p>text</p>" * 3000
        with FixtureServer() as srv:
            srv.add("/", big)
            srv.add("/blocked", "<title>Access denied</title>", status=403)
            ok = mod.ua_comparison(srv.url("/"), seohttp.fetch, ["browser"], None)
            blocked = mod.ua_comparison(srv.url("/blocked"), seohttp.fetch, ["browser"], None)
        self.assertEqual(ok["results"]["browser"]["challenge_markers"], [])
        self.assertEqual(blocked["results"]["browser"]["challenge_markers"], ["Access denied"])


if __name__ == "__main__":
    unittest.main()
