---
# The monitor file (content of the Write call that creates seo-reports/...-monitor.md) has at least one German heading: any common German form of the summary, key-numbers or brand headings.
type: regex
target: trace
flags: i
pattern: '-monitor\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?#{1,4} *(?:\d+\.? *)?[^\n\\"]{0,40}?(?:Zusammenfassung|K(?:ü|\\u00fc)rze|Kurz gesagt|Kurzfassung|Das Wichtigste|Auf einen Blick|Kennzahlen|Eckdaten|wichtigsten Zahlen|Wichtige Zahlen|Schl(?:ü|\\u00fc)sselzahlen|(?:Ü|\\u00dc)berblick|Markenanfragen|Markensuchen|Marke)'
---
