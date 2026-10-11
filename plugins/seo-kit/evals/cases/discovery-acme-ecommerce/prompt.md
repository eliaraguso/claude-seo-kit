---
description: The discovery skill builds SEO.md v2 for an English-only ecommerce repo that sells to the UK and Germany, with no live site reachable and no user to interview.
expected_outcome: SEO.md is created in English with Working language, Languages and markets (en-GB plus Germany/de), primary archetype ecommerce, a search-intent table mapped to pages, and section 9 Monitoring with a brand regex built on "acme".
tags: [discovery, en, ecommerce]
plugins: ["../../.."]
max_turns: 50
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

We want to start working on getting the Acme Widgets shop found on Google. Before anyone touches the site, I'd like the groundwork in place: what kind of site this is, which searches we should go after and which page should answer each one. Write it down in the repo so the team and future work can build on it.

I'm not available for questions: use the README and the product pages, and mark anything you had to guess as an assumption. Finish with a short summary of the main searches and the next step.
