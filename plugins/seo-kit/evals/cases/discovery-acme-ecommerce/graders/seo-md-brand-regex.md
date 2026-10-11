---
# SEO.md has section "## 9" (Monitoring) with a brand regex built on the distinctive token "acme".
type: regex
target: { source: file, path: SEO.md }
flags: i
pattern: '(?:^|\n)## 9\.[^\n]*\n(?:(?!\n## )[\s\S])*?regex[^\n]*acme'
---
