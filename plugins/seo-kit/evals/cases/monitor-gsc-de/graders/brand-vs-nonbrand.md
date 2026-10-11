---
# The monitor file separates brand and non-brand searches (German or English wording).
type: regex
target: trace
flags: i
pattern: '-monitor\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?(?:Marke|Marken|Brand)(?:[^"\\]|\\.){0,60}?(?:Nicht-?Marke|ohne Marke|markenfremd|Non-?Brand|Nicht-?Brand|generisch)'
---
