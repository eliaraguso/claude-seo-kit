import time, urllib.request, xml.etree.ElementTree as ET, email.utils, json, sys
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126"}
cut = email.utils.parsedate_to_datetime("Fri, 03 Oct 2025 00:00:00 +0000")
items, page = [], 1
while True:
    url = "https://www.searchenginejournal.com/category/seo/feed/" + (f"?paged={page}" if page > 1 else "")
    xml = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read()
    root = ET.fromstring(xml)
    its = root.findall("./channel/item")
    if not its: break
    stop = False
    for it in its:
        d = email.utils.parsedate_to_datetime(it.findtext("pubDate"))
        if d < cut: stop = True; continue
        items.append({"date": d.date().isoformat(), "title": it.findtext("title"), "url": it.findtext("link"),
                      "cats": [c.text for c in it.findall("category")]})
    if stop: break
    page += 1; time.sleep(2)
sys.stdout.reconfigure(encoding="utf-8"); print(json.dumps(items, ensure_ascii=False))
print(file=sys.stderr, *(len(items), "items, feed pages", page))
