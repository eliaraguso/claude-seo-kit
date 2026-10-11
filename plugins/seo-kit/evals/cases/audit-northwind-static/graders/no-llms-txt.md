---
# The audit file never recommends adding an llms.txt file (Google Search does not use it; seo-kit lists it as a myth). A clause that negates the verb ("do not add", "no need to create", "you don't need to publish") is allowed. No lookbehind, so the pattern is valid in JavaScript and Python; a clause starts at the beginning of the file, after a JSON-escaped line break or after . ! ? ; : and a space.
type: regex
target: trace
flags: i
match: not_contains
pattern: '-audit\.md\\*"\s*,\s*\\*"content\\*"\s*:\s*\\*"(?:(?:[^"\\]|\\.)*?(?:\\+n|[.!?;:] ))?(?:(?!not\b|never\b|n''t\b|no need\b|need not\b|without\b|avoid\b)(?:[^.!?;\\"]|\\+"))*?(?:add|create|publish|set up|generate|upload)(?:[^.!?;\\"]|\\+"){0,40}llms\.txt'
---
