import subprocess
import unittest
from unittest import mock

from helpers import LIB  # noqa: F401  (adds lib to sys.path)

from seokit import dns

NSLOOKUP_NS = """Server:  router.local
Address:  192.168.1.1

Non-authoritative answer:
northwind-physio.example	nameserver = ada.ns.cloudflare.com
northwind-physio.example	nameserver = bob.ns.cloudflare.com
"""
NSLOOKUP_TXT = """Non-authoritative answer:
northwind-physio.example	text =

	"google-site-verification=abc123"
northwind-physio.example	text =

	"v=spf1 -all"
"""
DIG_NS = "ns1.host.example.\nns2.host.example.\n"
DIG_TXT = '"v=spf1 include:_spf.host.example " "-all"\n"facebook-domain-verification=xyz"\n'


def completed(stdout):
    return subprocess.CompletedProcess(args=[], returncode=0, stdout=stdout, stderr="")


class DnsTests(unittest.TestCase):
    def test_registrable_domain(self):
        self.assertEqual(dns.registrable_domain("www.northwind-physio.example"), "northwind-physio.example")
        self.assertEqual(dns.registrable_domain("a.b.acme-widgets.example"), "acme-widgets.example")
        self.assertEqual(dns.registrable_domain("shop.acme.co.uk"), "acme.co.uk")
        self.assertEqual(dns.registrable_domain("acme.co.uk"), "acme.co.uk")
        self.assertEqual(dns.registrable_domain("127.0.0.1"), "127.0.0.1")

    def test_no_tool_available(self):  # bug 22
        with mock.patch.object(dns.shutil, "which", return_value=None), \
                mock.patch.object(dns.subprocess, "run") as run:
            ns = dns.nameservers("northwind-physio.example")
            txt = dns.txt("northwind-physio.example")
            summary = dns.summary("northwind-physio.example")
        run.assert_not_called()
        self.assertFalse(ns["available"])
        self.assertIn("dig nor nslookup", ns["reason"])
        self.assertFalse(txt["available"])
        self.assertIsNone(summary["cloudflare_dns"])
        self.assertIsNone(summary["google_domain_property_likely"])

    def test_nslookup(self):
        def which(name):
            return "C:/Windows/System32/nslookup.exe" if name == "nslookup" else None

        def run(args, **kw):
            return completed(NSLOOKUP_NS if "-type=NS" in args else NSLOOKUP_TXT)

        with mock.patch.object(dns.shutil, "which", side_effect=which), \
                mock.patch.object(dns.subprocess, "run", side_effect=run):
            summary = dns.summary("www.northwind-physio.example")
        self.assertEqual(summary["domain"], "northwind-physio.example")
        self.assertEqual(summary["nameservers"]["tool"], "nslookup")
        self.assertEqual(summary["nameservers"]["nameservers"], ["ada.ns.cloudflare.com", "bob.ns.cloudflare.com"])
        self.assertTrue(summary["cloudflare_dns"])
        self.assertTrue(summary["google_domain_property_likely"])
        self.assertEqual(summary["txt_verifications"], ["google-site-verification"])

    def test_dig(self):
        calls = []

        def run(args, **kw):
            calls.append(args)
            return completed(DIG_NS if "NS" in args else DIG_TXT)

        with mock.patch.object(dns.shutil, "which", side_effect=lambda n: "/usr/bin/dig" if n == "dig" else None), \
                mock.patch.object(dns.subprocess, "run", side_effect=run):
            ns = dns.nameservers("shop.acme-widgets.example")
            txt = dns.txt("acme-widgets.example")
        self.assertEqual(calls[0], ["/usr/bin/dig", "+short", "NS", "acme-widgets.example"])
        self.assertEqual(ns["nameservers"], ["ns1.host.example", "ns2.host.example"])
        self.assertEqual(txt["records"], ["v=spf1 include:_spf.host.example -all", "facebook-domain-verification=xyz"])

    def test_tool_failure_reported(self):
        with mock.patch.object(dns.shutil, "which", return_value="/usr/bin/dig"), \
                mock.patch.object(dns.subprocess, "run", side_effect=subprocess.TimeoutExpired("dig", 15)):
            ns = dns.nameservers("acme-widgets.example")
        self.assertTrue(ns["available"])
        self.assertIn("TimeoutExpired", ns["error"])

    def test_ip_and_localhost_skipped(self):
        with mock.patch.object(dns.subprocess, "run") as run:
            self.assertFalse(dns.nameservers("127.0.0.1")["available"])
            self.assertFalse(dns.txt("localhost")["available"])
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
