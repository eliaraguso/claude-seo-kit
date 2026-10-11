---
# The audit file names the sitemap URL /services/sports-injuries/, which returns 404.
type: regex
target: trace
flags: i
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?sports-injuries'
---
