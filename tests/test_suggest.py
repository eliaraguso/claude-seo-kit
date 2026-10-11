import io
import json
import unittest
import urllib.error
import urllib.parse
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

from helpers import load_script

suggest = load_script("suggest")


class FakeResponse:
    def __init__(self, payload, charset="utf-8"):
        self._raw = json.dumps(payload).encode(charset)
        self.headers = mock.Mock()
        self.headers.get_content_charset.return_value = charset

    def read(self):
        return self._raw

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def run(argv, urlopen):
    out, err = io.StringIO(), io.StringIO()
    with mock.patch("urllib.request.urlopen", side_effect=urlopen), \
            mock.patch.object(suggest, "_sleep") as sleep, redirect_stdout(out), redirect_stderr(err):
        code = suggest.main(argv)
    return code, out.getvalue(), err.getvalue(), sleep


def query_of(req):
    return urllib.parse.parse_qs(urllib.parse.urlsplit(req.full_url).query)


class SuggestTests(unittest.TestCase):
    def test_locale_defaults(self):  # bug 20: hl/gl defaulted to Italian
        self.assertEqual(suggest.locale_for("en"), ("en", "us"))
        self.assertEqual(suggest.locale_for("it"), ("it", "it"))
        self.assertEqual(suggest.locale_for("pt"), ("pt", "br"))
        self.assertEqual(suggest.locale_for("nb"), ("nb", "us"))
        self.assertEqual(suggest.locale_for("de", gl="at"), ("de", "at"))

    def test_default_request_is_english(self):  # bug 20
        seen = []

        def urlopen(req, timeout=None):
            seen.append(query_of(req))
            return FakeResponse(["physio oslo", ["physio oslo prices"]])

        code, out, _, _ = run(["physio oslo"], urlopen)
        self.assertEqual(code, 0)
        self.assertEqual(seen[0]["hl"], ["en"])
        self.assertEqual(seen[0]["gl"], ["us"])
        self.assertIn("- physio oslo prices", out)

    def test_alphabet_table(self):  # bug 20: j k w x y were missing
        v = suggest.variants("acme", "en", True)
        letters = {x.split(" ", 1)[1] for x in v if x.startswith("acme ")}
        for c in "jkwxy0123456789":
            self.assertIn(c, letters)
        self.assertEqual(len([x for x in v if x.startswith("acme ")]), 36)
        self.assertIn("how acme", v)
        self.assertIn("perché acme", suggest.variants("acme", "it", True))
        self.assertIn("por qué acme", suggest.variants("acme", "es", True))
        self.assertEqual(suggest.variants("acme", "en", False), ["acme"])

    def test_errors_not_returned_as_suggestions(self):  # bug 20
        calls = {"n": 0}

        def urlopen(req, timeout=None):
            calls["n"] += 1
            if calls["n"] == 1:
                raise urllib.error.URLError("network down")
            return FakeResponse(["q", ["acme widgets blue"]])

        code, out, err, sleep = run(["acme widgets", "acme", "--json"], urlopen)
        data = json.loads(out)
        self.assertEqual(code, 0)
        self.assertEqual(data["results"]["acme widgets"], [])
        self.assertEqual(data["results"]["acme"], ["acme widgets blue"])
        self.assertEqual(len(data["errors"]), 1)
        self.assertIn("network down", data["errors"][0]["error"])
        self.assertIn("network down", err)
        sleep.assert_called_with(0.5)

    def test_429_stops_and_exits_3(self):
        calls = {"n": 0}

        def urlopen(req, timeout=None):
            calls["n"] += 1
            if calls["n"] == 3:
                raise urllib.error.HTTPError(req.full_url, 429, "Too Many Requests", {}, None)
            return FakeResponse(["q", [f"s{calls['n']}"]])

        code, out, err, _ = run(["acme", "other", "--expand", "--json"], urlopen)
        self.assertEqual(code, 3)
        self.assertEqual(calls["n"], 3)
        data = json.loads(out)
        self.assertTrue(data["rate_limited"])
        self.assertEqual(data["results"], {"acme": ["s1", "s2"]})
        self.assertIn("429", err)

    def test_non_utf8_charset(self):
        def urlopen(req, timeout=None):
            return FakeResponse(["caf", ["café oslo"]], charset="latin-1")

        code, out, _, _ = run(["caf", "--json"], urlopen)
        self.assertEqual(json.loads(out)["results"]["caf"], ["café oslo"])


if __name__ == "__main__":
    unittest.main()
