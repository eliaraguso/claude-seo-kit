import json
import os
import tempfile
import unittest
from pathlib import Path

from helpers import fixture, load_script, run_script

BASE = "https://acme-widgets.example"
TEXT = "Acme Widgets designs and ships durable widgets for workshops and homes. " * 6


def page(title, canonical, h1="Widgets"):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width"><title>{title}</title>'
            f'<meta name="description" content="{title} description">'
            f'<link rel="canonical" href="{canonical}"></head><body><h1>{h1}</h1><p>{TEXT}</p></body></html>')


def checks(result):
    out = {(f["check"], f["severity"]) for f in result["site_findings"]}
    for p in result["pages"]:
        out |= {(f["check"], f["severity"]) for f in p["findings"]}
    return out


class CheckBuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def run_build(self, folder, *args):
        out = os.path.join(self.tmp.name, "result.json")
        proc = run_script("check_build", folder, "--json", out, *args, cwd=self.tmp.name)
        data = None
        if os.path.exists(out):
            with open(out, encoding="utf-8") as fh:
                data = json.load(fh)
        return proc, data

    def test_static_site(self):  # bug 19
        proc, data = self.run_build(fixture("build", "static_site"), "--base", BASE)
        self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
        found = checks(data)
        self.assertIn(("canonical-to-home", "high"), found)
        self.assertIn(("broken-internal-links", "medium"), found)
        self.assertIn(("sitemap-extra-urls", "medium"), found)
        self.assertIn(("sitemap-missing-pages", "low"), found)
        by_file = {p["file"]: p for p in data["pages"]}
        self.assertTrue(by_file["404.html"]["shell"])
        self.assertEqual(by_file["about/index.html"]["url"], BASE + "/about/")
        self.assertEqual(by_file["about/index.html"]["findings"], [])
        self.assertEqual(by_file["products/blue.html"]["url"], BASE + "/products/blue.html")
        self.assertIn("## High", proc.stdout)
        self.assertIn("Exit 1", proc.stdout)

    def test_fail_on_threshold(self):
        proc, data = self.run_build(fixture("build", "static_site"), "--base", BASE, "--fail-on", "critical")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertEqual(data["exit_code"], 0)

    def test_angular_dist(self):
        proc, data = self.run_build(fixture("build", "angular_prerender_dist"), "--base", "https://adanovak.example")
        self.assertEqual(proc.returncode, 1)
        self.assertTrue(data["dir"].endswith("browser"))
        found = checks(data)
        self.assertIn(("canonical-bad-host", "high"), found)
        self.assertIn(("links-to-dev-hosts", "high"), found)
        shells = [p["file"] for p in data["pages"] if p["shell"]]
        self.assertEqual(shells, ["index.csr.html"])

    def test_next_export(self):
        proc, data = self.run_build(fixture("build", "next_export"), "--base", BASE)
        self.assertEqual(proc.returncode, 1)
        found = checks(data)
        self.assertIn(("robots-disallow-all", "critical"), found)
        self.assertIn(("mixed-content", "medium"), found)
        about = [p for p in data["pages"] if p["file"] == "about.html"][0]
        self.assertEqual(about["url"], BASE + "/about.html")
        self.assertEqual(about["findings"], [])  # canonical /about matches the clean URL of about.html
        index = [p for p in data["pages"] if p["file"] == "index.html"][0]
        self.assertNotIn("broken-internal-links", [f["check"] for f in index["findings"]])

    def test_clean_site_exit_0_and_home_canonical_everywhere(self):
        root = Path(self.tmp.name) / "site"
        (root / "a").mkdir(parents=True)
        (root / "b").mkdir()
        (root / "index.html").write_text(page("Home", BASE + "/"), encoding="utf-8")
        (root / "a" / "index.html").write_text(page("Page A", BASE + "/a/"), encoding="utf-8")
        (root / "b" / "index.html").write_text(page("Page B", BASE + "/b/"), encoding="utf-8")
        (root / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
        locs = "".join(f"<url><loc>{BASE}{p}</loc></url>" for p in ("/", "/a/", "/b/"))
        (root / "sitemap.xml").write_text(
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{locs}</urlset>', encoding="utf-8")
        proc, data = self.run_build(root, "--base", BASE, "--fail-on", "low")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertEqual(checks(data), set())
        for name in ("a", "b"):
            (root / name / "index.html").write_text(page(f"Page {name}", BASE + "/"), encoding="utf-8")
        proc, data = self.run_build(root, "--base", BASE)
        self.assertEqual(proc.returncode, 1)
        self.assertIn(("canonical-home-everywhere", "critical"), checks(data))

    def test_usage_errors_exit_2(self):
        self.assertEqual(run_script("check_build", fixture("build", "static_site")).returncode, 2)  # no --base
        self.assertEqual(run_script("check_build", fixture("build", "static_site"), "--base", "acme").returncode, 2)
        missing = os.path.join(self.tmp.name, "nope")
        proc = run_script("check_build", missing, "--base", BASE)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("not a folder", proc.stderr)

    def test_page_url_and_shell_files(self):  # bug 19
        mod = load_script("check_build")
        root = Path(self.tmp.name)
        self.assertEqual(mod.page_url(BASE, root, root / "foo-index.html"), BASE + "/foo-index.html")
        self.assertEqual(mod.page_url(BASE, root, root / "blog" / "index.html"), BASE + "/blog/")
        self.assertEqual(mod.page_url(BASE + "/shop/", root, root / "index.html"), BASE + "/shop/")
        for name in ("404.html", "index.csr.html", "200.html", "_fallback.html", "google1234abcd.html",
                     "BingSiteAuth.xml"):
            self.assertTrue(mod.is_shell(name), name)
        self.assertFalse(mod.is_shell("foo-index.html"))


if __name__ == "__main__":
    unittest.main()
