---
name: seo-content
description: Writes and improves site copy so it is found on Google and cited by AI assistants without turning generic - service pages, home, About page, blog posts, case studies, titles, meta descriptions and H1, editorial plans. Starts from how people really search and from the author's first-hand experience; follows Google's rules on helpful and AI-generated content. Works for every archetype (personal brand, professional services, local business, editorial, ecommerce, SaaS), any stack or CMS, in any site language. Use it to write or rewrite a page or article, improve existing copy, decide what to write, build a content plan, or fix copy issues found by an audit.
when_to_use: |
  English: write a page; rewrite this article; improve the copy; title and meta description; what should I blog about; content plan; service page text; About page copy
  Italian: scrivere una pagina; riscrivere un articolo; migliorare i testi; title e meta description; di cosa scrivere nel blog; piano dei contenuti; testo pagina servizio
  Spanish: escribir una página; reescribir un artículo; mejorar los textos; title y meta description; sobre qué escribir en el blog; plan editorial
  German: Seite schreiben; Artikel überarbeiten; Texte verbessern; Title und Meta-Description; worüber bloggen; Redaktionsplan; Text für Leistungsseite
  French: écrire une page; réécrire un article; améliorer les textes; title et meta description; sur quoi écrire sur le blog; plan éditorial
argument-hint: "[page URL, file path or topic] [--plan]"
---

# Content for search

> **Working language.** Answer in the language of the user's message. Files written into the project (`SEO.md`, `seo-reports/*`) use the report language recorded in `SEO.md › 1. Site › Working language` (if `SEO.md` is missing, use the user's language and record it when creating `SEO.md`). Page copy (titles, descriptions, H1, body text, alt text) is always written in the site language(s) from `SEO.md › 1. Site › Languages and markets`. Check IDs, severities, JSON keys and script flags stay in English; report headings are translated.

Google rewards content written for people, that shows first-hand experience and answers a precise question well. Generic content, rewritten from other sources or produced in series (with AI or not) does not help and, at scale, is treated as spam. This skill helps write copy that someone in the field would recognise as useful, in the words the audience really uses.

## Knowledge base
Files live in `${CLAUDE_PLUGIN_ROOT}/knowledge/` (if the variable is not expanded: the `knowledge/` folder two levels above this skill's folder). Read by tier, as defined in `conventions.md › Reading tiers`: for Tier 1, Grep the heading in the named file and Read only that section with offset/limit, up to the next heading of the same level. Never load a whole topic file.

| Tier | What to read | When |
|---|---|---|
| 0 | `conventions.md`, `archetypes.md` (the site's archetype section) | Always, at the start |
| 0 | `INDEX.md`: generated list of every check, one row per check (`ID`, `Severity`, `Check`, `Where` = `file#section`, `Alias of`); read the header, then Grep it for an ID | Always; never edit it |
| 0 | The detected `adapters/<stack>.md` (detection table in `adapters/README.md`) | To know where titles, meta and copy live in the code or CMS |
| 1 | `content-quality-spam.md › ## Build rules` (helpful content, who/how/why, AI content, no pages in series) | Always |
| 1 | `on-page-appearance.md › ## Build rules` (title, description, H1, images, dates: OP-02, OP-03, OP-06, OP-08, OP-39) | Step 5 |
| 1 | `ai-search.md › ## Build rules` (what makes content citable, and what is myth) | Pages meant to be cited by assistants |
| 1 | `entity-personal-brand.md › ## Build rules` | Author, credentials, About page |
| 1 | `local-seo.md › ## Build rules` | Service pages and location pages without doorways |
| 1 | `structured-data.md › ## Build rules` (minimum JSON-LD per archetype; `Article` rows SD-19, SD-20) | Articles, case studies, author pages |
| 1 | `editorial-news.md › ## Build rules` | Blogs and news sites |
| 1 | `international.md › ## Build rules` | More than one site language or market |
| 2 | `content-quality-spam.md › ### Helpful, reliable, people-first content` (self-assessment questions); `international.md › ### Translated content quality`; `structured-data.md › ### Article / BlogPosting / NewsArticle` | Final check; translated pages; writing the markup |
| 3 | `myths-deprecated.md` in full | Before recommending a tactic you are not sure is current |

If a rule is missing, fetch the Google URL in the Source column with WebFetch; there is no local copy of Google's pages.

Read the project's `SEO.md` too: intents, audience, entity, languages and markets, queries not to chase. A file starting with `# Profilo SEO` is v1 (seo-kit 0.2.x): read it as is (archetype slugs per `conventions.md › Archetypes`; v1 sections 8b/8c/9 = v2 sections 9/10/11) and suggest `seo-discovery` to migrate it. If `SEO.md` is missing, ask the minimum (intent, audience, site language, conversion) or suggest running `seo-discovery` first.

## Scripts
```bash
# How the audience phrases its searches (Google autocomplete; no volumes)
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-discovery/scripts/suggest.py" "physio oslo" "how long does a sprained ankle take to heal" --lang en --expand

# Current page as served: title, description, H1, headings, full visible text, coverage of the audience's phrasings
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" https://northwind-physio.example/running-injuries --no-site --no-ua --full-text --lang en --terms "running injuries;knee pain" --json page.json
```
On Windows use `py -3` (or `python`) if `python3` is not available. The scripts need Python 3.9+ and only the standard library.

`suggest.py`: `--lang` is the site language (it sets `--hl`/`--gl`; override `--gl` for another market), `--json` for machine-readable output; exit code 3 = rate-limited, retry later. `seo_fetch.py`: `term_coverage` reports, per `--terms` entry, `in_title`, `in_description`, `in_h1`, `in_headings`, `text_count`.

## Procedure

### 1. Choose the intent and check what exists
- Each text answers **one intent** from the table in `SEO.md › 4` (or a new one you add there). If two pages answer the same question, merging them is better than letting them compete.
- Read the current page (if it exists: in the repository, the CMS, or with `seo_fetch.py`) and the related pages: do not repeat what is already elsewhere, link to it.
- No cloned "service + city" pages: a location page makes sense only with a real presence and different content (`local-seo.md › ## Build rules`).
- Note the site language and market of the page; on a multilingual site, check whether the page exists in the other languages.

### 2. Gather the material only the author has
This is what separates useful copy from generic copy, and it cannot be invented. Ask the user (grouping the questions) or derive it from their materials:
- real examples and cases (anonymised if needed), own numbers, common customer mistakes, what really happens in a session or a project;
- reasoned opinions, what they advise against and why, who the service is **not** for;
- true, verifiable credentials, method, prices or how prices are set.

If the user has no time, write a draft and mark with `[TO COMPLETE: …]` the points where their experience is needed, instead of filling them with generic sentences.

### 3. Use the audience's words
Run `suggest.py` in the site language (see Scripts). Suggestions show how people phrase their questions (not how many people ask). Use the relevant phrasings in the title, H1, subheadings and body, naturally: no keyword lists, no forced repetition. Keyword density is not a factor.

### 4. Write
- **Opening**: the answer or the main promise in the first lines; readers must understand at once whether they are in the right place.
- **Structure**: subheadings that say what the section contains; short paragraphs; lists where they help. There is no ideal length: as long as the intent needs.
- **Who / how / why**: who wrote it is clear (author with a profile page), how the content was produced when relevant, and its purpose is to help the reader.
- **Sensitive topics** (health, money, work, life choices): no promised outcomes, sources for data, a clear line between personal experience and general rules.
- **Call to action** consistent with the conversion in `SEO.md › 2` (contact, booking, download), without intrusive interstitials.
- **Internal links** to related pages with descriptive anchors, relevant blog posts included; also say which existing pages should link to the new one.
- **Site language**: write in the site language from `SEO.md › 1`, with correct spelling and accents (e.g. in Italian `è`, `perché`, `cos'è`; in German `ß` and umlauts), never in the conversation language unless they coincide.
- **Other languages** (`international.md`): each language version is written or reviewed by a native speaker; never publish machine translation without review (keep it `noindex` until reviewed); translate title, description, headings, alt text and structured data text too; a new language version must join the hreflang cluster (hand that to `seo-build`).

### 5. Prepare the elements for Google
- **Title**, **meta description** (one sentence that invites the click, specific to the page), **H1**: follow `on-page-appearance.md › ## Build rules` (OP-02, OP-03, OP-08) for length and form, or the project's own length check if it has one. Count the characters with a tool (e.g. `python3 -c "print(len('…'))"`), not by eye.
- **Date** visible ("Published … · updated …") for articles and case studies; change the date only for substantial edits (OP-39).
- **Structured data**: `Article` / `BlogPosting` with `author` referencing the profile page's `@id` (`structured-data.md › ## Build rules`, SD-19, SD-20); for blogs and news also `editorial-news.md › ## Build rules`. No `FAQPage` or `HowTo` to get rich results (retired).
- **Images**: real and relevant, with descriptive `alt` in the site language.

### 6. Final check
Reread the text with the self-assessment questions in `content-quality-spam.md › ### Helpful, reliable, people-first content`. In short:
- does it contain original information or experience that is not available elsewhere?
- does the reader leave satisfied, or have to search again?
- would an expert in the field consider it correct?
- are there unverifiable claims, vague credentials, promises?
- was it written for people or "to please Google"?

If the text was produced with AI, the author must check and approve it: list for the user the facts to verify.

### 7. Deliver
- Deliver in the project's format (Markdown content files, components, CMS): find where the copy lives in the repository (the adapter says where titles and meta are set) and propose the change there. If the copy lives in a CMS you cannot reach, deliver ready-to-paste text with field names.
- For an editorial plan use `assets/brief-template.md` (in this skill's folder) for each piece; save the briefs where the user prefers (e.g. `seo-reports/briefs/`).
- Update the intents table in `SEO.md › 4` (page that answers, status).
- **Change log step.** Before finishing, append one row to `SEO.md › 10. Change log` (date · change · pages/area · skill) for every file you created or modified in the project (e.g. `YYYY-MM-DD | Running-injuries page rewritten, new title and description | /running-injuries | seo-content`).

## Editorial plan
If the user asks "what should I write about": start from the intents without a page in `SEO.md › 4`, the questions customers really ask, autocomplete suggestions and, if available, Search Console queries with many impressions and few clicks (`seo-monitor`'s "Opportunities" table). Propose a few solid pieces (e.g. 1-2 a month) rather than many weak ones: content in series with little value is a risk, and consistency counts only if quality stays high. One brief per piece, in the working language, with title, description and H1 proposals in the site language.

## Output format
Headings are translated into the working language; their order and meaning stay as below.
- **Page or article**: the copy in the site language, in the project's format, followed by: **Elements for Google** (title with character count, meta description, H1, structured data, images) · **Internal links** (to add and to receive) · **To verify before publishing** (facts, figures, credentials, `[TO COMPLETE: …]` points).
- **Editorial plan**: a short table (priority · intent · page type · target URL · reason) plus one `assets/brief-template.md` per piece.

## Things to keep in mind
- Never invent experience, cases, numbers, credentials or reviews: mark the gap instead.
- No promises of rankings, traffic or AI citations; Google's own timelines are weeks to months.
- Respect the queries not to chase and the deliberate choices in `SEO.md › 8`.
- Page copy in the site language; notes, briefs and summaries in the working language.
