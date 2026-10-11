# Adapters
> Updated 2026-10-11. One file per framework, CMS or host: where the generic rules of `rendering-javascript.md`, `crawling-indexing.md` and `on-page-appearance.md` land in that stack.

## Purpose
The topic files say *what* Google needs (indexable HTML, true 404s, one canonical, crawlable links). An adapter says *where* that lives in one stack: which file or API sets the title, how the stack returns a real `404`, what it generates for robots.txt and the sitemap, and which pitfalls are typical, each tied to a check ID. Skills detect the stack with the table below and read **only** the matching adapter (Tier 0 in `conventions.md`). Framework APIs are framework knowledge, not Google rules: each adapter names the docs and the version it was checked against; verify against the version in use.

## Adapter template
Sections, in this order, each file under 4 KB:
1. Detection
2. Rendering default and options
3. Where title, meta, canonical and robots meta live
4. Links and routing
5. robots.txt and sitemap generation
6. 404 handling (true status)
7. hreflang and i18n
8. Structured data hooks
9. Common pitfalls (with check IDs)
10. Sources (framework docs, version checked)

Adapters create no check IDs: pitfalls point to existing IDs (`RJ-`, `CI-`, `OP-`, `SD-`…).

## Detection table
Check signals in the repository first, then in the served HTML or headers. When several match, the most specific wins (e.g. `next.config.*` over a generic React setup; `react-router.config.*` over a Vite React SPA). For a "planned" adapter, fall back to the closest ready one plus the topic files.

| Signal in repo or HTML | Adapter | Status |
|---|---|---|
| `angular.json`; `@angular/core` in `package.json`; HTML `ng-version=` | [angular](angular.md) | ready |
| `next.config.*`; `next` in `package.json`; HTML `/_next/static/`, `__NEXT_DATA__` | [nextjs-react](nextjs-react.md) | ready |
| `vite.config.*` + `react` without a meta-framework config; empty root `<div>` in `index.html` | [nextjs-react](nextjs-react.md) (React SPA) | ready |
| `nuxt.config.*`; HTML `/_nuxt/`, `<div id="__nuxt">`; `vue` + `vue-router` without Nuxt | [nuxt-vue](nuxt-vue.md) | ready |
| `astro.config.*`; HTML `<astro-island>`, `/_astro/` | [astro](astro.md) | ready |
| `wp-config.php`, `wp-content/`; HTML `<meta name="generator" content="WordPress`; WooCommerce: `wp-content/plugins/woocommerce` | [wordpress](wordpress.md) | ready |
| Only `.html` files, no framework config or build step | [static-html](static-html.md) | ready |
| `svelte.config.js` | sveltekit | planned |
| `remix.config.*`, `react-router.config.*` | remix-react-router | planned |
| `gatsby-config.*` | gatsby | planned |
| `hugo.toml` / `config.toml` + `content/`; `_config.yml` (Jekyll); `.eleventy.js` / `eleventy.config.*` | static-generators | planned |
| `manage.py` (Django); `artisan` (Laravel); `Gemfile` + `config/routes.rb` (Rails) | classic-ssr | planned |
| `theme/layout/theme.liquid`; `shopify.theme.toml` | shopify | planned |
| `core/lib/Drupal` | drupal | planned |
| `administrator/` + `configuration.php` | joomla | planned |
| HTML `data-wf-page` (Webflow); `X-Wix-*` response headers (Wix); `static1.squarespace.com` assets (Squarespace) | hosted-builders | planned |
