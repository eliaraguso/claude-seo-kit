---
# The audit file is in Italian: its summary heading is translated (In sintesi / Sintesi / Riepilogo / Riassunto / In breve / Sommario / Panoramica), not "Summary".
type: regex
target: trace
flags: i
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?#{1,3} *(?:In sintesi|Sintesi|Riepilogo|Riassunto|In breve|Sommario|Panoramica)'
---
