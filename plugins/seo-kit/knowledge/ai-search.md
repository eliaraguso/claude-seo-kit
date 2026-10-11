# AI search: AI Overviews, AI Mode and third-party assistants

> Updated 2026-10-11. Scope: visibility in Google's generative AI features (AI Overviews, AI Mode) and in third-party assistants (ChatGPT, Gemini app, Perplexity, Copilot, Claude, Siri); AI controls and AI bots. Primary source: Google Search Central; third-party views marked [SEJ] (October 2025 – October 2026).
> Legend: `[G](url)` = official Google documentation or blog · *(inference)* = a deduction of this file that no source states · **[SEJ YYYY-MM, author, type, sample]** = third-party source reported by Search Engine Journal · ⚠ = deprecated, unsupported by Google or otherwise not to be recommended.
> Evidence strength for third-party sources (used in [Third-party views](#third-party-views)): **Strong** (official statement or documentation of the vendor) · **Medium** (large study with a stated method, but correlational) · **Weak** (small sample, single account, vendor data) · **Opinion**.
> This file owns two shared tables: [Controls: what blocks what](#controls-what-blocks-what) and [AI crawlers and fetchers](#ai-crawlers-and-fetchers) (including which bots render JavaScript). Measurement (Search Console, GA4, Bing, prompt tracking): see `measurement.md`. Myths and outdated advice: see `myths-deprecated.md`.

## Contents
- [Facts and rules (Google)](#facts-and-rules-google)
  - [How AI Overviews and AI Mode work](#how-ai-overviews-and-ai-mode-work)
  - [Requirements to appear](#requirements-to-appear)
  - [Controls: what blocks what](#controls-what-blocks-what)
  - [What Google says not to do](#what-google-says-not-to-do)
  - [Content: what Google recommends](#content-what-google-recommends)
  - [Spam and manipulation of AI answers](#spam-and-manipulation-of-ai-answers)
  - [Google agents and fetchers](#google-agents-and-fetchers)
  - [AI crawlers and fetchers](#ai-crawlers-and-fetchers)
- [Audit checks](#audit-checks)
- [Procedures](#procedures)
  - [Procedure: AI access and eligibility](#procedure-ai-access-and-eligibility)
  - [Procedure: AI visibility with fixed questions](#procedure-ai-visibility-with-fixed-questions)
- [Build rules](#build-rules)
- [Notes by site type](#notes-by-site-type)
- [Third-party views](#third-party-views)
  - [Where assistants get their sources](#where-assistants-get-their-sources)
  - [AI bots and robots.txt](#ai-bots-and-robotstxt)
  - [What correlates with citations](#what-correlates-with-citations)
  - [Citable content structure](#citable-content-structure)
  - [JavaScript and AI bots](#javascript-and-ai-bots)
  - [Real traffic from chatbots](#real-traffic-from-chatbots)
- [Myths and outdated advice](#myths-and-outdated-advice)

---

## Facts and rules (Google)

### How AI Overviews and AI Mode work
- Google Search's generative AI features (AI Overviews, AI Mode) rest on the same ranking and quality systems as Search: for Google, **SEO remains relevant**. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Two declared techniques: **RAG / grounding** (the ranking systems retrieve relevant, up-to-date pages from the index; the answer shows clickable supporting links) and **query fan-out** (the model issues several related queries in parallel to gather more results; e.g. "lawn full of weeds" → "best weed killers", "remove weeds without chemicals", "prevent weeds"). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Fan-out works across several subtopics and several data sources; this is why AI answers show a **wider and more varied** set of links than a classic search. [G](https://developers.google.com/search/docs/appearance/ai-features)
- AI Overviews appear only when they add value over classic search, so they **often do not trigger**; AI Mode serves mainly queries that call for analysis, reasoning and complex comparisons. The two products can use different models and techniques: answers and links can differ. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Answers can include images, video, product listings and local business information; for the last two, **Merchant Center** and **Google Business Profile** matter. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- "AEO" and "GEO": for Google, optimising for generative AI search **is still SEO**; anyone weighing AEO/GEO consulting should compare it with the official guidance. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- The "preferred source" badge can also appear in AI Mode / AI Overviews, only for sites at domain or subdomain level that are included in the generative AI features in Search Console; useful mainly to news publishers. [G](https://developers.google.com/search/docs/appearance/preferred-sources)
- The ranking systems include **passage ranking** (evaluation of individual sections of a page). [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide)

### Requirements to appear
- To be a supporting link in AI Overviews or AI Mode, a page must be **indexed, eligible to be shown with a snippet**, and meet the Search technical requirements (Googlebot not blocked, HTTP 200, indexable content). **There are no additional technical requirements.** Crawling, indexing and serving are not guaranteed. [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/docs/essentials/technical)
- In addition, the site must be **included in Search generative AI features** through the Search Console setting. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) ([setting guide](https://support.google.com/webmasters/answer/16908024))
- Best practices listed by Google (none is "special" for AI): crawling allowed in robots.txt **and** by hosting/CDN; content reachable through internal links; good page experience; **important content in text form**; quality images and video in support; structured data consistent with the visible text; Merchant Center and Business Profile kept up to date. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Technical points in the 2026 guide: semantic HTML helps (screen readers) but "readability for people matters more than perfect code"; Google processes JavaScript if it is not blocked, but SEO for JS frameworks is "generally more complex"; reduce duplicates; crawl budget matters only for very large sites; verify the site in Search Console. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### Controls: what blocks what
AI in Google Search is part of Search: access is governed by **robots.txt for Googlebot**. There is no separate bot for AI Overviews / AI Mode. [G](https://developers.google.com/search/docs/appearance/ai-features) Other files point to this table for every AI opt-out question.

| Control | Where | Effect on Search, AI Overviews, AI Mode | Effect on Gemini apps / training | Source |
|---|---|---|---|---|
| `Disallow` for `Googlebot` in robots.txt | robots.txt | Googlebot stops crawling: the page leaves Search and therefore AI features too. Not an AI-only switch. | None by itself (Gemini uses Google-Extended, below) | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| `noindex` | robots meta tag or `X-Robots-Tag` | Page not shown in search results; since AI features require an indexed page, it is not a supporting link either | None documented | [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) · [G](https://developers.google.com/search/docs/appearance/ai-features) |
| `nosnippet` | robots meta tag or `X-Robots-Tag` | No snippet in any form of search results (web search, Images, Discover, AI Overviews, AI Mode) and the content is not used as a direct input for AI Overviews and AI Mode. Also removes the classic text snippet. | None documented | [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) |
| `max-snippet:[n]` | robots meta tag or `X-Robots-Tag` | Limits snippet length and how much of the content may be used as a direct input for AI Overviews and AI Mode. The limit does not apply where the publisher has separately granted permission for the content (e.g. structured data, licence agreement). | None documented | [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) |
| `data-nosnippet` | HTML attribute on `span`, `div`, `section` | Keeps the marked text out of snippets. Google's AI features page lists it among the controls that limit what is shown in Search; the robots meta tag page does not mention AI features for it. | None documented | [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) |
| `Google-Extended` | robots.txt token (no user agent of its own) | **None**: it does not affect inclusion in Search and is not a ranking signal, so it does not remove the site from AI Overviews or AI Mode | Controls whether crawled content is used for Gemini model training and grounding (Gemini Apps, Vertex AI API for Gemini, Grounding with Google Search on Vertex AI) | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) · [G](https://developers.google.com/search/docs/appearance/ai-features) |
| "Search generative AI" control | Search Console › Settings › Search generative AI | Excluding the site removes its links and content from AI Overviews, AI Mode and the generative AI features of Discover, and the content is not used to generate AI answers or previews there. Google states it is not a ranking or inclusion signal for the rest of Search. Exclusion takes effect within 1–2 days (some content longer, for caching). Rolled out to all websites worldwide as of 31 August 2026. | None documented | [G](https://support.google.com/webmasters/answer/16908024) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| robots.txt group per third-party bot | robots.txt | None on Google | Depends on the bot: see [AI crawlers and fetchers](#ai-crawlers-and-fetchers) | [G](https://developers.google.com/search/blog/2025/03/robotstxt-flexible-way-to-control) |

- The snippet controls (`nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`) also reduce classic snippets; the Search Console setting removes the site from AI features without touching classic snippets. [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) · [G](https://support.google.com/webmasters/answer/16908024)
- If a preview control "does not work": check with **URL Inspection** that it is in the HTML Googlebot sees; recrawling takes from days to months; a recrawl can be requested. [G](https://developers.google.com/search/docs/appearance/ai-features)
- History of the Search Console setting: first tested on a subset of sites from 17 June 2026, prompted by the UK regulator (CMA), then rolled out everywhere on 31 August 2026. [SEJ 2026-07/08/09, news on Google help, Strong] The rollout date is confirmed by the Google help page above.
- robots.txt choice for AI training crawlers: Google shows as an example a group that blocks a training bot while letting search engines through. It is an editorial choice of the owner. [G](https://developers.google.com/search/blog/2025/03/robotstxt-flexible-way-to-control)

### What Google says not to do
From the "myths" section of the official guide (15 May 2026) and the AI features page. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- **llms.txt and other files/markup/Markdown "for AI"**: Google Search does not use them; they neither help nor harm; they can be created for other services. No new machine-readable files, text files or "AI markup" are needed.
- **Splitting content into chunks**: not necessary; Google understands several topics on one page and shows the relevant part. **There is no ideal page length.**
- **Rewriting text just for AI** or chasing every long-tail variant: not necessary; the systems understand synonyms and meaning.
- **Seeking inauthentic mentions**: less useful than it seems; the core systems reward quality and other systems block spam.
- **Structured data "for AI"**: not needed for generative features, no special schema.org markup; it stays useful for rich results.
- **Separate pages for each query variant or fan-out query** created mainly to manipulate rankings or AI answers: they violate the **scaled content abuse** policy, and in any case many pages do not make a site better.
- **Trusting tools that claim Google "internal" metrics**: no third-party tool has access to Google's ranking or AI systems. [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)

### Content: what Google recommends
- Unique, useful and engaging content is, according to Google, the factor most likely to affect presence in generative search over the long term. Traits: a unique point of view (e.g. a first-hand review instead of a summary), **non-generic** content based on direct experience ("Why we stopped doing X" instead of "7 tips for X"), organisation in paragraphs and sections with headings, relevant images and video. Guiding question: "would my visitors find this satisfying?". [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- People asking AI use longer, more specific queries and ask follow-ups; the same fundamentals apply (people-first content, page experience, technical accessibility, consistent structured data, multimodal content). [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search)
- Content created with generative AI: useful for research and structure; generating many pages without value can violate scaled content abuse; take care over the accuracy of `<title>`, meta description, structured data and alt text too; explain to readers how content was created when they would expect it; ecommerce: AI images with IPTC `DigitalSourceType = TrainedAlgorithmicMedia`. [G](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- Update of 1 October 2026, first reported by [SEJ 2026-10, news on Google docs]: the English "Using generative AI content" page (updated 1 October 2026) now states it is critical to **manually fact-check and review all AI-generated content** before publishing, including metadata (title elements, meta descriptions, structured data, alt text) [G](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content); the people-first guide (updated 5 October 2026) warns against **deceptive authorship information** (invented names, AI-generated headshots, false qualifications) as a signal of a low-quality page [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Both checked on the English pages on 2026-10-11; translated versions may lag.
- Google states that clicks from pages with AI Overviews are "higher quality" (more time on site) and invites site owners to measure conversions, not just clicks. It is a Google statement, without public data. [G](https://developers.google.com/search/docs/appearance/ai-features)

### Spam and manipulation of AI answers
- The spam policies also define as spam the techniques used to **manipulate generative AI answers** in Search. [G](https://developers.google.com/search/docs/essentials/spam-policies) SEJ dates the clarification to 15 May 2026, with examples such as buying or altering citations. [SEJ 2026-06/08, news, Strong]
- Scaled content abuse "no matter how it is created" (AI, people, a mix); AI in itself is not spam. [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)
- Other policies relevant to "GEO" tactics: hidden text, cloaking, link spam, fake or undisclosed incentivised reviews (review snippet guidelines, possible manual action). [G](https://developers.google.com/search/docs/essentials/spam-policies)
- Outside Google: the Bing guidelines (rewritten in early 2026) have a section "Prompt Injection and AI Manipulation" and one on artificially engineered language. [SEJ 2026-02, news on Microsoft docs, Strong] Microsoft Defender documented 31 companies with "Summarize with AI" buttons that inject hidden instructions ("AI Recommendation Poisoning"). [SEJ 2026-02, Microsoft research, 60 days of URLs] → a tactic to report as risky.

### Google agents and fetchers
- AI agents (e.g. browser agents) can read screenshots, the DOM and the **accessibility tree**; Google refers to the web.dev guide on agent-friendly sites and mentions the emerging UCP protocol. Optional section: "if it is relevant and you have time". [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- `Google-Agent` (March 2026; agents hosted on Google infrastructure that navigate the web and perform actions on user request) and `Google-GeminiNotebook` (URLs users add as sources; support for the former token `Google-NotebookLM` ended in August 2026) are **user-triggered fetchers**: because the fetch was requested by a user, they **generally ignore robots.txt**. IPs are published in `user-triggered-agents.json` / `user-triggered-fetchers*.json`; Google is experimenting with Web Bot Auth (identity `https://agent.bot.goog`). [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) · [G](https://developers.google.com/crawling/docs/changelog)
- To really block an area you need authentication, not robots.txt. *(inference)*

### AI crawlers and fetchers
Owner table for "which bot does what, and which renders JavaScript"; other files point here. Purpose values: **search** (classic index) · **ai-training** · **ai-search** (index used by an AI answer engine) · **user-fetch** (fetch triggered by a user's request). Google rows are Google documentation; the other rows rely on the operators' own documentation as reported by SEJ.

| Bot | Operator | Purpose | Respects robots.txt | Renders JS | How to block | Source |
|---|---|---|---|---|---|---|
| `Googlebot` | Google | search (Search including AI Overviews / AI Mode, Discover, Images, Video, News) | Yes | **Yes** (evergreen Chromium) | Do not block if the site wants Search; to limit AI use, see [Controls](#controls-what-blocks-what) | [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) |
| `Google-Extended` | Google | ai-training (Gemini training and grounding) | It is a robots.txt token, not a crawler: crawling uses Google's existing user agents | Not applicable (no crawler of its own) | `User-agent: Google-Extended` + `Disallow: /`; no effect on Search or AI Overviews | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| `Google-Agent`, `Google-GeminiNotebook` | Google | user-fetch | **Generally no** (user-triggered) | Not documented | Authentication or server rules; IP lists in `user-triggered-agents.json` / `user-triggered-fetchers-google.json` | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) |
| `GPTBot` | OpenAI | ai-training | Yes (declared) | Not documented (third-party test: no) | robots.txt group | [SEJ 2025-11/2026-01, list from logs + OpenAI docs] |
| `OAI-SearchBot` | OpenAI | ai-search (ChatGPT search index; blocking it reduces presence in answers) | Yes | Not documented (third-party test: no) | robots.txt group (removes the site from ChatGPT search) | [SEJ 2026-01, OpenAI docs cited, Strong] |
| `ChatGPT-User` | OpenAI | user-fetch | No longer guaranteed (OpenAI docs updated) | Not documented (third-party test: no) | Server or WAF rules; robots.txt may be ignored | [SEJ 2026-07, Pollitt, Strong] |
| `ClaudeBot` | Anthropic | ai-training | Yes (declared) | Not documented (third-party test: no) | robots.txt group | [SEJ 2025-11, 2026-05] · Anthropic help center (link below) |
| `Claude-SearchBot` | Anthropic | ai-search | Yes (declared) | Not documented (third-party test: no) | robots.txt group | [SEJ 2025-11, 2026-05] · Anthropic help center (link below) |
| `Claude-User` | Anthropic | user-fetch | Anthropic states that its bots, this one included, honour robots.txt; as with every user-triggered fetcher, do not rely on robots.txt for private areas *(inference)* | Not documented (third-party test: no) | robots.txt group; authentication for private areas | Anthropic help center (link below) · [SEJ 2025-11, 2026-05] |
| `PerplexityBot` | Perplexity | ai-search (index) | Yes | Not documented (third-party test: no) | robots.txt group | [SEJ 2026-07] |
| `Perplexity-User` | Perplexity | user-fetch | Not guaranteed | Not documented (third-party test: no) | Server or WAF rules | [SEJ 2026-07] |
| `Bingbot` | Microsoft | search (Bing index, feeds Copilot) | Yes | Not documented in the sources of this file *(re-verify against Bing docs)* | robots.txt group (also removes the site from Bing and Copilot) | [SEJ 2025-11] |
| `Applebot` | Apple | search (Spotlight, Siri, Safari) | Yes; if there is no Applebot group it follows the Googlebot rules | Not documented (third-party test: yes) | robots.txt group | [SEJ 2026-06, Apple docs] |
| `Applebot-Extended` | Apple | ai-training (opt-out token) | robots.txt token | Not applicable | `User-agent: Applebot-Extended` + `Disallow: /` | [SEJ 2026-06, Apple docs] |
| `CCBot` | Common Crawl | ai-training (archive used to train many models; blocking stops future collection, does not remove the archive) | Yes; the name is often spoofed | Not documented (third-party sources disagree) | robots.txt group + IP verification | [SEJ 2026-06/08] |

- **User-triggered fetchers can ignore robots.txt.** Google says its own (`Google-Agent`, `Google-GeminiNotebook`) generally do, because the fetch was requested by a user [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers); OpenAI and Perplexity no longer guarantee it for `ChatGPT-User` and `Perplexity-User` [SEJ 2026-07]; Anthropic states that all its bots, `Claude-User` included, honour robots.txt [Anthropic help center](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler). For anything that must stay private, use authentication. *(inference)*
- "Renders JS": only Googlebot is documented to render JavaScript. "Third-party test" values come from the Vercel 2024 test with later checks [SEJ 2025-12, Vercel/Gabe, test, Medium]; see [JavaScript and AI bots](#javascript-and-ai-bots). Practical consequence *(inference)*: if the goal includes ChatGPT, Claude or Perplexity, essential content must be in the initial HTML.
- Verify bot names in logs before drawing conclusions: user agents are spoofed often (check AI-10).

---

## Audit checks

| ID | Check | How to verify | Severity | Source |
|---|---|---|---|---|
| AI-01 | Key pages indexed and eligible for a snippet | URL Inspection on home and service/project pages; look for `noindex`, `nosnippet`, a low `max-snippet`, `data-nosnippet` on important blocks, also in the `X-Robots-Tag` header | High | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| AI-02 | Googlebot not blocked by robots.txt, CDN or WAF | Live URL test (rendered screenshot: blank page or "are you human?" = problem); logs by Google IP; temporary blocks only with 503/429 | High | [G](https://developers.google.com/search/blog/2024/12/crawling-december-cdns) |
| AI-03 | Search Console "Search generative AI" setting not switched off by mistake | Search Console → Settings → Search generative AI; if exclusion is active, ask the owner whether it is intended; before turning it on, save a baseline of the AI report | High | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [G](https://support.google.com/webmasters/answer/16908024), [SEJ 2026-08, Shehata, opinion] |
| AI-04 | Important content in HTML text | Prices, services, opening hours, credentials, contacts, answers: in text, not only in images, canvas, PDF, video or widgets | High | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| AI-05 | Initial vs rendered HTML | `curl -A` / view-source vs URL Inspection; if key text appears only after JS: for Google it is enough that rendering works, but "not all bots can run JavaScript" → SSR/prerender for content pages. Never a different version only for bots. Caveat: applies to single-page apps and other client-rendered pages | High | [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [SEJ 2025-12, Vercel/Gabe, test] |
| AI-06 | Preview controls as a deliberate choice | If the owner wants out of AI features without losing classic snippets: consider the Search Console exclusion instead of `nosnippet` (see [Controls](#controls-what-blocks-what)) | Medium | [G](https://developers.google.com/search/docs/appearance/ai-features), [SEJ 2026-07, news] |
| AI-07 | Google-Extended correctly understood | Explain that blocking it does not remove the site from AI Overviews / AI Mode and does not affect ranking; it only covers Gemini training/grounding | Low | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| AI-08 | Explicit policy on third-party AI bots | Classify bots into training / search indexing / user fetch (see [AI crawlers and fetchers](#ai-crawlers-and-fetchers)); ask the owner whether they want to be cited; write robots.txt accordingly; remember user fetchers may ignore it. Caveat: High when the owner wants visibility in AI assistants | Medium | [SEJ 2026-07, Pollitt, opinion-guide] |
| AI-09 | CDN blocking bots by default | Check Cloudflare rules (AI crawlers blocked by default since July 2025; "AI training" / Bot Preference Sync settings since 15 September 2026) and verify that Googlebot and Bingbot get through. Caveat: SEJ reports conflicting accounts of how the Cloudflare AI settings affect Googlebot; confirm on the live site with the URL Inspection live test and logs | High | [SEJ 2025-12 and 2026-08/09, news, Strong on Cloudflare] |
| AI-10 | Logs: real or fake bots | Check IPs against the published lists (Google `common-crawlers.json`, OpenAI, Anthropic, Perplexity, Common Crawl) and reverse DNS; states: verified / fake / not verifiable | Medium | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests), [SEJ 2026-06, Forrester, 1 site 14 days] |
| AI-11 | Content that is not "commodity" | For each key page: what does it offer that cannot be found elsewhere (cases, own data, experience)? Apply Google's self-assessment questions | High | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| AI-12 | No page per variant or fan-out query | Look for near-identical pages per city/variant/question; consolidate with 301; one strong page per intent | High | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| AI-13 | Structured data only if consistent with what is visible | Validate (Rich Results Test / validator.schema.org); no "schema for AI"; no `AggregateRating` on self-published reviews (rule owned by SD-16) | Medium | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| AI-14 | Business Profile and Merchant Center up to date | Opening hours, services, area, photos, category; product feed if ecommerce. Caveat: applies to local-business and ecommerce sites | High | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| AI-15 | Consistent identity across the web | Name, bio, name/address/phone, services identical on site, schema, Business Profile, social profiles, directories; fix outdated sources | Medium | [G](https://developers.google.com/search/docs/appearance/establish-business-details), [SEJ 2026-07/09, several authors, opinion+vendor] |
| AI-16 | No speculative tactics as a lever | llms.txt, Markdown mirrors, chunking, "AI schema": do not propose them; if present they are not an error (Google ignores them) | Low | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| AI-17 | No manipulation | Look for hidden text with instructions for LLMs, "Summarize with AI" buttons with preloaded prompts, bought reviews/mentions, self-promotional listicles | Critical | [G](https://developers.google.com/search/docs/essentials/spam-policies), [SEJ 2026-02, Microsoft] |
| AI-18 | Agent-ready (optional) | Real `<a href>` links, native buttons with a name, forms with `label`, no CAPTCHA/modal blocking the contact flow, stable layout; do not block Google-Agent IPs. Caveat: Medium when an agent cannot complete the contact or booking flow | Low | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [SEJ 2026-05, Manic, opinion] |
| AI-19 | Bing indexes the site | Verify in Bing Webmaster Tools, submit the sitemap, consider IndexNow (Bing feeds Copilot and, according to third parties, other assistants) | Medium | [SEJ 2026-03/05, Microsoft news + opinions] |
| AI-20 | Accuracy of what AI assistants say about the entity | Fact prompts (who it is, what it offers, where, prices) on several assistants; fix wrong sources; see [Procedure: AI visibility with fixed questions](#procedure-ai-visibility-with-fixed-questions) and `measurement.md` | Medium | [SEJ 2026-07/09, Manic, Forrester, opinion] |

---

## Procedures

### Procedure: AI access and eligibility
Order of checks for "why are we not in AI Overviews / AI Mode". Each step maps to a check; stop at the first failure.
1. **Search Console setting**: Settings › Search generative AI is not set to exclude the site (AI-03). [G](https://support.google.com/webmasters/answer/16908024)
2. **Googlebot access**: robots.txt, CDN and WAF let Googlebot through; for Cloudflare, check the AI crawler settings too (AI-02, AI-09). [G](https://developers.google.com/search/blog/2024/12/crawling-december-cdns)
3. **Indexing and snippet eligibility**: URL Inspection on key pages; no `noindex`, `nosnippet`, low `max-snippet` or `data-nosnippet` on key blocks, also in headers (AI-01). [G](https://developers.google.com/search/docs/appearance/ai-features)
4. **Content in text**: key facts in the HTML text and present in the rendered HTML Google sees (AI-04, AI-05).
5. **Third-party assistants**: robots.txt groups match the owner's policy (AI-08); Bing indexes the site (AI-19).
6. Only then look at content quality and identity (AI-11, AI-12, AI-15). AI Overviews often do not trigger at all for a query: absence is not proof of a problem. [G](https://developers.google.com/search/docs/appearance/ai-features)

### Procedure: AI visibility with fixed questions
No official metric exists for third-party assistants; Google points to its own AI report in Search Console and warns against tools that promise internal metrics. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) The steps below summarise SEJ practices (Opinion; results only as a trend). The full protocol and the log template are owned by `measurement.md` (procedure "measuring visibility in AI assistants"); the fixed questions are stored in `SEO.md › 9. Monitoring` so that every run uses the same set.
1. **Accuracy before visibility** (AI-20): 5–10 fact prompts (who/what is [name], where it operates, what it offers, prices, is it reliable?); classify each claim: correct, outdated, unsupported, false, about another entity. [SEJ 2026-07/09, Manic, Forrester]
2. **Fixed set of decision questions**: 10–20 real questions from the audience (customer questions, Search Console queries, reviews), e.g. "best physiotherapist in Oslo for running injuries", "alternatives to …", "[service] online cost". Never change them between runs. [SEJ 2026-08, consultant, ~12 startups]
3. **Engines**: AI Overviews / AI Mode, ChatGPT, Gemini, Perplexity, Copilot (and Claude if relevant); measure **per engine**, not with a single score, because cited sources almost never overlap. [SEJ 2026-05, Indig/Omnia]
4. **Repetitions**: 3–5 runs per question and engine, in new conversations without memory; record date, account type, model, location, language. [SEJ 2026-07, Fishkin/SparkToro; SEJ 2026-08]
5. **Reading**: share of presence per engine and per question group, compared quarter on quarter; fix the wrong sources found in step 1 before chasing presence. Presence in answers is not a ranking and not a business KPI. [SEJ 2026-07, Forrester; Manic]
6. **Frequency**: monthly for sites with active PR/content work, quarterly for small sites. [SEJ 2025-12/2026-06, several authors]

---

## Build rules
- Keep key pages indexable and snippet-eligible; use snippet controls only on purpose → AI-01, AI-06.
- Never block Googlebot at robots.txt, CDN or WAF; check the CDN's AI-bot defaults at launch → AI-02, AI-09.
- Put prices, services, hours, credentials and contacts in HTML text, server-rendered or prerendered for content pages, same version for everyone → AI-04, AI-05.
- Leave the Search Console "Search generative AI" setting on unless the owner decides otherwise, and record the decision in `SEO.md › 8. Decisions and constraints` → AI-03.
- Write the robots.txt AI-bot policy with the owner (training vs AI search vs user fetch); Google-Extended is a training choice, not a Search switch → AI-07, AI-08.
- One strong page per intent; no page per city, variant or fan-out query → AI-12.
- Structured data only when it matches visible content; no "AI schema", no llms.txt as a lever → AI-13, AI-16.
- No hidden prompts, "Summarize with AI" injections or bought mentions → AI-17.
- Real links, native buttons, labelled forms, no CAPTCHA in the contact flow → AI-18.
- Keep identity data identical everywhere; keep Business Profile / Merchant Center current → AI-14, AI-15.

---

## Notes by site type
Archetypes as in `archetypes.md`.

**ecommerce**
- Merchant Center (feed) and up-to-date product data also feed AI answers: product listings can appear in AI Overviews and AI Mode, and Google names Merchant Center as the way to keep that data current. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) Check price, availability and variants in the feed match the product page (AI-14).
- AI-generated product images: mark them with IPTC `DigitalSourceType = TrainedAlgorithmicMedia`. [G](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- Agentic protocols (UCP, ACP) and checkout through agents: only if the platform supports them; no impact data [SEJ 2026-01/09]. For an example such as Acme Widgets, the product page (specs, sizes, shipping and returns in text) is the citable source, not the category listing *(inference)*.

**editorial**
- Main risk: generic informational content, the most absorbed by AI answers and the most hit in clicks [SEJ 2026-03/05, data from several sources]. Focus on direct experience, original data, real authors.
- The "preferred source" badge (button or deep link) is useful mainly for news. [G](https://developers.google.com/search/docs/appearance/preferred-sources)

**local-business**
- Google: for local AI answers, an up-to-date **Business Profile** and consistent information matter. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Third parties: name, address, phone, hours, services and service area identical on site, Business Profile, Apple/Bing Places and directories; real reviews with replies; mentions from associations and local press [SEJ 2026-07/09, data from local vendors, Weak-Medium]. Local AI lists are unstable: repeating the same search on Gemini, the same business was on top only in ~7% of cases vs ~90% in the local pack [SEJ 2026-09, Steady Demand, Weak].
- No cloned "service + city" pages to chase fan-out (doorway / scaled content), e.g. Northwind Physio keeps one page per service, not one per Oslo district.

**personal-brand**
- Realistic AI goal: assistants describe the person correctly (name, role, skills, city) and associate them with a niche; traffic from AI will be minimal *(inference)*.
- Levers: an "About" page in HTML text with verifiable facts, identical name and bio on site and professional/social profiles, case studies with experience and own data, authentic external mentions (talks, articles, podcasts, open source) [SEJ 2026-01/09, converging opinion]. `Person` + `sameAs` helps disambiguation; it is not a guaranteed citation lever [SEJ 2026-06/08].
- Namesakes: periodic audit of what assistants say about the name (AI-20); "bridge" content if role or titles have changed [SEJ 2026-09, opinion].
- Portfolio built as an SPA (Angular, React, Vue): AI-05 is blocking for AI bots; use SSR/prerender.
- Bots: a person who wants to be found by clients or employers through assistants (e.g. Ada Novak) should not block OAI-SearchBot, Claude-SearchBot, PerplexityBot, ChatGPT-User *(inference)*.

**professional-services**
- Google: Business Profile and consistent information matter also for professionals with a service area. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Prices or price ranges, delivery mode (online / in person), timing and booking in text, with the call to action near the top for visitors already convinced by an assistant [SEJ 2026-06, Manic, opinion]. Mentions from professional bodies and associations help [SEJ 2026-07/09, Weak-Medium].
- No cloned "service + city" pages (doorway / scaled content).
- Topics close to work, health or money: no promises, real and verifiable credentials (see `content-quality-spam.md`).

**saas-product**
- "X vs Y" comparisons and alternatives are the main ground for AI answers [SEJ 2026-08, study with minimal n]; honest comparison pages, indexable documentation, reviews on third-party platforms. Avoid "best of" listicles that put yourself first: associated with drops and, when cited, the brand is often excluded from the recommendation [SEJ 2026-07, Lily Ray, 100 queries, Weak].
- Documentation pages can serve as citation sources for "how do I…" questions: keep them public, in the initial HTML (not only in a client-rendered docs app), linked from the main site, with one canonical version per page *(inference)*. Same requirements as any page: indexed and snippet-eligible (AI-01, AI-05).

---

## Third-party views

### Where assistants get their sources
No third-party vendor publishes its source-selection factors. What follows are vendor statements (Strong) or third-party reconstructions (Weak/Medium).

| Assistant | Source of results (according to whom) | Evidence |
|---|---|---|
| AI Overviews / AI Mode | Google's index and ranking systems | Google fact [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| Gemini (app) | Google infrastructure; Google-Extended controls training and grounding in Gemini apps | Google fact [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| ChatGPT | Own bots (OAI-SearchBot for the search index); internal index "labrador" that also serves unlicensed sites, with local results and products almost always from there on free accounts; in "thinking" mode ~75% from Google results collected with scrapers; historically also Bing | [SEJ 2026-08, Resoneo/Mohanadasan, 1,249 answers, Weak-Medium] [SEJ 2026-07, single researcher, Weak] [SEJ 2026-02, Lily Ray, 11 subfolders, Weak] Conflicting reconstructions |
| Perplexity | Almost always retrieves; own pipeline (Brave hypothesised); for local queries the maps index / Business Profile weighs | [SEJ 2026-02/06/08, opinions + study with minimal n, Weak] |
| Claude | Brave Search according to some authors | [SEJ 2026-01/05, opinion, Weak] *(re-verify)* |
| Copilot / Bing | Bing index; Web IQ grounding API returning passages, used by Copilot and (Microsoft statement) by ChatGPT | [SEJ 2026-07, Microsoft news, Strong for Copilot] |
| Siri (Apple) | Applebot; `Applebot-Extended` for training; `nosnippet` prevents the page being used as context for AI answers | [SEJ 2026-06, Apple docs, Strong] |

- Cited sources vary a lot between engines: AI Mode and AI Overviews agreed in 86% of answers but cited the same URLs in only 13.7% [SEJ 2025-12, Ahrefs, 730,000 query pairs, Medium]; only 2.37% of cited URLs appeared in ChatGPT, Perplexity and AI Overviews for the same prompt [SEJ 2026-05, Indig/Omnia, 20,000 prompts, Medium].
- AI Overviews cite the organic top 10 less and less: 38% of cited pages (it was ~75% at the end of 2024) [SEJ 2026-05, Ahrefs, 4M URLs, Medium]; ~17% according to BrightEdge [vendor, Weak]. ~90% of the pages cited by ChatGPT ranked beyond position 20 for related queries [SEJ 2026-08, Semrush cited, Weak].
- But an organic drop on Google was reflected in citations: −27.8% ChatGPT, −23.8% AI Mode, −2.9% Perplexity [SEJ 2026-02, Lily Ray, 11 selected subfolders, Weak]. Cautious reading *(inference)*: classic SEO is a useful but not sufficient condition; each engine has to be measured separately.

### AI bots and robots.txt
The bot-by-bot table lives in [AI crawlers and fetchers](#ai-crawlers-and-fetchers). Third-party data around it:
- Volumes: AI crawling ~89% training, 8% search, 2% user fetch [SEJ 2026-05, Cloudflare Radar Q1 2026, Strong on the Cloudflare data]; another measure: 57% user fetch (almost all ChatGPT) [SEJ 2026-05, Duda, 68.9M visits, one platform]. Crawl-to-referral ratios were very unbalanced for Anthropic and OpenAI compared with Google (ClaudeBot from ~20,600:1 to ~70,900:1 depending on the period) [SEJ 2025-12/2026-05/07, Cloudflare, different figures per period].
- Blocking training bots is a choice; blocking search and user-fetch bots reduces presence in answers [SEJ 2025-12/2026-06, converging opinion]. Bot names have to be verified: on a new site 81.8% of AI "live fetches" and 87% of "Googlebot" requests were fake [SEJ 2026-06, Forrester, 1 site, 14 days, Weak].
- Example robots.txt for a site that wants to be cited but not to train models *(inference, to adapt with the owner)*:
  ```
  User-agent: GPTBot
  Disallow: /
  User-agent: ClaudeBot
  Disallow: /
  User-agent: CCBot
  Disallow: /
  User-agent: Google-Extended
  Disallow: /
  User-agent: Applebot-Extended
  Disallow: /
  User-agent: *
  Allow: /
  Sitemap: https://www.example.com/sitemap.xml
  ```
  Note: Google does not support `crawl-delay` or fields other than user-agent/allow/disallow/sitemap. [G](https://developers.google.com/search/blog/2025/03/robots-future)

### What correlates with citations
All correlations or observations; no controlled study shows causes, except the (negative) test on schema.

| Factor | What emerges | Evidence | Relation to Google |
|---|---|---|---|
| Brand mentions on the web | Highest correlation (~0.67) with frequency in AI Overviews | [SEJ 2025-11, Ahrefs, vendor, sample not detailed] Medium-Weak | Google: **authentic** mentions yes (Stein: AI with fan-out looks for lists and articles that mention businesses [SEJ 2025-11, Google statement]); inauthentic mentions of little use, and manipulation = spam |
| Earned media / third-party sources | ~84% of links cited by LLMs are earned mentions; 77% of citations on brand queries come from off-site | [SEJ 2026-07, Muck Rack 25M links; Omniscient] Weak (vendor; another article reports "25% of citations" for Muck Rack [SEJ 2026-05]: inconsistent figures) | Consistent with "quality content + spam signals" |
| Brand already "known" to the model | Brands the model inserted in its own query appeared in 68.9% of answers, those only retrieved in 2.1% | [SEJ 2026-08, Mohanadasan, 1 account, 57 conversations, "directional only"] Weak | No Google position |
| Direct experience / own data | First-party research ~3.3x citations; sites with mass AI content: 54% lost ≥30% | [SEJ 2026-07, Indig] [SEJ 2026-05, Lily Ray, 220+ sites, observational] Medium-Weak | Aligned with the Google guide (non-generic content) |
| Declarative opening, dates and numbers in the intro | "X is Y" opening +14%; DATE and NUMBER positive; price in the opening negative | [SEJ 2026-03, Indig, ~98,000 ChatGPT citations, 7 B2B verticals] Medium, ChatGPT only | Google: write for people, no format rule |
| Position in the text | 44% of citations from the first 30% of the text | [SEJ 2026-02, Indig, 18,012 ChatGPT citations] Medium, ChatGPT only | No Google position |
| H1 and top of page | The ChatGPT index keeps title + ~200 initial characters; H1 in 83.6% of snippets | [SEJ 2026-08, Resoneo, 534 pages] Weak-Medium; not tested whether changing it increases citations | Google uses H1 for title links |
| Too many pages on the same topic | Citation yield 1.7% with 6+ pages from the same domain vs 4–6% with 1–2 | [SEJ 2026-08, Mohanadasan, 1 account] Weak | Consistent with "consolidate duplicates" |
| Structured data (JSON-LD) | Adding JSON-LD: no significant increase (AIO −4.6%, AI Mode +2.4%, ChatGPT +2.2%) | [SEJ 2026-05/06, Ahrefs, 1,885 pages vs 4,000 controls, diff-in-diff] Medium (best available design; criticism: pages already heavily cited) | Google: not needed for AI |
| llms.txt | 97% of files never requested; no effect across 300,000 domains; adoption ~2%, often via plugins | [SEJ 2026-06, Ahrefs 137,000 domains; SE Ranking; Web Almanac] Medium | Google: ignored |
| Reddit / UGC | ChatGPT: corporate content 94.7%, Reddit 2–5% (almost zero in finance/health); Reddit share in ChatGPT −86% in 3 weeks (summer 2026); in AIO/Perplexity Reddit more present | [SEJ 2026-03, Indig] [SEJ 2026-08] Medium-Weak, highly variable | Buying presence on Reddit = manipulation |
| Freshness | ~30-day window observed in ChatGPT for commercial questions | [SEJ 2026-09, one observer] Weak | Google: no changed dates without real changes |

Summary *(inference)*: the levers with the most solid evidence that are consistent with Google are (1) being indexable and readable, (2) non-generic content with verifiable facts, (3) authentic off-site reputation and mentions. Schema, llms.txt, chunking and "magic" formats have no evidence.

### Citable content structure
- Google: organise for people (paragraphs, sections, headings), no chunking needed, no ideal length. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Practices on which third-party authors and the Bing/Microsoft guidelines converge [SEJ 2026-01/03, Microsoft guidelines, Strong for Bing; opinions for the rest]:
  - a clear answer at the start of the page or section, then the detail;
  - self-contained sections with descriptive headings, also in the form of a real question;
  - explicit facts with numbers, units, dates and proper names close to the sentence that uses them;
  - tables or lists for tabular data and comparisons;
  - **key information not hidden in closed tabs/accordions** (Bing: AI might not render it; Google: limits "Read more" deep links [G](https://developers.google.com/search/docs/appearance/snippet));
  - one page per intent; state "who it is for / not for", delivery mode, price range, limits;
  - recognisable author, visible and real date.
- ⚠ Figures not supported by Google nor replicated: 150–300-word blocks, 200–500-character chunks, "answer in the first 2 sentences", word or heading thresholds. [SEJ 2025-10/12, 2026-02, opinions and correlations] Do not use them as rules.
- Useful method [SEJ 2026-01/09, opinion]: derive the sub-questions (fan-out) from real customer questions, competitors' reviews, calls and Search Console queries, not from generated lists; without creating a page for each (AI-12).

### JavaScript and AI bots
- Google runs JavaScript, but writes that server-side or pre-rendering is "still a great idea" because it is faster and because **not all bots can run JavaScript**. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Third-party tests: the bots of OpenAI, Anthropic, Meta, ByteDance and Perplexity did not execute JS; Gemini (Googlebot infrastructure) and Applebot did. [SEJ 2025-12, Vercel 2024 test + checks by Gabe, Medium] An earlier version of this file also listed CCBot as rendering; sources disagree and Common Crawl does not document it, so the bot table says "not documented" *(re-verify)*. Study of 274 homepages: 36% had less than 80% of their content in the raw HTML. [SEJ 2026-06, industry study, Weak-Medium]
- ⚠ On 4 March 2026 Google removed from its JS guide the recommendation to test with JavaScript disabled (no longer current for Google). Many authors still propose it for AI bots: it is a valid test for third-party bots, not a Google requirement. [SEJ 2026-03, changelog news]
- ⚠ Serving a no-JS version only to bots: cloaking risk; dynamic rendering is a discouraged workaround. Use SSR/prerender, the same for everyone. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering)

### Real traffic from chatbots
- Volume: LLMs ~1.08% of sessions [SEJ 2026-03, Conductor, 13,770 domains, Medium]; all AI ~0.24% of global traffic, ChatGPT ~80% of AI referrals [SEJ 2026-04, SE Ranking, 101,000 sites, vendor]; <1% of referrals for publishers [SEJ 2026-03, Chartbeat]; 1–2% of customer calls from AI citations [SEJ 2026-09, CallRail, vendor]. Share of visits across AI platforms (May 2026): ChatGPT ~53%, Gemini ~28%, Claude ~9%, Perplexity ~1% [SEJ 2026-09, Similarweb].
- Value: opposite data. Conversions 11x organic [SEJ 2026-07, Microsoft Clarity, 1,200 publisher sites] against conversions lower than almost every channel [SEJ 2026-07, Marketing Science, 973 sites]; "2–4x" [SEJ 2026-03, Forrester, no sample]. Reading *(inference)*: a small, uneven channel, to be measured on the site's own data.
- Messy attribution: many ChatGPT users arrive as "Direct" [SEJ 2025-10, guide, opinion]; at one agency 80–90% of AI leads were classified organic/direct [SEJ 2026-08, data from one agency]; 58.8% of AI traffic landed on the home page while 65% of citations were on inner pages [SEJ 2026-08, Solís].
- Effect on clicks from Google: with an AI summary, clicks on 8% of visits vs 15% without [SEJ 2026-01, Pew cited, US data]; −38% clicks in a randomised experiment [SEJ 2026-05, ISB/CMU, 1,065 users, Medium-Strong]; −58% CTR in position 1 [SEJ 2025-12/2026-03, Ahrefs, 300,000 keywords]; brand queries with AIO +18% CTR [SEJ 2026-03, Amsive]. Google maintains that clicks from AIO are of higher quality. [G](https://developers.google.com/search/docs/appearance/ai-features)

---

## Myths and outdated advice
⚠ All beyond or against Google; no evidence of measured benefit. One-line entries with sources live in `myths-deprecated.md` (theme AI); do not recommend any of these.
- llms.txt, `llms-author.txt`, Content-Signal in robots.txt, Markdown mirrors "for agents", "AI Instructions", OKF/ARD, schemamap, WebMCP/MCP/NLWeb for content sites. [SEJ 2025-11 → 2026-09, many sources; Mueller: llms.txt "purely speculative"] (Lighthouse has an experimental "Agentic Browsing" audit that checks llms.txt: it only verifies syntax and says nothing about effects on Search [SEJ 2026-06/07].) Google's own position: see [What Google says not to do](#what-google-says-not-to-do).
- Chunking content into fixed-size blocks, fixed word counts, "answer in the first two sentences" as rules: see [Citable content structure](#citable-content-structure).
- "Schema to get cited", FAQPage "critical for GEO", knowledge graph/Wikidata "for AI". [SEJ 2025-12 → 2026-09] (FAQ rich results were retired: see the "Retired or restricted rich results" table in `structured-data.md` and `myths-deprecated.md`.)
- Blocking Google-Extended to leave AI Overviews: it does not work (see [Controls](#controls-what-blocks-what) and `myths-deprecated.md`).
- Aggregated "AI visibility score" tools presented as rankings; "share of model" on a handful of prompts. [SEJ 2026-06/09]
- Frameworks coined by authors ("Machine-First Architecture", "Verified Source Pack", "Latent Choice Signals", "Decision Distance"…): concepts, not standards.
- Bought Reddit posts, reviews or mentions, self-promotional "best of" listicles, hidden prompts: manipulation (spam for Google, abuse for Bing).
- Vendor percentages without a control group ("+13% with schema", "2.8x conversions", "+239% citations").
