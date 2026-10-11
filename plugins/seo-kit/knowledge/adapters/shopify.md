# Adapter: Shopify (Online Store 2.0 themes)
> Checked 2026-10-11 against shopify.dev theme docs and help.shopify.com. Platform knowledge, not Google rules; the rules are in `crawling-indexing.md`.

## Detection
Signals in the README table. Also `templates/*.json`, `sections/`.

## Rendering default and options
Liquid renders full HTML on the server: most RJ checks do not apply. Still relevant: apps that inject reviews, size charts, FAQs or prices with JS → RJ-01; filters and "load more" without URLs → RJ-22.

## Where title, meta, canonical and robots meta live
- `layout/theme.liquid` `<head>`: `<title>{{ page_title }}…</title>` (Shopify's pattern appends tags, page, `shop.name`), `<meta name="description" content="{{ page_description | escape }}">`, `<link rel="canonical" href="{{ canonical_url }}">`.
- Per-item title and description are edited in the admin *(not verified against the docs)* → OP-01, OP-08.
- `{{ content_for_header }}` is required in `<head>`; do not edit or parse it.
- `noindex`: the `seo.hidden` metafield (value `1`; also removes the page from the sitemap) or a conditional `<meta name="robots" content="noindex">` in `theme.liquid` → CI-10.

## Links and routing
The `within` filter builds `/collections/<c>/products/<handle>`, "the same content on separate URLs" (Shopify). Link to `/products/…` and check that the canonical of the collection-scoped URL points to it → CI-22, CI-23, CI-47 *(how `canonical_url` resolves is not documented: verify with curl)*.

## robots.txt and sitemap generation
- Generated robots.txt blocks `/admin`, `/cart`, `/checkout`, `/account`, `/orders` and filtered/sorted collection URLs. Customise only via `templates/robots.txt.liquid` looping over `robots.default_groups` (unsupported; "can result in loss of all traffic") → CI-03, CI-07.
- `/sitemap.xml` is automatic (child sitemaps for products, collections, blogs, pages) on every domain; not reachable while the store is in private (password) mode → CI-13.

## 404 handling (true status)
Invalid URLs render the theme's 404 template; the docs do not state the status, so check with curl → CI-26. Redirect removed products to the closest replacement, not the home page → CI-21.

## hreflang and i18n
With Shopify Markets, hreflang is added automatically via `content_for_header` and follows each market's domains and languages. When a theme or app also outputs it, switch off "Automatic hreflang tags" and build tags from the `localization` object → CI-36, IN-10. Non-international extra domains should redirect to the primary domain → CI-17.

## Structured data hooks
`{{ product | structured_data }}` and `{{ article | structured_data }}` return schema.org data (`Product`, or `ProductGroup` when variants exist; `Article`); the theme wraps it in `<script type="application/ld+json">`. Avoid a second `Product` from apps → SD-28.

## Common pitfalls (with check IDs)
- Duplicate `Product` markup from theme + review app → SD-28.
- Reviews/ratings rendered only by an app's JS → RJ-01, SD-03.
- robots.txt.liquid dropping default rules (cart, filtered collections) → CI-34.
- Store left in private (password) mode after launch: closed to Google → CI-48.

## Sources
[Docs theme SEO metadata](https://shopify.dev/docs/storefronts/themes/seo/metadata) · [Docs robots.txt](https://shopify.dev/docs/storefronts/themes/seo/robots-txt) · [Docs hreflang](https://shopify.dev/docs/storefronts/themes/seo/hreflang) · [Docs layouts](https://shopify.dev/docs/storefronts/themes/architecture/layouts) · [Liquid within](https://shopify.dev/docs/api/liquid/filters/within) · [Liquid structured_data](https://shopify.dev/docs/api/liquid/filters/structured_data) · [Help robots](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt) · [Help sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map) · [Help hide a page](https://help.shopify.com/en/manual/promoting-marketing/seo/hide-a-page-from-search-engines). Shopify docs carry no version number.
