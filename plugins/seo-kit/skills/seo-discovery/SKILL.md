---
name: seo-discovery
description: Creates or updates a site's SEO profile (SEO.md in the project root) - site type and goal, audience, searches to win and the page answering each, identity of the person or business, profiles, area served, languages and markets, Search Console and Business Profile access, baseline, monitoring. First step before audits, content or SEO fixes, for new and live sites of any archetype (personal brand, professional services, local business, editorial, ecommerce, SaaS) and stack (Next.js, Nuxt, Angular, Astro, SvelteKit, WordPress, Shopify, static HTML). Use it when starting SEO work, planning a new site's pages, choosing which searches to target, or when another seo-kit skill finds no SEO.md.
when_to_use: |
  English: start SEO on my site; which searches should we target; create SEO.md; plan the pages of a new site; keyword and page map; migrate SEO.md to v2
  Italian: iniziare la SEO del sito; per quali ricerche farmi trovare; creare SEO.md; progettare le pagine di un sito nuovo; mappa parole chiave; profilo SEO
  Spanish: empezar el SEO de mi web; qué búsquedas atacar; crear SEO.md; planificar las páginas de una web nueva; mapa de palabras clave; perfil SEO
  German: SEO für meine Website starten; für welche Suchanfragen gefunden werden; SEO.md anlegen; Seiten einer neuen Website planen; Keyword-Map; SEO-Profil
  French: démarrer le SEO de mon site; sur quelles recherches me positionner; créer SEO.md; planifier les pages d'un nouveau site; carte des mots-clés; profil SEO
argument-hint: "[site URL or project path]"
---

# Site SEO profile

> **Working language.** Answer in the language of the user's message. Files written into the project (`SEO.md`, `seo-reports/*`) use the report language recorded in `SEO.md › 1. Site › Working language` (if `SEO.md` is missing, use the user's language and record it when creating `SEO.md`). Page copy (titles, descriptions, H1, body text, alt text) is always written in the site language(s) from `SEO.md › 1. Site › Languages and markets`. Check IDs, severities, JSON keys and script flags stay in English; report headings are translated.

This skill produces `SEO.md`: the SEO memory of the project. The other seo-kit skills read it to know what kind of site it is, who must find it, with which searches, and which page must answer. Without this context an audit checks generic rules; with it, it checks what matters for *that* site.

## Knowledge base
Files live in `${CLAUDE_PLUGIN_ROOT}/knowledge/` (if the variable is not expanded: the `knowledge/` folder two levels above this skill's folder). Read by tier, as defined in `conventions.md › Reading tiers`: for Tier 1, Grep the heading (e.g. `^## Build rules`) in the named file and Read only that section with offset/limit, up to the next `## ` heading. Never load a whole topic file for this skill.

| Tier | What to read | When |
|---|---|---|
| 0 | `conventions.md` (Working language, SEO.md v2, Archetypes with the legacy alias line, Fictional examples) | Always, at the start |
| 0 | `archetypes.md` (How to choose, the archetype's section, Modifiers, Priority matrix) | Always, at the start |
| 0 | `INDEX.md`: generated list of every check, one row per check (`ID`, `Severity`, `Check`, `Where` = `file#section`, `Alias of`); read the header, then Grep it for an ID or a word | Always, at the start; never edit it |
| 0 | `adapters/README.md › Detection table`, then only the matching `adapters/<stack>.md` | When code or live HTML is available |
| 1 | `entity-personal-brand.md › ## Build rules` | Identity, entity home, profiles (section 3) |
| 1 | `local-seo.md › ## Build rules` | Area served, service pages vs city pages |
| 1 | `content-quality-spam.md › ## Build rules` (no pages in series) | Page map (section 4) |
| 1 | `on-page-appearance.md › ## Build rules` (title and description: OP-02, OP-03, OP-08) | Title, description and H1 proposals |
| 1 | `international.md › ## Build rules` | More than one language or market |
| 1 | `ai-search.md › ## Procedures` ("Procedure: AI visibility with fixed questions") | Monitoring setup |
| 2 | `measurement.md › ### Branded queries filter and the brand / non-brand split`; any `## Facts and rules` subsection named in an INDEX line | Brand regex; when a rule needs explaining |
| 3 | `myths-deprecated.md` in full | Before recommending a tactic you are not sure is current |

If a rule is missing, fetch the Google URL in the Source column with WebFetch; there is no local copy of Google's pages.

The template of the file is `assets/SEO-template.md` in this skill's folder.

## Scripts
```bash
# Live site: pages, titles, sitemaps (no user-agent comparison; site language sent as Accept-Language)
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" https://northwind-physio.example --sitemap 50 --no-ua --json seo-fetch.json --lang en

# How people phrase searches (Google autocomplete; no volumes)
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-discovery/scripts/suggest.py" "physio oslo" "northwind physio" --lang en --expand
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-discovery/scripts/suggest.py" "back pain exercises" --lang en --gl no --json
```
On Windows use `py -3` (or `python`) if `python3` is not available. The scripts need Python 3.9+ and only the standard library.

- `seo_fetch.py` reads the raw server HTML (no JavaScript). Useful output: `pages[]` (`title`, `meta_description`, `h1`, `lang`, `hreflang`, `jsonld_types`, `internal_links`, `visible_text`) and `site.sitemaps`. Exit code 2 = invalid URL or site unreachable.
- `suggest.py`: `--hl`/`--gl` default from `--lang` (en → en/us, it → it/it, de → de/de, es → es/es, fr → fr/fr, pt → pt/br); pass `--gl` (and `--hl`) when the market differs from that default. `--expand` adds "query a".."query z", "query 0".."query 9" and the language's question words. Exit code 3 = rate-limited by Google: stop and retry later, do not loop.

## Procedure

### 1. Start from what exists
- **`SEO.md` v2 exists** (first line `# SEO profile`): read it and work in **update mode**. Ask only what has changed; do not rewrite decisions already taken.
- **`SEO.md` v1 exists** (first line `# Profilo SEO`, Italian, seo-kit 0.2.x): offer to migrate it to v2 and explain what changes; never rewrite it silently. If the user agrees:
  - keep sections 1-7 (headings translated into the working language), then map `8. Decisioni e vincoli` → `8. Decisions and constraints`, `8b. Monitoraggio` → `9. Monitoring`, `8c. Registro interventi` → `10. Change log` (add the `Skill` column, empty for old rows), `9. Storico audit` → `11. Audit history`;
  - map the archetype slugs with the alias table of `conventions.md › Archetypes`: `professionista-servizi` → `professional-services`, `attivita-locale` → `local-business`, `editoriale` → `editorial`, `prodotto-saas` → `saas-product` (`personal-brand` and `ecommerce` unchanged);
  - add the new v2 fields (Languages and markets, Working language, Adapter, Modifiers, IndexNow key) and ask for the values you cannot deduce;
  - keep the user's own notes and data as they are (translate them only if the user asks); show a short summary of what moved where.

  If the user declines, leave the file untouched: the other skills read v1 as is.
- **Gather everything you can before asking**, so the user answers only what cannot be deduced:
  - **project documentation** (README, CLAUDE.md, status notes, TODO, decision records, briefs, previous reports): goals, audience, deliberate choices (e.g. what not to publish), tools already set up;
  - **code**: detect the stack with the `adapters/README.md` detection table (the most specific signal wins) and read only that adapter; note framework and version, rendering mode, routing, existing pages and routes, titles and copy, structured data, contacts, languages;
  - **live site** (if any): run `seo_fetch.py` as in Scripts for pages, titles and sitemaps;
  - **About / contact page**: exact name, role, location, linked profiles.

### 2. Short interview
Ask grouped questions (at most 2-3 rounds), only about what is missing. Always propose a default answer deduced from the site, so the user can just confirm. Topics:
1. **Goal and conversion**: what should happen when a person lands on the site (contact, booking, CV download, purchase)?
2. **Audience**: who searches and in what situation (e.g. a recruiter hiring developers, a runner with a knee injury, a company looking for a supplier).
3. **Services / offer** and **area**: in person, online or both; which city or region.
4. **Identity**: exact name to use everywhere, official profiles, verifiable credentials, known homonyms.
5. **Languages and markets**: the site language(s) and the countries or regions served (e.g. `en-GB` primary, `de-DE` secondary). Page copy will be written in these languages.
6. **Working language**: the language for `SEO.md` and the reports in `seo-reports/` (default: the language of the conversation).
7. **Access**: Search Console (Domain property?), Business Profile, analytics, Bing Webmaster Tools, IndexNow.
8. **Competitors** that currently appear for the target searches (if the user knows them).

### 3. Archetype and stack
- Pick the primary archetype and any secondary ones with `archetypes.md › How to choose`, using the English slugs (`personal-brand`, `professional-services`, `local-business`, `editorial`, `ecommerce`, `saas-product`), and add the modifiers that apply (`multilingual`, `marketplace-ugc`, `paywall`, `app-and-site`). Explain the choice in one line: the archetype changes the order of audit priorities (`archetypes.md › Priority matrix`).
- Record the stack, the adapter slug, the rendering mode and the router in section 1. If no row of the detection table matches, write "unknown" and say that the audit will fall back to the topic files.
- More than one language or market → modifier `multilingual`; read `international.md › ## Build rules` before planning pages per language.

### 4. Search intents and page map
Build the intents table starting from the archetype:
- **brand**: the name of the person or business, also with role or city;
- **service**: how the audience describes the offer, in their words, not the industry jargon;
- **local**: service + area, only where there is a real presence in that area;
- **informational**: questions and problems the audience has before searching for the service.

Rules:
- **one page per intent**, and each page must have genuinely different content;
- no copy-paste pages per city or variant: Google treats them as doorways / spam (`content-quality-spam.md › ## Build rules`, `local-seo.md › ## Build rules`);
- if an intent has no page yet, mark it "to create" instead of inventing a URL;
- on a multilingual site, one row per language when the searches differ, each answered by the page in that language.

**Evidence of real demand.** Queries stay **assumptions** until there is data, but you can reduce the uncertainty:
- **Google autocomplete suggestions** (free, no volumes): `suggest.py` with `--lang` set to the site language (and `--gl` for the market), `--expand` for variants, `--json` to keep the output. They show how people phrase searches and which variants exist. A phrasing that appears is really used; its absence proves nothing (low volumes).
- **Who holds the results today**: if you have a web search tool, look at what comes up for the main queries and state which engine you used (a different engine, or a different country, is only a hint). Read the intent: if a search is dominated by job ads, portals or aggregators, the people making it want something else and the site will hardly compete. Otherwise ask the user to check in a private window on the Google domain of the target market.
- **Search Console**: if the user has access, ask for the query export (Performance → Queries, last 3-12 months): it is the best source.
- Google Trends and Google Ads Keyword Planner are free alternatives to compare phrasings. Never invent volumes.

**Queries not to chase.** Also list searches that look relevant but are not: different intent (e.g. people searching "physiotherapist jobs Oslo" want a job, not a clinic), names of other people or clients, topics the site has chosen not to cover, searches dominated by portals. This avoids wasted work and forced pages.

**Proposals for the pages.** For the main pages propose a title, a meta description and an H1, written in the site language with the audience's words and without keyword lists. Follow `on-page-appearance.md › ## Build rules` (title and description length: OP-02, OP-03, OP-08) or the project's own length check if it has one, and count the characters with a tool, not by eye. Google may rewrite titles, but a clear, specific title is the basis.

### 5. Monitoring setup
Fill `SEO.md › 9. Monitoring`, so that every `seo-monitor` run uses the same definitions:
- **Brand regex.** Derive it from the entity name and its aliases (section 3): the distinctive tokens only, plus the joined domain form and frequent misspellings (e.g. `northwind`; for a person `ada ?novak|novak ?ada|adanovak`). Exclude generic words: a service word (`physio`) or a bare common surname also matches searches by people who do not know the brand (`physio oslo`); those would be counted as brand and hide the real non-brand growth. Explain this choice to the user in one line. `analyze_gsc.py --brand` matches the regex case- and accent-insensitively; the same regex works in the Search Console query filter when the built-in branded filter is not available (`measurement.md › ### Branded queries filter and the brand / non-brand split`).
- **Three fixed AI questions**, written in the site language with the audience's words and never changed between runs: one **accuracy** question about the entity (e.g. "What is Northwind Physio in Oslo?"), one **decision** question without the name (e.g. "Which physiotherapist in Oslo treats running injuries?"), one **service** question (e.g. "Who offers home physiotherapy visits in Oslo?"). For sites with active PR or content work, extend the set as described in `ai-search.md › ## Procedures`.
- Leave the AI log table empty: `seo-monitor` fills it.

### 6. Write SEO.md
Fill `assets/SEO-template.md` and save it as `SEO.md` in the project root, in the working language, with today's date. Leave `{{...}}` only where the information is really missing, and list those gaps in the closing summary. Use only facts from the project, the site or the user; never invent people, credentials or numbers.

If the user has Search Console data, record the baseline in section 7 (clicks, impressions, brand queries, last 3 months): it is how the effect of later changes will be measured.

### 7. Close with the next steps
- Summarise in a few plain-language lines: archetype and modifiers, the 3-5 main searches and the page that answers each, pages to create, queries not to chase, missing information. If you noticed obvious problems while gathering (e.g. the domain variants do not redirect, profiles do not link the site), list them as leads for the audit.
- Suggest the next step: usually `seo-audit` if the site is live, `seo-build` if it is in development, `seo-entity-local` when identity or local presence is the main gap.
- **Change log step.** Before finishing, append one row to `SEO.md › 10. Change log` (date · change · pages/area · skill) for every file you created or modified in the project (e.g. `YYYY-MM-DD | SEO.md created (v2) | SEO.md | seo-discovery`, or `SEO.md migrated from v1 to v2`).

## Output format
Two outputs. Headings are translated into the working language; their order and meaning stay as below.
1. **`SEO.md`** in the project root, following `assets/SEO-template.md` (sections 1-11, v2).
2. **Closing summary** in the conversation (language of the user's message):
   - **In short**: archetype (+ modifiers), stack and adapter, languages and markets;
   - **Main searches → page**: 3-5 rows, "to create" where needed;
   - **Queries not to chase**;
   - **Missing information** (the remaining `{{...}}`);
   - **Leads for the audit**;
   - **Next step** (which skill).

## Things to keep in mind
- Identity must be **true and verifiable**: Google's policies forbid invented authors, credentials and reviews. If the user proposes to "inflate" something, explain the risk.
- Personal data: put in the profile only what is already public or what the user wants to make public (e.g. the home address of a professional who works at clients' homes: ask first).
- Queries are hypotheses until data confirms them; never invent search volumes or promise rankings or timelines.
- Write `SEO.md` in the working language; the titles, descriptions and H1 you propose are in the site language(s).
- Respect deliberate choices recorded in section 8 or in the project documentation.
