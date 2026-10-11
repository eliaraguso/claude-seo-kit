# Entity and personal brand

> Updated 2026-10-11. Scope: identity of a person or small brand for Google and AI assistants (entity home, Person/ProfilePage/Organization markup, site name, homonyms, profiles, mentions, regulated professions). Primary source: Google Search Central; third-party views marked [SEJ].
> Legend: `[G](https://…)` = Google Search Central documentation, blog or Office Hours (fact). *(inference)* = reasoning from Google facts, not stated by Google. **[SEJ YYYY-MM, …]** = third-party source (opinion, vendor study, single case). ⚠ = claim not to be turned into a recommendation.
> Applies to people (portfolio, author, consultant) and small brands. Related files: `local-seo.md` (businesses with premises or a service area), `structured-data.md` (syntax), `content-quality-spam.md`, `ai-search.md`.

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
- [Audit checks](#audit-checks)
- [Build rules](#build-rules)
- [Off-site checklist](#off-site-checklist)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
- [Myths and outdated advice](#myths-and-outdated-advice)

## Facts and rules (Google)

### Entity home and "About" page
- Google recommends clear information **about the author or the site**: a byline where readers expect one, leading to a page with details about the author or an "about us" page; a reputation that can be checked by searching for the site. [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- `ProfilePage`: the page's main focus must be **a single person or organisation affiliated with the site**. Valid cases: author page, **a blog's "About me" page**, employee page. Not valid: the main home page of a store (too much non-profile information). [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page)
  - Required: `mainEntity` (`Person` or `Organization`; default `Person`) with `name` (the real name; a handle goes in `alternateName`; `alternateName` is enough if `name` is missing).
  - Recommended: `dateCreated`, `dateModified` (only human edits to the metadata); on Person: `alternateName`, `description` (the author's tagline or **relevant qualifications**), `identifier`, `image` (never placeholders or icons; ≥ 50,000 px; 16x9, 4x3 or 1x1), `sameAs` (other profiles or the profile's home), `interactionStatistic` (**only statistics from the platform hosting the profile**, not followers on other social networks), `agentInteractionStatistic`; `hasPart` for recent activity (e.g. an Article with `author` → `{"@id": "#main-author"}`).
- `Organization` goes on the **home page** or on a **single page** describing the organisation (e.g. About us), not on every page; no required properties; `name`/`alternateName` **the same as the site name**; `logo` ≥ 112×112 px and legible on white; `sameAs` to social and review sites; `vatID` = an important trust indicator. [G](https://developers.google.com/search/docs/appearance/structured-data/organization)
- Several connected entities: use **`@id`** to link them; always include the page's main type. [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Author in articles: `author` = `Person`/`Organization`; `author.name` **the name only** (job title in `jobTitle`, honorifics in `honorificPrefix`/`honorificSuffix`); `author.url` to the page that identifies the author (if internal, marked up as `ProfilePage`) or `sameAs`; one object per author. [G](https://developers.google.com/search/docs/appearance/structured-data/article)
- Structured data must not be used to **deceive**: impersonating people or organisations, misrepresenting ownership or affiliation; mark up only visible content. [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

### Site name and the SERP for your own name
- The **site name** is generated automatically; the main signal is **`WebSite` structured data on the home page** (`name` and `url` required; `alternateName` recommended), then `og:site_name`, `<title>`, headings and home page text, references across the web. [G](https://developers.google.com/search/docs/appearance/site-names)
  - One name per domain or subdomain; **subdirectories are not supported**; markup on **all** duplicates of the home page (http/https, www); a single `WebSite` node.
  - The name must be **unique, not generic** ("Best Dentists in Iowa" is Google's negative example) and consistent across the home page.
  - If it is not chosen: add `alternateName`; as a fallback, the **lowercase domain** as the last `alternateName` (or as `name` as a last resort). The Rich Results Test does **not** support site names: use validator.schema.org. Timing: days to weeks.
- Rebranding with an old name that persists: consistent name across the whole site, all versions updated, correct redirects. [G](https://developers.google.com/search/help/office-hours/2022/december)
- **Site diversity**: generally no more than **two results** per site in the top results (subdomains count as the same site). [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide) → *(inference)*: for the SERP of your own name, consistent external profiles fill the other positions.
- **Knowledge panel**: Google finds the name, contact details and social profiles on the web; a verified representative can update it and override the data; feedback via the link at the bottom of the panel. [G](https://developers.google.com/search/docs/appearance/establish-business-details)
- **Sitelinks** are fully automatic: concise titles, headings and internal anchor text help. [G](https://developers.google.com/search/docs/appearance/sitelinks)
- The page that shows for the site's name depends on the **perceived intent**; it can be an inner page. [G](https://developers.google.com/search/help/office-hours/2023/september)

### Homonyms and ambiguous names
- Names similar to a famous entity or to a misspelling of a common word: Google tends to correct the query; the systems learn the name **over time (even many months)**, with no shortcuts. Choose a name that is not a misspelling of something well known. [G](https://developers.google.com/search/help/office-hours/2022/november) · [G](https://developers.google.com/search/help/office-hours/2024/july)
- Names shared with others (social accounts, businesses): mixed results are "legitimate"; to be found you need a **clear identifier**, not a term used by many. [G](https://developers.google.com/search/help/office-hours/2023/january)
- Google does **not** use `llms.txt` or similar files (this also applies to `llms-author.txt`, according to Mueller). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [SEJ 2026-07, news Mueller]

### Domain and hosting
- Host content on **your own domain**: frames or masked forwarding make it impossible to rank with your own domain; Google Sites is "not ideal". [G](https://developers.google.com/search/help/crawling-index-faq) · [G](https://developers.google.com/search/help/office-hours/2023/september)
- Keywords in the domain: almost no effect; the TLD does not matter except for country targeting; hyphens are allowed. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- Copies of your content that outrank the original can point to quality problems on the original site. Syndication (e.g. LinkedIn articles): you trade visibility on the platform for the risk that the platform ranks above your own site; to keep syndicated copies out of Search the partner needs `noindex`, canonical is only a hint. [G](https://developers.google.com/search/help/office-hours/2024/june) · [G](https://developers.google.com/search/help/office-hours/2023/june)
- PDFs (CV, publications): put a **link to the site at the top** of the PDF; content accessible without login. [G](https://developers.google.com/search/help/office-hours/2023/december)

### Search profiles and platform properties
- **Search profile**: gathers content from the web and social platforms (Instagram, TikTok, YouTube, X, Facebook, website) at `profile.google.com/@handle`; followers see more of that content in the **personalised feed (Discover)**. Badge on the site: link to the profile, touch target ≥ 48×48 dp on Android / 44×44 px on the web, do not alter the "Super G". [G](https://developers.google.com/search/docs/appearance/search-profiles)
  - **US only** and with a **follower threshold** (10,000 on one platform since September 2026; previously 100,000/35,000); **no effect on ranking**. [SEJ 2026-06 and 2026-09, news Google]: the Google page read gives neither country nor threshold.
- **Platform properties** in Search Console for **Instagram, TikTok, X, YouTube** (global since 29 July 2026), even without a website; Performance, Insights and Goals reports; if the Search profile is claimed, the accounts are added automatically. **LinkedIn and GitHub are not supported.** [G](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) · [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide)

### Branded queries and Search Console
- **Branded / non-branded query filter** in the Performance report (plus a card in Insights): covers the name, variants, misspellings and unique products or services of the brand; classification by an internal AI system, errors possible; **no effect on ranking**; only **top-level properties** (not URL-prefix or subdomain properties) with enough volume; available to all eligible sites since 11 March 2026. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Verify the site in Search Console to establish it as the official presence; verification itself does not change ranking. [G](https://developers.google.com/search/docs/appearance/establish-business-details) · [G](https://developers.google.com/search/help/office-hours/2023/january)
- Generative AI performance report: impressions only (AI Overviews, AI Mode, Discover), global since 31 August 2026. [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)

### Author, credentials, E-E-A-T
- **E-E-A-T is not a specific ranking factor**; trust is the most important aspect; it weighs more on **YMYL** topics (health, financial stability, safety). [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- **Fabricated authors** (AI-generated headshots, made-up names, false credentials) = deception that makes a page untrustworthy to users and to Google's quality systems. [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) The dated update behind this wording (1 October 2026) was reported by [SEJ 2026-10] *(re-verify)*: see Third-party views.
- AI-assisted content: explain how it was created when readers would expect it; check text and metadata by hand. [G](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- First-hand experience, **non-generic** content ("Why we gave up on…" beats "7 tips for…"). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### Mentions, links and spam
- Link spam includes: guest posts, advertorials and press releases with optimised anchors; link exchanges; low-quality directories and social bookmarking; **widely distributed links in footers or templates of many sites (e.g. "site built by")**; forum signatures. Advertising links are allowed with `rel="sponsored"`/`nofollow`. [G](https://developers.google.com/search/docs/essentials/spam-policies)
- "Built by …" credit links on clients' sites: do not worry too much; if you control them, `nofollow`; a sensible anchor, not stuffed with keywords. [G](https://developers.google.com/search/help/office-hours/2023/january)
- Guest posts to obtain backlinks, even with valuable content = a violation if the links are not qualified. [G](https://developers.google.com/search/help/office-hours/2023/september)
- When hiring a consultant: **never add a link to the SEO's site**; the owner is responsible for what suppliers do. [G](https://developers.google.com/search/docs/fundamentals/do-i-need-seo)
- Spam includes **manipulating AI answers**; chasing inauthentic mentions is of little use. [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **Site reputation abuse**: hosting third-party content to exploit your own domain's signals (manual action outside the EEA; inside the EEA, separate classification of the section since 30 August 2026). **Expired domain abuse**. [G](https://developers.google.com/search/docs/essentials/spam-policies)
- Promote the site: communities, social media, the URL on business cards and printed material; Google finds sites through links and mentions. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G](https://developers.google.com/search/help/office-hours/2023/april)
- Structured data is **not required** for AI features; there is no special markup. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### Regulated professions and legal notices
- Many countries require identifying or legal information on the website of a business or professional. Examples (legal requirements outside Google's documentation; check current local rules or ask a local adviser):
  - **Italy**: the VAT number (partita IVA) on the site of anyone who holds one; for regulated professions, the professional register and registration number; professions not organised in registers have their own transparency duties (Law 4/2013).
  - **Germany**: an *Impressum* (legal notice) with name, address, contact details and, where they apply, register entries, VAT ID and the supervisory authority or professional chamber.
  - **United Kingdom**: companies show the registered name, company number, place of registration and registered office address on their website.
  - **United States**: many states require licensed trades and professions (e.g. contractors, real estate) to show their state licence number in advertising, websites included; rules vary by state.
- Google does not rank pages on these notices; no Google document lists them as signals *(inference)*. They still matter for search: consistency between the site, the public register and the markup (`Organization.vatID`, `identifier`) makes the reputation verifiable, which supports the trust at the centre of E-E-A-T, and Google calls `vatID` an important trust indicator. [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [G](https://developers.google.com/search/docs/appearance/structured-data/organization)
- `local-seo.md` points here for the legal-notice topic.

## Audit checks

Severity follows the scale in `conventions.md`. "Auto" = from code or HTML; "Manual" = needs the user or an external tool.

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| EN-01 | An **entity home** ("About" page) exists with full name, role, real photo, bio, contact details and links to profiles; linked from navigation or footer | Auto: crawl + internal links | High | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| EN-02 | `ProfilePage` with `mainEntity` `Person` + `name` on the About page (not on a mixed home page with services and blog) | Auto: JSON-LD + page type | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| EN-03 | `Person.image` = real photo, crawlable URL, ≥ 50,000 px; no placeholder avatar | Auto | Low | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| EN-04 | `sameAs` points only to the person's **own** profiles (professional profiles relevant to the field, e.g. GitHub for developers, ResearchGate for researchers, LinkedIn for most; social profiles), valid URLs (200), no one else's profile | Auto (status) + Manual (ownership). Caveat: raise to Critical when a `sameAs` URL points to someone else's profile (misrepresentation) | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| EN-05 | External profiles link **to the site** (bio or website field of the professional profiles relevant to the field, social profiles, Business Profile) | Manual: list of profiles | High | [G](https://developers.google.com/search/help/office-hours/2023/december) |
| EN-06 | Stable `@id` for `Person`, `Organization`, `WebSite`; defined once and referenced from `author`/`publisher`/`mainEntity` | Auto | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) · [SEJ 2026-10, Pollitt] |
| EN-07 | Alias of SD-10 — verify there, report once | `structured-data.md` › SD-10; site-name details (`alternateName`, all home page variants) in Facts › Site name | High | [G](https://developers.google.com/search/docs/appearance/site-names) |
| EN-08 | Site name = real name or brand (e.g. "Ada Novak", "Studio Ferri Orientamento"), **not generic** ("Portfolio", "Full Stack Developer", "Career Guidance"); consistent with `<title>`, `og:site_name`, home page H1 | Auto | Medium | [G](https://developers.google.com/search/docs/appearance/site-names) |
| EN-09 | `Organization` only if a brand or registered business exists; `name` = site name; `logo` ≥ 112 px, legible on white; `vatID` if there is a VAT or tax number | Auto | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/organization) |
| EN-10 | The name has an **identical** form everywhere (middle name, accents, initials) in title, H1, JSON-LD, profiles | Auto (site) + Manual (profiles) | High | [G](https://developers.google.com/search/help/office-hours/2023/january) · [SEJ 2026-09, Clarkson-Bennett] |
| EN-11 | Home page `<title>` = First Last + role or qualifier (not "Home") | Auto | Medium | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| EN-12 | Homonyms: a stable qualifier (role, city, specialisation) in title, `description`, profile bios; SERP check of the name | Manual: SERP from a clean browser. Caveat: applies only when homonyms exist | High | [G](https://developers.google.com/search/help/office-hours/2023/january) · [SEJ 2026-07, Montti] |
| EN-13 | Articles have a visible byline leading to the author page; `author` `Person` with only the name in `name`, `url` → profile page | Auto | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/article) |
| EN-14 | No **fabricated** authors or credentials; credentials verifiable (links to issuing bodies, associations, certifications) | Manual | Critical | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| EN-15 | Credentials, role and dates consistent across site, professional profiles, CV/PDF; no unexplained old role | Manual | Medium | [SEJ 2026-09, conflicting info] |
| EN-16 | `interactionStatistic` does not report followers from other platforms | Auto | Medium | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| EN-17 | Alias of SD-16 — verify there, report once | `structured-data.md` › SD-16 (no `AggregateRating`/`Review` stars on the site's own testimonials) | High | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| EN-18 | No self-referential listicle ("best Angular developers", "best career advisers" with oneself at no. 1, e.g. Ada Novak ranking herself first) | Auto: pattern `intitle:best` (or the equivalent in the site language) + own name in first position | High | [SEJ 2026-02 and 2026-06, Lily Ray] · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| EN-19 | "Built by" credit links on clients' sites: `nofollow`/`sponsored` or plain text; anchor = name, not keywords | Manual: list of client sites; Auto if accessible | High | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| EN-20 | On your own site: no "SEO by"/credit links to suppliers; sponsored links qualified | Auto | Medium | [G](https://developers.google.com/search/docs/fundamentals/do-i-need-seo) |
| EN-21 | A "Press / Talks" page with real mentions (talks, podcasts, articles) and links to the sources; no bought mentions | Auto + Manual | Medium | [G](https://developers.google.com/search/docs/essentials/spam-policies) · [SEJ 2026-09, Jarboe] |
| EN-22 | Own domain (not `github.io`/`vercel.app`/`netlify.app` as the main site) | Auto | High | [G](https://developers.google.com/search/help/crawling-index-faq) · [SEJ 2026-01, Mueller] |
| EN-23 | Republished articles (LinkedIn, dev.to, Medium): first on the site, then on the platform with a link or canonical to the original where possible | Manual | Medium | [G](https://developers.google.com/search/help/office-hours/2024/june) · *(inference)* |
| EN-24 | CV/publications: indexable HTML version + PDF with a link to the site at the top | Auto | Low | [G](https://developers.google.com/search/help/office-hours/2023/december) |
| EN-25 | Hosted third-party content (guest posts, sponsored articles) used to exploit the domain | Auto + judgement. Caveat: applies only when such content is present | High | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| EN-26 | Search Console: **Domain** property verified (needed for the branded filter) | Manual | Medium | [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter) |
| EN-27 | Platform properties added for YouTube/Instagram/X/TikTok if used | Manual | Low | [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) |
| EN-28 | Key content of the About page in the initial HTML (SPA: SSR/prerender) | Auto: raw vs rendered HTML. Caveat: Google renders JavaScript; the risk is for crawlers that do not (see the bot table in `ai-search.md`) | Medium | [SEJ 2026-09, brand protection] |
| EN-29 | (informational) `llms.txt`/`llms-author.txt`/"content-signal" directives: their absence is **not** an error; if present, report that Google ignores them | Auto | Low | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| EN-30 | Contact details for clients, employers or recruiters in text (email, profile link, form), not only behind JS or in an image | Auto | Medium | [G](https://developers.google.com/search/docs/fundamentals/get-started-developers) |

## Build rules
1. **One entity home**: an "About" page that is the canonical source of facts about the person; all other pages and profiles point to it. Home and About can coincide only if the home page really is a profile page [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page). → EN-01, EN-02
2. **Recommended JSON-LD structure** (*(inference)* from the ProfilePage and Organization docs [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page)): on the home page `WebSite` (`@id` `/#website`, `name`, `alternateName`, `url`) + optional `Organization` (`/#org`); on the About page `ProfilePage` with `mainEntity` `Person` (`@id` `/about#person`, `name`, `alternateName`, `description` with qualifications, `image`, `sameAs`, `jobTitle`); in articles `author: {"@id": "…#person"}`. Define each entity once and reference it. → EN-02, EN-06, EN-07, EN-13
3. **Fixed qualifier** next to the name (role + specialisation or city) in titles and bios, especially if homonyms exist [G](https://developers.google.com/search/help/office-hours/2023/january). → EN-11, EN-12
4. **Evidence, not adjectives**: projects and case studies with problem, decisions, results, stack or method, personal role in team work; screenshots, demos, repositories. No "the best", no rankings of yourself [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). → EN-18
5. **Credentials explained**: title, issuing body (with link), year; for qualifications little known outside their country, explain what they are [SEJ 2026-08, Hunt]. No unverifiable credentials [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Legal notices required by local law: see Facts › Regulated professions and legal notices. → EN-14, EN-15
6. **Testimonials**: real text with name (or initials) and context; never stars in the markup of your own entity [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet). → EN-17
7. **One page per project or service**, descriptive URL, specific title ("Project X: … — First Last") instead of "Project" [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
8. **Own content before platforms**: publish on the site, then repost on LinkedIn or dev.to with a link back; weigh full syndication case by case [G](https://developers.google.com/search/help/office-hours/2024/june). → EN-23
9. **Real dates and updates**: do not change dates without substantial edits [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
10. **Bilingual sites** (e.g. Studio Ferri Orientamento with Italian pages plus English pages for international clients): separate URLs per language, same entity (same `@id`), reciprocal hreflang; name and qualifications consistent in both languages (see `international.md`).
11. **SPA**: title, H1, bio, contact details and JSON-LD in the served HTML (SSR/prerender); Google renders JavaScript, many AI-assistant crawlers do not (bot table in `ai-search.md`) [SEJ 2026-09]. → EN-28, EN-30

## Off-site checklist

Manual actions the skill can only guide.

**Identity and profiles**
- [ ] Write a **canonical definition** (name, role, specialisation, for whom, where, credentials) and reuse it identically or nearly so on the site, LinkedIn (headline, About, custom URL), the professional profiles relevant to the field (e.g. GitHub bio, site link and profile README for developers; ResearchGate for researchers), social profiles, and the Business Profile if one exists [SEJ 2026-05, Manic; SEJ 2026-09, Clarkson-Bennett].
- [ ] Add the **link to the site** in every profile [G](https://developers.google.com/search/help/office-hours/2023/december).
- [ ] Register **domains and handles** for your name and projects early (NanoClaw case: an impostor outranked the real site) and, for developers, reserve the **package namespaces** [SEJ 2026-03; SEJ 2026-09].
- [ ] Remove or update abandoned profiles, old bios, PDFs with outdated roles; where a title has changed, add a bridging sentence ("since 2025 …, previously …") [SEJ 2026-09, conflicting info].

**Google**
- [ ] Verify the domain in Search Console (Domain property); turn on the branded filter when available; annotate launches and changes [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter).
- [ ] Add platform properties (YouTube, Instagram, X, TikTok) if used [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide).
- [ ] If a knowledge panel appears: claim it as a verified representative and correct the data [G](https://developers.google.com/search/docs/appearance/establish-business-details).
- [ ] Search profile: only if in the US and above the follower threshold; otherwise no action [SEJ 2026-09].

**SERP for your own name (periodic audit)**
- [ ] Search "First Last", "First Last + role", "First Last + city" from a clean, logged-out browser, on mobile too; note date, language and location; look at autocomplete, images, news, maps [SEJ 2026-09, brand protection].
- [ ] Classify the results: own site / own profiles / homonyms / correct third parties / wrong third parties.
- [ ] Repeat on Bing and on assistants (ChatGPT, Gemini, Perplexity, AI Mode) with direct questions ("who is …") and without the name ("who would you recommend for …"), several times and in new conversations; record correct, outdated or false statements and statements about another person [SEJ 2026-09, Forrester; SEJ 2026-07].

**Mentions and PR (earned, not bought)**
- [ ] Talks, meetups, podcasts, interviews, guest articles **without optimised anchors**; turn every appearance into a page on the site (transcript, slides, link to the source) [SEJ 2026-09, Jarboe] · [G](https://developers.google.com/search/docs/essentials/spam-policies).
- [ ] Professional associations, registers, institutions, industry newsletters (national first, then regional) [SEJ 2026-07, Montti].
- [ ] Verifiable contributions: open source, repositories, awards with public criteria.
- [ ] Do not edit Wikipedia/Wikidata about yourself (conflict of interest; a platform rule, outside Google's documentation); do not buy mentions or Reddit posts.

**Sites built for clients (developers and agencies)**
- [ ] Footer credit link: `rel="nofollow"` or plain text, anchor = your own name or brand [G](https://developers.google.com/search/help/office-hours/2023/january).
- [ ] Prefer a **portfolio page** on your own site with a case study (with the client's permission) to the sitewide link.

## Notes by site type
- **editorial**: every author needs a byline leading to a `ProfilePage` author page and an `author` object with only the name in `name` (EN-13); fabricated authors are the main risk (EN-14).
- **local-business**: identity rules here apply to the owner and the brand; address, phone, Business Profile and reviews live in `local-seo.md`; legal notices in Facts › Regulated professions and legal notices.
- **personal-brand**: the default case of this file (e.g. Ada Novak): one entity home, `ProfilePage` + `Person`, own domain, consistent profiles, SERP for the name.
- **professional-services**: `Organization` with `vatID` when a registered business exists (EN-09); credentials explained and verifiable (EN-14, EN-15); the legal notices required by local law (e.g. Studio Ferri Orientamento shows its VAT number).
- **saas-product**: the entity is the product brand: `WebSite` + `Organization` on the home page, founders' and authors' pages for the blog; no self-ranking "best X" listicles (EN-18).

## Third-party views
Format: [SEJ YYYY-MM, author, evidence type and sample]. ⚠ = a claim that goes beyond or against Google; never turn it into a recommendation.

**Entity and consistency**
- [SEJ 2026-09, Clarkson-Bennett, opinion] Framework "Own → Describe → Prove → Earn → Monitor": owned assets (site, About, schema/sameAs, profiles, Business Profile), pages that point to the right entity, a verifiable identity for each person, corroborating mentions, monitoring for drift. For small brands, consistency matters more than anything.
- [SEJ 2026-06, Pollitt, opinion] Entity optimisation ≠ schema only: identical names and addresses everywhere, `sameAs` to authoritative profiles, an entity home linking to the profiles, clear taxonomy and internal links.
- [SEJ 2026-01, Clarkson-Bennett, opinion + unverified third-party figure] Answer early, consistent dates across page, schema and sitemap, the entity in the first paragraph, claim the Knowledge Panel if one exists.
- [SEJ 2026-09, author not stated, opinion with anonymous example] The main risk is **conflicting information** (old PDFs, bios with outdated titles): a "brand claim audit" and bridging sentences.
- [SEJ 2026-03, news Mueller] Old name persisting after a rebrand: use the domain as an alternate name; clean sitemaps.
- ⚠ [SEJ 2026-03, Baker, anecdote] "Person schema trains LLMs" (a homonymous CEO corrected after adding schema): no confirmation; [SEJ 2026-07, Forrester, opinion + literature] schema acts on the Knowledge Graph and on retrieval, not on model memory; [SEJ 2026-06, Williams-Cook, small experiment] LLMs read JSON-LD as text; an Ahrefs study (1,885 pages vs 4,000 controls) found no effect on citations. Summary: Person + `sameAs` are useful for disambiguation, not a citation lever.
- ⚠ [SEJ 2026-03, Yoast "Schemamap"] a single JSON-LD endpoint for agents: no engine reads it; the useful principle (entities with consistent `@id`, no duplicates) already applies for Google.

**Fabricated authors (dated update)**
- [SEJ 2026-10, news Google] SEJ reported Google changes dated 1 October 2026 on fake authors and fact-checking. Google's helpful-content page (last updated 5 October 2026) now names AI-generated headshots, made-up names and false credentials as deceptive authorship. Exact date and scope of the update: *(re-verify)*.

**Homonyms**
- [SEJ 2026-07, news Mueller + Montti opinion] `llms-author.txt` and "content-signal" are not used by any crawler; the homonym problem is solved by becoming better known (interviews, podcasts, pages), not with technical files.
- [SEJ 2026-09, Forrester, opinion with paper; declared commercial interest] For poorly documented entities, models "fill in" with the better-known neighbour (competitor, homonym, old version): query them without your name too.
- [SEJ 2026-08, Lily Ray, summary of studies] ChatGPT often uses `site:` and sometimes "guesses" the wrong official domain: state the official domain consistently across the web.

**Mentions and PR**
- [SEJ 2025-11, news Google, Robby Stein on a podcast] With fan-out, AI looks for lists and articles that cite businesses: being mentioned in public articles helps you be found; it is not a declared factor.
- [SEJ 2025-11, Ahrefs, correlation ~0.67, sample not detailed, vendor] Brand mentions on the web are the factor most correlated with presence in AI Overviews. Correlation, not cause.
- [SEJ 2026-08, Forrester, opinion + academic literature] "Parametric" knowledge of a name grows with independent sources and varied wording: it is built over years, not with campaigns.
- [SEJ 2026-09, Jarboe, unverified third-party data] Wikipedia, podcasts, Reddit and YouTube are heavily cited by assistants; turn every appearance into a transcript and a page.
- [SEJ 2026-04, Shepard, >400 sites, correlations 0.21–0.39] Associated with gains: own service or product, a task that can be completed, proprietary assets, a narrow topic, a **strong brand** (share of branded searches); cumulative effect.
- ⚠ [SEJ 2026-06, WordCamp panel] "Brand is the new backlink" and nofollow PR that "ranks you in AI": slogans and anecdotes.

**Spam and risks**
- [SEJ 2026-02, Lily Ray, observational, ~9 SaaS sites] Drops of 29–49% on sites with blogs of self-promotional listicles (together with mass AI content, dates updated without edits, improper `AggregateRating`).
- [SEJ 2026-06, Lily Ray, 100 queries × 3 dates, B2B SaaS] When AI cites the "best" list a brand wrote about itself, that brand was left out of the recommendation in 69% of cases; AI Overviews flag the "self-proclaimed".
- [SEJ 2026-01, news Mueller] Free hosting subdomains and cheap TLDs attract spam and make assessment harder: use your own domain for a portfolio (the article's inference).
- [SEJ 2026-03, NanoClaw case, anecdotal] An open source project without a website was outranked by an impostor site registered earlier; countermeasures (links from GitHub, schema, Search Console) were not enough in the short term.

**Measurement**
- [SEJ 2026-03, news Mueller] The branded filter cannot be customised, is not retroactive, and is not available for sub-properties or sites with few impressions; ⚠ the author links it to a patent on branded searches as a ranking signal: speculation (Google: the filter does not affect ranking).
- [SEJ 2025-11, AWR, Q3 2025 dataset] Desktop branded queries: position 1 loses CTR, positions 2–6 gain: the SERP for the name "widens".
- [SEJ 2026-07, Walsh, opinion] Build a direct audience (newsletter, followers, searches for the name) to reduce dependence on Google.

## Myths and outdated advice
- **"`Person` schema creates the Knowledge Panel / gets you cited by LLMs"** → no guarantee; structured data is not required for AI features [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"`llms.txt` / `llms-author.txt` disambiguate homonyms"** → ignored [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [SEJ 2026-07].
- **"E-E-A-T is a ranking factor; adding a bio and a byline is enough"** → it is not a factor; a byline alone does not improve ranking [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [SEJ 2026-10, Search Liaison quoted].
- **"The Search profile improves ranking"** → no; the benefit is in Discover, US only with a follower threshold [G](https://developers.google.com/search/docs/appearance/search-profiles) · [SEJ 2026-09].
- **"LinkedIn and GitHub can be monitored in Search Console"** → platform properties cover only Instagram, TikTok, X, YouTube [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide).
- **"The site name can be set for a subfolder (e.g. /blog or github.io/user)"** → only domains and subdomains [G](https://developers.google.com/search/docs/appearance/site-names).
- **"More 'built by' links on client sites = more authority"** → sitewide links in templates are an example of link spam [G](https://developers.google.com/search/docs/essentials/spam-policies).
- **"A 'best X' list with me at no. 1 helps in AI answers"** → grey area, drops observed [SEJ 2026-02/06]; inauthentic mentions are of little use [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"Stars in the SERP from client testimonials on my site"** → not eligible (self-serving) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **"Verifying Search Console improves ranking"** → no [G](https://developers.google.com/search/help/office-hours/2023/january).
- **"A keyword domain (e.g. ada-novak-angular-developer.example) helps"** → almost no effect; choose the name of the person or brand (adanovak.example) [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
- **"Generic or invented credentials to look like an expert"** → fabricated authors and credentials = deception [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content); dated update of 1 October 2026 per [SEJ 2026-10] *(re-verify)*.
