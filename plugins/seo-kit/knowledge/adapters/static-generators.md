# Adapter: Static site generators (Hugo, Jekyll, Eleventy)
> Checked 2026-10-11 against gohugo.io (v0.167.0), jekyllrb.com (v4.4.1) with jekyll-seo-tag and jekyll-sitemap, 11ty.dev (3.1 stable, 4.0 docs). Tool knowledge, not Google rules; host rules in `static-html.md`.

## Detection
Signals in the README table. Jekyll also: `Gemfile` with `jekyll`, `_layouts/`; Eleventy: `@11ty/eleventy` in `package.json`.

## Rendering default and options
Complete HTML per page: minimal JS risk, except injected navigation, search or comments → RJ-01, RJ-05.

## Where title, meta, canonical and robots meta live
- **Hugo**: in the base template's `<head>`; embedded partials `opengraph.html`, `twitter_cards.html`, `schema.html` (`{{ partial "opengraph.html" . }}`). Canonical from `.Permalink` *(inference)*.
- **Jekyll**: `{% seo %}` from jekyll-seo-tag right before `</head>`: title (with site title), description, canonical, prev/next, Open Graph, Twitter card, JSON-LD. Needs `url` in `_config.yml`; per page `title`, `description`, `image`.
- **Eleventy**: layouts in `_includes/` (`layout:` in front matter); `title`/`description` flow through the data cascade into `<title>`/`<meta>` written by you → RJ-11, CI-22.

## Links and routing
- Hugo: one URL form per page; set `baseURL` to the production URL *(inference)*.
- Jekyll: `permalink` (`pretty` ends with `/`; `date`, `none` end in `.html`).
- Eleventy: trailing slash by default (`/about/` → `about/index.html`); `permalink: false` writes no file.
Keep links, canonicals and sitemap on the same form → CI-25, CI-23.

## robots.txt and sitemap generation
- **Hugo**: built-in `sitemap.xml` (one per language plus a sitemap index on multilingual sites); per page `sitemap: { disable: true }`; override with `layouts/sitemap.xml`. robots.txt from `enableRobotsTXT = true` (default template is just `User-agent: *`) or a file in `static/` → CI-08, CI-13.
- **Jekyll**: jekyll-sitemap (needs `url`; `sitemap: false` excludes a page; `lastmod` from `last_modified_at` or the post date) → CI-14, CI-15.
- **Eleventy**: no built-in sitemap or robots.txt; write them as templates or copy files *(inference)*.

## 404 handling (true status)
All three output a `404.html` (Hugo `layouts/404.html`, per language `404.de.html`; Eleventy `permalink: 404.html`). The **host** decides the status: GitHub Pages, Netlify, Cloudflare Pages serve it automatically; Apache needs `ErrorDocument 404 /404.html` → RJ-06, CI-26. See `static-html.md` for host rules; check with curl.

## hreflang and i18n
Hugo multilingual mode builds one tree and sitemap per language; output hreflang from `.Translations` in the head *(inference)*. Jekyll and Eleventy: one folder per language, hreflang written in the layout → CI-36, CI-37.

## Structured data hooks
- Hugo `schema.html` outputs **microdata** `meta` tags, not JSON-LD: add your own JSON-LD partial if needed → SD-04, SD-28.
- jekyll-seo-tag outputs JSON-LD; `publisher` needs `logo` → SD-09.
- Eleventy: JSON-LD in the layout → RJ-14.

## Common pitfalls (with check IDs)
- Wrong `baseURL`/`url` (localhost, staging): wrong canonicals and sitemap URLs → CI-14, CI-22.
- Draft or test pages built and listed in the sitemap → CI-14, CI-38.
- Hugo `layouts/robots.txt` example disallows every page: copied by mistake → CI-03.
- `lastmod` equal to the build date on every page → CI-15.
- Theme + plugin both writing a canonical or title → CI-22.

## Sources
[Docs Hugo sitemap](https://gohugo.io/templates/sitemap/) · [Docs Hugo robots](https://gohugo.io/templates/robots/) · [Docs Hugo 404](https://gohugo.io/templates/404/) · [Docs Hugo embedded](https://gohugo.io/templates/embedded/) · [Docs Jekyll 4.4 permalinks](https://jekyllrb.com/docs/permalinks/) · [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag) · [jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap) · [Docs 11ty permalinks](https://www.11ty.dev/docs/permalinks/) · [Docs 11ty layouts](https://www.11ty.dev/docs/layouts/) · [Docs 11ty 404](https://www.11ty.dev/docs/quicktips/not-found/)
