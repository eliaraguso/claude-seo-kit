# Adapter: Joomla 5
> Checked 2026-10-11 against the Joomla 5.x help (Global Configuration), the Joomla user manual (Schema.org) and the joomla-cms 5.4 source. CMS knowledge, not Google rules.

## Detection
Signals in the README table. Also `libraries/src/`, `robots.txt.dist`, `htaccess.txt` in the root.

## Rendering default and options
PHP templates render full HTML on the server: most RJ checks do not apply. Still relevant: extensions that load content, reviews or maps with JS → RJ-01; tabs/sliders hiding text → RJ-23.

## Where title, meta, canonical and robots meta live
- System › Global Configuration › Site › **Metadata**: Site Meta Description, Robots (`index, follow` … `noindex, nofollow`), Content Rights. A global `noindex` left from development blocks the whole site → CI-10.
- **SEO** settings: "Site Name in Page Titles" (before/after) → OP-02.
- Menu items and articles carry their own browser title, meta description and robots *(not verified against the docs)* → RJ-11.
- Canonical: the core System - SEF plugin adds one only when its "Site Domain" is set, built from the current path **and query** (parameters kept) → CI-22, CI-25. The plugin can also add or remove trailing slashes and redirect `index.php` URLs (joomla-cms 5.4 source).

## Links and routing
Global Configuration › SEO:
- **Search Engine Friendly URLs**: on.
- **Use URL Rewriting**: removes `index.php` from URLs; on Apache/LiteSpeed rename `htaccess.txt` to `.htaccess` (IIS and NGINX need their own config).
- **Add Suffix to URL**: adds `.html` etc. by document type; pick once and keep it → CI-25.

## robots.txt and sitemap generation
- Joomla ships `robots.txt.dist`; renamed to `robots.txt`, it disallows `/administrator/`, `/api/`, `/cache/`, `/components/`, `/modules/`, `/plugins/`, `/tmp/`… `/media/` (CSS/JS) is not blocked *(inference)*; check that no template or extension loads render assets from a blocked folder → RJ-18. In a subfolder install the file must move to the site root → CI-01.
- No core XML sitemap: extensions such as **OSMap** (XML and HTML sitemaps; Pro adds per-item noindex) → CI-13, CI-14.

## 404 handling (true status)
Unknown URLs go through the template's error page; check with curl that it returns `404`, also with SEF on and off *(not verified against the docs)* → CI-26. "Site Offline" shows the offline page to everyone: use it only for short maintenance → CI-48 *(status not documented; check it)*.

## hreflang and i18n
Core multilingual (language filter plugin and associations) gives per-language URLs; check reciprocal hreflang on associated items → CI-36, CI-37 *(not verified against the docs)*.

## Structured data hooks
Joomla 5 has core Schema.org support: enable **System - Schema.org**, set the site as Organization or Person, then choose a type in the article's Schema tab (BlogPosting, Book, Event, JobPosting, Organization, Recipe). Avoid a second graph from an extension → SD-28, SD-13.

## Common pitfalls (with check IDs)
- Global Robots set to `noindex` after launch → CI-10.
- `htaccess.txt` not renamed while rewriting is on: pages 404 *(inference)* → CI-26.
- Suffix or rewriting switched on a live site without redirects → CI-49, CI-25.
- Subfolder install with `robots.txt` left in the subfolder (crawlers read only the root file) → CI-01.
- Sitemap extension listing non-SEF or duplicate URLs → CI-14.

## Sources
[Docs 5.x Global Configuration](https://help.joomla.org/proxy?keyref=Help5.x:Site_Global_Configuration&lang=en) · [Joomla manual Schema.org](https://guide.joomla.org/user-manual/schema-org) · [joomla-cms 5.4 robots.txt.dist](https://github.com/joomla/joomla-cms/blob/5.4-dev/robots.txt.dist) · [SEF plugin](https://github.com/joomla/joomla-cms/blob/5.4-dev/plugins/system/sef/src/Extension/Sef.php) · [OSMap](https://extensions.joomla.org/extension/osmap/). docs.joomla.org returned 403 to the fetch: per-item metadata, 404 and multilingual behaviour are not verified against the docs.
