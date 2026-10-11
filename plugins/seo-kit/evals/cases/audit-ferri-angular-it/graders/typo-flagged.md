---
# The audit file reports the accent typo in the /servizi/ title ("perchè" for "perché").
type: regex
target: trace
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?perch(?:è|\\u00e8)'
---
