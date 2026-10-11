---
description: Code-mode audit, in Italian, of a prerendered Angular build for an Italian professional-services site, with an accent typo in one title and a localhost canonical.
expected_outcome: The audit skill writes seo-reports/YYYY-MM-DD-audit.md in Italian (translated headings), reports the "perchè" typo in the /servizi/ title with the correction "perché", and flags the localhost canonical on /chi-siamo/.
tags: [audit, it, code-mode, angular]
plugins: ["../../.."]
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

In questa cartella c'è il sito Angular dello Studio Ferri Orientamento, uno studio di orientamento scolastico e universitario a Bologna. La build prerenderizzata è in `dist/studio-ferri/browser/` e andrà online a fine mese su https://studioferri.example (adesso il dominio non risponde ancora).

Mi fai un audit SEO completo sul codice e sulla build, così sistemiamo tutto prima del lancio? Salva il report nel progetto. Non sono disponibile per domande: fai ipotesi ragionevoli e scrivile. Alla fine dimmi in poche righe da cosa partire.
