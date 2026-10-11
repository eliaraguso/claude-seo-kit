# Adapter: SvelteKit
> Checked 2026-10-11 against svelte.dev/docs/kit (SvelteKit 2.x and 3). Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
Signals in the README table (repo; HTML `__sveltekit_`, `/_app/immutable/`). Also `@sveltejs/kit` in `package.json`; from 2.62 the config can live in `vite.config.js` (`sveltekit({ adapter })`), and SvelteKit 3 no longer supports `svelte.config.js`.

## Rendering default and options
- SSR is the default, then hydration. Page options in `+page.js`/`+layout.js`: `prerender` (`true`, `false`, `'auto'`), `ssr`, `csr`.
- `ssr = false` renders an empty shell; in the root layout the whole app becomes an SPA → RJ-01, RJ-02. Keep SSR or prerender on content pages.
- The prerenderer crawls `<a>` links from the root; dynamic routes need `entries` or `config.prerender.entries`, or the build reports "marked as prerenderable, but were not prerendered".
- `csr = false` ships no JS: fine for pure content pages.

## Where title, meta, canonical and robots meta live
- `<svelte:head>` per page; common pattern: return SEO data from `load`, render it with `page.data` in the root layout's `<svelte:head>` → RJ-11.
- Canonical and robots meta: no built-in API; one `<link rel="canonical">` per page in `<svelte:head>` → RJ-09, CI-22 *(inference)*.

## Links and routing
Plain `<a href>` is what the prerenderer crawls and what Google follows; do not replace content links with click handlers → RJ-05. `trailingSlash`: `'never'` (default, `/about/` redirects to `/about`), `'always'`, `'ignore'` (not recommended) → CI-25.

## robots.txt and sitemap generation
`robots.txt` in `static/`. No built-in sitemap: the docs show an endpoint `src/routes/sitemap.xml/+server.js` returning XML with `Content-Type: application/xml`; prerender it on static hosts → CI-13, CI-14.

## 404 handling (true status)
- Unmatched routes are framework errors with status `404`; check the page served with curl.
- Missing slug: `error(404, 'Not found')` from `@sveltejs/kit` in `load` sets the status → RJ-07.
- Errors in `handle`, a `+server.js` handler or the root `+layout.js`/`+layout.server.js` use `src/error.html`.
- `adapter-static` `fallback` (e.g. `200.html`) serves the SPA shell for unknown URLs; the docs warn of "large negative performance and SEO impacts" → RJ-06, CI-26. On GitHub Pages the docs suggest generating a `404.html`.

## hreflang and i18n
No built-in i18n. The `reroute` hook maps translated paths (`/de/ueber-uns` → `/de/about`). Output hreflang in `<svelte:head>` and set `<html lang>` per locale → CI-36, CI-37 *(inference)*.

## Structured data hooks
The SEO page does not cover JSON-LD. Render `<script type="application/ld+json">` from `load` data inside `<svelte:head>` so it is in the SSR HTML → RJ-14, SD-30 *(inference)*.

## Common pitfalls (with check IDs)
- `export const ssr = false` in the root layout "to fix a build error" → RJ-01.
- Prerendered site with `fallback` answering every URL `200` → RJ-06, CI-26.
- Dynamic routes missing from `entries`: pages never built → CI-26 *(inference)*.
- `trailingSlash` not matching the host (`about.html` vs `about/index.html`) → CI-25.
- Sitemap endpoint listing non-canonical URLs → CI-14.

## Sources
[Docs page-options](https://svelte.dev/docs/kit/page-options) · [Docs seo](https://svelte.dev/docs/kit/seo) · [Docs adapters](https://svelte.dev/docs/kit/adapters) · [Docs adapter-static](https://svelte.dev/docs/kit/adapter-static) · [Docs errors](https://svelte.dev/docs/kit/errors) · [Docs hooks](https://svelte.dev/docs/kit/hooks). The docs show no version number; they reference SvelteKit 3.
