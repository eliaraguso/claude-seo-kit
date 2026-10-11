# seo-kit

A Claude Code plugin that brings SEO into the everyday work on a website, from the first line of code to monitoring after launch. It works on new and live sites, for any site type and any stack. Its rules come from Google Search Central documentation. Outdated or "hype" advice is marked and never recommended: for example `llms.txt` as a lever for Google, or FAQ markup for rich results.

## What it does

seo-kit adds six skills to Claude Code. They share a profile of your site (`SEO.md`) and a knowledge base of about 440 checks with stable IDs and sources. You can ask for an audit, a set of build rules, page copy, an identity and local-presence plan, or a monthly report. Each answer cites Google's own documentation and is written in plain language.

| Skill | When to use it | What it produces |
|---|---|---|
| `seo-discovery` | First, on a new or live site: site type and goal, searches to win, identity, access | `SEO.md`: profile, search intents and the page that answers each, entity, access and tools, baseline, monitoring setup |
| `seo-build` | While building: project foundations, new pages or routes, deploys, launch and migrations | Code changes and checks; `check_build.py` verifies the build output (exit code usable in CI) |
| `seo-audit` | To find out what to fix and in which order, before or after launch | `seo-reports/YYYY-MM-DD-audit.md`: a plain-language action plan with ready-to-paste copy, code fixes and a technical appendix |
| `seo-content` | To write or rewrite pages, service pages, articles, titles, descriptions and H1, or to plan content | Ready-to-use copy in the site language and content briefs (e.g. `seo-reports/briefs/`) |
| `seo-entity-local` | For a consistent identity of a person or business, and for local presence (Business Profile, Bing Places, reviews) | `seo-reports/YYYY-MM-DD-identity.md`: texts for each platform, JSON-LD with `@id`/`sameAs`, an off-site checklist |
| `seo-monitor` | To see how things went, from Search Console exports | `seo-reports/YYYY-MM-DD-monitor.md`: brand vs non-brand, pages, new and lost queries, AI-assistant visibility, next actions |

## Who it is for

**Any site type.** The knowledge base is organised around six archetypes: `personal-brand`, `professional-services`, `local-business`, `editorial`, `ecommerce` and `saas-product`. Four modifiers can apply on top of any archetype: `multilingual`, `marketplace-ugc`, `paywall` and `app-and-site`. A site can have a primary and a secondary archetype, for example a physiotherapy clinic that is both local-business and professional-services.

**Any stack.** The skills detect the framework or CMS and read one adapter file for it. The adapter says where titles, canonicals, robots meta, sitemaps and true 404s live in that stack. There are 15 adapters:

Angular · Next.js / React (including Vite React SPAs) · Nuxt / Vue · Astro · SvelteKit · Remix / React Router · Gatsby · static site generators (Hugo, Jekyll, Eleventy) · static HTML · classic server-side frameworks (Django, Laravel, Rails) · WordPress (including WooCommerce) · Shopify · Drupal · Joomla · hosted builders (Webflow, Wix, Squarespace).

## Language

The plugin itself, its knowledge base and its scripts are written in English. You can talk to it in any language:

- Claude **answers in the language of your message**.
- Files written into your project (`SEO.md`, `seo-reports/*`) use the **report language** recorded in `SEO.md`.
- Page copy (titles, descriptions, headings, body text, alt text) is always written in the **site language(s)**, never in the conversation language.
- Check IDs, severity words, JSON keys and script flags stay in English.

## Install

From a terminal:

```
claude plugin marketplace add eliaraguso/claude-seo-kit
claude plugin install seo-kit@seo-kit-marketplace
```

Or from inside a Claude Code session:

```
/plugin marketplace add eliaraguso/claude-seo-kit
/plugin install seo-kit@seo-kit-marketplace
```

To update to the latest version:

```
claude plugin marketplace update seo-kit-marketplace
claude plugin update seo-kit@seo-kit-marketplace
```

### Upgrading from 0.2.x

Version 1.0 is a breaking release; see [CHANGELOG.md](CHANGELOG.md). To upgrade, run the two update commands above, then restart Claude Code.

- An existing `SEO.md` from 0.2.x (Italian, starting with `# Profilo SEO`) is version 1. The skills still read it as it is.
- `seo-discovery` offers to migrate it to version 2, with English section names and archetype slugs. It always asks first and never migrates silently.
- Your existing reports in `seo-reports/` are left untouched.

## Requirements

- [Claude Code](https://docs.claude.com/en/docs/claude-code).
- Python 3.9 or later. The scripts use only the standard library, so there is nothing to `pip install`. On Windows, if `python3` is not available, the skills use `py -3` (or `python`).
- Optional: a browser MCP server (for example Chrome DevTools MCP) for rendered-DOM checks and Lighthouse/performance traces. Without it, the audit uses the server HTML and the PageSpeed Insights API.
- Optional: `dig` or `nslookup`, for DNS details: nameservers (for example a CDN in DNS-only mode) and TXT records (for example a Search Console verification). Without them, those checks are reported as unavailable.

## Usage

1. Open Claude Code in your site's project folder (or any folder, for a live site you only have a URL for).
2. Start with `/seo-kit:seo-discovery`. It creates `SEO.md`, the SEO memory of the project: profile, searches, decisions, baseline and change log.
3. Then use the others as needed: `/seo-kit:seo-audit`, `/seo-kit:seo-build`, `/seo-kit:seo-content`, `/seo-kit:seo-entity-local` and `/seo-kit:seo-monitor`.

The skills also trigger on their own when a request matches. For example: "why is my site not on Google?", "I added an /about page", "write the service page", "how did last month go?" or "il sito non esce su Google". If a skill finds no `SEO.md`, it suggests running `seo-discovery` first.

## What the plugin writes into your project

- **`SEO.md`** in the project root: the site profile, in 11 numbered sections. Every skill that changes a file in your project appends one row to `SEO.md › 10. Change log`, and `seo-monitor` uses it to explain changes in traffic.
- **`seo-reports/`**: dated reports (`YYYY-MM-DD-audit.md`, `-identity.md`, `-monitor.md`) and content briefs.
- Script outputs you ask for with `--json` (for example `seo-fetch.json`). They are working files that you can delete.
- When you ask for fixes, the skills edit your source files the way any Claude Code session does, with your usual permission prompts.

Nothing is written outside the project folder.

## Network use

**Calls the scripts make themselves:**

- **`seo_fetch.py` contacts the site being audited.** It requests:
  - the pages, `robots.txt` and the sitemaps;
  - the host variants (http/https, www/apex);
  - one made-up URL, to test the 404 status.
- **It compares user agents.** What a browser user agent receives is compared with what a Googlebot-like, a Bingbot-like and AI-bot-like user agents (OAI-SearchBot, Claude-SearchBot, PerplexityBot by default) receive. Requests are spaced by a delay (1 second by default), and 429/503 responses honour `Retry-After`.
- **It runs DNS lookups.** The optional `dig`/`nslookup` lookups (nameservers, TXT records) use your system resolver.
- **`suggest.py` calls Google autocomplete.** It uses Google's undocumented suggest endpoint `suggestqueries.google.com` for query research, and stops at the first rate-limit response.
- **`analyze_gsc.py --check-urls` checks the pages in your export.** It requests every page URL listed in your Search Console export to report its current HTTP status, 1 second apart. Without `--check-urls` it makes no network calls.
- **`check_build.py` makes no network calls.** It reads only the build output on disk.

**Calls the skills may ask Claude to make with its own tools** (WebFetch, web search, a browser MCP). These go through Claude Code's usual permission prompts:

- **PageSpeed Insights API** (`googleapis.com/pagespeedonline`) or the **CrUX API**, for performance data when no browser MCP is available.
- **GitHub public API** (`api.github.com/users/<name>`), when the identity includes a GitHub account.
- **Web search and WebFetch**: Google documentation pages when a rule is missing from the knowledge base, public profiles of the person or business, and current results for the main queries in `seo-discovery`, if a web search tool is available.

There is no telemetry, and nothing is sent to the plugin author.

## Knowledge base

The rules live in `plugins/seo-kit/knowledge/`, one file per topic. The sources are:

- **Google Search Central documentation**: 312 pages, selected and read in October 2026. The list is in [`sources/google-search-central/urls.txt`](sources/google-search-central/urls.txt).
- Bing Webmaster documentation, web.dev, Google Business Profile Help and Merchant Center Help, where a check cites them.
- **Search Engine Journal** articles from October 2025 to October 2026, as a secondary, dated source. These are reported as third-party views, never as rules.

All files were refreshed on **2026-10-11**; the date is at the top of each file.

Each topic file has an audit-check table with stable IDs (`CI-01`, `SD-12`…), a severity and a source link. `INDEX.md` is generated from those tables by `tools/build_index.py`, never by hand. It lists every check in one line, so a skill can find the right check without reading whole files. Severities use one scale everywhere: **Critical**, **High**, **Medium**, **Low**. There are no numeric scores. The **⚠** marker has exactly one meaning: deprecated, unsupported by Google, or otherwise not to be recommended. A check that applies only under conditions carries a `Caveat:` instead. The binding rules are in [`knowledge/conventions.md`](plugins/seo-kit/knowledge/conventions.md).

## Context size

The skills read the knowledge base in tiers. Tier 0 is always read at the start: `archetypes.md`, `conventions.md`, `INDEX.md` and the one adapter for the detected stack. It is about **90 KB**, of which `INDEX.md` is about 62 KB. Topic files are read section by section, only for the area being worked on, using Grep and offset reads. A whole file is read only rarely.

## Development

```
git clone https://github.com/eliaraguso/claude-seo-kit.git
cd claude-seo-kit
claude --plugin-dir plugins/seo-kit        # run Claude Code with the working copy of the plugin
```

| Task | Command |
|---|---|
| Unit tests (no network, standard library) | `python -m unittest discover -s tests -v` |
| Knowledge lint | `python tools/check_knowledge.py` |
| Rebuild the knowledge index | `python tools/build_index.py` (`--check` fails if `INDEX.md` is stale) |
| Skill evals (7 cases) | `claude plugin eval plugins/seo-kit --scaffold --allow-tools Bash Write Edit "WebFetch(domain:127.0.0.1)"` |
| Trigger test | `python tools/trigger_test.py --dry-run`, then `python tools/trigger_test.py --runs 2 --workers 4` |

- **Evals.** The 7 cases in `plugins/seo-kit/evals/cases/` cover the six skills, in English, Italian and German. Each case runs a request on a small fixture project or Search Console export.
  - Every case uses fictional businesses and `.example` domains.
  - Graders check the skill and tools used, the files written and what the report says; an LLM rubric judges plain-language quality.
  - `--scaffold` copies each fixture into the run workspace. The shell commands run in Claude Code's OS sandbox (macOS, Linux, or WSL2 on Windows).
  - Results go to `plugins/seo-kit/evals/results/`, which is gitignored.
  - Every run is a real Claude Code session and costs tokens.
  - Options, cost and how to add a case: [`plugins/seo-kit/evals/README.md`](plugins/seo-kit/evals/README.md).
- **Trigger test.** For each query in `tools/trigger-queries.json` (English and Italian requests per skill, plus negatives), it starts `claude -p` in a new temporary folder with `--plugin-dir plugins/seo-kit`. It records which skill fires.
  - The summary is printed as Markdown; the full results go to `tools/trigger-runs/`, which is gitignored.
  - Real runs are billable, so start with `--dry-run`.
  - `--only seo-content,none` limits the run to some skills; `none` means the negative queries.
- **CI.** GitHub Actions runs the unit tests on Ubuntu, Windows and macOS with Python 3.9 to 3.13. A lint job checks `extract_dom.js` syntax, validates the manifests, checks that the index is up to date and runs the knowledge lint.
- **Releases.** Raise `version` in `plugins/seo-kit/.claude-plugin/plugin.json` and add a [CHANGELOG.md](CHANGELOG.md) entry.

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for how to propose knowledge changes and adapters.

## Repository layout

```
.claude-plugin/marketplace.json   marketplace manifest
.github/workflows/ci.yml          tests (3 OS x Python 3.9-3.13) and lint
plugins/seo-kit/                  the plugin (what gets installed)
  .claude-plugin/plugin.json      plugin manifest
  skills/<skill>/                 SKILL.md, scripts/ and assets/ of each skill
  knowledge/                      topic files, archetypes, conventions, myths, INDEX.md
  knowledge/adapters/             one file per framework, CMS or host
  lib/seokit/                     shared standard-library code used by the scripts
  evals/                          eval cases with fictional fixture sites
docs/                             contributor guide, knowledge style guide, page schema of seo_fetch
sources/                          research notes, the list of Google pages read and the research fetch scripts (not shipped)
tests/                            unit tests and byte-exact fixtures
tools/                            index builder, knowledge lint, trigger test
```

The full texts downloaded during research (Google pages, Search Engine Journal articles) stay local and are not redistributed. Only the URL lists and the notes are committed.

## Limits

- No skill guarantees rankings or timelines. The skills remove obstacles and improve your chances; Google itself talks of weeks to months.
- Search Console, Business Profile and analytics need access that Claude does not have. The skills guide you through them, or work from exports that you download.
- Search changes. The knowledge base is dated 2026-10-11 and should be refreshed every few months, re-checking Google's changelog (`developers.google.com/search/updates`) and any item marked *(re-verify)*.
- The Google autocomplete endpoint is undocumented and may change, be rate-limited or return nothing.

## Disclaimer

seo-kit is an independent project. It is not affiliated with, endorsed by or sponsored by Google, Microsoft, Anthropic or Search Engine Journal. Google, Search Console, Business Profile, Bing, Claude and the other names mentioned are trademarks of their respective owners. The plugin summarises and links public documentation and does not reproduce it.

## License

[MIT](LICENSE)
