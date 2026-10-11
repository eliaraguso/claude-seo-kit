# Research backlog

> Generated 2026-10-11 from the knowledge base. Claims still marked *(re-verify)*, framework details marked "not verified" in the adapters, and deductions marked *(inference)*. Work through it at the next knowledge refresh: confirm on the cited page (for Google, also on the changelog `developers.google.com/search/updates`), then remove the marker or reword the claim.

Regenerate the raw list with:

```
grep -rnE '\(re-verify\)|not verified|unverified|not confirmed|\(inference\)' plugins/seo-kit/knowledge --include=*.md
```

Totals: 35 *(re-verify)*, 20 "not verified", 149 *(inference)* in 29 files. *(re-verify)* and "not verified" come first: they are claims to confirm. *(inference)* items are deductions no source states; check them only if a source may now state them.

Each line: kind · line number · check ID or section · excerpt.

## `ai-search.md` (2 re-verify, 11 inference)

- **re-verify** · L237 · Where assistants get their sources · [SEJ 2026-01/05, opinion, Weak] (re-verify)
- **re-verify** · L302 · JavaScript and AI bots · …earlier version of this file also listed CCBot as rendering; sources disagree and Common Crawl does not document it, so the bot table says "not documented" (re-verify)
- **inference** · L98 · Google agents and fetchers · To really block an area you need authentication, not robots.txt. (inference)
- **inference** · L113 · AI crawlers and fetchers · …bots honour robots.txt (the page does not name Claude-User individually); as with every user-triggered fetcher, do not rely on robots.txt for private areas (inference)
- **inference** · L121 · AI crawlers and fetchers · …bots honour robots.txt (the page does not name Claude-User individually) [Anthropic help center]. For anything that must stay private, use authentication. (inference)
- **inference** · L122 · AI crawlers and fetchers · …the Vercel 2024 test with later checks [SEJ 2025-12, Vercel/Gabe, test, Medium]; see [JavaScript and AI bots](#javascript-and-ai-bots). Practical consequence (inference)
- **inference** · L196 · Notes by site type · …For an example such as Acme Widgets, the product page (specs, sizes, shipping and returns in text) is the citable source, not the category listing (inference)
- **inference** · L208 · Notes by site type · Realistic AI goal: assistants describe the person correctly (name, role, skills, city) and associate them with a niche; traffic from AI will be minimal (inference)
- **inference** · L212 · Notes by site type · …wants to be found by clients or employers through assistants (e.g. Ada Novak) should not block OAI-SearchBot, Claude-SearchBot, PerplexityBot, ChatGPT-User (inference)
- **inference** · L222 · Notes by site type · …I…" questions: keep them public, in the initial HTML (not only in a client-rendered docs app), linked from the main site, with one canonical version per page (inference)
- **inference** · L243 · Where assistants get their sources · …Google was reflected in citations: −27.8% ChatGPT, −23.8% AI Mode, −2.9% Perplexity [SEJ 2026-02, Lily Ray, 11 selected subfolders, Weak]. Cautious reading (inference)
- **inference** · L285 · What correlates with citations · Summary (inference)
- **inference** · L308 · Real traffic from chatbots · …sites] against conversions lower than almost every channel [SEJ 2026-07, Marketing Science, 973 sites]; "2–4x" [SEJ 2026-03, Forrester, no sample]. Reading (inference)

## `bing-basics.md` (3 re-verify, 1 not verified, 2 inference)

- **re-verify** · L60 · Robots meta tags and Copilot · The guidelines also mention a data-snippet attribute "to specify allowed content"; no specification page for it was found in the help centre. (re-verify)
- **re-verify** · L123 · Third-party views · …and status dashboards. Third-party guides describe the import as re-runnable rather than an automatic sync, and list phone, email and postcard verification. (re-verify)
- **re-verify** · L126 · Third-party views · A secondary source reports that Bing removed cache links in December 2024, leaving Copilot as the main effect of noarchive. (re-verify)
- **not verified** · L76 · Bing Places · …text could not be read on 2026-10-11. Official documentation on import from Google Business Profile, verification and where listings appear was therefore not verified
- **inference** · L83 · BI-01 · Ask the owner for access; otherwise curl -s https://domain/BingSiteAuth.xml or grep the home <head> for the Bing verification meta (usually msvalidate.01, (inference))
- **inference** · L134 · Myths and outdated advice · …guidelines name title, meta description, headings and structured data, never the keywords meta; treat it as irrelevant, as for Google (myths-deprecated.md). (inference)

## `content-quality-spam.md` (4 re-verify, 1 not verified, 3 inference)

- **re-verify** · L63 · Who, how, why · …explicit warning was reported by SEJ as a 1 October 2026 update of the English guide and is not yet in the Google documentation we could read. [SEJ 2026-10] (re-verify)
- **re-verify** · L75 · AI-generated content · …by hand before publishing. Reported by SEJ as a 1 October 2026 update of the English guide, not yet in the Google documentation we could read. [SEJ 2026-10] (re-verify)
- **re-verify** · L168 · CQ-21 · High — [SEJ 2026-10] (re-verify)
- **re-verify** · L238 · Third-party views · [SEJ 2026-10] (re-verify)
- **not verified** · L251 · Third-party views · [SEJ 2026-07, forum case] Partial "thin content" manual action on a forum whose AI chatbot answered as a staff member: the cause is a hypothesis, not confirmed
- **inference** · L4 · Content quality, AI, updates and spam · Tags (see conventions.md): [G](url) Google documentation or blog · [G OH YYYY-MM](url) Google Search Office Hours · (inference)
- **inference** · L139 · Recovering from traffic drops · Recommended order (inference)
- **inference** · L230 · Notes by site type · …registers, certifications, issuing bodies); topics close to YMYL (health, finance, work and careers) need more trust. Treating "adjacent" topics this way is (inference)

## `crawling-indexing.md` (7 re-verify, 1 not verified, 1 inference)

- **re-verify** · L170 · Google crawlers and verification · …was due to be retired by the end of September 2026, about 6 months after the announcement of 31 March 2026 (whether the retirement happened: (re-verify))
- **re-verify** · L290 · Third-party views · …is better not to block search bots and to decide only on training. Conflicting: [SEJ 2026-05, Manić] writes that ChatGPT-User/Claude-User respect robots.txt. (re-verify)
- **re-verify** · L295 · Third-party views · …data] Very unbalanced crawl/referral ratios (ClaudeBot from ~20,600:1 to 70,900:1 depending on the period, Google ~9.4:1). Figures vary between articles (re-verify)
- **re-verify** · L304 · Third-party views · OpenAI no longer guarantees compliance (SEJ 2026-07); an SEJ 2026-05 author says the opposite (re-verify)
- **re-verify** · L307 · Third-party views · respected according to one author (SEJ 2026-05) (re-verify)
- **re-verify** · L309 · Third-party views · user-triggered — not respected (SEJ 2026-07) (re-verify)
- **re-verify** · L337 · Myths and outdated advice · IP path /search/apis/ipranges/ → replaced by /crawling/ipranges/ (old path due to be retired by the end of September 2026 (re-verify))
- **not verified** · L288 · Third-party views · [SEJ 2026-08, Reddit report] 403 to Googlebot/Bingbot on the sitemap with "AI Training = Block" or Bot Fight Mode; cause not confirmed
- **inference** · L261 · Build rules · …explicitly on training/search/user-triggered and write it in robots.txt (+ WAF where robots.txt is not enough); for sites that want visibility, default (inference)

## `ecommerce.md` (2 re-verify, 8 inference)

- **re-verify** · L151 · Third-party views · …and from February 2026 some large retailers allowed purchases in AI Mode. No Search action beyond accurate feeds and markup; availability outside the US (re-verify)
- **re-verify** · L163 · Myths and outdated advice · [SEJ 2026-07] "Without priceValidUntil, delivery time and return days Gemini will not include the product": one author's own audit; no Google statement (re-verify)
- **inference** · L35 · Structured data and Merchant Center · …product videos and live streams. The page does not map types to page types; mapping product page → Product, category → BreadcrumbList, home → Organization is (inference)
- **inference** · L51 · Variants · …URL on all variant pages (<link rel="canonical">); the page also points to Merchant Center's canonical_link documentation, and using it as an alternative is (inference)
- **inference** · L54 · Variants · Resolution between the two Google pages (inference)
- **inference** · L61 · Category pages and internal links · …content but set no minimum; the rule against copied manufacturer text lives in CQ-14. That a category needs some text of its own beyond the product grid is (inference)
- **inference** · L68 · Faceted navigation · …combinations deserve an indexable page (for example a colour or brand filter people search for) is a business decision that Google's page leaves to the site (inference)
- **inference** · L79 · Out-of-stock and discontinued products · …above come from the pages cited. Keeping a discontinued page live with Discontinued availability and links to successors, when it still answers searches, is (inference)
- **inference** · L84 · Reviews · …can be removed for trusted long-term contributors (→ CQ-09, CQ-16). Google's page names comments and forum posts; extending it to product reviews and Q&A is (inference)
- **inference** · L144 · Notes by site type · …usually get URL structure, variants and sitemaps from the platform: audit facets, stock states, feed consistency and duplicate manufacturer text first (inference)

## `editorial-news.md` (8 inference)

- **inference** · L98 · Web Stories · …policy (ineligibility when most pages exceed 180 characters) give different figures; the policy threshold is the one with consequences, so the audit uses 180 (inference)
- **inference** · L99 · Web Stories · When they make sense (inference)
- **inference** · L110 · Archives, tag pages and syndication · Tag and topic archives: the fetched Google pages say nothing specific about them. Treating near-empty or near-duplicate tag pages as low-value pages is an (inference)
- **inference** · L114 · Freshness: news vs evergreen · (inference)
- **inference** · L145 · ED-26 · Low — (inference)
- **inference** · L154 · Build rules · …them with isAccessibleForFree + hasPart/cssSelector, give Google's crawlers the full text (verify crawler identity by IP, not user agent alone: CI-46 (inference))
- **inference** · L161 · Notes by site type · …images if posts are timely (ED-14). News sitemaps, Googlebot-News, flexible sampling and Web Stories rarely apply: a services blog is seldom news (inference)
- **inference** · L166 · Third-party views · No third-party evidence is recorded in this file at this update; every rule above comes from Google documentation or from an (inference)

## `entity-personal-brand.md` (3 re-verify, 2 not verified, 4 inference)

- **re-verify** · L62 · Author, credentials, E-E-A-T · …makes a page untrustworthy to users and to Google's quality systems. [G] The dated update behind this wording (1 October 2026) was reported by [SEJ 2026-10] (re-verify)
- **re-verify** · L186 · Third-party views · …5 October 2026) now names AI-generated headshots, made-up names and false credentials as deceptive authorship [G]. Exact date and scope of the update: (re-verify)
- **re-verify** · L224 · Myths and outdated advice · …or invented credentials to look like an expert" → fabricated authors and credentials = deception [G]; dated update of 1 October 2026 per [SEJ 2026-10] (re-verify)
- **not verified** · L179 · Third-party views · [SEJ 2026-01, Clarkson-Bennett, opinion + unverified
- **not verified** · L197 · Third-party views · [SEJ 2026-09, Jarboe, unverified
- **inference** · L34 · Site name and the SERP for your own name · Site diversity: generally no more than two results per site in the top results (subdomains count as the same site). [G] → (inference)
- **inference** · L82 · Regulated professions and legal notices · Google does not rank pages on these notices; no Google document lists them as signals (inference)
- **inference** · L113 · EN-23 · Medium — [G] · (inference)
- **inference** · L124 · Build rules · 2. Recommended JSON-LD structure ((inference)

## `international.md` (6 inference)

- **inference** · L56 · Language and region codes · …return links, wrong language codes (including region-only), wrong or reserved region codes. Underscore forms such as en_US are not in the documented format (inference)
- **inference** · L72 · Language selector and internal links · Linking each selector entry to the equivalent page (not the other language's home page) is (inference)
- **inference** · L86 · International structured data · …in Organization; inLanguage appears only in specific types such as Book). Adding them is valid schema.org and harmless, but no Google effect is documented (inference)
- **inference** · L135 · Notes by site type · …over markup for shipping and returns, and Google suggested Merchant Center feeds against wrong-currency rich results; one feed or feed target per country is (inference)
- **inference** · L136 · Notes by site type · …and link each translation to the original with hreflang; keep the same author byline on each translation and name the translator where readers expect it (inference)
- **inference** · L152 · Myths and outdated advice · …be safe" → the methods are equivalent; using all three at once gives no benefit and is harder to manage (Google); two methods that disagree create a conflict (inference)

## `local-seo.md` (5 re-verify, 11 inference)

- **re-verify** · L4 · Local SEO · …Hours. [GBP](url) = Google Business Profile Help or the Maps contributed-content policy, checked 2026-10-11; [GBP] without a link = not found there, marked (re-verify)
- **re-verify** · L35 · 1. Business Profile and local listings · …unknown period; temporarily closed businesses can rank after open ones for broad queries. [GBP] · [GBP] Do not delete the profile to signal a closure. [GBP] (re-verify)
- **re-verify** · L234 · Third-party views · FAQ rich results removal (LO-26, Myths): reported by SEJ 2026-05; status owned by structured-data.md. (re-verify)
- **re-verify** · L235 · Third-party views · Effective date of the EEA change to site reputation abuse (§6): the policy page gives no date. (re-verify)
- **re-verify** · L236 · Third-party views · "Do not delete the profile to signal a closure" (§1): not stated on the GBP closure pages. (re-verify)
- **inference** · L4 · Local SEO · …= Google Business Profile Help or the Maps contributed-content policy, checked 2026-10-11; [GBP] without a link = not found there, marked (re-verify). (inference)
- **inference** · L97 · 8. Local directories (Google's position) · (inference)
- **inference** · L105 · LO-01 · High — [G] · (inference)
- **inference** · L123 · LO-19 · Medium — [G] · [GBP] · (inference)
- **inference** · L128 · LO-24 · Medium — [SEJ 2026-09, CallRail] · (inference)
- **inference** · L129 · LO-25 · Medium — (inference)
- **inference** · L140 · Build rules · 2. Anti-doorway test (inference)
- **inference** · L142 · Build rules · 4. Local + online practitioner ((inference)
- **inference** · L148 · Build rules · 6. Temporary closures ((inference)
- **inference** · L247 · Myths and outdated advice · "Geotags/EXIF in photos" → Google does not use image EXIF data in Search [G OH 2023-01]; undocumented for the GBP (inference)
- **inference** · L248 · Myths and outdated advice · "During holidays I put the site in maintenance mode / noindex" → visibility is lost; use special hours and notices ((inference)

## `measurement.md` (1 re-verify, 2 not verified, 17 inference)

- **re-verify** · L289 · Third-party views · …UI export rows: Google's Performance report help page does not state a row limit for exports [G]; practitioners commonly report a cap of 1,000 rows per table (re-verify)
- **not verified** · L217 · Procedure: server log analysis · …(common-crawlers.json for Googlebot; the other range files for special crawlers and user-triggered fetchers) or passes reverse + forward DNS. Report the unverified
- **not verified** · L296 · Third-party views · …hypothesise impressions generated by query fan-out without human clicks ("impressions up, clicks down" is not always human demand). [SEJ 2026-07, Manic, unverified
- **inference** · L4 · Measurement: Search Console, GA4, Bing, AI visibility, server logs, traffic drops · …strength] third-party view reported by Search Engine Journal (evidence, not rule; strength labels are explained in [Third-party views](#third-party-views)) · (inference)
- **inference** · L73 · Branded queries filter and the brand / non-brand split · …so follow them separately (ME-06) and read a drop in each differently (step 6 of the [traffic-drop procedure](#procedure-diagnosing-a-traffic-drop)). (inference)
- **inference** · L74 · Branded queries filter and the brand / non-brand split · …word (physio) or a bare surname (ferri) also matches searches by people who do not know the brand (physio oslo), which would then be counted as brand. (inference)
- **inference** · L100 · Beyond 16 months: API and exports · For small sites (inference)
- **inference** · L113 · Crawl Stats report and server logs · Analytics running in the browser may not give a full or accurate picture of Googlebot activity: use Crawl Stats. [G] Server logs are the other direct record. (inference)
- **inference** · L147 · ME-11 · High — [G], (inference)
- **inference** · L159 · ME-23 · Low — [G], (inference)
- **inference** · L160 · ME-24 · Medium — [G], (inference)
- **inference** · L161 · ME-25 · Medium — [G], (inference)
- **inference** · L162 · ME-26 · Medium — [G], (inference)
- **inference** · L193 · Procedure: exporting Search Console data · 6. Do not share exports outside the team that needs them; if a file is stored in the project, keep it out of version control. (inference)
- **inference** · L215 · Procedure: server log analysis · …sites (under about 1,000 pages) rarely need it. [G] Google documents how to verify its crawlers and what Crawl Stats shows; the analysis steps below are (inference)
- **inference** · L216 · Procedure: server log analysis · …user agent (response time if available). Logs contain personal data (IP addresses): work on an extract of bot lines and follow the site's retention rules. (inference)
- **inference** · L239 · Procedure: server log analysis · Pages marked noindex are not visible in the log: join the paths with a list of noindex URLs from a crawl or from the Page indexing report. (inference)
- **inference** · L258 · Notes by site type · Log analysis (ME-25) matters most here: faceted and sorting parameters are the usual crawl sink. (inference)
- **inference** · L270 · Notes by site type · …page, contacts and clicks to professional profiles, email and CV download as key events. Non-brand volume will be low: measure it per niche (role + skill). (inference)
- **inference** · L306 · Myths and outdated advice · "Browser analytics shows Googlebot activity": it may not represent it fully or accurately; use Crawl Stats (and server logs, (inference))

## `myths-deprecated.md` (6 re-verify)

- **re-verify** · L5 · Myths and outdated advice · …(documentation, blog, Office Hours) · [SEJ YYYY-MM] = reported by Search Engine Journal (for retired features: a news item about a Google announcement) · (re-verify)
- **re-verify** · L38 · Myths and outdated advice · …longer current"); it remains a useful test only for third-party AI bots that do not run JS (which bots render JS: ai-search.md › AI crawlers and fetchers) (re-verify)
- **re-verify** · L57 · Myths and outdated advice · Moved to developers.google.com/crawling/ipranges/; the old path was due to be retired by about the end of September 2026 (whether the retirement happened: (re-verify))
- **re-verify** · L61 · Myths and outdated advice · Since 1 July 2026 a click on an AMP result goes to the site's own host; no cache/SXG; AMP ranking unchanged (re-verify)
- **re-verify** · L66 · Myths and outdated advice · …to well-known government and health sites since August 2023. Markup harmless. SEJ also reported the removal of the report, Rich Results Test and API support (re-verify)
- **re-verify** · L107 · Notes · The FAQ, HowTo and Practice problem dates are confirmed on the Google changelog (developers.google.com/search/updates, checked 2026-10-11). (re-verify)

## `on-page-appearance.md` (3 inference)

- **inference** · L51 · Headings · Passage ranking evaluates individual sections of a page. (inference)
- **inference** · L204 · Build rules · …meta, canonical and main content present in the served or rendered HTML for every route (SSR/prerendering lowers the risk); verify with URL Inspection. (inference)
- **inference** · L244 · Notes by site type · One page per project with text, <img> images with alt, and an embedded demo video if any: more distinct pages = more queries covered and possible sitelinks. (inference)

## `performance-cwv.md` (8 inference)

- **inference** · L32 · Weight in Search · (inference)
- **inference** · L46 · Sites without field data · (inference)
- **inference** · L69 · By rendering mode · CMS (WordPress and similar): (inference)
- **inference** · L85 · Service workers and PWAs · (inference)
- **inference** · L129 · Notes by site type · Category filters and sorting are typical INP problems (heavy re-render on each click): measure the filter interaction, update the UI first and yield. → PF-14 (inference)
- **inference** · L137 · Notes by site type · …booking, map or chat widgets are the usual causes. Compress and size the hero, load maps and booking widgets on interaction or below the fold. → PF-15, PF-16 (inference)
- **inference** · L145 · Notes by site type · Same as local-business: builder platforms, oversized hero images, contact and booking widgets; no field data on most small sites. → PF-04, PF-15, PF-16 (inference)
- **inference** · L165 · Myths and outdated advice · "A service worker makes the site fast for Googlebot": Googlebot does not keep state between loads; the cache helps only repeat users (inference)

## `rendering-javascript.md` (1 inference)

- **inference** · L106 · Non-Google bots and JavaScript · …the third-party tests, their evidence level and their disagreement over CCBot are kept in one place: the bot table of ai-search.md. Practical consequence (inference)

## `site-architecture.md` (12 inference)

- **inference** · L31 · Hierarchy, hubs and click depth · …a hub page per section (category, service overview, topic page) keeps important pages a few links from the home page without putting everything in the menu. (inference)
- **inference** · L63 · Internal search, facets and pagination · …result pages (→ CI-34, CI-09, CQ-17). Architectural consequence: do not link to search result URLs from navigation, tag clouds or "popular searches" blocks. (inference)
- **inference** · L69 · Blog taxonomies: tags, categories, archives · …small set of taxonomies that work as real topic hubs (own introduction, curated links) and either merge the rest or keep them out of the index with noindex. (inference)
- **inference** · L78 · One topic per page · …two pages that answer the same intent compete with each other (cannibalisation, → CQ-31). Doorway variants by city or keyword are a spam issue (→ CQ-02). (inference)
- **inference** · L87 · SA-04 · …per [Procedures](#procedures); Search Console › Pages: "Discovered – currently not indexed" URLs that the crawl never reached are likely candidates (inference)
- **inference** · L96 · SA-13 · …– currently not indexed" concentrated on these patterns. Caveat: raise to Medium when archives outnumber posts. Official documentation is thin (see Facts) (inference)
- **inference** · L98 · SA-15 · …the intent table with the sitemap; Search Console › Performance › query → Pages tab with several URLs of the site; overlapping content measured as in CQ-31 (inference)
- **inference** · L155 · Notes by site type · …linked from the menu; tag pages limited to real topics (SA-13); related-article links in the body; date archives are rarely useful as entry points. (inference)
- **inference** · L156 · Notes by site type · …never one page per city served without a location (→ CQ-02, LO-13). Example: Northwind Physio has one clinic page for Oslo and a service page per treatment. (inference)
- **inference** · L157 · Notes by site type · …(entity home, → EN-01), projects or writing, contact; every page one click from the home page; project pages link back to About. Example: adanovak.example. (inference)
- **inference** · L158 · Notes by site type · …hub and from the home page; case studies and articles link to the service they illustrate. Example: Studio Ferri Orientamento with one page per service. (inference)
- **inference** · L159 · Notes by site type · …vs <competitor>", "alternatives") and docs; docs keep their own hierarchy with breadcrumbs; marketing pages link to the relevant docs and vice versa. (inference)

## `structured-data.md` (2 re-verify, 1 not verified, 25 inference)

- **re-verify** · L460 · Retired or restricted rich results · …15 June 2026. SEJ reported that the report and Rich Results Test support were removed in June 2026 and that Search Console API support ended in August 2026 (re-verify)
- **re-verify** · L562 · Third-party views · Microsoft/Bing (reported second-hand) states that schema helps Copilot [SEJ]: not verified in the sources read (re-verify)
- **not verified** · L562 · Third-party views · Microsoft/Bing (reported second-hand) states that schema helps Copilot [SEJ]: not verified
- **inference** · L4 · Structured data · …Search Central blog 2023–2026, Search Engine Journal summaries (secondary). Tags: [G](url) Google documentation or blog · [SEJ YYYY-MM] third-party view · (inference)
- **inference** · L28 · Formats · CMS (WordPress, Wix, Shopify…): use the SEO settings or a plugin instead of hand-writing markup [G]. (inference)
- **inference** · L72 · @id and the graph · (inference)
- **inference** · L73 · @id and the graph · (inference)
- **inference** · L81 · Choice matrix by site type · No dedicated rich result; helps entity understanding and author linking [G] (inference)
- **inference** · L83 · Choice matrix by site type · Organization (or Person via ProfilePage) with contactPoint; LocalBusiness only if a real address is shown (inference)
- **inference** · L119 · WebSite (site name) · (publisher and @id are (inference)
- **inference** · L128 · Organization · …to profiles the entity does not own (impersonation); white or transparent logo that is illegible; Organization repeated on every page with different data [G] (inference)
- **inference** · L151 · LocalBusiness (and subtypes) · …Google/Facebook widget) [G]; additionalType; approximate coordinates; phone without prefix; address or hours different from the Business Profile or the page (inference)
- **inference** · L152 · LocalBusiness (and subtypes) · (inference)
- **inference** · L153 · LocalBusiness (and subtypes) · ⚠ (inference)
- **inference** · L185 · Person / ProfilePage · (inference)
- **inference** · L228 · BreadcrumbList · Guidelines: a typical user path, not a copy of the URL structure; no element needed for the root (domain) or the page itself [G]. (inference)
- **inference** · L247 · Review / AggregateRating · (inference)
- **inference** · L292 · Course · (inference)
- **inference** · L353 · Product, Offer, ProductGroup and merchant listings · (inference)
- **inference** · L444 · JavaScript and SPA notes · (inference)
- **inference** · L446 · JavaScript and SPA notes · (inference)
- **inference** · L447 · JavaScript and SPA notes · (inference)
- **inference** · L495 · SD-13 · Medium — [G] (inference)
- **inference** · L497 · SD-15 · Medium — [G] (inference)
- **inference** · L503 · SD-21 · Medium — [G] (inference)
- **inference** · L510 · SD-28 · Medium — (inference)
- **inference** · L511 · SD-29 · Low — [G] (inference)
- **inference** · L531 · Build rules · @id conventions (inference)

## `adapters/angular.md` (1 inference)

- **inference** · L31 · hreflang and i18n · …one app per locale; serve each under its own prefix (/en/, /de/) with hreflang links in the head, not client-only language switching on one URL → RJ-31 (inference)

## `adapters/astro.md` (2 inference)

- **inference** · L10 · Rendering default and options · …→ no indexable content there (RJ-01). server:defer (server islands) renders a component on demand, outside the page render: keep primary content out of it (inference)
- **inference** · L16 · Links and routing · File-based routing in src/pages/; links are plain <a href> → RJ-05. Set trailingSlash and build.format so URLs, canonicals and sitemap entries agree (inference)

## `adapters/classic-ssr.md` (3 inference)

- **inference** · L11 · Where title, meta, canonical and robots meta live · Base template <head> (Django {% block %}, Blade sections, Rails content_for), filled per view → RJ-11 (inference)
- **inference** · L19 · robots.txt and sitemap generation · robots.txt: a static file (Laravel and Rails public/) or a view (inference)
- **inference** · L31 · hreflang and i18n · …= True, x_default = True on Sitemap adds hreflang to the sitemap. Laravel/Rails: locale prefix in routes and hreflang in the layout → CI-36, CI-37, IN-10 (inference)

## `adapters/drupal.md` (4 not verified, 3 inference)

- **not verified** · L11 · Where title, meta, canonical and robots meta live · Metatag (contrib): title, description, canonical (robots too, not verified)
- **not verified** · L12 · Where title, meta, canonical and robots meta live · Without Metatag, title and canonical come from core and the theme (not verified
- **not verified** · L24 · 404 handling (true status) · Core answers unknown paths with 404 (inference); a custom 404 page is set in Basic site settings (system.site page.404) (UI path not verified
- **not verified** · L40 · Sources · …Sitemap] · [Hreflang] · [RobotsTxt] · [SEO modules list] · [core robots.txt]. The brief's page drupal.org/docs/administering-a-drupal-site/seo returned 404: not verified
- **inference** · L24 · 404 handling (true status) · Core answers unknown paths with 404 (inference)
- **inference** · L27 · hreflang and i18n · …adds hreflang only on content entity pages; the Hreflang module (contrib) adds it on all pages → CI-36, CI-37. Language prefixes (/de/…) per language (inference)
- **inference** · L37 · Common pitfalls (with check IDs) · Views with exposed filters creating crawlable parameter URLs → CI-34 (inference)

## `adapters/gatsby.md` (1 not verified, 3 inference)

- **not verified** · L5 · Detection · Signals in the README table. Also gatsby in package.json, gatsby-node., src/pages/; HTML <div id="___gatsby"> (not verified
- **inference** · L15 · Where title, meta, canonical and robots meta live · …by the docs; add one <link rel="canonical"> in Head from siteUrl + location.pathname. Tags with the same id are deduplicated (last wins) → CI-22, RJ-09 (inference)
- **inference** · L30 · hreflang and i18n · No built-in i18n. One page per locale (/en/…, /de/…) created in gatsby-node, hreflang links in Head → CI-36, CI-37 (inference)
- **inference** · L40 · Common pitfalls (with check IDs) · Sitemap tested in gatsby develop (not generated there) (inference)

## `adapters/hosted-builders.md` (1 not verified, 1 inference)

- **not verified** · L27 · hreflang and i18n · Webflow Localize puts hreflang in the auto sitemap (manual with a custom one); Wix and Squarespace: not verified
- **inference** · L32 · Structured data hooks · Squarespace: generated by the platform; extra JSON-LD only via code injection (inference)

## `adapters/joomla.md` (4 not verified, 2 inference)

- **not verified** · L13 · Where title, meta, canonical and robots meta live · Menu items and articles carry their own browser title, meta description and robots (not verified
- **not verified** · L27 · 404 handling (true status) · Unknown URLs go through the template's error page; check with curl that it returns 404, also with SEF on and off (not verified
- **not verified** · L30 · hreflang and i18n · Core multilingual (language filter plugin and associations) gives per-language URLs; check reciprocal hreflang on associated items → CI-36, CI-37 (not verified
- **not verified** · L43 · Sources · …[joomla-cms 5.4 robots.txt.dist] · [SEF plugin] · [OSMap]. docs.joomla.org returned 403 to the fetch: per-item metadata, 404 and multilingual behaviour are not verified
- **inference** · L23 · robots.txt and sitemap generation · …renamed to robots.txt, it disallows /administrator/, /api/, /cache/, /components/, /modules/, /plugins/, /tmp/… /media/ (CSS/JS) is not blocked (inference)
- **inference** · L37 · Common pitfalls (with check IDs) · htaccess.txt not renamed while rewriting is on: pages 404 (inference)

## `adapters/remix-react-router.md` (1 not verified, 4 inference)

- **not verified** · L24 · 404 handling (true status) · …404 }) in the loader; the nearest ErrorBoundary renders it (isRouteErrorResponse) → RJ-07. Remix 2 pattern: throw new Response(null, { status: 404 }) (not verified
- **inference** · L18 · Links and routing · <Link to>/<NavLink> render <a href>; do not navigate content with useNavigate() on click → RJ-05 (inference)
- **inference** · L29 · hreflang and i18n · No built-in i18n. Locale prefix in routes.ts (/:lang/…) and hreflang link descriptors per route → CI-36, CI-37 (inference)
- **inference** · L32 · Structured data hooks · …{ … } } outputs <script type="application/ld+json">. With React 19, render the script in the route component from loader data → RJ-14, SD-30 (inference)
- **inference** · L37 · Common pitfalls (with check IDs) · meta + React 19 <title> both used: two titles or canonicals → RJ-09 (inference)

## `adapters/shopify.md` (1 not verified)

- **not verified** · L12 · Where title, meta, canonical and robots meta live · Per-item title and description are edited in the admin (not verified

## `adapters/static-generators.md` (4 inference)

- **inference** · L11 · Where title, meta, canonical and robots meta live · …the base template's <head>; embedded partials opengraph.html, twitter_cards.html, schema.html ({{ partial "opengraph.html" . }}). Canonical from .Permalink (inference)
- **inference** · L16 · Links and routing · Hugo: one URL form per page; set baseURL to the production URL (inference)
- **inference** · L24 · robots.txt and sitemap generation · Eleventy: no built-in sitemap or robots.txt; write them as templates or copy files (inference)
- **inference** · L30 · hreflang and i18n · Hugo multilingual mode builds one tree and sitemap per language; output hreflang from .Translations in the head (inference)

## `adapters/static-html.md` (1 inference)

- **inference** · L21 · 404 handling (true status) · …Netlify, Cloudflare Pages: a 404.html at the root ([GitHub], [Netlify], [Cloudflare]). Their docs do not state the status code, so confirm the 404 with curl (inference)

## `adapters/sveltekit.md` (4 inference)

- **inference** · L15 · Where title, meta, canonical and robots meta live · Canonical and robots meta: no built-in API; one <link rel="canonical"> per page in <svelte:head> → RJ-09, CI-22 (inference)
- **inference** · L30 · hreflang and i18n · …i18n. The reroute hook maps translated paths (/de/ueber-uns → /de/about). Output hreflang in <svelte:head> and set <html lang> per locale → CI-36, CI-37 (inference)
- **inference** · L33 · Structured data hooks · The SEO page does not cover JSON-LD. Render <script type="application/ld+json"> from load data inside <svelte:head> so it is in the SSR HTML → RJ-14, SD-30 (inference)
- **inference** · L38 · Common pitfalls (with check IDs) · Dynamic routes missing from entries: pages never built → CI-26 (inference)

## `adapters/wordpress.md` (1 inference)

- **inference** · L34 · Common pitfalls (with check IDs) · "Discourage search engines" left on after launch (inference)
