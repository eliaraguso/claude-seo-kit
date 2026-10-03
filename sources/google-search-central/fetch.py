"""Scarica pagine di Google Search Central e salva il corpo articolo come Markdown semplice.

Uso: python fetch.py urls.txt
"""
import concurrent.futures as cf
import html
import os
import sys
import urllib.request
from html.parser import HTMLParser

BASE = "https://developers.google.com"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pages")
if os.name == "nt":  # percorsi lunghi su Windows
    OUT = "\\\\?\\" + OUT
BLOCK = {"p", "div", "section", "tr", "br", "dt", "dd", "figure", "blockquote"}
SKIP = {"script", "style", "noscript", "devsite-feedback", "devsite-thumb-rating", "nav", "button"}


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_h1 = False
        self.depth = 0  # profondita div dentro article-body
        self.skip = 0
        self.pre = False
        self.out = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1" and not self.title:
            self.in_h1 = True
        if self.depth == 0:
            if tag == "div" and "devsite-article-body" in (a.get("class") or ""):
                self.depth = 1
            return
        if tag == "div":
            self.depth += 1
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5"}:
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "pre":
            self.pre = True
            self.out.append("\n```\n")
        elif tag == "code" and not self.pre:
            self.out.append("`")
        elif tag in {"td", "th"}:
            self.out.append(" | ")
        elif tag in BLOCK:
            self.out.append("\n")
        elif tag == "a" and a.get("href", "").startswith(("/search", "/crawling", "http")):
            self.out.append("[")
            self._href = a["href"]

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False
        if self.depth == 0:
            return
        if tag == "div":
            self.depth -= 1
            if self.depth == 0:
                return
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "pre":
            self.pre = False
            self.out.append("\n```\n")
        elif tag == "code" and not self.pre:
            self.out.append("`")
        elif tag == "a" and getattr(self, "_href", None):
            self.out.append(f"]({self._href.split('?')[0]})")
            self._href = None
        elif tag in BLOCK or tag in {"ul", "ol", "table"}:
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_h1:
            self.title += data.strip()
        if self.depth and not self.skip:
            self.out.append(data if self.pre else " ".join(data.split()) + (" " if data.endswith((" ", "\n")) else ""))


def clean(text):
    lines, blank = [], 0
    for line in text.splitlines():
        line = line.rstrip()
        if not line.strip():
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def fetch(path):
    url = f"{BASE}{path}?hl=it"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode("utf-8", "replace")
    p = ArticleParser()
    p.feed(raw)
    body = clean("".join(p.out))
    name = path.strip("/").replace("/", "__") + ".md"
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(f"# {html.unescape(p.title)}\n\nFonte: {url}\n\n{body}")
    return path, len(body)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    paths = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
    failed = []
    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(fetch, p): p for p in paths}
        for fut in cf.as_completed(futs):
            try:
                path, n = fut.result()
                if n < 200:
                    print("SHORT", path, n)
            except Exception as e:  # noqa: BLE001
                failed.append(futs[fut])
                print("FAIL", futs[fut], e)
    print(f"ok {len(paths) - len(failed)}/{len(paths)}")
