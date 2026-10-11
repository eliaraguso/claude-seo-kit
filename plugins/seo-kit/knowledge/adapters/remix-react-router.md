# Adapter: Remix 2 / React Router (framework mode)
> Checked 2026-10-11 against reactrouter.com (8.4.0, framework mode; same APIs as React Router 7) and v2.remix.run. Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
Signals in the README table. Also `@react-router/dev` or `@remix-run/*` in `package.json`, `app/routes.ts`, `app/root.tsx`. A plain Vite React app with `react-router` but no framework config belongs to `nextjs-react.md` (React SPA).

## Rendering default and options
- `ssr: true` (default in `react-router.config.ts`): server rendering; loaders run on the server.
- `prerender`: `true` (static paths of `routes.ts`, no dynamic ones), an array of paths, or `async prerender({ getStaticPaths })`. With `ssr: true` the rest is still server-rendered.
- `ssr: false` without `prerender` is SPA mode: only `root` is rendered to HTML → RJ-01, RJ-02. Use `prerender` for content routes.

## Where title, meta, canonical and robots meta live
- `meta` export returns descriptors (`{ title }`, `{ name: "description", content }`); `<Meta />` and `<Links />` in the root `<head>`.
- The last matching route's `meta` replaces the whole array, it is not merged: a child without description loses the parent's → RJ-11. Remix 2 shows merging via `matches`.
- Canonical: `{ tagName: "link", rel: "canonical", href }` in `meta` (Remix 2 docs). Since React 19 the docs recommend rendering `<title>`/`<meta>` in the component instead of `meta`; keep one canonical whatever the method → RJ-09, CI-22.

## Links and routing
`<Link to>`/`<NavLink>` render `<a href>`; do not navigate content with `useNavigate()` on click → RJ-05 *(inference)*.

## robots.txt and sitemap generation
`robots.txt` in `public/`. No built-in sitemap: use a resource route (a module with a `loader` returning a `Response` and no default export) for `/sitemap.xml`, with `Content-Type: application/xml` → CI-13, CI-14, CI-42 *(inference: docs show a PDF example)*.

## 404 handling (true status)
- Missing record: `throw data("Not Found", { status: 404 })` in the `loader`; the nearest `ErrorBoundary` renders it (`isRouteErrorResponse`) → RJ-07. Remix 2 pattern: `throw new Response(null, { status: 404 })` *(not verified against the docs)*.
- Unmatched URLs render the root `ErrorBoundary`; confirm the `404` with curl → RJ-06 *(not stated on the fetched pages)*.
- `ssr: false` + partial `prerender`: the host serves `index.html` or `__spa-fallback.html` with `200` for every other path (the docs' `_redirects` example) → RJ-06, CI-26.

## hreflang and i18n
No built-in i18n. Locale prefix in `routes.ts` (`/:lang/…`) and hreflang `link` descriptors per route → CI-36, CI-37 *(inference)*.

## Structured data hooks
Remix 2: `meta` descriptor `{ "script:ld+json": { … } }` outputs `<script type="application/ld+json">`. With React 19, render the script in the route component from loader data → RJ-14, SD-30 *(inference)*.

## Common pitfalls (with check IDs)
- SPA mode deployed for a content site → RJ-01.
- Child route `meta` without description/canonical (array replaced) → RJ-11, CI-22.
- `meta` + React 19 `<title>` both used: two titles or canonicals → RJ-09 *(inference)*.
- Static host rewriting every path to the SPA fallback with `200` → CI-26.
- Loader returning `200` with an empty "not found" component → RJ-07.

## Sources
[Docs 8.4 pre-rendering](https://reactrouter.com/how-to/pre-rendering) · [Docs 8.4 route module](https://reactrouter.com/start/framework/route-module) · [Docs 8.4 status codes](https://reactrouter.com/how-to/status) · [Docs 8.4 error boundary](https://reactrouter.com/how-to/error-boundary) · [Docs 8.4 resource routes](https://reactrouter.com/how-to/resource-routes) · [Docs Remix v2 meta](https://v2.remix.run/docs/route/meta)
