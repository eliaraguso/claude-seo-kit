---
description: The monitor skill analyses a German Search Console export (zip built by the scaffold) with analyze_gsc.py, using the brand regex from a German SEO.md, and writes the report in German.
expected_outcome: analyze_gsc.py runs on gsc-export-2026-09.zip with --brand northwind; seo-reports/YYYY-MM-DD-monitor.md is written in German with a brand vs non-brand split, links the numbers to the August changes in the change log, and notes the limits of one week of data.
tags: [monitor, de, gsc]
plugins: ["../../.."]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

Ich habe gerade den Search-Console-Export für die erste Septemberwoche heruntergeladen, er liegt als `gsc-export-2026-09.zip` im Projektordner. Wie läuft die Website? Haben die Änderungen vom August etwas gebracht?

Bitte speichere den Bericht im Projekt. Ich bin nicht erreichbar, also triff vernünftige Annahmen und nenne sie. Fasse mir am Ende in ein paar Sätzen zusammen, was ich als Nächstes tun sollte.
