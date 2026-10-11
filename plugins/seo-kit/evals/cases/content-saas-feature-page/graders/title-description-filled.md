---
# The frontmatter has a non-empty title (no longer just "Features") and a non-empty description.
type: regex
target: { source: file, path: "src/content/features/shift-scheduling.md" }
pattern: '^(?=[\s\S]*?(?:^|\n)title: *["'']?(?!Features["'']?\s*\n)[A-Za-z])(?=[\s\S]*?(?:^|\n)description: *["'']?[A-Za-z])'
---
