import tempfile
import unittest
from pathlib import Path

from helpers import fixture
from helpers.make_gsc_zip import make_zip

from seokit import gsc

LOCALES = ("en", "it", "de", "es", "pt", "fr", "it_semicolon")
ROLES = {"queries", "pages", "countries", "devices", "dates", "search_appearance"}


class ParseNumberTests(unittest.TestCase):
    def test_formats(self):  # bug 21
        cases = {"1,234": 1234, "1.234": 1234, "1 234": 1234, "1 234": 1234, "1.234,56": 1234.56,
                 "1,234.56": 1234.56, "12,5 %": 12.5, "12.5%": 12.5, "<0.1%": 0.1, "0.125": 0.125,
                 "4,56": 4.56, "7": 7, "": None, "-": None, "abc": None}
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(gsc.parse_number(raw), expected)

    def test_decimal_hint(self):
        self.assertEqual(gsc.parse_number("10.125", decimal=True), 10.125)
        self.assertEqual(gsc.parse_number("1,234", decimal=True), 1.234)

    def test_dates(self):
        self.assertEqual(gsc.normalize_date("01/09/2026"), "2026-09-01")
        self.assertEqual(gsc.normalize_date("09/25/2026"), "2026-09-25")
        self.assertEqual(gsc.normalize_date("2026-09-01"), "2026-09-01")


class LoadExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def zip_of(self, locale, utf8_flag=True):
        dest = Path(self.tmp.name) / f"{locale}-{int(utf8_flag)}.zip"
        return make_zip(fixture("gsc", "csv", locale), dest, utf8_flag=utf8_flag)

    def test_all_locales_identical(self):  # bug 21: stems, columns, delimiter
        reference = None
        for loc in LOCALES:
            with self.subTest(locale=loc):
                exp = gsc.load_export(self.zip_of(loc))
                self.assertEqual(set(exp["current"]), ROLES, exp["meta"]["files"])
                self.assertEqual(exp["warnings"], [])
                self.assertIsNone(exp["previous"])
                summary = (gsc.totals(exp["current"]),
                           [(r["clicks"], r["impressions"], r["ctr"], r["position"]) for r in exp["current"]["queries"]],
                           [r["key"] for r in exp["current"]["pages"]])
                if reference is None:
                    reference = summary
                    self.assertEqual(summary[0]["clicks"], 100)
                    self.assertEqual(summary[0]["impressions"], 10000)
                    self.assertEqual(summary[0]["from"], "2026-09-01")
                    self.assertEqual(summary[0]["days"], 7)
                else:
                    self.assertEqual(summary, reference)

    def test_semicolon_excel_resave(self):
        exp = gsc.load_export(fixture("gsc", "csv", "it_semicolon"))
        self.assertEqual(set(exp["meta"]["delimiters"].values()), {";"})
        self.assertIn("café physio oslo", [r["key"] for r in exp["current"]["queries"]])

    def test_zip_names_without_utf8_flag(self):
        exp = gsc.load_export(self.zip_of("de", utf8_flag=False))
        self.assertIn("Länder.csv", exp["meta"]["files"])
        self.assertEqual(exp["meta"]["files"]["Länder.csv"], "countries")

    def test_compare_export(self):  # bug 21: compare took the first column only
        exp = gsc.load_export(fixture("gsc", "csv", "en_compare"))
        self.assertTrue(exp["meta"]["compare"])
        cur, prev = exp["current"], exp["previous"]
        self.assertEqual(gsc.totals(cur)["clicks"], 100)
        self.assertEqual(gsc.totals(prev)["clicks"], sum(max(c - 3, 1) for c in (12, 15, 9, 20, 18, 7, 19)))
        prev_keys = [r["key"] for r in prev["queries"]]
        self.assertIn("physio near me", prev_keys)
        self.assertNotIn("physio near me", [r["key"] for r in cur["queries"]])
        self.assertNotIn("café physio oslo", prev_keys)
        self.assertEqual(exp["meta"]["filters"]["search_type"], "Web")

    def test_filters(self):  # bug 21: Filters.csv ignored
        exp = gsc.load_export(fixture("gsc", "csv", "with_filters_it"))
        f = exp["meta"]["filters"]
        self.assertEqual(f["search_type"], "Web")
        self.assertEqual(f["date_range"], "Ultimi 5 giorni")
        self.assertEqual(f["dimensions"], [{"name": "Query", "value": "+physio"}])

    def test_short_rows_skipped_with_warning(self):  # bug 21: IndexError
        folder = Path(self.tmp.name) / "short"
        folder.mkdir()
        (folder / "Queries.csv").write_text(
            "Top queries,Clicks,Impressions,CTR,Position\nnorthwind physio,4,40,10%,1.0\nbroken row,3\n\n",
            encoding="utf-8")
        exp = gsc.load_export(folder)
        self.assertEqual(len(exp["current"]["queries"]), 1)
        self.assertTrue(any("line 3" in w for w in exp["warnings"]))

    def test_unknown_language_by_position(self):
        folder = Path(self.tmp.name) / "xx"
        folder.mkdir()
        (folder / "a.csv").write_text("Zapytania,K,W,C,P\nnorthwind physio,4,40,10%,1.0\n", encoding="utf-8")
        (folder / "b.csv").write_text("Datum2,K,W,C,P\n2026-09-01,4,40,10%,1.0\n", encoding="utf-8")
        exp = gsc.load_export(folder)
        self.assertEqual(exp["current"]["dates"][0]["clicks"], 4)
        self.assertEqual(exp["current"]["dates"][0]["impressions"], 40)
        self.assertIn("could not tell", exp["warnings"][0])

    def test_errors(self):
        with self.assertRaises(gsc.GscError):
            gsc.load_export(Path(self.tmp.name) / "missing.zip")
        empty = Path(self.tmp.name) / "empty"
        empty.mkdir()
        with self.assertRaises(gsc.GscError):
            gsc.load_export(empty)


if __name__ == "__main__":
    unittest.main()
