# Adapter: Nuxt and Vue SPA
> Checked 2026-10-11 against Nuxt docs 4.x, Vue Router v4/v5 and @nuxtjs/i18n v10.6. Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
Nuxt: `nuxt.config.*`, `nuxt` in `package.json`; HTML: `/_nuxt/` assets, `<div id="__nuxt">`. Vue SPA: `vue` + `vue-router` without Nuxt, `index.html` with an empty mount `<div>`.

## Rendering default and options
- Nuxt uses universal rendering (SSR + hydration) by default. `routeRules` per path: `prerender: true` (SSG at build), `ssr: false` (client only, non-indexable areas), `isr` / `swr` (cached). `nuxt generate` builds a fully static site (no hybrid route rules).
- Components inside `<ClientOnly>` are not in the served HTML → RJ-01.
- Vue SPA: CSR → prerender the indexable pages or move to Nuxt → RJ-01, RJ-02.

## Where title, meta, canonical and robots meta live
- `useSeoMeta({ title, description, robots, ogTitle, … })` in pages/layouts; `useHead({ link: [{ rel: 'canonical', href }] })` for the canonical (one per page) → RJ-09, RJ-11.
- Global defaults in `app.head` (`nuxt.config`); no `noindex` there → RJ-08.
- Vue SPA: `@unhead/vue` (same `useHead` API) on the client only.

## Links and routing
`<NuxtLink>` and `<RouterLink>` render `<a href>` → RJ-05. Vue Router: `createWebHistory()`, never `createWebHashHistory()` (its docs warn about the SEO impact) → RJ-03.

## robots.txt and sitemap generation
Static `public/robots.txt`, or the community modules `@nuxtjs/robots` and `@nuxtjs/sitemap` (Nuxt SEO; not part of core). Vue SPA: static files; the host fallback must not serve `index.html` for them → CI-02.

## 404 handling (true status)
- Nuxt: `throw createError({ status: 404 })` (older releases: `statusCode`) when data is missing; `error.vue` renders the page. Check the real response code with curl → RJ-06, RJ-07.
- Vue SPA: with history mode the server sends `index.html` for every path (no 404s). Add a catch-all route `/:pathMatch(.*)*` that adds `noindex` or redirects to a URL served with `404`.

## hreflang and i18n
`@nuxtjs/i18n`: locale prefixes, plus `useLocaleHead()` with the `seo` option to output `lang`, alternate hreflang links and canonical through `useHead` → RJ-10, RJ-31.

## Structured data hooks
`useHead({ script: [{ type: 'application/ld+json', innerHTML: JSON.stringify(data) }] })`, rendered on the server; or the community `nuxt-schema-org` module → RJ-14.

## Common pitfalls (with check IDs)
- Main content fetched only on the client (`server: false`, `onMounted`) or wrapped in `<ClientOnly>` → RJ-01.
- `ssr: false` route rule on indexable pages → RJ-01, RJ-02.
- Error page served with `200` → RJ-06, RJ-30.
- Large serialised payload (`window.__NUXT__`) inline → RJ-15, RJ-17.
- Two head sources (module + manual) creating two canonicals → RJ-09.

## Sources
[Docs 4.x SEO and meta](https://nuxt.com/docs/4.x/getting-started/seo-meta) · [Docs 4.x rendering](https://nuxt.com/docs/4.x/guide/concepts/rendering) · [Docs 4.x createError](https://nuxt.com/docs/4.x/api/utils/create-error) · [Docs Vue Router v4/v5](https://router.vuejs.org/guide/essentials/history-mode.html) · [Docs @nuxtjs/i18n v10.6](https://i18n.nuxtjs.org/docs/composables/use-locale-head)
