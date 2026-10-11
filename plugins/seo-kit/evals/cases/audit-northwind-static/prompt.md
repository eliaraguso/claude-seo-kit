---
description: Live-site audit of a small static site with planted defects (robots.txt blocking /css/, soft-404 page, sitemap URL that returns 404, missing canonical, svg title inside the H1).
expected_outcome: The audit skill runs seo_fetch.py against the local preview, writes seo-reports/YYYY-MM-DD-audit.md in English with a plain-language summary and a prioritised plan, and reports the robots.txt block, the soft-404 and the 404 sitemap URL without recommending llms.txt.
tags: [audit, en, live-site]
plugins: ["../../.."]
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

This folder is the website of Northwind Physio, our physiotherapy clinic in Oslo (static HTML in `public/`, production domain https://northwind-physio.example). We have been live for months but we barely show up on Google, even when people search for our name.

Start a local preview in the background with `python3 -m http.server 8765 --directory public` and check the site at http://127.0.0.1:8765. It is the same build as production, so absolute links to northwind-physio.example point to these same pages.

Find out what is holding us back and save the report in the project. I am not available for questions, so make reasonable assumptions and state them. When you are done, tell me in a few lines what to fix first.
