---
# The monitor file (content of the Write call that creates seo-reports/...-monitor.md) has German headings.
type: regex
target: trace
flags: i
pattern: '-monitor\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?#{1,3} *(?:\d+\.? *)?(?:Zusammenfassung|Kurz gesagt|Kurzfassung|Auf einen Blick|Kennzahlen|Wichtige Zahlen|Überblick|\\u00dcberblick)'
---
