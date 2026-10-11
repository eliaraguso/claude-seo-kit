---
# SEO.md records languages and markets, including the German market.
type: regex
target: { source: file, path: SEO.md }
flags: i
pattern: 'Languages and markets[^\n]*(?:\bde\b|de-DE|German|Germany|Deutschland)'
---
