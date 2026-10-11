# Local SEO

> Updated 2026-10-11. Scope: Business Profile, `LocalBusiness` markup, reviews, location pages, local presence in AI features and assistants. Primary source: Google Search Central and Google Business Profile Help; third-party views marked [SEJ].
> Source legend: `[G](url)` = Google Search Central documentation. `[G OH YYYY-MM](url)` = Google Search Office Hours. `[GBP](url)` = Google Business Profile Help or the Maps contributed-content policy, checked 2026-10-11; `[GBP]` without a link = not found there, marked *(re-verify)*. *(inference)* = reasoning from Google facts, not stated by Google. `[SEJ …]` = third-party source (opinion, vendor study, single case).
> Related files: `structured-data.md` (JSON-LD syntax, self-reviews SD-16), `entity-personal-brand.md` (identity, author, legal notices), `content-quality-spam.md` (doorways, scaled content), `ai-search.md` (AI controls, AI measurement, bots), `crawling-indexing.md`, `bing-basics.md` (Bing Places and Bing Webmaster Tools).

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
- [Audit checks](#audit-checks)
- [Build rules](#build-rules)
- [Off-site checklist](#off-site-checklist)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

## Facts and rules (Google)

### 1. Business Profile and local listings
- Presence on the map and in local results goes through the **Google Business Profile** (GBP): if the business does not appear for a local query, the first check is whether the profile has been added and claimed. [G](https://developers.google.com/search/help/site-appearance-faq)
- After claiming (business.google.com) the owner manages **address, contact details, business type and photos**, which feed the knowledge panel and Maps. Google also recommends **verifying the site in Search Console** to establish it as the official presence. [G](https://developers.google.com/search/docs/appearance/establish-business-details)
- The knowledge panel can be corrected with the **Feedback** link if at least a week has passed since the page with markup was last crawled; a verified representative sees more options. The system takes **about a week** to update the details. [G](https://developers.google.com/search/docs/appearance/establish-business-details)
- Claiming the GBP also brings direct notices (Maps restrictions, legal removals, bulk review restrictions); verifying Search Console brings notices about manual actions and security. [G](https://developers.google.com/search/help/small-business-notifications)
- AI features (AI Overviews, AI Mode) can show information about local businesses: Google says to keep the **Business Profile** up to date (and Merchant Center for products). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- GBP images are a channel for showing products and services across Google products. [G](https://developers.google.com/search/help/site-appearance-faq)
- Link **all profiles** (GBP, social, listings) to the official site: Office Hours case of a service business that was not found because its "site" was not referenced by its other listings. [G OH 2023-12](https://developers.google.com/search/help/office-hours/2023/december)
- Business closed for good: **mark it as closed** in the GBP and remove or redirect the old site. [G OH 2023-12](https://developers.google.com/search/help/office-hours/2023/december)
- Other map listings: **Bing Places for Business** (free, can import from GBP; Bing details live in `bing-basics.md`) and **Apple Business Connect** (Apple Maps) are separate listings to keep consistent with the GBP (→ LO-02). [SEJ 2025-10, news Microsoft] · [SEJ 2026-07/08]

**Business Profile rules**
- **Eligibility**: "To qualify for a Business Profile, a business must make in-person contact with customers during its stated hours" (at its premises or at the customer's). Brands, organisations, artists and other **online-only** businesses are listed as ineligible, as are properties for rent or sale, lead-generation agents and P.O.-box addresses. [GBP](https://support.google.com/business/answer/13763036)
- **Service-area business** (visits or delivers to customers, does not serve them at its address): remove or hide the address and set the service area; a hybrid business shows the address and also sets a service area. Up to 20 service areas (cities, postal codes, regions), no radius. Unstaffed addresses (P.O. boxes, remote mailboxes, virtual offices) are not allowed. [GBP](https://support.google.com/business/answer/3038177) · [GBP](https://support.google.com/business/answer/9157481)
- **Name**: the real-world name used on signage, stationery and branding, with no taglines or location details added to the name. [GBP](https://support.google.com/business/answer/3038177)
- **Primary category**: the most specific category that describes the core business as a whole ("this business IS a", not "HAS a"); use as few categories as possible (up to 9 additional); never categories used only as keywords. [GBP](https://support.google.com/business/answer/3038177) · [GBP](https://support.google.com/business/answer/3039617)
- **Reviews**: no incentives (payment, discounts, free goods or services), no selective soliciting of satisfied customers only, no content based on a conflict of interest (including current or former employment, i.e. owners and staff), no fake engagement; merchants may not ask for a set number of reviews or for specific content, nor pressure customers to review on the premises. Asking for genuine reviews is allowed. [GBP](https://support.google.com/business/answer/2622994) · [GBP](https://support.google.com/contributionpolicy/answer/7400114)
- **Closures**: **special hours** for holidays and closures of up to 6 days in a row; "**Temporarily closed**" for 7 days or more, the off-season or an unknown period; temporarily closed businesses can rank after open ones for broad queries. [GBP](https://support.google.com/business/answer/6303076) · [GBP](https://support.google.com/business/answer/15300196) Do not delete the profile to signal a closure. [GBP] *(re-verify)*

### 2. `LocalBusiness` structured data [G](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- It enables details in the knowledge panel (hours, departments, contacts). Bookings and orders from results go through the **Maps Booking API**, not markup. The restaurant carousel has limited access. No country restriction is stated for the basic panel.
- It can go on any page, but is most useful on the page with the business information. **One entity per location**; use the **most specific subtype**; several types go in an **array** on `@type` (**`additionalType` is not supported**).
- `LocalBusiness` is a subtype of `Organization`: Organization fields also apply (`logo`, `sameAs`, `email`, `vatID`, `contactPoint`…). [G](https://developers.google.com/search/docs/appearance/structured-data/organization)
- **Required**: `name`, `address` (`PostalAddress`, as complete as possible; `addressCountry` ISO 3166-1 alpha-2, e.g. `NO`, `IT`).
- **Recommended**: `telephone` (with the international prefix, e.g. `+47`), `url` (URL of the **specific location**, working), `geo` (latitude/longitude with **at least 5 decimals**), `openingHoursSpecification`, `priceRange` (**under 100 characters**, otherwise not shown), `department`, `menu`/`servesCuisine` (food service only); `aggregateRating`/`review` **only for sites that collect reviews about other businesses**.
- **Hours**: `dayOfWeek` in English (short form `Monday` is accepted); without `validFrom`/`validThrough` they apply all year; past midnight in a single block; 24 h = `00:00`–`23:59`; closed all day = `00:00`–`00:00`; **seasonal or holiday closures** = `validFrom` + `validThrough` with `00:00`–`00:00`. Enum values stay in English on sites in any language. [G OH 2023-08](https://developers.google.com/search/help/office-hours/2023/august)
- Services priced on quotation: use `LocalBusiness` (which accepts a price range), **not `Product`**. [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january)
- Violations → possible manual action; under a manual action the structured data is **ignored** (the page stays in Search). Google does not guarantee display. [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Structured data is **not needed** to appear in AI features; there is no special markup "for AI". [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### 3. Reviews
- **Self-serving**: if the reviewed entity controls the reviews about itself, its pages with `LocalBusiness` or any `Organization` are **not eligible for stars**, both with direct markup and with **embedded widgets** (Google, Facebook reviews). Owner check: SD-16. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- Ratings of local businesses must come **directly from users**, not from human editors who create or curate them. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- **Do not aggregate** reviews from other sites; **no fake reviews or undisclosed incentivised reviews** (incentive = money, discounts, vouchers, free products), neither in markup nor on the page; reviews not from real users can lead to a **manual action**. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) · [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Each review or rating must refer to **one specific item** (a single target) and be **visible on the page**; if several reviews are marked up, mark up all of them. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- The **reviews system** (it applies in many languages; the source page lists them) evaluates review content written by the site (guides, comparisons), **not** customer reviews shown on the page. [G](https://developers.google.com/search/docs/appearance/reviews-system)
- Exchanging products or services for reviews that contain links = **link spam**. [G](https://developers.google.com/search/docs/essentials/spam-policies)

### 4. Location pages, doorways and keyword stuffing [G](https://developers.google.com/search/docs/essentials/spam-policies)
- **Doorways**: several pages or domains targeting regions or cities that funnel to a single destination; near-identical pages that look more like search results than a browsable hierarchy.
- **Keyword stuffing**: blocks of text listing the cities and regions the site wants to rank for; lists of phone numbers with no added value.
- **Scaled content abuse**: many pages generated (with AI or by hand) to manipulate ranking, including a page for every query variant. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- The **deduplication system** shows only the most relevant result among very similar pages; **site diversity** generally limits a site to two results. [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide)

### 5. Signals and appearance
- Local queries → local results: relevance also depends on the **user's location**; the map does not appear for every query and should not be "chased". [G](https://developers.google.com/search/docs/fundamentals/how-search-works) · [G OH 2023-03](https://developers.google.com/search/help/office-hours/2023/march)
- The `<title>` can include the **business name and physical location**; for a local business Mueller suggested the city or area in titles. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G OH 2023-03](https://developers.google.com/search/help/office-hours/2023/march)
- Google's example of a good meta description: **what it offers + opening hours + where it is**. [G](https://developers.google.com/search/docs/appearance/snippet)
- Queries with a high position but low CTR because users already find hours, address or phone in the results page: expected behaviour when the goal is contact. [G](https://developers.google.com/search/docs/monitor-debug/bubble-chart-analysis)
- **ccTLD** (e.g. `.no`, `.it`): a low-impact country signal; language matters more. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G OH 2024-07](https://developers.google.com/search/help/office-hours/2024/july)
- The crawler sees content from its own location, usually the USA: do not make hours, prices or contacts depend on IP geolocation. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- **Top places list**: shows third-party editorial lists in which the business is mentioned; **only businesses with a physical location**; lists must be curated, independent and not sponsored. [G](https://developers.google.com/search/docs/appearance/top-places-list)

### 6. Features vary by country
Some local features exist only in some countries, and the list changes. Before recommending one, check availability:
1. Open the Google page for the feature (Source column) and read its availability section; the overview of region-specific features is the aggregator-features page. [G](https://developers.google.com/search/docs/appearance/aggregator-features)
2. In Search Console › Performance, filter by **Country** and look at **Search appearance** to see whether the feature actually shows for the site's market.
3. For features reported only by third parties (no Google page), say so and give the country and date of the report.

| Feature | Where | Notes | Source |
|---|---|---|---|
| Aggregator units + supplier units (local business queries included since 18 September 2026) | EEA only | The direct supplier does not need to submit data beyond what is crawled (feeds optional); the supplier unit appears only with the aggregator unit; directories must be approved as vertical search services | [G](https://developers.google.com/search/docs/appearance/supplier-unit) · [G](https://developers.google.com/search/docs/appearance/aggregator-unit) |
| Structured data carousels for local businesses | EEA, Türkiye (South Africa has structured data carousels; check the type list for local businesses) | For sites that list several entities (aggregators), not for the single business | [G](https://developers.google.com/search/docs/appearance/aggregator-features) |
| "Places sites" (carousel + chips) | Türkiye only | No markup; interest form | [G](https://developers.google.com/search/docs/appearance/places-sites) |
| Site reputation abuse: manual action | Applies only outside the EEA since late August 2026 *(re-verify exact date)* | In the EEA the section may be classified separately from the main domain, without manual action | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| Ask Maps, AI calls to businesses, agentic booking of local services | USA (Ask Maps also India) | Third-party sources only; not available in the EEA as of October 2026 | [SEJ 2026-03/05/06] |
| GBP tools in the Gemini app | Global **except EEA and UK** | Insights, draft replies to reviews | [SEJ 2026-06] |
| Apple Maps ads (some categories banned) | USA/Canada | Advertising only | [SEJ 2026-07] |

### 7. AI and local search (Google's position)
- AI Overviews and AI Mode use the core ranking systems; there are no additional requirements: page **indexed and eligible for a snippet**, crawling allowed in robots.txt **and by the CDN/hosting**, important content **in text**, structured data consistent with the visible content, GBP up to date. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Controls over how content appears in AI features (snippet directives, the Search Console opt-out setting, the fact that Google-Extended does not affect Search) are listed once in the `ai-search.md` Controls table. [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Measurement: generative AI performance report in Search Console (**impressions only**, by page/country/device; global since 31 August 2026). [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)
- Manipulating AI answers (inauthentic mentions or reviews) falls under the spam policies; chasing inauthentic mentions is "not useful". [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **ChatGPT, Perplexity, Copilot, Apple**: no Google documentation; third-party sources only (see below). Bing Places and Apple Business Connect are separate, free listings (third-party sources).

### 8. Local directories (Google's position)
- Do **not** sign up to directories to improve SEO; use them, if at all, for direct traffic. "Local search is different." [G OH 2022-11](https://developers.google.com/search/help/office-hours/2022/november)
- **Low-quality** directories and social bookmarking for links = link spam; for off-page SEO "don't waste your time". [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G OH 2023-05](https://developers.google.com/search/help/office-hours/2023/may)
- *(inference)* Consistent data across listings (GBP, Bing, Apple, industry directories) serves users, the GBP and systems that read the web; it is not a link tactic.

## Audit checks

Severity follows the scale in `conventions.md`. For local sites, Critical also covers wrong information given to customers. "Auto" = verifiable from code or HTML; "Manual" = needs the user or an external tool.

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| LO-01 | NAP (name, address or area, phone) in visible **HTML text**, identical on home, contact page, footer and JSON-LD | Auto: extract text from initial and rendered HTML; compare normalised strings | High | [G](https://developers.google.com/search/docs/appearance/ai-features) · *(inference)* |
| LO-02 | Site NAP = GBP = Bing Places = Apple Business Connect = industry directories | Manual: the user pastes the listing data; the skill compares field by field | High | [SEJ 2026-08, Uberall/AthenaHQ] · [GBP](https://support.google.com/business/answer/3038177) |
| LO-03 | Hours, contacts and services not only in an image, PDF or JS widget | Auto: look for hours and phone in the DOM; flag flyer `<img>`, iframes, widgets | High | [G](https://developers.google.com/search/docs/fundamentals/get-started-developers) |
| LO-04 | Phone as a `tel:` link with the international prefix (e.g. `+47`) | Auto: regex on `href="tel:"` | Low | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-05 | `LocalBusiness` present on the info/contact page when there is a **location that receives customers** | Auto: parse JSON-LD; Manual: ask whether the location receives customers | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-06 | Most specific subtype; several types as an `@type` array; no `additionalType` | Auto | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-07 | Required `name` + complete `address` (`streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` ISO-2) | Auto | High | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-08 | `telephone` with country prefix; `geo` ≥ 5 decimals; `priceRange` < 100 characters; location `url` returns 200 | Auto | Low | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-09 | `openingHoursSpecification` consistent with the visible hours; `dayOfWeek` in English; valid time format | Auto: compare JSON-LD ↔ page text | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-10 | Alias of SD-16 — verify there, report once | Auto: JSON-LD + search for review-widget scripts (Google/Facebook) on the site's own `LocalBusiness`/`Organization` | High | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| LO-11 | Real testimonials; incentives disclosed; no invented or "curated" reviews; none aggregated from other sites | Manual: ask where they come from; Auto: look for markup with repeated or generic authors | Critical | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| LO-12 | Each rating has **a single** `itemReviewed` and is visible on the page | Auto | High | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| LO-13 | **Near-identical** city/area pages (doorways) | Auto: similarity of the main text across pages with a `/{service}-{city}` pattern; flag when only the place name changes | Critical | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| LO-14 | Blocks listing cities/neighbourhoods or repeated phone numbers | Auto: lists of more than ~10 place names without a contextual sentence (heuristic threshold) | High | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| LO-15 | One page per real **service**, with distinct content, CTA and next step | Auto: map pages to services; Manual: list of the real services | Medium | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [SEJ 2025-12, Riddall] |
| LO-16 | `<title>` of home, contact and service pages with business + place (or "online"); no bare "Home"/"Contact" | Auto | Medium | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| LO-17 | Meta description of home and contact page with what it offers + hours/format + where | Auto | Low | [G](https://developers.google.com/search/docs/appearance/snippet) |
| LO-18 | Service area / online format described in sentences (not lists of cities) | Auto + judgement | Medium | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| LO-19 | Temporary closures and holidays: visible notice + `validFrom`/`validThrough` + GBP special hours; site **not** switched off nor set to `noindex` | Auto (text/JSON-LD), Manual (GBP) | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) · [GBP](https://support.google.com/business/answer/6303076) · *(inference)* |
| LO-20 | Old pages with outdated NAP (`-old`, `v2`, duplicates after a redesign) still indexable | Auto: crawl + search for old numbers/addresses; Manual: `site:` | Medium | [SEJ 2026-09, Shaw/Jeffery] |
| LO-21 | Googlebot not blocked by robots.txt/CDN/WAF; an **explicit** decision on AI search bots (e.g. Cloudflare settings) | Auto: robots.txt; Manual: CDN panel, URL Inspection | High | [G](https://developers.google.com/search/docs/appearance/ai-features) · [SEJ 2026-09] |
| LO-22 | Accessible contact/booking form: `<label>`, named buttons, no CAPTCHA or overlay blocking the flow | Auto: accessibility tree | Medium | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| LO-23 | Key content in the **initial HTML** (SPA: SSR/prerender) for crawlers that do not run JS | Auto: compare raw vs rendered HTML. Caveat: Google renders JavaScript, so this is about third-party assistants and bots that do not (list in the `ai-search.md` bot table); raise to High when visibility in those assistants is a stated goal | Medium | [SEJ 2026-09, CallRail] |
| LO-24 | Browser-side call-tracking numbers do not replace the canonical number seen by crawlers | Auto: diff the number in raw HTML vs DOM | Medium | [SEJ 2026-09, CallRail] · *(inference)* |
| LO-25 | If **no location is open to the public**: no `LocalBusiness` with an address that the GBP hides; use `Organization`/`Person` | Manual + Auto | Medium | *(inference)* from [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) + [GBP](https://support.google.com/business/answer/3038177) |
| LO-26 | `FAQPage` kept only for users: no expectation of rich results | Auto. FAQ rich results stopped showing on 7 May 2026; status in `structured-data.md` › Retired or restricted rich results | Low | [G](https://developers.google.com/search/updates#removing-faq-rich-result) |
| LO-27 | Valid, parsable JSON-LD; no errors in the Rich Results Test | Auto: parse; Manual: Rich Results Test | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| LO-28 | Link from the site to the GBP (e.g. "Leave us a review") and GBP website field pointing to the home or canonical location page (https, no inconsistent parameters) | Auto (outgoing links); Manual (GBP) | Medium | [G OH 2023-12](https://developers.google.com/search/help/office-hours/2023/december) |
| LO-29 | Search Console verified (Domain property) and GBP claimed | Manual | High | [G](https://developers.google.com/search/help/small-business-notifications) |
| LO-30 | Conversions measured: clicks on `tel:`/email/booking as events; GBP → GA4 link | Auto (events in code); Manual (GA4) | Medium | [SEJ 2026-06, news Google] |
| LO-31 | Prices or ranges and format (in person/online, duration) stated in text | Auto + judgement | Medium | [SEJ 2026-07, Heitzman] · [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) (`priceRange`) |
| LO-32 | Credentials and professional registrations verifiable on the practitioner's page (topics close to work, money or health) | Manual | High | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |

## Build rules
1. **Service pages before city pages.** One page per real service (what, for whom, how it works, duration, price or range, in person/online, next step) → LO-15, LO-31. Location pages are legitimate only when there is a **real location** or genuinely local content (cases, partners, regulations, logistics); otherwise they are doorways → LO-13 [G](https://developers.google.com/search/docs/essentials/spam-policies).
2. **Anti-doorway test** *(inference)*: if the page stays true after swapping the city name, it must not exist as a separate page → LO-13. Example: Northwind Physio has one clinic in Oslo; pages such as `/physiotherapy-bergen` or `/physiotherapy-trondheim` that only change the city name are doorways, even if each one is "unique" after a rewrite. Doorways can lead to a manual action, which may affect only some pages or the whole site.
3. **Service area in prose** → LO-18, LO-14: "Clinic in Oslo; home visits across Oslo municipality" (Northwind Physio) or "Sessions at our Bologna office; online sessions anywhere in Italy" (Studio Ferri Orientamento), not lists of towns.
4. **Local + online practitioner** (*(inference)* from [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) + [GBP](https://support.google.com/business/answer/3038177)) → LO-05, LO-25:
   - physical location that receives customers → GBP with address + `LocalBusiness` (most specific subtype) on the contact page;
   - visits customers → GBP with service area; no address on the site that the GBP hides;
   - online only → no GBP (not eligible); `Organization` or `Person`/`ProfilePage` (see `entity-personal-brand.md`); one "Online sessions" page, not one per city;
   - same offer in person and online → one service page with two formats, not two near-identical pages.
5. **Complete contact page in HTML** → LO-01, LO-03, LO-04: name, address or area, `tel:` phone, email, hours, booking method, optional map (the iframe does not replace the text).
6. **Temporary closures** (*(inference)* + [G](https://developers.google.com/search/docs/appearance/structured-data/local-business)) → LO-19: visible notice at the top, hours updated in JSON-LD (`validFrom`/`validThrough`), GBP with special hours or "Temporarily closed"; do not add `noindex`, do not switch the site off, do not redirect.
7. **Reviews on the site** → LO-10, LO-11, LO-12: show them as text with name, date and source; **no stars in the markup** of your own business; no reviews edited or selected in a misleading way [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
8. **Verifiable facts in text** → LO-31, LO-32: prices or ranges with their variables, timings, formats, credentials; this is the information assistants look for and that Google suggests having in text form [G](https://developers.google.com/search/docs/appearance/ai-features).
9. **Topics close to YMYL** (jobs and careers, money, health) → LO-32: no guaranteed outcomes, an author with real credentials, cited sources, dated updates [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
10. **Informational content** (blog, guides) linked to the service pages, based on real customer questions, not one page per query variant [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
11. **Minimal, maintained structured data** → LO-08, LO-27: a correct, up-to-date `LocalBusiness` beats rich but stale markup (risk: an old phone number in the schema) [SEJ 2026-09, Shaw/Jeffery].
12. **Tax and legal identifiers**: whether VAT or registration numbers must appear on the site depends on the country and profession; see `entity-personal-brand.md` › Regulated professions and legal notices. In markup, `vatID` is an Organization field Google lists as a trust signal [G](https://developers.google.com/search/docs/appearance/structured-data/organization).

## Off-site checklist
Manual actions the skill can only guide: the skill prepares texts, fields and checks; the user carries them out.

**Google Business Profile**
- [ ] Check **eligibility** [GBP](https://support.google.com/business/answer/13763036): in-person meetings (office or at the customer's)? If the service is **online only**, the business is not eligible for a GBP: focus on the site, the entity and mentions.
- [ ] Claim/verify the profile; one profile per real location; no duplicate listings [GBP](https://support.google.com/business/answer/3038177).
- [ ] Real **name**, with no taglines or location details added to the name [GBP](https://support.google.com/business/answer/3038177).
- [ ] Most specific **primary category** + few relevant secondary ones [GBP](https://support.google.com/business/answer/3039617); check that the **services** listed match the site's service pages [SEJ 2025-12, Riddall].
- [ ] **Location vs service area**: if customers come to you → visible address; if you go to customers → hidden address + service area [GBP](https://support.google.com/business/answer/9157481). Never virtual-office addresses [GBP](https://support.google.com/business/answer/3038177).
- [ ] Real **hours** + special hours for holidays set in advance; "Temporarily closed" for closures of 7 days or more [GBP](https://support.google.com/business/answer/15300196); for SEJ, "open at the time of the search" is among the most cited local pack factors [SEJ 2026-03, Heitzman, Whitespark survey].
- [ ] **Description** in the customers' language (not a keyword list; no links allowed [GBP](https://support.google.com/business/answer/3038177)).
- [ ] Authentic **photos** (premises, people, context), not stock; refresh them periodically [SEJ 2026-03, opinion].
- [ ] **Posts** for news and events; since September 2026 the GBP shows **views per post** (last 18 months) [SEJ 2026-09, news Google].
- [ ] **Booking/appointment link** and website link with consistent UTM parameters (canonical to the URL without UTM [G OH 2024-08](https://developers.google.com/search/help/office-hours/2024/august)).
- [ ] Link **GBP → Google Analytics** (7 metrics, 6-month retention) [SEJ 2026-06, news Google].
- [ ] Check the **public profile**, not only the dashboard (bug in July 2026 with empty review dashboards) [SEJ 2026-07].

**Reviews**
- [ ] Ask **all** customers for reviews (no filtering for satisfied ones), with a simple link or QR code; no undisclosed incentives; Maps policy forbids asking for a set number of reviews or for specific content (e.g. the name of a staff member) [GBP](https://support.google.com/contributionpolicy/answer/7400114) · [SEJ 2026-09, Moz speakers].
- [ ] Remind customers that they can review under a **nickname**, useful where clients value privacy (e.g. physiotherapy at Northwind Physio, career guidance at Studio Ferri Orientamento, legal matters) [SEJ 2025-12, news Google].
- [ ] Reply to all of them, negative ones included, with the next reader in mind.
- [ ] Analyse the **themes** of your own reviews and of 2–3 competitors' to write H1s, FAQs and the GBP description [SEJ 2026-06, opinion].

**Other listings (NAP consistency)**
- [ ] **Bing Places** (free, imports from GBP) [SEJ 2025-10, news Microsoft]; details in `bing-basics.md`.
- [ ] **Apple Business Connect** / Apple Maps listing [SEJ 2026-07/08].
- [ ] Credible **industry** directories and professional associations (for users and reputation, not for links) [G OH 2022-11](https://developers.google.com/search/help/office-hours/2022/november).
- [ ] Inventory old or duplicate listings (old addresses, numbers) and ask for correction or closure.

**Reputation and local mentions**
- [ ] Mentions from local press, associations, public bodies, partners, events (talks, workshops) [SEJ 2026-08, Uberall/AthenaHQ; SEJ 2026-07, Montti].
- [ ] Never paid or self-published "best of [city]" lists.

**AI and assistants (monitoring, not optimisation)**
- [ ] A fixed list of 10–20 questions (hours, services, prices, "who would you recommend for … in [city]") on AI Overviews/AI Mode, ChatGPT, Gemini, Perplexity, Copilot; repeat several times, record date, place and device; correct the wrong **sources** (old directories, threads) [SEJ 2026-07, Searchable].
- [ ] Bing Webmaster Tools (AI Performance report) as a free source of Copilot citations [SEJ 2026-03].

## Notes by site type
- **ecommerce**: a shop with physical stores gets one `LocalBusiness` (most specific subtype, e.g. `Store`) per store page and one GBP per store; products go through Merchant Center, not the GBP. → LO-05, LO-07
- **local-business**: the full file applies; start with eligibility, NAP consistency and the contact page (LO-01, LO-02, LO-29), then reviews and location pages (LO-11, LO-13). Example: Northwind Physio (Oslo).
- **personal-brand**: usually online only → no GBP and no `LocalBusiness`; identity via `Person`/`ProfilePage` in `entity-personal-brand.md`. → LO-25
- **professional-services**: decide between location, service area and online only (Build rule 4); credentials and YMYL care apply (LO-32). Example: Studio Ferri Orientamento (Bologna, in person and online).

## Third-party views
Format: [SEJ YYYY-MM, author, evidence type and sample]. ⚠ = goes beyond or against Google; not to be recommended.

**Business Profile and local ranking**
- [SEJ 2026-03, Heitzman, opinion + Whitespark 2026 survey and BrightLocal on 50 businesses] Primary category = local pack factor no. 1, then proximity and **keywords in the name**; "open now" in the top 5; reviews gained weight (16%→20%). ⚠ Keywords in the name violate the GBP guidelines [GBP](https://support.google.com/business/answer/3038177): do not recommend them. Cadences (weekly posts, photos every two weeks, replies within 48 h) = opinion.
- [SEJ 2025-11, Riddall, experience checklist] 11-point local audit (complete GBP, reviews with replies, NAP, local links, content by stage, AI Mode). ⚠ Recommends `Review` and `FAQPage` schema: the first is not allowed on your own business, the second no longer yields rich results.
- [SEJ 2025-12, Riddall, opinion + third-party data] GBP as a "verified source" for AI Mode; GBP services consistent with the site; CTA above the fold; KPIs = calls, directions, bookings.
- [SEJ 2026-06, Southern, news] Ask Maps (USA/India): multi-condition answers based on complete profile data; Google shut down the Q&A API (November 2025); status of public Q&A unclear.
- [SEJ 2025-10, news Microsoft] Bing Places relaunched, free, imports from GBP.

**Reviews**
- [SEJ 2026-06, Southern, peer-reviewed study of 251 US SMBs, self-reported data] Stars alone do not predict results; **active** reputation management does.
- [SEJ 2026-06, vendor SOCi, 350,000 locations] ChatGPT recommended 1.2% of locations (Gemini 11%, Perplexity 7.4%) against 35.9% presence in the 3-pack; average rating of recommended locations ~4.3. Correlation, vendor data.
- [SEJ 2026-07, news Google] The review snippet guidelines now state explicitly that fake or undisclosed incentivised reviews → manual action.
- [SEJ 2026-06, Wiideman, case n=1] ⚠ Proposal to give customers suggested phrases for reviews ("semantic triples"): steered reviews, against the policies (Maps forbids soliciting specific content [GBP](https://support.google.com/contributionpolicy/answer/7400114)); do not use.

**Data consistency and directories**
- [SEJ 2026-07, vendor Searchable, 165 London companies, 13,365 questions] 93% had at least one wrong or missing fact in AI assistants; small businesses were hit hardest.
- [SEJ 2026-08, vendor Uberall/AthenaHQ, 7 models] Consistency of NAP, hours and categories across GBP, Apple, Bing and directories; external confirmations with editorial criteria, not paid lists.
- ⚠ Against Google: several authors treat directory "citations" as a ranking factor; Google says directories do not help SEO. Summary for the skill: consistency yes, mass listing for links no.
- [SEJ 2026-01, van Berkel/Schema App, single vendor case, no control] ⚠ `areaServed`/`sameAs` to Wikidata on location pages with "complete causation" of +25% clicks: claim not sustainable; `areaServed` is not among the properties Google documents for `LocalBusiness` (valid in schema.org, effect undocumented).

**AI and local search**
- [SEJ 2026-07/08, Whitespark cited, 540 queries in 3 US cities] AI Overviews on 15% of direct local queries, 92% of informational ones, 97% of hybrid ones; another article reported 68% for "business type" queries: figures depend on the query type, quote with care.
- [SEJ 2026-09, CallRail, sponsored webinar] Clicks from AI citations ~1–2% of calls; AI bots do not run JS → NAP in the initial HTML; browser-side number swapping invisible to bots.
- [SEJ 2026-09, Shaw/Jeffery, webinar without data] Cloudflare often blocks AI crawlers by default; JS review widgets invisible; schema "harmful" only when not maintained. Panel divided on the usefulness of schema.
- [SEJ 2026-09, news] Since 18 September 2026 EEA aggregator/supplier units also show for local queries: monitor, no specific action.
- [SEJ 2026-05, Southern on I/O] USA: Google can call businesses on the user's behalf; clear hours, prices and availability become a practical requirement.
- [SEJ 2026-08, Kris Jones, opinion] Audit: ask an assistant to recommend a provider in your own category; correct outdated sources (case of a Reddit thread with old prices).

**Location pages**
- [SEJ 2026-07, Heitzman, agency experience across 15+ markets] Location pages that are not copies, with NAP/hours, local FAQs, real cases; cost guides with ranges. ⚠ "3 photos of landmarks to prove the location" and "a 12–18 month window": no basis.
- [SEJ 2026-02, Forrester, conceptual model] Local pages with proof of real presence and service boundaries; remove doorways at template level.

**To re-verify**
- FAQ rich results removal (LO-26, Myths): reported by SEJ 2026-05; status owned by `structured-data.md`. *(re-verify)*
- Effective date of the EEA change to site reputation abuse (§6): the policy page gives no date. *(re-verify)*
- "Do not delete the profile to signal a closure" (§1): not stated on the GBP closure pages. *(re-verify)*

## Myths and outdated advice
- **"Signing up to lots of directories improves ranking"** → no, according to Google; low-quality directories for links = spam [G OH 2022-11](https://developers.google.com/search/help/office-hours/2022/november).
- **"A page for every city increases coverage"** → doorways [G](https://developers.google.com/search/docs/essentials/spam-policies).
- **"A list of cities in the footer"** → keyword stuffing [G](https://developers.google.com/search/docs/essentials/spam-policies).
- **"Stars in the results with the Google reviews widget on the site"** → not eligible (self-serving) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **"`FAQPage` to win space in the results"** → FAQ rich results stopped showing on 7 May 2026; see `structured-data.md` › Retired or restricted rich results [G](https://developers.google.com/search/updates#removing-faq-rich-result).
- **"`LocalBusiness` schema gets you into the local pack / into AI answers"** → the local pack depends on the GBP; there is no special markup for AI [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"`llms.txt` or Markdown versions help local assistants"** → ignored by Google Search [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"Keywords in the domain (e.g. physio-oslo.example)"** → near-zero effect; the systems do not reward exact-match domains [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide).
- **"Geotags/EXIF in photos"** → Google does not use image EXIF data in Search [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january); undocumented for the GBP *(inference)*.
- **"During holidays I put the site in maintenance mode / noindex"** → visibility is lost; use special hours and notices (*(inference)* + [G](https://developers.google.com/search/docs/appearance/structured-data/local-business)).
- **"Buying 'best of [city]' lists"** → the top places list requires non-sponsored lists [G](https://developers.google.com/search/docs/appearance/top-places-list); inauthentic mentions = spam.
- **"Variable prices with `Product` for services"** → use `LocalBusiness` with `priceRange` [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january).
- **US advice applied to other markets**: Ask Maps, AI calls, agentic booking, Apple Maps ads and GBP tools in Gemini are limited to some countries (see §6); as of October 2026 none of them was available in the EEA. Check availability before recommending them.
