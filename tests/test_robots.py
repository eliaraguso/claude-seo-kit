import unittest

from helpers import fixture

from seokit import bots, robots


def load(name):
    return robots.parse(fixture("robots", name).read_bytes())


class RobotsTests(unittest.TestCase):
    def test_bom_is_stripped(self):  # bug 3
        parsed = load("bom.txt")
        self.assertEqual(len(parsed["groups"]), 1)
        self.assertEqual(parsed["groups"][0]["user_agents"], ["*"])
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "/private/x"))
        self.assertTrue(robots.is_allowed(parsed, "Googlebot", "/public/"))
        self.assertEqual(robots.sitemaps(parsed), ["https://northwind-physio.example/sitemap.xml"])

    def test_most_specific_group_wins(self):  # bug 14
        parsed = load("groups_specific_ua.txt")
        self.assertTrue(robots.is_allowed(parsed, "Googlebot", "/"))  # * Disallow: / does not apply
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "/admin/x"))
        self.assertTrue(robots.is_allowed(parsed, "Googlebot", "/admin/public/x"))
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "/tmp/x"))  # merged googlebot groups
        self.assertTrue(robots.is_allowed(parsed, "Bingbot", "/tmp/x"))
        self.assertFalse(robots.is_allowed(parsed, "GPTBot", "/"))
        self.assertFalse(robots.is_allowed(parsed, "ClaudeBot", "/"))  # falls to *
        self.assertEqual(robots.evaluate(parsed, "Googlebot-Image", "/admin/x")["group"], "googlebot")
        other = parsed["groups"][-1]["other"]
        self.assertEqual(other[0]["key"], "crawl-delay")

    def test_wildcards_and_dollar(self):  # bug 14
        parsed = load("wildcards_dollar.txt")
        cases = {
            "/files/menu.pdf": False,
            "/files/menu.pdf?x=1": True,
            "/search": False,
            "/search/about": True,
            "/search/aboutus": True,
            "/item?sessionid=1": False,
            "/p": True,
            "/p/1": False,
            "/page": True,
            "/index.php": True,   # equal length: Allow /*.php$ beats Disallow /*.php
            "/index.php?x": False,
            "/robots.txt": True,
        }
        for path, expected in cases.items():
            with self.subTest(path=path):
                self.assertEqual(robots.is_allowed(parsed, "Googlebot", path), expected)

    def test_full_url_and_non_ascii_path(self):
        parsed = robots.parse("User-agent: *\nDisallow: /über/\n")
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "https://a.example/%C3%BCber/x"))
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "/über/x"))

    def test_html_fallback(self):
        parsed = load("html_fallback.txt")
        self.assertTrue(parsed["html_suspect"])
        self.assertEqual(parsed["groups"], [])
        self.assertTrue(robots.is_allowed(parsed, "Googlebot", "/"))

    def test_user_agent_spellings(self):
        parsed = load("typo_useragent.txt")
        self.assertEqual([g["user_agents"] for g in parsed["groups"]], [["GPTBot"], ["ClaudeBot"], ["*"]])
        self.assertFalse(robots.is_allowed(parsed, "GPTBot", "/"))
        self.assertFalse(robots.is_allowed(parsed, "ClaudeBot", "/"))
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "/cart/"))
        self.assertFalse(robots.is_allowed(parsed, "Googlebot", "/checkout/"))
        self.assertTrue(robots.is_allowed(parsed, "Googlebot", "/"))

    def test_status_semantics(self):  # bug 14
        self.assertEqual(robots.status_semantics(200), "parse")
        self.assertEqual(robots.status_semantics(404), "allow_all")
        self.assertEqual(robots.status_semantics(403), "allow_all")
        self.assertEqual(robots.status_semantics(429), "unavailable")
        self.assertEqual(robots.status_semantics(503), "unavailable")
        self.assertEqual(robots.status_semantics(None), "unavailable")

    def test_bot_tokens(self):
        tokens = bots.TOKENS
        for t in ("Googlebot", "Google-Extended", "Google-CloudVertexBot", "Applebot-Extended", "OAI-SearchBot",
                  "Claude-SearchBot", "anthropic-ai", "Perplexity-User", "meta-externalagent", "DuckAssistBot",
                  "YandexBot"):
            self.assertIn(t, tokens)
        self.assertEqual(len(tokens), 24)
        purposes = {b["purpose"] for b in bots.BOT_TOKENS}
        self.assertLessEqual(purposes, {"search", "ai-training", "ai-search", "user-fetch", "other"})


if __name__ == "__main__":
    unittest.main()
