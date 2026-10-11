# Knowledge style guide (for contributors)

The binding rules live in `plugins/seo-kit/knowledge/conventions.md`. This guide explains how to apply them when writing or translating a knowledge file.

## Translating an existing file (IT → EN)

1. Keep the file name, every check ID, every URL and every source tag. Translate the anchor text and headings; `## Contents` links must point to the translated anchors.
2. Apply the topic file template of `conventions.md`: rename "Fatti e regole (Google)" → "Facts and rules (Google)", "Controlli per l'audit" / "Controlli / procedure" → "Audit checks" (+ "Procedures" if the file has procedures), "Regole per chi costruisce…" / "Regole per contenuti e struttura del sito" → "Build rules", "Note per tipo di sito" → "Notes by site type", "Cosa dicono le fonti terze" → "Third-party views", "Miti e consigli obsoleti" → "Myths and outdated advice".
3. Rewrite the audit-check table header to exactly `| ID | Check | How to verify | Severity | Source |`. Map severities to Critical / High / Medium / Low. A row that was "Info" becomes Low and starts its check text with "(informational)".
4. Remove ⚠ from any check we still recommend; move its condition into a `Caveat:` sentence in "How to verify". Keep ⚠ only on deprecated or unsupported items.
5. Re-order "Notes by site type" into the fixed archetype order. Translate type names to the English slugs.
6. Replace every personal-case example (Verona, orientamento, raguso, GitHub-only assumptions written as general rules) with the fictional entities of `conventions.md`. Keep examples that are genuinely generic.
7. Generalise Italy-only content: a column "available in Italy" becomes `Rich result (Yes/No/Limited)` + `Availability notes`; Italian legal references become a short "Regulated professions and legal notices" paragraph with examples from several countries.
8. Fix tense: events that have happened are in the past tense with the date. Flag anything you could not verify with *(re-verify)* in the "Third-party views" section, not with ⚠.
9. Where the file contradicts another file, write the single resolution in the owning file (see the plan's contradiction table) and leave a one-line pointer in the other.
10. Do not shorten the substance. Translate tightly, but keep every rule, every caveat and every source.

## Writing a new check

- One check = one verifiable statement. "How to verify" names the tool, command, report or page to look at (e.g. `seo_fetch.py` field, Search Console report, a Grep on the build output).
- Severity follows the scale in `conventions.md`; when in doubt between two, choose the lower and explain the condition that raises it.
- Source is a Google URL whenever one exists. A check with only third-party evidence must say so in the Check text ("third-party evidence").
- Build rules do not create IDs; they point to the checks they satisfy (`→ CI-03`).

## Writing an adapter (`knowledge/adapters/<stack>.md`)

Sections, in order: Detection · Rendering default and options · Where title, meta, canonical and robots meta live · Links and routing · robots.txt and sitemap generation · 404 handling (true status) · hreflang and i18n · Structured data hooks · Common pitfalls (with check IDs) · Sources (framework docs, version checked). Keep each adapter under 4 KB: it is read in Tier 0.

## Tone

Plain language first, jargon second. Every rule says what to do and why in one sentence each. No marketing, no guarantees.
