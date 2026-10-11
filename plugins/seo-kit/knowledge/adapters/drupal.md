# Adapter: Drupal 10/11
> Checked 2026-10-11 against drupal.org project pages (Metatag 2.2, Pathauto 8.x-1.15, Redirect 8.x-1.13, Simple XML Sitemap 4.2, Hreflang, RobotsTxt) and Drupal core 11.x source. CMS knowledge, not Google rules.

## Detection
Signals in the README table. Also `drupal/core` in `composer.json`, `sites/default/settings.php`.

## Rendering default and options
Twig themes render full HTML on the server: most RJ checks do not apply. Still relevant: JS-only blocks or embeds (reviews, maps, listings loaded by AJAX) → RJ-01; decoupled front ends follow their own adapter (e.g. `nextjs-react.md`).

## Where title, meta, canonical and robots meta live
- **Metatag** (contrib): title, description, canonical (robots too, *not verified*), with defaults per entity type and bundle (tokens via the Token module) and per-item overrides; Open Graph and Twitter Cards via included submodules → RJ-11, CI-22.
- Without Metatag, title and canonical come from core and the theme *(not verified against the docs)*; check one canonical per page → CI-22.

## Links and routing
- Core Path module stores URL aliases; **Pathauto** (contrib) generates them from token patterns (`/node/123` → `/blog/my-title`) and can create redirects when an alias changes.
- **Redirect** (contrib): manual redirects and redirects of non-aliased paths (`/node/123`) to the alias → CI-25, CI-20. Its **Redirect 404** submodule logs 404s and turns them into redirects; map each to the real replacement → CI-21.

## robots.txt and sitemap generation
- Core ships `robots.txt` in the web root through Composer scaffolding: it allows CSS/JS/images under `/core/` and `/profiles/`, disallows `/admin/`, `/user/login`, `/search/`… Edits are overwritten on `composer` updates: add lines via `drupal-scaffold` `file-mapping` `append` → CI-03, RJ-18.
- **RobotsTxt** (contrib) for multisite: per-site file from the UI; delete the physical `robots.txt` first.
- **Simple XML Sitemap** (contrib, `^10.3 || ^11`): entities, views, custom links, hreflang alternates, IndexNow → CI-13, CI-14. No core XML sitemap.

## 404 handling (true status)
Core answers unknown paths with `404` *(inference)*; a custom 404 page is set in Basic site settings (`system.site` `page.404`) *(UI path not verified against the docs)*. Check with curl that the custom page keeps the `404` → CI-26.

## hreflang and i18n
Core Content Translation adds hreflang only on content entity pages; the **Hreflang** module (contrib) adds it on all pages → CI-36, CI-37. Language prefixes (`/de/…`) per language *(inference)*.

## Structured data hooks
JSON-LD is not in Metatag itself: **Schema.org Metatag** (contrib) adds it. Check for duplicates from theme templates → SD-28, RJ-14.

## Common pitfalls (with check IDs)
- `robots.txt` customisations lost after a core update (scaffold overwrite) → CI-03.
- Both `/node/123` and the alias answering `200` without redirect or canonical → CI-25.
- Metatag defaults with a fixed canonical or `noindex` copied to every bundle → CI-22, CI-10.
- Redirect 404 used to send every miss to the home page → CI-21.
- Views with exposed filters creating crawlable parameter URLs → CI-34 *(inference)*.

## Sources
[Metatag](https://www.drupal.org/project/metatag) · [Pathauto](https://www.drupal.org/project/pathauto) · [Redirect](https://www.drupal.org/project/redirect) · [Simple XML Sitemap](https://www.drupal.org/project/simple_sitemap) · [Hreflang](https://www.drupal.org/project/hreflang) · [RobotsTxt](https://www.drupal.org/project/robotstxt) · [SEO modules list](https://www.drupal.org/docs/extending-drupal/contributed-modules/contributed-module-archive/contrib-modules-for-building-the-site-functionality/search-engine-optimization/search-engine-optimization-modules) · [core robots.txt](https://git.drupalcode.org/project/drupal/-/blob/11.x/core/assets/scaffold/files/robots.txt). The brief's page `drupal.org/docs/administering-a-drupal-site/seo` returned 404: not verified against it.
