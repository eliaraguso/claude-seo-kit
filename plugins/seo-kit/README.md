# seo-kit (plugin)

SEO for new and live websites, on any stack and for any site type, grounded in Google Search Central documentation (October 2026). The plugin is written in English and answers in your language.

## What gets installed

- `skills/`: six skills, each with a `SKILL.md` and, where needed, Python scripts (standard library only, Python 3.9+) and templates.
- `knowledge/`: the shared knowledge base. It has topic files with about 440 checks, each with a stable ID, a severity and a source. It also has the site archetypes, the conventions, a list of myths and deprecated advice, the generated `INDEX.md` and 15 framework/CMS adapters.
- `lib/seokit/`: shared code used by the scripts (HTTP, HTML parsing, robots.txt, sitemaps, DNS, Search Console exports).
- `evals/`: 7 eval cases for `claude plugin eval`, using fictional sites.

## The six skills

| Skill | Use it to |
|---|---|
| `/seo-kit:seo-discovery` | Create or update `SEO.md`, the site profile every other skill reads. Start here. |
| `/seo-kit:seo-build` | Apply SEO rules while building: foundations, new routes, build-output check, launch and migration checklists. |
| `/seo-kit:seo-audit` | Audit a site and get a prioritised, plain-language action plan in `seo-reports/`. |
| `/seo-kit:seo-content` | Write or rewrite page copy, titles, descriptions and content plans. |
| `/seo-kit:seo-entity-local` | Build a consistent identity (person or business) and local presence. |
| `/seo-kit:seo-monitor` | Turn Search Console exports into a periodic report. |

The skills also trigger on their own when a request matches.

## Files written into your project

- `SEO.md`
- `seo-reports/`

## Network use

- **Scripts:** they contact only the audited site (`seo_fetch.py`, and `analyze_gsc.py --check-urls` for the pages in your export) and Google's autocomplete endpoint (`suggest.py`).
- **Skills:** they may ask Claude to use the PageSpeed Insights or CrUX API, the GitHub public API and web search/WebFetch.
- There is no telemetry, and nothing is sent to the plugin author.

Full documentation, requirements, upgrade notes and limits: https://github.com/eliaraguso/claude-seo-kit#readme
