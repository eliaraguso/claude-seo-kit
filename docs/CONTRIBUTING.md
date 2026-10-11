# Contributing to seo-kit

Thank you for helping. This guide covers the four kinds of change people usually propose: knowledge, adapters, code and evals. Open an issue first for anything larger than a fix, so we can agree on where the change belongs.

## Ground rules

- **English** in every committed file: knowledge, skills, scripts, tests and docs. The plugin answers users in their own language; the sources stay in English.
- **No real people, clients or small businesses** in examples, tests, fixtures or evals. Use only the fictional entities in [`conventions.md` › Fictional examples](../plugins/seo-kit/knowledge/conventions.md): Northwind Physio, Studio Ferri Orientamento, Acme Widgets, Ada Novak and Daily Fjord. Their domains end in `.example`. Well-known platforms and tools (Google, GitHub, Shopify…) can be named.
- **Google documentation is the primary source.** Third-party views are reported as views and never become rules. Do not promise rankings or timelines.
- **Standard library only** for Python, which must stay compatible with Python 3.9. Do not add runtime dependencies.

## Proposing a knowledge change

1. Read [`plugins/seo-kit/knowledge/conventions.md`](../plugins/seo-kit/knowledge/conventions.md) (the binding rules) and [`docs/knowledge-style-guide.md`](knowledge-style-guide.md) (how to apply them).
2. Find the **owning file**. Each topic has one owner. If another file needs the same check, it gets an alias row (`Alias of CI-17 — verify there, report once`) with the same severity, never a second copy.
3. **A source is required.** Use a Google URL whenever one exists (`[G](url)`). Use the other tags in `conventions.md` for Business Profile, web.dev, Bing, IndexNow, framework docs or SEJ. If a check has only third-party evidence, say so in the Check text. Mark deductions *(inference)*, and claims still to confirm *(re-verify)*.
4. **IDs are append-only.** Never renumber a check and never reuse a retired number. A new check takes the next free number in its prefix. To retire a check, keep its row: make it "(informational) Retired — merged into XX-NN", with severity Low.
5. **Severity** follows the Critical / High / Medium / Low scale in `conventions.md`. When in doubt, choose the lower one and write the condition that raises it as a `Caveat:`. Use **⚠** only for deprecated, unsupported or not-recommended items.
6. **Keep the table header exact**: `| ID | Check | How to verify | Severity | Source |`. Update the `> Updated YYYY-MM-DD` line of the file, and use absolute dates in the text.
7. Run the lint and rebuild the index, then commit `INDEX.md` together with your change:

   ```
   python tools/check_knowledge.py
   python tools/build_index.py
   python tools/build_index.py --check
   ```

   Never edit `INDEX.md` by hand. CI fails if the lint reports errors or if the index is stale.

## Adding an adapter

1. Check the detection table in [`knowledge/adapters/README.md`](../plugins/seo-kit/knowledge/adapters/README.md). If the stack is close to an existing adapter, a pitfall line there may be enough.
2. Create `plugins/seo-kit/knowledge/adapters/<stack>.md` with the sections in the order the template gives: Detection · Rendering default and options · Where title, meta, canonical and robots meta live · Links and routing · robots.txt and sitemap generation · 404 handling (true status) · hreflang and i18n · Structured data hooks · Common pitfalls (with check IDs) · Sources (framework docs, version checked).
3. Keep it **under 4 KB**, because it is read in Tier 0. Adapters create no check IDs: each pitfall points to an existing ID. Cite the framework docs with the version you checked (`[Docs vX](url)`).
4. Add a row to the detection table in `adapters/README.md`, with repository signals first and HTML/header signals second. Update the stack list in the root `README.md`.
5. Run `python tools/check_knowledge.py`.

## Changing scripts or the shared library

- The scripts live in `plugins/seo-kit/skills/<skill>/scripts/`, and the shared code in `plugins/seo-kit/lib/seokit/`. A script must not import from a sibling skill.
- Human-readable output, JSON keys and flags are in English. If you change an output key of `seo_fetch.py` or `extract_dom.js`, update [`docs/page-schema.md`](page-schema.md). Then search `knowledge/` and the SKILL.md files for the old field name.
- Every bug fix comes with a regression test that fails on the old code.
- The files in `tests/fixtures/` are byte-exact (charsets, BOMs, line endings): do not let an editor or git convert them.

## Running tests and evals

```
python -m unittest discover -s tests -v      # unit tests, no network (Windows: py -3 -m unittest ...)
python tools/check_knowledge.py              # knowledge lint
python tools/build_index.py --check          # index freshness
claude --plugin-dir plugins/seo-kit          # try the working copy in Claude Code
claude plugin eval plugins/seo-kit           # eval cases (costs tokens)
python tools/trigger_test.py --dry-run       # what the trigger test would run (free)
```

Evals and real trigger runs start real Claude sessions and cost tokens; run them before a release or after changing a skill's description. Their results land in `plugins/seo-kit/evals/results/` and `tools/trigger-runs/`, both gitignored. To add an eval case, follow `plugins/seo-kit/evals/README.md`:

- Put the fixture inside the case folder, with fictional entities only.
- Do not name the skill in the prompt, because the case also tests triggering.

## Commits and pull requests

- One logical change per commit. The message has a short imperative subject (≤ 72 characters, no trailing period), for example `Add Hugo i18n pitfall to static-generators adapter` or `Fix sitemap index parsing when a child is gzipped`. Add a body when the reason is not obvious.
- Stage files explicitly (`git add <paths>`). Do not commit research full texts, eval results, trigger runs or `__pycache__/`.
- A pull request must keep CI green: the unit tests on three OSes and Python 3.9–3.13, plus the lint job.
- For a user-visible change, add a line under an "Unreleased" heading in [`CHANGELOG.md`](../CHANGELOG.md).
