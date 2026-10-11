# Page schema

Shared page-level keys produced by the seo-kit scripts:

- **Python**: `seokit.html.parse_page()` on the raw server HTML. It is used by `skills/seo-audit/scripts/seo_fetch.py` (each item of `pages`) and by `skills/seo-build/scripts/check_build.py` (each generated file).
- **JS**: `skills/seo-audit/scripts/extract_dom.js`, which runs in a browser on the rendered DOM after JavaScript.

Compare the two outputs key by key to find content that only appears after rendering. "yes" means the key is present and computed. "null" means the key is present but always `null`, because that source cannot see it. "no" means the key is absent.

`tests/test_extract_dom_schema.py` checks that every key marked "yes" or "null" in the JS column appears in `extract_dom.js`.

## Page keys

| Key | Type | Python | JS | Notes |
|---|---|---|---|---|
| `title` | list of str | yes | yes | Every `<title>` outside `<svg>`/`<math>`. More than one is a finding. |
| `meta_description` | list of str | yes | yes | Every `<meta name="description">`, whitespace collapsed. |
| `robots_meta` | dict name → list of str | yes | yes | Keys present only for `robots`, `googlebot`, `bingbot`, `googlebot-news`. |
| `x_robots_tag` | list of str | yes | null | Every `X-Robots-Tag` header, in order. Headers are not visible from the DOM. |
| `indexable` | `{value: bool, reasons: [str]}` | yes | yes | Python: HTTP status, meta robots/googlebot, X-Robots-Tag (all and googlebot); `seo_fetch.py` adds robots.txt blocking. JS: meta tags only. |
| `canonical` | object | yes | yes | `{href, resolved, self_referencing, in_body, count, all}`. `resolved` is absolute (honours `<base>`). `self_referencing` compares with the final URL after normalising the trailing slash and the default port. `in_body` is true when the only canonical is in `<body>` (Google ignores it). |
| `hreflang` | list of object | yes | yes | `{lang, href, resolved, valid_code}`. `valid_code` rejects malformed codes and frequent mistakes (`en-UK`, `jp`, `cn`...). |
| `hreflang_issues` | list of object | yes | yes | `{issue, detail}`; issue ∈ `invalid_code`, `duplicate_code`, `missing_self_reference`. Return links are checked across pages by `seo_fetch.py` (`hreflang_return_issues`). |
| `lang` | str or null | yes | yes | `<html lang>`. |
| `viewport` | str or null | yes | yes | Content of the first `<meta name="viewport">`. |
| `og` | dict | yes | yes | `og:*` properties; first value wins. |
| `twitter` | dict | yes | yes | `twitter:*` names; first value wins. |
| `h1` | list of str | yes | yes | Text without `<svg>`/`<math>` content. |
| `headings` | list of `{level, text}` | yes | yes | All h1–h6 in document order. |
| `heading_skips` | list of `{from, to, text}` | yes | yes | Level jumps such as h1 → h3. |
| `internal_links` | list of object | yes | yes | `{href, resolved, text, rel, nofollow}`. Internal means the same host, ignoring `www.` and the default port. Subdomains are external. |
| `external_links` | list of object | yes | yes | Same shape as `internal_links`. |
| `other_links` | dict scheme → count | yes | yes | `mailto:`, `tel:`, `sms:`, `whatsapp:`, `javascript:`, `data:`, `ftp:` and any other non-http scheme, plus `fragment` for `#...` links. The scheme check is case-insensitive. |
| `anchors_without_href` | int | yes | yes | `<a>` elements without `href`. |
| `images` | list of object | yes | yes | `{src, resolved, alt, alt_empty, width, height, loading, lazy_attr}`. `alt` is null when the attribute is missing. `lazy_attr` is the first of `data-src`, `data-lazy-src`, `data-original`, `data-srcset`, `data-lazy`. JS `resolved` is `currentSrc`. |
| `images_without_alt` | int | yes | yes | Images with no `alt` attribute (an empty `alt=""` is valid for decorative images). |
| `documents` | list of str | yes | yes | Linked PDF/DOC/PPT/XLS/ODF/RTF files (absolute). |
| `jsonld` | list | yes | yes | Parsed JSON-LD blocks (also blocks recovered leniently). |
| `jsonld_errors` | list of `{index, error, recovered}` | yes | yes | `recovered: true` means the block only parsed after relaxing the rules (literal newline in a string, trailing comma, HTML comment/CDATA wrapper). Google may reject such blocks, so fix them. |
| `jsonld_types` | list of str | yes | yes | Every `@type` at any depth, including inside `@graph`, `offers` and `address`. |
| `microdata_present` | bool | yes | yes | Any `itemscope`/`itemtype`. |
| `rdfa_present` | bool | yes | yes | Any `vocab`/`typeof`. |
| `visible_text` | str | yes | yes | Python: text outside `<head>`, `<script>`, `<style>`, `<noscript>`, `<template>`, `<svg>`, `<math>`. JS: `document.body.innerText`. `seo_fetch.py` cuts it to 1,500 characters unless you pass `--full-text`. |
| `visible_text_chars` | int | yes | yes | Length of `visible_text` before any cut. |
| `main_text_chars` | int | yes | yes | Like `visible_text_chars`, without `<nav>`, `<header>`, `<footer>`, `<aside>`. |
| `spa_shell_suspect` | bool | yes | null | Raw HTML only: `main_text_chars < 300` and a root container (`id` root/app/__next/___gatsby/__nuxt/svelte/q-app or tag `app-root`/`app`) with at most 3 child elements. |
| `spa_root` | str or null | yes | no | Root container found, such as `div#root` or `app-root`. |
| `head_invalid_tags` | list of str | yes | null | Elements in `<head>` that the HTML parser moves to `<body>`. Meta tags after them may be ignored. `<noscript>`/`<template>` content does not count. The browser has already moved these elements, so the DOM cannot show this. |
| `base_href` | str or null | yes | yes | Resolved `<base href>`. |
| `meta_refresh` | str or null | yes | no | Content of `<meta http-equiv="refresh">`. |
| `icons` | list of object | yes | no | `<link rel~="icon">`: `{rel, sizes, href}`. |
| `parse_error` | str | when it happens | no | Present only if the HTML parser raised an error. |
| `clickable_non_links` | `{count, sample}` | no | yes | Elements with `routerlink`, `to`, `data-sveltekit-preload-data`, `onclick` or `role="link"` that are not `<a href>`. These are hints of navigation that crawlers cannot follow. |
| `css_background_images` | `{count, sample}` | no | yes | Elements with a CSS background image, from same-origin stylesheet rules and inline styles. Google does not index CSS background images. |
| `hash_routing_links` | list of str | no | yes | Links whose `href` starts with `#/` or `#!` (hash routing: not crawlable URLs). |
| `hidden_text_containers` | list of object | no | yes | Candidate containers (`hidden`, `aria-hidden`, collapse/tab/accordion classes) with 100 characters or more of hidden text. `getComputedStyle` is called only on these candidates. |

## Keys added by `seo_fetch.py` to each page

| Key | Type | Notes |
|---|---|---|
| `url`, `final_url` | str | Requested URL and URL after redirects. `extract_dom.js` returns `location.href` for both. |
| `status`, `chain` | int, list | `chain` items are `{url, status, location}`, with at most 10 redirects. |
| `content_type`, `bytes`, `transfer_bytes`, `over_2mb` | | `bytes` is the decoded size. `over_2mb` flags pages larger than the 2 MB that Googlebot reads. |
| `encoding`, `encoding_source` | str | `encoding_source` ∈ `header`, `meta`, `bom`, `fallback`. |
| `truncated`, `error`, `fetch_warnings`, `elapsed_ms` | | Network errors appear in `error` and never stop the run. |
| `server`, `cdn`, `link_header` | | CDN detected from response headers. |
| `robots_txt_allowed` | dict crawler → bool, or null | robots.txt verdict for each crawler token in `seokit.bots.BOT_TOKENS`. |
| `typo_suspects` | list | Present only when a typo pack exists for `--lang` or the page `lang` (packs: `it`, `en`). |
| `term_coverage` | dict term → object | With `--terms`: `{in_title, in_description, in_h1, in_headings, text_count}`. Matching is case-insensitive (casefold) and respects word boundaries. |
| `not_html` | bool | The response is not HTML. Only the fetch keys are present. |

## Site-level keys of `seo_fetch.py` (under `site`)

| Key | Notes |
|---|---|
| `site.robots` | `{url, status, final_url, error, status_semantics, content_type, bytes, over_500kib, html_suspect, groups, sitemaps, invalid_lines, verdicts_root, note}`. `status_semantics` (the robots status semantics) ∈ `parse`, `allow_all` (4xx), `unavailable` (5xx, 429, no response). |
| `site.sitemaps` | `{sitemaps: [...], total_urls}`; each item has `url_count`, `files`, `errors`, `warnings`, `truncated`, `host_mismatch_count`, `host_mismatch_sample`, `sample_urls`. |
| `site.host_variants` | `{variants: [{url, status, hops, final_url, chain, error}], all_reach_same_final_url, final_urls, multi_hop}`. `www.` variants are tried only for a registrable domain. |
| `site.not_found_probe` | `{url, status, final_url, hops, verdict, error}`; verdict ∈ `ok`, `soft_404`, `soft_404_redirect_to_home`, `server_error`, `other`, `error`. |
| `site.dns` | `seokit.dns.summary()`: `{domain, nameservers, txt, cloudflare_dns, txt_verifications, google_domain_property_likely}`. |
| `site.ua_comparison` | `{url, results: {ua: {status, final_url, hops, bytes, title, main_text_chars, challenge_markers, error}}, differences, note}`. |
