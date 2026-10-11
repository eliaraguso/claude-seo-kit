# Adapter: Static HTML
> Checked 2026-10-11. Hand-written or exported `.html` files served as they are. Host behaviour is host knowledge, not Google rules; the rules behind it are in `rendering-javascript.md` and `crawling-indexing.md`.

## Detection
Only `.html`/`.css`/`.js` files and assets, no framework config, no build step in `package.json` (if any). Common hosts: GitHub Pages, Netlify, Cloudflare Pages, Apache, nginx. Static output of a generator (Hugo, Jekyll, Eleventy) belongs to `static-generators.md`.

## Rendering default and options
Every page is complete HTML: minimal JS risk. JS matters only if navigation, contact details or text are injected by scripts → RJ-01, RJ-05.

## Where title, meta, canonical and robots meta live
In each file's `<head>`, written by hand or by a shared include. Check every page has its own title and description → RJ-11, one absolute canonical → CI-22, and no `noindex` copied from a template → CI-10. Keep the head valid (no `img`/`iframe` before the meta tags) → RJ-10.

## Links and routing
Plain `<a href>`. Pick one URL form (`/about/`, `/about` or `/about.html`) and use it in links, canonicals and the sitemap; the other forms redirect → CI-25.

## robots.txt and sitemap generation
Hand-written `robots.txt` and `sitemap.xml` at the root, with a `Sitemap:` line → CI-08. Update `lastmod` only when a page really changes → CI-15.

## 404 handling (true status)
The host must serve its error page with a `404` status, not `200` → RJ-06, CI-26:
- GitHub Pages, Netlify, Cloudflare Pages: a `404.html` at the root ([GitHub](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site), [Netlify](https://docs.netlify.com/routing/redirects/redirect-options/), [Cloudflare](https://developers.cloudflare.com/pages/configuration/serving-pages/)). Their docs do not state the status code, so confirm the `404` with curl *(inference)*; without a root `404.html`, Cloudflare Pages assumes an SPA and serves `/` for unknown paths.
- Apache: `ErrorDocument 404 /404.html`; nginx: `error_page 404 /404.html;`.
Check with curl on a made-up URL.

## hreflang and i18n
One folder per language (`/en/`, `/de/`), `<html lang>`, and reciprocal `<link rel="alternate" hreflang>` in every page of the cluster → CI-36, CI-37.

## Structured data hooks
`<script type="application/ld+json">` in the head of each page; keep values equal to the visible text → RJ-14.

## Common pitfalls (with check IDs)
- Error page served with `200` by the host → RJ-06, CI-26.
- Trailing slash / `.html` inconsistent with canonicals → CI-25, CI-22.
- Meta refresh used instead of server-side redirects → CI-20 [G](https://developers.google.com/search/docs/crawling-indexing/special-tags).
- Navigation or footer injected by a JS include → RJ-01, RJ-05.
- Inline base64 images inflating the HTML → RJ-15, RJ-17.

## Sources
[G](https://developers.google.com/search/docs/crawling-indexing/special-tags) · [G](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors) · [Docs Apache 2.4 ErrorDocument](https://httpd.apache.org/docs/2.4/custom-error.html) · [Docs nginx error_page](https://nginx.org/en/docs/http/ngx_http_core_module.html#error_page)
