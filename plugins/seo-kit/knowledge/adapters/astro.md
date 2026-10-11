# Adapter: Astro
> Checked 2026-10-11 against docs.astro.build (Astro 7 docs) and @astrojs/sitemap v3.7. Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
`astro.config.*`, `astro` in `package.json`, `src/pages/`; HTML: `<astro-island>` elements, `/_astro/` assets.

## Rendering default and options
- Default output is `'static'`: every page is prerendered to HTML and no JS is shipped unless a component is an island.
- On-demand rendering needs an adapter (`npx astro add <host>`); opt out per page with `export const prerender = false`, or set `output: 'server'` and keep static pages with `prerender = true`.
- Islands: `client:load`, `client:idle`, `client:visible` render HTML on the server, then hydrate. `client:only` skips server rendering → no indexable content there (RJ-01). `server:defer` (server islands) renders a component on demand, outside the page render: keep primary content out of it *(inference)*.

## Where title, meta, canonical and robots meta live
In a shared layout's `<head>`, fed by props from each page: `<title>`, description, `<link rel="canonical" href={new URL(Astro.url.pathname, Astro.site)}>`, robots meta. One absolute canonical per page → CI-22, RJ-09, RJ-10.

## Links and routing
File-based routing in `src/pages/`; links are plain `<a href>` → RJ-05. Set `trailingSlash` and `build.format` so URLs, canonicals and sitemap entries agree *(inference)*.

## robots.txt and sitemap generation
`@astrojs/sitemap` writes `sitemap-index.xml` + `sitemap-0.xml` and requires `site` in the config. robots.txt: static file in `public/` or an endpoint `src/pages/robots.txt.ts`.

## 404 handling (true status)
- `src/pages/404.astro` builds `404.html`; most hosts serve it with `404`, check with curl → RJ-06.
- On-demand pages: set `Astro.response.status = 404` or return `new Response(null, { status: 404 })` when a record is missing → RJ-07.

## hreflang and i18n
`i18n` config: `locales`, `defaultLocale`, `routing.prefixDefaultLocale`; `Astro.currentLocale` and `getRelativeLocaleUrl()` for links. Astro does not document automatic hreflang tags: add `<link rel="alternate" hreflang>` in the layout. The sitemap `i18n` option adds `xhtml:link` alternates.

## Structured data hooks
`<script type="application/ld+json" set:html={JSON.stringify(data)} />` in the layout or page; it is static HTML → RJ-14.

## Common pitfalls (with check IDs)
- Main content in a `client:only` island → RJ-01.
- Missing `site` → relative or missing canonicals and no sitemap → CI-22, CI-08.
- Host returns `200` for `404.html` or for unknown paths → RJ-06.
- Content collections with a bad slug rendered with `200` in SSR mode → RJ-07.
- Large framework islands or inline base64 images → RJ-15, RJ-17.

## Sources
[Docs directives](https://docs.astro.build/en/reference/directives-reference/) · [Docs on-demand rendering](https://docs.astro.build/en/guides/on-demand-rendering/) · [Docs pages and 404](https://docs.astro.build/en/basics/astro-pages/) · [Docs i18n](https://docs.astro.build/en/guides/internationalization/) · [Docs v3.7 sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/) · [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) (SSG/prerender recommended)
