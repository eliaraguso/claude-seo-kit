---
description: Moment 2 of the build skill on a SvelteKit repo - a new /about route with no head tags, not linked from the nav and missing from the sitemap endpoint.
expected_outcome: The build skill adds a specific title, meta description and absolute canonical to src/routes/about/+page.svelte (following the home page pattern), adds /about to the sitemap endpoint and an internal link, and mentions sitemap and/or 404 handling in the reply.
tags: [build, en, sveltekit]
plugins: ["../../.."]
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

I just added an /about page to my site (it's this SvelteKit repo, the new page is `src/routes/about/+page.svelte`). Make it SEO-complete before I push it; edit the files directly. The site lives at https://adanovak.example.

I'm not around for questions, so make reasonable assumptions. Afterwards tell me briefly what you changed and what is still left to do.
