import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from helpers import FixtureServer, fixture, load_script, run_script
from helpers.make_gsc_zip import make_zip

analyze = load_script("analyze_gsc")

HEADINGS = ["## Summary", "## Key numbers", "## Brand vs non-brand", "## Top queries", "## Top pages",
            "## Opportunities (high impressions, low CTR)", "## New and lost queries",
            "## Changes vs previous period", "## Data limits"]
LOCALES = ("en", "it", "de", "es", "pt", "fr", "it_semicolon")


class AnalyzeGscCliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def run_json(self, *args):
        out = os.path.join(self.tmp.name, "gsc.json")
        proc = run_script("analyze_gsc", *args, "--json", out)
        data = None
        if os.path.exists(out):
            with open(out, encoding="utf-8") as fh:
                data = json.load(fh)
        return proc, data

    def test_all_locales_give_identical_totals(self):  # bug 21
        totals = {}
        for loc in LOCALES:
            with self.subTest(locale=loc):
                zip_path = make_zip(fixture("gsc", "csv", loc), Path(self.tmp.name) / f"{loc}.zip")
                proc, data = self.run_json(zip_path, "--brand", "northwind|physio")
                self.assertEqual(proc.returncode, 0, proc.stderr)
                t = data["current"]["totals"]
                totals[loc] = (t["clicks"], t["impressions"], t["ctr_pct"], t["avg_position"], t["days"],
                               data["current"]["brand_split"]["brand"]["clicks"],
                               [r["key"] for r in data["current"]["opportunities"]])
                for h in HEADINGS:
                    self.assertIn(h, proc.stdout)
        self.assertEqual(len(set(map(repr, totals.values()))), 1, totals)
        self.assertEqual(totals["en"][:2], (100, 10000))

    def test_compare_export_yields_current_and_previous(self):  # bug 21
        proc, data = self.run_json(fixture("gsc", "csv", "en_compare"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(data["current"]["totals"]["clicks"], 100)
        self.assertEqual(data["previous"]["totals"]["clicks"], 79)
        self.assertEqual([r["key"] for r in data["compare_queries"]["lost"]], ["physio near me"])
        self.assertIn("café physio oslo", [r["key"] for r in data["compare_queries"]["new"]])
        self.assertIn("### Lost queries", proc.stdout)

    def test_previous_file_warnings(self):
        proc, data = self.run_json(fixture("gsc", "csv", "it"), "--previous", fixture("gsc", "csv", "with_filters_it"))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        warnings = " ".join(data["warnings"])
        self.assertIn("different lengths (7 days vs 5)", warnings)
        self.assertIn("different filters", warnings)

    def test_tiny_totals_warning(self):
        folder = Path(self.tmp.name) / "tiny"
        folder.mkdir()
        (folder / "Dates.csv").write_text("Date,Clicks,Impressions,CTR,Position\n2026-09-01,3,40,7.5%,4.0\n",
                                          encoding="utf-8")
        proc, data = self.run_json(folder)
        self.assertTrue(any("Small numbers" in w for w in data["warnings"]))
        self.assertIn("_Pass --brand REGEX", proc.stdout)

    def test_brand_regex_accent_folded(self):
        rx = analyze.compile_brand("FISIOTERAPIA PERUGIA|cafe")
        rows = [{"key": "fisioterapía perugia", "clicks": 1, "impressions": 2},
                {"key": "Café physio oslo", "clicks": 3, "impressions": 4},
                {"key": "other", "clicks": 5, "impressions": 6}]
        split = analyze.brand_split(rows, rx)
        self.assertEqual(split["brand"], {"queries": 2, "clicks": 4, "impressions": 6})
        self.assertTrue(analyze.compile_brand(r"\Dorthwind").search("northwind"))  # escapes not lower-cased

    def test_usage_errors_exit_2(self):
        proc = run_script("analyze_gsc", fixture("gsc", "csv", "en"), "--brand", "(unclosed")
        self.assertEqual(proc.returncode, 2)
        self.assertIn("not a valid regular expression", proc.stderr)
        proc = run_script("analyze_gsc", os.path.join(self.tmp.name, "missing.zip"))
        self.assertEqual(proc.returncode, 2)
        self.assertIn("not found", proc.stderr)

    def test_help_example(self):
        proc = run_script("analyze_gsc", "--help")
        self.assertIn('"northwind|physio"', proc.stdout)


class CheckUrlsTests(unittest.TestCase):
    def test_status_redirect_and_non_ascii(self):
        with FixtureServer() as srv:
            srv.add("/old/", status=301, headers=[("Location", "/new/")])
            srv.add("/new/", "<p>ok</p>")
            srv.add("/%C3%BCber/", "<p>ok</p>")
            with mock.patch.object(analyze, "_sleep") as sleep:
                res = analyze.check_urls([srv.url("/old/"), srv.url("/über/"), srv.url("/gone/"), "not-a-url"])
        by_key = {r["key"]: r for r in res}
        self.assertEqual(by_key[srv.url("/old/")]["status"], 301)
        self.assertEqual(by_key[srv.url("/old/")]["location"], srv.url("/new/"))
        self.assertEqual(by_key[srv.url("/old/")]["final_status"], 200)
        self.assertEqual(by_key[srv.url("/über/")]["status"], 200)
        self.assertEqual(by_key[srv.url("/gone/")]["status"], 404)
        self.assertEqual(len(res), 3)
        self.assertEqual([c.args for c in sleep.call_args_list], [(1.0,), (1.0,)])


if __name__ == "__main__":
    unittest.main()
