# Entità e personal brand

> Aggiornato al 2026-10-03. Fonte primaria: Google. Secondaria: SEJ (ott 2025–ott 2026).
> Legenda: **[G](url)** = documentazione Google Search Central (fatto). **Deduzione** = ragionamento da fatti Google, non affermato da Google. **[SEJ …]** = fonte terza (opinione, studio di vendor, caso singolo).
> Vale per persone (portfolio, autore, consulente) e piccoli brand. File collegati: `local-seo.md` (attività con sede/area servita), `structured-data.md` (sintassi), `content-quality-spam.md`, `ai-search.md`.

## Indice
- [Fatti e regole (Google)](#fatti-e-regole-google)
- [Controlli per l'audit](#controlli-per-laudit)
- [Checklist off-site](#checklist-off-site-azioni-manuali-che-la-skill-può-solo-guidare)
- [Regole per contenuti e struttura del sito](#regole-per-contenuti-e-struttura-del-sito)
- [Cosa dicono le fonti terze](#cosa-dicono-le-fonti-terze)
- [Miti e consigli obsoleti](#miti-e-consigli-obsoleti)

## Fatti e regole (Google)

### 1. Entity home e pagina "Chi sono"
- Google consiglia informazioni chiare **sull'autore o sul sito**: byline dove i lettori se l'aspettano, che porti a una pagina con dettagli sull'autore o a una pagina "chi siamo"; reputazione verificabile cercando il sito. [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- `ProfilePage`: la pagina deve avere come elemento principale **una singola persona o organizzazione affiliata al sito**. Casi validi: pagina autore, **pagina "Chi sono" di un blog**, pagina dipendente. Non valido: home principale di un negozio (troppe informazioni non di profilo). [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page)
  - Obbligatoria: `mainEntity` (`Person` o `Organization`; default `Person`) con `name` (nome reale; handle in `alternateName`; `alternateName` basta se manca `name`).
  - Consigliate: `dateCreated`, `dateModified` (solo modifiche umane ai metadati), su Person: `alternateName`, `description` (riga dell'autore o **qualifiche pertinenti**), `identifier`, `image` (mai segnaposto/icone; ≥ 50.000 px; 16x9/4x3/1x1), `sameAs` (altri profili o home del profilo), `interactionStatistic` (**solo statistiche della piattaforma che ospita il profilo**, non follower di altri social), `agentInteractionStatistic`; `hasPart` per attività recenti (es. Article con `author` → `{"@id": "#main-author"}`).
- `Organization` va sulla **home** o su una **singola pagina** che descrive l'organizzazione (es. Chi siamo), non su ogni pagina; nessuna proprietà obbligatoria; `name`/`alternateName` **uguali al nome del sito**; `logo` ≥ 112×112 px leggibile su bianco; `sameAs` verso social/siti di recensioni; `vatID` = importante indicatore di fiducia. [G](https://developers.google.com/search/docs/appearance/structured-data/organization)
- Più entità collegate: usare **`@id`** per collegarle; includere sempre il tipo principale della pagina. [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Autore negli articoli: `author` = `Person`/`Organization`; `author.name` **solo il nome** (qualifica in `jobTitle`, titoli in `honorificPrefix`/`honorificSuffix`); `author.url` verso la pagina che identifica l'autore (se interna, marcata `ProfilePage`) oppure `sameAs`; un oggetto per autore. [G](https://developers.google.com/search/docs/appearance/structured-data/article)
- Vietato usare i dati strutturati per **ingannare**: rubare l'identità di persone/organizzazioni, rappresentare in modo ingannevole proprietà o affiliazione; markup solo di contenuti visibili. [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

### 2. Nome del sito e SERP del proprio nome
- Il **nome del sito** è generato automaticamente; segnale principale = dati strutturati **`WebSite` sulla home** (`name`, `url` obbligatori; `alternateName` consigliato), poi `og:site_name`, `<title>`, intestazioni e testo della home, riferimenti sul web. [G](https://developers.google.com/search/docs/appearance/site-names)
  - Un nome per dominio o sottodominio; **sottodirectory non supportate**; markup su **tutti** i duplicati della home (http/https, www); un solo nodo `WebSite`.
  - Nome **univoco, non generico** ("I migliori dentisti in Iowa" è l'esempio negativo), coerente in tutta la home.
  - Se non viene scelto: aggiungere `alternateName`; come riserva il **dominio in minuscolo** come ultimo `alternateName` (o come `name` in ultima istanza). Il Test dei risultati avanzati **non** supporta i nomi dei siti: usare validator.schema.org. Tempi: giorni-settimane.
- Rebranding con vecchio nome che persiste: nome coerente in tutto il sito, tutte le versioni aggiornate; redirect corretti. [G](https://developers.google.com/search/help/office-hours/2022/december)
- **Diversità dei siti**: in genere non più di **due risultati** per sito nei risultati principali (sottodomini contano come lo stesso sito). [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide) → **Deduzione**: per la SERP del proprio nome, profili esterni coerenti occupano le altre posizioni.
- **Scheda informativa** (Knowledge Panel): Google trova nome, contatti e profili social dal web; un rappresentante verificato può aggiornarla e sovrascrivere i dati; feedback dal link in fondo alla scheda. [G](https://developers.google.com/search/docs/appearance/establish-business-details)
- **Sitelink** completamente automatici: aiutano title, intestazioni e anchor interni concisi. [G](https://developers.google.com/search/docs/appearance/sitelinks)
- La pagina che compare per il nome del sito dipende dall'**intento percepito**; può essere una pagina interna. [G](https://developers.google.com/search/help/office-hours/2023/september)

### 3. Omonimie e nomi ambigui
- Nomi simili a un'entità famosa o a un refuso di una parola comune: Google tende a correggere la query; i sistemi imparano il nome **col tempo (anche molti mesi)**, senza scorciatoie. Scegliere un nome che non sia il refuso di qualcosa di noto. [G](https://developers.google.com/search/help/office-hours/2022/november) · [G](https://developers.google.com/search/help/office-hours/2024/july)
- Nomi condivisi con altri (account social, attività): i risultati misti sono "legittimi"; per essere trovati serve un **identificatore chiaro**, non un termine usato da molti. [G](https://developers.google.com/search/help/office-hours/2023/january)
- Google **non usa** `llms.txt` né file simili (vale anche per `llms-author.txt` secondo Mueller). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [SEJ 2026-07, news Mueller]

### 4. Dominio e hosting
- Ospitare i contenuti sul **proprio dominio**: frame/inoltro mascherato rendono impossibile il ranking col proprio dominio; Google Sites "non ideale". [G](https://developers.google.com/search/help/crawling-index-faq) · [G](https://developers.google.com/search/help/office-hours/2023/september)
- Keyword nel dominio: effetto quasi nullo; TLD indifferente salvo target paese; trattini ammessi. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- Copie del proprio contenuto che superano l'originale possono indicare problemi di qualità del sito originale. Syndication (es. LinkedIn Pulse): si scambia visibilità sulla piattaforma con il rischio che la piattaforma si posizioni sopra il proprio sito; per escluderle dalla Ricerca serve `noindex` sul partner, il canonical è solo un suggerimento. [G](https://developers.google.com/search/help/office-hours/2024/june) · [G](https://developers.google.com/search/help/office-hours/2023/june)
- PDF (CV, pubblicazioni): inserire un **link al sito in cima** al PDF; contenuti accessibili senza login. [G](https://developers.google.com/search/help/office-hours/2023/december)

### 5. Profili della Ricerca e proprietà della piattaforma
- **Profilo della Ricerca**: riunisce contenuti da web e social (Instagram, TikTok, YouTube, X, Facebook, sito) su `profile.google.com/@handle`; chi lo segue vede più contenuti nel **Feed personalizzato (Discover)**. Badge sul sito: link al profilo, touch target ≥ 48×48 dp Android / 44×44 px web, non alterare la "Super G". [G](https://developers.google.com/search/docs/appearance/search-profiles)
  - **Solo USA** e con **soglia follower** (10.000 su una piattaforma da settembre 2026; prima 100.000/35.000); **non influisce sul ranking**. [SEJ 2026-06 e 2026-09, news Google] — la pagina Google letta non riporta paese né soglia.
- **Proprietà della piattaforma** in Search Console per **Instagram, TikTok, X, YouTube** (globali dal 29/07/2026), anche senza sito; report Rendimento, Insight, Obiettivi; se il profilo della Ricerca è rivendicato, gli account vengono aggiunti automaticamente. **LinkedIn e GitHub non sono supportati.** [G](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) · [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide)

### 6. Query con brand e Search Console
- **Filtro query con brand / non correlate al brand** nel report Rendimento (+ scheda in Approfondimenti): include nome, varianti, refusi, prodotti/servizi unici del brand; classificazione con sistema AI interno, possibili errori; **nessun effetto sul ranking**; solo **proprietà di primo livello** (non prefisso percorso né sottodominio) e con volume sufficiente; disponibile per tutti i siti idonei dall'11/03/2026. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Verificare il sito in Search Console per stabilirlo come presenza ufficiale; la verifica in sé non cambia il ranking. [G](https://developers.google.com/search/docs/appearance/establish-business-details) · [G](https://developers.google.com/search/help/office-hours/2023/january)
- Report sul rendimento dell'AI generativa: solo impressioni (AI Overview, AI Mode, Discover), globale dal 31/08/2026. [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)

### 7. Autore, credenziali, E-E-A-T
- **E-E-A-T non è un fattore di ranking** specifico; l'affidabilità è l'aspetto più importante; peso maggiore su temi **YMYL** (salute, stabilità finanziaria, sicurezza). [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- **Autori fittizi** (foto generate, nomi inventati, credenziali false) = inganno, segnale di bassa qualità (aggiornamento del 01/10/2026). [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [SEJ 2026-10, news Google]
- Contenuti con AI: spiegare come sono stati creati quando i lettori se lo aspettano; verifica manuale di testo e metadati. [G](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- Esperienza in prima persona, contenuti **non generici** ("Perché abbiamo rinunciato a…" > "7 consigli…"). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### 8. Menzioni, link e spam
- Link spam include: guest post/advertorial/comunicati con anchor ottimizzati; scambi di link; directory e social bookmarking di bassa qualità; **link diffusi in footer o template di più siti (es. "sito realizzato da")**; firme nei forum. Link pubblicitari ammessi con `rel="sponsored"`/`nofollow`. [G](https://developers.google.com/search/docs/essentials/spam-policies)
- Credit link "Realizzato da …" nei siti dei clienti: non preoccuparsi troppo; se controllabili, `nofollow`; anchor sensato, non pieno di keyword. [G](https://developers.google.com/search/help/office-hours/2023/january)
- Guest post per ottenere backlink, anche con contenuto di valore = violazione se i link non sono qualificati. [G](https://developers.google.com/search/help/office-hours/2023/september)
- Chi si affida a un consulente: **non inserire mai un link al sito del SEO**; il proprietario risponde delle azioni dei fornitori. [G](https://developers.google.com/search/docs/fundamentals/do-i-need-seo)
- Spam include la **manipolazione delle risposte AI**; cercare menzioni inautentiche è poco utile. [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **Abuso della reputazione del sito**: ospitare contenuti di terzi per sfruttare i segnali del proprio dominio (azione manuale fuori SEE; nel SEE classificazione separata della sezione dal 30/08/2026). **Abuso di domini scaduti**. [G](https://developers.google.com/search/docs/essentials/spam-policies)
- Far conoscere il sito: community, social, URL su biglietti da visita e materiali; Google trova i siti tramite link e menzioni. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G](https://developers.google.com/search/help/office-hours/2023/april)
- Dati strutturati **non necessari** per le funzionalità AI; nessun markup speciale. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

## Controlli per l'audit

Gravità: **Critica** = inganno/rischio azione manuale · **Alta** = identità confusa o nome non trovato · **Media** = miglioramento importante · **Bassa** = rifinitura. "Auto" = dal codice/HTML; "Manuale" = serve l'utente o uno strumento esterno.

| ID | Controllo | Come verificarlo | Gravità | Fonte |
|---|---|---|---|---|
| EN-01 | Esiste un'**entity home** ("Chi sono"/About) con nome completo, ruolo, foto reale, bio, contatti, link ai profili; linkata da navigazione/footer | Auto: crawl + link interni | Alta | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| EN-02 | `ProfilePage` con `mainEntity` `Person` + `name` sulla pagina Chi sono (non su una home mista con servizi/blog) | Auto: JSON-LD + tipo di pagina | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| EN-03 | `Person.image` = foto reale, URL scansionabile, ≥ 50.000 px; niente avatar segnaposto | Auto | Bassa | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| EN-04 | `sameAs` solo verso profili **propri** (LinkedIn, GitHub, social), URL validi (200), nessun profilo altrui | Auto (status) + Manuale (proprietà) | Critica se profilo altrui, altrimenti Media | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| EN-05 | I profili esterni linkano **al sito** (bio LinkedIn, GitHub, social, GBP) | Manuale: elenco profili | Alta | [G](https://developers.google.com/search/help/office-hours/2023/december) |
| EN-06 | `@id` stabili per `Person`, `Organization`, `WebSite`; definiti una volta e richiamati da `author`/`publisher`/`mainEntity` | Auto | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) · [SEJ 2026-10, Pollitt] |
| EN-07 | `WebSite` sulla home (radice dominio) con `name`, `url`, `alternateName`; un solo nodo; presente su tutte le varianti della home | Auto | Alta | [G](https://developers.google.com/search/docs/appearance/site-names) |
| EN-08 | Nome del sito = nome/brand reale, **non generico** ("Portfolio", "Full Stack Developer", "Orientamento al lavoro"); coerente con `<title>`, `og:site_name`, H1 della home | Auto | Media | [G](https://developers.google.com/search/docs/appearance/site-names) |
| EN-09 | `Organization` solo se esiste un brand/ditta; `name` = nome del sito; `logo` ≥ 112 px leggibile su bianco; `vatID` se c'è partita IVA | Auto | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/organization) |
| EN-10 | Forma del nome **identica** ovunque (secondo nome, accenti, iniziali) in title, H1, JSON-LD, profili | Auto (sito) + Manuale (profili) | Alta | [G](https://developers.google.com/search/help/office-hours/2023/january) · [SEJ 2026-09, Clarkson-Bennett] |
| EN-11 | `<title>` della home = Nome Cognome + ruolo/qualificatore (no "Home") | Auto | Media | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| EN-12 | Omonimi: qualificatore stabile (ruolo, città, specializzazione) in title, `description`, bio dei profili; controllo SERP del nome | Manuale: SERP da browser pulito | Alta (se omonimi) | [G](https://developers.google.com/search/help/office-hours/2023/january) · [SEJ 2026-07, Montti] |
| EN-13 | Articoli con byline visibile che porta alla pagina autore; `author` `Person` con solo il nome in `name`, `url` → pagina profilo | Auto | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/article) |
| EN-14 | Nessun autore o credenziale **fittizi**; credenziali verificabili (link a enti, associazioni, certificazioni) | Manuale | Critica | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| EN-15 | Credenziali, ruolo e date coerenti tra sito, LinkedIn, CV/PDF; nessun ruolo vecchio non spiegato | Manuale | Media | [SEJ 2026-09, conflicting info] |
| EN-16 | `interactionStatistic` non riporta follower di altre piattaforme | Auto | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page) |
| EN-17 | Nessuna stella (`AggregateRating`/`Review`) sulle **proprie** testimonianze (Organization/LocalBusiness) | Auto | Alta | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| EN-18 | Nessun listicle autoreferenziale ("i migliori sviluppatori/orientatori" con sé al n.1) | Auto: pattern `intitle:migliori` + proprio nome in prima posizione | Alta | [SEJ 2026-02 e 2026-06, Lily Ray] · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| EN-19 | Credit link "realizzato da" nei siti dei clienti: `nofollow`/`sponsored` o testo; anchor = nome, non keyword | Manuale: elenco siti clienti; Auto se accessibili | Alta | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| EN-20 | Sul proprio sito: nessun link "SEO by"/credit verso fornitori; link sponsorizzati qualificati | Auto | Media | [G](https://developers.google.com/search/docs/fundamentals/do-i-need-seo) |
| EN-21 | Pagina "Stampa/Interventi" con menzioni reali (talk, podcast, articoli) e link alle fonti; nessuna menzione comprata | Auto + Manuale | Media | [G](https://developers.google.com/search/docs/essentials/spam-policies) · [SEJ 2026-09, Jarboe] |
| EN-22 | Dominio proprio (non `github.io`/`vercel.app`/`netlify.app` come sito principale) | Auto | Alta | [G](https://developers.google.com/search/help/crawling-index-faq) · [SEJ 2026-01, Mueller] |
| EN-23 | Articoli ripubblicati (LinkedIn, dev.to, Medium): prima sul sito, poi sulla piattaforma con link/canonical all'originale dove possibile | Manuale | Media | [G](https://developers.google.com/search/help/office-hours/2024/june) · deduzione |
| EN-24 | CV/pubblicazioni: versione HTML indicizzabile + PDF con link al sito in alto | Auto | Bassa | [G](https://developers.google.com/search/help/office-hours/2023/december) |
| EN-25 | Contenuti di terzi ospitati (guest post, articoli sponsorizzati) per sfruttare il dominio | Auto + giudizio | Alta (se presenti) | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| EN-26 | Search Console: proprietà **Dominio** verificata (serve al filtro brand) | Manuale | Media | [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter) |
| EN-27 | Proprietà della piattaforma aggiunte per YouTube/Instagram/X/TikTok se usati | Manuale | Bassa | [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) |
| EN-28 | Contenuti chiave della pagina Chi sono nell'HTML iniziale (SPA: SSR/prerender) | Auto: HTML grezzo vs renderizzato | Media | [SEJ 2026-09, brand protection] · ⚠ Google esegue JS |
| EN-29 | `llms.txt`/`llms-author.txt`/direttive "content-signal": assenza **non** è un errore; se presenti, segnalare che Google li ignora | Auto | Bassa (informativo) | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| EN-30 | Contatti per recruiter/clienti in testo (email, LinkedIn, modulo), non solo dietro JS o immagine | Auto | Media | [G](https://developers.google.com/search/docs/fundamentals/get-started-developers) |

## Checklist off-site (azioni manuali che la skill può solo guidare)

**Identità e profili**
- [ ] Scrivere una **definizione canonica** (nome, ruolo, specializzazione, per chi, dove, credenziali) e riusarla identica o quasi su sito, LinkedIn (headline, About, URL personalizzato), GitHub (bio, link al sito, README del profilo), social, GBP se esiste [SEJ 2026-05, Manic; SEJ 2026-09, Clarkson-Bennett].
- [ ] Inserire il **link al sito** in ogni profilo [G](https://developers.google.com/search/help/office-hours/2023/december).
- [ ] Registrare per tempo **dominio e handle** del proprio nome/progetti (caso NanoClaw: un impostore ha superato il sito reale) e, per sviluppatori, riservare i **namespace dei pacchetti** [SEJ 2026-03; SEJ 2026-09].
- [ ] Rimuovere/aggiornare profili abbandonati, bio vecchie, PDF con ruoli superati; dove un titolo è cambiato, aggiungere una frase ponte ("dal 2025 …, prima …") [SEJ 2026-09, conflicting info].

**Google**
- [ ] Verificare il dominio in Search Console (proprietà Dominio); attivare il filtro brand quando disponibile; annotare lanci e modifiche [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter).
- [ ] Aggiungere le proprietà della piattaforma (YouTube, Instagram, X, TikTok) se usate [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide).
- [ ] Se compare una scheda informativa: rivendicarla come rappresentante verificato e correggere i dati [G](https://developers.google.com/search/docs/appearance/establish-business-details).
- [ ] Profilo della Ricerca: solo se in USA e oltre la soglia follower; altrimenti nessuna azione [SEJ 2026-09].

**SERP del proprio nome (audit periodico)**
- [ ] Cercare "Nome Cognome", "Nome Cognome + ruolo", "Nome Cognome + città" da browser pulito, non loggato, anche da mobile; annotare data, lingua, luogo; guardare autocomplete, immagini, notizie, mappe [SEJ 2026-09, brand protection].
- [ ] Classificare i risultati: propri / profili propri / omonimi / terzi corretti / terzi sbagliati.
- [ ] Ripetere su Bing e sugli assistenti (ChatGPT, Gemini, Perplexity, AI Mode) con domande dirette ("chi è …") e senza il nome ("chi consiglieresti per …"), più volte e in conversazioni nuove; registrare affermazioni corrette/obsolete/false/su un'altra persona [SEJ 2026-09, Forrester; SEJ 2026-07].

**Menzioni e PR (guadagnate, non comprate)**
- [ ] Talk, meetup, podcast, interviste, articoli ospiti **senza anchor ottimizzati**; trasformare ogni intervento in pagina del sito (trascrizione, slide, link alla fonte) [SEJ 2026-09, Jarboe] · [G](https://developers.google.com/search/docs/essentials/spam-policies).
- [ ] Associazioni professionali, ordini, enti, newsletter di settore (livello nazionale poi regionale) [SEJ 2026-07, Montti].
- [ ] Contributi verificabili: open source, repository, premi con criteri pubblici.
- [ ] Non modificare in prima persona Wikipedia/Wikidata per sé (conflitto di interessi; regola delle piattaforme, fuori corpus); non comprare menzioni o post Reddit.

**Siti realizzati per clienti (sviluppatori/agenzie)**
- [ ] Credit link nel footer: `rel="nofollow"` o testo semplice, anchor = proprio nome/brand [G](https://developers.google.com/search/help/office-hours/2023/january).
- [ ] Preferire una **pagina portfolio** sul proprio sito con caso di studio (con permesso del cliente) al link sitewide.

## Regole per contenuti e struttura del sito
1. **Entity home unica**: una pagina "Chi sono" che è la fonte canonica dei fatti sulla persona; tutte le altre pagine e profili rimandano lì. Home e Chi sono possono coincidere solo se la home è davvero una pagina di profilo [G](https://developers.google.com/search/docs/appearance/structured-data/profile-page).
2. **Struttura JSON-LD consigliata** (deduzione da [G]): sulla home `WebSite` (`@id` `/#website`, `name`, `alternateName`, `url`) + eventuale `Organization` (`/#org`); sulla pagina Chi sono `ProfilePage` con `mainEntity` `Person` (`@id` `/chi-sono#person`, `name`, `alternateName`, `description` con qualifiche, `image`, `sameAs`, `jobTitle`); negli articoli `author: {"@id": "…#person"}`. Definire ogni entità una volta e richiamarla.
3. **Qualificatore fisso** accanto al nome (ruolo + specializzazione o città) nei title e nelle bio, soprattutto se esistono omonimi [G](https://developers.google.com/search/help/office-hours/2023/january).
4. **Prove, non aggettivi**: progetti/casi con problema, decisioni, risultati, stack o metodo, ruolo personale nel lavoro di gruppo; screenshot, demo, repository. Niente "il migliore", niente classifiche su se stessi [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
5. **Credenziali spiegate**: titolo, ente che lo rilascia (con link), anno; per titoli italiani poco noti all'estero spiegare cosa sono [SEJ 2026-08, Hunt]. Nessuna credenziale non verificabile [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Nota fuori corpus (Italia): le professioni non organizzate in ordini hanno obblighi di trasparenza propri (L. 4/2013): verificare con un consulente.
6. **Testimonianze**: testo reale con nome (o iniziali) e contesto; mai stelle nel markup della propria entità [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
7. **Una pagina per progetto/servizio**, URL descrittivo, title specifico ("Progetto X: … — Nome Cognome") invece di "Progetto" [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
8. **Contenuti propri prima delle piattaforme**: pubblicare sul sito e poi riprendere su LinkedIn/dev.to con rimando; valutare caso per caso la syndication integrale [G](https://developers.google.com/search/help/office-hours/2024/june).
9. **Date e aggiornamenti reali**: non cambiare date senza modifiche sostanziali [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
10. **Bilingue (es. IT/EN per recruiter esteri)**: URL distinti per lingua, stessa entità (`@id` uguale), hreflang reciproco; nome e qualifiche coerenti nelle due lingue (vedi `crawling-indexing.md`).
11. **SPA**: title, H1, bio, contatti e JSON-LD nell'HTML servito (SSR/prerender); Google esegue JS, molti crawler di assistenti no [SEJ 2026-09].

## Cosa dicono le fonti terze
Formato: [SEJ AAAA-MM, autore, tipo evidenza e campione]. ⚠ = va oltre o contro Google.

**Entità e coerenza**
- [SEJ 2026-09, Clarkson-Bennett, opinione] Schema "Own → Describe → Prove → Earn → Monitor": asset propri (sito, About, schema/sameAs, profili, GBP), pagine che puntano all'entità giusta, identità verificabile per ogni persona, menzioni che corroborano, monitoraggio della deriva. Per piccoli brand la coerenza conta più di tutto.
- [SEJ 2026-06, Pollitt, opinione] Entity optimization ≠ solo schema: nomi/indirizzi identici ovunque, `sameAs` verso profili autorevoli, entity home con link ai profili, tassonomia e link interni chiari.
- [SEJ 2026-01, Clarkson-Bennett, opinione + dato terzo non verificato] Rispondere presto, date coerenti tra pagina/schema/sitemap, entità nel primo paragrafo, rivendicare il Knowledge Panel se esiste.
- [SEJ 2026-09, autore n.d., opinione con esempio anonimo] Rischio principale = **informazioni in conflitto** (vecchi PDF, bio con titoli superati): "brand claim audit" e frasi ponte.
- [SEJ 2026-03, news Mueller] Vecchio nome che persiste dopo un rebrand: usare il dominio come nome alternativo; sitemap pulite.
- ⚠ [SEJ 2026-03, Baker, aneddoto] "Lo schema Person addestra gli LLM" (CEO omonimo corretto dopo lo schema): nessuna conferma; [SEJ 2026-07, Forrester, opinione + letteratura] lo schema agisce sul Knowledge Graph e sul retrieval, non sulla memoria dei modelli; [SEJ 2026-06, Williams-Cook, esperimento piccolo] gli LLM leggono il JSON-LD come testo; studio Ahrefs (1.885 pagine vs 4.000 controlli) senza effetto sulle citazioni. Sintesi: Person + `sameAs` utili per disambiguare, non leva di citazione.
- ⚠ [SEJ 2026-03, Yoast "Schemamap"] endpoint unico di JSON-LD per agenti: nessun motore lo legge; il principio utile (entità con `@id` coerenti, senza duplicati) vale già per Google.

**Omonimie**
- [SEJ 2026-07, news Mueller + opinione Montti] `llms-author.txt` e "content-signal" non usati da nessun crawler; il problema degli omonimi si risolve diventando più noti (interviste, podcast, pagine), non con file tecnici.
- [SEJ 2026-09, Forrester, opinione con paper; interesse commerciale dichiarato] Per entità poco documentate i modelli "riempiono" con il vicino più noto (concorrente, omonimo, versione vecchia): interrogarli anche senza il proprio nome.
- [SEJ 2026-08, Lily Ray, sintesi studi] ChatGPT usa spesso `site:` e a volte "indovina" il dominio ufficiale sbagliato: chiarire il dominio ufficiale in modo coerente sul web.

**Menzioni e PR**
- [SEJ 2025-11, news Google, Robby Stein in podcast] Con il fan-out l'AI cerca liste e articoli che citano le attività: essere menzionati in articoli pubblici aiuta a essere trovati; non è un fattore dichiarato.
- [SEJ 2025-11, Ahrefs, correlazione ~0,67, campione non dettagliato, vendor] Le menzioni del brand sul web sono il fattore più correlato alla presenza nelle AI Overview. Correlazione, non causa.
- [SEJ 2026-08, Forrester, opinione + letteratura accademica] La conoscenza "parametrica" di un nome cresce con fonti indipendenti e formulazioni varie: si costruisce in anni, non con campagne.
- [SEJ 2026-09, Jarboe, dati terzi non verificati] Wikipedia, podcast, Reddit, YouTube molto citati dagli assistenti; trasformare ogni intervento in trascrizione e pagina.
- [SEJ 2026-04, Shepard, >400 siti, correlazioni 0,21–0,39] Associati ai guadagni: servizio/prodotto proprio, compito completabile, asset proprietari, tema stretto, **brand forte** (quota di ricerche brand); effetto cumulativo.
- ⚠ [SEJ 2026-06, panel WordCamp] "Brand is the new backlink" e PR nofollow che "posizionano nelle AI": slogan/aneddoti.

**Spam e rischi**
- [SEJ 2026-02, Lily Ray, osservazionale su ~9 siti SaaS] Cali del 29–49% su siti con blog di listicle autopromozionali (insieme a contenuti AI in serie, date aggiornate senza modifiche, `AggregateRating` improprio).
- [SEJ 2026-06, Lily Ray, 100 query × 3 date, B2B SaaS] Quando l'AI cita la lista "migliori" scritta da un brand su se stesso, quel brand è escluso dalla raccomandazione nel 69% dei casi; AIO segnala gli "autoproclamati".
- [SEJ 2026-01, news Mueller] Sottodomini di hosting gratuito e TLD economici attirano spam e rendono più difficile la valutazione: per un portfolio usare un dominio proprio (deduzione dell'articolo).
- [SEJ 2026-03, caso NanoClaw, aneddotico] Progetto open source senza sito superato da un sito impostore registrato prima; contromisure (link da GitHub, schema, Search Console) non sufficienti nel breve.

**Misurazione**
- [SEJ 2026-03, news Mueller] Filtro brand non personalizzabile, non retroattivo, non per sottoproprietà né siti con poche impressioni; ⚠ l'autore lo collega a un brevetto sulle ricerche brand come segnale di ranking: speculazione (Google: il filtro non influisce sul ranking).
- [SEJ 2025-11, AWR, dataset Q3 2025] Query brand desktop: la posizione 1 perde CTR, le posizioni 2–6 guadagnano: la SERP del nome si "allarga".
- [SEJ 2026-07, Walsh, opinione] Costruire audience diretta (newsletter, follower, ricerche del nome) per ridurre la dipendenza da Google.

## Miti e consigli obsoleti
- **"Lo schema `Person` crea il Knowledge Panel / fa citare dagli LLM"** → nessuna garanzia; i dati strutturati non sono necessari per le funzionalità AI [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"`llms.txt` / `llms-author.txt` disambiguano gli omonimi"** → ignorati [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [SEJ 2026-07].
- **"E-E-A-T è un fattore di ranking; basta aggiungere bio e byline"** → non è un fattore; la byline da sola non migliora il ranking [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [SEJ 2026-10, Search Liaison citato].
- **"Il profilo della Ricerca migliora il ranking"** → no; beneficio in Discover, solo USA con soglia follower [G](https://developers.google.com/search/docs/appearance/search-profiles) · [SEJ 2026-09].
- **"LinkedIn/GitHub si monitorano in Search Console"** → le proprietà della piattaforma coprono solo Instagram, TikTok, X, YouTube [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide).
- **"Il nome del sito si imposta su una sottocartella (es. /blog o github.io/utente)"** → solo domini e sottodomini [G](https://developers.google.com/search/docs/appearance/site-names).
- **"Più link 'realizzato da' nei siti clienti = più autorità"** → link sitewide nei template = esempio di link spam [G](https://developers.google.com/search/docs/essentials/spam-policies).
- **"Una lista 'i migliori X' con me al primo posto aiuta nelle AI"** → zona grigia, osservati cali [SEJ 2026-02/06]; menzioni inautentiche poco utili [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"Stelle in SERP con le testimonianze dei clienti sul mio sito"** → non idonee (self-serving) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **"Verificare Search Console migliora il ranking"** → no [G](https://developers.google.com/search/help/office-hours/2023/january).
- **"Il dominio con keyword (nome-sviluppatore-angular.dev) aiuta"** → effetto quasi nullo; scegliere il nome della persona/brand [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
- **"Credenziali generiche o inventate per sembrare esperti"** → autori/credenziali fittizi = inganno (01/10/2026) [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
