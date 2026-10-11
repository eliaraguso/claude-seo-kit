# Changelog

All notable changes to seo-kit are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## 1.0.0 — 2026-10-11

### Breaking
- **English everywhere.** Skills, knowledge base, templates, scripts and script output are now in English. Answers still follow the language of your message. Reports follow the report language recorded in `SEO.md`, and page copy follows the site language.
- **New plugin location.** The plugin moved from the repository root to `plugins/seo-kit/`; the marketplace entry points there. Update with `claude plugin marketplace update seo-kit-marketplace` and `claude plugin update seo-kit@seo-kit-marketplace`.
- **`SEO.md` v2.**
  - It has 11 numbered sections: Site · Site type and goal · Entity · Audience and search intents · Competitors · Access and tools · Baseline · Decisions and constraints · Monitoring · Change log · Audit history.
  - A v1 file (`# Profilo SEO`) is still read. `seo-discovery` offers to migrate it and never does so silently.
- **English archetype slugs.**
  - `professionista-servizi` → `professional-services`
  - `attivita-locale` → `local-business`
  - `editoriale` → `editorial`
  - `prodotto-saas` → `saas-product`
  - `personal-brand` and `ecommerce` are unchanged.
- **Script flags and JSON keys in English.** The `seo_fetch.py` output has a new schema, documented in `docs/page-schema.md`. Examples: `internal_links` is a list, `robots_meta` and `canonical` are objects, and `ua_comparison` moved under `site`.
  - `check_build.py` now requires `--base`.
  - `suggest.py` defaults to `--lang en`.
  - The `analyze_gsc.py` report headings are in English.
- **Exit codes.**
  - `seo_fetch.py`: 0 = done, 2 = invalid URL or site unreachable.
  - `check_build.py`: 0 = clean, 1 = findings at or above `--fail-on`, 2 = usage error.
  - `suggest.py`: 0 = done, 2 = usage error, 3 = rate-limited.
  - `analyze_gsc.py`: 0 = done, 2 = error.

### Added
- **Six new knowledge files:** `ecommerce.md`, `editorial-news.md`, `international.md`, `performance-cwv.md`, `site-architecture.md` and `bing-basics.md`.
- **Nine new framework/CMS adapters:** SvelteKit, Remix/React Router, Gatsby, static generators (Hugo, Jekyll, Eleventy), classic SSR (Django, Laravel, Rails), Shopify, Drupal, Joomla and hosted builders (Webflow, Wix, Squarespace). With the six extracted from the 0.2.x rendering guidance (Angular, Next.js/React, Nuxt/Vue, Astro, WordPress, static HTML), there are 15.
- **`lib/seokit/`:** a shared standard-library package used by every script:
  - HTTP with redirects, charsets and retries
  - HTML parser
  - robots.txt with Google semantics
  - sitemaps
  - DNS via `dig` or `nslookup`
  - Search Console export loader
  - typo packs (EN, IT)
- **Unit tests** (`tests/`): no network access needed, with byte-exact fixtures. There is a regression test for every fixed bug.
- **CI** (GitHub Actions):
  - Unit tests on Ubuntu, Windows and macOS with Python 3.9–3.13.
  - A lint job: `extract_dom.js` syntax, manifest JSON, index freshness and knowledge lint.
- **Evals** (`plugins/seo-kit/evals/`) for `claude plugin eval`, on fixture sites of fictional businesses.
- **`knowledge/INDEX.md`:** one line per check (440 checks, 46 aliases). It is generated from the check tables.
- **Tools:**
  - `tools/build_index.py` (with `--check`)
  - `tools/check_knowledge.py` (knowledge lint)
  - `tools/trigger_test.py` (skill-triggering test with `--dry-run`)
- **Docs:** `docs/knowledge-style-guide.md`, `docs/page-schema.md` and `docs/CONTRIBUTING.md`.
- **Language rules:** `knowledge/conventions.md` defines the working language and the fictional examples used across knowledge, skills, tests and evals.
- **Skills:** multilingual trigger phrases (EN, IT, ES, DE, FR) in every skill. Every skill that changes a project file appends a row to `SEO.md › 10. Change log`.

### Changed
- **Contradictions resolved, one owner per topic.** Each topic now has a single owning file; the other files hold an alias row (`Alias of CI-17`) or a one-line pointer. Examples:
  - Retired rich results (FAQ, HowTo, Practice problem) are owned by `structured-data.md`, citing Google's changelog. Book actions are not retired.
  - AI-visibility protocol: `ai-search.md` owns it; `measurement.md` owns the Search Console and GA4 side.
  - Orphan pages: owned by `crawling-indexing.md` (CI-47).
  - JavaScript lazy content (RJ-21) and lazy images (OP-24) are now distinct checks.
  - Core Web Vitals third-party views: kept only in `performance-cwv.md`.
- **One severity scale:** Critical / High / Medium / Low, in every file and report. There are no numeric scores. Legacy Italian labels map onto it.
- **Markers:**
  - **⚠** now means only "deprecated, unsupported or not to be recommended". Conditional checks carry a `Caveat:` instead.
  - Source tags are standardised: `[G]`, `[G OH]`, `[GBP]`, `[web.dev]`, `[SEJ YYYY-MM]`, `[Bing]`, `[IndexNow]`, `[Docs vX]`, *(inference)* and *(re-verify)*.
- **Archetypes rebalanced**, plus four modifiers: `multilingual`, `marketplace-ugc`, `paywall` and `app-and-site`.
- **Examples:** they use only fictional entities (Northwind Physio, Studio Ferri Orientamento, Acme Widgets, Ada Novak, Daily Fjord) and `.example` domains.
- **Knowledge field names** are aligned with the `seo_fetch.py` 1.0 output.
- **PageSpeed Insights:** the API's field data is being discontinued, so field data now comes from the CrUX API or the Search Console Core Web Vitals report.

### Fixed
1. An `<svg><title>` inside `<h1>` was reported as the page title, and the H1 was lost.
2. A `<noscript><img>` in `<head>` was reported as an invalid head tag.
3. A robots.txt starting with a UTF-8 BOM parsed to zero groups.
4. A missing `lang` attribute fell back to Italian accent checks on any page.
5. `<base href>` was ignored when resolving links.
6. An unknown charset in `Content-Type` crashed the run (`LookupError`).
7. Non-ASCII URLs crashed the run (`UnicodeEncodeError`). This affected request URLs, `Location` headers and links.
8. `deflate` responses were decoded only with the zlib wrapper; raw deflate failed.
9. Only the first `X-Robots-Tag` header was read.
10. The canonical was never resolved to an absolute URL, nor compared with the final URL.
11. Internal and external links were split on the exact host, so www vs apex and default ports caused mismatches.
12. JSON-LD `@type` detection recursed into only 5 keys.
13. SPA-shell detection matched only when `id="..."` was the first attribute.
14. robots.txt rules were listed but never evaluated per path and user agent, and the 4xx/5xx semantics were ignored.
15. The host-variant check never tested `https://host`.
16. Sitemaps:
    - Only 5 sitemaps and 5 children were read.
    - `.xml.gz` failed without `Content-Encoding`.
    - One broken child aborted its siblings.
17. The user-agent comparison flagged `g-recaptcha` as a challenge page.
18. `Accept-Language` was hard-coded to `it-IT` for every user agent.
19. `check_build.py`:
    - `foo-index.html` was matched as an index page.
    - `404.html` was missing from the shell files.
    - The canonical was never compared with the page URL.
    - The exit code was always 0.
    - A fragile `parents[2]` import.
20. `suggest.py`:
    - Italian `hl`/`gl` were the defaults.
    - The `--expand` alphabet lacked j, k, w, x and y.
    - Errors were returned as suggestions.
21. `analyze_gsc.py`:
    - `"1,234"` was parsed as 1.234.
    - File names were recognised only in Italian and English.
    - Column matching failed for Spanish, German and Portuguese exports.
    - The delimiter was fixed to `,`.
    - Compare exports used only the first column.
    - A short row raised `IndexError`.
    - `Filters.csv` was ignored.
22. The DNS check depended on `nslookup` and failed silently on Linux systems without it. It now uses `dig`, then `nslookup`, and reports when neither is available.

### Removed
- The 0.2.x evals and trigger runs. They referenced real third-party data and local paths. They are replaced by fixture-based evals that use fictional entities.

## 0.2.0 — 2026-10-03

### Added
- First public version (Italian): six skills (`seo-discovery`, `seo-build`, `seo-audit`, `seo-content`, `seo-entity-local`, `seo-monitor`), a shared knowledge base from Google Search Central and Search Engine Journal, and helper scripts in Python and JavaScript.
