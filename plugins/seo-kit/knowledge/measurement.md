# Measurement: Search Console, GA4, Bing, AI visibility, server logs, traffic drops

> Updated 2026-10-11. Scope: measuring search performance, diagnosing traffic drops, AI visibility and server-log analysis for any site. Primary source: Google Search Central; third-party views marked [SEJ].
> Source tags as in `conventions.md`: `[G](url)` Google documentation or blog · `[SEJ YYYY-MM, author, type, sample, strength]` third-party view reported by Search Engine Journal (evidence, not rule; strength labels are explained in [Third-party views](#third-party-views)) · *(inference)* a deduction of this file that no source states explicitly · ⚠ deprecated or not to be recommended.
> A skill without access to the owner's data can only prepare instructions, regexes and checklists, and read exports the user provides. AI search: `ai-search.md`. Bing: `bing-basics.md`. Myths: `myths-deprecated.md`.

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
  - [Search Console: role and use](#search-console-role-and-use)
  - [Properties: Domain, URL prefix, platform](#properties-domain-url-prefix-platform)
  - [Key reports](#key-reports)
  - [Branded queries filter and the brand / non-brand split](#branded-queries-filter-and-the-brand--non-brand-split)
  - [Generative AI performance report](#generative-ai-performance-report)
  - [Data reliability and limits](#data-reliability-and-limits)
  - [Beyond 16 months: API and exports](#beyond-16-months-api-and-exports)
  - [Search Console + Google Analytics](#search-console--google-analytics)
  - [Crawl Stats report and server logs](#crawl-stats-report-and-server-logs)
  - [Expected timings](#expected-timings)
- [Audit checks](#audit-checks)
- [Procedures](#procedures)
  - [Procedure: diagnosing a traffic drop](#procedure-diagnosing-a-traffic-drop)
  - [Procedure: exporting Search Console data](#procedure-exporting-search-console-data)
  - [Procedure: measuring visibility in AI assistants](#procedure-measuring-visibility-in-ai-assistants)
  - [Procedure: GA4 for AI traffic and leads](#procedure-ga4-for-ai-traffic-and-leads)
  - [Procedure: server log analysis](#procedure-server-log-analysis)
- [Build rules](#build-rules)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

---

## Facts and rules (Google)

### Search Console: role and use
- The official tool for understanding crawling, indexing and performance in Search. Google **strongly** recommends using it, with or without third-party tools. [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- No need to log in every day: new issues arrive by **email**; check **about once a month** or after changes to the site. [G](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- First steps: verify the property → Page indexing report (fix errors and warnings) → consider submitting a sitemap (not mandatory, can speed up discovery) → monitor the Performance report. [G](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- Verifying Search Console (or changing the verification method) **does not affect** indexing or ranking; it is how you receive notifications about manual actions, security issues and legal removals. [G](https://developers.google.com/search/help/office-hours/2023/january) · [G](https://developers.google.com/search/help/small-business-notifications)
- Only **manual actions** are notified; algorithmic changes are not. [G](https://developers.google.com/search/help/office-hours/2022/december)

### Properties: Domain, URL prefix, platform
- **Domain property**: covers http/https, www/non-www and all subdomains; it is the recommended choice for a complete picture. With a **URL-prefix** property, moving from HTTP to HTTPS requires a new property. [G](https://developers.google.com/search/help/office-hours/2024/april) · [G](https://developers.google.com/search/help/crawling-index-faq)
- Subdomains and subdirectories can be added as separate properties without new verification if the domain is already verified. [G](https://developers.google.com/search/help/office-hours/2023/june)
- The **branded queries filter** is available only for **top-level** properties (not path prefixes, not subdomains). [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Data belongs to the property, not to the user who verified it; if verification lapses for a long time the missing data cannot be recovered; the per-account property limit cannot be raised. Better not to depend on the personal account of an employee or an agency. [G](https://developers.google.com/search/help/office-hours/2024/august) · [G](https://developers.google.com/search/help/office-hours/2022/december) · [G](https://developers.google.com/search/help/office-hours/2024/april)
- When a former owner (agency, developer) leaves: **also remove their verification tokens** (Users and permissions → Unused ownership tokens → Remove → Verify removal), otherwise they can regain access. [G](https://developers.google.com/search/blog/2024/04/search-console-ownership-token-management)
- Give a consultant doing an audit **read-only access** only. [G](https://developers.google.com/search/docs/fundamentals/do-i-need-seo)
- **Platform properties** (announced in July 2026, rolled out globally on 29 July 2026): **Instagram, TikTok, X and YouTube** accounts can be added as properties, also for creators without a website; they have a Performance report (clicks, impressions, posts, queries, export), Insights and Goals. Owners who claimed their **Search profile** see the accounts added automatically. LinkedIn and GitHub are not among the platforms named. [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) · [G](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content)

### Key reports
| Report / feature | What it is for | Notes | Source |
|---|---|---|---|
| Performance (Search results) | Clicks, impressions, CTR, average position by query, page, country, device, search appearance, date | **Search type** filter: Web, Image, Video, News (+ a **multimodal** filter since 24 September 2026). AI Overviews and AI Mode are included in the **Web** type | [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/blog/2026/09/web-multimodal-in-sc) |
| Discover / Google News performance | Separate surfaces | Discover: only above a minimum impression threshold; Discover has its own core updates (the first one in February 2026) | [G](https://developers.google.com/search/docs/appearance/google-discover) |
| **24 hours** view | Hourly data, a delay of a few hours | Dashed line = partial data; browser time zone | [G](https://developers.google.com/search/blog/2024/12/recent-data-search-console) |
| Daily / weekly / monthly granularity | Trends and comparisons | Slightly changes the export format | [G](https://developers.google.com/search/blog/2025/12/weekly-monthly-views-search-console) |
| **Annotations** | Mark deploys, migrations, content, campaigns, updates | Right-click on the chart, max 120 characters; visible to every user of the property: no personal data | [G](https://developers.google.com/search/blog/2025/11/custom-chart-annotations) |
| AI-powered configuration (experimental) | Set filters and comparisons in natural language | Search performance only; it can get filters wrong: check them | [G](https://developers.google.com/search/blog/2025/12/ai-powered-configuration) |
| Insights | Clicks/impressions vs the previous period, growing/declining pages and queries, Goals (28 days) | Built into the interface since 2025; **query groups** (AI) only for high-volume properties | [G](https://developers.google.com/search/blog/2025/06/search-console-insights) · [G](https://developers.google.com/search/blog/2025/10/search-console-query-groups) |
| Page indexing | Indexed/excluded pages and reasons | Read as patterns; expected 404s are not a problem | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| URL Inspection | Index status, live test, rendered HTML, screenshot, crawl request | More reliable than `site:` | [G](https://developers.google.com/search/docs/monitor-debug/search-operators) |
| Crawl Stats | Requests, responses, Googlebot type, timings | Read together with Page indexing for technical problems; see [Crawl Stats report and server logs](#crawl-stats-report-and-server-logs) | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Manual actions · Security issues | Manual penalties, malware/phishing | A mandatory check in every drop | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Core Web Vitals · HTTPS | Real field data | | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Rich result status reports | Errors/warnings on the structured data Google read | Retired types disappear from the reports | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Removals · Change of address | Hide URLs (~6 months) · domain/subdomain migration | Change of address is not needed for HTTP→HTTPS or www changes | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Recommendations | Automatic suggestions in Overview | Experimental, only when available | [G](https://developers.google.com/search/blog/2024/08/search-console-recommendations) |
| **Data anomalies** page | Logging errors and changes in data handling | Check it before interpreting a drop | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |

### Branded queries filter and the brand / non-brand split
- **Branded / Non-branded** filter in the Performance report (web, image, video, news) and a card in Insights. Branded queries = the brand name, its variants and misspellings, and products/services unique to the brand. Classification uses an **internal AI-assisted system** (not a regex), works across languages, can make mistakes and has **no effect on ranking**. Top-level properties with enough volume only; available to all eligible sites since 11 March 2026. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Why split: brand queries measure demand for and recognition of the name (people who already know you); non-brand queries measure how well the site wins searches from people who do not know you yet. The two curves move for different reasons, so follow them separately (ME-06) and read a drop in each differently (step 6 of the [traffic-drop procedure](#procedure-diagnosing-a-traffic-drop)). *(inference)*
- If the filter does not appear (small site, URL-prefix property): use a regex filter on queries with the name and its misspellings, and record it in `SEO.md › 9. Monitoring` so every report uses the same one. Examples: a person `(?i)ada ?novak|novak ?ada|adanovak`; a business `northwind`; a consultancy `studio ferri`. Use the distinctive part of the name only: a generic service word (`physio`) or a bare surname (`ferri`) also matches searches by people who do not know the brand (`physio oslo`), which would then be counted as brand. *(inference)* (regex method in [SEJ 2025-12, traffic-drop diagnosis guide, Opinion]).

### Generative AI performance report
- Google facts: dedicated reports on visibility in the generative AI features of **Search (AI Overviews and AI Mode)** and **Discover**; metrics: **impressions**, pages shown, countries, devices (Search only), dates with hourly/daily/weekly/monthly granularity. The data also stays in the overall Performance report. Launched on 3 June 2026 for a subset of sites and **became available to all sites on 31 August 2026**. [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) ([help](https://support.google.com/webmasters/answer/16984139)) The post mentions impressions only, not clicks.
- It is the tool Google points to for measuring visibility in generative features (Discover included). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- How to read it (details from SEJ, reporting Google/Mueller statements):
  - no **query**, no **clicks**, CTR, position or cited passage; no API or BigQuery, export from the UI only; per-page export limited to 1,000 rows [SEJ 2026-08/09, news + Mueller, Strong];
  - an impression counts when the link is visible; links behind "show more" count only if the user expands; in the chart two URLs in the same answer count as 1 for the property, in the table 1 per page [SEJ 2026-08, news, Strong];
  - in the Performance report a link inside an AI Overview **inherits the position of the block**; AI Mode follow-ups count as new queries (queries such as "yes go on" appear) [SEJ 2026-08/09, Mueller, Strong];
  - recent data is preliminary; do not add AI and organic impressions together or compute a blended CTR [SEJ 2026-08, author's opinion].
- Date discrepancy: one SEJ article said the report went "live for everyone on 11 August 2026" [SEJ 2026-08]; the Google blog says 31 August 2026. Use the Google date.
- Regex to isolate conversational artefacts in the Query field: `^(yes|yeah|ok|okay|sure)[?!.,]*$` [SEJ 2026-08, one author's tactic].

### Data reliability and limits
- **Impressions bug**: a logging error **inflated impressions from 13 May 2025 to 27 April 2026** (clicks not affected); Google fixed it without recalculating history. CTR and average position for that period are distorted. Treat late April 2026 as a **discontinuity**; use clicks in comparisons. [SEJ 2026-04/06/10, news on Google's Data anomalies page, Strong] (Google asks you to check that page in every analysis. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops))
- Fixed **Pacific Time** time zone; data delayed by **a couple of days** (except the 24-hour view); Search Console reports the **canonical URL** only; it separates web, image, video, news and Discover; it does not necessarily filter bots. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Filtered totals can exceed the overall total because of Bloom filters (speed at the expense of precision). [G](https://developers.google.com/search/help/office-hours/2023/september)
- Rare queries are anonymised: at query level a large share of the data is missing (~75% of impressions and ~38% of clicks across 10 SaaS sites). [SEJ 2026-01, Indig, 10 B2B sites, Weak-Medium] → always compare the aggregate total with the sum of the queries.
- After the `num=100` parameter was removed (September 2025) impressions normalised (fewer impressions "from tools"). [SEJ 2026-01, Indig, Weak]
- Strange queries in the report: the data is real (what was shown); narrow by country, type or period. [G](https://developers.google.com/search/help/office-hours/2023/may)
- Average position: do not obsess over the absolute value; impressions and clicks are the main metrics. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)

### Beyond 16 months: API and exports
- The interface shows **16 months**. To keep more: the **Search Analytics API** or the **bulk data export to BigQuery**, storing the data in your own systems. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
- API with the `HOUR` dimension and `dataState: HOURLY_ALL`: hourly data for up to **10 days** (the UI shows 24 hours only). [G](https://developers.google.com/search/blog/2025/04/san-hourly-data)
- In the BigQuery export the fields of retired rich results have been `NULL` since 1 October 2025: in queries use `IS NOT TRUE` instead of `NOT field`. [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results)
- For small sites *(inference)*: a monthly export (CSV, or Sheets via the API) of queries, pages, countries and devices is enough as an archive. How to export: [Procedure: exporting Search Console data](#procedure-exporting-search-console-data).

### Search Console + Google Analytics
- Search Console = what happens **before** the visit (impressions, clicks, queries); Google Analytics = what happens **on the site** (pages, engagement, conversions, channels). Source of truth: Search Console for Search performance, Analytics for behaviour. The most comparable metrics: **Search Console clicks vs Analytics sessions**, which will not match: trends are what count. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Official Looker Studio template: Search Console table "URL impression"; Analytics filtered on `Session source = google` and `Session medium = organic`; default range 28 days. Metrics: sessions, **engagement rate** (a session with a key event, or longer than 10 seconds, or ≥2 page views), returning users, clicks, CTR. There is no "right" share of organic traffic. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Causes of discrepancy: Analytics tag missing on some pages, cookie consent refused, time zone, attribution model (the Analytics default is the closest), canonical URLs, traffic breakdowns, non-HTML pages (PDF: turn on enhanced measurement), bots. For maximum precision: Search Console export + GA4 export to BigQuery. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Google asks you to measure the **value of visits** (sales, sign-ups, leads), not just clicks, also for traffic from AI features. [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- Linking tools: link Search Console to Analytics; Site Kit for WordPress. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Google Trends for seasonality and comparison with the sector (up to 5 terms; 30/90-day ranges for how well known a name is). [G](https://developers.google.com/search/docs/monitor-debug/trends-start)

### Crawl Stats report and server logs
- **Crawl Stats** (Settings → Crawl stats) shows Google's crawl requests over time with breakdowns by **response** (200, 301/302, 404, 5xx, DNS or connectivity errors), **file type** (HTML, image, JavaScript, CSS, PDF...), **purpose** (Discovery = a URL not crawled before; Refresh = a recrawl) and **Googlebot type** (Smartphone, Desktop, Image, Video, Page resource load, AdsBot, StoreBot, other agents), plus **host status** (robots.txt fetching, DNS resolution, server connectivity) over the past 90 days. It is meant for advanced users; sites with fewer than about 1,000 pages usually do not need it. Only root-level properties (Domain property, or URL prefix at the root) have it. [G](https://support.google.com/webmasters/answer/9679690)
- Google states that Crawl Stats may differ slightly from your server logs because some requests might not be counted; totals can be much higher than the logs when robots.txt was unavailable for too long (Google counts the crawls it might have made); only the selected domain is included (images on another host are not); http and https are both counted; each hop of a server-side redirect counts as a request; example URLs are samples, not a complete list. [G](https://support.google.com/webmasters/answer/9679690)
- Analytics running in the browser may not give a full or accurate picture of Googlebot activity: use Crawl Stats. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript) Server logs are the other direct record. *(inference)*
- **Verifying Googlebot** in logs: either reverse DNS on the logged IP (`host <ip>`), check that the name ends in `googlebot.com`, `google.com` or `googleusercontent.com`, then forward DNS on that name (`host <name>`) and check it returns the same IP; or match the IP against Google's published IP ranges (CIDR, JSON): `common-crawlers.json` (Googlebot and the other common crawlers), `special-crawlers.json` (e.g. AdsBot), `user-triggered-fetchers.json` and `user-triggered-fetchers-google.json` (user-triggered fetchers), `user-triggered-agents.json` (user-triggered agents), all under `https://developers.google.com/static/crawling/ipranges/`; other Google IPs are in `https://www.gstatic.com/ipranges/goog.json`. Common crawlers resolve to `crawl-***-***-***-***.googlebot.com` or `geo-crawl-***-***-***-***.geo.googlebot.com`. [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests)
- Persistent `5xx` / `429` responses make Google slow down crawling: owner check CI-28 in `crawling-indexing.md`. Crawl budget thresholds, parameter URLs and infinite spaces: `crawling-indexing.md`. Which bots render JavaScript and how AI bots are verified: `ai-search.md` (bot table, AI-10).
- How to analyse logs: [Procedure: server log analysis](#procedure-server-log-analysis).

### Expected timings
| Event | Stated time | Source |
|---|---|---|
| Effect of an SEO change | From a few hours to several months; wait a few weeks before judging | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| Recrawl after a fix | Usually a few days | [G](https://developers.google.com/search/help/debug) |
| Core update | Rollout up to ~2 weeks; analyse **at least one week after it ends**, comparing with a week before it started; recovery in days or several months, sometimes only at the next core update | [G](https://developers.google.com/search/docs/appearance/core-updates) |
| Improvements after a significant drop | Check again after a few weeks; the systems can take months | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Medium-sized site migration | A few weeks, longer for large sites | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Preview controls (`nosnippet` etc.) take effect | Days to months; which control does what (and the Search Console setting for AI features): `ai-search.md` › Controls: what blocks what | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| Recovery from spam | Months of detected compliance | [G](https://developers.google.com/search/docs/appearance/spam-updates) |
| Reconsideration request | Several weeks | [G](https://developers.google.com/search/help/site-position-in-search-faq) |
| First AI citation of new content (third-party figure) | Median ~6.8 days | [SEJ 2026-07, Profound, vendor, Weak] |

---

## Audit checks

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| ME-01 | Domain property verified | DNS verification; if only URL-prefix properties exist, add the Domain one; keep the prefix properties for sections | High | [G](https://developers.google.com/search/help/office-hours/2024/april) |
| ME-02 | Clean access and tokens | Users and permissions: current owners, former agencies removed, unused ownership tokens removed; consultants read-only | High | [G](https://developers.google.com/search/blog/2024/04/search-console-ownership-token-management) |
| ME-03 | Sitemap submitted and read | Sitemaps report: status, discovered URLs; no non-canonical or non-200 URLs | Medium | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| ME-04 | Baseline before every intervention | 16-month export (queries, pages, countries, devices), brand vs non-brand, AI report; a "baseline" annotation; record it in `SEO.md › 7. Baseline` | High | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| ME-05 | Systematic annotations | Annotate launches, migrations, templates, plugins, campaigns, core/spam updates (from the Search Status Dashboard) | Medium | [G](https://developers.google.com/search/blog/2025/11/custom-chart-annotations) |
| ME-06 | Brand vs non-brand tracked separately | Branded filter (if available) or the name regex from `SEO.md › 9. Monitoring`; follow the two curves separately | High | [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter) |
| ME-07 | Visibility in Google's AI features | Generative AI performance report: pages with AI impressions, trend; do not add them to organic impressions | Medium | [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) |
| ME-08 | Impressions-bug discontinuity handled | In 2025–2026 comparisons use clicks; flag the period 13 May 2025 – 27 April 2026 in reports | High | [SEJ 2026-04/10, Google news] |
| ME-09 | Archive beyond 16 months | Monthly export via the API or BigQuery. Raise to High for large sites | Medium | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| ME-10 | Search Console linked to GA4 | Link in GA4; Looker Studio dashboard of clicks vs organic sessions | Medium | [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console) |
| ME-11 | Contact key events in GA4 | See the GA4 procedure: form, `tel:`, `mailto:`, booking, CV/PDF download | High | [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search), *(inference)* |
| ME-12 | AI traffic segmented | Default channel "AI Assistant" + a custom channel group for unrecognised referrers; check "Direct" on the most-cited pages | Medium | [SEJ 2026-05, Google Analytics news, Strong] |
| ME-13 | Lead sites ask "How did you hear about us?" | Field in the contact/booking form (options: Google, ChatGPT/other AI assistant, social, word of mouth, other + free text); same question on the phone. Caveat: applies to sites whose conversion is a contact or booking | High | [SEJ 2026-07/08, Forrester and agency data, Opinion/Weak] |
| ME-14 | Alias of BI-01 — verify there, report once | See BI-01 (site verified in Bing Webmaster Tools, import from Search Console works); sitemap, AI Performance report and IndexNow: `bing-basics.md` | Medium | [Bing](https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b) |
| ME-15 | Microsoft Clarity (optional) | Install if acceptable for privacy/consent: behaviour + Copilot citations and grounding queries | Low | [SEJ 2026-05, Microsoft news, Strong] |
| ME-16 | Fixed set of AI questions | See the AI visibility procedure; monthly or quarterly | Medium | [SEJ 2026-07/09, several authors, Opinion] |
| ME-17 | Server logs reviewed for AI bots and Googlebot | 30 days of logs; most-crawled pages; Googlebot verification: ME-22; AI bots: AI-10 in `ai-search.md`; see the log procedure. Raise to Medium for large sites | Low | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests), [SEJ 2026-07, Pollitt] |
| ME-18 | Business Profile linked to GA4 (local-business) | Link the Business Profile to GA4 (call and direction metrics); profiles grouped in a manager account must be separated first. Caveat: applies to businesses with a Business Profile | Medium | [SEJ 2026-06, Google news, Strong] |
| ME-19 | Monthly check | Search Console emails, Page indexing, Manual actions, Security issues, Performance vs previous month/year | Medium | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| ME-20 | No "Google-internal" metrics from third-party tools | Label DA/DR, "visibility score", "AI score" as vendor metrics | Medium | [G](https://developers.google.com/search/docs/fundamentals/third-party-seo) |
| ME-21 | Platform properties | If the brand publishes on YouTube/Instagram/TikTok/X: add them, compare formats and posts. Raise to Medium when those platforms are a main channel | Low | [G](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) |
| ME-22 | Googlebot in logs verified by IP, not by user agent | Match log IPs against `common-crawlers.json` (and the other range files) or reverse + forward DNS; report verified / spoofed / unverifiable shares; base every log conclusion on verified lines only. Caveat: applies when server logs are available | Medium | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests) |
| ME-23 | Crawl Stats and server logs tell the same story | Compare daily requests and the status-code mix of verified Googlebot with Crawl Stats (same days); explain large gaps (CDN answering without origin logs, other hosts, unavailable robots.txt, filter too strict or too loose). Caveat: root-level property and logs needed | Low | [G](https://support.google.com/webmasters/answer/9679690), *(inference)* |
| ME-24 | Status-code mix per site section is healthy | From verified Googlebot lines: share of 2xx / 3xx / 4xx / 5xx per first path segment; a section with many 3xx/4xx or any 5xx spike needs action (5xx/429 → CI-28) | Medium | [G](https://support.google.com/webmasters/answer/9679690), *(inference)* |
| ME-25 | Googlebot crawl not wasted on noindex, parameter or redirected URLs | Share of verified hits on URLs with `?`, on redirects and on pages marked `noindex`; fix the links or rules that expose them (thresholds and rules: `crawling-indexing.md`). Raise to High for large sites | Medium | [G](https://support.google.com/webmasters/answer/9679690), *(inference)* |
| ME-26 | Key pages crawled regularly | Last verified Googlebot hit for each page listed in `SEO.md › 4` and for new pages; flag key pages with no hit in 30 days | Medium | [G](https://support.google.com/webmasters/answer/9679690), *(inference)* |

---

## Procedures

### Procedure: diagnosing a traffic drop
Order designed to rule out trivial causes first. Main sources: [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) · [G](https://developers.google.com/search/docs/appearance/core-updates); third-party additions are marked.
1. **Is it a measurement problem?** Does the drop appear in all GA4 channels? Do Search Console and GA4 diverge? Tag missing after a release, cookie consent changed, CDN blocking scripts? [SEJ 2025-10/12, checklists by several authors] · Search Console **Data anomalies** page and the 2025–2026 impressions bug. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
2. **Known incidents and updates**: Search Status Dashboard (incidents, core/spam updates with dates). If a core update is rolling out, wait for it to end + one week. [G](https://developers.google.com/search/help/status-dashboard)
3. **Shape of the chart** (16 months): sudden collapse → update, security, spam, site-wide technical problem; slow decline → wrong `noindex` on pages (it depends on recrawling) or changing interests; recurring dip → seasonality. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
4. **Comparison**: last 3 months vs the previous period and vs the previous year; go through every tab (queries, pages, countries, devices, search appearance). [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
5. **Clicks vs impressions**: both down → the causes above; impressions stable and clicks down → weak title/snippet or competitors with richer results. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) Also consider AI Overviews appearing on the main queries (CTR falls when an AI Overview is shown) [SEJ 2026-03/05, several studies, Medium].
6. **Brand vs non-brand**: a drop in non-brand only points to competition/ranking; a brand drop points to demand or reputation. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
7. **Search type**: Web, Image, Video, News separately; Discover separately (it has its own core updates). [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
8. **Pages affected**: Pages table sorted by "Clicks difference"; whole site → Page indexing report; a group of pages → URL Inspection on a few of them. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
9. **Size of the position loss**: small (e.g. 2 → 4) → fluctuation, no radical changes; large (e.g. top 10 → 29) across many terms → assess the whole site with the helpful-content questions. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
10. **Technical**: Crawl Stats (error spikes, response times), Page indexing, robots.txt, server/DNS, CDN/WAF blocking Googlebot, `noindex`/canonical left over from staging; server logs if available ([log procedure](#procedure-server-log-analysis)). [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
11. **Security and spam**: Security issues and Manual actions reports. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
12. **External demand**: one query at a time in Google Trends to tell a site drop from a sector drop. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
13. **Recent migration or redesign**: one-to-one 301 redirects, no forgotten `noindex`, canonicals updated, content/titles not removed; the Internet Archive for comparison. [G](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [SEJ 2026-06, guide, Opinion]
14. **Decision**: no quick changes "because people say so"; make substantial improvements; delete content only as a last resort; do not buy links. [G](https://developers.google.com/search/docs/appearance/core-updates)
15. **Annotate** the actions and check again after a few weeks. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)

### Procedure: exporting Search Console data
Used by `seo-monitor` (`analyze_gsc.py`) and for the monthly archive of small sites (ME-04, ME-09).
1. Open **Performance → Search results** (Discover and News have their own reports). Keep the search type on **Web** unless the question is about images, video or news; export those separately.
2. Set the date range. For a comparison, export each period separately (for example the last 3 months and the 3 months before, or the same months of the previous year) and pass the older export with `--previous`. Keep the same filters on both exports.
3. **Export → Download CSV**. The download is a `.zip` with one CSV per tab (queries, pages, countries, devices, search appearance, dates, filters); `analyze_gsc.py` accepts the `.zip` or the unzipped folder.
4. **Language of the export**: Search Console localises the CSV file names and column headers into the account language. `analyze_gsc.py` recognises exports in Italian, English, German, Spanish, Portuguese and French, with either `,` or `;` as delimiter. For any other language, switch the Search Console interface to English before exporting.
5. Totals: anonymised queries are missing from the queries file, so the sum of clicks per query is lower than the real total; the reliable total is in the dates (chart) file. For more rows than the UI export holds, use the API or the BigQuery export (row cap: see [Third-party views](#third-party-views)).
6. Do not share exports outside the team that needs them; if a file is stored in the project, keep it out of version control. *(inference)*

### Procedure: measuring visibility in AI assistants
There is no official third-party metric; Google points to its own AI report and warns against tools that promise internal metrics. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **The protocol** (accuracy questions, fixed decision questions, engines, repetitions, reading, frequency) is owned by `ai-search.md` › Procedures ("Procedure: AI visibility with fixed questions"); the fixed questions of a site live in `SEO.md › 9. Monitoring`. This file holds the measurement side only.
- **Google's own data**: the generative AI performance report in Search Console (ME-07, [facts above](#generative-ai-performance-report)); AI traffic in GA4 through the "AI Assistant" channel and a custom channel group (ME-12, [GA4 procedure](#procedure-ga4-for-ai-traffic-and-leads)).
- **Logging template** (one row per run): date · engine · model · account (free/paid) · location · language · question · result (cited with a link / named without a link / absent) · cited URL · competitors named · answer length · number of brands in the answer (a longer answer inflates presence) · notes. [SEJ 2026-07, Manic] One proposed alarm threshold when reading the sheet: present in fewer than 12 runs out of 20. [SEJ 2026-08, consultant, single case] *(inference: indicative threshold only)*
- **Reachability test** (note it in the sheet): search ChatGPT for an exact sentence of the page to check that it can be retrieved. [SEJ 2026-10, Chris Green, tactic]
- **Link to outcomes**: cross-check with AI traffic in GA4, brand searches in Search Console and "How did you hear about us?" answers. Presence in answers is neither a ranking nor a business KPI. [SEJ 2026-07, Forrester; Manic]

### Procedure: GA4 for AI traffic and leads
- **Default channel "AI Assistant"** (since 13 May 2026, medium `ai-assistant`): automatically assigns recognised referrers (ChatGPT, Gemini and Claude were named); the full list is not public; no retroactive data. According to one author it does not recognise Perplexity. [SEJ 2026-05/07/10, Google Analytics news, Strong; Pollitt for Perplexity]
- **Custom channel group** for referrers not covered *(inference; check against the property's real referrers)*: condition "Session source matches regex", placed **before** Referral:
  ```
  (^|\.)(chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|meta\.ai|grok\.com|chat\.mistral\.ai|chat\.deepseek\.com)$
  ```
  Starting domains given by [SEJ 2025-10, guide]: chatgpt.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com. ChatGPT often adds `utm_source=chatgpt.com` to links; Gemini also adds UTM parameters [SEJ 2026-03/06/09]. App users and visits without a referrer end up in "Direct".
- **Key events** recommended *(inference, consistent with Google's advice to measure conversions)*: contact/booking form submission (`generate_lead`), clicks on `tel:`, `mailto:`, WhatsApp, external booking links, CV/PDF download (enhanced measurement `file_download`); for local businesses, calls and directions from the linked Business Profile.
- **Explorations**: a funnel with an organic/AI segment to see where leads drop off [SEJ 2025-12, tutorial, Opinion]; Landing page report filtered on Google organic. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Do not expect GA4, Search Console and the CRM to match: one source of truth per question (visibility = Search Console, behaviour = GA4, leads = CRM or contact log). [SEJ 2026-04, guide, Opinion], consistent with [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)

### Procedure: server log analysis
When: large sites, after a migration, when Crawl Stats shows anomalies, or when new or updated pages take long to be indexed. Small sites (under about 1,000 pages) rarely need it. [G](https://support.google.com/webmasters/answer/9679690) Google documents how to verify its crawlers and what Crawl Stats shows; the analysis steps below are *(inference)* built on those documents.
1. **Collect** at least 30 days of access logs (90 days matches the Crawl Stats host-status window) from the origin **and** the CDN, since a CDN can answer requests that never reach the origin. Fields needed: timestamp, client IP, method, URL with query string, status, bytes, user agent (response time if available). Logs contain personal data (IP addresses): work on an extract of bot lines and follow the site's retention rules. *(inference)*
2. **Verify Googlebot (ME-22)**: keep lines whose user agent claims Googlebot, then keep only those whose IP falls in Google's published ranges (`common-crawlers.json` for Googlebot; the other range files for special crawlers and user-triggered fetchers) or passes reverse + forward DNS. Report the unverified "Googlebot" lines separately. [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests) (How often bot names are spoofed: Third-party views, "Bots in logs".) For AI bots use the same method with each operator's published list (AI-10 in `ai-search.md`).
3. **Compare with Crawl Stats (ME-23)**: same days, daily request count and status-code mix. Small differences are expected (Google says some requests might not be counted); large gaps mean the logs are incomplete (CDN, other hosts), robots.txt was unavailable, or the verification filter is wrong. [G](https://support.google.com/webmasters/answer/9679690)
4. **Compute**, on verified lines only:
   - **status-code mix per section** (first path segment): share of 2xx / 3xx / 4xx / 5xx (ME-24);
   - **crawl of URLs that should not take crawl time**: parameter URLs (`?sort=`, `?filter=`, session IDs), redirected URLs, pages marked `noindex`, 404s reached through old links (ME-25); thresholds and fixes in `crawling-indexing.md`;
   - **crawl frequency of key pages**: hits and last hit date for each page in `SEO.md › 4`, and days from publication to first hit for new pages (ME-26);
   - **5xx / 429 bursts**: count per hour and match them against deploys, traffic peaks and WAF/CDN rules; persistent errors → CI-28 in `crawling-indexing.md`.
5. **Recipe** (tool-agnostic, Apache/Nginx "combined" format, where `$1` = IP, `$4` = time, `$7` = path, `$9` = status; adjust the field numbers to your format):
   ```
   # 1. lines that claim to be Googlebot
   grep -i 'googlebot' access.log > gb.log
   # 2. keep only IPs in Google's published ranges
   python -c "import json,ipaddress,sys,urllib.request as u; P=json.load(u.urlopen('https://developers.google.com/static/crawling/ipranges/common-crawlers.json'))['prefixes']; N=[ipaddress.ip_network(p.get('ipv4Prefix') or p.get('ipv6Prefix')) for p in P]; sys.stdout.writelines(l for l in sys.stdin if any(ipaddress.ip_address(l.split()[0]) in n for n in N))" < gb.log > gb-verified.log
   # 3. status-code mix per first path segment
   awk '{split($7,u,"?"); split(u[1],p,"/"); c["/" p[2] " " $9]++} END {for (k in c) print k, c[k]}' gb-verified.log | sort
   # 4. share of hits on parameter URLs
   awk '$7 ~ /\?/ {n++} END {print n+0, "of", NR, "verified hits on parameter URLs"}' gb-verified.log
   # 5. 5xx/429 per hour
   awk '$9 ~ /^(5..|429)$/ {split($4,t,":"); c[t[1] ":" t[2]]++} END {for (k in c) print k, c[k]}' gb-verified.log | sort
   # 6. last hit per path (logs in time order)
   awk '{split($7,u,"?"); last[u[1]]=$4} END {for (k in last) print k, last[k]}' gb-verified.log
   ```
   Pages marked `noindex` are not visible in the log: join the paths with a list of `noindex` URLs from a crawl or from the Page indexing report. *(inference)*
6. **Report** the findings by severity with the check IDs (ME-22..ME-26, CI-28), annotate any fix in Search Console, and repeat the analysis after a few weeks.

---

## Build rules
Pointers only; the checks are in [Audit checks](#audit-checks).
- At launch or migration: verify a Domain property → ME-01, give access only to who needs it → ME-02, submit the sitemap → ME-03, link Search Console to GA4 → ME-10.
- Before any intervention on a live site: take a baseline and record it in `SEO.md › 7. Baseline` → ME-04; annotate each deploy, migration and campaign → ME-05.
- Configure contact key events and the AI channel group when analytics is installed → ME-11, ME-12; add the "How did you hear about us?" field to contact and booking forms → ME-13.
- Set up Bing Webmaster Tools at launch → ME-14 (details in `bing-basics.md`).
- Keep server and CDN access logs for at least 30 days with IP, full URL, status and user agent, so that crawl questions can be answered → ME-17, ME-22.
- Record the brand regex and the fixed AI questions in `SEO.md › 9. Monitoring` → ME-06, ME-16.

## Notes by site type
Archetypes as in `archetypes.md`.

**ecommerce**
- Merchant Center has an "AI performance insights" pilot (US only, only for merchants with a feed): queries grouped for AI Mode/AI Overviews and share of voice, without clicks. [SEJ 2026-07, Google news, Strong] Link GA4 with purchase events and compare with the Search Console export per product page.
- Log analysis (ME-25) matters most here: faceted and sorting parameters are the usual crawl sink. *(inference)*

**editorial**
- Separate Search, Discover and News; follow the AI report for Discover; Discover has its own core updates. [G](https://developers.google.com/search/blog/2026/02/discover-core-update) Record the impressions-bug dates in year-on-year comparisons.

**local-business**
- KPIs: calls, directions and bookings (Business Profile linked to GA4, ME-18), Business Profile post views (a new metric, last 18 months) [SEJ 2026-09, Google news, Strong], non-brand "service + city" queries.
- AI traffic outside opening hours (almost two thirds) and ~1–2% of calls from AI citations in a sample of local businesses. [SEJ 2026-09, CallRail/Wiideman, vendor, Weak]
- Call tracking with dynamic numbers swapped in the browser does not work for AI bots that do not run scripts; keep one canonical number consistent everywhere. [SEJ 2026-09, Opinion]
- The "How did you hear about us?" field (ME-13), at the desk and on the phone too.

**personal-brand**
- Main KPIs: impressions and clicks on **queries with the name** (branded filter or regex), CTR of the name results page, contacts and clicks to professional profiles, email and CV download as key events. Non-brand volume will be low: measure it per niche (role + skill). *(inference)*
- The branded filter and query groups may not appear because of low volume: use the regex (e.g. `(?i)ada ?novak|novak ?ada|adanovak`). [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Platform properties for YouTube/Instagram/TikTok/X if used; accuracy questions about the name (namesakes) every quarter. [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) · [SEJ 2026-07, Opinion]

**professional-services**
- KPIs: contact and booking requests, calls, non-brand "service + city" queries; brand regex such as `studio ferri` (not the bare surname, which also matches unrelated searches).
- The "How did you hear about us?" field and the same question on the phone: for a professional it is often the most reliable measure of the influence of Google, AI and word of mouth. [SEJ 2026-08/09, Opinion]

**saas-product**
- Measure sign-ups/demos per channel including "AI Assistant"; B2B/SaaS AI traffic is the most sensitive to ChatGPT changes (a jump on 7 May 2026 of +157.7% in ChatGPT referrals, +200% for B2B/SaaS). [SEJ 2026-07, Profound/Similarweb, vendor, Weak]

---

## Third-party views
Evidence strength for third-party sources: **Strong** (official vendor announcement or documentation, as reported) · **Medium** (large study with a stated method, but correlational) · **Weak** (small sample, single account, vendor data, anecdote) · **Opinion**. Third-party figures are attributed and dated; they are not Google rules.
- **Bing Webmaster Tools – AI Performance**: public preview since February 2026 with total citations, cited pages per day, citations per page and **grounding queries** (phrases the AI used to retrieve content); grounding query → page mapping (March); Citation Share, Intents, Topics, Compare (June, preview). It covers Copilot, Bing summaries and partners, on a sample; **no clicks**. Search Console has no per-citation equivalent. [SEJ 2026-02/03/06, Microsoft news, Strong] Details: `bing-basics.md`.
- **Microsoft Clarity**: shows grounding queries and Copilot citations to everyone (May 2026) and insights on AI referrals; free. [SEJ 2025-11, 2026-05, Microsoft news, Strong] One author saw 1–3 citations according to Ahrefs and more than 36,000 according to Copilot/Clarity for the same site. [SEJ 2026-06, Taylor, single case] → third-party citation tools see a tiny fraction.
- **IndexNow** (Bing, Yandex, Naver, Seznam, Yep; not Google) to notify Bing of updates; its benefit on AI answers has not been measured. [SEJ 2026-04/05, Opinion]
- **AI visibility protocols**: the steps and their sources are in `ai-search.md` › Procedures ("Procedure: AI visibility with fixed questions"). Additional evidence on why several runs are needed: lists change almost every time; ~1,500 repetitions would be needed to get two identical lists, and agreement on the first brand across 3 models was 41.6%. [SEJ 2026-07, Fishkin/SparkToro; SEJ 2026-08]
- **Search Console UI export rows**: Google's Performance report help page does not state a row limit for exports [G](https://support.google.com/webmasters/answer/7576553); practitioners commonly report a cap of 1,000 rows per table *(re-verify)*. The generative AI report export is limited to 1,000 rows per page [SEJ 2026-08/09, news + Mueller, Strong]. For more rows use the API or the BigQuery export.
- **Prompt tracking**: useful only as a repeated survey; as "rank tracking" it is a vanity metric [SEJ 2026-07, Manic and others, Opinion]; with GPT-5.3 the tools that read sub-query metadata broke [SEJ 2026-03, Forrester]; recommendations changed in 80.2% of cases with active search, citation–recommendation correlation 0.4 [SEJ 2026-07, Visibility Labs, 20,000 answers, vendor].
- **Mention ≠ citation ≠ click ≠ conversion**: measure them separately. [SEJ 2026-09, several authors, Opinion]
- **Brand searches as a proxy for AI influence**: 55.9% of the traffic that follows a ChatGPT recommendation goes through a brand search. [SEJ 2026-06, Similarweb, Weak-Medium]
- **"How did you hear about us?"**: at one agency 80–90% of the leads that came from AI showed up as organic or direct in analytics. [SEJ 2026-08, one agency's data, Weak] Several authors recommend the field for "dark funnel" influence. [SEJ 2025-10, 2026-07]
- **Bots in logs**: spoofed names are frequent (81.8% of AI fetches and ~87% of fake "Googlebot" hits on a new site; fake CCBot requests looking for `.env` files). Verify IP and reverse DNS before drawing conclusions; do not report "AI fetches" as success. [SEJ 2026-06/08, Forrester; nohacks case, Weak]
- **GA4 data at zero**: empty standard reports were reported for many properties on 1 September 2026 (Realtime kept working). [SEJ 2026-09/10, news, Weak] → check for data gaps before reading a drop.
- **Impressions inflated by AI systems**: some authors hypothesise impressions generated by query fan-out without human clicks ("impressions up, clicks down" is not always human demand). [SEJ 2026-07, Manic, unverified hypothesis]
- **Cadence recommended by one author**: monitoring with GA4 anomaly alerts; a monthly report with a year-on-year comparison; a quarterly technical audit (Search Console and Bing), plus on-page, link and local listing (NAP) audits. [SEJ 2025-12, Opinion]

## Myths and outdated advice
Full list: `myths-deprecated.md`.
- "Verifying Search Console helps rankings": it does not; it only gives access to data and notifications. [G](https://developers.google.com/search/help/office-hours/2023/january)
- "`site:` shows what is indexed": use URL Inspection and the Page indexing report. [G](https://developers.google.com/search/docs/monitor-debug/search-operators)
- "Average position is the KPI": impressions and clicks are the main metrics. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
- "There is a right share of organic traffic": Google gives none. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- "DA/DR or an AI score are Google metrics": they are vendor metrics (ME-20). [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- "Browser analytics shows Googlebot activity": it may not represent it fully or accurately; use Crawl Stats (and server logs, *(inference)*). [G](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)
- ⚠ Vendor figures used as benchmarks: "AI = 15% of traffic" (BrightEdge), "AI converts 2–4x" (Forrester, no sample given), "+393% AI retail traffic" (Adobe, US retail). Do not use them as targets or norms. [SEJ 2026-03/06]
