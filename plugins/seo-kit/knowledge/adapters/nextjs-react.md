# Adapter: Next.js and React SPA
> Checked 2026-10-11 against Next.js docs v16.4 and React Router v8.4. Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
Next.js: `next.config.*`, `next` in `package.json`, `app/` or `pages/`; HTML: `/_next/static/` assets, `__NEXT_DATA__` (Pages Router). React SPA: `vite.config.*` + `react`, `index.html` with an empty root `<div>`, no meta-framework config.

## Rendering default and options
- Next.js App Router: Server Components, prerendered at build unless the route uses request-time data, then server-rendered. Data fetched in `'use client'` components after mount is not in the served HTML → RJ-01.
- React SPA (Vite and similar): CSR → prerender/SSG the indexable pages or move them to a meta-framework → RJ-01, RJ-02.

## Where title, meta, canonical and robots meta live
- Next.js: `metadata` export or `generateMetadata` in `layout`/`page`: `title` (with `template`), `description`, `alternates.canonical`, `robots` (`index`, `follow`, `googleBot`). Set `metadataBase` in the root layout so relative URLs become absolute.
- Streaming metadata (since v15.2): a slow `generateMetadata` can be appended to `<body>` for bots not in `htmlLimitedBots`. Keep it fast, or set `htmlLimitedBots: /.*/` to keep tags in the head → RJ-10.
- Pages Router: `next/head`. React SPA: one head manager, one canonical, no `noindex` in `index.html` → RJ-08, RJ-09.

## Links and routing
`next/link` and React Router `<Link>` render `<a href>` → RJ-05. React Router: `createBrowserRouter` / `<BrowserRouter>`, never `createHashRouter` / `<HashRouter>` → RJ-03.

## robots.txt and sitemap generation
Next.js: `app/robots.ts` (or a static `app/robots.txt`) and `app/sitemap.ts` (`generateSitemaps` for large sites). SPA: static files in `public/`; the host fallback must not rewrite them to `index.html` → CI-02.

## 404 handling (true status)
- `notFound()` from `next/navigation` + `not-found.tsx`. Called before streaming starts → `404`; called inside a `<Suspense>` boundary after streaming began → the response keeps `200` and Next.js injects `noindex`. Run existence checks before streaming (page or `generateMetadata`, or Proxy) → RJ-06, RJ-07.
- React SPA: catch-all route that adds `noindex` or redirects to a URL served with `404`; configure the host.

## hreflang and i18n
`alternates.languages` in metadata outputs `<link rel="alternate" hreflang>`. App Router has no built-in i18n routing: use a `[lang]` segment, one URL per language, no client-only switching → RJ-31.

## Structured data hooks
Next.js recommends a native `<script type="application/ld+json">` in `page`/`layout`, with `JSON.stringify(data).replace(/</g, '\\u003c')` against XSS; not `next/script` → RJ-14.

## Common pitfalls (with check IDs)
- Main content only in client components fetched after mount → RJ-01.
- `notFound()` inside `<Suspense>`: `200` + `noindex` instead of `404` → RJ-06, RJ-07.
- Metadata streamed into `<body>` → RJ-10.
- Hydration swaps text (e.g. stock status) → RJ-12.
- Large inline RSC payload or `__NEXT_DATA__` → RJ-15, RJ-17.
- "Application error" shell served with `200` during outages → RJ-30.

## Sources
[Docs v16.4 metadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) · [Docs v16.4 notFound](https://nextjs.org/docs/app/api-reference/functions/not-found) · [Docs v16.4 JSON-LD](https://nextjs.org/docs/app/guides/json-ld) · [Docs v8.4 React Router](https://reactrouter.com/api/data-routers/createHashRouter) · [G OH 2024-06](https://developers.google.com/search/help/office-hours/2024/june) (Next.js works when configured; set SEO up before launch)
