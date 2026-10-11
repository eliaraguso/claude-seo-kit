# Conventions

> Shared rules for every file in `knowledge/` and every skill of seo-kit. Read this at the start of any seo-kit task (Tier 0). Updated 2026-10-11.

## Severity (one scale, everywhere)

| Severity | Meaning |
|---|---|
| **Critical** | Blocks crawling or indexing, or exposes the site to spam policies / manual actions. |
| **High** | Strongly limits visibility: wrong canonical, empty server HTML, key content not in HTML, inconsistent entity data. |
| **Medium** | Measurable loss of clarity, click-through or trust; worth fixing in the next weeks. |
| **Low** | Minor, informational or accessibility-only; fix when convenient. |

No numeric scores, ever. Reports group findings by this scale. Legacy labels map as: critica/Critico → Critical · alta/Alto → High · media/Medio → Medium · bassa/Basso/Info → Low · "Priorità Alta/Media" → High/Medium.

## Markers and source tags

- **⚠** has exactly one meaning: *deprecated, unsupported by Google, or otherwise not to be recommended*. It never appears on a check we recommend. A recommended check that applies only under conditions gets a `Caveat:` sentence inside its "How to verify" cell instead.
- `[G](url)` Google documentation: Search Central documentation and blog, Merchant Center Help, Search Console Help, PageSpeed Insights and CrUX documentation (no separate `[PSI docs]`/`[CrUX docs]` tags) · `[G OH YYYY-MM](url)` Google Search Office Hours · `[GBP](url)` Google Business Profile Help · `[web.dev](url)` Google-authored web.dev guidance (not Search Central) · `[SEJ YYYY-MM]` Search Engine Journal (third-party view, evidence not rule), with the month when known, `[SEJ]` otherwise · `[Bing](url)` Bing Webmaster documentation · `[IndexNow](url)` IndexNow documentation · `[Docs vX](url)` framework or CMS documentation, with the version checked · *(inference)* a deduction no source states explicitly · *(re-verify)* a claim to confirm on the cited page (for Google, on the changelog `developers.google.com/search/updates`) before treating it as final.
- Hierarchy: Google documentation is primary. Third-party views are reported as views. Anything marked ⚠ or listed in `myths-deprecated.md` is never recommended.

## Check IDs

| Prefix | File | Prefix | File |
|---|---|---|---|
| CI | crawling-indexing.md | AI | ai-search.md |
| RJ | rendering-javascript.md | ME | measurement.md |
| OP | on-page-appearance.md | EC | ecommerce.md |
| SD | structured-data.md | IN | international.md |
| CQ | content-quality-spam.md | ED | editorial-news.md |
| EN | entity-personal-brand.md | PF | performance-cwv.md |
| LO | local-seo.md | SA | site-architecture.md |
| | | BI | bing-basics.md |

- IDs are **append-only**: never renumber, never reuse a retired number. New checks take the next free number in their prefix.
- One check lives in one owning file. If another file needs it, the row there reads `Alias of CI-17 — verify there, report once` with the same severity. `INDEX.md` marks such rows `alias→CI-17`.
- The audit-check table header is exactly: `| ID | Check | How to verify | Severity | Source |`. `tools/build_index.py` parses it; `tools/check_knowledge.py` fails on any other header.

## Topic file template

```
# <Title>
> Updated YYYY-MM-DD. Scope: <one line>. Primary source: Google Search Central; third-party views marked [SEJ].
## Contents
## Facts and rules (Google)
## Audit checks
## Build rules              (bullets that point to check IDs; they create no new IDs)
## Notes by site type      (fixed order: ecommerce · editorial · local-business · personal-brand · professional-services · saas-product; omit a type that has nothing specific)
## Third-party views
## Myths and outdated advice
```

`archetypes.md`, `conventions.md`, `myths-deprecated.md`, `INDEX.md` and `adapters/*` are exempt from this template. Files may add a `## Procedures` section (measurement, ai-search) or a `## Off-site checklist` (entity, local).

## Archetypes

Slugs (English, stable): `personal-brand` · `professional-services` · `local-business` · `editorial` · `ecommerce` · `saas-product`. Modifiers (not archetypes): `multilingual`, `marketplace-ugc`, `paywall`, `app-and-site`.

Legacy slugs from SEO.md v1 map as: professionista-servizi → professional-services · attivita-locale → local-business · editoriale → editorial · prodotto-saas → saas-product (personal-brand and ecommerce unchanged).

## Working language

1. Answer in the language of the user's message.
2. Files written into the user's project (`SEO.md`, `seo-reports/*`) use the **report language** recorded in `SEO.md › 1. Site › Working language`. If `SEO.md` is missing, use the user's language and record it when `SEO.md` is created.
3. Page copy (titles, descriptions, H1, body text, alt text) is always written in the **site language(s)** listed in `SEO.md › 1. Site › Languages and markets`, never in the conversation language.
4. Check IDs, severity words, JSON keys and script flags stay in English.

Report section headings are translated into the report language; their order and meaning follow the skill's template.

## SEO.md (v2)

Sections, numbered 1-11: 1 Site · 2 Site type and goal · 3 Entity · 4 Audience and search intents · 5 Competitors · 6 Access and tools · 7 Baseline · 8 Decisions and constraints · 9 Monitoring (brand regex, fixed AI questions) · 10 Change log · 11 Audit history. Template: `skills/seo-discovery/assets/SEO-template.md`.

- A file starting with `# Profilo SEO` is v1 (Italian, 0.2.x). Skills read it as is; `seo-discovery` offers to migrate it to v2 (sections 8/8b/8c/9 → 8/9/10/11, slugs per the alias table), never silently.
- **Change log rule:** any skill that creates or modifies a file in the user's project appends one row to `SEO.md › 10. Change log` (date · change · pages/area · skill). `seo-monitor` relies on it to explain variations.

## Reading tiers (context budget)

| Tier | What | When |
|---|---|---|
| 0 | `archetypes.md`, `conventions.md`, `INDEX.md`, the detected `adapters/<stack>.md` | Always, at the start |
| 1 | Only the `## Audit checks` (or `## Build rules`, `## Procedures`, `## Off-site checklist`) section of the relevant file, located with Grep on the heading and read with offset/limit | For each area being worked on |
| 2 | The `## Facts and rules` subsection named in the INDEX line | When a check fails or needs explaining |
| 3 | Whole file; `myths-deprecated.md` in full before writing recommendations | Rarely |

`INDEX.md` is generated by `tools/build_index.py` from the check tables. Never edit it by hand. If a rule is missing from the knowledge base, fetch the Google URL in the Source column with WebFetch; there is no local copy of Google's pages.

## Fictional examples

Use only these, consistently, in knowledge, skills, templates, tests and evals:

| Entity | Archetype | Language / place | Domain |
|---|---|---|---|
| Northwind Physio | local-business (+ professional-services) | en, Oslo | northwind-physio.example |
| Studio Ferri Orientamento | professional-services | it, Bologna | studioferri.example |
| Acme Widgets | ecommerce | en | acme-widgets.example |
| Ada Novak | personal-brand (developer) | en | adanovak.example |
| Daily Fjord | editorial | en | dailyfjord.example |

Never use real people, clients or real small businesses as examples.

## Dates and claims

- Every topic file starts with `> Updated YYYY-MM-DD`. Use absolute dates in the text ("since 15 June 2026"), never relative ones ("next month").
- Events already past are written in the past tense; re-check any date in the future at each knowledge refresh.
- Figures from third parties (percentages, sample sizes) are attributed and dated; never present them as Google rules.
- No promises of rankings or timelines beyond Google's own statements (weeks to months).
