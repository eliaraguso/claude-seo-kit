import re
import shutil
import subprocess
import unittest

from helpers import REPO, SCRIPTS

from seokit import html as seohtml

NODE = shutil.which("node")
SCHEMA = REPO / "docs" / "page-schema.md"


def schema_rows():
    """(key, python, js) from the first table of docs/page-schema.md."""
    rows = []
    text = SCHEMA.read_text(encoding="utf-8")
    section = text.split("## Page keys", 1)[1].split("\n## ", 1)[0]
    for line in section.splitlines():
        m = re.match(r"^\| `([a-z_]+)` \|[^|]*\| ([^|]+) \| ([^|]+) \|", line)
        if m:
            rows.append((m.group(1), m.group(2).strip(), m.group(3).strip()))
    return rows


class ExtractDomSchemaTests(unittest.TestCase):
    def test_python_keys_match_schema(self):
        page = seohtml.parse_page("<html><head><title>x</title></head><body></body></html>", "https://adanovak.example/")
        documented = {k for k, py, _ in schema_rows() if py == "yes"}
        self.assertTrue(documented)
        self.assertEqual(documented - set(page), set())

    @unittest.skipIf(NODE is None, "node is not installed")
    def test_js_syntax_and_keys(self):
        path = SCRIPTS["extract_dom"]
        proc = subprocess.run([NODE, "--check", str(path)], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        source = path.read_text(encoding="utf-8")
        returned = source.rsplit("return {", 1)[1]
        js_keys = [k for k, _, js in schema_rows() if js in ("yes", "null")]
        self.assertGreater(len(js_keys), 30)
        for key in js_keys:
            with self.subTest(key=key):
                self.assertRegex(returned, rf"\b{key}\b[,:]")

    def test_usage_comment_shows_both_forms(self):
        source = SCRIPTS["extract_dom"].read_text(encoding="utf-8")
        self.assertIn("evaluate_script", source)
        self.assertIn("(function () {", source)


if __name__ == "__main__":
    unittest.main()
