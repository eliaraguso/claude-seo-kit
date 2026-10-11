# Adapter: Angular
> Checked 2026-10-11 against angular.dev v22.2. Framework APIs are framework knowledge, not Google rules; the rules behind them are in `rendering-javascript.md`.

## Detection
`angular.json`, `@angular/core` in `package.json`; HTML: `ng-version="…"` on the root element. SSR is set up when `@angular/ssr` and a server routes file (`app.routes.server.ts`) exist.

## Rendering default and options
- A plain `ng new` app is CSR (app shell): content needs JS → RJ-01. Add SSR with `ng add @angular/ssr`.
- Server routes choose per route: `RenderMode.Prerender` (SSG, best for content pages; `getPrerenderParams` for parameterised routes), `RenderMode.Server` (SSR for dynamic pages), `RenderMode.Client` (non-indexable areas only).
- Hydration (`provideClientHydration()`): server and client HTML must match; do not swap text after hydration → RJ-12.
- `@defer`: on the server only the `@placeholder` is rendered (triggers do not run) unless incremental hydration with `hydrate` triggers is enabled.

## Where title, meta, canonical and robots meta live
- `title` on each route (or a custom `TitleStrategy`); `Meta` service (`updateTag`) for description and robots.
- Canonical: no built-in service; keep one `<link rel="canonical">` (via `DOCUMENT`) and update it on navigation, never append a new one → RJ-09.
- No `noindex` in `src/index.html` → RJ-08.

## Links and routing
- `PathLocationStrategy` is the default; never `HashLocationStrategy` / `withHashLocation()` → RJ-03.
- `routerLink` on `<a>` outputs `href`; on `div`/`button`/`span` it creates no crawlable link; do not navigate with `(click)="router.navigate(…)"` → RJ-05. Check that `href` is in the served HTML (Google lists `<a routerLink>` without `href` as not recommended).

## robots.txt and sitemap generation
`robots.txt` goes in `public/` (copied as is). No built-in sitemap: generate it at build time from the route list. The SPA fallback must not answer `/robots.txt` or `/sitemap.xml` with `index.html` → CI-02.

## 404 handling (true status)
- SSR: wildcard route `**` to a not-found component plus server route `{ path: '**', renderMode: RenderMode.Server, status: 404 }`; for statuses known only at runtime (missing slug), inject `RESPONSE_INIT` and set `status` → RJ-06, RJ-07.
- Prerendered routes: `PrerenderFallback` (`Server` default, `Client`, `None`) decides what unknown params get.
- Pure CSR: `Meta.addTag({ name: 'robots', content: 'noindex' })` in the not-found component, or redirect to a URL the host serves with `404`.

## hreflang and i18n
`@angular/localize` + `ng build --localize` builds one app per locale; serve each under its own prefix (`/en/`, `/de/`) with hreflang links in the head, not client-only language switching on one URL → RJ-31 *(inference)*.

## Structured data hooks
Insert `<script type="application/ld+json">` from a service (via `DOCUMENT`) so it is rendered on the server; keep values equal to the visible text → RJ-14.

## Common pitfalls (with check IDs)
- Content pages shipped as CSR only → RJ-01, RJ-02.
- Indexable content inside `@defer` with `on interaction`/`on hover` (never triggered by Google) → RJ-21.
- `TransferState` / serialised state inline counts toward the 2 MB HTML limit → RJ-15, RJ-17; bundle budgets in `angular.json` → RJ-16.
- Keep `outputHashing: "all"` (production default) for fingerprinting → RJ-24.
- Canonical appended on every navigation → RJ-09.

## Sources
[Docs v22.2 SSR](https://angular.dev/guide/ssr) · [Docs v22.2 defer](https://angular.dev/guide/templates/defer) · [Docs v22.2 i18n](https://angular.dev/guide/i18n) · [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
