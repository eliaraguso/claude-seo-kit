# SEO profile — Fjordly

> SEO state file of the site, read and updated by the seo-kit skills (format v2).
> Last updated: 2026-09-20. Entries marked *(assumption)* still need confirming.

**In short:** Fjordly must be found by restaurant and café managers who search for a way to plan staff shifts; today the site gets clicks almost only for the brand name.

## 1. Site
- **Production URL:** https://fjordly.example (canonical host without www)
- **Status:** live since 2025-04-01
- **Repository / code folder:** this repository
- **Stack:** Astro 5 · **Adapter:** astro · **Rendering:** SSG/prerender · **Router:** path
- **Hosting / CDN / WAF:** Netlify
- **Languages and markets:** en (primary; customers in Norway, Sweden, Denmark, UK)
- **Working language (reports, SEO.md):** English

## 2. Site type and goal
- **Primary archetype:** saas-product
- **Secondary archetypes:** none
- **Modifiers:** none
- **Business goal:** free-trial sign-ups from restaurant and café managers
- **Measurable conversions:** trial sign-up, demo request

## 3. Entity (who is behind the site)
- **Exact name to use everywhere:** Fjordly · **Variants / alternateName:** Fjordly Scheduling
- **Role / profession:** software company, shift scheduling for hospitality
- **Location and area served:** online; customers in the Nordics and the UK
- **Official profiles (sameAs):** LinkedIn company page, App Store and Google Play listings
- **Verifiable credentials:** none relevant
- **Homonyms or entities that could be confused:** none known

## 4. Audience and search intents
| Priority | Intent / representative query | Type (brand, service, local, informational) | Page that answers | Page status | Notes |
|---|---|---|---|---|---|
| 1 | "fjordly" | brand | / | exists | |
| 2 | "restaurant shift scheduling app" | service | /features/shift-scheduling/ | exists (weak) | main feature page |
| 3 | "staff rota app for cafés" | service | /features/shift-scheduling/ | exists (weak) | UK wording: "rota" |
| 4 | "how to make a restaurant staff schedule" | informational | to create | to create | |
| 5 | "shift swap app for staff" | service | /features/shift-swaps/ | exists | |

> Queries are assumptions until Search Console shows real data. One page per intent.

**Evidence collected:** Google autocomplete (en, gb) for "restaurant shift" suggests "restaurant shift scheduling app", "restaurant shift planner", "restaurant rota template".

### Product facts (confirmed by the founders, 2026-09-20)
- Drag-and-drop weekly schedule by role (kitchen, floor, bar); templates for recurring weeks.
- Availability: staff enter their availability and time-off requests in the app; conflicts are flagged while planning.
- Labour cost: the schedule shows planned labour cost per day against a target set by the manager.
- Publishing: the schedule is pushed to staff phones; changes trigger a notification.
- Integrations: payroll export (CSV), POS sales import for labour-cost targets.
- Pricing: EUR 3 per active employee per month; 30-day free trial without a card.
- Not offered: payroll processing, hiring, tips management.

## 5. Competitors and references
- **Search competitors:** large international scheduling suites and free spreadsheet templates hold the generic queries.

## 6. Access and tools
- **Search Console:** Domain property · **Business Profile:** no (online only)
- **Analytics:** Plausible · **Bing Webmaster Tools:** no · **IndexNow key:** not set up

## 7. Baseline
| Date | Source | Metric | Value |
|---|---|---|---|
| 2026-09-15 | Search Console (last 3 months) | clicks / impressions / brand queries | 410 / 9,800 / 92% of clicks |

## 8. Decisions and constraints
- No customer logos or testimonials without written permission from the customer.
- No comparison pages naming competitors for now.

## 9. Monitoring
- **Brand query regex:** fjordly
- **Fixed questions for AI assistants:**
  1. "What is Fjordly?"
  2. "Which app helps a restaurant manager plan staff shifts?"
  3. "Is there a shift scheduling app that shows labour cost while you plan?"

| Date | Assistant | Question | Site cited | Information (correct / outdated / false / about someone else) |
|---|---|---|---|---|

## 10. Change log
| Date | Change | Pages/area | Skill |
|---|---|---|---|
| 2026-09-20 | SEO.md created (v2) | SEO.md | seo-discovery |

## 11. Audit history
| Date | Report | Critical | High | Medium | Low | Notes |
|---|---|---|---|---|---|---|
