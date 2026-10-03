"""Scarica articoli SEJ (elenco in sej_keep.json) come Markdown semplice, 1 richiesta ogni 2 s."""
import json, os, re, sys, time, urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "google-search-central"))
import fetch as gsc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "articles")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126"}


class SejParser(gsc.ArticleParser):
    def handle_starttag(self, tag, attrs):
        if self.depth == 0 and tag == "div" and "sej-article-content" in (dict(attrs).get("class") or ""):
            self.depth = 1
            return
        super().handle_starttag(tag, attrs)


os.makedirs(OUT, exist_ok=True)
items = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sej_keep.json"), encoding="utf-8"))
fail = 0
for n, it in enumerate(items, 1):
    parts = it["url"].rstrip("/").split("/")
    slug = re.sub(r"[^a-z0-9-]", "", parts[-2])[:30]
    path = os.path.join(OUT, f"{parts[-1][:30]}.md")
    if os.path.exists(path):
        continue
    try:
        raw = urllib.request.urlopen(urllib.request.Request(it["url"], headers=UA), timeout=30).read().decode("utf-8", "replace")
        p = SejParser()
        p.feed(raw)
        body = gsc.clean("".join(p.out))
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {it['title']}\n\nFonte: {it['url']}\nData: {it['date']}\nCategorie: {', '.join(it['cats'])}\n\n{body}")
        if len(body) < 500:
            print("SHORT", it["url"], len(body), flush=True)
    except Exception as e:  # noqa: BLE001
        fail += 1
        print("FAIL", it["url"], e, flush=True)
    if n % 50 == 0:
        print(f"{n}/{len(items)}", flush=True)
    time.sleep(2)
print(f"done, fail {fail}", flush=True)
