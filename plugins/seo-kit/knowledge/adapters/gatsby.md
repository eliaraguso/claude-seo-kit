# Adapter: Gatsby
> Checked 2026-10-11 against gatsbyjs.com docs (Gatsby 5; Head API since 4.19). Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
Signals in the README table. Also `gatsby` in `package.json`, `gatsby-node.*`, `src/pages/`; HTML `<div id="___gatsby">` *(not verified against the docs)*.

## Rendering default and options
- Pages are built to static HTML (SSG); the docs recommend SSG, with Deferred Static Generation (DSG) as the alternative to SSR.
- SSR: an async `getServerData` on a page; it may return `props`, `headers` and `status`.
- Client-only routes (`matchPath`) are not pre-rendered: keep them for non-indexable areas → RJ-01.

## Where title, meta, canonical and robots meta live
- `export function Head` in pages and `createPage` templates only (not in components); allowed tags: `title`, `meta`, `link`, `base`, `script`, `style`, `noscript`. Metadata is server-rendered into the static HTML.
- Usual pattern: a `SEO` component fed by `siteMetadata` (with `siteUrl` for absolute URLs) through `useStaticQuery`, overridden per page → RJ-11.
- Canonical: not covered by the docs; add one `<link rel="canonical">` in `Head` from `siteUrl` + `location.pathname`. Tags with the same `id` are deduplicated (last wins) → CI-22, RJ-09 *(inference)*.
- `<html lang>`: `Head` can set `html`/`body` attributes since 5.5 (overrides `onRenderBody`'s `setHtmlAttributes`).

## Links and routing
`<Link>` from `gatsby` for internal links; `trailingSlash` in `gatsby-config` (`always` default, `never`, `ignore`; since 4.7) must match canonicals and the host → CI-25.

## robots.txt and sitemap generation
- `static/robots.txt`: files in `static/` are copied to `public/` untouched.
- `gatsby-plugin-sitemap` writes `sitemap-index.xml` and `sitemap-0.xml` (new file every 45,000 URLs), only in production builds; needs `siteMetadata.siteUrl` or `resolveSiteUrl`. `/404`, `/dev-404-page` are always excluded; `excludes` for more; `serialize` can map `lastmod` → CI-13, CI-14, CI-15. Point the `Sitemap:` line to `sitemap-index.xml` → CI-08.

## 404 handling (true status)
- `src/pages/404.js` is built as `404.html`; many static hosts serve it for unknown URLs, others need a rule → RJ-06, CI-26. Check the status with curl.
- SSR pages: return `status: 404` from `getServerData` for a missing record → RJ-07 *(inference: the docs give no 404 example)*.

## hreflang and i18n
No built-in i18n. One page per locale (`/en/…`, `/de/…`) created in `gatsby-node`, hreflang `link`s in `Head` → CI-36, CI-37 *(inference)*.

## Structured data hooks
`<script type="application/ld+json">` inside `Head` (the docs allow data-block scripts there); check it in the Rich Results Test → RJ-14.

## Common pitfalls (with check IDs)
- Content behind client-only routes or fetched in `useEffect` → RJ-01.
- `siteUrl` missing or set to a preview host: wrong absolute URLs in sitemap and meta → CI-14, CI-38.
- `trailingSlash` vs host behaviour causing redirect or duplicate variants → CI-25.
- Large `page-data` / inline styles bloating HTML → RJ-15, RJ-17.
- Sitemap tested in `gatsby develop` (not generated there) *(inference)*.

## Sources
[Docs v5 SEO](https://www.gatsbyjs.com/docs/how-to/adding-common-features/seo/) · [Docs v5 Head](https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-head/) · [gatsby-plugin-sitemap](https://www.gatsbyjs.com/plugins/gatsby-plugin-sitemap/) · [Docs v5 404](https://www.gatsbyjs.com/docs/how-to/adding-common-features/add-404-page/) · [Docs v5 SSR](https://www.gatsbyjs.com/docs/reference/rendering-options/server-side-rendering/) · [Docs v5 gatsby-config](https://www.gatsbyjs.com/docs/reference/config-files/gatsby-config/) · [Docs v5 static folder](https://www.gatsbyjs.com/docs/how-to/images-and-media/static-folder/)
