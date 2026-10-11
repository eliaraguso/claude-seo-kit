# Adapter: WordPress (+ WooCommerce)
> Checked 2026-10-11 against the WordPress code reference (7.1). CMS behaviour is CMS knowledge, not Google rules; the rules behind it are in `rendering-javascript.md` and `crawling-indexing.md`.

## Detection
`wp-config.php`, `wp-content/`, `wp-includes/`; HTML: `<meta name="generator" content="WordPress …">`, `/wp-content/` assets, `/wp-json/` link. WooCommerce: `wp-content/plugins/woocommerce`, `woocommerce` body class.

## Rendering default and options
PHP renders full HTML on the server: JS risk comes from heavy themes, page builders and plugins (sliders, tabs, review and contact widgets) → RJ-01, RJ-23.

## Where title, meta, canonical and robots meta live
- `<title>`: themes declare `add_theme_support( 'title-tag' )` and core prints it in `wp_head`.
- Canonical: core prints `rel="canonical"` on single posts and pages; an SEO plugin usually takes over (one canonical only → CI-22).
- Robots meta: `wp_robots()` (since 5.7, filter `wp_robots`). Settings › Reading › "Discourage search engines from indexing this site" (`blog_public` = 0) adds `noindex, nofollow` to every page → CI-10.
- Meta description: not in core; set it with the SEO plugin. Use the CMS or SEO plugin settings for `noindex` and canonical, not hand-written tags.

## Links and routing
Settings › Permalinks: use a readable structure, not "Plain" (`?p=123`). Menus and core blocks output `<a href>`; check page-builder buttons and JS mega menus → RJ-05.

## robots.txt and sitemap generation
Without a physical file, core serves a virtual `robots.txt` (filter `robots_txt`) that lists the core sitemap. Core XML sitemaps (since 5.5) live at `/wp-sitemap.xml`; SEO plugins often replace them: keep one sitemap → CI-08, CI-14.

## 404 handling (true status)
Core answers unknown URLs with `404` and the theme's `404.php`. Plugins that redirect every 404 to the home page create soft 404s → CI-21, CI-26.

## hreflang and i18n
Not in core: multilingual plugins output hreflang and per-language URLs. Check for one set of tags, in the `<head>`, reciprocal → RJ-10, CI-36, CI-37.

## Structured data hooks
SEO plugins print a JSON-LD graph in `wp_head`; WooCommerce adds `Product` data on product pages. Avoid duplicates from theme + plugins and keep prices/stock equal to the page → RJ-14.

## Common pitfalls (with check IDs)
- Two robots meta tags from two plugins (case reported in [G OH 2023-05](https://developers.google.com/search/help/office-hours/2023/may)) → CI-10.
- Plugin or theme updates that block search ([G OH 2024-08](https://developers.google.com/search/help/office-hours/2024/august)) → CI-10, RJ-18.
- "Discourage search engines" left on after launch *(inference)* → CI-10.
- Core lazy-loads images (since 5.5; since 6.3 it skips the first content image and adds `fetchpriority`); lazy-load plugins may still hit the hero → OP-24 [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading).
- Reviews, prices or contact details shown only by JS widgets → RJ-01.
- Page-builder CSS/JS inline bloat → RJ-15, RJ-17.

## Sources
[Docs 7.1 wp_robots](https://developer.wordpress.org/reference/functions/wp_robots/) · [Docs 7.1 wp_robots_no_robots](https://developer.wordpress.org/reference/functions/wp_robots_no_robots/) · [Docs 7.1 sitemaps](https://developer.wordpress.org/reference/functions/wp_sitemaps_get_server/) · [G](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
