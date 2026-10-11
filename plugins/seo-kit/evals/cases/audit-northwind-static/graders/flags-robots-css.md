---
# The audit file (content of the Write call that creates seo-reports/...-audit.md) says that robots.txt blocks /css/.
type: regex
target: trace
flags: i
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?(?:(?:robots\.txt|disallow)(?:[^"\\]|\\.){0,400}?/css|/css(?:[^"\\]|\\.){0,400}?(?:robots\.txt|disallow|blocked))'
---
