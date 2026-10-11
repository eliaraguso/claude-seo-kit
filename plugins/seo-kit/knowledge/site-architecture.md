# Site architecture

> Updated 2026-10-11. Scope: how pages are organised and linked (hierarchy and hubs, click depth, URL folders, crawlable navigation, breadcrumbs, internal links, orphan pages, blog taxonomies, sitelinks, one page per topic). Primary source: Google Search Central; third-party views marked [SEJ].
> Source tags, ⚠ and the severity scale follow `conventions.md`. Related files: `crawling-indexing.md` (URL format, facets, internal search, pagination, sitemaps), `rendering-javascript.md` (links created by JavaScript), `on-page-appearance.md` (anchor text, sitelinks and breadcrumb appearance), `structured-data.md` (`BreadcrumbList`, `WebSite`), `content-quality-spam.md` (cannibalisation, doorways), `ecommerce.md` (categories and filters; EC-05 product links from categories, EC-07 key products linked from the home page).

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
  - [How Google discovers and weighs pages through links](#how-google-discovers-and-weighs-pages-through-links) · [Hierarchy, hubs and click depth](#hierarchy-hubs-and-click-depth) · [URLs and folders](#urls-and-folders)
  - [Crawlable navigation](#crawlable-navigation) · [Breadcrumbs](#breadcrumbs) · [Internal links and anchor text](#internal-links-and-anchor-text) · [Orphan pages and sitemaps](#orphan-pages-and-sitemaps)
  - [Internal search, facets and pagination](#internal-search-facets-and-pagination) · [Blog taxonomies: tags, categories, archives](#blog-taxonomies-tags-categories-archives) · [Sitelinks and site name](#sitelinks-and-site-name) · [One topic per page](#one-topic-per-page)
- [Audit checks](#audit-checks)
- [Procedures](#procedures)
- [Build rules](#build-rules)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

## Facts and rules (Google)

### How Google discovers and weighs pages through links
- Google primarily finds pages through links from pages it has already crawled; the vast majority of new pages Google finds every day are found through links. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- If a site's pages are properly linked, Google can usually discover most of the site. "Proper linking" means every page you deem important can be reached through some form of navigation. [G](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- Google uses the link structure to judge how important pages are **relative to each other**: it can consider the number of links it needs to follow to reach a page, and the more internal links point to a page, the higher its relative importance. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- Crawling is necessary to appear in results, but it is not a ranking signal. [G](https://developers.google.com/crawling/docs/myths-about-crawling)

### Hierarchy, hubs and click depth
- Organise the site in a logical way: it helps search engines and users understand how pages relate. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- Build a chain of links: from menus to category pages, from category pages to sub-category pages, and from there to the individual pages. Pages must be reachable by following links through the site's navigation. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- To signal that a page matters (e.g. a best-selling product), link to it from the home page or from other content such as blog posts. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- **Click depth.** Google's statement is "partly true": pages linked directly from the home page *may* be seen as more important and therefore crawled more often, but this does not mean they will rank higher than other pages of the site. Google gives **no fixed maximum depth**. [G](https://developers.google.com/crawling/docs/myths-about-crawling)
- What follows is deduction, not a Google rule: the more clicks a page sits from the home page, the fewer internal links it usually receives and the more it depends on the sitemap for discovery; a hub page per section (category, service overview, topic page) keeps important pages a few links from the home page without putting everything in the menu. *(inference)*

### URLs and folders
- Use descriptive URLs with readable words, not random identifiers; parts of the URL can be shown as breadcrumbs in results, and Google learns breadcrumbs automatically from the words in the URL. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- On sites with more than a few thousand URLs, grouping topically similar pages in directories (folders) can help Google learn how often the URLs in each directory change. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- At the same time, Google **generally does not look at the structure of URLs to work out the structure of a site**: the hierarchy is read from links, not folders. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- URL format rules (hyphens, case, parameters, fragments, session IDs, root-relative links) are owned by `crawling-indexing.md` › URL structure (→ CI-33) and `on-page-appearance.md` (→ OP-18). Google states it can crawl parameters; "clean URLs only" is not a requirement. [G](https://developers.google.com/search/docs/crawling-indexing/url-structure) · [G](https://developers.google.com/crawling/docs/myths-about-crawling)

### Crawlable navigation
- Google can generally only crawl a link if it is an `<a>` element with an `href` that resolves to a real web address. `<a routerLink>`, `<span href>`, `<a onclick>` without `href` and `href="javascript:…"` are not recommended. Links inserted by JavaScript are fine when the final markup is a standard `<a href>`. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Do not use JavaScript events on other DOM elements for navigation; use `<a href>` for links to other content. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- Menus, footers, breadcrumbs, "load more" and pagination all follow this rule. The owning check is RJ-05 (crawlable navigation); infinite scroll is RJ-22.

### Breadcrumbs
- A breadcrumb trail indicates the page's position in the site hierarchy and lets users move up one level at a time. Google recommends breadcrumbs that represent a **typical user path** to the page rather than mirroring the URL structure; a page reachable by several paths may carry several trails. [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)
- Since **23 January 2025** mobile results no longer show breadcrumbs: the visible URL on mobile is the domain only. Desktop results still show domain + breadcrumb, and `BreadcrumbList` markup is still supported (Rich Results Test, Search Console report). [G](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs)
- Markup rules (≥ 2 `ListItem`, `position` from 1, `item` on every element except the last) are owned by `structured-data.md` (→ SD-21). This file owns the visible, linked breadcrumb as part of navigation (→ SA-11). The breadcrumb's appearance in results is described in `on-page-appearance.md` › Breadcrumbs and visible URL.

### Internal links and anchor text
- Every page you care about should have a link from at least one other page on your site. Think about which other resources on the site help readers understand a given page and link to them **in context**. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- There is **no magical ideal number** of links per page; "if you think it's too much, then it probably is." [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Anchor text: descriptive, reasonably concise, relevant to both pages; not "click here"; no keyword cramming (keyword stuffing is a spam-policy violation); the words around the link matter; do not chain links next to each other. For image links the anchor is the `alt`. Owning check: OP-15. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Internal links should point to canonical URLs, not to redirects or parameter variants (→ CI-23, CI-47). Long redirect chains have a negative effect on crawling. [G](https://developers.google.com/crawling/docs/crawl-budget)

### Orphan pages and sitemaps
- An orphan page is a page that exists (in the sitemap, in the CMS, in Search Console) but receives no internal link. Google's own wording is the positive rule above: every page you care about needs at least one internal link. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- A sitemap helps when it is hard to make sure every page is linked by at least one other page (large sites), for new sites with few external links, and for rich media; it does **not** guarantee that its URLs are crawled and indexed. A sitemap complements links; it does not replace them. [G](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- On ecommerce sites: if category pages do not link to all products, Googlebot might not find them by crawling; Google "strongly recommends" linking to every product you want indexed, and only where that is not possible, using a sitemap or a Merchant Center feed. Products reachable only through the search box may not be found: Googlebot generally does not submit searches. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- Google's crawl-budget guide does not discuss orphan pages as such; it says to keep sitemaps up to date and to eliminate duplicate content so crawling focuses on unique content rather than unique URLs. [G](https://developers.google.com/crawling/docs/crawl-budget)
- Ownership: the orphan check is CI-47; click depth is owned here (SA-03). This file supplies the measurement method for both in [Procedures](#procedures).

### Internal search, facets and pagination
- **Internal search result pages** are an infinite URL space. The decision (robots.txt `Disallow` vs `noindex`, never both) lives in `crawling-indexing.md` › Internal search result pages (→ CI-34, CI-09, CQ-17). Architectural consequence: do not link to search result URLs from navigation, tag clouds or "popular searches" blocks. *(inference)*
- **Facets and filters** multiply URLs when combined; Google recommends blocking problematic filter and sort URLs or handling them as described in its faceted-navigation guide. Rules and checks: `crawling-indexing.md` › URL structure, parameters and facets (→ CI-34) and `ecommerce.md`. [G](https://developers.google.com/search/docs/crawling-indexing/url-structure)
- **Pagination** stays crawlable and self-canonical, linked with `<a href>`: `crawling-indexing.md` › Pagination (→ CI-22, RJ-22, OP-41).

### Blog taxonomies: tags, categories, archives
- Google's documentation is **thin** on tag, category, author and date archives: no page addresses them directly. The applicable general rules are: eliminate duplicate content so crawling focuses on unique content [G](https://developers.google.com/crawling/docs/crawl-budget); avoid mass-produced low-value pages (→ CQ-03); sitelinks benefit from avoiding repetition in content [G](https://developers.google.com/search/docs/appearance/sitelinks).
- Deductions from those rules: a tag with one or two posts, near-duplicate tags (`/tag/widget` and `/tag/widgets`), a category that lists the same posts as another, or date and author archives on a single-author blog produce many URLs that repeat the same snippets; keep a small set of taxonomies that work as real topic hubs (own introduction, curated links) and either merge the rest or keep them out of the index with `noindex`. *(inference)*

### Sitelinks and site name
- Sitelinks are automated and derived from the site's link structure; Google shows them only when useful, and there is no way to request them. What helps: a logical site structure, informative and compact titles and headings, concise and relevant internal anchors, no repetition. [G](https://developers.google.com/search/docs/appearance/sitelinks)
- To remove a page from sitelinks, the only documented options are to remove the page from the site or to use `noindex`. [G](https://developers.google.com/search/docs/appearance/sitelinks)
- Site name (`WebSite` on the home page, one name per domain or subdomain, subdirectories not supported) is owned by `structured-data.md` (→ SD-10) and explained in `on-page-appearance.md` › Site name.

### One topic per page
- Search engines choose one canonical URL per piece of content; duplicate content is not a spam violation, but it splits signals and wastes crawling. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G](https://developers.google.com/crawling/docs/crawl-budget)
- Architectural deduction: give each search intent recorded in `SEO.md › 4` one designated page in the hierarchy, and link other pages to it with consistent anchors; two pages that answer the same intent compete with each other (cannibalisation, → CQ-31). Doorway variants by city or keyword are a spam issue (→ CQ-02). *(inference)*

## Audit checks

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| SA-01 | Logical hierarchy: home → sections → pages; each section has a hub page (category, service overview, topic page) that links with `<a href>` to the pages in it | Group the sitemap URLs (the `pages[].url` added by `seo_fetch.py --sitemap N --json`, see [Procedures](#procedures); `site.sitemaps.sitemaps[].sample_urls` holds only the first 20) by section (first path folder or template); for each group find the hub whose `internal_links[].resolved` contains the members; list pages with no hub. Compare with the main menu in the rendered DOM | Medium | [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) |
| SA-02 | Alias of EC-07 — verify there, report once | See EC-07 (key products and categories linked from the home page or other prominent pages). Method: `seo_fetch.py` on the home page → `pages[0].internal_links[].resolved`; Search Console › Links › Top internally-linked pages. Other site types apply the same test to services, About and contact (Facts › Hierarchy, hubs and click depth) | Low | [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) |
| SA-03 | Key pages sit within a few clicks of the home page. Google sets no fixed limit: pages linked directly from the home page "may be seen as more important, and therefore crawled more often", which does not mean they rank higher | Depth histogram from `seo_fetch.py` output per [Procedures](#procedures): flag key pages (those in `SEO.md › 4`) at depth ≥ 4 from the home page or reachable only through long pagination *(inference: 4 is a triage heuristic, not a Google number)*. Pages with no depth at all are orphans: CI-47 (SA-04) | Medium | [G](https://developers.google.com/crawling/docs/myths-about-crawling) |
| SA-04 | Alias of CI-47 — verify there, report once | See CI-47 (no important orphan page; internal links point to canonical URLs). Sitemap-vs-links comparison per [Procedures](#procedures); Search Console › Pages: "Discovered – currently not indexed" URLs that the crawl never reached are likely candidates *(inference)* | Medium | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| SA-05 | Alias of RJ-05 — verify there, report once | See RJ-05 (menus, footer, breadcrumbs and pagination as crawlable `<a href>`). Compare `anchors_without_href` and the number of `internal_links` in `seo_fetch.py` (raw HTML) with the rendered DOM | High | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| SA-06 | Alias of EC-05 — verify there, report once | See EC-05 (every product meant for indexing linked with `<a href>` from a category or subcategory page, not only through site search or JS events). Method: union of `internal_links[].resolved` of each listing page and its paginated pages (pass them as URLs to `seo_fetch.py`) vs the item URLs from the sitemap (`pages[].url` added by `--sitemap N`). Blog and service listings follow the same rule (Facts › Orphan pages and sitemaps) | High | [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) |
| SA-07 | Contextual links in the main content to related pages (article → service or product, product → related guides, service → case studies), not only menu and footer links | Rendered DOM: `document.querySelectorAll('main a[href], article a[href]')` on key templates; or Grep the build output for links inside the content container | Low | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| SA-08 | Alias of OP-15 — verify there, report once | See OP-15 (descriptive anchors; no empty links; image links with `alt`). Extract anchors from the rendered DOM; read each anchor out of context | Medium | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| SA-09 | No template with an excessive number of links (mega-menu listing every product, tag cloud, footer listing every city or service). Google: "There's no magical ideal number of links a given page should contain", but "if you think it's too much, then it probably is" | Number of `internal_links` per page in `seo_fetch.py` output: compare each template with the site median and inspect outliers, e.g. several hundred links *(inference: a triage heuristic, not a Google number)*. Footer lists of cities: see CQ-04 | Low | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| SA-10 | URL folders reflect the sections: topically similar pages share a directory with readable words; no flat mix of IDs (`/p?id=123`) and folders for the same content type | Group the sitemap URLs (`pages[].url` added by `--sitemap N`) by first path segment; flag ID-only paths and the same content type spread over several folders. Caveat: do not change existing URLs only for this; if a change is made, follow the migration rules (CI-49) | Low | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| SA-11 | Visible breadcrumb on pages below the first level, each step an `<a href>` to its parent, following the typical user path | Rendered DOM: `nav[aria-label*="breadcrumb" i] a[href]` (or the theme's breadcrumb container) on a sample of deep pages; compare steps with the hub pages of SA-01 | Low | [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) |
| SA-12 | Alias of SD-21 — verify there, report once | See SD-21 (`BreadcrumbList` structure consistent with the visible breadcrumb). Rich Results Test; Search Console › Breadcrumbs report. Effect visible on desktop only since 23 January 2025 | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) |
| SA-13 | Blog taxonomies do not bloat the index: no indexable tags with one or two posts, near-duplicate tags, or date/author archives duplicating the blog home | Count `/tag/`, `/category/`, `/author/`, `/YYYY/MM/` URLs in the sitemap and crawl vs number of posts; Search Console › Pages: "Crawled – currently not indexed" concentrated on these patterns. Caveat: raise to Medium when archives outnumber posts. Official documentation is thin (see Facts) *(inference)* | Low | [G](https://developers.google.com/crawling/docs/crawl-budget) |
| SA-14 | (informational) Unwanted sitelinks are handled only with `noindex` or page removal; no expectation that markup or a setting chooses sitelinks | Search for the brand name on desktop and mobile; list sitelinks; check that pages meant to be hidden carry `noindex` (CI-10) | Low | [G](https://developers.google.com/search/docs/appearance/sitelinks) |
| SA-15 | Each search intent in `SEO.md › 4` maps to one designated page of the hierarchy (no intent without a page, no intent split over two pages) | Compare the intent table with the sitemap; Search Console › Performance › query → Pages tab with several URLs of the site; overlapping content measured as in CQ-31 *(inference)* | Medium | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| SA-16 | Internal link distribution matches priorities: key pages are among the most internally linked; utility pages (login, cookie policy, tag pages) do not dominate | Search Console › Links › Top internally-linked pages (a sample, at most 1,000 rows); or count inbound links per URL from `internal_links[].resolved` of all fetched pages | Low | [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) · [G](https://support.google.com/webmasters/answer/9049606) |

## Procedures

**Depth histogram and orphan candidates from `seo_fetch.py`.** The script reads raw HTML only and fetches the URLs you give it plus up to N sitemap URLs; it does not follow links. The result is therefore an approximation, valid for small and medium sites.

1. Run `python seo_fetch.py https://acme-widgets.example --no-ua --json site.json` once and read the sitemap URL count in `site.sitemaps.total_urls` (all declared sitemaps, child sitemaps of an index included; each `site.sitemaps.sitemaps[]` entry has its own `url_count`, while `files[].children` counts child sitemaps, not URLs). If an entry has `truncated: true` the script stopped early and the count is a lower bound.
2. Fetch the home page, every sitemap URL and any hub or paginated listing that is not in the sitemap, with N = that count: `python seo_fetch.py https://acme-widgets.example https://acme-widgets.example/widgets?page=2 --sitemap N --no-ua --json crawl.json` (do not use `--no-site`: without `site` no sitemap is read). The output does not list every sitemap URL (`sample_urls` keeps 20 per sitemap): the sitemap URLs are the `pages[]` entries added after the URLs you passed (`requested_urls`).
3. Run a breadth-first search from the home page over the internal links, after mapping every requested URL and redirect hop to its final URL:

```python
# Schema: seo_fetch.py 1.0 (requested_urls, pages[].url, pages[].final_url, pages[].chain[].url,
# pages[].internal_links[].resolved, pages[].error, site.sitemaps.total_urls)
import json, collections
r = json.load(open("crawl.json", encoding="utf-8"))
norm = lambda u: (u or "").split("#")[0].rstrip("/")
alias = {}  # requested URL and every redirect hop -> final URL
for p in r["pages"]:
    final = norm(p.get("final_url") or p["url"])
    for u in [p["url"]] + [h.get("url") for h in p.get("chain") or []]:
        alias[norm(u)] = final
canon = lambda u: alias.get(norm(u), norm(u))
links = {canon(p["url"]): {canon(l["resolved"]) for l in p.get("internal_links") or [] if l.get("resolved")}
         for p in r["pages"] if not p.get("error")}
home = canon(r["pages"][0]["url"])
depth, queue = {home: 0}, collections.deque([home])
while queue:
    cur = queue.popleft()
    for nxt in links.get(cur, ()):
        if nxt not in depth:
            depth[nxt] = depth[cur] + 1
            queue.append(nxt)
requested = {norm(u) for u in r["requested_urls"]}
sitemap = {canon(p["url"]) for p in r["pages"] if norm(p["url"]) not in requested}  # added by --sitemap N
print(len(sitemap), "of", r["site"]["sitemaps"]["total_urls"], "sitemap URLs fetched")
print(sorted(collections.Counter(depth.values()).items()))  # depth histogram
print(sorted(sitemap - set(depth)))                         # orphan candidates
```

4. Read the results: orphan candidates are sitemap URLs never reached from the home page (SA-04 / CI-47); the histogram shows how many pages sit at each depth (SA-03). Limits: sitemap URLs you also passed on the command line are not counted as sitemap URLs; pages that were not fetched (N smaller than the sitemap, sitemaps the script could not read) contribute no outgoing links, so pages linked only from them also appear as candidates; host case and http/https/www variants are not normalised (CI-17 handles those). Before reporting, check the candidates in the rendered DOM: links added by JavaScript are invisible to the script (→ RJ-01, RJ-05). On large sites use a dedicated crawler or the Search Console Links report instead.

## Build rules

1. **Plan the tree before the pages**: home → sections with a hub page each → individual pages; every page belongs to one section. → SA-01, SA-15
2. **Link the money pages from the home page** or from the global navigation; keep the menu to sections, not to every page. → SA-02, SA-09
3. **Only `<a href>` navigation**, rendered in the server HTML where possible; no buttons, `select` menus or click handlers as links. → SA-05 (RJ-05)
4. **Every new page gets at least one contextual link** from a related page and a link from its hub at publish time; add it to the sitemap too. → SA-04, SA-06, SA-07
5. **Readable, grouped URLs** chosen once at launch; changes only with a 1:1 redirect map. → SA-10, CI-33, CI-49
6. **Visible breadcrumb + `BreadcrumbList`** on pages below the first level, built from the same data so they never diverge. → SA-11, SA-12 (SD-21)
7. **Listings link to items** through crawlable, self-canonical pagination; filters and internal search stay out of the crawlable link graph per `crawling-indexing.md` › Internal search result pages. → SA-06, CI-34
8. **Taxonomies are hubs, not tag clouds**: create a tag or category only when it will hold several posts and has its own introduction. → SA-13
9. **Descriptive anchors** that match the target page's topic. → SA-08 (OP-15)

## Notes by site type

- **ecommerce**: categories → sub-categories → products as the main chain; every product linked from at least one category (pagination crawlable), best sellers also from the home page or editorial content; filters and sort orders handled per CI-34 and `ecommerce.md`; products reachable only via search are not found by crawling (→ EC-05, EC-07). Example: Acme Widgets links `/widgets/` → `/widgets/waterproof/` → product pages. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- **editorial**: hub pages by topic (an introduction plus curated links to the best articles), linked from the menu; tag pages limited to real topics (SA-13); related-article links in the body; date archives are rarely useful as entry points. *(inference)*
- **local-business**: one page per **real** location, each linked from a locations hub and from the contact page, with distinct content; never one page per city served without a location (→ CQ-02, LO-13). Example: Northwind Physio has one clinic page for Oslo and a service page per treatment. *(inference)*
- **personal-brand**: a small, flat structure is enough: home, About (entity home, → EN-01), projects or writing, contact; every page one click from the home page; project pages link back to About. Example: adanovak.example. *(inference)*
- **professional-services**: one page per service (not a single page listing everything), linked from a services hub and from the home page; case studies and articles link to the service they illustrate. Example: Studio Ferri Orientamento with one page per service. *(inference)*
- **saas-product**: separate sections for features, use cases, integrations, comparison pages ("<product> vs <competitor>", "alternatives") and docs; docs keep their own hierarchy with breadcrumbs; marketing pages link to the relevant docs and vice versa. *(inference)*

## Third-party views

- No third-party source is used in this file. Industry heuristics such as a "three-click rule", "flat architecture" or "silos" are not Google rules; the Google position on depth is in [Hierarchy, hubs and click depth](#hierarchy-hubs-and-click-depth).

## Myths and outdated advice

- "Every page must be within three clicks of the home page" → Google documents no required depth; its myths page calls "the closer your content is to the home page the more important it is" partly true: such pages may be crawled more often, which does not mean they rank higher. [G](https://developers.google.com/crawling/docs/myths-about-crawling)
- "Google reads the site structure from the folders in the URL" → Google generally does not look at URL structure to work out the site structure; links define it. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- "Keep each page under 100 links" → there is no magical ideal number of links per page. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- "Google does not like query parameters; only clean URLs get crawled" → false: Google can crawl parameters. [G](https://developers.google.com/crawling/docs/myths-about-crawling)
- "A sitemap is enough, internal links are optional" → a sitemap does not guarantee crawling or indexing; every important page needs an internal link. [G](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- "`nofollow` on internal links stops Google from crawling those URLs" → a URL is still crawled if another link to it is followed; `nofollow` is meant for untrusted, paid or user-generated links. [G](https://developers.google.com/crawling/docs/myths-about-crawling) · [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- "`noindex` saves crawl budget" → Google still requests the page before dropping it; use robots.txt for URLs that should not be crawled. [G](https://developers.google.com/crawling/docs/crawl-budget)
- "Breadcrumb markup shows the trail in mobile results" → since 23 January 2025 mobile results show the domain only; the trail appears on desktop. [G](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs)
- "Sitelinks can be chosen with markup or a Search Console setting" → sitelinks are automated; the only control is `noindex` or removing the page. The sitelinks search box was retired (see `on-page-appearance.md` › Sitelinks). [G](https://developers.google.com/search/docs/appearance/sitelinks)
- "Put keywords in folder names to rank" → near-zero effect; see `myths-deprecated.md` (keyword in the domain or URL).
