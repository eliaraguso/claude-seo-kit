# Site archetypes

> Updated 2026-10-11. Scope: choosing audit priorities and checks by site type. Primary source: Google Search Central.
> A site can have one primary archetype and one or more secondary ones (e.g. professional-services with a blog: Studio Ferri Orientamento publishing guides).
> The technical principles (indexing, rendering, on-page) apply to every site: what changes is the order of priorities and what counts as a "conversion".

## Contents
- [How to choose](#how-to-choose)
- [ecommerce](#ecommerce)
- [editorial](#editorial)
- [local-business](#local-business)
- [personal-brand](#personal-brand)
- [professional-services](#professional-services)
- [saas-product](#saas-product)
- [Modifiers](#modifiers)
- [Priority matrix](#priority-matrix)

## How to choose
| Question | If yes |
|---|---|
| Do people buy products on the site? | ecommerce |
| Is the main value articles, guides or news? | editorial |
| Do customers come to a physical location, or is the service delivered within a geographic area? | local-business (often together with professional-services) |
| Does the site present a person (portfolio, CV, author) and is the "product" the person themselves? | personal-brand |
| Does it sell the professional services of a person or a firm, including online? | professional-services |
| Does it sell software or an app? | saas-product |

Several yeses: the primary archetype is where most conversions happen; the others are secondary. Legacy slugs from SEO.md v1 (`professionista-servizi`, `attivita-locale`, `editoriale`, `prodotto-saas`) map to these English slugs as listed in `conventions.md` › Archetypes.

## ecommerce
- **Typical goal:** get product and category pages shown in Search, Images and Shopping surfaces (product snippets, merchant listings, free listings) and turn those visits into orders. Example: Acme Widgets.
- **Key queries:** product name, model or SKU; category + attribute ("waterproof widgets"); brand + product; comparisons and "best X for Y"; store name.
- **Priorities:** unique product pages (own descriptions, original photos, specifications, real reviews) · `Product` + `Offer` markup (`ProductGroup` for variants) matching the visible price and availability · product data shared with Google through Merchant Center as well as markup, kept consistent with the page · one stable URL per product (and per variant if it has its own page), parameters in a consistent order · faceted navigation under control: only valuable filter combinations crawlable and indexable · category pages reachable through `<a href>` links, pagination with a distinct URL per page · store policies (returns, shipping) in Merchant Center or `OnlineStore` markup · site structure that shows which categories and products matter most.
- **Typical risks:** filters and sort parameters creating near-infinite URL spaces (crawl wasted, duplicates); infinite scroll or "load more" without paginated URLs, so deeper products are never discovered; manufacturer descriptions copied across many sites; temporarily out-of-stock products removed or redirected to the home page (soft 404) instead of staying live with availability updated (→ `ecommerce.md` EC-14, EC-15); price or availability that differ between page, markup and feed; variants indexed as duplicates without canonical or `ProductGroup`; prices and stock rendered only client-side; review markup on content the store wrote itself.
- **Conversions:** add to cart, checkout started, purchase; secondary: newsletter sign-up, wishlist.
- **Files to read:** `ecommerce.md`, `structured-data.md` (Product, merchant listings, variants), `crawling-indexing.md` (faceted navigation, pagination, crawl budget), `site-architecture.md`, `rendering-javascript.md`, `performance-cwv.md`, `international.md` (if multilingual).
- **Stacks commonly seen:** `adapters/shopify.md`, `adapters/wordpress.md` (WooCommerce), `adapters/nextjs-react.md` and `adapters/nuxt-vue.md` (headless storefronts), `adapters/hosted-builders.md` (Wix, Squarespace stores), `adapters/classic-ssr.md`.
- **Sources:** [G](https://developers.google.com/search/docs/specialty/ecommerce) · [G](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) · [G](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) · [G](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) · [G](https://developers.google.com/search/docs/appearance/structured-data/product-variants)

## editorial
- **Typical goal:** steady organic readership from articles, guides or news, in Search results, Top stories, Discover and Google News, turned into loyal readers or subscribers.
- **Key queries:** informational questions and how-tos; topic + current event; broad topics covered by hub pages; publication name; author names.
- **Priorities:** original content based on first-hand experience, not generic summaries · real authors with a profile page, bylines linked to it · correct dates: visible date matches `datePublished`/`dateModified`, updated only for real changes · `Article`/`NewsArticle`/`BlogPosting` with `author`, `image` and dates · internal links and topic structure (hub and category pages, related articles) · Discover readiness: large images at least 1200 px wide, `max-image-preview:large`, titles that describe the content without clickbait · News sitemap for news publishers (only articles published in the last two days, up to 1,000 news URLs per sitemap) · crawlable archive pagination · paywalled content declared (see [Modifiers](#modifiers)).
- **Typical risks:** articles mass-produced with AI or templates (scaled content abuse); fake date refreshes; misleading or sensational titles and images (Discover content policies); third-party content hosted to exploit the site's ranking signals (site reputation abuse); thin tag pages indexed by the hundred; infinite scroll without URLs; syndicated copies outranking the original.
- **Conversions:** newsletter sign-up, subscription or membership, return visits; ad or affiliate revenue where applicable.
- **Files to read:** `editorial-news.md`, `content-quality-spam.md`, `on-page-appearance.md`, `structured-data.md` (Article), `site-architecture.md`, `entity-personal-brand.md` (author pages), `ai-search.md`, `performance-cwv.md`.
- **Stacks commonly seen:** `adapters/wordpress.md`, `adapters/static-generators.md` (Hugo, Jekyll, Eleventy), `adapters/astro.md`, `adapters/nextjs-react.md`, `adapters/gatsby.md`, `adapters/drupal.md`, `adapters/joomla.md`, `adapters/hosted-builders.md`.
- **Sources:** [G](https://developers.google.com/search/docs/appearance/google-discover) · [G](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap) · [G](https://developers.google.com/search/docs/appearance/structured-data/article) · [G](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content) · [G](https://developers.google.com/search/docs/essentials/spam-policies)

## local-business
- **Typical goal:** appear in the local pack and on Maps, and turn that into calls, visits and bookings. Example: Northwind Physio in Oslo.
- **Key queries:** service or category + city, or "near me"; business name.
- **Priorities:** complete, up-to-date Business Profile · name, address and phone (NAP) identical everywhere · `LocalBusiness` with the most specific subtype · opening hours, services and contacts as HTML text · real reviews, with replies.
- **Typical risks:** data that differ between the site and the listings; near-identical location pages; temporary closures handled by switching the site off.
- **Conversions:** phone calls, direction requests, bookings, Business Profile actions (website clicks, calls, directions).
- **Files to read:** `local-seo.md`, `structured-data.md`, `crawling-indexing.md` (temporary closures), `entity-personal-brand.md`, `bing-basics.md` (Bing Places), `on-page-appearance.md`.
- **Stacks commonly seen:** `adapters/wordpress.md`, `adapters/hosted-builders.md`, `adapters/static-html.md`, `adapters/joomla.md`.
- **Sources:** [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) · [GBP](https://support.google.com/business/answer/3038177) · [G](https://developers.google.com/search/docs/essentials/spam-policies)

## personal-brand
- **Typical goal:** be found and chosen when someone searches the person's name (clients, employers, event organisers), and be associated with specific skills. Example: Ada Novak, developer.
- **Key queries:** first and last name; name + role or skill; name + city.
- **Priorities:** the results page for one's own name · a clear entity (About page as entity home, `ProfilePage` + `Person` with `sameAs`) · consistent name and bio across professional and social profiles · projects and case studies showing first-hand experience · external mentions (talks, articles, communities).
- **Typical risks:** namesakes; generic titles ("Home", "Portfolio"); "made by" links in the footers of client sites (link spam); credentials that cannot be verified.
- **Conversions:** contact, clicks to professional profiles or email, CV download.
- **Files to read:** `entity-personal-brand.md`, `structured-data.md`, `on-page-appearance.md`, `ai-search.md`.
- **Stacks commonly seen:** `adapters/static-html.md`, `adapters/astro.md`, `adapters/static-generators.md`, `adapters/nextjs-react.md`, `adapters/gatsby.md`, `adapters/wordpress.md`, `adapters/hosted-builders.md`.
- **Sources:** [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) · [G](https://developers.google.com/search/docs/appearance/site-names) · [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [G](https://developers.google.com/search/docs/essentials/spam-policies)

## professional-services
- **Typical goal:** consultation requests from people searching for the service, or for a problem the service solves. Example: Studio Ferri Orientamento in Bologna.
- **Key queries:** service (+ city if delivered in person, + "online" if remote); the client's problem or question; the professional's name.
- **Priorities:** one page per service with unique content · About page with real credentials · clear answers to clients' doubts · real reviews · Business Profile if there is a service area or an office.
- **Typical risks:** cloned "service + city" pages (doorways); promises and guarantees on topics close to health, work or money; self-published review stars (not eligible).
- **Conversions:** contact form, booking, phone, email.
- **Files to read:** `local-seo.md` (if there is a local presence), `content-quality-spam.md`, `entity-personal-brand.md`, `structured-data.md`, `site-architecture.md`.
- **Stacks commonly seen:** `adapters/wordpress.md`, `adapters/hosted-builders.md`, `adapters/static-html.md`, `adapters/astro.md`, `adapters/joomla.md`, `adapters/drupal.md`.
- **Sources:** [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) · [GBP](https://support.google.com/business/answer/3038177)

## saas-product
- **Typical goal:** sign-ups, trials and demo requests from people searching for the problem the software solves, for alternatives, or for the product name; documentation that answers both users and prospects.
- **Key queries:** the problem or task ("how to send recurring invoices"); category ("invoicing software for freelancers"); "<competitor> alternative", "X vs Y"; integrations ("<product> + <tool>"); product name + pricing, login or docs; error messages and how-tos answered in the docs.
- **Priorities:** feature, use-case and integration pages with unique content · indexable documentation and help centre: HTML served by the server or prerendered, stable URLs, crawlable links, not behind login · marketing pages rendered in the HTML; the logged-in app kept out of the index · `SoftwareApplication` (`WebApplication`/`MobileApplication`) only with genuine ratings or reviews: the rich result requires `aggregateRating` or `review` plus `offers.price` · `Organization` and `WebSite` on the home page · honest comparison pages: verifiable facts, dated, fair to the alternatives · pricing in text, not only in images or scripts · one canonical version of versioned docs.
- **Typical risks:** single-page app with an empty server HTML or `#` routes; soft 404s from client-side routing (every route returns 200); app, login or staging subdomains indexed; versioned docs duplicated without canonical; "alternative to X" or integration pages generated at scale from a template (scaled content abuse, doorways); ratings in markup written by the company itself; comparison pages with false or stale claims.
- **Conversions:** sign-up, trial start, demo request, pricing-page visit, app install.
- **Files to read:** `rendering-javascript.md`, `content-quality-spam.md`, `structured-data.md` (SoftwareApplication), `site-architecture.md`, `crawling-indexing.md`, `on-page-appearance.md`, `ai-search.md`, `performance-cwv.md`, `international.md` (often multilingual).
- **Stacks commonly seen:** `adapters/nextjs-react.md`, `adapters/nuxt-vue.md`, `adapters/angular.md`, `adapters/sveltekit.md`, `adapters/remix-react-router.md`, `adapters/astro.md`, `adapters/gatsby.md`, `adapters/static-generators.md` (docs), `adapters/hosted-builders.md` (Webflow).
- **Sources:** [G](https://developers.google.com/search/docs/appearance/structured-data/software-app) · [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) · [G](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews) · [G](https://developers.google.com/search/docs/essentials/spam-policies)

## Modifiers
Modifiers are not archetypes: they add checks to whatever archetype the site has.
- **`multilingual`** → `international.md`: add hreflang (reciprocal, self-referencing, valid codes), one URL per language or region, canonical within the same language, no forced redirects by IP or browser language; page copy is written in each site language.
- **`marketplace-ugc`** → `content-quality-spam.md` UGC and spam rows (CQ-09, CQ-16, CQ-17): moderation, `rel="ugc"`/`nofollow` on user links, `noindex` on new users' content until it earns trust, internal search pages not indexable (decision tree: `crawling-indexing.md` › Internal search result pages), third-party content not hosted to exploit the site's reputation.
- **`paywall`** → `editorial-news.md`: paywalled sections marked with `isAccessibleForFree: false` and `hasPart` + `cssSelector`, so Google can tell the paywall from cloaking; check that Googlebot receives the full content.
- **`app-and-site`** → `structured-data.md` SoftwareApplication: app pages carry `SoftwareApplication`/`MobileApplication` with genuine ratings; store links crawlable; the logged-in web app stays out of the index.

## Priority matrix
Suggested order of audit areas per archetype (1 = first). Indexing and rendering are always blocking: if they fail, nothing else counts. "—" = not applicable. The "International" rank applies only when the site has the `multilingual` modifier; otherwise skip that row.

| Area | ecommerce | editorial | local-business | personal-brand | professional-services | saas-product |
|---|---|---|---|---|---|---|
| Bot access and indexing | 1 | 1 | 1 | 1 | 1 | 1 |
| JavaScript rendering | 2 | 2 | 2 | 2 | 2 | 2 |
| Ecommerce specifics (if ecommerce) | 3 | — | — | — | — | — |
| Structured data | 4 | 6 | 5 | 6 | 8 | 9 |
| Site architecture and internal links | 5 | 5 | 8 | 8 | 7 | 5 |
| On-page and appearance in results | 6 | 3 | 4 | 3 | 3 | 3 |
| International (if multilingual) | 7 | 8 | 9 | 9 | 9 | 6 |
| Content, quality and spam | 8 | 4 | 7 | 5 | 6 | 4 |
| Performance (Core Web Vitals) | 9 | 9 | 10 | 7 | 10 | 7 |
| Entity and personal brand | 10 | 7 | 6 | 4 | 5 | 8 |
| Local | 11 | 10 | 3 | 10 | 4 | 10 |
| AI search and measurement | 12 | 11 | 11 | 11 | 11 | 11 |
