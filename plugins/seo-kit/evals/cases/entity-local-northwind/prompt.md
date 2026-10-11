---
description: The entity/local skill reconciles a local clinic's identity (name variants, phone formats, stale Saturday hours, no structured data, no Business Profile) and writes the identity report.
expected_outcome: seo-reports/YYYY-MM-DD-identity.md with one definition of the clinic, the inconsistencies found, a LocalBusiness (or Physiotherapy) JSON-LD graph with @id and sameAs, ready texts and an off-site checklist (Business Profile, Bing Places, Apple Business Connect, reviews).
tags: [entity-local, en, local-business]
plugins: ["../../.."]
max_turns: 50
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TodoWrite]
---

This repo is the website of Northwind Physio, our physiotherapy clinic in Oslo (static HTML in `public/`). We want to show up properly when people search for our name and on Google Maps, where we are not listed at all.

Please sort out our identity online: what should be on the website and what we need to do on other platforms. Save the result in the project. I'm not around for questions, so make reasonable assumptions and say which ones. Finish with the three things to do first.
