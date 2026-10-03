# Sintesi di periodo SEJ (ott 2025 - ott 2026), estratte dai 16 file S01-S16


=============== \S01 ===============
# Sintesi del periodo (3 ott – 11 nov 2025)

## (a) Tendenze e novità
- Dichiarazioni ufficiali Google (Robby Stein, Liz Reid, Pichai, Splitt, Mueller): l'AI di Google fa "query fan-out" usando Google Search come strumento e i suoi segnali di qualità/spam; non esiste un "GEO" separato; contano intento soddisfatto, originalità, fonti citate, prospettiva ed esperienza di prima mano; il contenuto "ripetitivo/a basso valore" è trattato come spam, quello generato da AI non lo è di per sé. Google ha aggiustato il ranking verso video brevi, forum e UGC.
- Novità tecniche ufficiali: Lighthouse 13 (audit "insight", punteggi invariati, rimossi font-size ecc.); NotebookLM come user-triggered fetcher che ignora robots.txt; Bing data-nosnippet; AI Mode dentro il tipo "Web" di Search Console; Chrome 154 (ott 2026) avvisa sui siti HTTP; deprecazione Practice Problem (gen 2026); S2R per la ricerca vocale; Bing Places rinnovato; Splitt: gli audit tecnici non devono affidarsi ai punteggi dei tool.
- Studi sul comportamento in AI Mode (Growth Memo/Indig, Semrush, iPullRank, Propellic): zero clic esterni in ~78-94% delle sessioni, clic frequenti solo nello shopping, link inline > icone; traffico LLM referral in calo da luglio (router ChatGPT-5) e circa 1% dell'organico. Narrativa dominante: "visibilità e menzioni, non traffico".
- Forte filone "menzioni di brand / digital PR / off-page" (Ahrefs, Stein, Montti, Oberstein, Indig).

## (b) Tattiche pratiche ricorrenti, con evidenza
- Fondamentali tecnici e di indicizzazione (crawl, canonical coerenti e case-sensitive, noindex accidentali, HTTPS, mobile/CWV): evidenza forte (documentazione Google e dichiarazioni di Mueller/Splitt). 404 dopo rimozione di contenuti sono normali.
- ★ Contenuto non nascosto e leggibile senza JS complessi: Shelby (alcuni LLM catturano solo il primo render, ignorano toggle/tab) e Riddall (alcuni LLM non eseguono JS: HTML grezzo o SSR). Evidenza: opinioni di esperti, plausibile ma non documentata da Google.
- Contenuto originale con esperienza/prospettiva propria, risposte dirette, fatti misurabili, HTML semantico, liste/tabelle per dati tabellari, titoli/H1 coerenti con il contenuto: supportato da Google (Reid, Stein, rater guidelines) e dalla guida Bing; passage ranking esiste dal 2020.
- ★ Locale: GBP completo (categoria, orari, servizi, link appuntamento, foto, post), service area se senza sede, recensioni gestite e citano il servizio, NAP coerente su elenchi, Bing Places gratuito (import da GBP), link da realtà locali; scheda GBP molto cliccata in AI Mode (Growth Memo: 1 solo task locale, campione debole; Propellic travel).
- ★ Misurazione: GA4 con raggruppamento regex di referrer AI, tracciare utenti "direct" per le pagine più citate, sondaggio "come ci hai conosciuto", baseline manuale di citazioni su ChatGPT/Perplexity/Copilot/AI Mode in foglio di calcolo, audit di sentiment; Search Console per query per impression. Evidenza: guide metodologiche, nessun dato Google ufficiale sulle citazioni.
- Menzioni di terzi (Reddit, YouTube, recensioni, elenchi di settore, newsletter di associazioni, PR) per la visibilità AI: correlazione 0,67 Ahrefs, conferma qualitativa di Stein ("l'AI cerca come una persona"). Causalità non dimostrata.
- Refresh vs nuove pagine: aggiornare se obsoleto, creare nuova pagina se tema distinto; test con gruppo di controllo.

## (c) Affermazioni discutibili / hype
- ⚠ "Wordlim" di GPT-5 e schema che "allarga la quota" (WordLift, 97 URL, conflitto di interesse, non significativo).
- ⚠ Chunking a 150-300 parole, schema FAQ/HowTo/TechArticle "per assistenti", PDF canonici, "Machine-Validated Authority", "retrieval batte ranking" (Forrester): ipotesi senza evidenza; Google ha ridotto FAQ/HowTo.
- ⚠ "33% delle ricerche organiche da agenti AI" (BrightEdge, interno), previsione 10-15% di adozione di browser agentici, "ChatGPT 1 mld utenti 2026" (proiezioni).
- ⚠ Dichiarazioni vendor Search Atlas (aggregatori di citazioni venduti agli LLM, press release da 10-20 $ indicizzate in ChatGPT, auto-post social "per gli LLM").
- ⚠ Pipeline Discover e criteri di riscrittura titoli dedotti dai nomi di attributi del "Google leak"; "12 parole/600 pixel" per i title non è un limite Google; budget percentuali di Indig e "refresh ogni 90 giorni" illustrativi.
- ⚠ Densità keyword: smentita (Montti, Google "how search works"); nessuna densità target.
- llms.txt non compare in questo gruppo; nessun articolo ne raccomanda l'uso.
- Voci contrapposte: Barry Adams/Clarkson-Bennett: ottimizzazione LLM = SEO (99,9%); Shelby/Forrester: va fatto di più per l'AI; Oberstein: non affrettare cambi.

## (d) Implicazioni per la skill SEO
- Audit: seguire Splitt (contesto prima dei punteggi, prioritizzare per impatto/sforzo, capire la tecnologia, ID Lighthouse 13 nuovi); controllare canonical/case/redirect, HTTPS, noindex/robots accidentali, immagini con alt, un H1 coerente con title, Search Console (copertura, azioni manuali); per SPA Angular: verificare SSR/prerender e che il testo chiave sia nell'HTML iniziale e non in tab/accordion/JS lazy (rilevante per Google solo se il rendering fallisce, ma più rilevante per i crawler AI).
- Contenuti: esperienza di prima mano, casi, dati propri, risposte dirette; una pagina per servizio/intento distinto; non scrivere pagine Q&A fittizie; niente keyword stuffing; usare query reali (Search Console per impression, domande dei clienti) e il fan-out come lista di domande da coprire (metodo reverse-question euristico).
- Locale: GBP + Bing Places + NAP coerente + recensioni + link locali + pagina servizio/città con prenotazione chiara; schema LocalBusiness/Service coerente con il visibile (valore principale: chiarezza, non rich result garantito); GBP card molto presente nelle risposte AI locali.
- Personal brand: portfolio con progetti documentati, pagina "chi sono" con entità chiare e profili collegati; strategia di menzioni (articoli ospiti, talk, newsletter di settore, GitHub/dev.to, YouTube); identità di brand coerente; monitorare sentiment e cosa dicono gli LLM del nome.
- Visibilità su ChatGPT/Perplexity/AI Overviews: trattarla come misurazione di visibilità, non di traffico; baseline manuale mensile, regex GA4, 'direct' sospetto; nessuna promessa di risultati; non vendere "ottimizzazione LLM" come disciplina separata; evitare tattiche spam; ricordare che robots.txt non controlla i fetcher avviati da utenti.
- Reporting onesto: etichettare ciò che è ufficiale Google vs correlazione vs opinione.


=============== \S02 ===============
# Sintesi del periodo (12 nov – 9 dic 2025)

## (a) Tendenze e novità
- Google: Gemini 3 in AI Mode al lancio; AI Mode con shopping agentico e chiamate ai negozi locali (solo USA); test mobile AI Overviews → AI Mode; Search Console con annotazioni personalizzate, filtro "branded queries" e configurazione report via AI (sperimentale); recensioni Maps con nickname; nuova doc su ShippingService (solo e-commerce) e promemoria "un solo target per recensione/aggregateRating".
- Mueller (fonte Google): TLD keyword senza vantaggio SEO; video hero in background non incide se il contenuto carica prima; 5xx brevi rallentano il crawl ma si recupera; siti in "bad state" per contenuti AI di basso valore non si risolvono riscrivendo a mano. Pichai: la ricerca resta base di "grounding" per l'AI.
- Outage Cloudflare (18 nov e 5 dic) e blocco AI crawler di default su Cloudflare: la catena infrastrutturale incide su crawl e visibilità AI.
- Dati: Ahrefs (traffico da AI <1% ma conversioni sproporzionate), SE Ranking (correlazioni di citazioni ChatGPT con domini referenti), report OpenAI per partner (CTR sotto 1%), SALT (LCP/CLS e citazioni in AI Mode), AWR Q3 (CTR in calo in vetta per query locali/commerciali), BrightEdge (AIO volatili: 18% di sovrapposizione anno su anno), Seer (CTR in calo con AIO). Metodi spesso parziali o proprietari.

## (b) Tattiche ricorrenti con evidenza
- Basi tecniche e accessibilità (SSR/HTML iniziale, LCP/INP, uptime, HTTPS): doc Google + Mueller; SALT e hosting a supporto (correlazioni). ★ SPA Angular: non nascondere il contenuto sotto JS; per i bot AI l'HTML è ancora più importante (opinione).
- Controllo dei bot AI (robots.txt per GPTBot/OAI-SearchBot/ClaudeBot/PerplexityBot/Google-Extended; verifica IP; controllo CDN): lista SEJ da log reali; ricorre in 4 articoli.
- Misurazione: GSC (brand vs non-brand, annotazioni, export per superare i 16 mesi), test manuali periodici di prompt su ChatGPT/Perplexity/Google e registro delle risposte (3 articoli concordi: Forrester, Terrasi, Southern), Bing Webmaster Tools + Clarity per traffico AI.
- E-E-A-T pratico: autore e credenziali visibili, coerenza di nome/bio/NAP tra sito, LinkedIn, YouTube e schede, recensioni, contenuti esperienziali e dati originali (Forrester, Stox, Clarkson-Bennett, SEJ Trends). Evidenza: opinioni e correlazioni, coerenti con la doc Google su contenuti utili.
- Menzioni/PR su fonti terze rilevanti (associazioni, trade, media locali, community) invece di link massivi; no link a pagamento senza nofollow/sponsored (doc Google).
- Diagnosi calo traffico (tracking, brand, stagionalità, segmenti) e checklist su migrazioni (redirect 1:1, SEO coinvolta prima).

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt: nessun sistema AI lo usa (Mueller); Forrester lo sconsiglia come tattica di traffico.
- ⚠ Schema/knowledge graph/Wikidata "per la visibilità AI" (van Berkel, Terrasi): conflitto di interessi o ipotesi; la stessa Hunt/Forrester ammettono prove limitate. Google dice solo che i dati strutturati sono utili per i rich result.
- ⚠ Numeri "magici" sul contenuto: chunk 100-300 parole, risposta nelle prime 2-3 frasi, >2.900 parole = più citazioni (SE Ranking, correlazione), 19+ dati: non da doc Google; non usarli come regole.
- ⚠ "Hreflang ignorato dagli LLM", "universal verifiers", "share of model", "AI poisoning" con 250 documenti (studio reale ma applicato in modo ipotetico ai brand).
- ⚠ Navboost/Glue/Q*/DocID, "130 giorni senza crawl", "indicizzazione a livelli": derivati da fughe/DOJ/blog.
- ⚠ Post sponsorizzati come "validazione" per le AI; listicle auto-promozionali ("funzionano oggi", non a prova di futuro secondo Stox).
- Previsioni 2026 di Indig (Perplexity venduta, Nvidia, ecc.): speculative. Molte statistiche citate di seconda mano (Seer, Bain, Rise at Seven) non verificate.

## (d) Implicazioni per la skill SEO
- Audit: includere controllo robots.txt/CDN/WAF per bot AI (distinguere training vs ricerca/utente), HTML iniziale senza JS (Angular: SSR/prerender), 5xx e uptime, LCP/INP/CLS, un solo target per review/aggregateRating, redirect in caso di migrazione, sitemap XML automatica (siti piccoli: facoltativa ma economica), esportazione periodica dei dati GSC. Procedura di diagnosi del calo traffico (tracking, brand/non-brand, stagionalità, segmenti).
- Contenuti: risposta chiara in apertura, un tema per sezione, fatti verificabili, aggiornamento, nessun contenuto di massa generato da AI; esperienza diretta e dati originali; non adottare lunghezze o densità keyword come regole. Video/YouTube come canale complementare.
- Locale (orientatrice): NAP coerente, area servita esplicita nel testo, profilo Google Business curato, recensioni (nickname non cambia le procedure di richiesta), menzioni da associazioni/media locali, attenzione al calo CTR delle query "location" (moduli/mappa). Schema LocalBusiness/ProfessionalService secondo doc Google, ma senza promettere effetti sull'AI.
- Personal brand (sviluppatore): pagina persona con bio/credenziali coerenti con LinkedIn/GitHub/altri profili (sameAs), contenuti tecnici originali, presenza in community, monitoraggio di cosa dicono le AI sul proprio nome (rischio di errori reputazionali), metrica brand vs non-brand in GSC (nuovo filtro).
- Visibilità su ChatGPT/Perplexity/AI Overviews: trattarla come estensione della SEO; aspettarsi poco traffico diretto (<1% in più fonti) ma citazioni/menzioni; testare i prompt manualmente e a intervalli, registrare le risposte (volatilità alta); non usare llms.txt né markup "per AI" come promessa; presentare ogni dato di vendor come correlazione.


=============== \S03 ===============
# Sintesi del periodo

## (a) Tendenze e novità del periodo (9 dic 2025 – 9 gen 2026)
- Core update di dicembre 2025 (11–29 dic, 18 giorni): terzo dell'anno dopo marzo e giugno. Google ha aggiornato la documentazione: esistono anche core update minori continui e non annunciati, quindi i miglioramenti possono essere premiati senza attendere un update nominato (fatto Google). Prime analisi (Solís, Gabe, SISTRIX, NewzDash): a guadagnare sono siti/brand specializzati, a perdere i generalisti su query "best of" e mid-funnel; forte volatilità per news e Discover.
- Documentazione Google JavaScript SEO aggiornata due volte: (1) noindex nell'HTML iniziale può impedire il rendering, quindi non va rimosso via JS; (2) canonical: valutato due volte (HTML grezzo e renderizzato), meglio impostarlo nell'HTML iniziale uguale a quello finale, o ometterlo se lo cambia JS; un solo canonical dopo il rendering. Mueller: "Page indexed without content" = blocco server/CDN, non JS.
- Posizione ufficiale Google su AI (podcast Search Off the Record con Mueller e Sullivan; intervista a Robby Stein; Nick Fox): niente di nuovo da fare per AI Mode/Overviews; contano contenuti originali, utili, veloci, con fonti citate; evitare di ottimizzare per LLM o per "GEO"; i contenuti "commodity" non sono un vantaggio. AI Mode: 75M utenti giornalieri, query 2–3 volte più lunghe, Gemini 3 Flash predefinito.
- Dati sui crawler (Cloudflare Year in Review 2025): Googlebot raggiunge la quota più alta di pagine; i bot AI sono ~4% delle richieste HTML; il crawling "user-action" è cresciuto >15x; rapporti crawl/referral molto sbilanciati (Anthropic, OpenAI) rispetto a Google; Perplexity il più "equilibrato".
- Studio Ahrefs (730.000 coppie di query): AI Mode e AI Overviews concordano nel 86% ma citano gli stessi URL solo nel 13,7%.
- Safari 26.2 espone LCP e Event Timing (INP) per il RUM, ma CrUX/PSI/GSC restano solo Chrome. Core Web Vitals per CMS (HTTP Archive, nov 2025): Duda 85%, Wix 75%, Squarespace 70%, Drupal 63%, Joomla 57%, WordPress 46% di siti conformi.
- Hype di fine anno: previsioni 2026 (Forrester, Indig, 20 esperti SEJ), GEO/AEO come disciplina, "agentic SEO", llms.txt (plugin WordPress lo aggiungono per richiesta dei clienti; Google l'aveva per errore e l'ha rimosso).
- Search Console: test di dati sui profili social associati al sito (Insights, solo piccolo gruppo).

## (b) Tattiche pratiche ricorrenti con evidenza a supporto
1. HTML renderizzato lato server per i contenuti essenziali (testo, titoli, link, contatti): evidenza = doc Google JS (noindex, canonical) + test Vercel/Gabe: i crawler AI principali non eseguono JS + Mueller (blocchi CDN). Verifica con "view source", URL Inspection, DOM al primo caricamento.
2. Canonical coerente (HTML grezzo = renderizzato), nessun noindex iniziale, un solo canonical (doc Google).
3. Contenuto originale e con esperienza reale (Sullivan, Stein: originalità e citazione fonti); evitare contenuti "commodity" e scalati (spam policy Google).
4. Specializzazione tematica (analisi Solís sul core update di dicembre: indicativa, non una dichiarazione Google).
5. Coerenza delle informazioni su tutto il web (NAP, servizi, bio) e menzioni/recensioni di terzi (opinione ricorrente: Forrester, Shelby, Riddall, Lily Ray; Sullivan: essere riconosciuti come brand). Evidenza quantitativa solo da studi di terzi (BrightEdge, Indig).
6. SEO locale: GBP completo, categoria primaria corretta, orari verificati, recensioni gestite, schema LocalBusiness coerente, CTA e KPI di contatto (articolo Riddall: opinione, ma coerente con la documentazione locale di Google).
7. Misurare conversioni reali con eventi GA4 (clic contatto/prenotazione) e annotare gli update; manutenzione trimestrale (audit tecnico, on-page, link, listing locali).
8. Velocità e CWV: raccogliere dati reali (RUM) anche per Safari; CWV peso ridotto ma utili a UX.
9. Potatura/aggiornamento dei contenuti obsoleti: 301 se sostituiti, 404 se inutili (Montti; opinione).

## (c) Affermazioni discutibili o hype
- ⚠ llms.txt, MCP server "AI-ready", "markup per AI": nessuna evidenza di uso da parte di Google o dei principali LLM; Mueller contrario; Google stesso lo ha rimosso.
- ⚠ GEO/AEO come disciplina separata: Sullivan e Stein dicono di no; chi la vende ha incentivi (Forrester sostiene il contrario con tesi basata su dati di terzi su calo di CTR, non su prove di tattiche GEO).
- ⚠ Schema/FAQPage "per l'AI", "Review schema per sintesi AI", `geo` per AI Mode, `lastReviewed` per freschezza: nessuna conferma Google; lo schema resta utile solo secondo le linee guida sui rich result.
- ⚠ Consigli come "aggiornare ogni 3 mesi", "anno nell'URL", "paragrafi brevi per estrazione", keyword nei nomi file/alt per l'AI (Indig, Riddall): correlazioni o intuizioni non convalidate.
- ⚠ Teorie su link/trust (seed set, reduced link graph, sponsored articles citati dall'AI) e sulla leak per spam: inferenze dell'autore, non dichiarazioni Google. Le tattiche spam (liste "best of" auto-referenziali, PBN, domini scaduti) sono da evitare per rischio di azione manuale/SpamBrain.
- ⚠ "Latent Choice Signals", "Machine Comfort Bias", "agent-to-agent commerce", "i formati sono segnali di ranking per macchine" (Forrester): concetti coniati senza evidenza.
- ⚠ Keyword density: nessuna soglia ufficiale; i punteggi dei tool sono artefatti (conferma indiretta in "Ask An SEO").
- ⚠ Stime di traffico: ChatGPT ~0,2–0,5% della ricerca (Montti) vs "fino al 4% del referral organico" (Indig): i numeri variano molto; usare cautela e dati propri.
- Studio Ahrefs sulla "misinformazione AI": metodologicamente debole (domande suggestive, brand finto senza segnali); la lezione utile è che contenuti specifici e diretti vengono usati più di pagine evasive.

## (d) Implicazioni per la skill SEO
- Audit tecnico (priorità SPA/Angular): controllare in HTML grezzo (view source, curl con user-agent, URL Inspection) presenza di title, meta description, canonical (unico, coerente), robots meta (nessun noindex iniziale), H1, testo principale, link interni come `<a href>`, JSON-LD, contatti; raccomandare SSR/prerender (Angular SSR/SSG) per le route indicizzabili; errori gestiti con status code lato server, non con noindex via JS; controllare blocchi CDN/WAF contro Googlebot (Page indexed without content); verificare accesso dei crawler AI in robots.txt in modo consapevole (training vs user-action vs ricerca) senza bloccare Googlebot.
- Contenuti: originalità ed esperienza dimostrabile, risposte dirette, fonti citate, nessun contenuto commodity o scalato; pagine/entità chiare per tema (specializzazione); contenuti nascosti in tab/accordion presenti nel DOM; aggiornare/potare con 301/404 motivati; nessun obiettivo di densità keyword.
- Locale (libera professionista): GBP (categoria, servizi, orari, attributi, foto, risposte alle recensioni), coerenza NAP/servizi tra GBP, sito e directory, pagine di servizio con CTA e prova sociale reale, recensioni autentiche, link/menzioni da associazioni e testate locali, evento di conversione per telefonate/prenotazioni; area di servizio esplicita se non c'è sede aperta al pubblico; audit trimestrale dei listing.
- Personal brand (sviluppatore): pagina "chi sono" con identità coerente su sito, LinkedIn, GitHub (profili social collegati, possibile segnale di entità), progetti reali con casi studio e decisioni tecniche (originalità ed esperienza), ricerche per nome come KPI, menzioni da community tecniche pertinenti, nicchia/stack chiari; evitare siti "template" generici. Per i recruiter: testo reale in HTML, contatti e CV facili da trovare.
- Visibilità su ChatGPT/Perplexity/AI Overviews: nessuna "GEO" separata; stessa base SEO (indicizzazione, rendering, contenuto originale, menzioni terze); monitoraggio manuale periodico di query-chiave sui diversi motori (i risultati divergono molto: 62% disaccordo BrightEdge, 13,7% overlap URL Ahrefs); non investire in llms.txt; i bot AI senza JS richiedono HTML renderizzato; misurare il traffico AI come canale piccolo (referral) ma l'influenza di brand va tracciata con ricerche per brand/menzioni.
- Misurazione: GA4 con eventi di conversione (contatto, prenotazione, download CV), annotare gli update di Google, RUM con web-vitals per includere Safari, revisione periodica (mensile/trimestrale).


=============== \S04 ===============
# Sintesi del periodo (9 gen – 5 feb 2026)

## (a) Tendenze e novità del periodo
- Core update di dicembre 2025 (11–29 dic): letture preliminari (Solís, esempi non sistematici) a favore di siti specialistici contro generalisti; a metà gennaio volatilità con crolli di blog SaaS ricchi di listicle autopromozionali e contenuto AI scalato (Lily Ray, osservazione su pochi siti).
- Google/Googler: Sullivan (SOTR) contro il "chunking per LLM"; Mueller su sottodomini gratuiti/TLD economici e noindex "visibile solo a Google"; documentazione crawler aggiornata (15 MB default, 2 MB Googlebot HTML, 64 MB PDF); Illyes: parametri di azione ~25% e faceted nav ~50% dei problemi di crawl 2025; Google "esplora" controlli di opt-out dalle funzioni AI; Gemini 3 predefinito in AI Overviews (>1 miliardo di utenti); AI Mode personale (Gmail/Photos, USA, opt-in); Social Channel Insights in GSC (test).
- Agentic commerce: UCP (Google) e ACP (OpenAI/Stripe): rilevante solo per ecommerce.
- Dati AI/crawler: Hostinger (66 mld richieste, 5 mln siti): bot di training in calo (GPTBot 84%→12%), bot di ricerca/assistente in crescita (OAI-SearchBot fino al 68%); Web Almanac 2025: llms.txt ~2% dei siti, spinto da plugin.
- Misurazione: GSC filtra ~75% delle impression e ~38% dei click a livello query (Indig, 10 siti SaaS); bot impression; AIO e calo click (correlazione 0,6); Pew: con riassunto AI click 8% vs 15%.
- Dibattito SEO/GEO/AEO: Microsoft pubblica la sua guida (ecommerce); Googler e molti SEO: "è SEO"; voci contrarie (Forrester, Search Atlas) vendono GEO come livello aggiuntivo.

## (b) Tattiche pratiche ricorrenti e relativa evidenza
- Fondamentali tecnici (crawlability, HTML renderizzato lato server, canonical SSR, nessun mismatch crawler/utente): evidenza = documentazione Google/Microsoft e osservazioni (Magento, Web Almanac, Clarkson-Bennett: "GPTBot vede solo l'HTML"). ★ SPA: SSR/prerender per i crawler AI; Google renderizza JS ma i bot di terze parti spesso no (affermazione di un autore, coerente con la pratica nota).
- robots.txt per bot AI: consentire i bot di ricerca (OAI-SearchBot, Applebot) e decidere separatamente sul training (GPTBot) in base agli obiettivi; verificare i log (doc OpenAI, Hostinger, Solís). Evidenza: documentazione OpenAI + dati descrittivi, non prova che consentire porti a citazioni.
- Dominio proprio, no hosting gratuito/TLD spam-prone (Mueller, Illyes): evidenza = dichiarazioni Google.
- Entità e disambiguazione: About chiaro, nome coerente, sameAs a profili ufficiali, NAP coerente, Knowledge Panel se esiste (van Berkel, Clarkson-Bennett, Hunt); evidenza = un caso vendor (Brightview, +25% click non-brand, senza controllo) e opinioni; lo schema è coerente con la documentazione Google, i benefici "per AI" non sono dimostrati.
- Struttura leggibile (risposta in apertura, heading, tabelle/liste, FAQ, qualificatori "per chi è / non è"): consigliata da Forrester, Microsoft, Clarkson-Bennett; Sullivan: scrivere per persone, non spezzettare per LLM. Evidenza: convergente come buona pratica; E-GEO è un paper ecommerce.
- Menzioni/citazioni di terzi, PR, premi, associazioni, podcast, eventi (Montti, Indig, Clarkson-Bennett): evidenza = esperienza degli autori e RAG che attinge a fonti terze; nessuno studio controllato qui.
- Misurazione: non basarsi sulle sole sessioni; query brand, contatti/lead, citazioni AI manuali; confrontare totale aggregato GSC con somma query (Indig); test controllati su 10–20 pagine (Forrester).
- Audit link interni: cluster tematici, >=~75% link dallo stesso tema, anchor descrittive (Pollitt; soglia euristica).

## (c) Affermazioni discutibili o hype
- ⚠ llms.txt: nessun motore AI lo usa ufficialmente; Google lo ha escluso; ~2% di adozione guidata da plugin. Non consigliarlo come tattica SEO (al massimo opzionale, a costo zero, senza aspettative).
- ⚠ "Chunk optimization", contenuto per LLM, "semantic density", markdown per agenti, tag ai-disclosure: Google dice di no; zero evidenza; unico supporto da Forrester/Microsoft (interessi di parte).
- ⚠ Causalità assoluta dello schema (Brightview "complete causation"); vendor di schema/GEO (Schema App, Search Atlas, Rio SEO) con conflitto di interessi.
- ⚠ "SEO non esisterà nell'agentic" (Shopify), "agenti = 20% vendite natalizie" (Indig, definizione lasca), "entrare nei dati di training" (impossibile retroattivamente, quasi grey hat per lo stesso autore).
- ⚠ Soddisfazione utente / dati Chrome / scroll e durata sessione come fattore principale (Haynes): inferenza da documenti legali, non conferma Google.
- ⚠ Listicle autopromozionali: funzionano nel breve in AI ma associati a cali; non farli.
- Studi con campione ristretto: Lily Ray (~9 siti SaaS), Indig (10 siti B2B SaaS), Hostinger (siti di un solo host); non estendere a portfolio/locale senza cautela.

## (d) Implicazioni per la skill SEO
- Audit: includere (1) HTML ricevuto senza JS (title, canonical, contenuti principali, link interni, structured data nell'HTML iniziale); (2) peso HTML sotto 2 MB e risorse separate; (3) robots.txt per bot AI di ricerca vs training con intento dichiarato; (4) noindex/header serviti a Google vs utenti (CDN/cache; Rich Results Test; user agent Googlebot); (5) niente parametri/URL infiniti (booking, calendari); (6) coerenza date/dati strutturati; (7) schema onesto: niente AggregateRating su auto-recensioni, WebSite solo sul dominio principale; (8) re-audit trimestrale.
- Contenuti: scrivere per persone con risposta in apertura e heading chiari; pagine servizio con "per chi è/non è", processo, modalità, fascia di prezzo, prove (casi, credenziali); no listicle autopromozionali, no refresh finti, no contenuto AI scalato senza controllo umano; segnare come ⚠ ogni consiglio "per l'AI" non supportato da Google.
- Locale (orientatrice): Google Business Profile e local pack dominano le query "near me" (AIO sulle query locali sceso da ~90% a ~10% nel dato BrightEdge, rilevato su finanza); pagine con città/area servita, NAP coerente, LocalBusiness/ProfessionalService con areaServed, recensioni reali; associazioni e media locali come menzioni; credenziali ed esperienza evidenti (YMYL-adjacent).
- Personal brand (sviluppatore): dominio proprio; pagina About/Person con sameAs (GitHub, LinkedIn), nome coerente ovunque; posizionamento di nicchia netto (core update favorevole a specialisti); contributi esterni (talk, articoli, open source) come segnali di terzi; misurare le ricerche del proprio nome; SSR/prerender per Angular.
- Visibilità su ChatGPT/Perplexity/AI Overviews: dichiarare che non esiste un playbook GEO separato validato; ChatGPT e Perplexity dipendono da indici web classici + bot propri (OAI-SearchBot): essere indicizzabili, consentire i bot di ricerca, avere menzioni di terzi e identità chiara; test manuale periodico (chiedere agli assistenti "chi è X / migliori orientatori a Y") invece di ottimizzazioni speculative; risposte AI personalizzate e instabili (BrightEdge 62% di disaccordo, Dwyer): monitorare tendenze, non singole risposte.


=============== \S05 ===============
# Sintesi del periodo (5 feb – 6 mar 2026)

## (a) Tendenze e novità
- Google: primo "Discover core update" separato (5-27 feb, ~22 giorni), linee guida Discover riscritte (anti-clickbait, "great page experience"); la lettura di Search Console va fatta per superficie.
- Documentazione Google aggiornata in modo concreto: limite 2 MB di HTML per file (64 MB PDF); metadati solo nell'`<head>`; resource hints inutili per Googlebot; HTML valido non è un segnale; scelta thumbnail con `primaryImageOfPage`/`image` su mainEntity/`og:image`; rimossa la raccomandazione di testare con JS disattivato (4 mar 2026).
- Misurazione AI: Bing Webmaster Tools AI Performance (citazioni + grounding queries); Google non ha un equivalente. Bing riscrive le linee guida includendo Copilot e prompt injection come abuso.
- Divario ranking/citazioni AIO: sovrapposizione top 10 scesa da 76% a 38% (Ahrefs) o ~17% (BrightEdge); AIO su ~48% delle query; ChatGPT sembra dipendere da Google (Lily Ray, 11 siti), Perplexity no.
- Dichiarazioni di Googler: Mueller "buona SEO è buona GEO", no a Markdown per bot, sito non sempre necessario (Illyes/Splitt, opinione personale), Liz Reid: nelle AIO si clicca su contenuti "più ricchi e profondi".
- Ondata di concetti degli autori (Forrester, Indig, Taylor): "SSIT", "Verified Source Pack", "infinite tail", "agentic commerce": non sono standard.

## (b) Tattiche pratiche ricorrenti e evidenza
- Risposta in alto, definizioni dirette, H2 come domande, entità concrete: studio Indig (1,2 mln risposte ChatGPT / 18.012 citazioni, dati Gauge, solo ChatGPT, correlazionale); ripreso da Clarkson-Bennett e da Indig stesso (strategia). Coerente con "contenuto utile e chiaro" ma non è guida ufficiale Google.
- Contenuto originale/esperienza diretta, non "commodity": casi Marie Haynes (4 siti, causalità non provata), dichiarazione Liz Reid, rater guidelines ("paraphrased" da 3 a 25 menzioni); LinkedIn: autori nominati, credenziali, date visibili (test interni).
- Una pagina = un intento; focus tematico stretto (Simmons, Forrester, Taylor): opinioni coerenti, senza dati.
- Diagnosi tecnica con strumenti: curl/Live Test per l'HTTP fantasma (Mueller), ricerca di citazione esatta per verificare i passaggi indicizzati, URL Inspection per il rendering, Tame The Bots per il cap 2 MB.
- Contenuto JS: non sostituire testo o robots via JS dopo il caricamento; caricare tutto il blocco (Mueller). ★ SPA.
- Coerenza dell'identità di brand e prove di fiducia (contatti, proprietà, recensioni reali, servizio clienti): SSIT, Taylor, LinkedIn, Haynes. Evidenza: aneddotica/opinione.
- Misurare esiti di business e non solo click (articolo KPI del 9 feb, Taylor): opinione.

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt: nessun provider LLM dichiara di usarlo (nemmeno Forrester lo nega); Mueller lo paragona alle meta keywords; SE Ranking (300.000 domini, citato) nessun effetto; presente su ~2% dei siti (Web Almanac), spesso attivato di default dai plugin.
- ⚠ Markdown per i bot: Mueller contrario; Cloudflare Markdown for Agents (content negotiation) senza evidenza di beneficio; Google non ha chiarito il rapporto con il cloaking.
- ⚠ "Schemamap" Yoast e "Verified Source Pack": nessuna conferma che motori o agenti li leggano; endpoint e firme sono eccessivi per piccoli siti.
- ⚠ Studio CORE (manipolare il ranking LLM con recensioni finte o testo di ragionamento): laboratorio via API, non prodotti reali; è pratica di spam. Lily Ray: le tattiche GEO dannose per la SEO si ripercuotono sulle citazioni. Microsoft: 31 aziende con prompt injection nei pulsanti "Summarize with AI".
- ⚠ Cifre non ufficiali: chunk 200-500 caratteri, "liste riducono i token del 20-40%", titoli Discover >13 parole, "p=0.0" nello studio Indig (campione grande ma un solo fornitore e un solo modello).
- "Google Zero" contestato (Barry Adams: -2,5% medio sui top siti, dati selezionati) contro evidenze opposte (WaPo -50% in 3 anni; Chartbeat): evidenza mista, dipende dal settore.
- Previsioni su agenti/abbonamenti e "search becoming infrastructure" senza dati.

## (d) Implicazioni per la skill SEO
- Audit tecnico (agnostico, SPA): verificare homepage HTTP vs HTTPS (curl); robots.txt reale (non fallback 404/HTML); sitemap valida ma senza garanzie; canonical, hreflang, meta robots nel `<head>` del DOM renderizzato; HTML grezzo ben sotto i 2 MB (attenzione a JSON di stato inline); resource hints non sono un fix SEO; rendering con URL Inspection Live Test; Google rende il JS, ma contenuti critici anche in HTML/SSR per crawler AI e per sicurezza; non sostituire testo via JS dopo il load; thumbnail con `og:image`/schema image (>=1.200 px, non loghi).
- Contenuti: risposta in apertura, una pagina per intento, esperienza di prima mano, dati propri, autore/credenziali/date visibili; evitare contenuto "commodity" o AI generico; blocchi autosufficienti e citabili con limiti e fonti. Per mercati non anglofoni, ipotesi da testare: presenza anche in inglese (Peec AI: 43% fan-out ChatGPT in inglese).
- Locale (orientatrice): quasi nessun dato locale in questo periodo; utili: pagine con prova di località e confini di servizio (SSIT), coerenza identità, recensioni reali e servizio clienti (Haynes), approccio prudente YMYL-adiacente (nessuna garanzia, fonti, aggiornamento); AIO su istruzione 83% e sanità 88% delle query (BrightEdge). Illyes/Splitt: profilo curato meglio di un sito fatto male, ma il sito è l'asset di proprietà.
- Personal brand (sviluppatore): registrare presto dominio e sito per nome e progetti (caso NanoClaw), collegare GitHub/LinkedIn al sito, descrizione identica ovunque (entità), casi reali e dati propri, schema Person/Organization coerente; presenze su piattaforme terze (LinkedIn, Reddit, YouTube è il dominio più citato in AIO) come sintesi + rimando al sito.
- Visibilità su ChatGPT/Perplexity/AIO: la SEO classica resta la base (ChatGPT sembra attingere a Google; Perplexity ad altro, ipotesi Brave); AIO cita spesso pagine fuori dalla top 10; misurare con Bing AI Performance, analytics e prompt tracking direzionale; llms.txt/markdown/schemamap solo come opzioni a costo zero, mai priorità; mai manipolazioni (prompt injection, recensioni false).
- Reporting: separare Search/Discover/AI; KPI di esito (contatti, richieste) più che click.


=============== \S06 ===============
# Sintesi del periodo

## (a) Tendenze e novità del periodo (6–30 marzo 2026)
- Ufficiali Google (Search Status Dashboard / documentazione): spam update marzo 2026 (24–25 marzo, meno di 20 ore, nessuna nuova policy); core update marzo 2026 avviato (fino a 2 settimane; attendere almeno una settimana dopo la fine prima di analizzare); core update di febbraio 2026 solo Discover (inglese, USA); test "piccolo e ristretto" di titoli riscritti con AI nei risultati di ricerca; nuovo user agent "Google-Agent"; Search Live esteso a oltre 200 paesi; Ask Maps (Gemini) in Maps solo USA/India; filtro "branded queries" di Search Console aperto a tutti i siti idonei (non per sub-property né siti con poche impression); Personal Intelligence di AI Mode gratuito negli USA; aggiornamento doc dati strutturati forum/Q&A (`digitalSourceType`).
- Dichiarazioni di Googler (podcast e social): Googlebot è solo un client di un'infrastruttura di crawling condivisa con centinaia di crawler/fetcher non documentati; limite di 15 MB di default, 2 MB di fatto per Search (HTML), 64 MB PDF; Mueller: HTTPS = migrazione, 404 in Search Console non sono un problema (410 non cambia il re-crawl), disavow "strumento non religione" anche con `domain:` per interi TLD (non documentato), nome sito alternativo = nome di dominio per correggere nomi legacy.
- Dati sul calo di clic: AI Overviews riducono il CTR in posizione 1 del 58–59% (Ahrefs dic 2025; SISTRIX Germania 27% → 11%, oltre 100 mln keyword); Pew 8% vs 15%; Chartbeat: referral da ricerca ai piccoli editori -60% in due anni; Define Media: evergreen -40%, breaking news +103%. Eccezione ricorrente: query brand con AIO +18% CTR (Amsive) e query transazionali poco colpite.
- Traffico da AI ancora marginale: ~1,08% delle sessioni (Conductor, 13.770 domini), meno dell'1% dei referral degli editori (Chartbeat), ~87% di quel traffico da ChatGPT. ChatGPT ha tolto i metadati dei sub-query (GPT-5.3): gli strumenti che li leggevano si sono rotti.
- Bing Webmaster Tools: AI Performance con mappatura grounding query / pagine citate (campione, gratuito); Search Console non ha un equivalente.

## (b) Tattiche pratiche ricorrenti, con evidenza
- Contenuto con esperienza/dati propri invece di riassunti sostituibili ("golden knowledge"): ripetuto da Walsh, Haynes (Reid: non la stessa cosa di centomila altri), Dias. Evidenza indiretta: studi sul calo dei clic per le query informative; Reid conferma che Google combatte lo slop. Evidenza forte contro la scalabilità di contenuti generici: policy Google sullo scaled content abuse, azioni manuali dal giugno 2025.
- Brand, menzioni e ricerche per nome come segnale e come KPI: Ahrefs (menzioni di brand = correlazione più forte con le risposte AI), Toronto (earned media), Amsive (+18% CTR per query brand), filtro brand di Search Console; esempio Ahrefs (personal brand dei dipendenti). Evidenza correlazionale, non causale.
- Struttura citabile: heading descrittivi, risposta in apertura, sezioni autonome, liste/tabelle, nessuna risposta nascosta in tab/accordion (guida Microsoft/Bing; Indig: ~44% delle citazioni ChatGPT dal primo 30% della pagina, conclusioni quasi mai citate; pagine che rispondono a più intenti vengono citate su più prompt). Evidenza: correlazioni su campioni ChatGPT (98.000 citazioni) e GEO-16 (1.702 citazioni); nessuna conferma Google.
- Tecnica di base: HTML sotto 2 MB, risorse in file separati, canonical, robots.txt coerente, non bloccare per errore i bot AI se si vuole visibilità, separare crawler di ricerca da quelli di training; sitemap pulita; HTTPS/redirect 301 per migrazioni senza rimozioni URL.
- Locale (GBP): categoria primaria, prossimità, nome, orari ("aperto ora" tra i primi 5 fattori), recensioni fresche e risposte, foto recenti autentiche, prenotazione, Q&A. Evidenza: Whitespark 2026, BrightLocal (50 attività), Birdeye; le tattiche di cadenza (post settimanali, risposte entro 48 h) sono consigli dell'autore, non provati.
- Titoli: Google riscrive i title con regole (61–76% nelle analisi citate) e ora testa riscritture AI; title/H1 coerenti e descrittivi riducono lo spazio di riscrittura (deduzione dalle fonti documentate: title element, H1, og:title, anchor).
- Crawl con rendering JavaScript attivo (Screaming Frog, Spider > Rendering) per siti SPA.

## (c) Affermazioni discutibili / hype
- ⚠ "SEO → AEO → GEO → AAIO" e "il più grande cambio mentale della storia SEO" (Manić, Haynes): framing promozionale; l'unica dichiarazione ufficiale Google riportata dice che non servono file, testi o markup speciali per AI Overviews/AI Mode.
- ⚠ Schema (Organization/Person, FAQPage, HowTo) che "addestra gli LLM" (Baker, Manić): aneddoto su un CEO omonimo e linee guida Microsoft; nessuna prova per Google; FAQ/HowTo rich result limitati da Google (verificare nella doc primaria).
- ⚠ llms.txt: solo 2,13% dei siti, in gran parte autogenerato da plugin (Web Almanac); "da osservare"; nessuna evidenza di effetto.
- ⚠ Dashboard di prompt tracking / "share of answer" (Dias): conteggi su prompt campione, non ranking; fragilità dimostrata dal caso GPT-5.3 (Forrester).
- ⚠ "Training cutoff come fattore di ranking" e "cutoff-aware content calendaring" (Forrester): concetto plausibile, senza dati; i cicli di training non sono noti.
- ⚠ TurboQuant nel core update, "meno link/SEO", "i giorni della ricerca tradizionale sono finiti" (Haynes), possibile "Florida 2.0" (Scott): speculazione.
- ⚠ Indig: soglie di lunghezza per le citazioni (10.000 parole) con parole e caratteri mescolati, solo ChatGPT e solo verticali commerciali: non estendibile alla SEO di Google né al locale.
- ⚠ 404 "segnale positivo" (interpretazione di Mueller/autore): il fatto verificabile è che non serve correggerli.
- Reddit/UGC come scorciatoia per farsi citare dall'AI: esistono tool di auto-reply e account comprati, ma è manipolazione (Dias) con rischio reputazionale.
- Sondaggi informali (skills gap) e dati di soli editori news (Chartbeat, Define, DiscoverSnoop) non vanno estrapolati a siti piccoli o locali.

## (d) Implicazioni per la skill SEO
- Audit tecnico: ★ verificare che il contenuto principale sia nell'HTML iniziale o prerenderizzato (SPA Angular: SSR/prerender per meta, canonical, H1, link `<a href>`); peso HTML sotto 2 MB; robots.txt (nessun blocco accidentale di Googlebot né dei bot AI voluti; distinguere search e training); sitemap solo con URL canonici 200; HTTPS/redirect 301 per migrazioni e rebranding; title/H1 coerenti; JSON-LD minimo e valido; non preoccuparsi dei 404 in Search Console. Citare il Google Search Status Dashboard come unica fonte per gli update.
- Contenuti: evitare pagine in serie (es. "orientamento a [città]"); per ogni pagina chiedersi cosa offre che il lettore non trova altrove; esperienza diretta, casi, dati propri; risposta chiave nei primi paragrafi, heading descrittivi, sezioni autonome; ogni pagina con un prossimo passo chiaro (contatto/prenotazione). Prezzi, modalità e limiti dichiarati in chiaro (utile anche per i sistemi AI).
- Locale (orientatrice): GBP completo (categoria primaria corretta, orari, area di servizio/online, servizi, foto reali, Q&A), recensioni con risposta, coerenza di nome/indirizzo/telefono tra sito e profilo, pagine servizio/città uniche e non duplicate, schema LocalBusiness/ProfessionalService coerente col profilo (Wix lo automatizza, Angular no). Ask Maps non è ancora in Italia: nessuna azione specifica oltre a GBP e recensioni.
- Personal brand (sviluppatore): pagina "chi sono" con entità chiara (nome coerente, link ai profili GitHub/LinkedIn con `sameAs`: pratica comune, da verificare nella doc primaria), progetti con casi concreti e risultati, contenuti originali (articoli tecnici, demo) e presenza su canali terzi; monitorare le ricerche per nome e cognome con il filtro brand di Search Console (solo proprietà a livello radice e con impression sufficienti); coerenza del nome sito (WebSite name); per un rebrand usare il nome alternativo.
- Visibilità su ChatGPT/Perplexity/AI Overviews: trattarla come secondaria e non misurabile con precisione; consentire i bot di ricerca (OAI-SearchBot, PerplexityBot, Bingbot) e decidere su quelli di training; strumenti gratuiti: Bing Webmaster Tools AI Performance e `utm_source=chatgpt.com` nelle analisi; non promettere "posizionamenti" nelle risposte AI; non usare llms.txt o markup speciali come tattica principale (al più opzionale, a costo zero e senza aspettative). Per Google valgono i fondamentali: contenuti utili, tecnica pulita, segnali di brand.


=============== \S07 ===============
# Sintesi del periodo (2026-03-31 → 2026-04-20)

## (a) Tendenze e novità
- Google ufficiale (fatti): March 2026 core update 27/3–8/4 (12 giorni), preceduto dallo spam update 24–25/3; Search Console: attendere 1 settimana dopo la fine, baseline pre-27/3; core update minori avvengono di continuo. Bug impressioni GSC dal 13/5/2025 (click non toccati), correzione in corso. Nuova spam policy sul back button hijacking (enforcement 15/6/2026; può derivare da script/ad di terze parti). I report di spam ora possono generare azioni manuali. Googlebot: 2 MB per URL HTML (header inclusi), 64 MB PDF, risorse esterne con limite proprio, WRS senza stato; il limite "può cambiare".
- Mueller (dichiarazioni): i duplicati non penalizzano, Google sceglie un canonical ma conviene dare hint coerenti; 9 cause di canonical "sbagliato" (inclusa la mancata resa di un framework JS → HTML bootstrap identico); i link in uscita di siti problematici vengono ignorati, non "contagiano"; sitemap multipli non necessari per siti piccoli; i "guru" SEO sono sospetti.
- Narrativa AI: Pichai descrive la ricerca come "agent manager" (visione di prodotto; 2027 anno di svolta; capex 175–185 mld $); Google estende la prenotazione ristoranti agentica in AI Mode (via partner). Serie "agentic web" di Manic (MCP, A2A, NLWeb, AGENTS.md, accessibility tree, agentic commerce): riguarda soprattutto sviluppatori/e-commerce, non il ranking.
- Misurazioni AI: Gemini supera Perplexity come referral (SE Ranking, 101k siti), ma tutta l'AI è ~0,24% del traffico globale e ChatGPT ~80% del referral AI.
- Contro-narrativa: Dias (GEO come categoria creata dai VC), Lily Ray (AI slop loop: informazioni false sulla SEO citate dalle AI), Mueller sui guru, Indig (la maggior parte dei consigli "AI SEO" non regge tra verticali).

## (b) Tattiche pratiche ricorrenti con evidenza
- Fondamenta tecniche prima di tutto (docs/Mueller/Illyes + più autori): contenuto nell'HTML iniziale; metadati/canonical/structured data presto nel documento; CSS/JS pesanti esterni; niente base64 o menu enormi inline; URL e hint coerenti (301, canonical, link interni, sitemap).
- ★ SPA/JS: rendering fallito = HTML shell identico = duplicati/canonical errato (Mueller, ufficiale); crawler AI che spesso non eseguono JS (Manic, Lai/Cloudflare; evidenza debole) → SSR/prerender per le pagine di contenuto, link <a href> reali, niente contenuto nascosto dietro interazioni, router che non rompe il tasto Indietro.
- Accessibilità/semantica come interfaccia per agenti e crawler: elementi nativi, label, heading ordinati, landmark; ARIA solo dove serve (documentazione OpenAI/W3C + studio CHI 2026 su 60 task; indicativo).
- Contenuti per AI: pagina focalizzata su una domanda (500–2.000 parole, heading simili alla query; AirOps 815k coppie, ChatGPT), intro dichiarativa senza condizionali, data di pubblicazione e almeno un numero specifico (Indig, 98k citazioni); nessun numero universale di heading. Correlazioni su ChatGPT, non su Google.
- Brand/entità fuori dal sito: menzioni, recensioni, community, contributi reali (Lai/Forrester, Duane Forrester, Jones, Shepard); studio Shepard (400+ siti): prodotto/servizio proprio, task completabile, asset proprietari, tema stretto, brand forte, effetto cumulativo (correlazioni moderate). Indig: UGC solo ~5% delle citazioni ChatGPT, quasi nullo in finanza/sanità.
- Manutenzione e data: aggiornare i contenuti importanti con date/revisioni visibili (opinione cshel/Clarkson-Bennett; coerente con il dato "DATE" di Indig).
- Misurazione: non cercare coincidenza tra GA4/GSC/CRM; usare i click più delle impressioni per il periodo del bug; segmentare il traffico AI via referral; share of voice/citation su prompt reali (Lai, Indig).
- Bing con IndexNow (Lai): azione di 15 minuti, beneficio sulle risposte AI non verificato con dati.

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt: nessuna piattaforma si è impegnata a usarlo; un audit di log su 1.000 domini AEM non ha mostrato richieste dei bot LLM (Forrester); Illyes ritiene "utopica" la separazione contenuto umano/macchina (il collegamento a llms.txt è inferenza di Montti). Non raccomandarlo come tattica di visibilità.
- ⚠ "Markup per AI": cifre come "2,3x più probabilità nelle AI Overviews con structured data" e "+40% da segnali strutturali (Princeton GEO)" riportate da Forrester senza verifica; Illyes stesso si chiede se lo schema gonfi le pagine. Lo schema serve per rich result e coerenza, non provato come fattore AI.
- ⚠ Stack "machine-readable" a 4 livelli, endpoint API, MCP/NLWeb/A2A per un sito normale: pensati per aziende/dev tool; nessun supporto nelle linee guida Google Search.
- ⚠ "Servire una versione senza JS ai bot": rischio cloaking; Google raccomanda lo stesso contenuto per tutti (SSR/prerender coerente).
- ⚠ "GEO sostituisce SEO" è contestata (Dias); l'"85–90% di SEO ancora valida" (Lai) è una stima non misurata. Gli studi Indig/AirOps/Shepard sono correlazioni su ChatGPT/verticali B2B, non su Google né su professionisti locali.
- ⚠ "Reddit domina le AI" (Duane Forrester: dati AIO/Perplexity 2024–25) vs Indig (ChatGPT, 2–5%): dipende da piattaforma e settore.
- ⚠ Dati Forrester/Lai (conversione 2–4x, +40% m/m, query di 23 parole) senza campione o metodo; i dati SE Ranking/Waikay/Profound sono prodotti da venditori di tool.
- Modelli concettuali d'autore ("autorità = filtro di eleggibilità", "trust come probabilità", "relational knowledge per brand") sono ipotesi.
- Le risposte AI possono essere false e auto-rinforzanti (Lily Ray): non usare fonti LLM come base della skill.

## (d) Implicazioni per la skill SEO
- Audit tecnico: controllare peso dell'HTML iniziale (<2 MB, meta/canonical/JSON-LD presto), contenuto presente nell'HTML iniziale (SSR/prerender per Angular), canonical per route e hint coerenti (trailing slash, parametri), link <a href> reali, resa senza JS, assenza di manipolazione della history/Back (e audit degli script di terze parti prima del 15/6/2026), pagine non identiche tra route, heading/landmark/label.
- Contenuti: una pagina = una domanda chiara; intro dichiarativa, data visibile, dati/numeri verificabili; niente gonfiaggio di lunghezza né numero "magico" di heading; informazioni uniche/di prima mano; aggiornamento mirato con date/revisioni. Prezzi/tariffe dei servizi come condizionali ("dipende da...").
- Locale (professionista orientatrice): coerenza NAP/orari/servizi tra sito, Google Business Profile, directory e piattaforme di prenotazione partner; recensioni; italiano nativo e terminologia locale; tracciare chiamate/prenotazioni come conversioni offline; orari, servizi e modalità di prenotazione in HTML (non solo in JS o PDF).
- Personal brand sviluppatore: asset proprietari (progetti, strumenti, repository, articoli con dati), tema stretto e ripetuto, identità coerente (nome, bio, schema Person) su sito/GitHub/LinkedIn; menzioni terze (conferenze, articoli, community) e ricerche brand; indicizzazione corretta della SPA; tono sobrio sui claim.
- Visibilità su ChatGPT/Perplexity/AI Overviews: base = SEO classica e retrieval (la posizione nel risultato sottostante pesa più dei dettagli on-page); decidere consapevolmente l'accesso dei crawler (OAI-SearchBot, PerplexityBot) in robots.txt; Bing + IndexNow come opzione; monitorare periodicamente un set di prompt reali e il traffico da referral; verificare informazioni errate su di sé; non promettere risultati.
- Non implementare per default: llms.txt, endpoint API/MCP/NLWeb, schema "per AI" oltre ciò che Google documenta, contenuti "per bot" separati. Se richiesti, marcarli come sperimentali e senza evidenza.
- Guardrail di metodo: distinguere sempre fatto Google / correlazione di studio / opinione; segnalare i conflitti d'interesse dei tool vendor; le impressioni GSC sono inquinate dal bug dal 13/5/2025.



=============== \S08 ===============
# Sintesi del periodo (2026-04-20 → 2026-05-07)

## (a) Tendenze e novità
- Doc Google ufficiali del periodo: (1) "Read more" deep links (snippet doc): contenuto visibile al load, niente JS che sposta lo scroll, mantenere hash fragment; (2) robots.txt: solo 4 campi supportati (user-agent, allow, disallow, sitemap), a breve elenco esteso dei campi non supportati e più tolleranza ai refusi di "disallow"; (3) web.dev "Build agent-friendly websites": HTML semantico, label associate, layout stabili, accessibility tree; WebMCP solo sperimentale; (4) Web Bot Auth sperimentale per verificare bot Google; Google-Agent (fetcher user-triggered) ignora robots.txt; (5) Preferred Sources globale (utile solo per news/Top Stories).
- Dichiarazioni Googler: Todorovic e Splitt (Search Off the Record): dare valore, usare l'AI senza moltiplicare contenuti, esperienza umana e giudizio contano di più; Liz Reid: query più lunghe/in linguaggio naturale, "browsy queries" preferiscono la SERP, tesi non verificata dei "bounce clicks".
- Search sempre più "task-based/agentic" (chiamate a negozi, Canvas, AI Mode in Chrome affiancato), senza strumenti di reporting per vedere inclusione/chiamate.
- Dati sul traffico: esperimento randomizzato ISB/CMU (-38% click con AIO, 1.065 utenti), Seer, Pew, Ahrefs, Chartbeat concordano sul calo di CTR; March 2026 core update: perdono aggregatori/UGC, guadagnano proprietari del servizio e domini ufficiali.
- Misurazione AI: ghost citation (Semrush/Indig), BrightEdge (poca sovrapposizione di fonti tra motori, più sui brand), Duda (crawler AI), tracker che inquinano i log, Bing Webmaster Tools con dati sulle citazioni AI e "Citation Share" in arrivo.

## (b) Tattiche pratiche ricorrenti con evidenza
- ★ Contenuto fondamentale in HTML iniziale (no accordion/tab per informazioni chiave; SSR/SSG per SPA): doc Google (deep links) + test curl proposto da Manić; AI crawler non renderizzano JS (dichiarazione di terzi, tabella non datata/non verificata qui).
- ★ HTML semantico e accessibile (button/a, label, heading in ordine, ARIA solo se necessaria): doc web.dev di Google + WebAIM 2026 (pagine con ARIA più errori).
- ★ Robots.txt pulito, testo reale non HTML, decisioni per bot (training vs search vs user fetch): doc Google + Cloudflare (via Manić).
- ★ Locale: GBP sincronizzato, schema locale completo (nome, tel, indirizzo, orari, social), dati coerenti: evidenza solo correlazionale Duda (858k siti su una piattaforma); coerenza NAP è anche pratica consolidata nelle doc Google locali.
- Contenuti con esperienza diretta, dati e prime fonti, non riscritture di specifiche: Splitt (ufficiale), paper GEO (statistiche, citazioni, fluidità), Fishkin/Shepard (400 siti), studio originalità (debole).
- Essere citati da fonti terze (PR, recensioni, podcast, YouTube): BrightEdge, Stacker, Muck Rack (dati di vendor).
- Misurare con dati grezzi (log, GSC, CrUX), non solo punteggi di tool; separare impression e click per mese; non riportare "AI fetches" come successo.
- URL descrittivi e stabili, non ristrutturare per guadagni marginali (opinione).
- Entity/brand: Person/Organization con sameAs e ricerche per nome; Indig: l'AI cita senza nominare, il brand nominato richiede riconoscibilità.

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt: l'autore dell'audit stesso dice "impatto non provato"; nessun supporto Google; Mueller ha bocciato il markdown per bot.
- ⚠ "Technical GEO" / schema che "garantisce" parsing LLM: confutato da Dias (nessuna prova; il paper GEO non testa schema); l'unico claim pro-schema è di Bing/Canel (aiuta Copilot) e Google ("vantaggio in ricerca") riportati di seconda mano.
- ⚠ Percentuali di lift da vendor (AirOps schema +13%, paragrafi corti +49%, Stacker +239%): non riproducibili; sistemi non deterministici.
- ⚠ Correlazioni Duda (50+ post = 33x crawl; più contenuti = più visibilità): effetto di selezione, non causalità.
- ⚠ "Bounce clicks" di Reid: senza dati, contraddetto dallo studio randomizzato sulla soddisfazione.
- ⚠ Previsioni non verificate: "tra 18 mesi tutti chiederanno MCP", sito "fully non-human", WebMCP/NLWeb/A2A per siti normali.
- ⚠ Articoli sponsorizzati/auto-listicle per farsi citare: funzionano a breve (BBC, Ahrefs 44% listicle) ma sono fragili e discutibili.
- ⚠ "Posizione nel primo 30% della pagina" (Indig/via Manić) e "frasi autosufficienti": utili ma non Google.

## (d) Implicazioni per la skill SEO
- Audit: aggiungere controllo di rendering (curl/View Source), robots.txt per bot AI e campi non supportati, HTML semantico/accessibility tree, hash/scroll nelle SPA (deep links), contenuti nascosti in accordion/tab, canonical e sitemap; distinguere raccomandazioni "Google doc" da "terze parti/sperimentali" e dichiarare il grado di evidenza. Verificare con dati grezzi (GSC, log, CrUX), non solo con tool.
- Contenuti: privilegiare esperienza/casi/dati propri, pagine curate e poche; evitare scaling AI e listicle auto-promozionali; prompt di "reverse question generation" come controllo di coerenza tematica.
- Locale (orientatrice): GBP completo e coerente, NAP identico, schema LocalBusiness/ProfessionalService con campi completi, recensioni autentiche, pagina contatti con orari, presenza su directory affidabili; agenti AI possono usare i dati per chiamare/prenotare; valutare Bing Places/BWT. Mantenere info locali in HTML iniziale.
- Personal brand (portfolio dev): entità chiara (Person schema con sameAs a GitHub/LinkedIn), pagina "chi sono" in testo, case study con decisioni e risultati misurabili, ricerche per nome come obiettivo, presenza multicanale (video, community, articoli terzi), non nascondere i progetti dietro form/PDF; per Angular: SSR/prerender, route con URL descrittivi (non hash), componenti semantici.
- Visibilità AI (ChatGPT/Perplexity/AIO): comportamenti diversi per motore; ChatGPT cita molto ma nomina poco; crawler di training non portano traffico (rapporti crawl/referral); non esiste metrica unica; ridurre le promesse; misurare menzioni su un set fisso di prompt con consapevolezza di rumore e non-determinismo; Bing Webmaster Tools per dati citazioni.


=============== \S09 ===============
# Sintesi del periodo

## (a) Tendenze e novità (7-29 maggio 2026)
- ★ Documento chiave del periodo: la nuova guida Google "Optimizing your website for generative AI features" (15/5): AEO/GEO = "ancora SEO"; mythbusting ufficiale (no llms.txt, no chunking, no riscrittura per AI, no mentions artificiali, no schema speciale; lo schema resta utile per i rich result). Focus su contenuto "non commodity", pagina indicizzata e idonea a snippet, HTML semantico, JavaScript SEO best practice, Google Business Profile/Merchant Center per locale e prodotti, agenti (screenshot, DOM, accessibility tree) come sezione opzionale.
- Deprecazione definitiva dei rich result FAQ (stop 7/5/2026; report e Rich Results Test a giugno; API ad agosto). Markup innocuo ma inutile per Google.
- Core update di maggio 2026 (dal 21/5, fino a 2 settimane); March 2026 core update: perdono aggregatori/UGC, guadagnano siti proprietari dei prodotti/servizi (Amsive, SISTRIX, US).
- Google I/O (19-20/5): search box AI, AI Mode con Gemini 3.5 Flash di default, >1 mld utenti AI Mode, agenti di ricerca, booking agentico per servizi locali (USA, estate), link inline e Preferred Sources anche in AIO/AI Mode (345K fonti).
- Misurazione: GA4 ha un canale predefinito "AI Assistant"; Microsoft Clarity/Bing Webmaster Tools mostrano citazioni e grounding queries Copilot; Search Console ancora senza dati AI Mode/AIO.
- Agenti: Google-Agent (fetcher user-triggered che ignora robots.txt), Lighthouse 13.3 con audit "Agentic Browsing" (incl. llms.txt, sperimentale), Cloudflare Agent Readiness Score, UCP.
- Calo di click da AIO: dati multipli (-38% esperimento randomizzato, -58% CTR Ahrefs, Pew 8% vs 15%); contemporaneamente più attenzione/permanenza sulla SERP con AIO (846k sessioni).

## (b) Tattiche pratiche ricorrenti con evidenza
1. Contenuto non commodity/esperienza diretta (guida Google 15/5; Lily Ray su 220+ siti: 54% ha perso ≥30% con contenuti AI scalati; Mueller/Splitt sul vibe coding). Evidenza: documentazione Google + studio osservazionale con caveat.
2. Dati critici nell'HTML iniziale, non solo dopo JS (test "JS off" di Manic, staging con/senza rendering di Pollitt, Machine-First Architecture; Google dice di seguire le JavaScript SEO best practice). Evidenza: indicazioni tecniche coerenti; sui crawler AI le affermazioni sono di autori terzi (searchVIU: leggono solo HTML visibile).
3. Coerenza di identità/entità tra sito e profili esterni (Forrester, Manic; Digital Bloom 2,8x per 4+ piattaforme, correlazione). Evidenza debole-media, di parte.
4. Evitare pagine template scalate: città/lingue programmatiche, FAQ farm, confronti, glossari (Lily Ray). Evidenza osservazionale.
5. Title/meta chiari e specifici: più attenzione sulla SERP con AIO (846k sessioni, dati cursore).
6. Misurare: canale AI Assistant in GA4, Bing/Clarity, log per Google-Agent e bot AI; non reagire ai primi giorni di un core update (doc Google).
7. Staging: crawl multi-user-agent, confronto render/non render, casi limite (Pollitt).
8. CWV: usare dati di campo (CrUX), non solo Lighthouse; attenzione a LCP/INP/CLS e JS di terze parti (HTTP Archive).
9. Form/azioni accessibili (test con screen reader) per futuri agenti (Manic); Google lo considera opzionale.

## (c) Affermazioni discutibili o hype
- ⚠ "Schema per citazioni AI": non supportato (Ahrefs 1.885 pagine: esito nullo/negativo; searchVIU; Google). Limite: pagine già molto citate.
- ⚠ "FAQ schema è critico per GEO" (~168k pagine lo dicono): bocciato da Google (rich result rimossi, nessuno schema speciale).
- ⚠ llms.txt e Markdown per bot: Google Search lo sconsiglia; Mueller "stupid idea" per i non-developer; Lighthouse lo controlla in modo sperimentale (contraddizione interna Google); nessun provider conferma l'uso.
- ⚠ "Chunking" e riscrittura per AI: smentiti da Google. "Lost in the middle" e posizione nella pagina: ricerche accademiche, applicazione SEO non confermata da Google.
- ⚠ Percentuali precise di vendor ("13% lift", "2.8x conversioni", "abbandono agenti ~100%") senza controlli; Adobe vende il tool che il report promuove; Amsive/Lily Ray: correlazioni non causali.
- ⚠ Speculazioni: Preferred Sources come "trust signal" da brevetto, FAQ rimossi perché Google "non ne ha più bisogno", direct traffic come fattore di ranking, brevetto information gain come prova di uso.
- ⚠ Framework enterprise (context graph, governed visibility, agent policy, machine-first) = concettuali, irrilevanti per portfolio/locale.
- Dati interni Google su AI Mode non verificabili; tesi dei "bounce clicks" (Liz Reid) senza dati.

## (d) Implicazioni per la skill SEO
- Audit: (1) HTML iniziale vs renderizzato (SSR/prerender per Angular; title, heading, canonical, link interni, schema, testo chiave presenti senza JS); (2) robots.txt/sitemap, indicizzabilità e idoneità allo snippet; (3) CWV con dati CrUX, controllare JS di terze parti e hydration; (4) log/GA4 per bot AI e canale AI Assistant; (5) pre-lancio: crawl con più UA e render on/off; (6) non raccomandare llms.txt, markdown per bot, chunking, FAQPage per rich result; JSON-LD solo per rich result o per descrivere entità (Person/Organization/ProfilePage/LocalBusiness), senza promettere citazioni AI.
- Contenuti: esperienza diretta, casi, dati propri, opinioni argomentate; evitare pagine template scalate e FAQ farm; autore chiaro con bio e profili collegati; titoli/meta specifici (SERP con AIO più "deliberata"); le risposte semplici (orari, prezzi) sono le più assorbite dall'AI: arricchirle con contesto/esperienza.
- Locale (libera professionista): Google Business Profile completo e coerente (Google lo cita come base per le funzioni AI/agentiche locali); NAP e identità coerenti con sito/directory; evitare pagine città duplicate senza sede reale; form di contatto/prenotazione accessibili e non bloccati da CDN/firewall per Google-Agent; recensioni autentiche (mentions artificiali sconsigliate da Google). Per le query conversazionali lunghe (AI Mode) scrivere contenuti che rispondono a domande reali dei clienti (da conversazioni vere, non "FAQ farm").
- Personal brand (sviluppatore): definizione canonica di sé coerente su portfolio, LinkedIn, GitHub, blog; contenuti da esperienza reale (case study con dati, decisioni, errori); pagina "chi sono" con Person schema opzionale; target recruiter: la SERP del proprio nome conta anche con AIO; costruire audience diretta (newsletter) per ridurre la dipendenza da Google (barbell di Condé Nast); non gonfiare metriche.
- Visibilità su ChatGPT/Perplexity/AIO: ogni motore ha un pool di fonti molto diverso (2,37% di URL in comune tra i tre motori; solo ~11% di domini cross-piattaforma; AIO cita sempre meno la top 10): misurare per motore, non con un solo "AI score"; registrarsi a Bing Webmaster Tools (ChatGPT/Copilot si appoggiano a Bing secondo fonti di terzi, da verificare); consentire i bot AI in robots.txt se si vuole visibilità (GPTBot/OAI-SearchBot/ChatGPT-User, ClaudeBot/Claude-SearchBot, PerplexityBot; Google-Extended riguarda solo il training Gemini); presenza autentica su fonti molto citate (Wikipedia, YouTube, Reddit, news).
- Governance della skill: separare "doc Google" (affidabile) da "studi di terzi" (con campione e conflitto d'interesse) e da "opinione"; dichiarare il livello di evidenza di ogni raccomandazione; dopo un core update attendere almeno una settimana dal completamento prima di analizzare.


=============== \S10 ===============
# Sintesi del periodo (30 maggio – 13 giugno 2026)

## (a) Tendenze e novità del periodo
- ★ Google ha pubblicato una guida all'ottimizzazione per la ricerca generativa: "ancora SEO"; nessun file speciale, nessuno schema speciale, no chunking/riscrittura per AI (fonte indiretta: Manic, 575497; Pollitt/altri la richiamano). Pagina "Do you need an SEO?" riscritta e nuova pagina su tool/consigli di terzi (578151, 578162): Google chiede che ogni consiglio sia sostenuto da documentazione ufficiale o dichiarato come opinione.
- John Mueller su llms.txt: "puramente speculativo", nessun sistema AI lo usa; preferisce WebMCP e integrazioni commerce; il livello minimo di ottimizzazione per gli agenti è "non bloccarli" (577576). Lighthouse (Canary) ha una categoria "Agentic Browsing" che controlla anche llms.txt (577421).
- Web agentico: web.dev "Build agent-friendly websites" (7 regole = accessibilità), Chrome auto-browse su Android da fine giugno, Universal Cart/agentic booking/chiamate agli esercenti locali (I/O), UCP, WebMCP in Chromium 146 (575495, 574698, 576217, 574224).
- Misurazione AI: Search Console testa (UK) report "Generative AI" (solo impressioni, niente click) e toggle di opt-out a livello di dominio; CMA UK impone l'opt-out; Bing Webmaster Tools con citazioni AI/Citation Share; GBP→GA4 (7 metriche, 6 mesi) e GBP in Gemini (578003, 577978, 577891, 578107, 578824).
- May 2026 core update (21 mag–2 giu): volatile; analisi (SISTRIX/Solís, SE Ranking) indicano premio al "fit di tipo di fonte/intento/mercato", Reddit in crescita nelle nicchie "esperienza" (non YMYL), .com perde su mercato UK a favore di siti locali (577996, 578502, 577704).
- Dati sul calo dei click: SparkToro/Similarweb: 232 click open-web ogni 1.000 ricerche USA, 68% zero-click (578724); AIO: click −~60% (Ahrefs citato); quota AI Mode ancora <0,25% degli eventi desktop (578349); BrightLocal: 45% usa AI per consigli locali (575702).
- Apple: Siri AI con web answers; controlli via Applebot/Applebot-Extended/nosnippet (578931).
- Pichai (577489, 577923): "fonti e link ci saranno sempre", transizione graduale a AI Mode, mix abbonamenti+ads, "click di bassa qualità filtrati".

## (b) Tattiche pratiche ricorrenti con evidenza a supporto
- Non bloccare crawler/agenti legittimi (robots.txt, WAF, CDN): Mueller (577576), caso CDN che bloccava Googlebot (575543), BrightEdge (575379, vendor), Manic (575499). Distinguere training / search / user agent; decisione deliberata. Evidenza: dichiarazione Google + casi, non studi controllati.
- ★ HTML semantico e accessibilità (button/a, label for, no overlay, layout stabile, contenuto visibile senza JS): web.dev (via 575495), 574698, 575543, 577421. Evidenza: guida Google (formula "consider"), nessun legame dichiarato con ranking.
- ★ Contenuto critico non dipendente da JS lato client / SSR: 574224, 575597, 574698, 575489 (opinioni di practitioner, coerenti con la documentazione Google sul JS ma qui motivate con agenti AI).
- ★ Coerenza di identità/entità (nome, NAP, sameAs, profili LinkedIn/GitHub, pagine autore/about, @id nel JSON-LD): 575597, 577854, 578567, 574224, 575702. Evidenza: opinioni + SOCi (correlazioni).
- ★ Locale: GBP completo e aggiornato, orari corretti, attributi, risposta alle recensioni, recensioni con contesto di servizio/luogo; collegare GBP a GA4; sito che spiega i servizi (575702, 577542, 578107, 576217). Evidenza: sondaggi di esperti (Whitespark/BrightLocal), SOCi (vendor), non conferme Google.
- Contenuto non-commodity con esperienza di prima mano, dati/esempi propri, "uno strato che l'AI non può replicare" (577891, 578379, 578567, 576068, 577996). Evidenza: coerente con guida Google; nessun esperimento causale.
- Migrazioni/redesign: 301 1:1, niente noindex/canonical vecchi, sitemap, no sottodominio legacy (575102): esperienza dell'autrice, in linea con la Site Move guide Google.
- Verifica manuale della visibilità AI: stesse query su più motori, leggere citazioni, ripetere trimestralmente (578192); test "senza JS + solo tastiera" del flusso di prenotazione (574698).

## (c) Affermazioni discutibili / hype (⚠)
- llms.txt come tattica di citazione: smentito da Google (Mueller, guida GEO); persino i sostenitori lo limitano a casi per agenti. Nessun dato di adozione (577576, 577854 con benchmark Grimm).
- "AI schema", "Integrity Graph", EntityMap, "Machine-First Architecture", "machine comfort bias": framework di autori/vendor senza dati di impatto; EntityMap proposto da chi lo sponsorizza (576146). Lo studio Ahrefs citato (1.885 pagine, nessun incremento di citazioni con schema) va contro l'idea che lo schema muova le citazioni.
- "Brand is the new backlink", "nofollow PR che fa posizionare nelle AI", "Siri optimization": slogan/aneddoti (578567, 578931).
- Cifre di vendor (BrightEdge 150% e 40 mld $, SOCi, SE Ranking, Kinsta) non verificabili in modo indipendente; Adobe +393% traffico AI retail/+42% conversione è US retail, non trasferibile a siti-vetrina.
- Previsioni "i fallimenti degli agenti sono invisibili e vi costeranno prenotazioni" (574698): plausibile ma speculativo; Chrome auto-browse è a pagamento (AI Pro/Ultra) e inizialmente su pochi dispositivi.
- Pichai: "link sempre presenti" e click "di bassa qualità" non supportati da dati pubblici; Search Console AI senza click non permette di verificare.

## (d) Implicazioni per la skill SEO
- Audit tecnico: aggiungere un livello "agent/AI readability" basato su fonti Google: crawlability (robots/WAF/CDN, status code), rendering (contenuto e CTA nel DOM iniziale; SSR/prerender per Angular), HTML semantico/accessibilità (7 regole web.dev + WCAG), form con label, nessun CAPTCHA/modale bloccante nel flusso di conversione, velocità. Verificare noindex/canonical/redirect (specialmente dopo migrazioni). Segnalare esplicitamente: llms.txt non necessario per Google.
- Contenuti: privilegiare risposte dirette in apertura, specificità, esperienza di prima mano, dati propri; evitare riscrittura "per AI", chunking e densità keyword come tattica; usare semantic alignment solo come segnale direzionale.
- Locale (orientatrice di carriera): GBP completo e coerente con il sito (servizi, orari, area, attributi), cura delle recensioni (richiesta e risposta), NAP uniforme sulle directory, pagine servizio/località chiare, collegamento GBP–GA4 e monitoraggio chiamate/indicazioni; prepararsi a chiamate/prenotazioni automatiche (disponibilità e prezzi chiari, risposta telefonica/segreteria con info essenziali, form di prenotazione accessibile).
- Personal brand (sviluppatore, target recruiter): entity home (About/profilo) con Person schema + sameAs (GitHub, LinkedIn); coerenza di nome/bio sui profili; pagine progetto con esperienza reale e risultati; LinkedIn come fonte che i motori AI associano a competenza professionale (BrightEdge, correlazione); le Search Profiles non sono accessibili (soglie follower). Chiave: ricerche per nome/brand, non traffico generico (SparkToro: SEO ancora utile per brand, locale, transazionale).
- Visibilità su ChatGPT/Perplexity/AI Overviews: AIO/AI Mode usano l'indice Google (Google-Extended non incide); Perplexity recupera quasi sempre; ChatGPT/Claude/Copilot decidono per query; Bing Webmaster Tools utile per citazioni. Non esistono ancora metriche affidabili: la skill deve proporre audit manuale di prompt/citazioni ripetuto nel tempo e Search Console (report AI quando disponibile), evitando promesse di ranking AI.
- Policy sui bot: chiedere esplicitamente all'utente se vuole essere citato dalle AI; consigliare robots.txt distinto per training (GPTBot, Google-Extended, Applebot-Extended, CCBot) e search/user agent (OAI-SearchBot, ChatGPT-User, PerplexityBot); ricordare nosnippet come controllo granulare.
- Fonti e metodo: la skill deve citare la documentazione Google come fonte primaria e marcare le affermazioni di terzi come opinione/correlazione (indicazione della nuova pagina Google); cautela con tool e metriche proprietarie.


=============== \S11 ===============
# Sintesi del periodo

## (a) Tendenze e novità del periodo (14–30 giugno 2026)
- Linea ufficiale Google: "GEO/AEO" è SEO. Fox (GML 2026): ottimizzare per l'AI search è come per la ricerca, ottimi contenuti che vanno oltre la superficie; Kraham: "good SEO is good GEO", Google non valuta tool SEO di terzi; Reid: contenuti che le persone vogliono leggere + accesso al crawl; Mueller: ciò che serve agli utenti serve anche ai browser agentici, "non bloccare alla cieca i browser agentici".
- llms.txt e Markdown, giro di vite coordinato. Changelog Google giugno 2026: si possono fare per altri servizi, ma Google Search li ignora (né aiuta né danneggia). Mueller/Splitt (Search Off the Record ep. 111): llms.txt non serve alla discovery ed è auto-dichiarato quindi non affidabile; versioni Markdown parallele = doppio lavoro e guasti invisibili (analogia col dynamic rendering); convertire HTML in testo è banale. Dato Ahrefs: 97% dei llms.txt su 137.000 domini senza richieste, bot di retrieval 1% dei fetch; SE Ranking (300k domini) nessun effetto evidente.
- Spam: spam update 24–26 giugno 2026 (secondo del 2026), nessun cambio di policy; a maggio Google ha chiarito che manipolare le risposte generative (comprare/alterare citazioni) è spam. Lily Ray: cali di siti con listicle auto-promozionali e contenuti AI scalati (gennaio e core update di maggio; osservazioni, non conferme Google). Preprint Cornell: i report degli agenti di ricerca sono avvelenabili via UGC.
- Misurazione AI: Bing Webmaster Tools AI Performance (Citation Share, Intents, Topics, Compare, preview); GSC senza dati sulle citazioni; Mueller: impression AI = link comparsi (non quelli dietro espansione se non aperti), niente clic. Bug impression GSC (maggio 2025-aprile 2026) corretto senza ripristino. CTR: AWR Q1 2026 desktop in crescita, mobile -2,2 punti in pos. 1; Ahrefs -58%/Pew per query con AIO.
- Traffico e agenti: Cloudflare Radar, bot oltre il 57% delle richieste HTML; AI Mode 1 miliardo di utenti (Google, 20 mag). Chrome auto-browse e Gemini agent; spec draft ARD v0.9 e OKF v0.1 (non per siti di contenuto).
- Preferred Sources in AIO/AI Mode (badge), Search Profiles (100k+ follower). Doc migrazione: Change of Address per tutte le varianti (www, non-www, sottodomini). Regolazione: CMA UK (ranking equo, preavviso), tribunale di Monaco (AIO è contenuto di Google).
- Indicizzazione: ondata di segnalazioni "crawled, currently not indexed" da aprile; Google: nulla di insolito.

## (b) Tattiche pratiche ricorrenti con evidenza a supporto
- HTML con contenuto visibile senza JavaScript (SSR/SSG/prerender) per home, servizi, prezzi: studio con dati (274 homepage, 36% sotto l'80% nel raw HTML, 101 al 100%) + accessibility tree + Mueller/Splitt (HTML base della discovery). Evidenza più forte per i bot AI che per Googlebot (che renderizza). ★ Rilevante per Angular.
- Accessibilità e markup semantico (button/a nativi, label, testi accessibili): WebAIM Million 2026 (95,9% con errori; link vuoti 46%, pulsanti vuoti 31%); OpenAI Atlas usa ARIA. ARIA solo dove manca l'equivalente nativo (pagine con ARIA: più errori, correlazione).
- Contenuti unici, con esperienza diretta; consolidare invece di moltiplicare (cshel, opinione) + Reid/Fox (dichiarazioni Google).
- Internal linking governato (link a redirect, orfane, hub): guida tecnica senza dati, in linea con la prassi.
- Verifiche tecniche a basso costo: meta description solo per pagine chiave (Mueller + doc), robots.txt non deindicizza, X-Frame-Options/CSP frame-ancestors (Mueller) e altri security header (opinione), diagnosi GSC (query ad alto volume e zero clic).
- Locale: recensioni come ricerca (2–3 competitor, temi, linguaggio) per H1/GBP/FAQ; coerenza NAP e profili esterni; recensioni anche oltre Google; pagine città solo se uniche (rischio "thin template").
- Monitoraggio: segmento traffico AI (utm_source=chatgpt.com, referral chat.openai.com/gemini.google.com), ricerca brand come proxy (Similarweb: 55,9% del traffico a valle di una raccomandazione ChatGPT passa da ricerca brand), verifica IP dei bot nei log (Forrester: 81,8% dei "bot AI" falsi e ~87% dei "Googlebot" falsi su un sito nuovo), prompt set ripetuti (frequenza di citazione, non rank).
- Landing con l'azione in alto (prenotazione/contatto) per visitatori da AI Mode (argomento di un autore con dati Google/Adobe).

## (c) Affermazioni discutibili o hype
- ⚠ "Schema/JSON-LD fa citare dagli LLM": evidenza debole. Esperimento Williams-Cook (JSON-LD invalido letto comunque come testo) e Ahrefs (1.885 pagine vs 4.000 controlli: effetto nullo, ma popolazione già molto citata). Schema resta utile per disambiguazione e rich result Google; per un personal brand con omonimi vale Person + sameAs, ma non come leva di citazione garantita.
- ⚠ llms.txt, pagine "AI Instructions" in Markdown, ARD/OKF/WebMCP per siti di contenuto: nessun beneficio dimostrato su Google; i casi Nectiv/Seer su ChatGPT sono esperimenti singoli con impatto di business modesto e al confine con la manipolazione.
- ⚠ "Diluizione degli embedding", "vector competition", "accessibility tree = ranking AI": ragionamenti, non evidenza.
- ⚠ "I bot AI non eseguono JS": plausibile ma non confermato dai vendor; lo studio fintech lo deduce dal gap raw-vs-render.
- ⚠ Percentuali "segnali di ranking location page" e recensioni indotte con "semantic triples" (Wiideman): metodo non spiegato, rischio policy recensioni.
- ⚠ Recensioni/Reddit/menzioni acquistate: nelle spam policy Google (manipolazione AI); la previsione tipo Penguin è un'analogia dell'autore.
- ⚠ Campioni piccoli: Forrester (1 sito, 14 giorni), iPullRank (3 account, 17 giorni), Lily Ray (100 query B2B SaaS), Wiideman (n=1); preprint Cornell non peer-reviewed.
- Refuso nell'articolo QueryFan ("10 settembre 2026" per la rimozione di num=100, in realtà settembre 2025): cautela sui dettagli. Diversi autori promuovono il proprio tool (QueryFan, CitationIQ, GBP Sentiment Analyzer).

## (d) Implicazioni per la skill SEO
- Audit tecnico: aggiungere il test "JS disabilitato / HTML grezzo" (curl vs render) e il controllo dell'accessibility tree (HTML nativo, link/pulsanti con nome, label, lang). Su Angular verificare SSR/prerender per home, servizi, about, contatti, blog. Controllare robots.txt per bot AI senza blocchi involontari (Mueller), sitemap, canonical, noindex vaganti, security header (X-Frame-Options/frame-ancestors). Distinguere avvisi GSC non azionabili (es. "indexed though blocked by robots") e ricordare il bug impression 2025-2026 nei confronti storici.
- Contenuti: poche pagine forti, esperienza diretta (casi, risultati, firma), niente listicle "siamo i migliori" né contenuti scalati/ridondanti; meta description solo per pagine chiave; internal linking pianificato (link a redirect, orfane, hub).
- Locale (orientatrice di carriera): GBP completo e coerente, NAP identico ovunque (Bing Places, Apple Maps, directory di settore), analisi di sentiment delle recensioni proprie e dei 2–3 concorrenti per H1/FAQ/descrizione GBP, raccolta recensioni genuina anche oltre Google; una pagina per servizio/città solo se davvero diversa; CTA di prenotazione in alto; monitorare chiamate/indicazioni in GBP Insights e ricerche brand.
- Personal brand (sviluppatore, target recruiter): entità chiara e coerente (Person + sameAs verso GitHub/LinkedIn, About con fatti verificabili, stessa descrizione ovunque), menzioni di terzi (articoli, talk, repo) invece di autocelebrazione, pulsante "Preferred Sources" solo se si pubblica contenuto editoriale; audit periodico di cosa dicono ChatGPT/Perplexity/AIO sul proprio nome (omonimi).
- Visibilità AI (ChatGPT/Perplexity/AIO): "GEO = SEO" come baseline (Google: nessun markup speciale richiesto per AIO/AI Mode). llms.txt/Markdown: opzionali, non raccomandati come tattica SEO (zero effetto su Google, pochi fetch dai bot di retrieval). Misurare con prompt set ripetuti e frequenza di citazione, UTM/referral AI, ricerca brand, Bing AI Performance; verificare i bot via IP prima di trarre conclusioni dai log. Evitare manipolazioni (recensioni/Reddit/listicle): ora esplicitamente nelle spam policy.


=============== \S12 ===============
# Sintesi del periodo

## (a) Tendenze e novità del periodo (30 giu – 18 lug 2026)
- Fatti Google/Chrome/Apple/Cloudflare: Search Console aggiunge un report "generative AI" (solo impressioni, non click; rilascio iniziale UK) e le "platform properties" per post Instagram/TikTok/X/YouTube; la guida Google sull'AI search (citata da SEJ) dice che AEO/GEO sono "ancora SEO". AMP: dal 1 luglio niente più AMP cache/signed exchanges. Documentazione aggiornata: canonical (fino a 2 settimane dopo la correzione del contenuto), JavaScript (canonical iniettato via JS), Merchant Listing (category, sale duration), nuovo user agent Google-GeminiNotebook. Lighthouse 13.3 introduce la categoria "Agentic Browsing". Chrome Auto-Browse su Android; Safari MCP server; WebMCP in origin trial Chrome 149–156 con guida di sicurezza. Cloudflare dal 15 settembre: regola del crawler multiscopo (rischio di bloccare Googlebot se si blocca "Training").
- Tema dominante: infrastruttura "per macchine" (llms.txt, OKF, ARD, MCP/WebMCP, markdown per AI) contro la posizione di Google (Mueller: llms.txt non usato, content-signal inutile, no versioni markdown parallele, "un sito fatto bene funziona per tutti").
- Bot AI: ChatGPT-User e Perplexity-User non rispettano più robots.txt; i fetch utente di Google (Notebook) neppure; servono WAF/regole server per bloccarli.
- Misurazione AI: instabilità statistica dei ranking di visibilità AI; studio sulle raccomandazioni che svaniscono dopo una domanda di contesto (62%); Bing con AI Performance/Citation Share.
- Click: -39,8% di click organici con AIO (esperimento randomizzato); 68% delle ricerche senza click (Fishkin/Similarweb); fiducia USA 28% verso AI vs 70% verso motori (YouGov, solo USA).

## (b) Tattiche pratiche ricorrenti con evidenza
- Fatti chiave (prezzi, servizi, credenziali) in HTML disponibile al primo caricamento, non in JS/immagini/PDF. Evidenza: traffico di rete ChatGPT (singolo ricercatore, ragionamento del modello sul JS), report Siteline (100 prodotti B2B, agente Claude simulato), Mueller sul valore dell'HTML normale, audit "JS disabilitato" (Manic). ★ SPA Angular: SSR/prerender fondamentale.
- Link come `<a href>` reali (doc Google + Mueller); in Angular `routerLink` su `<a>`.
- Passaggi autosufficienti, risposta in apertura, entità nominate esplicitamente (Forrester su Web IQ; Montti sullo snippet); fatti coerenti tra le pagine (coerenza, non markup per AI).
- Contenuto non-commodity: dati originali, esperienza diretta, casi, autore identificabile (Sullivan a Toronto, Mueller "insightful & useful", Kevin Indig 3,3x citazioni per ricerca first-party, aneddoti su temi specifici). Evidenza di qualità media (dichiarazioni Googler + opinioni + studio di terzi).
- Autorità fuori sito: menzioni su terze parti, Reddit, PR su associazioni di categoria; Muck Rack (25 mln link: 84% menzioni guadagnate), Ahrefs su Reddit citato 1,93%; ChatGPT cita G2/terze parti quando la pagina ufficiale non è leggibile. Studi di terzi, tendenza coerente ma campioni B2B/SaaS.
- Misura: ricerche di marca in Search Console (filtro branded), report generativo di GSC, log file per i bot, canale "AI Assistant" di GA4 (non cattura Perplexity), prompt ripetuti più volte (instabilità >99% secondo SparkToro/IQRush).
- Non bloccare alla cieca bot di ricerca AI/agenti (Pollitt; Mueller sugli agenti): decisione per bot con matrice valore/costo; attenzione a Cloudflare.
- Indicizzazione: se molte pagine sono "scoperte/scansionate ma non indicizzate" senza cause tecniche, ripensare la qualità complessiva (Mueller/Splitt).
- Meta description: fattuale, unica per pagina, senza keyword/CTA forzate (Montti, coerente con la doc Google).
- LCP: identificare l'elemento LCP reale; niente lazy-loading sulla prima immagine; `fetchpriority="high"` su 1–2 immagini (caso Nuvemshop, web.dev).

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt, llms-author.txt, Content-Signal in robots.txt, markdown per agenti, OKF/ARD per siti pubblici: nessun supporto di Google (Mueller); nessun crawler lo conferma; l'audit Lighthouse verifica solo la sintassi. OKF "off-label" ammesso dagli stessi autori.
- ⚠ Brevetto di information gain, "contentEffort", Navboost come spiegazione (Clarkson-Bennett, Montti): un brevetto non prova l'uso reale; "10% di differenza" è speculazione; la regola dei 130–140 giorni di ricrawl è empirica; "E-E-A-T inutile" è opinione.
- ⚠ Studio ChatGPT (Mohanadasan): 1 account, query SaaS/tech, percentuali "direzionali" per ammissione dell'autore; `labrador/bright/oxylabs` sono osservazioni sul traffico, non documentazione.
- Dati Clovion, Fuel Online/Profound, Muck Rack: B2B/SaaS e fonti con interesse commerciale (Clovion ha corretto un errore di zeri); eMarketer è una previsione.
- Liz Reid: "personalizzazione aiuta i piccoli" e "bounce clicks" senza dati; l'esperimento randomizzato li contraddice.
- Interpretazioni speculative (social report come "trappola", Google che "maschera" la perdita di click) senza evidenza.
- Nuvemshop: +8,9% di conversioni è un confronto pre/post senza controllo; CWV è un fattore minore (Mueller).
- Enterprise/agenzie/plugin (WPVibe, "Unified Object Graph" di Bill Hunt, Kaushik sui contratti): non rilevanti per i due siti.

## (d) Implicazioni per la skill SEO
- Audit: (1) rendering: contenuto, link (`<a href>`), canonical, meta e dati strutturati nell'HTML iniziale (SSR/prerender per Angular); (2) indicizzazione: controllare "scoperta/scansionata non indicizzata" e collegare alla qualità complessiva; (3) robots.txt + WAF/Cloudflare: Googlebot e bot di ricerca AI non devono essere bloccati per errore; decisione informata su training/fetch utente (robots.txt non basta per ChatGPT-User, Perplexity-User, Google-GeminiNotebook); (4) LCP reale; (5) llms.txt mai come requisito: se presente, solo extra opzionale e accurato.
- Contenuti: pagine specifiche con esperienza diretta, dati o casi propri, passaggi autosufficienti e autore chiaro; evitare scaled content e pagine-segnaposto; niente versioni "per AI" parallele; separare pagine di conversione da pagine informative; nessuna regola di lunghezza o densità keyword (nessuna evidenza ufficiale).
- Locale (orientatrice): Business Profile curato e controllato sul profilo pubblico (bug recensioni a luglio 2026), scheda Apple Maps/Business, recensioni, NAP coerente; ChatGPT restituisce solo 2 risultati locali (osservazione singola); niente pagine-città clonate; PR su associazioni professionali/ordini/enti locali; esplicitare "per chi" è il servizio (le liste AI cambiano con il contesto).
- Personal brand (sviluppatore): disambiguazione del nome (omonimi: about page con fatti chiari, profili coerenti su GitHub/LinkedIn/X/YouTube, menzioni esterne, collegamento profili in Search Console), case study con dati/esperimenti propri, contenuti specifici su nicchie, audience diretta (newsletter), ricerche di marca come KPI.
- Visibilità su ChatGPT/Perplexity/AIO: nessun "fattore di ranking AI" segreto; massimizzare copertura di terzi, HTML leggibile, fatti corretti; test manuale con 15–20 prompt ripetuti (con avviso di instabilità); usare report generativo di GSC e AI Performance di Bing per una parte del quadro; mai una sola rilevazione.
- Da NON includere come raccomandazioni: llms.txt/OKF/ARD/WebMCP per siti vetrina, markup "per AI", schema come scorciatoia di citazione, contenuti markdown paralleli, regole di lunghezza.


=============== \S13 ===============
# Sintesi del periodo (19 lug – 4 ago 2026)

## (a) Tendenze e novità
- Misurazione AI: Google ha lanciato in test (3 giu) il report "Generative AI" in Search Console (solo impression di AI Overviews/AI Mode per pagina/paese/dispositivo/data, niente click, query, CTR), più il pilota Merchant Center (solo US, solo chi ha feed) e le "platform properties" (social: Instagram/TikTok/X/YouTube) aperte a tutti. Google ha detto che i tool AI-visibility di terzi non vedono le sue metriche interne. Nessun dato di click AI pubblicato.
- Controllo nuovo: impostazione Search Console per escludere il sito da AI Overviews, AI Mode e funzioni AI di Discover (attiva dal 17 giu, rollout a un sottoinsieme, imposta dal regolatore UK/CMA); Google-Extended resta separato e non incide su Search.
- Indicizzazione e qualità: forte messaggio Google (Mueller/Splitt, Toronto) che "crawled-not indexed" è quasi sempre qualità/commodity content, non un bug da correggere; i report GSC vanno letti come pattern; Google più severo sull'indicizzazione. Azione manuale parziale per thin content su un forum con chatbot AI (ipotesi non confermata). Ahrefs: pagine molto "AI-flagged" rankano ancora ma un po' più in basso e sono meno indicizzate.
- Documentazione Google aggiornata: linee guida review snippet (recensioni false/incentivate non dichiarate → azione manuale), crawl budget (304, capacità condivisa), robots.txt (gruppo user-agent specifico prevale), metadati in conflitto (nessuna precedenza pubblica), unavailable_after.
- Mercato AI: ChatGPT Atlas chiuso (9 ago), commercio agentico (ACP/UCP), pay-per-crawl (Cloudflare, AWS), OKF v0.2 (Google Cloud), PACT; molto rumore enterprise/agentico. Similarweb: ricerca ~5x i chatbot, 95% degli utenti ChatGPT usa ancora Google.
- Sentenze/regolazione: Munich (Google responsabile di AI Overview false, in appello), DMA (dati ai rivali, multe), AI Act art. 50 in vigore.

## (b) Tattiche pratiche ricorrenti, con evidenza
- Coerenza dei fatti di identità e locali (NAP, orari, categorie, descrizione) su sito, Google Business Profile, Apple/Bing, directory, profili: citata in 6+ articoli (Searchable: 93% delle PMI londinesi con almeno un errore su 13.365 domande; Uberall/AthenaHQ; Heitzman). Evidenza: dati di vendor, plausibile ma non Google.
- Audit manuale delle risposte AI: lista fissa di domande sui propri fatti, ripetute, su AI Overviews/AI Mode/ChatGPT/Gemini/Perplexity; Fishkin: singole risposte sono rumore (servono molte ripetizioni).
- Contenuto non-commodity: esperienza diretta, dati propri, casi reali (Google a Toronto, Mueller/Splitt, Haynes, Ahrefs). Evidenza: dichiarazioni Googler + studio correlazionale.
- Menzioni e conferme di terzi indipendenti (premi, stampa locale, liste con criteri reali): Jones, Uberall, Forrester (la memoria degli LLM si forma dal consenso del web, non dal markup). Evidenza: opinioni e dati di vendor; Omniscient: 77% delle citazioni su query di brand viene da fuori sito.
- Tecnico: robots.txt non è noindex; noindex su pagine di ricerca interna; non bloccare CSS/JS con regole come `Disallow: /*?*`; verificare cosa vede Google con Ispeziona URL/Test live; il "limite 5 secondi" di rendering è un mito (test Dave Smart + Splitt); allineare HTML iniziale, DOM renderizzato e schema (Mueller); attenzione a WAF/CDN che servono pagine "sei un bot?" a Googlebot.
- Misurazione: referral AI classificati in GA4 con regole (floor), brand search e campo "come ci hai conosciuti?" per l'influenza; mediana invece di posizione media; separare citazioni da conversioni (Solis: 58,8% del traffico AI atterra sulla homepage mentre il 65% delle citazioni è su pagine profonde).
- Perplexity (studio con n minuscolo): cerca sempre, premia testo letterale e video; per query locali pesa l'indice mappe/GBP; la pagina del vendor vince nei confronti "X vs Y".

## (c) Affermazioni discutibili / hype
- ⚠ "Foto di landmark verificano la legittimità geografica" (Heitzman), "finestra di 12–18 mesi", tabelle/FAQ schema che aumentano le citazioni: nessuna base Google; FAQ rich result di Google è stato eliminato (giu 2026) e lo stesso articolo linka un test Ahrefs in cui lo schema non ha mosso le citazioni.
- ⚠ llms.txt, OKF, WebMCP, markdown per agenti, EntityMap, "Machine-First Architecture": nessun agente li legge oggi (ammesso da Manic e Moss); Google non li documenta per Search (Google sconsiglia versioni markdown). Non priorità.
- ⚠ "Schema/entity mapping addestra ChatGPT/Claude" (smentito da Forrester); correlazione schema-citazioni spiegata da qualità/menzioni.
- ⚠ Senza i campi priceValidUntil/deliveryTime/returnDays "Gemini non include il prodotto" (articolo ecommerce del 21 lug, audit proprio dell'autore; irrilevante qui).
- ⚠ Tokenizzazione lingue europee come "nuova disciplina di localizzazione" (Motoko Hunt): nessuna evidenza.
- ⚠ Cover-all dei fan-out query come strategia: Haynes ipotizza rischio di scaled content; non provato. Penalità link "più che in cinque anni" (Taylor): aneddotico.
- Dati di vendor non indipendenti (Searchable, Uberall/AthenaHQ, NewzDash, Visibility Labs); Whitespark compare con valori diversi (15% vs 68%) a seconda del tipo di query: citare con cautela.
- Il prompt tracking come "metrica di vanità" è opinione forte ma ben argomentata.

## (d) Implicazioni per la skill SEO
- Audit tecnico: includere robots.txt (precedenza dei gruppi user-agent, regole che bloccano risorse), noindex vs disallow, pagine di ricerca interna, Ispeziona URL per SPA/Angular (contenuto nel DOM renderizzato, nessun limite fisso di 5 s ma dipendenza da richieste di rete lente per i crawler non-Google), coerenza HTML/DOM/JSON-LD (anche date: visibile vs dateModified vs lastmod), WAF/CDN che bloccano Googlebot o servono challenge, JSON-LD nel sorgente (non dietro consenso/GTM), interpretare GSC come pattern (404, redirect, "non indicizzata").
- Contenuti: criterio "non-commodity" (esperienza, dati propri, casi); se molte pagine sono "crawled-not indexed", diagnosticare qualità complessiva prima di ritoccare; niente contenuti AI su scala; risposte dirette in alto, titoli descrittivi, informazioni importanti in HTML (non solo in tab/immagini/JS); aggiornamento periodico con data di obsolescenza.
- Locale (orientatrice): dati NAP e GBP coerenti, recensioni reali (no incentivi non dichiarati: rischio azione manuale), pagine servizio/sede non fotocopia con FAQ locali e prezzi/range, citazioni locali indipendenti, audit trimestrale delle risposte AI, verifica fonti obsolete (es. vecchi thread).
- Personal brand (sviluppatore): coerenza dell'identità (Person con @id e sameAs verso LinkedIn/GitHub, nome uguale ovunque), pagine "chi sono" ed esperienza concreta, case study con dati reali, menzioni indipendenti (articoli, talk, repo), video/YouTube come canale aggiuntivo; platform properties in Search Console per social/video.
- Visibilità su ChatGPT/Perplexity/AI Overviews: trattare come estensione della SEO; non bloccare i bot di ricerca AI se si vuole essere raccomandati (decidere separatamente training e ricerca); misurare con GSC generative report (impression), brand search, campione ripetuto di prompt, referral classificati in GA4, "come ci hai conosciuti"; evitare di promettere ranking AI; documentare che nessuna fonte pubblica fattori di ranking di Perplexity/ChatGPT.
- Da escludere o marcare come "sperimentale": llms.txt, OKF, WebMCP, EntityMap, markdown per agenti, protocolli di commercio agentico.


=============== \S14 ===============
# Sintesi del periodo (4–24 agosto 2026)

## (a) Tendenze e novità
- Misurazione AI: Google ha lanciato il report "Generative AI performance" in GSC (3/6/2026, live per tutti dall'11/8): solo impression per pagina/paese/dispositivo/data, niente query, niente clic, niente API/BigQuery. Le conversazioni di AI Mode finiscono come "query" strane nel rapporto Prestazioni (conferma Mueller). Bing ha un AI Performance Report con "grounding queries" (da febbraio 2026).
- Google: spam update 18–21/8/2026 (terzo dell'anno, nessuna nuova policy); dal 15 maggio le spam policy valgono anche per la manipolazione delle risposte generative; generative UI (strumenti interattivi generati) da AI Mode agli AI Overviews; pulsante Preferred Sources incorporabile (>600.000 fonti); opt-out "generative AI" in test in GSC (UK); guida ufficiale AI optimization (developers.google.com/search/docs/fundamentals/ai-optimization-guide, riportata da SEJ: llms.txt ignorato, niente chunking, framework JS "più complessi", agenti che leggono DOM/albero di accessibilità).
- Mueller (agosto): gli update non partono prima dell'annuncio; gli annunci riguardano cambiamenti ampi, molti sistemi si aggiornano di continuo. Citazione storica: nessun sistema AI usa llms.txt.
- ChatGPT: più fan-out per prompt con GPT-5.6, molto uso di site: e "official", prima query già con brand non nominati dall'utente, indice interno OpenAI che serve anche siti senza accordi di licenza, tag di pipeline rimossi a fine luglio, quota Reddit nelle citazioni crollata (−86% in circa 3 settimane).
- Accesso/bot: Cloudflare dal 15/9 blocca di default i bot "misti" (compreso Googlebot) quando "block AI training" è attivo; traffico macchina > umano (maggio 2026 secondo Cloudflare); Meta e scanner mascherati da crawler pesano nei log.
- Discoverability: si sposta verso persone/creator e social (Discover mostra più post social; GSC ha aggiunto proprietà per piattaforme social/video); reach organico LinkedIn −47% dopo il nuovo ranking.

## (b) Tattiche pratiche ricorrenti con evidenza
1. Risposta diretta in alto + fatti (prezzi, orari, contatti, numeri) in HTML visibile, non in immagini o JS client-side. Fonti: Resoneo (indice ChatGPT = titolo + ~200 caratteri dall'inizio; H1 nell'83,6% degli snippet su 534 pagine), Suganthan, Lily Ray, guida Google (via Southern), Clarkson-Bennett. Evidenza: osservazionale, non causale.
2. Una sola pagina forte per intento, consolidare i duplicati: Suganthan (resa di citazione cala con 6+ pagine dello stesso dominio; un account), Ask an SEO sulla cannibalizzazione.
3. Coerenza di entità/NAP su tutte le proprietà (sito, GBP, social, directory, schede): Clarkson-Bennett, Southern (locale), YMYL-article, Forrester. Evidenza: ragionamento + correlazioni di vendor (Seer/Trustpilot).
4. Verificare blocchi CDN/WAF/robots per bot legittimi e rendering lato server per crawler che non eseguono JS (CCBot): Suganthan, news Cloudflare, Clarkson-Bennett.
5. Misurazione povera ma onesta: campo "come ci hai conosciuto?" (80–90% dei lead AI taggati organic/direct nei dati di un'agenzia), set fisso di prompt su più assistenti ripetuto (accordo sul brand top solo 41,6% tra 3 modelli), segmento AI in GA4, confronto CTR prima/dopo AIO in GSC.
6. Brand/menzioni esterne come leva principale per entrare nella "shortlist" dell'AI (Suganthan 68,9% vs 2,1%; Semrush ~90% delle pagine citate da ChatGPT in posizione 21+; Forrester; Hunt). Evidenza: un account, vendor.
7. Contenuti per decisioni e sotto-domande (fan-out) invece del solo volume: articolo "search volume screens out", Pollitt (difendere/adattare/abbandonare), Hunt.
8. Accessibilità/HTML semantico (pulsanti etichettati, form con label, link <a href>) per Googlebot e agenti: guida Google (via Southern), Clarkson-Bennett.

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt: smontato dall'esperimento cats.txt; nessun provider lo documenta; Ahrefs: 97% dei file senza richieste; Google lo ignora (guida ufficiale). Costo basso, nessuna evidenza di beneficio.
- ⚠ Structured data "per AI/GEO": Clarkson-Bennett ammette che per gli LLM è testo semplice, utile solo per ridurre l'ambiguità; Suganthan: schema non influisce sulla shortlist. Nessuna prova di vantaggio di citazione. Usarlo solo se coerente con il contenuto visibile.
- ⚠ Framework inventati senza validazione: "Click Worthiness" (Hunt), "Decision Distance" (Stoy), "6 segnali" (consulente), "site: come filtro anti-spam" (Ray, teoria dichiarata).
- ⚠ Percentuali da un solo account o un solo vendor: Suganthan (Dubai, personalizzazione), Whitespark (3 città USA), Uberall (un settore), Seer/Trustpilot (correlazione), DataDome (vendor di bot-protection), sondaggio Forrester (163 risposte autoselezionate), tool di AI visibility (varianza trattata come segnale). "GSC 75% incompleta" riportato senza metodo.
- ⚠ Ordine soggetto/oggetto delle entità per ottimizzare per l'AI: ipotesi dell'autore, il paper di Google non lo afferma.
- ⚠ "Official" nel title tag per ChatGPT: pratica vecchia con motivazione non provata.
- Cloudflare che "blocca già ora Googlebot": segnalazione Reddit non confermata; il cambio ufficiale è dal 15/9.
- Metriche tipo "86% dei clic discovery-led" (iPullRank, via un publisher) non trasferibili a siti piccoli. Contenuti "AI-written" e correzioni di dati (es. WSJ −85%→−43%) mostrano quanto i numeri circolanti siano instabili.

## (d) Implicazioni per la skill SEO
- Audit: (1) accesso reale dei bot: robots.txt + CDN/WAF + impostazione Cloudflare "AI training block" dopo il 15/9/2026; nei log diffidare di user agent falsi (CCBot) e verificare via reverse DNS; (2) rendering: per SPA Angular verificare che titolo, H1, testo principale, link <a href> e contatti siano nell'HTML iniziale (SSR/prerender): Google può eseguire JS ma è "più complesso" e molti crawler AI non lo eseguono; (3) HTML semantico e albero di accessibilità; (4) coerenza di date/NAP/nome tra sito, schema, GBP, social; (5) ricerca interna e homepage come landing per visitatori AI già convinti; (6) cannibalizzazione e consolidamento; (7) controllo spam policy (nessun contenuto scalato o AI non rivisto).
- Contenuti: risposta diretta in apertura, linguaggio delle domande reali (sotto-domande/fan-out ricavate dal parlato dei clienti), prove di esperienza (casi, dati propri, autore con credenziali), pagine di confronto e posizionamento esplicito, meno pagine ma migliori; il volume di ricerca non come unico filtro.
- Locale (libera professionista): orari/servizi/area di servizio in testo semplice e identici a GBP e directory; recensioni e profili esterni coerenti; verificare directory obsolete e pagine di terzi; controllo periodico delle risposte degli assistenti sulla propria attività (misure direzionali); GBP aggiornato; le attività locali risultano spesso servite dall'indice interno di ChatGPT (dati Resoneo, account free).
- Personal brand (sviluppatore): disambiguare il nome (Person schema con sameAs coerente come supporto, non come garanzia), presenza coerente su GitHub/LinkedIn/YouTube/blog; LinkedIn premia salvataggi e dwell time; "Official site" nel title solo se naturale; verificare cosa dicono gli assistenti della persona (query sul nome) e correggere le fonti; non dipendere da un solo canale.
- Visibilità su ChatGPT/Perplexity/AI Overviews: trattarla come lavoro di brand/PR e chiarezza della pagina, non come markup; includere nella skill una procedura manuale (5 prompt x assistenti x 5 ripetizioni, leggere quali brand inserisce il modello) e il campo "come ci hai conosciuto?"; non promettere punteggi; dichiarare variabilità e campioni piccoli; non raccomandare llms.txt come leva (al massimo opzionale, ricordando che Google lo ignora); avvertire che il report GSC generativo conta solo impression (no query) e che AIO/AI Mode sono nel tipo "Web" del rapporto Prestazioni.
- Da rivalidare sulla fonte primaria Google: guida AI optimization, doc Preferred Sources, doc del report generative AI, impostazione di esclusione generative AI, spam policy sulla manipolazione delle risposte AI.


=============== \S15 ===============
# Sintesi del periodo (24 ago – 15 set 2026)

## (a) Tendenze e novità
- Google (fonte ufficiale): Mueller ribadisce "nulla di speciale per le risposte generative" (GEO = SEO). Search Console: report AI (impression da AI Overviews, AI Mode, Discover) globale dal 31 agosto con opt-out; Mueller ammette che posizione e impression AI sono approssimative (blocco, non link; filtrato dentro il report Web).
- Policy: aggiornata la site reputation abuse (30 agosto): azioni manuali solo fuori SEE, separazione di sezioni nel SEE; quattro fattori (presentazione, qualità, paternità, duplicazione). Agosto: spam update con segnalazioni (aneddotiche) su contenuti AI in massa.
- Mueller: recupero dopo grandi update = mesi; vecchie pagine di basso valore (programmatic) possono pesare ancora; sitemap con parametri variabili = errore; il disavow agisce in mesi.
- Locale: view count dei post del Business Profile (rollout globale); nuove unità aggregator/supplier nel SEE per query commerciali, query locali forse prossime.
- ChatGPT: cambio di formato delle ricerche (pipe, finestra di freschezza, tipi `business`/`product`, widget senza citazioni); comportamento di Reddit dipendente dalla query.
- Misurazione: crescente scetticismo su punteggi aggregati di "AI visibility"; menzione ≠ citazione ≠ click; dati su calo dei click (Bocconi -9,4% query, AI Mode -18,8 punti di click, Wikipedia ~-5%) ma anche "si usano entrambi" (95% sovrapposizione Similarweb). Quote: ChatGPT ~53%, Gemini ~28%, Claude ~9%, Perplexity ~1% (visite, Similarweb maggio).
- Standard per agenti (WebMCP, MCP, UCP/ACP): sperimentali, senza dati di impatto.

## (b) Tattiche pratiche ricorrenti con evidenza
- Coerenza dei dati su tutte le superfici (sito, schema, GBP/feed, terze parti): schema 586785, entità 587886, claim audit 586904, locale 588095. Evidenza: soprattutto opinione e casi aneddotici; coerente con il principio Google di dati corretti e consistenti, non una prova causale.
- Pagina autore/"Chi sono" verificabile con Person, sameAs, credenziali reali, link a istituzioni: 583439, 586785, 587886, 587715. Evidenza: aneddotica; Google non lo promette per le AI.
- HTML renderizzato lato server/contenuto essenziale senza JS; i bot AI non eseguono script (CallRail, 588096; audit 586381: 1/4 contenuto lato server nel caso peggiore). Evidenza: dichiarazioni di vendor, plausibili, e allineate a quanto Google raccomanda per il rendering.
- Frase-risposta autosufficiente, citabile, con numeri/unità/date vicini: 586700, 588595, 586710 (estratti limitati). Evidenza: ipotesi plausibili, non dimostrate come fattori.
- Aggiornare pagine che rispondono a domande commerciali con date visibili (finestra ~30 giorni osservata in ChatGPT, 586710; ipotesi di un solo osservatore).
- Verificare che robots.txt/CDN/WAF non blocchino per errore i bot di ricerca AI (586381, 588095, 588605). Evidenza: audit di agenzia/vendor.
- Locale: NAP e orari identici ovunque, rispondere alle recensioni, percorso facile al profilo, niente recensioni "guidate", misurare chiamate e fonte dichiarata (588095, 588096). Evidenza: webinar sponsorizzati, linea con le linee guida Google sul ranking locale (citate).
- Audit del brand nei motori e negli assistenti AI con prompt ripetuti e condizioni registrate (587581, 587876, 586904); correggere le fonti sbagliate con contenuti "ponte". Evidenza: pratica, nessun dato.
- Evitare: sitemap con timestamp, disavow di massa, pagine programmatiche a combinazione, cambi di dominio senza necessità (588222, 588268, 588837, 588840).

## (c) Affermazioni discutibili / hype
- ⚠ llms.txt: nessun motore o assistente lo usa secondo più fonti (586737, 586381 come "Frontier", 585714 critica); markdown per i bot: Mueller vede solo tool SEO che lo richiedono (587671). Non raccomandarli come tattica di visibilità.
- ⚠ Schema per citazioni AI: Ahrefs non trova effetto significativo dall'aggiunta di JSON-LD (587888) mentre 586785 sostiene benefici con casi aneddotici; Google dice che non serve per le funzioni AI.
- ⚠ "Penalità per contenuti AI" nello spam update: solo segnalazioni social con campioni minimi; S-CTS non riguarda Search (587325).
- ⚠ Metriche vendor: punteggi di visibilità aggregati, crawl-to-refer (7 valori diversi, 588659), "AI CTR" e dati di LightSite/Moz/CallRail sono materiale di marketing o campioni opachi.
- Concetti nominati dagli autori (Authority Translation, Decision Coverage, Google Reset, entity drift, brand claim audit) sono framework personali, non terminologia Google.
- Studi accademici citati sono working paper non peer-reviewed e con campioni particolari (desktop USA, utenti Chrome giovani, un solo vertical).
- WebMCP e protocolli commerce: nessun dato di performance; da non trattare come urgenza per siti piccoli.

## (d) Implicazioni per la skill SEO
- Audit: includere (1) indicizzabilità/rendering senza JS (SSR/prerender per Angular, verifica HTML iniziale con user agent diversi, risposte 200 con guscio vuoto), (2) robots.txt/CDN/WAF e decisione esplicita sui bot AI, (3) sitemap stabile con lastmod corretto, (4) controllo pagine thin/programmatiche e storico di migrazioni, (5) controllo del report AI di Search Console con avvertenze di lettura, (6) coerenza entità/NAP/bio su tutte le superfici.
- Contenuti: paragrafi di risposta autosufficienti con fatti, date, numeri e unità; aggiornare pagine che influenzano decisioni; niente produzione di massa o pagine per ogni variante di query; contenuti di terzi integrati, firmati e con disclosure; nessuna versione markdown/llms.txt come tattica di ranking (al più da segnalare come non necessario).
- Locale: GBP completo e coerente con schema LocalBusiness (areaServed diverso da service area GBP), recensioni su più piattaforme senza richieste guidate, post con view count, tracciamento di chiamate e attribuzione auto-dichiarata; attenzione alle novità SEE su query di servizi locali (monitorare, non agire).
- Personal brand: pagina "Chi sono" con Person + sameAs, credenziali spiegate con istituzioni collegate (importante per titoli italiani), entity map, audit periodico di come Google e gli assistenti descrivono il nome, gestione omonimi e varianti, protezione di domini/handle/namespace dei pacchetti, "bridge content" per ruoli o titoli cambiati.
- Visibilità su ChatGPT/Perplexity/AI Overviews: trattare come estensione della SEO; misurare menzione, citazione, click e conversione separatamente; usare molti prompt ripetuti e solo come tendenza; verificare i referrer AI nelle proprie analytics prima di decidere quali motori monitorare; non promettere risultati su singole citazioni (Reddit e widget cambiano rapidamente).
- Marcare nella skill le affermazioni come "opinione/vendor" quando non provengono da documentazione Google.


=============== \S16 ===============
# Sintesi del periodo

Periodo: 15 settembre - 2 ottobre 2026. 52 articoli letti per intero. Molti sono opinioni o agentic/ecommerce non pertinenti; le fonti di maggior valore per la skill sono le news su documentazione Google e le dichiarazioni di Mueller.

## (a) Tendenze e novità del periodo
- Documentazione Google (fatti): (1) 1 ottobre, guida sui contenuti generativi: fact-check manuale obbligatorio di testo e metadata; (2) 1 ottobre, guida people-first: avviso su autori/credenziali falsi; (3) 18 settembre, aggregator e supplier unit SEE ora includono query local business; (4) Search Console: filtro "multimodal" (ricerche con immagine) e report AI generativo (dal 31 agosto) senza click per link né query; (5) spam update di settembre iniziato il 24 (4 del 2026, fino a due settimane) e paper su SAFE (rilevatore di AI slop/abuso coordinato); (6) guida per il badge dei Search profiles (soglia 10.000 follower, solo USA); (7) test Google di pagamenti ai publisher per contributo alle risposte AI.
- Dichiarazioni Mueller: la posizione negli AI Overview è "difficile da rendere utile" (il blocco è appiattito: tutti i link ereditano la posizione del blocco); risposta sul de-indexing dovuto a pagina di errore JS indicizzata come canonical; consiglia test automatici pre-deploy e monitoraggio; vede UTM aggiunti da Gemini e chiede casi sul referrer perso.
- Traffico e misurazione: Chartbeat (rete publisher): Google Search -40,2% a/a; studio UPenn/Northeastern (1.100 tracciati): con AI Mode forzato -18,8 punti percentuali di clic verso altri siti; AWR: CTR con AI Overview 10% vs 29% senza (desktop pos. 1-2, USA). Errore di logging impression in GSC fino al 27 aprile 2026: discontinuità nei confronti storici. GA4 ha un canale "AI Assistant" dal 13 maggio (copertura incompleta, senza backfill).
- Cloudflare: nuovo "Disallow AI Training" (robots.txt senza bloccare i motori), Bot Preference Sync con default per nuovi domini dal 15 settembre; rischio di blocchi involontari (anche Googlebot, segnalato in un articolo collegato non letto qui).
- Agentic web: Muse (Meta), dots (OpenAI), Shopify auto-enroll, x402/pay-per-crawl, WebMCP: molto rumore, pochissima evidenza di uso reale; nessuna azione consigliata per siti non ecommerce.

## (b) Tattiche pratiche ricorrenti con evidenza a supporto
- Accessibilità tecnica per crawler e agenti: robots.txt/noindex/WAF/CDN verificati; contenuto importante nell'HTML (SSR/prerender) per i sistemi AI che non eseguono JS (opinione di praticanti: Jeffery/Shaw/Manic; Google esegue JS). Evidenza: caso reale di pagina di errore JS indicizzata (Mueller) e dati WebAIM (95,9% di home con errori WCAG; input senza label 51%).
- HTML semantico e form con conferma leggibile da macchine; elementi nativi, label, nomi ai bottoni (WebAIM + studio CHI 2026 sul calo di successo degli agenti con interazioni non standard).
- Coerenza dei dati dell'attività: telefono/indirizzo/servizi uguali su pagina, schema e Business Profile; eliminare pagine duplicate/obsolete ("old", "v2") (Shaw, Jeffery, Pollitt). Il valore dello schema per ranking/AI resta non provato (Shaw, Ahrefs citato); il rischio concreto è lo schema non mantenuto o incoerente col contenuto visibile (azione manuale nella doc Google).
- Contenuti: partire da obiettivi di business e domande reali dei clienti (fan-out, recensioni dei concorrenti, domande ricorrenti); rispondere subito in 2-3 frasi e poi approfondire; nominare il brand/entità nei passaggi chiave; scrivere in testo prove e numeri (recensioni, premi) invece di widget JS; fact-check e autori reali (doc Google, 1 ottobre). Evidenza: opinioni di consulenti; nessuno studio controllato nel periodo.
- Misurazione: guardare esiti (richieste, conversioni), ricerche di brand, diretto, ritorno; non la "posizione" negli AI Overview; ripetere i campionamenti AI (variabilità elevata, Pedro Dias); controllare i log per i bot AI; segmentare utm_source dei chatbot; test di retrieval con frase esatta in ChatGPT (Chris Green) per verificare che la pagina sia raggiungibile.
- Audit deterministico: confronto HTML grezzo vs DOM renderizzato (link, canonical, redirect) con codice, non con LLM (Chris Green).
- Notorietà fuori dal sito (opinione + dati di terzi): podcast/interviste trasformate in trascrizione, clip e backlink; menzioni su YouTube/Reddit/Wikipedia correlate con AI visibility (Ahrefs, Muck Rack; metodologie non verificate).

## (c) Affermazioni discutibili / hype
- ⚠ "GEO" come disciplina distinta: nel sondaggio SEJ 43% pianifica GEO contro 14% che dice che funziona; solo 9% si fida della misura; la guida Google sull'AI (citata in 588593 e 590088) dice che le feature generative poggiano sui fondamentali del ranking.
- ⚠ Schema per AI visibility: nessuna evidenza di effetto su ranking/citazioni (Shaw cita test di Hundley senza effetti; Ahrefs: schema non ha spostato le citazioni); gli articoli pro-schema (Pollitt, Baker) sono ragionamenti, non dati.
- ⚠ Markdown/"text-only" per AI: Jeffery non ha trovato motori AI che li usino; Manic dice che tolgono le azioni. llms.txt non discusso nel periodo.
- ⚠ Attribuzione di cause a singole variabili (cannibalizzazione, disavow, "autorità") senza esperimento (Montti, Dias). Studio MemToC su modelli 7-9B non trasferibile a ChatGPT/AIO.
- ⚠ "Google mente su AI Mode" (Montti) e "AI Mode toglie l'attribuzione per design" (claim di vendor mai riverificato dopo il fix). Previsioni McKinsey/Gartner sul commercio agentico trattate con scetticismo da Manic.
- ⚠ Dati con conflitto d'interesse: Duane Forrester (vende CitationIQ/piattaforma di misura), Chartbeat (vende analytics), Menlo (investitore Anthropic), EC Innovations (localizzazione); AWR calcolato su dati GSC attraversati dall'errore di logging.
- ⚠ Fonti opache: la pagina "State of Search" è promozionale; Ahrefs -58% clic con AIO senza metodologia nell'articolo.

## (d) Implicazioni per la skill SEO
- Audit tecnico: aggiungere controlli su (1) robots.txt vs regole del CDN (Cloudflare Bot Preference Sync/AI bot policy); (2) HTML grezzo vs renderizzato per SPA Angular (SSR/prerendering, contenuto e link critici nell'HTML iniziale; pagine di errore/app shell non devono restituire 200 indicizzabile: vero 404/soft-404, test pre-deploy e monitoraggio periodico delle pagine critiche, consiglio di Mueller); (3) noindex dimenticati, URL di vecchie versioni, sitemap; (4) HTML semantico/form accessibili (label, bottoni, conferma di invio); (5) coerenza schema-pagina-profili; (6) lingua: URL distinte per lingua con contenuto realmente tradotto e lang corretto, hreflang solo quando serve (doc Google).
- Contenuti: checklist di fact-check manuale di testo e metadata se si usa AI e divieto di autori/credenziali fittizi (doc Google 1 ottobre); niente produzione di massa (spam update/SAFE); scrivere per domande reali del cliente; prove in testo.
- Locale (orientatrice): coerenza NAP con Business Profile; pagine servizio per bisogno; recensioni e prove scritte in testo; novità/eventi in HTML crawlabile; attenzione ai nuovi aggregator/supplier unit SEE per le query locali e a tracking GSC potenzialmente diverso; nessuna Indexing API (solo job posting/livestream).
- Personal brand (sviluppatore): pagina autore reale con Person schema e @id, link coerenti a profili esterni, byline vero, portfolio con casi e dati verificabili; menzioni/interviste/talk trasformati in asset indicizzabili; costruire ricerche di brand e audience diretta (newsletter) perché il traffico Google su contenuti generici cala; Search profiles solo USA e con soglia follower.
- Visibilità su ChatGPT/Perplexity/AI Overviews: test di retrieval a frase esatta, monitoraggio di referral AI con UTM/canale GA4, log dei bot; non promettere citazioni; non bloccare i crawler per default su siti piccoli, ma sapere che robots.txt vale solo per bot educati; gli AI Overviews si controllano solo con nosnippet/data-nosnippet/max-snippet/noindex (doc Google), Google-Extended non influisce su ricerca/AIO.
- Reportistica: usare esiti e brand search; segnare il 27 aprile 2026 come discontinuità GSC; la "posizione" AIO in GSC è appiattita.
- Da non includere come raccomandazioni: x402/pay-per-crawl, WebMCP, markdown mirror, commercio agentico, Baidu/ICP.
