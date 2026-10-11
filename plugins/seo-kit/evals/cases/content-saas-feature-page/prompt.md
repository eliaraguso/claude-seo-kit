---
description: The content skill rewrites a weak, keyword-stuffed SaaS feature page using the facts in SEO.md v2, without inventing customer stories or numbers.
expected_outcome: 'src/content/features/shift-scheduling.md is rewritten in place with a specific title and meta description, copy built on the product facts in SEO.md, "[TO COMPLETE: ...]" markers where first-hand experience is needed, no keyword stuffing, and internal links to the related feature and pricing pages.'
tags: [content, en, saas-product]
plugins: ["../../.."]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

Our shift-scheduling feature page (`src/content/features/shift-scheduling.md`) is weak: it gets almost no search traffic and honestly reads like fluff. Rewrite it in place so that it can be found by restaurant and café managers and actually convinces them.

I'm not around for questions. When you're done, tell me briefly what you changed and what you still need from me.
