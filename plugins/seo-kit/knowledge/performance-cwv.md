# Performance and Core Web Vitals

> Updated 2026-10-11. Scope: Core Web Vitals (LCP, INP, CLS), field vs lab data, their weight in ranking, typical causes and fixes by rendering mode, images, fonts, third-party scripts, service workers. Primary source: Google Search Central; third-party views marked [SEJ].
> Source tags, ⚠ and the severity scale follow `conventions.md`. `[web.dev](url)` marks Google-authored web performance guidance (not Search Central); PageSpeed Insights and CrUX documentation are tagged `[G](url)`. Related: `on-page-appearance.md` (HTTPS, mobile, interstitials, image indexing), `rendering-javascript.md` (SSR/CSR, app shell, 2 MB limits), `crawling-indexing.md` (redirects, caching, compression).

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
  - [The three metrics](#the-three-metrics) · [Weight in Search](#weight-in-search) · [Field vs lab data](#field-vs-lab-data) · [Sites without field data](#sites-without-field-data)
  - [LCP: causes and fixes](#lcp-causes-and-fixes) · [INP: causes and fixes](#inp-causes-and-fixes) · [CLS: causes and fixes](#cls-causes-and-fixes)
  - [By rendering mode](#by-rendering-mode) · [Images](#images) · [Fonts](#fonts) · [Third-party scripts](#third-party-scripts) · [Service workers and PWAs](#service-workers-and-pwas)
- [Audit checks](#audit-checks)
- [Build rules](#build-rules)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

## Facts and rules (Google)

### The three metrics
- **LCP** (Largest Contentful Paint, loading): render time of the largest image, text block or video visible in the viewport, measured from the start of navigation. Good **≤ 2.5 s**, needs improvement 2.5–4.0 s, poor **> 4.0 s**. [G](https://developers.google.com/search/docs/appearance/core-web-vitals) [web.dev](https://web.dev/articles/lcp)
- **INP** (Interaction to Next Paint, responsiveness): observes clicks, taps and key presses during the whole visit (not hover, scroll or zoom) and reports roughly the worst one (one outlier ignored per 50 interactions). Good **≤ 200 ms**, needs improvement 200–500 ms, poor **> 500 ms**. Each interaction = input delay + processing duration + presentation delay. [G](https://developers.google.com/search/docs/appearance/core-web-vitals) [web.dev](https://web.dev/articles/inp)
- **CLS** (Cumulative Layout Shift, visual stability): the largest burst ("session window": shifts < 1 s apart, window ≤ 5 s) of unexpected layout shifts. Good **≤ 0.1**, poor **> 0.25**. Shifts within 500 ms of a click, tap or key press are excluded; scrolls are not "recent input"; CSS `transform` animations do not count. [G](https://developers.google.com/search/docs/appearance/core-web-vitals) [web.dev](https://web.dev/articles/cls)
- **Pass rule**: measure at the **75th percentile** of page loads, segmented by mobile and desktop; a page passes when all three metrics are good at p75. [web.dev](https://web.dev/articles/vitals)
- In PageSpeed Insights, if INP has too little data the assessment passes on LCP and CLS alone; if LCP or CLS lacks data the page or origin **cannot be assessed**. [G](https://developers.google.com/speed/docs/insights/v5/about)
- Stable metrics change at most once per year; INP is the successor of FID, which was retired (the Search Central page no longer lists FID). [web.dev](https://web.dev/articles/vitals) [web.dev](https://web.dev/articles/inp)
- Lab tools cannot measure INP without interactions; Total Blocking Time (TBT) is a lab proxy, not a substitute. Bots and headless browsers without scripted interactions produce no INP value. [web.dev](https://web.dev/articles/inp)

### Weight in Search
- "Core Web Vitals are used by our ranking systems." Google highly recommends good Core Web Vitals, but good results in the report or in third-party tools **do not guarantee top rankings**, and chasing a perfect score only for SEO "may not be the best use of your time". [G](https://developers.google.com/search/docs/appearance/page-experience) [G](https://developers.google.com/search/docs/appearance/core-web-vitals)
- There is **no single page experience signal**; the other aspects (HTTPS, mobile, ads, interstitials, distinguishable main content) do not raise rankings directly but are aligned with what the core systems reward. **Relevance wins**: Google ranks the most relevant content even with a weak page experience; page experience helps when many pages are equally helpful. Assessment is mostly per page, with some site-wide assessments. [G](https://developers.google.com/search/docs/appearance/page-experience)
- Self-assessment questions: good Core Web Vitals; served over HTTPS (→ OP-35, OP-46); displays well on mobile (→ OP-36); no excessive ads (→ OP-38); no intrusive interstitials (→ OP-37); main content easy to distinguish. [G](https://developers.google.com/search/docs/appearance/page-experience)
- *(inference)* For audit priority: a site that is not indexed or has thin content gains nothing from faster pages; fix crawling, rendering and content first, then performance.

### Field vs lab data
- **Field data** (real Chrome users, via the Chrome UX Report, CrUX): what the Search Console Core Web Vitals report and the "real users" part of PageSpeed Insights show. **Lab data** (Lighthouse, DevTools): one simulated load on one device and network, useful for debugging and regressions, **not a substitute** for field data. [web.dev](https://web.dev/articles/vitals) [G](https://developers.google.com/speed/docs/insights/v5/about)
- PSI field data: trailing **28 days**, p75 for every metric, updated daily; if the URL has too little data PSI falls back to the **origin**; if the origin has too little data, no field data is shown. CrUX needs a public (crawlable, indexable) URL with enough distinct samples. [G](https://developers.google.com/speed/docs/insights/v5/about)
- The Lighthouse **Performance score** (90+ good, 50–89 needs improvement, < 50 poor) is a lab score; it is not the Core Web Vitals assessment. [G](https://developers.google.com/speed/docs/insights/v5/about)
- Search Console Core Web Vitals report: CrUX data, **only indexed URLs**, similar pages grouped into URL groups (fallback to an origin group), mobile and desktop reported separately, a group takes the status of its **worst** metric; groups without enough LCP and CLS data are left out; "Start Tracking" opens a **28-day** validation window. [G](https://support.google.com/webmasters/answer/9205520)
- Office Hours: PSI lab tests vary from run to run and field data is what counts; resource hints (`preload`, `preconnect`) matter only if they improve the real metrics. [G OH 2024-06](https://developers.google.com/search/help/office-hours/2024/june) [G OH 2023-08](https://developers.google.com/search/help/office-hours/2023/august)
- Lab CLS covers only the load; field CLS covers the page's whole lifetime: a large field-vs-lab gap in PSI usually means post-load shifts. [web.dev](https://web.dev/articles/optimize-cls)
- APIs: PSI `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=…` (key optional, recommended for automation) returns `loadingExperience` (URL), `originLoadingExperience` (origin) and `lighthouseResult` (lab). The PSI page states that Google plans to discontinue real-world data in this API (no date given) and points to the **CrUX API** (`POST https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=…`, API key required, `url` or `origin`, `formFactor` `PHONE`/`DESKTOP`/`TABLET`, `p75` per metric, 28-day rolling window). [G](https://developers.google.com/speed/docs/insights/v5/get-started) [G](https://developer.chrome.com/docs/crux/api)

### Sites without field data
- Small sites often have **no URL-level and no origin-level data**: PSI shows only lab data and Search Console shows "No data available". Then no Core Web Vitals verdict is possible; report the lab findings as lab diagnostics. [G](https://developers.google.com/speed/docs/insights/v5/about) [G](https://support.google.com/webmasters/answer/9205520)
- To get field data anyway, set up your own real-user monitoring, e.g. the `web-vitals` library (`onLCP`, `onINP`, `onCLS`) sending to analytics; values may differ slightly from CrUX. [web.dev](https://web.dev/articles/vitals)
- *(inference)* With no field data and lab LCP well under 2.5 s, CLS near 0 and low TBT on a mobile Lighthouse run, report "no evidence of a problem", not "passes Core Web Vitals".

### LCP: causes and fixes
- Break LCP into four sub-parts: **TTFB** (~40%), **resource load delay** (< 10%), **resource load duration** (~40%), **element render delay** (< 10%); guidelines, not fixed millisecond targets. Find the LCP element and its sub-parts in PSI or the DevTools Performance panel first. [web.dev](https://web.dev/articles/optimize-lcp)
- **Load delay**: the LCP image must be discoverable in the initial HTML (`<img src>` or `srcset`), not injected by JS, not `data-src` lazy loading, not a CSS background; otherwise preload it. **Never** `loading="lazy"` on the LCP image. `fetchpriority="high"` on one or two likely LCP images, `fetchpriority="low"` on hidden carousel slides. Critical resources on the same origin. [web.dev](https://web.dev/articles/optimize-lcp)
- **Render delay**: reduce render-blocking CSS (remove unused, defer non-critical, inline only small CSS); no synchronous scripts in `<head>` (`async`/`defer`); prefer SSR or static generation; break up long tasks; watch for A/B testing scripts that hide content. [web.dev](https://web.dev/articles/optimize-lcp)
- **Load duration**: right-sized, compressed images in AVIF or WebP; a CDN; not too many high-priority downloads at once; efficient caching. [web.dev](https://web.dev/articles/optimize-lcp)
- **TTFB**: few redirects; cacheable HTML at the CDN edge (unique analytics parameters can bypass the cache); SSR adds server time but is usually worth it. PSI's experimental TTFB thresholds: good ≤ 800 ms, poor > 1,800 ms. → CI-19, CI-40, CI-41 [web.dev](https://web.dev/articles/optimize-lcp) [G](https://developers.google.com/speed/docs/insights/v5/about)
- Critical JS/CSS on a separate host adds connection overhead (LCP); Google advises against it. → RJ-25 [G](https://developers.google.com/search/blog/2024/12/crawling-december-resources)

### INP: causes and fixes
- Start from field data (RUM shows which interaction is slow), then reproduce in the lab, including during page load, when the main thread is busiest. [web.dev](https://web.dev/articles/optimize-inp)
- **Input delay**: long tasks from script evaluation at startup. **Processing**: do the minimum in event callbacks, update the UI first and defer the rest (`setTimeout`, `scheduler.yield()`); avoid layout thrashing. **Presentation delay**: keep the DOM small, use `content-visibility`, avoid rendering large amounts of HTML with JavaScript. [web.dev](https://web.dev/articles/optimize-inp) [web.dev](https://web.dev/articles/optimize-long-tasks)
- A **long task** is any task over **50 ms**; DevTools marks long tasks with a red triangle. [web.dev](https://web.dev/articles/optimize-long-tasks)

### CLS: causes and fixes
- Common causes: images or videos without dimensions, web fonts that render differently from their fallback, ads or widgets that resize themselves, content inserted above existing content. [web.dev](https://web.dev/articles/cls)
- Fixes: `width` and `height` on `img`/`video` (or CSS `aspect-ratio`), also on `<source>` in `<picture>`; reserve space for ads and embeds (`min-height`, smallest or most likely size, keep the space when no ad is returned); late content lower on the page, in a fixed-size container, or behind a "Load more" button; banners overlaid or with reserved space; animate with `transform`, not `top`/`left`; make pages eligible for the back/forward cache. [web.dev](https://web.dev/articles/optimize-cls)

### By rendering mode
- **SSR / SSG**: content arrives as HTML, so LCP usually depends on the hero image, fonts and render-blocking CSS (image priority, dimensions, font loading). Static rendering gives fast FCP, low TBT and INP and a consistently fast TTFB. [web.dev](https://web.dev/articles/rendering-on-the-web) [web.dev](https://web.dev/articles/optimize-lcp)
- **Hydration**: SSR pages can look ready but not respond to input; full rehydration "can have a significant negative impact on TBT and INP". Google's web.dev recommends SSR or static rendering over a full rehydration approach, shipping mostly HTML with minimal JavaScript. [web.dev](https://web.dev/articles/rendering-on-the-web)
- **CSR / SPA / app shell**: heavy client rendering creates a large gap between TTFB and first paint (FCP) and large HTML rendered by JS hurts INP; the JS amount tends to grow with the app. Indexing risks of CSR are in `rendering-javascript.md`. → RJ-01, RJ-02 [web.dev](https://web.dev/articles/optimize-lcp) [web.dev](https://web.dev/articles/optimize-inp) [web.dev](https://web.dev/articles/rendering-on-the-web)
- **CMS (WordPress and similar)**: *(inference)* plugins and themes typically add render-blocking CSS/JS, third-party scripts and unoptimised images; the web.dev fixes above apply unchanged, applied through the CMS settings or a performance plugin. The sources fetched do not discuss CMS plugins.

### Images
- Indexing rules (formats BMP, GIF, JPEG, PNG, WebP, SVG, AVIF; `<img>` not CSS backgrounds; `srcset`/`<picture>` with a fallback `src`): see `on-page-appearance.md`. → OP-19, OP-21 [G](https://developers.google.com/search/docs/appearance/google-images)
- Images are often the largest contributor to page size; Google recommends current image optimisation and responsive image techniques and PageSpeed Insights to analyse speed. [G](https://developers.google.com/search/docs/appearance/google-images)
- Lazy loading: viewport-based (native or IntersectionObserver), never on content likely to be visible immediately. → OP-24 [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading)

### Fonts
- WOFF2; subset unused glyphs (`unicode-range`); few font files (system fonts or a variable font); preconnect to a third-party font origin (with `crossorigin`); preload only critical fonts; `font-display` other than `auto`/`block` so text is not hidden (`optional` avoids swap shifts, `swap` can cause them); a close fallback with `size-adjust` and the metric overrides. Self-hosting is not automatically faster. [web.dev](https://web.dev/articles/font-best-practices) [web.dev](https://web.dev/articles/optimize-cls)

### Third-party scripts
- Find costly scripts with DevTools, PSI or WebPageTest; remove any script without clear value; load the rest with `async` or `defer` unless they are on the critical path; preconnect to their origins; lazy-load embeds and below-the-fold ads with IntersectionObserver; run A/B variant selection server-side; load tags through a tag manager and keep the number of tags low. [web.dev](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript)

### Service workers and PWAs
- The Search Central JavaScript pages fetched (JavaScript SEO basics, fix-search-javascript) **do not mention service workers**. They state that the rendering service **does not retain state across page loads** (local storage, session storage and cookies are cleared) and caches resources aggressively, ignoring caching headers. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript) [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- On a first visit all requests go straight to the server; a service worker is not available on first load and controls a page only from the next navigation. [web.dev](https://web.dev/learn/pwa/service-workers)
- *(inference)* Googlebot behaves like a first-time visitor on every load, so it never benefits from a service worker cache: the network response must contain the content, and performance gains from a service worker only reach repeat users (not Googlebot, and not the first visit counted in field data).
- The **app shell** model caches the shell and loads content client-side: for Google this is CSR, and Google must run JS to see the content. → RJ-01 [web.dev](https://web.dev/learn/pwa/architecture) [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)

## Audit checks

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| PF-01 | Field LCP at p75 ≤ 2.5 s, on mobile and on desktop | PSI (`https://pagespeed.web.dev/` or the API: `loadingExperience`, else `originLoadingExperience`) or the CrUX API (`largest_contentful_paint.percentiles.p75`, `formFactor` `PHONE` and `DESKTOP`); Search Console Core Web Vitals report. Caveat: state whether the value is URL-level or origin-level; no field data → PF-04 | Medium | [G](https://developers.google.com/search/docs/appearance/core-web-vitals) |
| PF-02 | Field INP at p75 ≤ 200 ms, on mobile and on desktop | As PF-01 with `interaction_to_next_paint`. Caveat: lab TBT is only a proxy; never report a lab INP verdict | Medium | [G](https://developers.google.com/search/docs/appearance/core-web-vitals) |
| PF-03 | Field CLS at p75 ≤ 0.1, on mobile and on desktop | As PF-01 with `cumulative_layout_shift`; a large field-vs-lab gap in PSI points to post-load shifts | Medium | [G](https://developers.google.com/search/docs/appearance/core-web-vitals) |
| PF-04 | (informational) Field data level stated: URL, origin or none; lab results labelled as lab | PSI header ("This URL" vs "Origin", or no real-user data); Search Console "No data available". Without field data: give lab diagnostics only, no pass/fail | Low | [G](https://developers.google.com/speed/docs/insights/v5/about) |
| PF-05 | Search Console Core Web Vitals report: Poor and Needs improvement URL groups mapped to templates and devices; fixes validated | Search Console → Core Web Vitals → Mobile / Desktop → issue → example URLs; after a fix, "Start Tracking" (28 days). Caveat: requires property access; only indexed URLs appear | Medium | [G](https://support.google.com/webmasters/answer/9205520) |
| PF-06 | LCP element identified for each key template (home, service/product, article) with its dominant sub-part | PSI diagnostics (LCP element and breakdown), DevTools Performance panel on a mobile profile; record element, TTFB, load delay, load duration, render delay | Medium | [web.dev](https://web.dev/articles/optimize-lcp) |
| PF-07 | LCP image discoverable in the initial HTML (`<img src>`/`srcset`), not JS-injected, `data-src` or CSS background, unless preloaded | `curl -s URL \| grep -i '<img'` near the top of the body; grep `data-src`, `background-image` on the hero; `<link rel="preload" as="image">` if the image comes from CSS/JS | Medium | [web.dev](https://web.dev/articles/optimize-lcp) |
| PF-08 | Alias of OP-24 — verify there, report once | See OP-24 (no `loading="lazy"` on immediately visible images, including the LCP image; viewport-based lazy loading elsewhere) | Medium | [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading) |
| PF-09 | `fetchpriority="high"` on the likely LCP image only (one or two images per page) | `curl -s URL \| grep -o 'fetchpriority="[a-z]*"' \| sort \| uniq -c`; flag none on an image LCP, or more than two `high` | Low | [web.dev](https://web.dev/articles/optimize-lcp) |
| PF-10 | `width` and `height` (or CSS `aspect-ratio`) on `img`, `video`, `iframe` and `<picture><source>` | Grep the raw and rendered HTML for `<img` without `width=`/`height=`; DevTools Performance → Layout shifts track | Medium | [web.dev](https://web.dev/articles/optimize-cls) |
| PF-11 | Space reserved for ads, embeds and late banners (cookie, promo); no content inserted above existing content after load | Mobile load in DevTools with the Layout shifts track; check ad slots have `min-height`; banners overlaid or with reserved space | Medium | [web.dev](https://web.dev/articles/optimize-cls) |
| PF-12 | Web fonts: WOFF2, few files, `font-display` not `block`/`auto`, close fallback (`size-adjust`) | DevTools Network filtered by Font; grep `@font-face` and `font-display` in CSS. Caveat: raise to Medium when a font is the LCP text or causes field CLS | Low | [web.dev](https://web.dev/articles/font-best-practices) |
| PF-13 | No render-blocking synchronous scripts in `<head>`; render-blocking CSS small (unused CSS removed, non-critical deferred) | `curl -s URL` and inspect `<head>`: `<script src>` without `async`/`defer`/`type="module"`; PSI render-blocking diagnostics. Caveat: raise to Medium when LCP render delay dominates (PF-06) | Low | [web.dev](https://web.dev/articles/optimize-lcp) |
| PF-14 | No long tasks (> 50 ms) blocking load or key interactions (menu, filters, add-to-cart, forms); hydration cost reviewed on SSR/SPA sites | DevTools Performance panel (red-cornered tasks) during load and while using the key controls; Lighthouse TBT as lab proxy; RUM attribution for the slow interaction (PF-21) | Medium | [web.dev](https://web.dev/articles/optimize-long-tasks) |
| PF-15 | Third-party scripts inventoried (origin, purpose, owner); unused ones removed; the rest `async`/`defer`; embeds and below-the-fold ads lazy-loaded | DevTools Network grouped by domain or PSI third-party diagnostics; grep `<script src="https://` for external origins; tag manager container review. Caveat: raise to Medium when field LCP or INP fails | Low | [web.dev](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript) |
| PF-16 | Large images served in AVIF/WebP, compressed and sized for the viewport (`srcset`/`sizes`) | `curl -sI` on the hero and gallery images (`Content-Type`, `Content-Length`); compare intrinsic vs rendered size in DevTools. Indexing side of formats: OP-21 | Low | [web.dev](https://web.dev/articles/optimize-lcp) |
| PF-17 | (informational) Field TTFB p75 ≤ 800 ms; HTML cacheable at the CDN | PSI field TTFB (experimental) or CrUX `experimental_time_to_first_byte`; `curl -sI URL` for `Cache-Control`/CDN cache headers. Redirects: CI-19; caching: CI-40; compression: CI-41 | Low | [G](https://developers.google.com/speed/docs/insights/v5/about) |
| PF-18 | Alias of RJ-25 — verify there, report once | See RJ-25 (critical JS/CSS on the same host as the page) | Low | [G](https://developers.google.com/search/blog/2024/12/crawling-december-resources) |
| PF-19 | Alias of OP-37 — verify there, report once | See OP-37 (no full-page interstitial on load; consent without a redirect; age verification overlaid) | Medium | [G](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials) |
| PF-20 | Alias of RJ-19 — verify there, report once | See RJ-19 (content does not depend on storage, cookies or previous visits). For PWAs also load the page in a fresh profile with DevTools → Application → Service workers → "Bypass for network": the content must come from the network response, not the service worker cache | High | [G](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript) |
| PF-21 | (informational) Own real-user monitoring when CrUX has no data or the slow interaction is unknown | Check for the `web-vitals` library (`onLCP`, `onINP`, `onCLS`) or a RUM provider in the page scripts and in analytics | Low | [web.dev](https://web.dev/articles/vitals) |
| PF-22 | Pages eligible for the back/forward cache | DevTools → Application → Back/forward cache → "Test back/forward cache" (the panel lists what blocks eligibility) | Low | [web.dev](https://web.dev/articles/optimize-cls) |

## Build rules
- **Budget from day one**: design for LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at p75 on mobile; verify with field data after launch, with lab runs only as regression tests. → PF-01, PF-02, PF-03, PF-04 [web.dev](https://web.dev/articles/vitals)
- **Prefer SSR or static generation**; avoid full rehydration (ship mostly HTML with minimal JavaScript). → PF-14, RJ-01 [web.dev](https://web.dev/articles/rendering-on-the-web)
- **Hero image**: `<img>` in the server HTML with `src`/`srcset`, `width`/`height`, AVIF or WebP, no `loading="lazy"`, `fetchpriority="high"`; every other image below the fold lazy. → PF-07, PF-08, PF-09, PF-10, PF-16 [web.dev](https://web.dev/articles/optimize-lcp)
- **Head**: small critical CSS, scripts with `async`/`defer`, critical CSS and JS on the page's own host. → PF-13, PF-18 [web.dev](https://web.dev/articles/optimize-lcp)
- **Fonts**: one or two WOFF2 families (or system fonts), subset, `font-display: swap` or `optional`, fallback tuned with `size-adjust`. → PF-12 [web.dev](https://web.dev/articles/font-best-practices)
- **Reserve space** for ads, embeds, cookie and promo banners; never push content down after load. → PF-11, PF-19 [web.dev](https://web.dev/articles/optimize-cls)
- **Third parties**: keep a list (what, why, who owns it); add a new one only with a reason; `async`/`defer` by default. → PF-15 [web.dev](https://web.dev/articles/optimizing-content-efficiency-loading-third-party-javascript)
- **Event handlers**: update the UI first, yield, defer saving and tracking. → PF-14 [web.dev](https://web.dev/articles/optimize-inp)
- **PWA**: the service worker is an enhancement for repeat visits; every URL must return its full content from the server. → PF-20, RJ-01 [web.dev](https://web.dev/learn/pwa/service-workers)

## Notes by site type
**ecommerce** (example: Acme Widgets, acme-widgets.example)
- Product pages: the main product photo is usually the LCP element; gallery and carousel slides after the first get `fetchpriority="low"` or lazy loading, thumbnails with dimensions. → PF-06, PF-09, PF-10 [web.dev](https://web.dev/articles/optimize-lcp)
- Category filters and sorting are typical INP problems (heavy re-render on each click): measure the filter interaction, update the UI first and yield. → PF-14 *(inference)* from [web.dev](https://web.dev/articles/optimize-inp)
- Reviews, recommendation and chat widgets are third parties: inventory and defer them. → PF-15

**editorial**
- Ads and embeds are the main CLS source: reserve the slot size, keep the space when no ad is returned, lazy-load below-the-fold ads. → PF-11, PF-15 [web.dev](https://web.dev/articles/optimize-cls)
- Templates with many tags (analytics, A/B testing, paywall, consent): A/B tests that hide content delay LCP; prefer server-side variant selection. → PF-13, PF-15 [web.dev](https://web.dev/articles/optimize-lcp)

**local-business** (example: Northwind Physio, northwind-physio.example)
- Often a site builder or theme: oversized hero photos and booking, map or chat widgets are the usual causes. Compress and size the hero, load maps and booking widgets on interaction or below the fold. → PF-15, PF-16 *(inference)*
- Usually no field data: report lab diagnostics only. → PF-04

**personal-brand** (example: Ada Novak, adanovak.example)
- Portfolios often use a full-screen hero image or video and decorative animations: size the hero, animate with `transform`, avoid layout-moving effects. → PF-03, PF-16 [web.dev](https://web.dev/articles/optimize-cls)
- Small traffic: CrUX data is usually missing; add `web-vitals` RUM if performance matters. → PF-04, PF-21

**professional-services** (example: Studio Ferri Orientamento, studioferri.example)
- Same as local-business: builder platforms, oversized hero images, contact and booking widgets; no field data on most small sites. → PF-04, PF-15, PF-16 *(inference)*

**saas-product**
- Marketing pages in the same SPA as the app pay the app's hydration and bundle cost: render them statically and keep the app bundle off them. → PF-14, RJ-01 [web.dev](https://web.dev/articles/rendering-on-the-web)
- Signup and pricing interactions (toggles, calculators) are INP-sensitive. → PF-14

## Third-party views
- [SEJ 2026-07, web.dev Nuvemshop case flagged by Mueller] LCP improved by removing CSS transitions at the top, removing `loading="lazy"` from the first image and adding `fetchpriority="high"` to 1–2 images; first check which element is the real LCP element. Self-reported data; consistent with web.dev.
- [SEJ 2025-12 and 2026-05, HTTP Archive/CrUX] Share of sites with good Core Web Vitals by platform (April 2026: Duda ~85%, Wix ~80%, Shopify ~79%, WordPress ~49%); page weight and Lighthouse score do not predict real Core Web Vitals. Descriptive data, not causal.
- [SEJ 2025-12, news] Safari 26.2 exposes LCP and INP to RUM scripts; CrUX, PSI and Search Console remain Chrome-based, so Safari users need your own measurement (PF-21).
- [SEJ 2025-11, Mueller] A heavy hero video loaded in the background after the content should have no visible SEO effect.
- [SEJ 2026-02, Illyes/Splitt] Googlebot does not benefit from resource hints (`preload`, `preconnect`); they remain useful for users and Core Web Vitals.
- [SEJ 2025-10] Several Lighthouse audits were removed in Lighthouse 13; scripts or reports that use old audit IDs need remapping (see `myths-deprecated.md`).

## Myths and outdated advice
- **"A Lighthouse/PSI score of 100 is a ranking goal"**: the Performance score is lab data and not the Core Web Vitals assessment; Google says a perfect score just for SEO may not be worth the time. [G](https://developers.google.com/search/docs/appearance/page-experience) [G](https://developers.google.com/speed/docs/insights/v5/about)
- **"Lab LCP/CLS = what Google uses"**: the Search Console Core Web Vitals report and the PSI assessment use field data (CrUX); lab values are for debugging. [G](https://support.google.com/webmasters/answer/9205520) [web.dev](https://web.dev/articles/vitals)
- **"Core Web Vitals outrank relevance"**: relevance wins; page experience helps among equally helpful pages. [G](https://developers.google.com/search/docs/appearance/page-experience)
- **"There is a page experience score/signal"**: there is no single signal. [G](https://developers.google.com/search/docs/appearance/page-experience)
- **FID as a Core Web Vital**: retired; INP is its successor. [web.dev](https://web.dev/articles/vitals)
- **"A service worker makes the site fast for Googlebot"**: Googlebot does not keep state between loads; the cache helps only repeat users *(inference)*. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)
- **"Lazy-load every image"**: never the LCP or other immediately visible images. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading) [web.dev](https://web.dev/articles/optimize-lcp)
- **Moving critical JS/CSS to a separate CDN host "for crawl budget"**: advised against since 6 December 2024 for performance reasons. [G](https://developers.google.com/search/blog/2024/12/crawling-december-resources)
