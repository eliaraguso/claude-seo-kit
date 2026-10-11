# Bing basics

> Updated 2026-10-11. Scope: what a site needs for Bing and Copilot on top of the Google work: Bing Webmaster Tools, bingbot access and verification, robots.txt `crawl-delay`, `noarchive`/`nocache` for Copilot, IndexNow and URL submission, Bing Places. Primary source: Bing Webmaster documentation `[Bing]`; Google rules live in the other files; third-party views marked [SEJ].
> Related files: `crawling-indexing.md` (robots.txt, sitemaps, redirects, WAF) · `ai-search.md` (AI bots and controls) · `measurement.md` (Bing reports in the monthly review) · `local-seo.md` (listings and NAP).

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
  - [Same as Google](#same-as-google) · [What differs from Google](#what-differs-from-google) · [Bing crawlers and verification](#bing-crawlers-and-verification)
  - [robots.txt and crawl rate](#robotstxt-and-crawl-rate) · [Robots meta tags and Copilot](#robots-meta-tags-and-copilot) · [Discovery: sitemaps, IndexNow, URL submission](#discovery-sitemaps-indexnow-url-submission)
  - [Bing Webmaster Tools](#bing-webmaster-tools) · [Bing Places](#bing-places)
- [Audit checks](#audit-checks)
- [Procedures](#procedures)
- [Build rules](#build-rules)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

## Facts and rules (Google)

The section name is fixed by the template; in this file every rule comes from Bing documentation or the IndexNow protocol site; Google's side is in the files linked by check ID. Bing's help centre renders with JavaScript; its pages were read on 2026-10-11 through the help centre's own content endpoint.

### Same as Google
- Bing and Copilot use the same crawling, indexing and ranking foundation as classic search; practices that help discovery, indexing accuracy and clarity also help eligibility for grounding results and citations. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- Crawlable `<a href>` links with descriptive anchor text or image `alt`; every important URL reachable through internal links; one URL per piece of content (canonical, consistent URLs); `404` for deleted content; 301 for permanent moves. → RJ-05, CI-22, CI-26. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- Unique, non-empty `<title>` and meta description, logical `H1`–`H6`, semantic HTML; missing, duplicate or very short titles and descriptions "may reduce indexing reliability". → OP-01, OP-02, OP-08. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- Structured data must match visible content and does not guarantee visibility; Bing reads Schema.org (Microdata, JSON-LD, RDFa), Microformats and Open Graph, and has no preferred syntax. → `structured-data.md`. [Bing](https://www.bing.com/webmasters/help/marking-up-your-site-with-structured-data-3a93e731)
- Do not hide critical content behind client-side rendering; Bingbot renders with the current stable Microsoft Edge engine, but "content that cannot be reliably rendered may not be indexed". → RJ-01. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
- Abuse list close to Google's spam policies: cloaking, link schemes, duplicate and scraped content, keyword stuffing and "artificially engineered language", scaled auto-generated content, thin affiliate pages, malware, misleading structured data, and **prompt injection or AI manipulation** aimed at Bing or Copilot models. → `content-quality-spam.md`. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)

### What differs from Google
| Topic | Bing | Google |
|---|---|---|
| `crawl-delay` in robots.txt | Supported; overrides the Crawl Control setting in Bing Webmaster Tools | Ignored (CI-05) |
| `noarchive` / `nocache` | Live controls for Copilot and for training Microsoft's models | Obsolete (CI-12) |
| Instant change notification | IndexNow (shared with other participating engines); URL and Content Submission APIs | No IndexNow; sitemaps and Search Console |
| Setup | Bing Webmaster Tools can import verified sites and sitemaps from Search Console | — |
| Temporary redirects | `302` only for very short changes (under 2 days); for moved content use redirects, not canonical tags | `302`/`307` for temporary moves (CI-20) |
| Crawler verification | Reverse DNS ends in `search.msn.com`, then forward DNS; or `bingbot.json`, refreshed daily | `googlebot.com`/`google.com`, Google IP JSON (CI-44, CI-46) |
| Local listings | Bing Places (see below) | Google Business Profile |

Sources: [Bing](https://www.bing.com/webmasters/help/crawl-control-55a30303) · [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240) · [Bing](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b) · [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing](https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26)

### Bing crawlers and verification
- Main crawlers: **Bingbot** (standard crawler, desktop and mobile UAs containing `bingbot/2.0`), **AdIdxBot** (Bing Ads quality control), **BingPreview** and **MicrosoftPreview** (page snapshots), **BingVideoPreview** (video previews). [Bing](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
- User agents are easy to spoof. Verify an IP with: reverse DNS → name ending in `search.msn.com` → forward DNS of that name returns the same IP; or the Verify Bingbot tool (in Bing Webmaster Tools or public at `bing.com/toolbox/verify-bingbot`); or match against `https://www.bing.com/toolbox/bingbot.json`, **refreshed daily**. Do not hardcode IP ranges. [Bing](https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26) · [Bing](https://www.bing.com/webmasters/help/verify-bingbot-2195837f)

### robots.txt and crawl rate
- robots.txt controls crawling, not indexing; to keep a URL out of Bing, Copilot and grounding results use `noindex` on a crawlable URL. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing](https://www.bing.com/webmasters/help/how-to-permanently-remove-a-url-or-page-from-bing-or-copilot-37c07477)
- When Bingbot finds a group for itself it **ignores the generic `*` group**, so a `User-agent: bingbot` group must repeat every generic rule; Bing does not recommend per-bot groups because they are a common source of crawl problems. File in ASCII or UTF-8 at the root; Bing caches it "at least for a few hours". [Bing](https://www.bing.com/webmasters/help/how-to-create-a-robotstxt-file-cb7c31ec)
- `crawl-delay` is placed in a bot-specific group (example: `User-agent: Bingbot` / `Crawl-delay: 1`). The pages read do not define the unit or a safe value. [Bing](https://www.bing.com/webmasters/help/how-to-create-a-robotstxt-file-cb7c31ec)
- **Crawl Control** in Bing Webmaster Tools sets the crawl rate for each of the 24 hours relative to a baseline that Bing calculates (for example, slower during business hours). A `crawl-delay` in robots.txt **always takes precedence** over it. [Bing](https://www.bing.com/webmasters/help/crawl-control-55a30303)
- Blocking Bingbot in robots.txt is listed among things to avoid; a wrong robots.txt is one of the causes listed in "Why is my site not in the index?", together with a new site not yet crawled, crawl errors, no inbound links, `noindex`, URLs blocked in Bing Webmaster Tools, low quality and penalties. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing](https://www.bing.com/webmasters/help/why-is-my-site-not-in-the-index-2141dfab)
- Content sent through the Content Submission API is indexed even if robots.txt disallows it (Bing does not apply the `Disallow` rule there); `noindex` is still honoured. [Bing](https://www.bing.com/webmasters/help/url-submission-62f2860b)

### Robots meta tags and Copilot
- Each value works in `<meta name="robots">`, in `<meta name="bingbot">` (Bing only) and in the `X-Robots-Tag` header; values are combined with commas. [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240)
- `noindex`: not indexed (the page must be crawlable). `nosnippet` and `data-nosnippet`: no caption or thumbnail for the page or the marked part, and possibly weaker Copilot citations. `max-snippet`, `max-image-preview`, `max-video-preview`: as at Google. [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240) · [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- `noarchive`: not used in Copilot answers or grounding results, not linked in Copilot, not used to train Microsoft's generative AI foundation models. `nocache`: Copilot may show only URL, title and snippet; only those are used for training. Both together are treated as `nocache`. Pages with either tag **still appear in Bing search results**. [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240) · [Bing 2023-09](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat)
- For richer citations, avoid `nocache` on content meant for Copilot. For paywalled sites that use only `noarchive`, Bing suggested adding `nocache` so articles can still appear in chat answers. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing 2023-09](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat)
- The guidelines also mention a `data-snippet` attribute "to specify allowed content"; no specification page for it was found in the help centre. *(re-verify)* [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)

### Discovery: sitemaps, IndexNow, URL submission
- Discovery uses IndexNow, XML sitemaps, crawlable internal links and external links; a new site needs at least one inbound link to be found. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing](https://www.bing.com/webmasters/help/why-is-my-site-not-in-the-index-2141dfab)
- Sitemaps: XML (and index files), RSS 2.0, Atom 0.3/1.0, text; only canonical URLs, deleted or redirected URLs removed promptly, accurate `lastmod`; `ETag` helps Bing detect changes. Submit in Bing Webmaster Tools or reference with `Sitemap:` in robots.txt; sitemaps imported from Search Console are listed too; Bing typically reads sitemaps once a day. [Bing](https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed) · [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Bing](https://www.bing.com/webmasters/help/url-submission-62f2860b)
- **IndexNow**: notify when URLs are added, updated or deleted; Bing says to avoid batch submissions when possible, because streaming submissions are faster. The IndexNow FAQ says to wait at least 5 minutes before resubmitting a frequently updated URL; its `429` answer says 10 minutes. Key: 8–128 characters (letters, digits, `-`) in a UTF-8 file `{key}.txt` at the host root whose content is the key (or elsewhere with `keyLocation`, covering only that path); each subdomain needs its own key. GET for one URL, POST JSON up to 10,000 URLs. Responses: `200` ok, `202` key pending validation, `400` bad format, `403` key not valid, `422` URL or protocol mismatch, `429` too many requests. Submit only changed URLs, including redirected and `404`/`410` URLs; keep sitemaps as well; no guarantee of indexing. [IndexNow](https://www.indexnow.org/documentation) · [IndexNow](https://www.indexnow.org/faq) · [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- One submission is shared with every participating engine. The list published by the protocol on 2026-10-11: Bing, Yandex, Seznam, Naver, Yep, Internet Archive, Amazonbot. **Google is not on it.** Many CMS and CDNs have built-in support (WordPress plugin, Cloudflare, Shopify, Drupal and others). [IndexNow](https://www.indexnow.org/searchengines.json) · [Bing](https://www.bing.com/webmasters/help/indexnow-0z209wby)
- **URL Submission**: manual in Bing Webmaster Tools or by API, up to 10,000 URLs per domain per day (reset at midnight UTC, API batches of up to 500, OAuth 2.0); repeated manual submissions do not speed up indexing. Bing calls IndexNow "strongly recommended" and says the URL and Content Submission APIs "may be deprecated in the future". [Bing](https://www.bing.com/webmasters/help/url-submission-62f2860b)

### Bing Webmaster Tools
- Free account (Microsoft, Google or Facebook sign-in). Add a site by **importing from Google Search Console** (sites are verified automatically and sitemaps are imported, also later ones) or manually, as a domain or a single branch (`example.com/clothing/`). Up to 100 sites per import, 1,000 per account; data appears after about 48 hours. [Bing](https://www.bing.com/webmasters/help/getting-started-checklist-66a806de) · [Bing](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b)
- Manual verification: DNS auto-verification (Domain Connect providers), `BingSiteAuth.xml` at the root, a `<meta>` tag at the end of the home page `<head>`, or a CNAME record. [Bing](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b)
- Useful reports: URL Inspection, Site Explorer, Sitemaps, IndexNow (including "Important URLs missed": URLs indexed in the last 7 days but not through IndexNow), Crawl Control, Block URLs, robots.txt tester, SEO reports every other week, and **AI Performance** (citations in Copilot, Bing AI summaries and some partners, with grounding queries; it does not measure rankings or clicks). → `measurement.md`. [Bing](https://www.bing.com/webmasters/help/getting-started-checklist-66a806de) · [Bing](https://www.bing.com/webmasters/help/indexnow-0z209wby) · [Bing](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)
- Check indexing with the `url:` operator on Bing followed by the URL, or with URL Inspection. Bing does not index every page. [Bing](https://www.bing.com/webmasters/help/why-is-my-site-not-in-the-index-2141dfab)

### Bing Places
- `bingplaces.com` redirects (301) to `bing.com/forbusiness/`, a JavaScript app whose text could not be read on 2026-10-11. Official documentation on import from Google Business Profile, verification and where listings appear was therefore **not verified**; what follows is third-party (see [Third-party views](#third-party-views)). [Bing](https://www.bing.com/forbusiness/)
- Bing's own guidelines ask for consistent naming of people, organisations, products and locations; this is what listing consistency serves. → LO-02. [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)

## Audit checks

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| BI-01 | Site added and verified in Bing Webmaster Tools (import from Search Console or manual) | Ask the owner for access; otherwise `curl -s https://domain/BingSiteAuth.xml` or grep the home `<head>` for the Bing verification meta (usually `msvalidate.01`, *(inference)*). A DNS-verified site leaves no trace in HTML: ask | Medium | [Bing](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b) |
| BI-02 | Sitemap known to Bing and processed without errors | Bing Webmaster Tools › Sitemaps: status, last processed date, URLs discovered; else `Sitemap:` line in robots.txt (CI-08). Sitemap content rules: CI-13, CI-14 | Medium | [Bing](https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed) |
| BI-03 | robots.txt does not block Bingbot; a `User-agent: bingbot` group, if present, repeats every generic rule | Read the groups that apply to `bingbot` (named group, else `*`): no `Disallow: /`, no missing rules; Bing Webmaster Tools robots.txt tester. Google side: CI-03, CI-06. Caveat: if a named group that drops the `*` rules also affects Google, report it once under CI-06 | Critical | [Bing](https://www.bing.com/webmasters/help/how-to-create-a-robotstxt-file-cb7c31ec) |
| BI-04 | CDN/WAF does not block or challenge Bingbot | `seo_fetch.py` field `ua_comparison.bingbot` (status, bytes, `challenge_suspect`) against `browser`; confirm with URL Inspection live test in Bing Webmaster Tools. Caveat: the script spoofs the UA from a non-Bing IP, so a WAF that verifies IPs may block it correctly; trust the URL Inspection result. CDN AI-bot categories: CI-31 | Critical | [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) |
| BI-05 | Bingbot allowlists and log checks use reverse + forward DNS (`search.msn.com`) or `bingbot.json` refreshed daily, not hardcoded IP ranges | WAF/firewall rule export; `host <IP>` → `host <name>`; Verify Bingbot tool | Medium | [Bing](https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26) |
| BI-06 | `crawl-delay` (for `bingbot` or `*`) does not throttle Bing more than intended; Crawl Control preferred for load management | `curl -s https://domain/robots.txt \| grep -i -B3 crawl-delay`; Bing Webmaster Tools › Crawl Control and crawl errors. Caveat: Bing publishes no safe value; raise to High when new or changed URLs stay "discovered but not crawled" or crawl errors appear | Medium | [Bing](https://www.bing.com/webmasters/help/crawl-control-55a30303) |
| BI-07 | No active Block URLs or content removal in Bing Webmaster Tools on pages meant to be indexed | Bing Webmaster Tools › Block URLs / Content Removal: list of active blocks | High | [Bing](https://www.bing.com/webmasters/help/why-is-my-site-not-in-the-index-2141dfab) |
| BI-08 | Home page and key pages indexed in Bing | Search `url:https://domain/page` on Bing; URL Inspection; Site Explorer. If missing, walk the causes in "Why is my site not in the index?" | Medium | [Bing](https://www.bing.com/webmasters/help/why-is-my-site-not-in-the-index-2141dfab) |
| BI-09 | IndexNow set up (CMS plugin, CDN feature or own code) | Bing Webmaster Tools › IndexNow: URLs submitted and sources; CMS/CDN settings. Caveat: Medium for editorial and ecommerce sites or any site that changes daily | Low | [Bing](https://www.bing.com/webmasters/help/url-submission-62f2860b) |
| BI-10 | IndexNow key file valid: `https://host/{key}.txt` returns `200`, UTF-8 text equal to the key, 8–128 characters `[A-Za-z0-9-]`, one per host/subdomain | `curl -s -w "%{http_code} %{content_type}" https://domain/{key}.txt` (key from the plugin/CDN settings or the `key` parameter in logs); submissions answered `403`/`422` mean a bad key or host. Caveat: applies only when IndexNow is used | Medium | [IndexNow](https://www.indexnow.org/documentation) |
| BI-11 | IndexNow fires on publish, update and delete (incl. redirects and `404`/`410`), only for changed URLs | Publish or edit a test page, then check the sample list in Bing Webmaster Tools › IndexNow; "Important URLs missed" should be near empty; no repeated resubmission of unchanged URLs in logs | Low | [IndexNow](https://www.indexnow.org/faq) · [Bing](https://www.bing.com/webmasters/help/indexnow-0z209wby) |
| BI-12 | No unintended `noarchive` or `nocache` (meta `robots`/`bingbot` or `X-Robots-Tag`) on content meant to be cited in Copilot | `seo_fetch.py` fields `robots_meta` and `x_robots_tag` (the script reads `robots`/`googlebot` only: also `curl -s URL \| grep -i 'name="bingbot"'`). Caveat: a deliberate choice (paywall, licensing) passes; CI-12 calls these values obsolete for Google, so do not remove them without asking about Bing | Medium | [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240) |
| BI-13 | Bing Places listing claimed and verified for a business with an address or service area | Ask the owner for the listing or search the business name on Bing Maps. Caveat: local-business only; official help could not be read, details from third parties | Medium | [Bing](https://www.bing.com/forbusiness/) · [SEJ 2025-10](https://www.searchenginejournal.com/microsoft-launches-new-bing-places-for-business/557520/) |
| BI-14 | Alias of LO-02 — verify there, report once | Bing Places name, address, phone, hours and categories against the site and Google Business Profile | High | [SEJ 2025-10](https://www.searchenginejournal.com/microsoft-launches-new-bing-places-for-business/557520/) |

## Procedures

### Set up Bing in 15 minutes (new or existing site)
1. Sign in to Bing Webmaster Tools; if the site is in Search Console, choose **Import** (verification and sitemaps come along). Otherwise add the domain and verify with DNS or `BingSiteAuth.xml`. → BI-01
2. Sitemaps: confirm the imported sitemap or submit it; check that robots.txt has a `Sitemap:` line. → BI-02
3. robots.txt: no `Disallow: /` for Bingbot, no `bingbot` group that drops generic rules, no `crawl-delay` unless the server really needs it (use Crawl Control instead). → BI-03, BI-06
4. Run URL Inspection on the home page; if it fails while browsers work, check the WAF/CDN. → BI-04
5. Turn on IndexNow in the CMS or CDN (or add the key file and a publish hook), then publish a test change and watch the IndexNow report. → BI-09, BI-10, BI-11
6. Local businesses: claim the Bing Places listing (import from Google Business Profile where offered) and compare its data with the site. → BI-13, BI-14
7. Two days later: Search Performance, AI Performance and Site Explorer have data; record the baseline in `SEO.md › 7. Baseline`.

## Build rules
- Generate robots.txt with one `*` group; add a `bingbot` group only if needed, copying every generic rule into it. → BI-03
- Do not ship `crawl-delay` by default in templates or CMS presets. → BI-06
- Wire IndexNow into the publish, update and delete events of the CMS or deploy pipeline; serve the key file as static UTF-8 text. → BI-09, BI-10, BI-11
- Add `noarchive`/`nocache` only on an explicit decision recorded in `SEO.md › 8. Decisions and constraints`. → BI-12
- Allowlist Bingbot by DNS verification or the daily `bingbot.json`, never by a copied IP list. → BI-05

## Notes by site type
- **ecommerce**: Bing Shopping and Shopping campaigns run on Microsoft Merchant Center feeds, outside the pages read here *(re-verify in Microsoft Advertising documentation)*; IndexNow on price and stock changes helps Bing refresh product URLs. → BI-09
- **editorial**: IndexNow is the main lever for fast discovery of new articles and corrections; paywalled sites choose between `noarchive` and `nocache` deliberately. The help centre also has Bing News PubHub guidelines (not reviewed here). → BI-11, BI-12
- **local-business**: claim Bing Places and keep it identical to the site and Google Business Profile. → BI-13, BI-14
- **personal-brand**: name queries on Bing and Copilot depend on consistent entity naming across the site and profiles. → `entity-personal-brand.md`

## Third-party views
- [SEJ 2025-10, Microsoft news](https://www.searchenginejournal.com/microsoft-launches-new-bing-places-for-business/557520/) Bing Places relaunched on 3 October 2025 at `bing.com/forbusiness`, free, with a faster import from Google Business Profile, bulk edits and status dashboards. Third-party guides describe the import as re-runnable rather than an automatic sync, and list phone, email and postcard verification. *(re-verify)*
- [SEJ 2026-02, news on Microsoft documentation] Bing rewrote its Webmaster Guidelines in early 2026, adding Copilot/grounding wording, GEO and the prompt-injection abuse category (consistent with the page read on 2026-10-11).
- [SEJ 2026-07, Microsoft news] The Bing index and its grounding API also serve AI products outside Bing; see `ai-search.md`.
- A secondary source reports that Bing removed cache links in December 2024, leaving Copilot as the main effect of `noarchive`. *(re-verify)*

## Myths and outdated advice
- **"`crawl-delay` is ignored by every engine"**: ignored by Google, honoured by Bing, where it overrides Crawl Control. [Bing](https://www.bing.com/webmasters/help/crawl-control-55a30303)
- **"`noarchive` and `nocache` are dead"**: true for Google (CI-12), not for Bing and Copilot. [Bing](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240)
- **"IndexNow also notifies Google"**: Google is not a participating engine. [IndexNow](https://www.indexnow.org/searchengines.json)
- **"Submitting a URL again and again speeds up indexing"**: Bing says repeated manual submissions do not; IndexNow asks not to resubmit unchanged URLs. [Bing](https://www.bing.com/webmasters/help/url-submission-62f2860b) · [IndexNow](https://www.indexnow.org/faq)
- **"IndexNow replaces sitemaps"**: use both. [IndexNow](https://www.indexnow.org/faq)
- **Meta keywords for Bing**: the current guidelines name title, meta description, headings and structured data, never the `keywords` meta; treat it as irrelevant, as for Google (`myths-deprecated.md`). *(inference)* [Bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
