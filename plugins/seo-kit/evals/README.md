# seo-kit evals

Behaviour tests for the six seo-kit skills, in the format of [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Each case is a realistic request (it never names the skill, so it also tests triggering), a small fixture project, and graders that check what Claude did and produced.

| Case | Language | Skill expected | What it checks |
|---|---|---|---|
| `audit-northwind-static` | EN | seo-audit | Live audit of a static site served on `http://127.0.0.1:8765`: robots.txt blocking `/css/`, a soft-404, a sitemap URL that returns 404, a missing canonical, an `<svg><title>` inside the H1. Report written, plain summary first, no llms.txt advice |
| `audit-ferri-angular-it` | IT | seo-audit | Code-mode audit of a prerendered Angular build: report in Italian, accent typo ("perchè") in a title, localhost canonical |
| `build-sveltekit-new-route` | EN | seo-build | New SvelteKit route `/about` with no head tags: title, description, canonical, sitemap entry, internal link |
| `discovery-acme-ecommerce` | EN | seo-discovery | `SEO.md` v2 for an ecommerce repo selling to the UK and Germany: working language, languages and markets, archetype, brand regex in section 9 |
| `content-saas-feature-page` | EN | seo-content | Rewrite of a stuffed SaaS feature page from the facts in `SEO.md`: `[TO COMPLETE: …]` placeholders instead of invented facts, title and description, internal links |
| `entity-local-northwind` | EN | seo-entity-local | Identity report for a local clinic: LocalBusiness (or subtype) JSON-LD with `@id` and `sameAs`, off-site checklist |
| `monitor-gsc-de` | DE | seo-monitor | German Search Console export analysed with `analyze_gsc.py`, report in German with brand vs non-brand |

## Requirements

- Claude Code 2.1.269 or later and git 2.31 or later (see the eval docs).
- The cases need `Bash`, `Write` and `Edit`, which a run gets only through `--allow-tools`. Every granted shell command runs in Claude Code's OS sandbox, which exists on macOS, on Linux (install `bubblewrap` and `socat`) and on Windows only under WSL2. On native Windows the runs are refused.
- `python3` on `PATH` (the skills' scripts and the `monitor-gsc-de` scaffold use it).

## Run

From the repository root:

```bash
claude plugin eval plugins/seo-kit --scaffold \
  --allow-tools Bash Write Edit "WebFetch(domain:127.0.0.1)"
```

- `--scaffold` is required: each case's `setup.sh` copies its `fixture/` folder into the empty run workspace (and `monitor-gsc-de` zips `gsc-csv/` into `gsc-export-2026-09.zip`). Without it every case runs in an empty folder and fails.
- `"WebFetch(domain:127.0.0.1)"` is meant to let sandboxed shell commands reach the local preview that `audit-northwind-static` starts with `python3 -m http.server 8765` (the sandbox limits network access to granted domains). If your sandbox still blocks loopback traffic, `seo_fetch.py` exits with code 2 (site unreachable) and the audit can only read `public/`, so the report graders may fail for reasons unrelated to the skill; check the run's NOTES and transcript before reading it as a regression.
- One case, one run, no baseline (cheapest loop while editing a skill or a grader):

  ```bash
  claude plugin eval plugins/seo-kit --case audit-northwind-static --runs 1 --ablation none \
    --scaffold --allow-tools Bash Write Edit "WebFetch(domain:127.0.0.1)"
  ```

- Filter by tag with `--tag audit` (tags: `audit`, `build`, `discovery`, `content`, `entity-local`, `monitor`, plus language tags `en`, `it`, `de`).
- Results go to `plugins/seo-kit/evals/results/<timestamp>/` (git-ignored). Add `--no-publish` to keep the HTML report local.

### Cost

Every run is a real Claude Code session on your account, and every `llm` grader adds three judge calls per run. With the defaults (3 runs with the plugin and 3 without, per case) the full suite is 42 agent sessions of up to 40-60 turns each, plus the judge calls of the 4 `llm` graders. Use `--runs 1 --ablation none` and `--case` while iterating, and set a ceiling with `--max-cost-usd` for full runs.

To check that every case file loads, without running anything, point the run at a model that does not exist and set a zero ceiling; the command reports load errors and grader warnings, then stops with `cost ceiling $0 hit` (exit code 2) before the first run:

```bash
ANTHROPIC_MODEL=no-such-model claude plugin eval plugins/seo-kit --scaffold \
  --allow-tools Bash Write Edit --runs 1 --ablation none \
  --model no-such-model --judge-model no-such-model --max-cost-usd 0 --no-publish
```

(Observed with Claude Code 2.1.296; check the eval docs if the behaviour of `--max-cost-usd 0` changes.)

## How the cases are built

- **Fixtures are fictional.** They use only the example entities of `knowledge/conventions.md` (Northwind Physio, Studio Ferri Orientamento, Acme Widgets, Ada Novak) plus Fjordly, a fictional SaaS used by the content case, all on `.example` domains. Never put real sites, people or exports in a case.
- **Layout of a case:**

  ```text
  cases/<case>/
  ├── prompt.md      # frontmatter: description, tags, plugins ["../../.."], limits, allowed_tools; body: the request
  ├── case.yaml      # schema_version "1.1", name, context.scaffold_script: setup.sh
  ├── setup.sh       # copies fixture/ into the workspace
  ├── fixture/       # the project Claude works on
  └── graders/*.md   # one grader per file
  ```

- **Prompts** are written the way a user would ask, in the case's language, never with the skill's name, and end with "I'm not available for questions" so the run does not stall on an interview.
- **Graders** pair a check on the steps (`tool_used: Skill` with `input_match` on the skill name, `tool_used: Bash` on the script) with checks on the result. `tool_used: Skill` is a plugin-fired indicator: in a run with the no-plugin baseline it is shown but not scored.
- **Report content.** Report files are named `seo-reports/YYYY-MM-DD-<kind>.md`, so their path is not known in advance. Graders that read a report use `target: trace` with a pattern anchored on the Write call that creates it (`-audit\.md","content":"…`), so text Claude merely reads from the knowledge base (which mentions llms.txt, robots.txt, sameAs and so on) cannot satisfy them. Files with a fixed path (`SEO.md`, the edited page) are read with `target: { source: file, path: … }`.
- **Baseline.** Runs compare the plugin with no plugin by default (`W/OUT` and `Δ` columns). There are no `baseline` graders yet: that grader type needs a reference transcript (`.jsonl`) recorded from a real run. To add one, run a case once with `--keep-temp`, save a good transcript as `cases/<case>/reference.jsonl`, and add a `graders/<name>.md` with `type: baseline`, `baseline_file: reference.jsonl` and the criteria in the body.

## Add a case

1. Create `cases/<new-case>/` and put the project Claude should work on in `fixture/` (fictional entity, `.example` domain, a few planted problems that a grader can see).
2. Copy `setup.sh` and `case.yaml` from an existing case and set `name` to the folder name.
3. Write `prompt.md`: the frontmatter keys allowed by the docs only (an unknown key fails the case), `plugins: ["../../.."]`, `allowed_tools` with the tools the skill needs, generous `max_turns` and `timeout_seconds`.
4. Add graders: one `tool_used: Skill` for the skill you expect, at least one check on a produced file or on the final message, and at most one `llm` grader with concrete PASS and FAIL conditions. Patterns are JavaScript regexes; put `i` in `flags`, never `(?i)`.
5. Run the load check above, then the case alone with `--runs 1 --ablation none`.

Trigger accuracy across many phrasings (without fixtures) is measured separately by `tools/trigger_test.py` with `tools/trigger-queries.json`.
