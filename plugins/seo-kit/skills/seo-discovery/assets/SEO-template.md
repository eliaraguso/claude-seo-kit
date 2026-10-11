# SEO profile — {{site name}}

> SEO state file of the site, read and updated by the seo-kit skills (format v2).
> Last updated: {{YYYY-MM-DD}}. Entries marked *(assumption)* still need confirming.
> Headings and notes are written in the working language recorded in section 1; page copy (titles, descriptions, H1) in the site language(s).

**In short:** {{2-3 plain-language lines: who must find the site, with which searches, what is missing}}

## 1. Site
- **Production URL:** {{https://...}} (canonical host: with or without www)
- **Status:** in development | live since {{YYYY-MM-DD}}
- **Repository / code folder:** {{path or "not available"}}
- **Stack:** {{framework and version, e.g. Astro 5}} · **Adapter:** {{adapter slug from knowledge/adapters/README.md, e.g. astro}} · **Rendering:** CSR | SSR | SSG/prerender | hybrid · **Router:** path | hash
- **Hosting / CDN / WAF:** {{e.g. Netlify, Vercel, Cloudflare}}
- **Languages and markets:** {{e.g. en-GB primary; de-DE secondary}}
- **Working language (reports, SEO.md):** {{e.g. English}}

## 2. Site type and goal
- **Primary archetype:** {{personal-brand | professional-services | local-business | editorial | ecommerce | saas-product}}
- **Secondary archetypes:** {{...}}
- **Modifiers:** {{none | multilingual | marketplace-ugc | paywall | app-and-site}}
- **Business goal:** {{e.g. get booking requests from people with back pain in Oslo}}
- **Measurable conversions:** {{contact form, email/phone click, booking, CV download, purchase}}

## 3. Entity (who is behind the site)
- **Exact name to use everywhere:** {{First Last / Business name}} · **Variants / alternateName:** {{...}}
- **Role / profession:** {{...}}
- **Location and area served:** {{city, region; online yes/no}} · **NAP:** {{name, address, phone}} (only if public)
- **Official profiles (sameAs):** {{LinkedIn, GitHub, Instagram, Business Profile, professional register or association}}
- **Verifiable credentials:** {{degrees, certifications, register entries, with issuing body and year}}
- **Homonyms or entities that could be confused:** {{...}}

## 4. Audience and search intents
| Priority | Intent / representative query | Type (brand, service, local, informational) | Page that answers | Page status | Notes |
|---|---|---|---|---|---|
| 1 | {{"northwind physio"}} | brand | / | exists | |

> Queries are assumptions until Search Console shows real data. One page per intent: no copy-paste pages per city or variant.

**Evidence collected:** {{Google autocomplete suggestions (language/country), observations on the results (engine used), Search Console export}}

**Queries not to chase:**
| Query | Why not |
|---|---|
| {{...}} | {{different intent / dominated by portals / deliberately not covered}} |

### Proposals for the main pages
| Page | Proposed title (characters) | Meta description | H1 |
|---|---|---|---|
| / | {{...}} ({{n}}) | {{...}} | {{...}} |

## 5. Competitors and references
- **Search competitors:** {{sites that currently hold the target queries}}
- **Notes:** {{...}}

## 6. Access and tools
- **Search Console:** {{Domain property | URL-prefix property | none}} · **Business Profile:** {{yes/no; address or service area}}
- **Analytics:** {{GA4 / other / none}} · **Bing Webmaster Tools:** {{yes/no}} · **IndexNow key:** {{key file URL / not set up}}
- **Who can carry out manual actions (Business Profile, profiles, reviews):** {{...}}

## 7. Baseline
| Date | Source | Metric | Value |
|---|---|---|---|
| {{YYYY-MM-DD}} | Search Console (last 3 months) | clicks / impressions / brand queries | |

## 8. Decisions and constraints
- {{e.g. "No blog for now", "SSR not possible on the current hosting", "Home address not published"}}

## 9. Monitoring
- **Brand query regex:** {{e.g. northwind}} — distinctive tokens of the name only; used by `analyze_gsc.py --brand` and in the Search Console regex filter
- **Fixed questions for AI assistants** (same wording every run; repeat every 3 months):
  1. {{accuracy, e.g. "What is Northwind Physio in Oslo?"}}
  2. {{decision, e.g. "Which physiotherapist in Oslo treats running injuries?"}}
  3. {{service, e.g. "Who offers home physiotherapy visits in Oslo?"}}

| Date | Assistant | Question | Site cited | Information (correct / outdated / false / about someone else) |
|---|---|---|---|---|

## 10. Change log
| Date | Change | Pages/area | Skill |
|---|---|---|---|

## 11. Audit history
| Date | Report | Critical | High | Medium | Low | Notes |
|---|---|---|---|---|---|---|
