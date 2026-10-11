# Adapter: Classic server-rendered frameworks (Django, Laravel, Rails)
> Checked 2026-10-11 against Django 6.1, Laravel 13.x and Rails Guides 8.1.4. Framework APIs are framework knowledge, not Google rules; the rules behind them are in `crawling-indexing.md`.

## Detection
Signals in the README table. Also Django `settings.py`/`urls.py`; Laravel `routes/web.php`, `resources/views/*.blade.php`; Rails `app/views/**/*.erb`.

## Rendering default and options
Templates render full HTML on the server: most RJ checks do not apply. Still relevant: JS-only widgets (reviews, maps, prices) and front-end islands loading content later → RJ-01; infinite scroll → RJ-22; JS-injected canonical → RJ-09.

## Where title, meta, canonical and robots meta live
Base template `<head>` (Django `{% block %}`, Blade sections, Rails `content_for`), filled per view → RJ-11 *(inference)*. None of the three has a built-in SEO tag API: build the canonical from the production host and the route, not from the request `Host` header → CI-22, CI-17 *(inference)*. `noindex` on staging via an environment flag → CI-38.

## Links and routing
- Django: `path()` routes, `get_absolute_url()`.
- Laravel: `Route::redirect` returns `302` by default; use `Route::permanentRedirect` (`301`) for moves → CI-20.
- Rails: `redirect` in `routes.rb` is `301` by default (`:status` to change); `to_param` for readable slugs → OP-18.

## robots.txt and sitemap generation
- robots.txt: a static file (Laravel and Rails `public/`) or a view *(inference)* → CI-01.
- Django: `django.contrib.sitemaps` (core contrib app, needs the sites framework); `Sitemap` classes with `items()`, `location`/`get_absolute_url()`, `lastmod`, `protocol`, `i18n`/`alternates`/`x_default`; paginates at 50,000 URLs with an index → CI-13, CI-15.
- Laravel: no core sitemap; `spatie/laravel-sitemap` (Spatie, third-party) builds one manually or by crawling the site.
- Rails: no core sitemap; `sitemap_generator` gem (community): `config/sitemap.rb`, `default_host`, `rake sitemap:refresh` → `public/sitemap.xml.gz`. Its ping step is obsolete for Google ([G](https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping)): use `sitemap:refresh:no_ping` and Search Console → CI-50.

## 404 handling (true status)
Native in all three → CI-26:
- Django: `raise Http404` → standard page with `404`; template `404.html` shown when `DEBUG = False`; `handler404` in the root URLconf.
- Laravel: unmatched routes, failed constraints and missing implicitly bound models return `404`. `Route::fallback` runs with web middleware; a `missing()` closure that redirects every miss to a list page creates soft 404s → CI-21.
- Rails: `ActiveRecord::RecordNotFound` and `ActionController::RoutingError` map to `:not_found` and render `public/404.html` with `404`.

## hreflang and i18n
Django: `i18n = True`, `alternates = True`, `x_default = True` on `Sitemap` adds hreflang to the sitemap. Laravel/Rails: locale prefix in routes and hreflang in the layout → CI-36, CI-37, IN-10 *(inference)*.

## Structured data hooks
JSON-LD in the template from the same fields shown on the page → SD-03.

## Common pitfalls (with check IDs)
- `DEBUG = True` in production: Django's debug page (status still `404`) instead of a useful 404 page → CI-26.
- Catch-all route returning `200` "not found" → RJ-06.
- `Route::redirect` left at `302` after a URL change → CI-20.
- Sitemap built with `http` or the wrong host (`protocol`, `default_host`) → CI-14.

## Sources
[Docs Django 6.1 sitemaps](https://docs.djangoproject.com/en/stable/ref/contrib/sitemaps/) · [Docs Django 6.1 views](https://docs.djangoproject.com/en/stable/topics/http/views/) · [Docs Laravel 13 routing](https://laravel.com/docs/routing) · [Docs Rails 8.1 routing](https://guides.rubyonrails.org/routing.html) · [Docs Rails 8.1 configuring](https://guides.rubyonrails.org/configuring.html) · [spatie/laravel-sitemap](https://github.com/spatie/laravel-sitemap) · [sitemap_generator](https://github.com/kjvarga/sitemap_generator)
