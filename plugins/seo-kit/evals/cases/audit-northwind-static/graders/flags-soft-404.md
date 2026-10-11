---
# The audit file names the soft-404: /team/ingrid/ says "not found" but answers 200.
type: regex
target: trace
flags: i
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?(?:soft[ -]?404|team/ingrid)'
---
