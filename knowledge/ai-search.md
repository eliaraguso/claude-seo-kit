# Ricerca AI: AI Overviews, AI Mode e assistenti di terzi

> Aggiornato al 2026-10-03. Fonte primaria: Google. Secondaria: SEJ (ott 2025–ott 2026).
> Legenda: **[G](url)** = documentazione o blog ufficiale Google · **[D]** = deduzione di questo file, non scritta da nessuna fonte · **[SEJ AAAA-MM, autore, tipo, campione]** = fonte terza riportata da Search Engine Journal · ⚠ = va oltre o contro quanto dice Google.
> Forza dell'evidenza per le fonti terze: **Forte** (dichiarazione o documentazione ufficiale del fornitore) · **Media** (studio ampio con metodo dichiarato, ma correlazionale) · **Debole** (campione piccolo, un solo account, dati di un vendor) · **Opinione**.
> Misurazione (Search Console, GA4, Bing, prompt tracking): vedi `measurement.md`. Miti e consigli obsoleti: vedi `myths-deprecated.md`.

## Indice
- [Fatti e regole (Google)](#fatti-e-regole-google)
  - [Come funzionano AI Overviews e AI Mode](#come-funzionano-ai-overviews-e-ai-mode)
  - [Requisiti per comparire](#requisiti-per-comparire)
  - [Controlli: accesso, anteprime, esclusione](#controlli-accesso-anteprime-esclusione)
  - [Cosa Google dice di NON fare](#cosa-google-dice-di-non-fare)
  - [Contenuti: cosa Google raccomanda](#contenuti-cosa-google-raccomanda)
  - [Spam e manipolazione delle risposte AI](#spam-e-manipolazione-delle-risposte-ai)
  - [Agenti e fetcher di Google](#agenti-e-fetcher-di-google)
- [Controlli / procedure](#controlli--procedure)
- [Cosa dicono le fonti terze](#cosa-dicono-le-fonti-terze)
  - [Da dove attingono gli assistenti](#da-dove-attingono-gli-assistenti)
  - [Bot AI e robots.txt](#bot-ai-e-robotstxt)
  - [Cosa correla con le citazioni](#cosa-correla-con-le-citazioni)
  - [Struttura di contenuto citabile](#struttura-di-contenuto-citabile)
  - [JavaScript e bot AI](#javascript-e-bot-ai)
  - [Traffico reale dai chatbot](#traffico-reale-dai-chatbot)
  - [Hype da non seguire](#hype-da-non-seguire)
- [Note per tipo di sito](#note-per-tipo-di-sito)

---

## Fatti e regole (Google)

### Come funzionano AI Overviews e AI Mode
- Le funzionalità di AI generativa della Ricerca (AI Overviews, AI Mode) poggiano sugli stessi sistemi di ranking e qualità della Ricerca: per Google **la SEO resta pertinente**. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Due tecniche dichiarate: **RAG / grounding** (i sistemi di ranking recuperano pagine pertinenti e aggiornate dall'indice; la risposta mostra link cliccabili a supporto) e **query fan-out** (il modello genera in parallelo più query correlate per raccogliere altri risultati; es. "prato pieno di erbacce" → "migliori erbicidi", "rimuovere erbacce senza chimica", "prevenire le erbacce"). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Il fan-out lavora su più sottoargomenti e più origini dati; per questo le risposte AI mostrano un insieme di link **più ampio e vario** di una ricerca classica. [G](https://developers.google.com/search/docs/appearance/ai-features)
- AI Overviews compaiono solo quando aggiungono valore rispetto alla ricerca classica, quindi **spesso non si attivano**; AI Mode serve soprattutto a query che chiedono analisi, ragionamento, confronti complessi. I due prodotti possono usare modelli e tecniche diverse: risposte e link possono differire. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Le risposte possono includere immagini, video, schede prodotto e informazioni sulle attività locali; per queste ultime contano **Merchant Center** e **Profilo dell'attività su Google**. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- "AEO" e "GEO": per Google ottimizzare per la ricerca con AI generativa **è sempre SEO**; chi valuta consulenze AEO/GEO deve confrontarle con le indicazioni ufficiali. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- Badge "fonte preferita" possibile anche in AI Mode/AI Overviews, solo per siti a livello di dominio o sottodominio e inclusi nelle funzionalità di AI generativa in Search Console; utile soprattutto a chi pubblica notizie. [G](https://developers.google.com/search/docs/appearance/preferred-sources)
- I sistemi di ranking includono il **ranking dei passaggi** (valutazione di singole sezioni di una pagina). [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide)

### Requisiti per comparire
- Per essere link di supporto in AI Overviews o AI Mode una pagina deve essere **indicizzata, idonea a comparire con uno snippet** e rispettare i requisiti tecnici della Ricerca (Googlebot non bloccato, HTTP 200, contenuto indicizzabile). **Nessun requisito tecnico aggiuntivo.** Nessuna garanzia di scansione, indicizzazione o pubblicazione. [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/docs/essentials/technical)
- Inoltre il sito deve risultare **incluso nelle funzionalità di AI generativa della Ricerca** tramite l'impostazione di Search Console. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) ([guida all'impostazione](https://support.google.com/webmasters/answer/16908024))
- Best practice elencate da Google (nessuna è "speciale" per l'AI): scansione consentita in robots.txt **e** da hosting/CDN; contenuti raggiungibili con link interni; buona esperienza sulla pagina; **contenuti importanti in forma di testo**; immagini e video di qualità a supporto; dati strutturati coerenti con il testo visibile; Merchant Center e Profilo dell'attività aggiornati. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Aspetti tecnici citati nella guida 2026: HTML semantico utile (screen reader) ma "la leggibilità per le persone conta più di un codice perfetto"; Google elabora JavaScript se non bloccato, ma la SEO dei framework JS è "generalmente più complessa"; ridurre i duplicati; crawl budget rilevante solo per siti molto grandi; verificare il sito in Search Console. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### Controlli: accesso, anteprime, esclusione
- L'AI fa parte della Ricerca: l'accesso si governa con **robots.txt per Googlebot**. Non esiste un bot separato per AI Overviews/AI Mode. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Per limitare cosa viene mostrato (anche nell'AI): `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`. Questi controlli riducono anche gli snippet classici. [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search)
- Se un controllo di anteprima "non funziona": verificare con **Controllo URL** che sia nell'HTML visto da Googlebot; la ri-scansione richiede da giorni a mesi; si può chiederla. [G](https://developers.google.com/search/docs/appearance/ai-features)
- **Google-Extended** è un token di robots.txt (nessun user agent proprio) che limita l'uso dei contenuti per l'addestramento di Gemini e per il grounding nelle app Gemini/Vertex AI; **non influisce sull'inclusione nella Ricerca né sul ranking**, quindi non toglie dagli AI Overviews. [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- Impostazione di esclusione "AI generativa della Ricerca" in Search Console: toglie il sito da AI Overviews, AI Mode e funzioni AI di Discover (anche come link); Google dichiara che non è un segnale di ranking per il resto della Ricerca; prima in test su un sottoinsieme (dal 17/6/2026, spinta dal regolatore britannico CMA), disponibile ovunque dal 31/8/2026. [SEJ 2026-07/08/09, news su help Google, Forte] — l'esistenza del controllo è confermata dalla guida Google sopra.
- Scelta di robots.txt per i crawler AI di addestramento: Google mostra come esempio un gruppo che blocca un bot di training lasciando passare i motori di ricerca. È una scelta editoriale del proprietario. [G](https://developers.google.com/search/blog/2025/03/robotstxt-flexible-way-to-control)

### Cosa Google dice di NON fare
Dalla sezione "miti" della guida ufficiale (15/5/2026) e dalla pagina sulle funzionalità AI. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- **llms.txt e altri file/markup/Markdown "per l'AI"**: la Ricerca Google non li usa; non aiutano né danneggiano; si possono creare per altri servizi. Non servono nuovi file leggibili dalle macchine, file di testo o "markup AI".
- **Spezzare i contenuti in blocchi (chunking)**: non necessario; Google capisce più argomenti in una pagina e mostra la parte pertinente. **Non esiste una lunghezza ideale** di pagina.
- **Riscrivere i testi solo per l'AI** o inseguire ogni variante long-tail: non necessario, i sistemi capiscono sinonimi e significati.
- **Cercare menzioni non autentiche**: meno utile di quanto sembri; i sistemi principali premiano la qualità e altri sistemi bloccano lo spam.
- **Dati strutturati "per l'AI"**: non necessari per le funzioni generative, nessun markup schema.org speciale; restano utili per i risultati avanzati.
- **Pagine separate per ogni variante di query o query di fan-out** create principalmente per manipolare ranking o risposte AI: violano la norma sull'**abuso di contenuti su larga scala**, e comunque molte pagine non rendono un sito migliore.
- **Fidarsi di strumenti che dichiarano metriche "interne" di Google**: nessuno strumento terzo ha accesso ai sistemi di ranking o AI di Google. [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)

### Contenuti: cosa Google raccomanda
- I contenuti unici, utili e interessanti sono, secondo Google, il fattore che più probabilmente inciderà nel lungo periodo sulla presenza nella ricerca generativa. Caratteristiche: punto di vista unico (es. recensione di prima mano invece di riassunto), contenuto **non generico** basato su esperienza diretta ("Perché abbiamo rinunciato all'ispezione…" invece di "7 consigli per…"), organizzazione in paragrafi e sezioni con intestazioni, immagini e video pertinenti. Domanda guida: "i miei visitatori lo troverebbero soddisfacente?". [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Chi fa domande all'AI usa query più lunghe e specifiche e fa follow-up; valgono gli stessi fondamentali (contenuti people-first, esperienza sulla pagina, accessibilità tecnica, dati strutturati coerenti, contenuti multimodali). [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search)
- Contenuti creati con AI generativa: utili per ricerca e struttura; generare molte pagine senza valore può violare l'abuso di contenuti su larga scala; curare accuratezza anche di `<title>`, meta description, dati strutturati, alt text; spiegare ai lettori come sono stati creati quando se lo aspettano; ecommerce: immagini AI con IPTC `DigitalSourceType = TrainedAlgorithmicMedia`. [G](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- ⚠ SEJ riporta un aggiornamento del 1/10/2026 della stessa guida con **fact-check manuale obbligatorio** di testo e metadati e un avviso su autori/credenziali falsi nella guida people-first [SEJ 2026-10, news su doc Google]: la versione italiana scaricata il 3/10/2026 non lo contiene ancora. Verificare la versione inglese prima di citarlo.
- Google dichiara che i clic da pagine con AI Overviews sono "di qualità superiore" (più tempo sul sito) e invita a misurare conversioni, non solo clic. È un'affermazione di Google, senza dati pubblici. [G](https://developers.google.com/search/docs/appearance/ai-features)

### Spam e manipolazione delle risposte AI
- Le norme antispam definiscono spam anche le tecniche per **manipolare le risposte dell'AI generativa** nella Ricerca. [G](https://developers.google.com/search/docs/essentials/spam-policies) SEJ data il chiarimento al 15/5/2026 con esempi come comprare o alterare citazioni. [SEJ 2026-06/08, news, Forte]
- Abuso di contenuti su larga scala "indipendentemente da come sono creati" (AI, persone, mix); l'AI in sé non è spam. [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)
- Altre norme rilevanti per tattiche "GEO": testo nascosto, cloaking, link di spam, recensioni false/incentivate non dichiarate (linee guida review snippet, possibile azione manuale). [G](https://developers.google.com/search/docs/essentials/spam-policies)
- Fuori da Google: le linee guida Bing (riscritte inizio 2026) hanno una sezione "Prompt Injection and AI Manipulation" e una su linguaggio artificiosamente ingegnerizzato. [SEJ 2026-02, news su doc Microsoft, Forte] Microsoft Defender ha documentato 31 aziende con pulsanti "Riassumi con AI" che iniettano istruzioni nascoste ("AI Recommendation Poisoning"). [SEJ 2026-02, ricerca Microsoft, 60 giorni di URL] → tattica da segnalare come rischiosa.

### Agenti e fetcher di Google
- Gli agenti AI (es. agenti del browser) possono leggere screenshot, DOM e **albero di accessibilità**; Google rimanda alla guida web.dev sui siti adatti agli agenti e cita il protocollo emergente UCP. Sezione facoltativa: "se è pertinente e hai tempo". [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- `Google-Agent` (marzo 2026) e `Google-GeminiNotebook` (ex `Google-NotebookLM`) sono **fetcher attivati dall'utente**: in genere **ignorano robots.txt**; IP pubblicati in `user-triggered-agents.json` / `user-triggered-fetchers*.json`; Web Bot Auth sperimentale. [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) · [G](https://developers.google.com/crawling/docs/changelog)
- Per bloccare davvero un'area serve autenticazione, non robots.txt. [D]

---

## Controlli / procedure

| ID | Cosa | Come (strumento, passi) | Priorità | Fonte |
|---|---|---|---|---|
| AI-01 | Pagine chiave indicizzate e idonee allo snippet | Controllo URL su home e pagine di servizio/progetto; cercare `noindex`, `nosnippet`, `max-snippet` basso, `data-nosnippet` su blocchi importanti, anche nell'header `X-Robots-Tag` | Alta | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| AI-02 | Googlebot non bloccato da robots.txt, CDN o WAF | Test URL live (screenshot renderizzato: pagina vuota o "sei umano?" = problema); log per IP Google; blocchi temporanei solo con 503/429 | Alta | [G](https://developers.google.com/search/blog/2024/12/crawling-december-cdns) |
| AI-03 | Impostazione "AI generativa della Ricerca" non disattivata per errore | Search Console → Impostazioni; se l'esclusione è attiva, chiedere al proprietario se è voluta; prima di attivarla, salvare una baseline del report AI | Alta | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [SEJ 2026-08, Shehata, opinione] |
| AI-04 | Contenuto importante in testo HTML | Prezzi, servizi, orari, credenziali, contatti, risposte: in testo, non solo in immagini, canvas, PDF, video o widget | Alta | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| AI-05 | HTML iniziale vs renderizzato | `curl -A` / view-source vs Controllo URL; se il testo chiave c'è solo dopo JS: per Google basta che il rendering funzioni, ma "non tutti i bot eseguono JS" → SSR/prerender per le pagine di contenuto. Mai una versione diversa solo per i bot | Alta (SPA) | [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [SEJ 2025-12, Vercel/Gabe, test] |
| AI-06 | Controlli di anteprima come scelta consapevole | Se si vuole uscire dall'AI senza perdere gli snippet classici: valutare l'impostazione di esclusione in Search Console invece di `nosnippet` | Media | [G](https://developers.google.com/search/docs/appearance/ai-features), [SEJ 2026-07, news] |
| AI-07 | Google-Extended capito correttamente | Spiegare che bloccarlo non toglie da AI Overviews/AI Mode né incide sul ranking; serve solo per training/grounding Gemini | Bassa | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| AI-08 | Politica sui bot AI di terzi esplicita | Classificare i bot in training / indicizzazione per ricerca / fetch per utente; chiedere al proprietario se vuole essere citato; scrivere robots.txt di conseguenza; ricordare che i fetch per utente possono ignorarlo | Alta se si vuole visibilità AI | [SEJ 2026-07, Pollitt, opinione-guida] |
| AI-09 | CDN che blocca bot per impostazione predefinita | Controllare regole Cloudflare (blocco crawler AI predefinito da luglio 2025; impostazioni "AI training" / Bot Preference Sync dal 15/9/2026) e verificare che Googlebot e Bingbot passino | Alta | [SEJ 2025-12 e 2026-08/09, news, Forte su Cloudflare] ⚠ effetti su Googlebot da verificare |
| AI-10 | Log: bot veri o falsi | Verificare IP contro gli elenchi pubblicati (Google `common-crawlers.json`, OpenAI, Anthropic, Perplexity, Common Crawl) e reverse DNS; stati: verificato / falso / non verificabile | Media | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests), [SEJ 2026-06, Forrester, 1 sito 14 giorni] |
| AI-11 | Contenuti non "commodity" | Per ogni pagina chiave: cosa offre che non si trova altrove (casi, dati propri, esperienza)? Applicare le domande di autovalutazione Google | Alta | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| AI-12 | Nessuna pagina per variante o fan-out | Cercare pagine quasi identiche per città/varianti/domande; consolidare con 301; una pagina forte per intento | Alta | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| AI-13 | Dati strutturati solo se coerenti con il visibile | Validare (Test risultati avanzati / validator.schema.org); niente "schema per l'AI"; niente `AggregateRating` su recensioni auto-pubblicate | Media | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| AI-14 | Profilo dell'attività e Merchant Center aggiornati | Orari, servizi, area, foto, categoria; feed prodotti se ecommerce | Alta (locale, ecommerce) | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| AI-15 | Coerenza di identità su tutto il web | Nome, bio, NAP, servizi uguali su sito, schema, Business Profile, social, directory; correggere fonti obsolete | Media | [G](https://developers.google.com/search/docs/appearance/establish-business-details), [SEJ 2026-07/09, più autori, opinione+vendor] |
| AI-16 | Niente tattiche speculative come leva | llms.txt, mirror Markdown, chunking, "AI schema": non proporli; se presenti non sono un errore (Google li ignora) | Bassa | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| AI-17 | Nessuna manipolazione | Cercare testo nascosto con istruzioni per LLM, pulsanti "Riassumi con AI" con prompt precaricati, recensioni/menzioni comprate, listicle auto-promozionali | Alta | [G](https://developers.google.com/search/docs/essentials/spam-policies), [SEJ 2026-02, Microsoft] |
| AI-18 | Pronto per gli agenti (facoltativo) | Link `<a href>` reali, pulsanti nativi con nome, form con `label`, nessun CAPTCHA/modale che blocca il flusso di contatto, layout stabile; non bloccare gli IP di Google-Agent | Bassa-Media | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [SEJ 2026-05, Manic, opinione] |
| AI-19 | Bing indicizza il sito | Verificare in Bing Webmaster Tools, inviare sitemap, valutare IndexNow (Bing alimenta Copilot e, secondo terzi, altri assistenti) | Media | [SEJ 2026-03/05, news Microsoft + opinioni] |
| AI-20 | Accuratezza di cosa dicono le AI su di te | Prompt di fatti (chi è, cosa offre, dove, prezzi) su più assistenti; correggere le fonti sbagliate; procedura in `measurement.md` | Media | [SEJ 2026-07/09, Manic, Forrester, opinione] |

---

## Cosa dicono le fonti terze

### Da dove attingono gli assistenti
Nessun fornitore terzo pubblica i propri fattori di selezione delle fonti. Quanto segue sono dichiarazioni dei fornitori (Forte) o ricostruzioni di terzi (Debole/Media).

| Assistente | Fonte dei risultati (secondo chi) | Evidenza |
|---|---|---|
| AI Overviews / AI Mode | Indice e sistemi di ranking di Google | Fatto Google [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| Gemini (app) | Infrastruttura Google; Google-Extended controlla training e grounding nelle app Gemini | Fatto Google [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| ChatGPT | Bot propri (OAI-SearchBot per l'indice di ricerca); indice interno "labrador" che serve anche siti senza licenza, locali e prodotti quasi sempre da lì negli account free; in modalità "thinking" ~75% da risultati Google raccolti con scraper; storicamente anche Bing | [SEJ 2026-08, Resoneo/Mohanadasan, 1.249 risposte, Debole-Media] [SEJ 2026-07, singolo ricercatore, Debole] [SEJ 2026-02, Lily Ray, 11 sottocartelle, Debole] ⚠ ricostruzioni in conflitto |
| Perplexity | Recupera quasi sempre; pipeline propria (ipotesi Brave); per query locali pesa l'indice mappe/Business Profile | [SEJ 2026-02/06/08, opinioni + studio con n minimo, Debole] |
| Claude | Brave Search secondo alcuni autori | [SEJ 2026-01/05, opinione, Debole] — da verificare |
| Copilot / Bing | Indice Bing; API di grounding Web IQ che restituisce passaggi, usata da Copilot e (dichiarazione Microsoft) da ChatGPT | [SEJ 2026-07, news Microsoft, Forte per Copilot] |
| Siri (Apple) | Applebot; `Applebot-Extended` per il training; `nosnippet` impedisce l'uso della pagina come contesto per risposte AI | [SEJ 2026-06, doc Apple, Forte] |

- Le fonti citate cambiano molto tra motori: AI Mode e AI Overviews concordano nell'86% delle risposte ma citano gli stessi URL solo nel 13,7% [SEJ 2025-12, Ahrefs, 730.000 coppie di query, Media]; solo il 2,37% degli URL citati compare in ChatGPT, Perplexity e AI Overviews per lo stesso prompt [SEJ 2026-05, Indig/Omnia, 20.000 prompt, Media].
- AI Overviews citano sempre meno la top 10 organica: 38% delle pagine citate (era ~75% a fine 2024) [SEJ 2026-05, Ahrefs, 4 mln URL, Media]; ~17% per BrightEdge [vendor, Debole]. ~90% delle pagine citate da ChatGPT sta oltre la posizione 20 per query correlate [SEJ 2026-08, Semrush citato, Debole].
- Ma un calo organico su Google si riflette sulle citazioni: -27,8% ChatGPT, -23,8% AI Mode, -2,9% Perplexity [SEJ 2026-02, Lily Ray, 11 sottocartelle scelte, Debole]. Lettura prudente [D]: la SEO classica è condizione utile ma non sufficiente; ogni motore va misurato a parte.

### Bot AI e robots.txt

| User agent | Operatore | Scopo | Rispetta robots.txt | Fonte |
|---|---|---|---|---|
| Googlebot | Google | Ricerca, incluse AI Overviews/AI Mode | Sì | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| Google-Extended | Google | Token (non crawler): training/grounding Gemini | Token di robots.txt | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| Google-Agent, Google-GeminiNotebook | Google | Fetch su richiesta dell'utente | In genere no | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers) |
| GPTBot | OpenAI | Training | Sì (dichiarato) | [SEJ 2025-11/2026-01, lista da log + doc OpenAI] |
| OAI-SearchBot | OpenAI | Indice di ChatGPT search; bloccarlo riduce la presenza nelle risposte | Sì | [SEJ 2026-01, doc OpenAI citata, Forte] |
| ChatGPT-User | OpenAI | Fetch su richiesta dell'utente | Non più garantito (doc OpenAI aggiornata) | [SEJ 2026-07, Pollitt, Forte] |
| ClaudeBot / Claude-SearchBot / Claude-User | Anthropic | Training / ricerca / fetch utente | Dichiarato per i primi due | [SEJ 2025-11, 2026-05] |
| PerplexityBot / Perplexity-User | Perplexity | Indice / fetch utente (quest'ultimo non garantisce robots.txt) | Sì / non garantito | [SEJ 2026-07] |
| Bingbot | Microsoft | Indice Bing, alimenta Copilot | Sì | [SEJ 2025-11] |
| Applebot / Applebot-Extended | Apple | Spotlight/Siri/Safari / opt-out training | Sì; se manca un gruppo Applebot segue le regole di Googlebot | [SEJ 2026-06, doc Apple] |
| CCBot | Common Crawl | Archivio usato per addestrare molti modelli; bloccarlo ferma la raccolta futura, non toglie l'archivio | Sì; nome spesso falsificato | [SEJ 2026-06/08] |

- Volumi: crawl AI ~89% training, 8% ricerca, 2% fetch utente [SEJ 2026-05, Cloudflare Radar Q1 2026, Forte sul dato Cloudflare]; altra misura: 57% fetch utente (quasi tutto ChatGPT) [SEJ 2026-05, Duda, 68,9 mln visite, una piattaforma]. Rapporti scansioni/visite inviate molto sbilanciati per Anthropic e OpenAI rispetto a Google (ClaudeBot da ~20.600:1 a ~70.900:1 secondo il periodo) [SEJ 2025-12/2026-05/07, Cloudflare, cifre diverse per periodo].
- Bloccare i bot di training è una scelta; bloccare quelli di ricerca e di fetch utente riduce la presenza nelle risposte [SEJ 2025-12/2026-06, opinione convergente]. I nomi dei bot vanno verificati: in un sito nuovo l'81,8% dei "live fetch" AI e l'87% dei "Googlebot" erano falsi [SEJ 2026-06, Forrester, 1 sito, 14 giorni, Debole].
- Esempio di robots.txt per chi vuole essere citato ma non addestrare i modelli [D, da adattare con il proprietario]:
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
  Nota: Google non supporta `crawl-delay` né campi diversi da user-agent/allow/disallow/sitemap. [G](https://developers.google.com/search/blog/2025/03/robots-future)

### Cosa correla con le citazioni
Tutte correlazioni o osservazioni; nessuno studio controllato mostra cause, tranne il test (negativo) sullo schema.

| Fattore | Cosa emerge | Evidenza | Rapporto con Google |
|---|---|---|---|
| Menzioni del brand sul web | Correlazione più alta (~0,67) con la frequenza nelle AI Overviews | [SEJ 2025-11, Ahrefs, vendor, campione non dettagliato] Media-Debole | Google: menzioni **autentiche** sì (Stein: l'AI col fan-out cerca liste e articoli che citano le attività [SEJ 2025-11, dichiarazione Google]); menzioni non autentiche poco utili e manipolazione = spam |
| Earned media / fonti terze | ~84% dei link citati dagli LLM sono menzioni guadagnate; 77% delle citazioni su query di brand viene da fuori sito | [SEJ 2026-07, Muck Rack 25 mln link; Omniscient] Debole (vendor; un altro articolo riporta per Muck Rack "25% delle citazioni" [SEJ 2026-05]: cifre incoerenti) | Coerente con "contenuti di qualità + segnali di spam" |
| Brand già "noto" al modello | Brand inseriti dal modello nella propria query compaiono nel 68,9% delle risposte, quelli solo recuperati nel 2,1% | [SEJ 2026-08, Mohanadasan, 1 account, 57 conversazioni, "solo direzionale"] Debole | Nessuna posizione Google |
| Esperienza diretta / dati propri | Ricerche first-party ~3,3x citazioni; siti con contenuti AI in serie: 54% ha perso ≥30% | [SEJ 2026-07, Indig] [SEJ 2026-05, Lily Ray, 220+ siti, osservazionale] Media-Debole | Allineato alla guida Google (contenuti non generici) |
| Apertura dichiarativa, date e numeri nell'intro | "X è Y" in apertura +14%; DATE e NUMBER positivi; prezzo in apertura negativo | [SEJ 2026-03, Indig, ~98.000 citazioni ChatGPT, 7 verticali B2B] Media, solo ChatGPT | Google: scrivere per le persone, nessuna regola di formato |
| Posizione nel testo | 44% delle citazioni dal primo 30% del testo | [SEJ 2026-02, Indig, 18.012 citazioni ChatGPT] Media, solo ChatGPT | Nessuna posizione Google |
| H1 e inizio pagina | L'indice ChatGPT conserva titolo + ~200 caratteri iniziali; H1 nell'83,6% degli snippet | [SEJ 2026-08, Resoneo, 534 pagine] Debole-Media; non testato se cambiarlo aumenti le citazioni | Google usa H1 per i title link |
| Troppe pagine sullo stesso tema | Resa di citazione 1,7% con 6+ pagine dello stesso dominio vs 4–6% con 1–2 | [SEJ 2026-08, Mohanadasan, 1 account] Debole | Coerente con "consolidare i duplicati" |
| Dati strutturati (JSON-LD) | Aggiunta di JSON-LD: nessun aumento significativo (AIO -4,6%, AI Mode +2,4%, ChatGPT +2,2%) | [SEJ 2026-05/06, Ahrefs, 1.885 pagine vs 4.000 controlli, diff-in-diff] Media (miglior disegno disponibile; critica: pagine già molto citate) | Google: non servono per l'AI |
| llms.txt | 97% dei file senza richieste; nessun effetto su 300.000 domini; adozione ~2%, spesso da plugin | [SEJ 2026-06, Ahrefs 137.000 domini; SE Ranking; Web Almanac] Media | Google: ignorato |
| Reddit / UGC | ChatGPT: contenuti corporate 94,7%, Reddit 2–5% (quasi zero in finanza/sanità); quota Reddit in ChatGPT -86% in 3 settimane (estate 2026); in AIO/Perplexity Reddit più presente | [SEJ 2026-03, Indig] [SEJ 2026-08] Media-Debole, molto variabile | Comprare presenza su Reddit = manipolazione |
| Freschezza | Finestra ~30 giorni osservata in ChatGPT per domande commerciali | [SEJ 2026-09, un osservatore] Debole | Google: niente date cambiate senza modifiche reali |

Sintesi [D]: le leve con evidenza più solida e coerenti con Google sono (1) essere indicizzabili e leggibili, (2) contenuti non generici con fatti verificabili, (3) reputazione e menzioni autentiche fuori sito. Schema, llms.txt, chunking e formati "magici" non hanno evidenza.

### Struttura di contenuto citabile
- Google: organizzare per le persone (paragrafi, sezioni, intestazioni), nessun chunking necessario, nessuna lunghezza ideale. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Pratiche convergenti tra autori terzi e guida Bing/Microsoft [SEJ 2026-01/03, linee guida Microsoft, Forte per Bing; opinioni per il resto]:
  - risposta chiara all'inizio della pagina o della sezione, poi approfondimento;
  - sezioni autosufficienti con intestazioni descrittive, anche in forma di domanda reale;
  - fatti espliciti con numeri, unità, date e nomi propri vicini alla frase che li usa;
  - tabelle o liste per dati tabellari e confronti;
  - **informazioni chiave non nascoste in tab/accordion** chiusi (Bing: l'AI potrebbe non renderizzarle; Google: limita i deep link "Leggi tutto" [G](https://developers.google.com/search/docs/appearance/snippet));
  - una pagina per intento; dichiarare "per chi è / per chi non è", modalità, fascia di prezzo, limiti;
  - autore riconoscibile, data visibile e reale.
- ⚠ Numeri non supportati da Google né replicati: blocchi di 150–300 parole, chunk di 200–500 caratteri, "risposta nelle prime 2 frasi", soglie di parole o di heading. [SEJ 2025-10/12, 2026-02, opinioni e correlazioni] Non usarli come regole.
- Metodo utile [SEJ 2026-01/09, opinione]: ricavare le sotto-domande (fan-out) da domande reali dei clienti, recensioni dei concorrenti, chiamate e query di Search Console, non da liste generate; senza creare una pagina per ciascuna (AI-12).

### JavaScript e bot AI
- Google esegue JavaScript, ma scrive che SSR o pre-rendering restano "un'ottima soluzione" perché più veloci e perché **non tutti i bot eseguono JS**. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Test di terzi: i bot di OpenAI, Anthropic, Meta, ByteDance e Perplexity non eseguono JS; Gemini (infrastruttura Googlebot), Applebot e CCBot sì. [SEJ 2025-12, test Vercel 2024 + verifiche Gabe, Media] Studio su 274 homepage: 36% ha meno dell'80% del contenuto nell'HTML grezzo. [SEJ 2026-06, studio di settore, Debole-Media]
- ⚠ Il 4/3/2026 Google ha tolto dalla guida JS la raccomandazione di testare con JavaScript disattivato (non più attuale per Google). Molti autori la propongono per i bot AI: è un test valido per i bot terzi, non un requisito Google. [SEJ 2026-03, news changelog]
- ⚠ Servire una versione senza JS solo ai bot: rischio cloaking; il rendering dinamico è un ripiego sconsigliato. Usare SSR/prerender uguale per tutti. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering)

### Traffico reale dai chatbot
- Volume: LLM ~1,08% delle sessioni [SEJ 2026-03, Conductor, 13.770 domini, Media]; tutte le AI ~0,24% del traffico globale, ChatGPT ~80% del referral AI [SEJ 2026-04, SE Ranking, 101.000 siti, vendor]; <1% dei referral per gli editori [SEJ 2026-03, Chartbeat]; 1–2% delle chiamate dei clienti da citazioni AI [SEJ 2026-09, CallRail, vendor]. Quota visite tra piattaforme AI (maggio 2026): ChatGPT ~53%, Gemini ~28%, Claude ~9%, Perplexity ~1% [SEJ 2026-09, Similarweb].
- Valore: dati opposti. Conversioni 11x l'organico [SEJ 2026-07, Microsoft Clarity, 1.200 siti editori] contro conversioni inferiori a quasi tutti i canali [SEJ 2026-07, Marketing Science, 973 siti]; "2–4x" [SEJ 2026-03, Forrester, senza campione]. Lettura [D]: canale piccolo e disomogeneo, va misurato sui propri dati.
- Attribuzione sporca: molti utenti ChatGPT arrivano come "Direct" [SEJ 2025-10, guida, opinione]; in un'agenzia l'80–90% dei lead AI era classificato organico/diretto [SEJ 2026-08, dati di un'agenzia]; il 58,8% del traffico AI atterra in home mentre il 65% delle citazioni è su pagine interne [SEJ 2026-08, Solís].
- Effetto sui clic da Google: con un riassunto AI clic sull'8% delle visite vs 15% senza [SEJ 2026-01, Pew citato, dati USA]; -38% di clic in un esperimento randomizzato [SEJ 2026-05, ISB/CMU, 1.065 utenti, Media-Forte]; -58% CTR in posizione 1 [SEJ 2025-12/2026-03, Ahrefs, 300.000 keyword]; query di brand con AIO +18% CTR [SEJ 2026-03, Amsive]. Google sostiene che i clic da AIO sono di qualità superiore. [G](https://developers.google.com/search/docs/appearance/ai-features)

### Hype da non seguire
⚠ Tutte oltre o contro Google; nessuna evidenza di beneficio misurato:
- llms.txt, `llms-author.txt`, Content-Signal in robots.txt, mirror Markdown "per agenti", "AI Instructions", OKF/ARD, schemamap, WebMCP/MCP/NLWeb per siti di contenuto. [SEJ 2025-11 → 2026-09, molte fonti; Mueller: llms.txt "puramente speculativo"] (Lighthouse ha un audit sperimentale "Agentic Browsing" che controlla llms.txt: verifica solo la sintassi, non indica effetti sulla Ricerca [SEJ 2026-06/07]).
- "Schema per farsi citare", FAQPage "critico per GEO", knowledge graph/Wikidata "per l'AI". [SEJ 2025-12 → 2026-09] (I rich result FAQ sono stati ritirati: vedi `myths-deprecated.md`.)
- Tool di "AI visibility score" aggregati presentati come ranking; "share of model" su pochi prompt. [SEJ 2026-06/09]
- Framework coniati da autori ("Machine-First Architecture", "Verified Source Pack", "Latent Choice Signals", "Decision Distance"…): concetti, non standard.
- Reddit/recensioni/menzioni acquistate, listicle "i migliori" auto-promozionali, prompt nascosti: manipolazione (spam per Google, abuso per Bing).
- Percentuali di vendor senza controllo ("+13% con schema", "2,8x conversioni", "+239% citazioni").

---

## Note per tipo di sito
Archetipi come in `archetypes.md`.

**personal-brand**
- Obiettivo AI realistico: che gli assistenti descrivano correttamente la persona (nome, ruolo, competenze, città) e la associno a una nicchia; il traffico da AI sarà minimo [D].
- Leve: pagina "Chi sono" in testo HTML con fatti verificabili, nome e bio identici su sito/LinkedIn/GitHub/YouTube, case study con esperienza e dati propri, menzioni esterne autentiche (talk, articoli, podcast, open source) [SEJ 2026-01/09, opinione convergente]. `Person` + `sameAs` aiuta a disambiguare, non è una leva di citazione garantita [SEJ 2026-06/08].
- Omonimi: audit periodico di cosa dicono gli assistenti sul nome (AI-20); contenuto "ponte" se ruolo o titoli sono cambiati [SEJ 2026-09, opinione].
- Portfolio in SPA (Angular, React, Vue): AI-05 è bloccante per i bot AI; usare SSR/prerender.
- Bot: chi vuole essere trovato dai recruiter via assistenti non dovrebbe bloccare OAI-SearchBot, Claude-SearchBot, PerplexityBot, ChatGPT-User [D].

**professionista-servizi / attivita-locale**
- Google: per le risposte AI locali contano il **Profilo dell'attività** aggiornato e le informazioni coerenti. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Terzi: NAP, orari, servizi e area servita identici su sito, Business Profile, Apple/Bing Places e directory; recensioni reali con risposta; menzioni da associazioni, ordini professionali, stampa locale [SEJ 2026-07/09, dati di vendor locali, Debole-Media]. Le liste AI locali sono instabili: ripetendo la stessa ricerca su Gemini la stessa attività è in cima solo nel ~7% dei casi contro ~90% del local pack [SEJ 2026-09, Steady Demand, Debole].
- Niente pagine "servizio + città" clonate per inseguire il fan-out (doorway / contenuti su larga scala).
- Prezzi o fasce di prezzo, modalità (online/in presenza), tempi e prenotazione in testo, CTA in alto per chi arriva già convinto da un assistente [SEJ 2026-06, Manic, opinione].
- Temi vicini a lavoro, salute, denaro: niente promesse, credenziali vere e verificabili (vedi `content-quality-spam.md`).

**editoriale**
- Rischio principale: contenuto informativo generico, il più assorbito dalle risposte AI e il più colpito nei clic [SEJ 2026-03/05, dati di più fonti]. Puntare su esperienza diretta, dati originali, autori reali.
- Badge "fonte preferita" (pulsante o deep link) utile soprattutto per notizie. [G](https://developers.google.com/search/docs/appearance/preferred-sources)

**ecommerce**
- Merchant Center (feed) e dati prodotto aggiornati alimentano anche le risposte AI. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) Protocolli agentici (UCP, ACP) e checkout via agenti: solo se la piattaforma li supporta; nessun dato di impatto [SEJ 2026-01/09].

**prodotto-saas**
- I confronti "X vs Y" e le alternative sono il terreno principale delle risposte AI [SEJ 2026-08, studio con n minimo]; pagine di confronto oneste, documentazione indicizzabile, recensioni su piattaforme terze. Evitare listicle "i migliori" in cui ci si mette primi: associati a cali e, se citati, il brand viene spesso escluso dalla raccomandazione [SEJ 2026-07, Lily Ray, 100 query, Debole].
