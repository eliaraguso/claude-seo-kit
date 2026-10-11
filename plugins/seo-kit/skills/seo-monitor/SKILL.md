---
name: seo-monitor
description: Measures a site's SEO results over time and writes a periodic plain-language report - analyses Google Search Console exports (clicks, impressions, brand vs non-brand queries, pages, new and lost queries), compares them with the baseline and the previous period, links changes to the work done, checks visibility in AI assistants with fixed questions and suggests next actions. For any archetype and stack; exports in English, Italian, German, Spanish, Portuguese or French. Use it when the user asks how the site is doing, whether changes worked, why traffic dropped, wants a monthly report, has downloaded Search Console data or wants a recurring check.
when_to_use: |
  English: how is my site doing; did the changes work; why did traffic drop; monthly SEO report; analyse Search Console export; brand vs non-brand; recurring SEO check
  Italian: come sta andando il sito; le modifiche hanno funzionato; calo di traffico; report SEO mensile; analizzare export Search Console; controllo ricorrente
  Spanish: cómo va mi web; han funcionado los cambios; caída de tráfico; informe SEO mensual; analizar exportación de Search Console; control SEO periódico
  German: wie läuft meine Website; haben die Änderungen gewirkt; Traffic-Einbruch; monatlicher SEO-Bericht; Search-Console-Export auswerten; regelmäßiger SEO-Check
  French: comment va mon site; les changements ont-ils marché; baisse de trafic; rapport SEO mensuel; analyser l'export Search Console; suivi SEO régulier
argument-hint: "[current export .zip or folder] [previous export] [--brand REGEX]"
---

# SEO monitoring

> **Working language.** Answer in the language of the user's message. Files written into the project (`SEO.md`, `seo-reports/*`) use the report language recorded in `SEO.md › 1. Site › Working language` (if `SEO.md` is missing, use the user's language and record it when creating `SEO.md`). Page copy (titles, descriptions, H1, body text, alt text) is always written in the site language(s) from `SEO.md › 1. Site › Languages and markets`. Check IDs, severities, JSON keys and script flags stay in English; report headings are translated.

SEO results take weeks or months and come with a lot of noise: without a recorded starting point and a log of changes it is impossible to tell what worked. This skill turns Search Console data (and, when available, analytics and Bing) into a few clear answers: how it went, probably why, what to do next.

## Knowledge base
Files live in `${CLAUDE_PLUGIN_ROOT}/knowledge/` (if the variable is not expanded: the `knowledge/` folder two levels above this skill's folder). Read by tier, as defined in `conventions.md › Reading tiers`: Grep the heading in the named file and Read only that section with offset/limit, up to the next heading of the same level. Never load a whole topic file.

| Tier | What to read | When |
|---|---|---|
| 0 | `conventions.md`, `archetypes.md` (the site's archetype: what counts as a conversion) | Always, at the start |
| Lookup | `INDEX.md`: generated list of every check, one row per check (`ID`, `Severity`, `Check`, `Where` = the owning `file.md#audit-checks`, `Alias of`); Grep it for ME- IDs or a keyword, never read it in full | To look up a check ID; never edit it |
| 0 | The detected `adapters/<stack>.md` | Only if a technical cause is suspected |
| 1 | `measurement.md › ## Procedures` ("diagnosing a traffic drop", "exporting Search Console data", "measuring visibility in AI assistants") | Always |
| 1 | `measurement.md › ## Audit checks` (ME- rows) | Checking the measurement setup |
| 1 | `ai-search.md › ## Procedures` ("AI visibility with fixed questions") | Step 4 |
| 2 | `measurement.md › ### Data reliability and limits` (impressions bug 13 May 2025 – 27 April 2026, anonymised queries, delays), `› ### Expected timings`, `› ### Branded queries filter and the brand / non-brand split`, `› ### Generative AI performance report` | Interpreting the numbers |
| 3 | `myths-deprecated.md` in full | Before recommending a fix you are not sure is current |

If a rule is missing, fetch the Google URL in the Source column with WebFetch; there is no local copy of Google's pages.

Read `SEO.md`: baseline (section 7), intents (4), entity (3), monitoring (9: brand regex, fixed AI questions, AI log), change log (10), audit history (11). A file starting with `# Profilo SEO` is v1: read it as is (v1 sections 8b/8c/9 = v2 sections 9/10/11) and suggest `seo-discovery` to migrate it.

## Scripts
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-monitor/scripts/analyze_gsc.py" current.zip \
  --previous previous.zip --brand "northwind" --check-urls --json gsc.json
```
On Windows use `py -3` (or `python`) if `python3` is not available. The scripts need Python 3.9+ and only the standard library.

Flags: `export` (positional: `.zip` or unzipped folder of the current period) · `--previous PATH` (previous period; not needed for a "Compare" export, which holds both periods) · `--brand REGEX` (matched case- and accent-insensitively) · `--check-urls` (current HTTP status of the pages in the data) · `--json PATH` (also write JSON) · `--top N` (rows per table, default 15) · `--min-impressions N` and `--max-ctr X` (opportunities: at least N impressions, CTR below X percent; defaults 20 and 2.0). Exit codes: 0 done · 2 usage error (unreadable export, invalid `--brand` regex).

The Markdown output has: Summary · Key numbers · Brand vs non-brand · Top queries · Top pages (with current HTTP status under `--check-urls`) · Opportunities (high impressions, low CTR) · New and lost queries · Changes vs previous period · Data limits.

## Procedure

### 1. Get the data
Claude cannot access Search Console by itself (unless the user has set up a connector). Ask the user, following `measurement.md › ## Procedures` ("exporting Search Console data"):
1. **Search Console → Performance → Search results**, search type **Web**, a period (e.g. last 28 days or last 3 months), then **Export → Download CSV**: a `.zip` with queries, pages, countries, devices, search appearance, dates and filters.
2. For the comparison, the same export for the previous period of equal length (or use "Compare" in the interface, then export: one file holds both periods). Keep the same filters on both.
3. Optional: the **Pages** (indexing) report, the **generative AI** performance report (impressions only), Bing Webmaster Tools **AI Performance**, conversion events from analytics.

**Localisation note**: Search Console names the CSV files and columns in the account language, so file names and headers vary. `analyze_gsc.py` recognises exports in English, Italian, German, Spanish, Portuguese and French, separated by `,` or `;` (tabs and Excel re-saves too). For any other language, ask the user to switch the Search Console interface to English before exporting. Do not commit exports to version control.

### 2. Analyse
- Take the brand regex from `SEO.md › 9. Monitoring` and pass it to `--brand`, so every report uses the same split. If it is missing, derive it as `seo-discovery` does (distinctive tokens of the name only, e.g. `northwind`; never generic service words such as `physio`, which match people who do not know the brand), use it, and record it in section 9.
- Run `analyze_gsc.py` as in Scripts. With `--check-urls` the script checks the current status of the pages in the data: pages that now return 404 or a redirect must be explained (renamed URLs, www/http variants) before the numbers are interpreted. The script also warns when the periods have different lengths or the volumes are too small for solid conclusions.
- The brand regex separates searches for the person's or business's name from the others: for a small site they are two different stories (people who already know you versus people discovering you). The script gives totals, top queries and pages, queries with many impressions and few clicks, new and lost queries, growth and decline. Queries anonymised by Google do not appear in the queries file: the reliable total is the one by date.

### 3. Interpret, carefully
- **Small volumes = big noise.** With a few dozen clicks, 50% swings can be random: say so, and look at trends over several months.
- **Link to the changes** in `SEO.md › 10. Change log` (date of each change) and to external events: Google core and spam updates, seasonality, technical problems. Update dates in the knowledge base stop at its last refresh: for later periods, mark them as to be checked on Google's Search Status Dashboard. If a drop coincides with a change, first check that the change did not break something (indexing, redirects, titles).
- **Data discontinuities**: Search Console inflated impressions from 13 May 2025 to 27 April 2026 (clicks not affected); compare clicks across that boundary, not impressions, CTR or position (`measurement.md › ### Data reliability and limits`).
- **Traffic drop**: follow the steps of "Procedure: diagnosing a traffic drop" in `measurement.md › ## Procedures` (measurement, known updates, chart shape, brand vs non-brand, pages and queries involved, technical, security and manual actions) before proposing remedies.
- **Many impressions, few clicks**: title and description to review (`seo-content`), or an intent different from the page's.
- **New relevant queries without a dedicated page**: candidates for new content (add them to `SEO.md › 4`).
- Timings: Google states weeks to months for the effect of changes (`measurement.md › ### Expected timings`); do not judge a change after a few days.

### 4. Visibility in AI assistants
Keep the **fixed set of questions** in `SEO.md › 9. Monitoring` (e.g. "What is Northwind Physio in Oslo?", "Which physiotherapist in Oslo treats running injuries?", "Who offers home physiotherapy visits in Oslo?"). Following `ai-search.md › ## Procedures` ("AI visibility with fixed questions"), every 3 months (monthly for sites with active PR or content work) the user asks them to ChatGPT, Gemini, Perplexity, Copilot and Google's AI Mode, in new conversations, and notes for each: site cited yes/no, information correct / outdated / false / about someone else. Add one row per answer to the AI log table in section 9. Read the results as a trend, not as a precise measure; fix wrong sources before chasing presence. Claude cannot query those assistants on the user's behalf.

### 5. Report and update
Write `seo-reports/YYYY-MM-DD-monitor.md` in the working language:
1. **In short** (3-5 lines, plain language): how it went compared with the previous period and the baseline, what probably caused it;
2. **Key numbers**: clicks, impressions, CTR, position; brand and non-brand searches; top pages;
3. **What changed**: new and lost queries, relevant growth and decline, linked to the change log;
4. **AI assistants** (if there are new runs);
5. **Next actions** (3-5 at most), each with the seo-kit skill that handles it;
6. **Data limits**.

Then update `SEO.md`:
- **section 7 Baseline**: a new row with the date, period and the key metrics (the first run of a site without a baseline sets it);
- **section 9 Monitoring**: the brand regex if it was missing, the new AI log rows;
- **Change log step.** Before finishing, append one row to `SEO.md › 10. Change log` (date · change · pages/area · skill) for every file you created or modified in the project (e.g. `YYYY-MM-DD | Monitor report Jul-Sep | seo-reports/ | seo-monitor`); if the user confirms changes made to the site that are not logged yet, add them with their real dates.

### 6. Recurring check
If the user wants a monthly reminder, propose a scheduled task (the `schedule` skill, if available) that each month reminds them to download the export and runs this analysis. Search Console data arrives with a delay of a couple of days, and meaningful comparisons are between periods of equal length.

## Output format
The report above, with headings translated into the working language and the order kept; numbers taken from the script output, never retyped from memory. In the conversation, give the **In short** block and the next actions.

## Things to keep in mind
- No promises of rankings or timelines beyond Google's own statements (weeks to months).
- Correlation is not causation: say "probably" when linking a change to a variation, and name the alternatives.
- Exports contain business data: keep them out of version control and do not share them beyond the team.
