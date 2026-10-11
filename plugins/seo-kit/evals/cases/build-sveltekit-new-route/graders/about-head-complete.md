---
# After the run the /about page declares a title, a meta description and a canonical link.
type: regex
target: { source: file, path: "src/routes/about/+page.svelte" }
flags: i
pattern: '^(?=[\s\S]*<title>)(?=[\s\S]*name=["'']description["''])(?=[\s\S]*rel=["'']canonical["''])'
---
