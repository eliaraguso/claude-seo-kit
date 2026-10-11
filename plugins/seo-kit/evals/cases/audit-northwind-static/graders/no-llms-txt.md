---
# The audit file never recommends adding an llms.txt file (Google Search does not use it; seo-kit lists it as a myth). Negated mentions such as "you do not need to add an llms.txt" are allowed.
type: regex
target: trace
flags: i
match: not_contains
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:[^"\\]|\\.)*?(?<!(?:\bnot|n''t|\bnever|\bno need to|\bneed not)\s(?:\w+\s){0,2})(?:\b|(?<=\\[nt]))(?:add|create|publish|set up|generate|upload)\b[^.\\]{0,40}llms\.txt'
---
