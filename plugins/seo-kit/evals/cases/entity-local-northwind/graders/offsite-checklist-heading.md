---
# The identity file has an "Off-site checklist" heading (section 6 of the skill's report template).
type: regex
target: trace
flags: i
pattern: '-identity\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?#{1,4} *(?:\d+\.? *)?(?:\*\*)?Off-site checklist'
---
