import unittest

from helpers import fixture, fixture_text

from seokit import html as seohtml
from seokit import typos

NW = "https://northwind-physio.example"


def parse(name, url="https://northwind-physio.example/", **kw):
    return seohtml.parse_page(fixture_text("html", name), url, **kw)


class ParserRegressionTests(unittest.TestCase):
    def test_svg_title_inside_h1(self):  # bug 1
        p = parse("svg_in_h1.html")
        self.assertEqual(p["title"], ["Physiotherapy in Oslo | Northwind Physio"])
        self.assertEqual(p["h1"], ["Main heading"])
        self.assertEqual(p["headings"][0], {"level": 1, "text": "Main heading"})
        self.assertNotIn("icon", p["visible_text"])

    def test_noscript_img_in_head_is_not_a_violation(self):  # bug 2
        p = parse("noscript_in_head.html", NW + "/contact/")
        self.assertEqual(p["head_invalid_tags"], [])
        self.assertEqual(p["images"], [])
        self.assertEqual(p["external_links"], [])
        self.assertNotIn("Please enable", p["visible_text"])
        self.assertFalse(p["canonical"]["in_body"])
        self.assertTrue(p["canonical"]["self_referencing"])
        self.assertEqual(p["meta_description"], ["Book a physiotherapy appointment in Oslo."])

    def test_real_head_violation_detected(self):
        p = seohtml.parse_page('<html><head><title>x</title><div>ad</div>'
                               '<link rel="canonical" href="/x"></head><body></body></html>',
                               NW + "/x")
        self.assertEqual(p["head_invalid_tags"], ["div"])
        self.assertTrue(p["canonical"]["in_body"])

    def test_base_href_resolves_links(self):  # bug 5
        p = parse("base_href.html", NW + "/clinic/team/")
        self.assertEqual(p["base_href"], NW + "/clinic/")
        resolved = [l["resolved"] for l in p["internal_links"]]
        self.assertEqual(resolved, [NW + "/clinic/therapists/anna/", NW + "/prices/", NW + "/contact/"])
        self.assertEqual(p["images"][0]["resolved"], NW + "/clinic/img/anna.jpg")
        self.assertEqual(p["canonical"]["resolved"], NW + "/clinic/team/")
        self.assertTrue(p["canonical"]["self_referencing"])

    def test_canonical_relative_resolved_and_compared(self):  # bug 10
        p = parse("canonical_relative.html", NW + "/prices/")
        self.assertEqual(p["canonical"]["href"], "/prices")
        self.assertEqual(p["canonical"]["resolved"], NW + "/prices")
        self.assertTrue(p["canonical"]["self_referencing"])  # trailing slash normalised
        other = parse("canonical_relative.html", NW + "/prices/?page=2")
        self.assertFalse(other["canonical"]["self_referencing"])

    def test_canonical_default_port_normalised(self):  # bug 10
        p = seohtml.parse_page('<link rel="canonical" href="https://northwind-physio.example:443/a/">',
                               NW + "/a")
        self.assertTrue(p["canonical"]["self_referencing"])

    def test_canonical_in_body(self):
        p = parse("canonical_in_body.html", "https://acme-widgets.example/blog/")
        self.assertTrue(p["canonical"]["in_body"])
        self.assertEqual(p["canonical"]["resolved"], "https://acme-widgets.example/blog/")

    def test_internal_external_ignores_www_and_default_port(self):  # bug 11
        p = parse("non_ascii_links.html", "https://adanovak.example/links")
        internal = [l["href"] for l in p["internal_links"]]
        external = [l["href"] for l in p["external_links"]]
        self.assertIn("https://www.adanovak.example/blog/", internal)
        self.assertIn("https://adanovak.example:443/talks/", internal)
        self.assertIn("https://blog.adanovak.example/", external)
        self.assertIn("https://bücher.example/", external)

    def test_non_ascii_links(self):  # bug 7
        p = parse("non_ascii_links.html", "https://adanovak.example/links")
        resolved = [l["resolved"] for l in p["internal_links"]]
        self.assertIn("https://adanovak.example/%C3%BCber-uns/", resolved)
        self.assertIn("https://adanovak.example/a%C3%B1o/se%C3%B1ales?q=ni%C3%B1o", resolved)
        self.assertIn("https://adanovak.example/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/", resolved)
        ext = {l["href"]: l["resolved"] for l in p["external_links"]}
        self.assertEqual(ext["https://bücher.example/"], "https://xn--bcher-kva.example/")

    def test_other_schemes(self):
        p = parse("non_ascii_links.html", "https://adanovak.example/links")
        self.assertEqual(p["other_links"], {"mailto": 1, "tel": 1, "sms": 1, "whatsapp": 1, "javascript": 1,
                                            "data": 1, "ftp": 1, "fragment": 1})
        self.assertEqual(p["anchors_without_href"], 1)
        cv = [l for l in p["internal_links"] if l["href"].endswith(".pdf")][0]
        self.assertTrue(cv["nofollow"])
        self.assertEqual(p["documents"], ["https://adanovak.example/cv/ada-novak.pdf"])

    def test_jsonld_types_recursive(self):  # bug 12
        p = parse("jsonld_graph_nested.html", "https://acme-widgets.example/widgets/blue")
        for t in ("Organization", "PostalAddress", "Product", "Brand", "Offer", "OfferShippingDetails",
                  "DefinedRegion", "Review", "Person", "WebPage", "ItemPage"):
            self.assertIn(t, p["jsonld_types"])
        self.assertEqual(p["jsonld_errors"], [])
        self.assertEqual(len(p["jsonld"]), 2)

    def test_jsonld_lenient(self):
        p = parse("jsonld_lenient.html", "https://adanovak.example/")
        self.assertEqual(p["jsonld_types"], ["Person", "WebSite", "BreadcrumbList"])
        errors = p["jsonld_errors"]
        self.assertEqual(len(errors), 4)
        self.assertTrue(all(e["recovered"] for e in errors[:3]))
        self.assertFalse(errors[3]["recovered"])
        self.assertEqual(errors[3]["index"], 3)
        self.assertIn("control character", errors[0]["error"])
        self.assertIn("trailing comma", errors[1]["error"])

    def test_spa_shells(self):  # bug 13
        for name, root in (("spa_shell_vite.html", "div#root"), ("spa_shell_angular.html", "app-root"),
                           ("spa_shell_nuxt.html", "div#__nuxt")):
            with self.subTest(name=name):
                p = parse(name, "https://acme-widgets.example/")
                self.assertTrue(p["spa_shell_suspect"])
                self.assertEqual(p["spa_root"], root)

    def test_ssr_page_is_not_spa_shell(self):
        filler = "Real server-rendered content about widgets. " * 20
        p = seohtml.parse_page(f'<body><div id="__next"><main><h1>Widgets</h1><p>{filler}</p></main></div></body>',
                               "https://acme-widgets.example/")
        self.assertFalse(p["spa_shell_suspect"])

    def test_heading_skips(self):
        p = parse("headings_skip.html")
        self.assertEqual([(s["from"], s["to"]) for s in p["heading_skips"]], [("h1", "h3"), ("h2", "h5")])

    def test_hreflang_issues(self):
        p = parse("hreflang_missing_return.html", NW + "/en/")
        codes = {h["lang"]: h["valid_code"] for h in p["hreflang"]}
        self.assertFalse(codes["en-UK"])
        self.assertTrue(codes["nb"])
        kinds = [i["issue"] for i in p["hreflang_issues"]]
        self.assertIn("invalid_code", kinds)
        self.assertIn("duplicate_code", kinds)
        self.assertIn("missing_self_reference", kinds)

    def test_hreflang_return_links_across_pages(self):
        en = seohtml.parse_page(
            '<link rel="alternate" hreflang="en" href="/en/"><link rel="alternate" hreflang="nb" href="/nb/">',
            NW + "/en/")
        nb = seohtml.parse_page('<link rel="alternate" hreflang="nb" href="/nb/">', NW + "/nb/")
        en["final_url"], nb["final_url"] = NW + "/en/", NW + "/nb/"
        issues = seohtml.hreflang_return_issues([en, nb])
        self.assertEqual(issues, [{"page": NW + "/en/", "alternate": NW + "/nb/", "lang": "nb",
                                   "issue": "missing_return_link"}])

    def test_robots_meta_per_ua_and_indexable(self):
        p = seohtml.parse_page('<meta name="robots" content="index"><meta name="googlebot" content="noindex">'
                               '<meta name="bingbot" content="nosnippet">', NW + "/")
        self.assertEqual(p["robots_meta"], {"robots": ["index"], "googlebot": ["noindex"], "bingbot": ["nosnippet"]})
        self.assertFalse(p["indexable"]["value"])

    def test_images_and_social(self):
        p = seohtml.parse_page(
            '<meta property="og:title" content="OG"><meta name="twitter:card" content="summary">'
            '<meta name="viewport" content="width=device-width">'
            '<body><img src="a.jpg"><img src="b.jpg" alt=""><img data-src="c.jpg" alt="C" loading="lazy" '
            'width="10" height="20"><div itemscope itemtype="https://schema.org/Thing"></div></body>', NW + "/")
        self.assertEqual(p["og"], {"og:title": "OG"})
        self.assertEqual(p["twitter"], {"twitter:card": "summary"})
        self.assertEqual(p["viewport"], "width=device-width")
        self.assertEqual(p["images_without_alt"], 1)
        self.assertTrue(p["images"][1]["alt_empty"])
        self.assertEqual(p["images"][2]["lazy_attr"], "c.jpg")
        self.assertTrue(p["microdata_present"])
        self.assertFalse(p["rdfa_present"])

    def test_main_text_excludes_nav_and_footer(self):
        p = seohtml.parse_page("<body><nav>Menu items</nav><main>Body text</main><footer>Footer</footer></body>",
                               NW + "/")
        self.assertEqual(p["visible_text"], "Menu items Body text Footer")
        self.assertEqual(p["main_text_chars"], len("Body text"))


class TypoTests(unittest.TestCase):
    def test_missing_lang_has_no_italian_checks(self):  # bug 4
        page = seohtml.parse_page("<html><body><p>Perchè no? Un pò di testo.</p></body></html>", NW + "/")
        self.assertIsNone(page["lang"])
        self.assertIsNone(typos.find(page, page["lang"]))
        self.assertIsNone(typos.find(page, "de"))

    def test_italian_pack_applies_to_italian_pages(self):
        page = seohtml.parse_page('<html lang="it-IT"><body><p>Perchè no? Un pò di testo.</p></body></html>', NW + "/")
        found = typos.find(page, page["lang"])
        self.assertEqual(sorted(f["match"] for f in found), ["Perchè", "pò"])

    def test_english_pack(self):
        page = seohtml.parse_page('<html lang="en"><body><p>See teh the the list.</p></body></html>', NW + "/")
        matches = [f["match"].lower() for f in typos.find(page, "en")]
        self.assertIn("teh", matches)
        self.assertIn("the the", matches)

    def test_charset_fixture_is_latin1(self):
        raw = fixture("html", "charset_meta_latin1.html").read_bytes()
        with self.assertRaises(UnicodeDecodeError):
            raw.decode("utf-8")


if __name__ == "__main__":
    unittest.main()
