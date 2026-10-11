# Structured data

> Updated 2026-10-11. Scope: choosing, generating and validating JSON-LD for any site (new or live, any framework). Primary source: Google Search Central; third-party views marked [SEJ].
> Sources: Google Search Central documentation (read 2026-10-03; retirement statuses re-checked against the Google changelog on 2026-10-11), Google Search Central blog 2023–2026, Search Engine Journal summaries (secondary). Tags: `[G](url)` Google documentation or blog · `[SEJ YYYY-MM]` third-party view · *(inference)* operational deduction, not Google text · ⚠ deprecated or not to be recommended.
> Golden rule: Google never guarantees a rich result, even with valid markup [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). Before proposing a type, check [Retired or restricted rich results](#retired-or-restricted-rich-results) and, for changes after this date, the changelog `https://developers.google.com/search/updates`.

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
  - [Formats](#formats) · [Required and recommended properties](#required-and-recommended-properties) · [Visible content and quality guidelines](#visible-content-and-quality-guidelines) · [Manual actions](#manual-actions) · [JavaScript-generated markup](#javascript-generated-markup) · [Testing and validation](#testing-and-validation) · [@id and the graph](#id-and-the-graph)
  - [Choice matrix by site type](#choice-matrix-by-site-type)
  - Types: [WebSite](#website-site-name) · [Organization](#organization) · [LocalBusiness](#localbusiness-and-subtypes) · [Person / ProfilePage](#person--profilepage) · [Article](#article--blogposting--newsarticle) · [BreadcrumbList](#breadcrumblist) · [Review / AggregateRating](#review--aggregaterating) · [Event](#event) · [Course](#course) · [VideoObject](#videoobject) · [Product and merchant listings](#product-offer-productgroup-and-merchant-listings) · [JobPosting](#jobposting)
  - [JavaScript and SPA notes](#javascript-and-spa-notes)
- [Retired or restricted rich results](#retired-or-restricted-rich-results)
- [Audit checks](#audit-checks)
- [Build rules](#build-rules)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

## Facts and rules (Google)

### Formats
- Three supported formats: **JSON-LD (recommended)**, Microdata, RDFa. All are valid when correct; JSON-LD is preferred because it is easier to maintain at scale and less error-prone [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
- JSON-LD goes in `<script type="application/ld+json">`, in `<head>` or `<body>`; it is not interleaved with visible text. Google also reads JSON-LD **injected dynamically** (JavaScript, CMS widgets) [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
- Exception: for `DiscussionForumPosting` Google suggests Microdata/RDFa (avoids duplicating long texts), but JSON-LD remains supported [G](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum).
- Vocabulary: almost always schema.org, but **Google's reference is Search Central, not schema.org**; many schema.org properties are not used by Google [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). `data-vocabulary.org` is no longer eligible [G](https://developers.google.com/search/updates).
- `@context`: `https://schema.org`. One value per field when the property is an identifier (e.g. GTIN, `sku`): no comma-separated lists [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) (also said in Google Search Office Hours, 2022).
- CMS (WordPress, Wix, Shopify…): use the SEO settings or a plugin instead of hand-writing markup [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). *(inference)* Before adding manual markup, check that the CMS or plugin does not already emit some (avoid contradictory duplicates).

### Required and recommended properties
- All **required** properties are needed for eligibility; **recommended** properties increase the chance of the feature being shown [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).
- **Fewer recommended properties, complete and accurate,** are better than many incomplete or wrong ones [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).
- Google may make general use of `sameAs` and other undocumented schema.org data, including for future features [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).

### Visible content and quality guidelines
- Markup describes **the page it is on**: no empty pages created only to carry structured data, no markup of information **not visible** to users, even if true [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).
- Quality guidelines (not testable by tools; violating them can block rich results or get the markup flagged as spam) [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies):
  - follow the spam policies; keep information **up to date**; content must be **original** (yours or your users');
  - no irrelevant or misleading content (e.g. **fake reviews**); no impersonation of people or organisations and no misrepresentation of ownership, affiliation or purpose;
  - **relevance**: the markup faithfully represents the page (examples of errors: a sports live stream marked up as a local event; woodworking instructions marked up as a recipe);
  - **location**: markup on the page it describes; with duplicate pages, **the same markup on all of them**, not only on the canonical;
  - **specificity**: use the **most specific** applicable schema.org type and properties;
  - **images**: relevant to the page, crawlable and indexable URLs.
- Several items on one page: either **nest** them (one main item with the others inside) or declare them **separately** (JSON-LD array). Always include the **main type** that reflects the purpose of the page; if you mark up several reviews, mark up **all** the visible ones [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).
- Access: do not block pages carrying markup with robots.txt, `noindex` or a login [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).

### Manual actions
- A structured data problem can lead to a **manual action**: the page loses rich result eligibility, **but its ranking does not change**; the page's markup is **ignored** [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).
- Check the Manual actions report in Search Console; after fixing, request reconsideration [G](https://support.google.com/webmasters/answer/9044175).
- The Rich Results Test **does not detect** spam or policy problems (only syntax and fields) [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).

### JavaScript-generated markup
- Methods: Google Tag Manager, custom JavaScript, server-side rendering [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
- Google processes the structured data **present in the DOM at render time** [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
- With GTM, use **variables that read the page** instead of copying the data into the tag (duplication creates mismatches) [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
- `Product`: JS-generated markup can make Shopping crawls **less frequent and less reliable**; Google recommends `Product` in the **initial HTML** [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing). Details in [JavaScript and SPA notes](#javascript-and-spa-notes).

### Testing and validation
| Tool | When | Notes |
|---|---|---|
| Rich Results Test (`search.google.com/test/rich-results`) | Development and verification | Use **URL input** (code input has JS limits, e.g. CORS). It does not support site names or retired types [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). |
| Schema Markup Validator (`validator.schema.org`) | Syntax of types the Rich Results Test does not cover (e.g. `WebSite` for the site name) | Google points to it for site names [G](https://developers.google.com/search/docs/appearance/site-names). |
| URL Inspection (Search Console) | After deploy | Checks the rendered HTML and robots/`noindex`/login blocks; request recrawl (takes days) [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing). |
| Rich result status reports, "Unparsable structured data", Manual actions | After deploy and after every new template | A rise in errors = broken template; **a drop in valid items without a rise in invalid ones** = markup no longer embedded [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing). |
| Performance report (search appearance / URL filter) | Measuring the effect | Before/after test on stable pages over a few months [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). |

- "Critical" errors in the test must be fixed; "non-critical" ones improve quality but are not needed for eligibility [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). A sitemap is recommended to signal changes [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).

### @id and the graph
- Google: if separate items are related (e.g. a recipe and a video), use **`@id`** to link them, otherwise Google may not understand the relationship [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data). The `ProfilePage` example uses `"@id": "#main-author"` to link the author to their articles [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page). In `BreadcrumbList`, `item` can be an object with `@id` [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb).
- On the home page, **a single `WebSite` node**: nest its properties there (site name included) instead of creating several blocks [G](https://developers.google.com/search/docs/appearance/site-names) (also said in Google Search Office Hours, 2022).
- *(inference)* Recommended convention: **absolute, stable** `@id`s per entity, reused across the site: `https://acme-widgets.example/#website`, `https://acme-widgets.example/#organization`, `https://adanovak.example/about#person`. Other pages reference the entity (`"author": {"@id": "https://adanovak.example/about#person"}`) instead of redefining it with different data. Full rules in [Build rules](#build-rules).
- *(inference)* A JSON-LD array (documented by Google) and `@graph` (standard JSON-LD syntax, not mentioned in the documentation read) are equivalent; choose one style per site and never create duplicate entities with different `@id`s for the same thing.

### Choice matrix by site type
Archetypes match `knowledge/archetypes.md`. "Rich result" = a visible Search feature exists for this markup according to Google's documentation as read on 2026-10-03; the notes say where it is limited by region, language or programme.

| Site / page | Recommended types | Rich result (Yes / No / Limited) | Availability notes |
|---|---|---|---|
| Any site – home | `WebSite` (`name`, `url`, `alternateName`) + `Organization` (or subtype) if there is a brand or company | Yes | Site name: all languages, domain or subdomain level only [G](https://developers.google.com/search/docs/appearance/site-names); logo in results / knowledge panel possible, not guaranteed [G](https://developers.google.com/search/docs/appearance/structured-data/organization) |
| personal-brand – About page | `ProfilePage` with `mainEntity` `Person` (`sameAs`, `image`, `description`) | No | No dedicated rich result; helps entity understanding and author linking [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) *(inference)* |
| personal-brand / editorial – articles | `BlogPosting` / `Article` / `NewsArticle` with `author` → the person's `@id` + `BreadcrumbList` | Yes | Article: no regional limits stated (better title, image, date) [G](https://developers.google.com/search/docs/appearance/structured-data/article); breadcrumbs shown on desktop only since 23 January 2025, all regions and languages [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) |
| professional-services without premises open to the public | `Organization` (or `Person` via `ProfilePage`) with `contactPoint`; `LocalBusiness` only if a real address is shown *(inference)* | Limited | Logo / knowledge panel possible; **no stars** from own reviews (SD-16) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| local-business (one or more locations) | Specific `LocalBusiness` subtype, **one per location**, on the contact/location page or home | Yes | Details in the knowledge panel; the Google Business Profile remains the main source [G](https://developers.google.com/search/docs/appearance/structured-data/local-business); **no stars** for self-reviews; restaurant carousel limited access; beta carousels only in EEA, Türkiye, South Africa for aggregators via interest form [G](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta) |
| ecommerce – product page | `Product` + `Offer` (or `ProductGroup` for variants), `BreadcrumbList`, `Review` / `AggregateRating` from real users | Yes | Product snippets and merchant listings [G](https://developers.google.com/search/docs/appearance/structured-data/product); pros and cons in Dutch, English, French, German, Italian, Japanese, Polish, Portuguese, Spanish, Turkish [G](https://developers.google.com/search/docs/appearance/structured-data/product-snippet); loyalty programmes (member prices) only in AU, BR, CA, FR, DE, MX, UK, US [G](https://developers.google.com/search/docs/appearance/structured-data/loyalty-program) |
| ecommerce – About / policies page | `OnlineStore` with `hasMerchantReturnPolicy`, `hasShippingService` | Yes | Merchant listings; Merchant Center / Search Console settings **take precedence** over markup [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) |
| Review site (third-party reviews) | `Review` / `AggregateRating` nested in the reviewed type (`Product`, someone else's `LocalBusiness`, `Book`…) | Yes | No regional limits stated [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| saas-product / app | `SoftwareApplication` (`WebApplication` / `MobileApplication`) + `Organization` | Limited | **Only with real ratings or reviews** (required) [G](https://developers.google.com/search/docs/appearance/structured-data/software-app) |
| Event page | `Event` (one page per event) | Limited | Event experience only in Australia (en), Brazil (pt), Canada (en), Germany (de), India (en), Latin America (es), Spain (es), United Kingdom (en), United States (en) [G](https://developers.google.com/search/docs/appearance/structured-data/event) |
| Courses / training | `Course` + `ItemList` (≥ 3 courses) | Limited | Course list in English only, all regions; "Course info" was retired in 2025 [G](https://developers.google.com/search/docs/appearance/structured-data/course) |
| Page with a hosted video | `VideoObject` (+ `Clip` / `SeekToAction`, `BroadcastEvent` for live streams) | Yes | Video results, key moments; `SeekToAction` in 12 languages (English, Spanish, Portuguese, Italian, Chinese, French, Japanese, German, Turkish, Korean, Dutch, Russian) [G](https://developers.google.com/search/docs/appearance/structured-data/video) |
| Job postings (employer or job board) | `JobPosting` on the single-job page | Limited | Job search experience only in listed countries (much of Europe, Asia, Latin America, MENA, sub-Saharan Africa…); check the list [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting) |
| Recipes | `Recipe` (+ `ItemList` for a carousel) | Yes | No regional limits stated [G](https://developers.google.com/search/docs/appearance/structured-data/recipe) |
| Forum / community | `DiscussionForumPosting` or `QAPage` (one question) + user `ProfilePage` | Yes | [G](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum) [G](https://developers.google.com/search/docs/appearance/structured-data/qapage) |
| Original photos / illustrations | `ImageObject` with `license`, `acquireLicensePage`, `creator` | Yes | "Licensable" badge in Google Images [G](https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata) |
| Paywalled content | `isAccessibleForFree: false` + `hasPart` with `cssSelector` | No | Not a rich result: it tells the paywall apart from cloaking [G](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content) |
| FAQ page / "how to" guide | No markup for a rich result (`FAQPage`, `HowTo` retired); `QAPage` must **not** be used for FAQs written by the site | No | See [Retired or restricted rich results](#retired-or-restricted-rich-results) |

### WebSite (site name)
- **Availability**: all languages, mobile and desktop; sites at **domain or subdomain** level (`www` and `m` count as the domain); **subdirectories are not supported** [G](https://developers.google.com/search/docs/appearance/site-names).
- **Where**: only on the **home page** (root URI; `example.com/en/index.html` is not the home page). On every duplicate home page (http/https, www/non-www) [G](https://developers.google.com/search/docs/appearance/site-names); the variants should redirect to one host anyway (CI-17). A subdomain without markup may inherit the domain's name [G](https://developers.google.com/search/docs/appearance/site-names).
- **Required**: `name`, `url` (canonical home, e.g. `https://acme-widgets.example/`). **Recommended**: `alternateName` (an array is allowed, in order of preference, most important first) [G](https://developers.google.com/search/docs/appearance/site-names).
- **Choosing the name** [G](https://developers.google.com/search/docs/appearance/site-names): unique, not misleading, concise and commonly recognised ("Google", not "Google LLC"); no character limit but it may be truncated; avoid generic names ("Best dentists in X"); **consistent** with `<title>`, `og:site_name` and the home page headings; `Organization.name` equal to the site name.
- **If the name is not picked up** [G](https://developers.google.com/search/docs/appearance/site-names): check errors and consistency; add `alternateName`; add the **lowercase domain** as the last `alternateName`; as a last resort use the lowercase domain as `name`. Timing: days to weeks.
- **Testing**: Schema Markup Validator (the Rich Results Test does not support site names) + URL Inspection [G](https://developers.google.com/search/docs/appearance/site-names).
- **Common errors**: `WebSite` on inner pages or subfolders; two `WebSite` nodes on the home page; removing `WebSite` in the belief that it only served the sitelinks search box (retired in 2024: the node is still used for the site name) [G](https://developers.google.com/search/blog/2024/10/sitelinks-search-box).
- **Favicon** (attribution, not structured data) [G](https://developers.google.com/search/docs/appearance/favicon-in-search): `<link rel="icon" href="...">` in the **home page** `<head>`; one per hostname; square, **minimum 8x8 px, recommended > 48x48 px**; formats BMP, GIF, ICO, PNG, JPEG, PPM, TIFF (SVG not listed); stable URL; file and home page not blocked to Googlebot / Googlebot-Image.
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://acme-widgets.example/#website",
  "name": "Acme Widgets",
  "alternateName": ["Acme", "acme-widgets.example"],
  "url": "https://acme-widgets.example/",
  "publisher": { "@id": "https://acme-widgets.example/#organization" }
}
```
(`publisher` and `@id` are *(inference)*: graph links, not required by Google.)

### Organization
- **Availability**: no limitation stated. Influences the logo in results and in the knowledge panel; for merchants also the merchant knowledge panel and brand profile [G](https://developers.google.com/search/docs/appearance/structured-data/organization).
- **Where**: the **home page** or a **single page** describing the organisation (About); **not needed on every page** [G](https://developers.google.com/search/docs/appearance/structured-data/organization).
- **Required: none**. Focus on `name` / `alternateName`, physical presence (`address`, `telephone`), online presence (`url`, `logo`) [G](https://developers.google.com/search/docs/appearance/structured-data/organization).
- **Recommended (exact names)** [G](https://developers.google.com/search/docs/appearance/structured-data/organization): `address` (`PostalAddress`, multiple allowed: `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` ISO 3166-1 alpha-2), `alternateName`, `contactPoint` (`telephone`, `email`), `description`, `duns`, `email`, `foundingDate` (ISO 8601), `globalLocationNumber`, `hasMerchantReturnPolicy`, `hasMemberProgram`, `hasShippingService`, `iso6523Code` (`ICD:identifier`, e.g. `0060:` DUNS, `0088:` GLN, `0199:` LEI), `legalName`, `leiCode`, `logo`, `naics`, `name`, `numberOfEmployees` (`QuantitativeValue`), `sameAs`, `taxID` (consistent with the country in `address`), `telephone` (with international prefix), `url`, `vatID` (VAT number, if applicable: "an important trust signal for users", who can look it up in public VAT registries).
- **Constraints**: `logo` **≥ 112x112 px**, crawlable, in a format supported by Google Images, legible on a **white background**; with `ImageObject`, `contentUrl` or `url` is needed [G](https://developers.google.com/search/docs/appearance/structured-data/organization).
- **Subtype**: the most specific one (e.g. `OnlineStore` rather than `OnlineBusiness`); for physical premises use `LocalBusiness` and its requirements [G](https://developers.google.com/search/docs/appearance/structured-data/organization).
- **Common errors**: `name` different from the site name; `sameAs` pointing to profiles the entity does not own (impersonation); white or transparent logo that is illegible; `Organization` repeated on every page with different data [G](https://developers.google.com/search/docs/appearance/structured-data/organization) *(inference)*.
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://studioferri.example/#organization",
  "name": "Studio Ferri Orientamento",
  "url": "https://studioferri.example/",
  "logo": "https://studioferri.example/img/logo-512.png",
  "email": "info@studioferri.example",
  "telephone": "+39-051-0000000",
  "vatID": "IT00000000000",
  "sameAs": ["https://social.example/studioferri", "https://directory.example/studioferri"]
}
```

### LocalBusiness (and subtypes)
- **Availability**: no limitation stated for the knowledge panel; restaurant carousel with **limited access**; bookings and orders from results go through the Maps Booking API, not markup [G](https://developers.google.com/search/docs/appearance/structured-data/local-business). Beta carousels (`ItemList` + `LocalBusiness`) only in the EEA, Türkiye and South Africa, for summary pages with ≥ 3 entities and an interest form [G](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta).
- **Where**: any page, preferably the one with the business information; **one entity per location** [G](https://developers.google.com/search/docs/appearance/structured-data/local-business).
- **Type**: the **most specific** subtype (`Restaurant`, `Dentist`, `HealthClub`, `LegalService`, `Physiotherapy`…); several categories → array in `@type` (e.g. `["Electrician","Plumber"]`); **`additionalType` is not supported** [G](https://developers.google.com/search/docs/appearance/structured-data/local-business). It is a subtype of `Organization`: the Organization fields apply too [G](https://developers.google.com/search/docs/appearance/structured-data/local-business).
- **Required**: `name`, `address` (`PostalAddress`, as complete as possible) [G](https://developers.google.com/search/docs/appearance/structured-data/local-business).
- **Recommended**: `aggregateRating` and `review` (**only** if the site collects reviews about **other** businesses), `department`, `geo` (`latitude` / `longitude` with **≥ 5 decimals**), `menu`, `openingHoursSpecification` (`dayOfWeek`, `opens`, `closes`, `validFrom`, `validThrough`), `priceRange`, `servesCuisine`, `telephone` (country prefix), `url` (URL of the **specific location**, working) [G](https://developers.google.com/search/docs/appearance/structured-data/local-business). Main email and phone at `LocalBusiness` level, then `contactPoint` for additional channels [G](https://developers.google.com/search/docs/appearance/structured-data/local-business).
- **Constraints** [G](https://developers.google.com/search/docs/appearance/structured-data/local-business): `priceRange` **< 100 characters** (≥ 100 is not shown); times `hh:mm:ss` (Google's examples use `"09:00"`); days `https://schema.org/Monday` or the short form `Monday`; open 24 hours = `00:00`–`23:59`; closed all day = `00:00`–`00:00`; past midnight = a single object (e.g. 18:00–03:00); seasonal closures with `validFrom` / `validThrough` (YYYY-MM-DD). Departments: name in the format "{store} {department}".
- **Common errors**: stars on the business's own reviews (also via an embedded Google/Facebook widget) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet); `additionalType`; approximate coordinates; phone without prefix; address or hours different from the Business Profile or the page *(inference)*; a single entity for several locations.
- *(inference)* Business without a public address (home visits / online service): `address` is required for this type → use `Organization`, or `LocalBusiness` only with a real address shown on the page. `areaServed` is valid schema.org but not documented by Google.
- ⚠ *(inference)* `ProfessionalService` is often recommended by third parties [SEJ], but schema.org states that this general type for local businesses "was deprecated due to confusion with Service" ([schema.org](https://schema.org/ProfessionalService), checked 2026-10-11): prefer a specific subtype or `LocalBusiness`.
```json
{
  "@context": "https://schema.org",
  "@type": "Physiotherapy",
  "@id": "https://northwind-physio.example/locations/oslo#localbusiness",
  "name": "Northwind Physio",
  "url": "https://northwind-physio.example/locations/oslo",
  "telephone": "+47-00-00-00-00",
  "image": "https://northwind-physio.example/img/oslo-clinic-1200x900.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Example Street 1",
    "addressLocality": "Oslo",
    "postalCode": "0150",
    "addressCountry": "NO"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 59.91000, "longitude": 10.75000 },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00", "closes": "17:00"
  }]
}
```

### Person / ProfilePage
- **Availability**: no limitation stated. It produces no dedicated rich result: it helps Google understand creators (e.g. "Discussions and forums") and is the target of `author.url` in Article, Recipe, forums, QAPage [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page). The Search "profile" (badge on `profile.google.com`) is a different thing and is not obtained through markup [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
- **Valid cases**: user profile on a forum or social site, author page on a news site, **"About me" page of a blog**, employee page on a company site. **Not valid**: a shop's home page (too much non-profile information), a page of reviews about an unaffiliated organisation [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page). The main entity must be **a single person or organisation affiliated with the site** [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
- **ProfilePage – required**: `mainEntity` (`Person` or `Organization`; if unknown, `Person`). **Recommended**: `dateCreated`, `dateModified` (ISO 8601; only human edits to the metadata) [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
- **Person / Organization – required**: `name` (or `alternateName` if missing). **Recommended**: `agentInteractionStatistic`, `alternateName` (handle), `description` (author line / qualifications), `identifier` (stable internal ID), `image`, `interactionStatistic`, `sameAs` [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
- **Constraints**: a real `image` (never a placeholder or icon), ≥ 50,000 px, 16x9 / 4x3 / 1x1 recommended; `interactionStatistic` **only** with data from the platform hosting the profile (not followers on other networks) [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page). Recent activity: `hasPart` with `Article` items pointing to the author via `@id` [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
- *(inference)* A `Person` without `ProfilePage` (e.g. on the home page) is allowed but enables no documented feature; for a personal brand put `ProfilePage` on the About page and reuse its `@id` as `author` everywhere. `jobTitle` and `honorificPrefix` are properties Google mentions for authors [G](https://developers.google.com/search/docs/appearance/structured-data/article).
```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "dateModified": "2026-01-15T10:00:00+01:00",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://adanovak.example/about#person",
    "name": "Ada Novak",
    "jobTitle": "Software developer",
    "description": "Short bio with verifiable qualifications.",
    "image": "https://adanovak.example/img/ada-novak-800x800.jpg",
    "sameAs": ["https://code.example/adanovak", "https://social.example/adanovak"]
  }
}
```

### Article / BlogPosting / NewsArticle
- **Availability**: no limitation stated; improves title, images and date in Search, Google News, Assistant. Not required for Google News features [G](https://developers.google.com/search/docs/appearance/structured-data/article).
- **Required: none**. **Recommended**: `author` (`Person` / `Organization`), `author.name`, `author.url` (page identifying the author; if internal, mark it up as `ProfilePage`; alternatively `sameAs`), `dateModified`, `datePublished` (ISO 8601 **with time zone**, otherwise Googlebot's time zone is assumed), `headline` (concise), `image` [G](https://developers.google.com/search/docs/appearance/structured-data/article).
- **Images**: relevant, **not logos or captions**, ≥ 50,000 px (width × height), ideally 16x9, 4x3, 1x1 [G](https://developers.google.com/search/docs/appearance/structured-data/article).
- **Author best practices** [G](https://developers.google.com/search/docs/appearance/structured-data/article): every visible author in the markup; **one object per author** (never "Name A, Name B" in a single `name`); `name` contains only the name (publisher in `publisher`, role in `jobTitle`, titles in `honorificPrefix` / `honorificSuffix`, no "by" / "posted by"); `Person` for people, `Organization` for bodies, **never `Thing`**.
- **Technical**: multi-part articles → canonical to each page or to a view-all page (not to the first page); subscription content → paywall markup [G](https://developers.google.com/search/docs/appearance/structured-data/article).
- **Dates** [G](https://developers.google.com/search/docs/appearance/publication-dates): a visible, labelled date ("Published", "Updated") consistent with the markup; no future dates.
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Concise article title",
  "image": ["https://adanovak.example/img/post-1x1.jpg", "https://adanovak.example/img/post-4x3.jpg", "https://adanovak.example/img/post-16x9.jpg"],
  "datePublished": "2026-03-10T09:00:00+01:00",
  "dateModified": "2026-04-02T14:30:00+02:00",
  "author": [{ "@type": "Person", "@id": "https://adanovak.example/about#person", "name": "Ada Novak", "url": "https://adanovak.example/about" }],
  "publisher": { "@id": "https://adanovak.example/about#person" }
}
```
(For a personal brand the publisher is the person; for a company blog use `{"@id": "https://<host>/#organization"}`.)

### BreadcrumbList
- **Availability**: **desktop only** since 23 January 2025 (on mobile the visible URL shows only the domain); all regions and languages; markup still supported, report and test still active [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) [G](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs).
- **Structure**: `BreadcrumbList` with **at least 2 `ListItem`s**; several trails allowed (array of `BreadcrumbList`) [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb).
- **Required**: `itemListElement`; for each `ListItem`: `position` (integer, 1 = start), `name`, `item` (URL or object with `@id`) — `item` is **not needed for the last element** (Google uses the page URL) [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb).
- **Guidelines**: a **typical** user path, not a copy of the URL structure; no element needed for the root (domain) or the page itself [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb). *(inference)* It must match a breadcrumb visible on the page (visible-content rule).
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Services", "item": "https://northwind-physio.example/services/" },
    { "@type": "ListItem", "position": 2, "name": "Sports physiotherapy" }
  ]
}
```

### Review / AggregateRating
- **Availability**: no limitation stated; stars in rich results or knowledge panels [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **Reviewable types** (`itemReviewed`): `Book`, `Course`, `CreativeWorkSeason`, `CreativeWorkSeries`, `Episode`, `Event`, `Game`, `HowTo`, `LocalBusiness`, `MediaObject`, `Movie`, `MusicPlaylist`, `MusicRecording`, `Organization`, `Product`, `Recipe`, `SoftwareApplication` [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) (some correspond to retired features, e.g. `HowTo`: see [Retired or restricted rich results](#retired-or-restricted-rich-results)).
- **Review – required**: `author` (valid name, **< 100 characters**), `itemReviewed` (if not nested) + `itemReviewed.name` (or the parent's `name`), `reviewRating`, `reviewRating.ratingValue`. **Recommended**: `datePublished`, `reviewRating.bestRating` (default 5), `reviewRating.worstRating` (default 1) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **AggregateRating – required**: `itemReviewed` (if not nested) + name, `ratingValue`, **`ratingCount` or `reviewCount`**. **Recommended**: `bestRating`, `worstRating` [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **Constraints** [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet): value as number, fraction or percentage (`4`, `6 / 10`, `60%`); default scale 1–5; **decimal point** (`4.4`, not `4,4`); a review is about a **specific item**, not a category or list; with several individual reviews include the aggregate too; review text and rating **visible** on the page.
- **Prohibited** [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet): aggregating reviews **from other sites**; fake reviews or **undisclosed incentivised** ones; for `LocalBusiness` / `Organization`: if the entity **controls the reviews about itself** (on its own site, in markup or through **embedded widgets** from Google/Facebook) its pages are **not eligible** for stars; ratings must come directly from users, not editors. Reviews not from real users → possible manual action.
- *(inference)* Client testimonials on a professional's or company's site: do **not** mark them up as `Review` / `AggregateRating` of the business itself (SD-16).
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "Physiotherapy",
    "name": "Northwind Physio",
    "address": { "@type": "PostalAddress", "streetAddress": "Example Street 1", "addressLocality": "Oslo", "addressCountry": "NO" }
  },
  "author": { "@type": "Person", "name": "Kari N." },
  "datePublished": "2026-05-20",
  "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": 5 }
}
```
(Valid on a **third-party** review site or directory reviewing Northwind Physio; not valid on northwind-physio.example itself.)

### Event
- **Availability**: event experience in Australia (English), Brazil (Portuguese), Canada (English), Germany (German), India (English), Latin America (Spanish), Spain (Spanish), United Kingdom (English), United States (English). Other countries and languages are not listed [G](https://developers.google.com/search/docs/appearance/structured-data/event).
- **Guidelines** [G](https://developers.google.com/search/docs/appearance/structured-data/event): **one page with a unique URL per event** (no calendars or lists); event **at a physical venue** (virtual-only experiences not supported), bookable by the general public; school events with minors excluded; do not mark up promotions, opening hours, coupons, travel packages.
- **Required**: `name` (title of the event, not the venue, without prices or promotions), `startDate` (ISO 8601 with offset), `location` (`Place`) with `location.address` (complete `PostalAddress`) [G](https://developers.google.com/search/docs/appearance/structured-data/event).
- **Recommended**: `description`, `endDate`, `eventStatus` (`EventScheduled`, `EventCancelled`, `EventPostponed`, `EventRescheduled`; never drop `startDate` / `location` when changing status), `image` (recommended width 1920 px, min 720 px; ≥ 50,000 px), `location.name`, `offers` (`availability` `InStock` / `SoldOut` / `PreOrder`, lowest `price` including fees, `0` if free, `priceCurrency`, `validFrom`, `url`), `organizer` (`name`, `url`), `performer` (`name`), `previousStartDate` (only with `EventRescheduled`) [G](https://developers.google.com/search/docs/appearance/structured-data/event).
- **Common errors**: `T00:00:00` or `T23:59:59+00:00` used as "all day" (Google treats them as real times: for a whole day use the date only); dates without time zone; venue name in `name` [G](https://developers.google.com/search/docs/appearance/structured-data/event).
```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Running injury prevention workshop",
  "startDate": "2026-11-14T18:30:00+01:00",
  "endDate": "2026-11-14T21:00:00+01:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "Place",
    "name": "Northwind Physio Oslo",
    "address": { "@type": "PostalAddress", "streetAddress": "Example Street 1", "addressLocality": "Oslo", "postalCode": "0150", "addressCountry": "NO" }
  },
  "offers": { "@type": "Offer", "price": 0, "priceCurrency": "NOK", "availability": "https://schema.org/InStock", "url": "https://northwind-physio.example/events/running-workshop" }
}
```
(Norway is not among the listed markets: the markup is valid but produces no event experience there — SD-07.)

### Course
- **Status**: "**Course info**" was phased out from June 2025 and its documentation was removed (and dropped from reports and the test) on 9 September 2025 [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) [G](https://developers.google.com/search/updates). The "**course list**" result (carousel) is still documented, **in English only**, in all regions where Search is available [G](https://developers.google.com/search/docs/appearance/structured-data/course).
- **Guidelines (course list)** [G](https://developers.google.com/search/docs/appearance/structured-data/course): `Course` only for a **series or unit of learning** with instructors and students (not a single event or a 2-minute video); **at least 3 courses** marked up; **`ItemList` carousel markup required** on a summary page or an all-in-one page; valid `name` and `provider` (no promotions, prices or discounts in the name).
- **Required**: `name`, `description` (displayed up to **60 characters**); `ItemList` with `itemListElement`, `ListItem.position`, `ListItem.url` (unique canonical URL). `provider` (`Organization`) is "recommended" in the table but "must" be valid according to the guidelines → always include it [G](https://developers.google.com/search/docs/appearance/structured-data/course).
- *(inference)* For sites not in English: no rich result; the markup is optional and must not be promised as a visibility lever.
```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Metodo di studio per l'università",
  "description": "Short description, within 60 characters.",
  "provider": { "@type": "Organization", "name": "Studio Ferri Orientamento", "sameAs": "https://studioferri.example/" }
}
```
(Studio Ferri's site is in Italian: valid markup, no course list result.)

### VideoObject
- **Availability**: main results, Video mode, Google Images, Discover; key moments with `Clip` (all languages) or `SeekToAction` (12 languages: English, Spanish, Portuguese, Italian, Chinese, French, Japanese, German, Turkish, Korean, Dutch, Russian); LIVE badge with `BroadcastEvent` [G](https://developers.google.com/search/docs/appearance/structured-data/video).
- **Where**: on the **watch page** (where the video is played) [G](https://developers.google.com/search/docs/appearance/structured-data/video).
- **Required**: `name` (unique per video), `thumbnailUrl`, `uploadDate` (ISO 8601, time zone recommended) [G](https://developers.google.com/search/docs/appearance/structured-data/video).
- **Recommended**: `contentUrl` (video file, the most effective method), `embedUrl` (player), `description`, `duration` (ISO 8601, e.g. `PT2M30S`), `expires`, `hasPart` (`Clip`: `name`, `startOffset`, `url`, recommended `endOffset`), `interactionStatistic`, `regionsAllowed` / `ineligibleRegion`, `publication` (`BroadcastEvent` with `isLiveBroadcast`, `startDate`, `endDate`), `creator` / `author` [G](https://developers.google.com/search/docs/appearance/structured-data/video).
- **Constraints**: `Clip` / `SeekToAction` require videos ≥ **30 seconds** and timestamped deep links (e.g. `?t=30`); two clips cannot start at the same point; disable key moments with `nosnippet` [G](https://developers.google.com/search/docs/appearance/structured-data/video). Live streams: Indexing API at start and end [G](https://developers.google.com/search/docs/appearance/structured-data/video).
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to mount the Acme wall widget",
  "description": "Unique description of this video.",
  "thumbnailUrl": "https://acme-widgets.example/video/wall-widget-1280x720.jpg",
  "uploadDate": "2026-02-05T08:00:00+01:00",
  "duration": "PT4M12S",
  "contentUrl": "https://acme-widgets.example/video/wall-widget.mp4",
  "embedUrl": "https://acme-widgets.example/player?video=123"
}
```

### Product, Offer, ProductGroup and merchant listings
`ecommerce.md` references this section and its checks (SD-22, SD-24, SD-26) instead of duplicating them.

**Two families** [G](https://developers.google.com/search/docs/appearance/structured-data/product)
- **Product snippets**: pages where people **cannot buy directly** (editorial reviews, comparison pages); more options for review information, such as pros and cons.
- **Merchant listings**: pages where customers **buy from you**; more options for product detail (apparel sizing, shipping, return policy).
- They overlap: the required merchant-listing properties also make the page eligible for product snippets. Each experience decides what to show. Providing **both markup and a Merchant Center feed** maximises eligibility; product snippets may use feed pricing when the page lacks it [G](https://developers.google.com/search/docs/appearance/structured-data/product).

**Page rules** [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- Merchant listings: only pages where a shopper can buy the product; pages that only link to other sellers are not eligible.
- Each page focuses on **one product or variants of the same product**; never category or list pages. Variants need distinct URLs (see ProductGroup below). One URL per currency [G](https://developers.google.com/search/docs/appearance/structured-data/product-snippet).
- Put `Product` in the **initial HTML**: JS-generated markup can make Shopping crawls less frequent and less reliable.
- Do not mark up prohibited or regulated goods (e.g. firearms, recreational drugs, tobacco and vaping products, gambling products).
- `Car` is not automatically a `Product`: declare both types to attach ratings.

**Product snippet – properties** [G](https://developers.google.com/search/docs/appearance/structured-data/product-snippet)
- Required: `name` + **at least one of** `review`, `aggregateRating`, `offers`. Reviews must name a valid `Person` or `Team` as reviewer.
- `Offer`: `price` (or `priceSpecification.price`) required; `priceCurrency`, `availability`, `priceValidUntil` recommended. Use `Offer`, not `AggregateOffer`, to qualify for the price-drop enhancement.
- `AggregateOffer` (`lowPrice`, `priceCurrency` required; `highPrice`, `offerCount` recommended): only for a product sold by **several merchants**, never for variants.
- **Pros and cons**: only on **editorial** product review pages (not merchant pages, not customer reviews); `positiveNotes` and/or `negativeNotes` on the nested `Review`, **at least two statements** in total, each a `ListItem` with `name` (optional `position`). Available in Dutch, English, French, German, Italian, Japanese, Polish, Portuguese, Spanish and Turkish, in all countries where Search is available.

**Merchant listing – required** [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- `Product`: `name`, `image`, `offers`.
- `Offer` (not `AggregateOffer`): a price (`price` or `priceSpecification.price`) **> 0** and a currency (`priceCurrency` or `priceSpecification.priceCurrency`) in ISO 4217. Product snippets do not have the > 0 rule.

**Merchant listing – recommended** [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- `Product`: `aggregateRating`, `review`, `audience`, `brand.name` (at most one brand), `category`, `color`, `description`, `material`, `mpn`, `pattern`, `size`, `sku` (one value, no whitespace), global identifiers `gtin` / `gtin8` / `gtin12` / `gtin13` / `gtin14` / `isbn` (most specific GTIN, numeric form), `hasCertification` (up to 10), `hasAdultConsideration`, `inProductGroupWithID`, `isVariantOf`, `subjectOf` (a 3D model, one value).
- `Offer`: `availability` (one of `BackOrder`, `Discontinued`, `InStock`, `InStoreOnly`, `LimitedAvailability`, `OnlineOnly`, `OutOfStock`, `PreOrder`, `PreSale`, `SoldOut`; one value only), `itemCondition` (`NewCondition`, `RefurbishedCondition`, `UsedCondition`; one value), `priceValidUntil` (a past date may stop the listing from showing), `validFrom` / `validThrough` (sale period, ISO 8601), `url` (one URL), `shippingDetails`, `hasMerchantReturnPolicy`.
- **Images**: crawlable and indexable, matching the marked-up product, in a format supported by Google Images; several high-resolution images (≥ 50,000 px) in 16x9, 4x3 and 1x1 recommended.
- *(inference)* **Availability in practice**: mark the real stock state and keep it identical to the visible page (SD-03). A product temporarily out of stock keeps its page and markup with `OutOfStock` (or `BackOrder` / `PreOrder` when orders are accepted); Google does not state how `OutOfStock` affects display. Permanently removed products are a crawling question (status codes, redirects: `crawling-indexing.md`).

**Prices** [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- Active price in `price` or in `priceSpecification`; if both are present `offers.price` is used.
- Strikethrough (was) price: a `UnitPriceSpecification` with `priceType` `https://schema.org/StrikethroughPrice` (`ListPrice` accepted during a transition period); never put `priceType` on the active price.
- Member price: a price specification with `validForMemberTier`, without `priceType` (specifications with both are ignored); `membershipPointsEarned` (beta). Unit pricing: `referenceQuantity` (`QuantitativeValue` with `unitCode` and `value`).

**Shipping** [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) [G](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy)
- Offer level: `shippingDetails` (`OfferShippingDetails`), one per shipping option (e.g. standard, overnight). Required for eligibility: `shippingRate` (`currency` ISO 4217 matching the offer, plus `value` or `maxValue`; `0` = free shipping; one rate per `OfferShippingDetails`), `shippingDestination` (`DefinedRegion` with two-letter `addressCountry`; `addressRegion` supported for US, AU, JP; `postalCode` for AU, CA, US; not both in one region), `deliveryTime` (one per offer shipping details: `handlingTime` and/or `transitTime` as `QuantitativeValue` with non-negative whole `minValue` / `maxValue` days and `unitCode` `DAY` or `d`).
- Organization level: `hasShippingService` (`ShippingService` with `ShippingConditions`) on the `Organization` / `OnlineStore`; Google prefers organization-level policies, and offer-level shipping supports only a subset of properties.

**Return policy** [G](https://developers.google.com/search/docs/appearance/structured-data/return-policy) [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- `MerchantReturnPolicy`, preferably nested in `Organization` via `hasMerchantReturnPolicy`; if both organization-level and product-level policies exist, the **product-level one wins**.
- Required: `applicableCountry` (up to 50 two-letter codes), `returnPolicyCategory` (`MerchantReturnFiniteReturnWindow`, `MerchantReturnNotPermitted`, `MerchantReturnUnlimitedWindow`), `merchantReturnDays` when the window is finite.
- Fees: `returnFees` `FreeReturn`, `ReturnFeesCustomerResponsibility` or `ReturnShippingFees`; only `ReturnShippingFees` takes a non-zero `returnShippingFeesAmount`. Method: `returnMethod` `ReturnAtKiosk`, `ReturnByMail`, `ReturnInStore` (recommended for finite or unlimited windows).

**Precedence of shipping and return information** (strongest first) [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing): (1) product-level feeds in Merchant Center → (2) Content API for Shopping settings → (3) Merchant Center or Search Console settings → (4) product-level markup → (5) organization-level markup. If markup is hard to keep current, configure shipping and returns in Merchant Center or Search Console.

**Variants** [G](https://developers.google.com/search/docs/appearance/structured-data/product-variants): `ProductGroup` (`productGroupID`, `variesBy`, `hasVariant`) with variant `Product`s linked by `inProductGroupWithID` / `isVariantOf`. Supported by both product snippets and merchant listings.

**Loyalty programmes** [G](https://developers.google.com/search/docs/appearance/structured-data/loyalty-program): `hasMemberProgram` (`MemberProgram`, `MemberProgramTier`) nested in `Organization`; shown only in Australia, Brazil, Canada, France, Germany, Mexico, the United Kingdom and the United States.
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Acme Wall Widget, oak",
  "image": ["https://acme-widgets.example/img/wall-widget-oak-1x1.jpg", "https://acme-widgets.example/img/wall-widget-oak-16x9.jpg"],
  "sku": "AW-0001-OAK",
  "gtin13": "0000000000000",
  "brand": { "@type": "Brand", "name": "Acme Widgets" },
  "offers": {
    "@type": "Offer",
    "url": "https://acme-widgets.example/products/wall-widget?color=oak",
    "price": 49.90,
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": { "@type": "MonetaryAmount", "value": 0, "currency": "USD" },
      "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "US" },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
        "transitTime": { "@type": "QuantitativeValue", "minValue": 2, "maxValue": 5, "unitCode": "DAY" }
      }
    }
  }
}
```
Organization-level return policy (preferred place), on the home or policies page:
```json
{
  "@context": "https://schema.org",
  "@type": "OnlineStore",
  "@id": "https://acme-widgets.example/#organization",
  "name": "Acme Widgets",
  "url": "https://acme-widgets.example/",
  "hasMerchantReturnPolicy": {
    "@type": "MerchantReturnPolicy",
    "applicableCountry": ["US"],
    "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
    "merchantReturnDays": 30,
    "returnMethod": "https://schema.org/ReturnByMail",
    "returnFees": "https://schema.org/FreeReturn"
  }
}
```

### JobPosting
- **Availability**: the job search experience is available only in listed countries (much of Europe — e.g. Austria, Belgium, France, Germany, Italy, Netherlands, Spain, Switzerland, United Kingdom — plus Asia, Latin America, MENA, sub-Saharan Africa); check the current list [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting).
- **Rules** [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting): only on the **single job page**, never on lists or search results; one `JobPosting` per job; most properties once per page; **"job requests" are prohibited** (a candidate offering their services): never use it to say "I am available"; no fees charged to applicants; no fake, misleading or impersonating postings; a way to apply, no login needed to read the description; complete description (no disguised ads). Expired jobs → `validThrough` in the past, 404/410, or removal of the markup, then notify via the Indexing API (recommended) and ideally update the sitemap.
- **Required**: `datePosted`, `description` (complete HTML, different from the title), `hiringOrganization` ("confidential" allowed for anonymous hiring), `jobLocation` (with `addressCountry`; not needed if 100% remote with `applicantLocationRequirements`), `title` (only the job title: no codes, dates, salaries or company names) [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting).
- **Recommended**: `applicantLocationRequirements`, `baseSalary` (`unitText` `HOUR` / `DAY` / `WEEK` / `MONTH` / `YEAR`; employer-provided, not an estimate; `minValue` / `maxValue` for ranges), `directApply`, `employmentType` (`FULL_TIME`, `PART_TIME`, `CONTRACTOR`, `TEMPORARY`, `INTERN`, `VOLUNTEER`, `PER_DIEM`, `OTHER`), `identifier`, `jobLocationType` (`TELECOMMUTE` only if 100% remote, stated in the description, with at least one eligible country), `validThrough` (omit if no expiry) [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting). Salary in the markup → must be visible on the page [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting).
```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "Physiotherapist",
  "description": "<p>Responsibilities, requirements, working hours.</p>",
  "datePosted": "2026-09-01",
  "validThrough": "2026-10-31T23:59:00+01:00",
  "employmentType": "FULL_TIME",
  "hiringOrganization": { "@type": "Organization", "name": "Northwind Physio", "sameAs": "https://northwind-physio.example/" },
  "jobLocation": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Oslo", "addressCountry": "NO" } }
}
```
(Norway was not in Google's country list when checked on 2026-10-11: valid markup, no job experience there.)

### JavaScript and SPA notes
- Google reads dynamically injected JSON-LD and processes the data present in the DOM at render time [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript). The documented options are GTM, custom JS and **server-side rendering** [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
- *(inference)* Prefer SSR / prerendering / SSG that emit JSON-LD in the initial HTML, especially for `Product` (explicit Google guidance), `WebSite`, `Organization`, `LocalBusiness`, `ProfilePage`. Reasons: more reliable Shopping crawls [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing); non-Google bots are not documented to render JavaScript (bot table in `ai-search.md`; RJ-01).
- Verification: Rich Results Test **in URL mode** and URL Inspection (rendered HTML); for types the test does not support, inspect the rendered HTML [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript).
- *(inference)* Client-side router: **one JSON-LD block per route**, replaced or removed on every navigation; never leave the previous view's markup behind or duplicate it.
- *(inference)* If the JSON-LD depends on a `fetch` (as in Google's example), the endpoint must be reachable by Googlebot (not blocked by robots.txt, fast).
- [SEJ] Do not load JSON-LD through GTM behind the cookie banner: if the script fires only after consent, crawlers may not see it.
- Googlebot fetches only the first **2 MB** of each HTML file and of each JS/CSS resource: huge inline serialised state can push the markup past the limit; put metadata and essential structured data early in the document [G](https://developers.google.com/search/blog/2026/03/crawler-blog-post) (RJ-15, RJ-17).
- After a release: a drop in valid items without a rise in invalid ones means the markup is no longer embedded (rendering / SSR regression) [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing).
- General rendering details: `knowledge/rendering-javascript.md`.

## Retired or restricted rich results
This table is the owner for retired and restricted features; `myths-deprecated.md` keeps one-line entries that point here. No retirement affects ranking; retired markup is **harmless but useless** for Google (it does not generate Search Console errors) [G](https://developers.google.com/search/blog/2024/10/sitelinks-search-box) [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results).

| Type / feature | Status | Date | Source | Guidance |
|---|---|---|---|---|
| ⚠ Sitelinks search box (`WebSite` + `potentialAction` / `SearchAction`) | Removed from results worldwide; documentation removed on 29 November 2024 | since 21 November 2024 | [G](https://developers.google.com/search/blog/2024/10/sitelinks-search-box) [G](https://developers.google.com/search/updates) | Do not propose it; `SearchAction` can be removed, but **not** the `WebSite` node (site name, SD-10) |
| Breadcrumbs in mobile results | Not shown on mobile (domain only); still shown on desktop | since 23 January 2025 | [G](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs) | `BreadcrumbList` remains valid for desktop |
| ⚠ `FAQPage` (FAQ rich result) | Limited to well-known government and health sites from August 2023; Google announced on 8 May 2026 that it would no longer appear from 7 May 2026, and removed the documentation on 15 June 2026. SEJ reported that the report and Rich Results Test support were removed in June 2026 and that Search Console API support ended in August 2026 *(re-verify)* | 2023 → 2026 | [G](https://developers.google.com/search/updates#removing-faq-rich-result) [G](https://developers.google.com/search/blog/2023/08/howto-faq-changes) [SEJ 2026-05] | Do not recommend for a rich result; `QAPage` is not a substitute |
| ⚠ `HowTo` | Restricted to desktop in August 2023; deprecated on 14 September 2023 (no longer shown on desktop either); search appearance, report and Rich Results Test support dropped 30 days later, Search Console API support 180 days later; absent from the current gallery | 2023 | [G](https://developers.google.com/search/blog/2023/08/howto-faq-changes) [G](https://developers.google.com/search/updates#how-to-deprecation) | Do not recommend |
| ⚠ Course info | Phase-out announced 12 June 2025; documentation removed and dropped from reports, test and filters on 9 September 2025 | 2025-06-12; 2025-09-09 | [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) [G](https://developers.google.com/search/updates) | The "course list" result remains, English only |
| ⚠ `ClaimReview` (fact check) | Phase-out from Google Search announced 12 June 2025; the documentation stays online with a phase-out notice; still used by Fact Check Explorer | 2025-06-12 | [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) [G](https://developers.google.com/search/docs/appearance/structured-data/factcheck) | Only for Fact Check Explorer |
| ⚠ Estimated salary, Learning video, `SpecialAnnouncement`, Vehicle listing | Retired: phase-out announced 12 June 2025 (`SpecialAnnouncement` already announced on 23 April 2025 for 31 July 2025); documentation removed and dropped from reports on 9 September 2025 | 2025-06-12; 2025-09-09 | [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) [G](https://developers.google.com/search/updates) | Do not propose |
| Book actions | Listed in the 12 June 2025 phase-out; on 5 November 2025 Google removed the deprecation banner "as there's still a feature using the markup in Google Search". The documentation is online; the feature is limited to book providers with a wide catalogue, onboarded via an interest form and a partner feed | 2025-06-12 → 2025-11-05 | [G](https://developers.google.com/search/updates) [G](https://developers.google.com/search/docs/appearance/structured-data/book) | Not applicable to ordinary sites; do not propose by default |
| ⚠ Practice problem | Deprecation announced 5 November 2025; documentation removed, no longer shown | 2026-01-06 | [G](https://developers.google.com/search/updates#removing-practice-problems) [SEJ 2025-11] | Do not propose |
| Other "lesser-used" features | Progressive phase-out announced 5 November 2025; support in Search Console and its API removed from January 2026 | 2025-11 → | [G](https://developers.google.com/search/blog/2025/11/update-on-our-efforts) | Check `/search/updates` before proposing marginal types |
| ⚠ `data-vocabulary.org` | No longer eligible for rich results | since 29 January 2021 (announced 2020) | [G](https://developers.google.com/search/updates) | Migrate to schema.org |
| Event | Active but **only in listed markets** (AU, BR, CA, DE, IN, Latin America, ES, UK, US with the listed languages) | — | [G](https://developers.google.com/search/docs/appearance/structured-data/event) | Useful only for the listed markets |
| Course list | Active **in English only** | — | [G](https://developers.google.com/search/docs/appearance/structured-data/course) | No effect on pages in other languages |
| Education Q&A (flashcards) | English, Portuguese, Vietnamese; Spanish only in Mexico | — | [G](https://developers.google.com/search/docs/appearance/structured-data/education-qa) | Only for those languages |
| Speakable (beta) | US only, English | — | [G](https://developers.google.com/search/docs/appearance/structured-data/speakable) | Only for US English news publishers |
| Loyalty programmes (`MemberProgram`) | AU, BR, CA, FR, DE, MX, UK, US | — | [G](https://developers.google.com/search/docs/appearance/structured-data/loyalty-program) | Only in those countries |
| Restaurant carousel; vacation rentals | Limited access (form / Hotel Center) | — | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) [G](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental) | Do not propose by default |
| Beta carousels (`ItemList` + `LocalBusiness` / `Product` / `Event`) | EEA, Türkiye, South Africa; beta, for aggregators, interest form | since 2024 | [G](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta) | Only summary pages with ≥ 3 entities |
| `Dataset` | Used only by Dataset Search (clarified 5 November 2025) | — | [G](https://developers.google.com/search/docs/appearance/structured-data/dataset) [G](https://developers.google.com/search/updates) | Not a Search rich result |

## Audit checks
Severity follows `conventions.md`: **Critical** here means markup that is ineffective, or a manual-action risk, across many pages.

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| SD-01 | Every `application/ld+json` block is valid, parseable JSON | JSON parser on the rendered HTML; "Unparsable structured data" report | Critical | [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) |
| SD-02 | `@context` is `https://schema.org`; no `data-vocabulary.org` | Search the source | High | [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) |
| SD-03 | Every marked-up value is visible on the rendered page (names, prices, availability, hours, reviews, dates, salaries) | Compare JSON-LD ↔ rendered DOM text | Critical | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| SD-04 | Required properties present for every type used | Type sections of this file; Rich Results Test (URL input) | High | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| SD-05 | Correct and most specific type; the page's main type included | Review type vs content (e.g. `Article` only on articles, a specific LocalBusiness subtype) | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| SD-06 | Retired types present (`FAQPage`, `HowTo`, sitelinks `SearchAction`, `ClaimReview`, `SpecialAnnouncement`, Course info…) | Search `@type`; compare with [Retired or restricted rich results](#retired-or-restricted-rich-results). Harmless: report that it has no effect in Search | Low | [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) [G](https://developers.google.com/search/updates) [SEJ 2026-05] |
| SD-07 | (informational) Type not available in the site's market or language (e.g. Event outside the listed countries, course list outside English, Education Q&A, loyalty programmes, Speakable) | Site language/country vs the matrix and the restricted table | Low | [G](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) |
| SD-08 | Pages with markup not blocked by robots.txt, `noindex` or login | URL Inspection; robots.txt; meta robots | High | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| SD-09 | Markup images crawlable, relevant, ≥ 50,000 px; no logos in `Article`; `logo` ≥ 112x112 and legible on white | Fetch the image URLs and measure them | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| SD-10 | `WebSite` on the home page only, with `name` + `url`; a single `WebSite` node; name consistent with `<title>`, `og:site_name`, `Organization.name`; identical `WebSite` markup on every home variant (http/https, www/apex) that still answers 200 | Analyse the home page; Schema Markup Validator; fetch each home variant: any that answers 200 instead of redirecting (CI-17) must carry the same `WebSite` node | High | [G](https://developers.google.com/search/docs/appearance/site-names) |
| SD-11 | Alias of CI-17 — verify there, report once | Fetch the home variants (http/https, www/non-www): one host answers, the others redirect | High | [G](https://developers.google.com/search/docs/appearance/site-names) |
| SD-12 | `WebSite` not placed on subdirectories or inner pages as an alternative "home" | Map the pages carrying `WebSite` | Medium | [G](https://developers.google.com/search/docs/appearance/site-names) |
| SD-13 | `Organization` on the home or About page, specific subtype, data consistent across pages | Compare the Organization nodes across the site | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/organization) *(inference)* |
| SD-14 | `LocalBusiness`: `name` + complete `address`, one entity per location, `telephone` with prefix, `geo` ≥ 5 decimals, `priceRange` < 100 characters, no `additionalType` | Field validation | High | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| SD-15 | `openingHoursSpecification` consistent with the page and the Business Profile; valid day/time formats | Manual or automatic comparison | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) *(inference)* |
| SD-16 | No self-serving reviews: no `Review` / `AggregateRating` on the site's own `Organization` / `LocalBusiness` (in markup or via embedded Google/Facebook review widgets); testimonials are not marked up as reviews | `itemReviewed` / parent node = the entity that owns the site; search for review-widget scripts | High | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| SD-17 | Reviews: not aggregated from other sites, no undisclosed incentives; `ratingValue` with a decimal point; scale consistent with `bestRating` / `worstRating`; `ratingCount` or `reviewCount`; `author.name` < 100 characters | Field validation + review of the source | High | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| SD-18 | `ProfilePage`: `mainEntity` with `name`; page dedicated to a single affiliated person or organisation; `image` not a placeholder; `interactionStatistic` only from the hosting platform | Page review | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| SD-19 | `Article` authors: `@type` `Person` / `Organization` (never `Thing`), one object per author, `name` without roles or titles, valid `url` or `sameAs`, every visible author present | Field validation | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/article) |
| SD-20 | ISO 8601 dates with time zone; `datePublished` / `dateModified` consistent with the visible date; no future dates; no `T00:00:00` as "whole day" in events | Date parsing + comparison with the text | Medium | [G](https://developers.google.com/search/docs/appearance/publication-dates) |
| SD-21 | `BreadcrumbList`: ≥ 2 `ListItem`s, `position` from 1 without gaps, `item` on all but the last, consistent with the visible breadcrumb | Structure validation | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) *(inference)* |
| SD-22 | `Event`, `JobPosting`, `Product` only on leaf pages for a single item (not lists, calendars, categories) | Classify page vs type | High | [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) |
| SD-23 | `JobPosting`: expired jobs removed / `validThrough` in the past; `addressCountry`; `TELECOMMUTE` only when 100% remote; no job requests (self-promotion) | Validation + current date | High | [G](https://developers.google.com/search/docs/appearance/structured-data/job-posting) |
| SD-24 | `Product`: for merchant listings `price` > 0 and ISO 4217 `priceCurrency`, `Offer` not `AggregateOffer`; `priceValidUntil` not in the past; `availability` matches the visible stock state (incl. `OutOfStock`); shipping and return policy consistent with Merchant Center / Search Console settings; `Product` in the initial HTML | Validation + raw HTML (`curl`) + comparison with the visible price/stock and the policies page | High | [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) |
| SD-25 | `VideoObject` on the watch page with `name`, `thumbnailUrl`, `uploadDate`; `contentUrl` or `embedUrl` | Validation | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/video) |
| SD-26 | Enumerations as schema.org URLs or accepted short forms (`availability`, `itemCondition`, `returnPolicyCategory`, `eventStatus`, `dayOfWeek`); ISO codes (country alpha-2, currency 4217) | Value validation | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) |
| SD-27 | `sameAs` points to the entity's official profiles, valid URLs (not random third-party pages) | Fetch and review | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/organization) |
| SD-28 | No duplicate or contradictory entities (two `Organization`s with different data, plugin + manual markup) | Group the nodes by type / `@id` | Medium | *(inference)* |
| SD-29 | Stable, reused `@id`s; `@id` references resolvable in the page or on the site | Graph analysis | Low | [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) *(inference)* |
| SD-30 | JS-generated markup present in the rendered DOM, updated on every route, not conditional on cookie consent | Rich Results Test by URL; URL Inspection; raw vs rendered HTML comparison | High | [G](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript) [SEJ] |
| SD-31 | Search Console: rich result status, unparsable data, Manual actions; trends after releases | Search Console reports | High | [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) |
| SD-32 | No page created only to host structured data; no "markup for AI" promised as a lever | Review | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |

## Build rules
Build rules create no IDs; each points to the checks it satisfies.

**What to propose at all**
- Propose JSON-LD only (1) for documented rich results available in the site's market and language (matrix and restricted table), or (2) to describe entities (`WebSite`, `Organization`, `LocalBusiness`, `Person` / `ProfilePage`, `Article`). Never promise AI citations, ranking or "GEO" visibility from markup; never recommend `FAQPage` / `HowTo` for rich results; `llms.txt` and "AI markup" are out of scope (see `ai-search.md`) → SD-06, SD-07, SD-32.
- If the CMS or a plugin already emits markup, configure it instead of adding a second hand-written block → SD-28.

**Minimum JSON-LD per archetype**
- **ecommerce**: home → one `WebSite` + `OnlineStore` (`@id` `/#organization`) with `hasMerchantReturnPolicy` / `hasShippingService` (or on the policies page); product pages → `Product` + `Offer` (or `ProductGroup` with variants) in the initial HTML, `BreadcrumbList`; ratings only from real customers → SD-10, SD-13, SD-22, SD-24, SD-26, SD-17, SD-21.
- **editorial**: home → `WebSite` + `Organization` (publisher); articles → `Article` / `NewsArticle` / `BlogPosting` with `author` referencing each author's `@id`, labelled visible dates; author pages → `ProfilePage`; `BreadcrumbList`; paywalled pages → `isAccessibleForFree` markup → SD-19, SD-20, SD-18, SD-21.
- **local-business**: home → `WebSite`; contact or location page → the most specific `LocalBusiness` subtype, one per location, with NAP and hours identical to the page and the Business Profile; no `aggregateRating` / `review` on itself → SD-14, SD-15, SD-16.
- **personal-brand**: home → `WebSite`; About page → `ProfilePage` with `mainEntity` `Person` (`@id` `/about#person`), `sameAs` to the person's own profiles; every article reuses that `@id` as `author` (and as `publisher` when there is no company) → SD-10, SD-18, SD-27, SD-29.
- **professional-services**: home → `WebSite` + `Organization` (or `ProfilePage` + `Person` when the practice is one person); `LocalBusiness` only with a real address shown on the page; client testimonials never marked up as `Review` → SD-13, SD-14, SD-16.
- **saas-product**: home → `WebSite` + `Organization`; product page → `SoftwareApplication` only with real ratings or reviews visible on the page; otherwise describe the entity only → SD-04, SD-17.

**`@id` conventions** *(inference)*
- Absolute, stable, on the canonical host: `https://host/#website`, `https://host/#organization`, `https://host/about#person` (use the real About path), `https://host/locations/<city>#localbusiness` for each location.
- Define each entity once (home or About page) and reference it elsewhere with `{"@id": "…"}`; never give the same entity two `@id`s or two different sets of data → SD-28, SD-29.

**One `WebSite` node, home only**
- Exactly one `WebSite` node, on the home page only, with `name`, `url` and optional `alternateName`; the other home variants redirect to the canonical host (CI-17) → SD-10, SD-11, SD-12.

**Where to emit JSON-LD by rendering mode**
- **SSR / SSG / prerendering**: emit JSON-LD in the server HTML (in `<head>` or early in `<body>`), per route; this is the default for every archetype and required for reliable `Product` handling → SD-24, SD-30.
- **CSR (client-side rendering)**: Google renders JavaScript and reads JSON-LD present in the rendered DOM, but other bots (most AI crawlers and link-preview bots) are not documented to render JavaScript — see the bot table in `ai-search.md`. Verify with RJ-01 (initial HTML), RJ-14 (JSON-LD in the rendered DOM) and RJ-17 (essentials early, under 2 MB); one block per route, replaced on navigation, not behind cookie consent → SD-30.

**Consistency with visible content**
- Every value in the markup appears on the page (prices, stock, hours, ratings, dates, salaries); names match `<title>`, `og:site_name` and the Business Profile → SD-03, SD-10, SD-15, SD-20.

**Testing before and after release**
- Development: Rich Results Test by URL for supported types; Schema Markup Validator for syntax and for types the test does not cover (e.g. `WebSite` site name); parse every `application/ld+json` block in the build output → SD-01, SD-04.
- After deploy: URL Inspection on a sample of templates; watch the rich result status reports and Manual actions after each release → SD-31.

## Notes by site type
- **ecommerce**: `Product` in the initial HTML; organization-level return and shipping policies are preferred, but Merchant Center / Search Console settings override markup; member prices and loyalty programmes only in the listed countries; beta carousels only for aggregator category pages in the EEA, Türkiye, South Africa. `ecommerce.md` references SD-22, SD-24 and SD-26 instead of repeating them.
- **editorial**: one author object per person, linked to an author `ProfilePage`; labelled visible dates; paywall markup to distinguish a paywall from cloaking; breadcrumbs only show on desktop; reviews of third-party products or businesses can carry stars (no self-reviews).
- **local-business**: the Google Business Profile remains the main source for the knowledge panel; one `LocalBusiness` per location; no public address → `Organization`; restaurant carousel and vacation rentals are limited-access programmes.
- **personal-brand**: `ProfilePage` + `Person` on the About page gives no rich result but anchors the entity; never use `JobPosting` to say "available for hire" (job requests are prohibited).
- **professional-services**: client testimonials are not `Review` markup; ⚠ avoid the deprecated `ProfessionalService` type, use a specific subtype. *Regulated professions and legal notices*: show what local law requires on the site (e.g. a VAT ID in the EU, a company registration number in the UK, a professional register or licence number in Germany or the US); `vatID`, `taxID` or `identifier` can mirror the visible value. Google describes `vatID` as a trust signal for users; it does not present it as a ranking factor.
- **saas-product**: `SoftwareApplication` rich results require real ratings or reviews; course list results for training content exist only in English.

## Third-party views
- **Google's position on AI** [G](https://developers.google.com/search/docs/appearance/ai-features): AI Overviews and AI Mode have no additional requirements; **no** special files, "AI markup" or special schema.org are needed; structured data only has to match the visible text. Google's May 2026 guidance on optimising for generative AI repeats that AEO/GEO are "still SEO" and that structured data is not required for AI features (it remains useful for rich results) [SEJ 2026-05] *(re-verify: Google URL not recorded)*. AI-features opt-out controls and Google-Extended: see the "Controls" table in `ai-search.md`.
- **Ahrefs study (May 2026)** [SEJ 2026-05]: across ~6 million URLs, pages cited by AI had about 3 times more JSON-LD (**correlation**). In the causal test (1,885 pages that added JSON-LD between August 2025 and March 2026, compared with ~4,000 controls, ±30-day window) the effect was null or negative: AI Overviews −4.6%, AI Mode +2.4%, ChatGPT +2.2% (the latter two indistinguishable from chance). Stated limits: only pages already heavily cited, only schema present in the HTML (not injected via JS), types aggregated, Bing/Copilot/Perplexity/Claude not measured.
- Williams-Cook experiment [SEJ]: **invalid** JSON-LD was still read as text by LLMs → for LLMs, markup is mostly text, not a privileged structure.
- Widespread, plausible but **unproven** opinions [SEJ]: `Person` / `Organization` with consistent `sameAs` and `@id` help **entity disambiguation** (namesakes, personal brands); keep name, NAP and hours identical across site, schema and Business Profile. This is consistent with Google's principles (accurate, consistent data), but no effect on ranking or citations has been shown. The concrete risk cited is **stale** schema (e.g. an old phone number) [SEJ].
- Microsoft/Bing (reported second-hand) states that schema helps Copilot [SEJ]: not verified in the sources read *(re-verify)*.
- John Mueller: markup types "come and go", few are worth maintaining [SEJ] (quote reported by SEJ).

## Myths and outdated advice
Full list of retired features: [Retired or restricted rich results](#retired-or-restricted-rich-results); general myths: `myths-deprecated.md`.
- ⚠ **"Schema for AI / GEO"** [SEJ]: many sources (often vendors with a conflict of interest) claim that JSON-LD, `FAQPage` or `HowTo` increase citations in AI assistants. No Google confirmation; several SEJ authors classify these claims as hypotheses or "snake oil". About 168,000 pages reportedly claim that "FAQ schema is critical for GEO" (figure reported by SEJ), while Google retired the FAQ rich result in 2026.
- ⚠ **Adding `FAQPage` or `HowTo` markup to win rich results**: both features are retired (HowTo in 2023, FAQ in 2026); the markup is harmless but has no effect in Search → SD-06.
- ⚠ **Removing `WebSite` because the sitelinks search box was retired**: only `SearchAction` became useless; the `WebSite` node still feeds the site name → SD-10.
- ⚠ **Marking up client testimonials or embedded Google/Facebook reviews as stars on your own business**: self-serving reviews are not eligible and can lead to a manual action → SD-16.
- ⚠ **`data-vocabulary.org` markup**: no longer eligible since January 2021; migrate to schema.org → SD-02.
- ⚠ **`ProfessionalService` as the type for a local professional**: deprecated in schema.org; use a specific subtype.
- ⚠ **Valid markup guarantees a rich result**: Google never guarantees it [G](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
