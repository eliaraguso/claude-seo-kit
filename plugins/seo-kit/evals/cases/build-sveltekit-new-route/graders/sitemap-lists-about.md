---
# The sitemap endpoint now lists /about (a new route must appear in the sitemap).
type: regex
target: { source: file, path: "src/routes/sitemap.xml/+server.js" }
pattern: '[''"`]/about/?[''"`]'
---
