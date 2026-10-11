---
name: seo-entity-local
description: Builds one clear, consistent identity of a person or business for Google and AI assistants, and takes care of local presence - one definition of name, role and services, About page, Person/ProfilePage/Organization/LocalBusiness structured data with @id and sameAs, consistent profiles (LinkedIn, GitHub, social) and name/address/phone, Google Business Profile, Bing Places, Apple Business Connect, industry directories, reviews. Delivers ready-to-paste texts and an off-site checklist. For personal brands, portfolios, professionals and local businesses on any stack. Use it to be found by name, appear on Google Maps, set up or fix a Business Profile, collect reviews or align online profiles.
when_to_use: |
  English: found when searching my name; appear on Google Maps; set up Google Business Profile; fix my About page; align LinkedIn and site; get more reviews; Person schema; local SEO
  Italian: farmi trovare cercando il mio nome; comparire su Google Maps; aprire la scheda Google; pagina chi sono; allineare i profili; raccogliere recensioni; SEO locale
  Spanish: aparecer al buscar mi nombre; salir en Google Maps; crear el Perfil de Empresa; página sobre mí; conseguir reseñas; SEO local
  German: bei Suche nach meinem Namen gefunden werden; in Google Maps erscheinen; Unternehmensprofil einrichten; Über-mich-Seite; Bewertungen sammeln; lokales SEO
  French: être trouvé en cherchant mon nom; apparaître sur Google Maps; fiche Google Business Profile; page à propos; obtenir des avis; SEO local
argument-hint: "[site URL or project path] [name of the person or business]"
---

# Identity and local presence

> **Working language.** Answer in the language of the user's message. Files written into the project (`SEO.md`, `seo-reports/*`) use the report language recorded in `SEO.md › 1. Site › Working language` (if `SEO.md` is missing, use the user's language and record it when creating `SEO.md`). Page copy (titles, descriptions, H1, body text, alt text) is always written in the site language(s) from `SEO.md › 1. Site › Languages and markets`. Check IDs, severities, JSON keys and script flags stay in English; report headings are translated.

For a small site, what Google and AI assistants know about the person or business matters as much as the site itself. They piece it together from the site, the structured data, external profiles and listings, reviews and mentions. If these sources say different things (role, services, city, "online only" versus "also in person"), the result is confusion. This skill creates **one definition** and carries it everywhere.

## Knowledge base
Files live in `${CLAUDE_PLUGIN_ROOT}/knowledge/` (if the variable is not expanded: the `knowledge/` folder two levels above this skill's folder). Read by tier, as defined in `conventions.md › Reading tiers`: for Tier 1 and 2, Grep the heading in the named file and Read only that section with offset/limit, up to the next heading of the same level. Never load a whole topic file.

| Tier | What to read | When |
|---|---|---|
| 0 | `conventions.md`, `archetypes.md` (does the local part apply?) | Always, at the start |
| Lookup | `INDEX.md`: generated list of every check, one row per check (`ID`, `Severity`, `Check`, `Where` = the owning `file.md#audit-checks`, `Alias of`); Grep it for EN-, LO-, SD- IDs or a keyword, never read it in full | To look up a check ID; never edit it |
| 0 | The detected `adapters/<stack>.md` (detection table in `adapters/README.md`) | Where JSON-LD and the About page live in the code |
| 1 | `entity-personal-brand.md › ## Audit checks`, `› ## Build rules`, `› ## Off-site checklist` | Always |
| 1 | `local-seo.md › ## Audit checks`, `› ## Build rules`, `› ## Off-site checklist` (Business Profile rows tagged `[GBP]`) | Physical location or service area |
| 1 | `structured-data.md › ## Build rules` (minimum JSON-LD per archetype, `@id` conventions) | Step 3 |
| 2 | `structured-data.md › ### LocalBusiness (and subtypes)` (Northwind Physio example), `› ### Person / ProfilePage` (Ada Novak example), `› ### Review / AggregateRating` | Writing the JSON-LD |
| 2 | `entity-personal-brand.md › ### Regulated professions and legal notices` | Regulated professions; VAT, register or licence numbers |
| 2 | `bing-basics.md › ### Bing Places`; `local-seo.md › ### 1. Business Profile and local listings` | Bing Places and Apple Business Connect |
| 3 | `myths-deprecated.md` in full | Before recommending a tactic you are not sure is current |

If a rule is missing, fetch the Google URL in the Source column with WebFetch; there is no local copy of Google's pages.

Business Profile rules come from Google Business Profile Help, not from Search documentation: `[GBP](url)` rows were checked against that Help on the date in the `local-seo.md` legend; a `[GBP]` tag without a link was not found there and is marked *(re-verify)*: check it on the official Business Profile Help before presenting it as certain.

Read the project's `SEO.md` (section 3 Entity, section 8 Decisions) and the project documentation: they often contain choices to respect (e.g. what not to publish). A file starting with `# Profilo SEO` is v1: read it as is (v1 sections 8b/8c/9 = v2 sections 9/10/11) and suggest `seo-discovery` to migrate it.

## Scripts
```bash
# Site as served online (not just the code): contacts, footer, About text, JSON-LD
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" https://northwind-physio.example --sitemap 20 --full-text --lang en --json identity-fetch.json

# Selected public pages only (About, contact, a public CV), no site-wide checks
python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" https://adanovak.example/about https://adanovak.example/contact --no-site --no-ua --full-text --terms "Ada Novak;developer"
```
On Windows use `py -3` (or `python`) if `python3` is not available. The scripts need Python 3.9+ and only the standard library.

Fields to compare with the definition: `visible_text` (complete with `--full-text`), `jsonld` and `jsonld_types`, `other_links` (`mailto:`/`tel:` counts), `external_links` (links to the profiles), `documents` (public PDFs such as a CV), `title`, `h1`.

## Procedure

### 1. One definition
Write with the user (or propose, deriving it from the site) the **identity card**:
- exact name to use everywhere and the accepted variants;
- role / profession in words the audience understands;
- short introduction (about 150 characters) and long bio (about 600-800 characters), consistently in first or third person, in the site language(s);
- main services or skills (3-6), in the audience's words;
- mode (in person where, online, both), area served, address if public;
- public contacts (only those the user wants to publish);
- verifiable credentials (issuing body, year): no vague or invented titles; for regulated professions, the register and number required by local law (`entity-personal-brand.md › ### Regulated professions and legal notices`).

Save it in `SEO.md › 3. Entity` and use it as the source for everything else.

### 2. Check that the sources agree
Check yourself what is public and note every difference from the definition:
- **site**: home, About, contact, footer, structured data, on the HTML **served online** and not only in the code (`seo_fetch.py` with `--full-text`, see Scripts): CDNs and plugins can alter contacts and text (e.g. obfuscated emails that become unreadable);
- **public profiles**: GitHub (public API `https://api.github.com/users/<username>`), public pages you can reach, other sites of the same owner that should link here;
- **linked public documents** (CV, brochure): exposed personal data, consistent role and dates;
- **what you cannot see** (LinkedIn behind login, Business Profile, real Google results): give the user precise instructions to check it and paste back the fields.

### 3. On the site
- **Entity home**: an About page (or the home page, if the site has a single page) with a real photo, bio, credentials, mode and area, links to the profiles. It is the page that `sameAs`, `author` and the external profiles point to.
- **Structured data** as a graph with stable `@id`s, following `structured-data.md › ## Build rules` and its examples (Northwind Physio for `LocalBusiness`, Ada Novak for `ProfilePage` + `Person`): `WebSite` on the home page; `Person` (personal brand) inside `ProfilePage` on the profile page, or `Organization` / the most specific `LocalBusiness` subtype for a business; `sameAs` only to official profiles (SD-27); no property with data not visible on the page; no `aggregateRating` stars on reviews collected or shown by the business itself. Where the stack has an SEO plugin or CMS module that already emits markup, configure it instead of adding a second block (the adapter says how).
- **NAP and mode** in HTML text, identical everywhere on the site (footer, contact, structured data).
- **Legal notices** required by the country or profession (VAT number, register, *Impressum*, licence number) visible and consistent with `Organization.vatID` / `identifier` when used.

### 4. Off the site: ready texts and checklist
Prepare texts already fitted to each platform's fields, starting from the one definition:
- **LinkedIn**: headline, About section, link to the site;
- **GitHub** (technical personal brand): bio, website, optional profile README;
- **Google Business Profile** (only with a location or a service area where customers are met in person; check eligibility in `local-seo.md › ## Off-site checklist`): real name with no added keywords, the most specific primary category, service area or address, services, hours, description, links to the site and to booking, real photos;
- **Bing Places and Apple Business Connect** with the same data (`bing-basics.md › ### Bing Places`; both are separate, free listings to keep consistent with the Business Profile, LO-02);
- **industry directories and registers** (professional associations, chambers, local bodies): they count for credibility and for people, not as "SEO links".

Reviews: ask real customers, one person at a time, without incentives and without filtering for happy ones; reply to all of them. Never self-written or bought reviews. Follow the Reviews block of `local-seo.md › ## Off-site checklist`.

### 5. Report
Write `seo-reports/YYYY-MM-DD-identity.md` in the project root (working language):
1. **In short** (plain language): how consistent the identity is today and what to do first;
2. **One definition** (the card from step 1);
3. **Inconsistencies found**, source by source, with the fix;
4. **Ready texts** for each platform (in the site language);
5. **Ready code** for the site (JSON-LD graph, About page copy);
6. **Off-site checklist**, in order, with who does it and the estimated time;
7. **To verify** (private access) and **what to monitor**: a search for the name in a private window, the fixed AI questions of `SEO.md › 9. Monitoring` (e.g. "What is Northwind Physio in Oslo?", "Who is Ada Novak?") every 3 months, brand queries in Search Console.

Then:
- update `SEO.md › 3. Entity` (and `› 9. Monitoring` if the brand regex or the fixed questions changed);
- **Change log step.** Before finishing, append one row to `SEO.md › 10. Change log` (date · change · pages/area · skill) for every file you created or modified in the project (e.g. `YYYY-MM-DD | Person + ProfilePage JSON-LD, About page bio | /about | seo-entity-local`, and one row for the report).

## Output format
The report above, with headings translated into the working language and the order kept. Ready texts and code are delivered inside it and, for code, as changes in the repository where the adapter says the About page and JSON-LD live.

## Things to keep in mind
- The name must be the real one: adding keywords to the Business Profile name breaks its rules.
- Cloned "service + city" pages created to appear in more areas are doorways: a location page only where there is a real presence and different content.
- An employee does not need a Business Profile: the local part comes down to the city in the text and in the structured data. An online-only business is not eligible for one.
- Respect the user's privacy choices: point out the risks (e.g. personal data in a public PDF), the user decides.
- Never invent credentials, reviews or affiliations; Google's spam policies and the Maps content policy forbid them.
