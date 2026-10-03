# Gruppo G — Blog Google Search Central 2024–2026 (appunti)

Ambito: 85 articoli del blog ufficiale Google Search Central (febbraio 2024 – settembre 2026), letti integralmente dai Markdown scaricati. Ordine cronologico (per data di pubblicazione dell'articolo; a parità di mese, ordine di data). Gli annunci di eventi Search Central Live (SCL) sono riassunti in una riga salvo contenuti tecnici rilevanti.

Legenda: **[DEPRECATO]** = funzionalità rimossa/ritirata; **[NUOVO]** = nuova funzionalità/regola; **[SPAM]** = norma antispam; **[GSC]** = Google Search Console.

---

## 2024-02 — Search Central Live Argentina (annuncio evento)
Fonte: https://developers.google.com/search/blog/2024/02/search-central-live-argentina?hl=it
- Evento a Buenos Aires il 5 marzo 2024 (SEO di base: crawling/indicizzazione/pubblicazione, Search Console, Google News Argentina). Nessun contenuto tecnico.

## 2024-02 — Search Central Live torna in Brasile (annuncio evento)
Fonte: https://developers.google.com/search/blog/2024/02/search-central-live-sao-paulo-2024?hl=it
- San Paolo, 29 febbraio 2024; temi: dati Search Console in BigQuery, audit SEO tecnico, partnership locali. Nessun contenuto tecnico.

## 2024-02 — La Guida introduttiva alla SEO ha cambiato look (2 feb 2024)
Fonte: https://developers.google.com/search/blog/2024/02/ssg-gets-a-makeover?hl=it
- La SEO Starter Guide (nata nel 2008 come PDF di 22 pagine) è stata riscritta, più compatta, per **principianti** (nuovi proprietari di siti, creator), non per professionisti.
- **Rimosso dalla guida**: glossario (termini spiegati nel contesto); sezione dati strutturati (considerata avanzata: chi usa CMS come Wix/Squarespace può usare plugin); sezione ottimizzazione mobile ("la maggior parte dei nuovi siti è già ottimizzata per il mobile"); sezione analisi prestazioni del sito (passo successivo/avanzato).
- **Snellito**: "Sei su Google?" (unica sezione su come verificare la presenza e primi passi); "Hai bisogno di un esperto SEO?" (2 frasi + link); link dei titoli e snippet (rimandi alla doc dedicata); immagini (per i principianti **il testo alternativo è l'indicazione più importante**); "Disattivare la Ricerca Google"; link (messaggio invariato: i link sono utili a utenti e motori); promozione del sito (rimando a Google for Creators); struttura del sito (rimossi: sezione navigazione — focus su **link interni importanti**; sezione pagine 404 — "le pagine 404 non ci interessano davvero", fate ciò che è più utile per gli utenti; configurazione esplicita dei breadcrumb, ritenuta avanzata).
- **Aggiunto**: sezione sui contenuti duplicati (cosa sono e come correggerli "se necessario"); breve sezione video; sezione su **teorie/miti SEO su cui non concentrarsi troppo**; sezione su **quanto tempo serve per vedere l'impatto della SEO**.
- Implicazione: Google non considera più il "mobile-friendly" e i dati strutturati come temi base da principiante; l'enfasi è su contenuti, link interni, alt text, titoli/snippet.

## 2024-02 — Nuove esperienze della Ricerca nel SEE: risultati avanzati, unità di aggregatori e chip di perfezionamento (15 feb 2024)
Fonte: https://developers.google.com/search/blog/2024/02/search-experiences-in-eea?hl=it
- Contesto: preparazione al **Digital Markets Act (DMA)**; esperienze lanciate **solo per utenti nello Spazio Economico Europeo** (Italia inclusa).
- **[NUOVO] Risultato avanzato carosello** per query **locali, di viaggio e di acquisto** (es. "hotel nelle vicinanze"): ogni riquadro può mostrare prezzo, valutazione, immagini delle entità presenti sulla pagina; scorrimento orizzontale per più entità dello stesso sito. Senza dati strutturati → risultato testuale standard. Per query di shopping test iniziale in DE, FR, CZ, UK. Aggiornamento 29/02/2024: documentazione "dati strutturati per caroselli (beta)" disponibile (`/search/docs/appearance/structured-data/carousels-beta`).
- **[NUOVO] Unità di aggregatori** (siti di luoghi, offerte di lavoro, voli, prodotti) con link "Altri siti" e **chip di perfezionamento** (es. "Siti di luoghi"): **nessun markup richiesto**.
- Nuova unità per siti di compagnie aeree nelle query di voli.
- Come partecipare: moduli di interesse (trasporto via terra, hotel, case vacanze, offerte di lavoro, **attività locali**, cose da fare); voli → modulo dedicato; shopping → programma CSS. Aggiornamento 10/04/2025: moduli aggiornati.
- Pertinenza: aggregatori, fornitori e attività nel SEE. Una professionista locale *singola* non è aggregatore; i caroselli riguardano siti che elencano più entità.

## 2024-02 — Aggiungere il supporto per i dati strutturati per le varianti dei prodotti (20 feb 2024)
Fonte: https://developers.google.com/search/blog/2024/02/product-variants?hl=it
- **[NUOVO]** Supporto a `ProductGroup` (schema.org) con tre proprietà: `hasVariant` (nidifica i `Product` varianti), `variesBy` (proprietà che differenziano le varianti: taglia, colore…), `productGroupID` ("SKU principale").
- Le varianti devono essere raggruppate sotto un prodotto "principale"; supportati siti a pagina singola e multi-pagina per varianti.
- Integra i feed di Merchant Center (anche feed automatici). Nuove convalide nei report GSC "Snippet prodotto" e "Schede del commerciante" e nel Test dei risultati avanzati.
- Pertinenza: solo e-commerce.

## 2024-03 — Search Central Live Bucarest, Romania (annuncio evento, 4 mar 2024)
Fonte: https://developers.google.com/search/blog/2024/03/search-central-live-romania-2024?hl=it
- 4 aprile 2024; temi: priorità del team, miti SEO, argomenti sensibili come le elezioni. Nessun contenuto tecnico.

## 2024-03 — Aggiornamento principale di marzo 2024 e nuove norme relative allo spam (5 mar 2024)
Fonte: https://developers.google.com/search/blog/2024/03/core-update-spam-policies?hl=it
- **Core update marzo 2024**: più complesso del solito, modifica più sistemi principali; "evoluzione nel modo in cui identifichiamo l'utilità dei contenuti". **Non esiste più un solo indicatore o un solo sistema** per l'utilità (di fatto il "helpful content system" come sistema separato è assorbito nei sistemi di ranking principali); nuova FAQ `/search/help/helpful-content-faq`. Implementazione fino a un mese, fluttuazioni maggiori; esito pubblicato sulla Search Status Dashboard.
- Cosa fare: niente di speciale, creare contenuti soddisfacenti "pensati per le persone" (people-first). Chi perde ranking: leggere la guida sui contenuti utili, affidabili e people-first.
- **[SPAM][NUOVO] Tre nuove norme**:
  1. **Abuso di domini scaduti**: acquistare un dominio scaduto e riutilizzarlo principalmente per manipolare i ranking con contenuti di scarso valore (es. ex sito medico → casinò). È lecito usare un vecchio dominio per un sito nuovo, originale e pensato per le persone.
  2. **Abuso di contenuti su larga scala** (scaled content abuse): generare molte pagine principalmente per manipolare i ranking, non per aiutare gli utenti — **indipendentemente da come sono create** (automazione, IA generativa, persone o mix). Estende la vecchia norma sui "contenuti generati automaticamente". L'IA non è spam di per sé; lo è se lo scopo principale è manipolare il ranking.
  3. **Abuso della reputazione del sito** (site reputation abuse / "parassita"): pagine di terze parti pubblicate con supervisione minima o nulla del sito host per sfruttarne gli indicatori di ranking (sponsorizzate, pubblicitarie, di partner), tipicamente estranee allo scopo del sito. Non tutti i contenuti di terze parti sono violazione (advertorial/pubblicità nativa per i lettori abituali non necessariamente vanno bloccati). Contenuti violanti vanno **bloccati dalla Ricerca** (noindex ecc.). In vigore dal **5 maggio 2024**.
- Violazioni → ranking più basso o esclusione; azioni manuali notificate in GSC, richiesta di riconsiderazione.
- Lanciato anche lo **spam update di marzo 2024**.
- FAQ: i sistemi di ranking operano principalmente **a livello di pagina**, con alcuni indicatori a livello di sito. I punteggi "authority/reputation" di servizi terzi (es. DA/DR) **non corrispondono ad alcun indicatore di Google**.
- Coupon: ok se la pubblicazione è attivamente coinvolta (reperisce direttamente i coupon), non se usa servizi white-label per manipolare. Aggiornamenti: 26/04/2024 modulo feedback ranking (fino al 31/05/2024); 04/06/2024 FAQ coupon ampliate.

## 2024-03 — Search Central Live Varsavia, Polonia (annuncio evento)
Fonte: https://developers.google.com/search/blog/2024/03/search-central-live-poland-2024?hl=it
- 24 aprile 2024; temi: news ed e-commerce, miti e best practice. Nessun contenuto tecnico.

## 2024-04 — Migliorare la gestione dei token di proprietà di Search Console (16 apr 2024)
Fonte: https://developers.google.com/search/blog/2024/04/search-console-ownership-token-management?hl=it
- **[GSC][NUOVO]** In "Utenti e autorizzazioni" → "Token di proprietà inutilizzati": selezionare i token, "Rimuovi", poi "Verifica rimozione" per confermare che il token (meta tag, file HTML, record DNS ecc.) sia davvero stato tolto dal sito.
- Best practice: quando si rimuove un ex proprietario verificato, **rimuovere tutti i suoi token di verifica**, altrimenti può riottenere l'accesso (rilevante ad es. dopo cambio di agenzia/sviluppatore).

## 2024-05 — Search Central Live 2024 torna nella regione APAC (annuncio)
Fonte: https://developers.google.com/search/blog/2024/05/search-central-live-jakarta-apac-2024?hl=it
- Giacarta 25 luglio 2024 (in indonesiano), lightning talk della community; Q3 Indonesia/Thailandia, Q4 Malaysia/Taiwan. Nessun contenuto tecnico.

## 2024-06 — Siamo su LinkedIn (finalmente) (4 giu 2024)
Fonte: https://developers.google.com/search/blog/2024/06/linkedin-we-are-here?hl=it
- Apertura del canale LinkedIn ufficiale di Google Search Central (aggiornamenti algoritmo, best practice, Search Console). Nessun contenuto tecnico.

## 2024-06 — Aggiunta del supporto del markup per le norme sui resi a livello di organizzazione (11 giu 2024)
Fonte: https://developers.google.com/search/blog/2024/06/structured-data-return-policies?hl=it
- **[NUOVO]** Le norme sui resi si possono dichiarare nei dati strutturati **`Organization`** (a livello di attività) invece che per ogni `Product`; riduce il markup; idoneità a schede informative (knowledge panel), profili del brand e risultati prodotto.
- Utile soprattutto **senza account Merchant Center**; con Merchant Center è preferibile definirle lì.
- Testabili con il Test dei risultati avanzati.
- Consiglio esplicito: per attività online o locali usare i sottotipi di `Organization` **`OnlineStore`** o **`LocalBusiness`**.

## 2024-06 — Search Central Live Bangkok 2024 (annuncio evento)
Fonte: https://developers.google.com/search/blog/2024/06/search-central-live-bangkok-2024?hl=it
- 9 agosto 2024; temi: come funziona la Ricerca, qualità/aggiornamenti, analisi cali di traffico in GSC, Google Trends per SEO. Nessun contenuto tecnico.

## 2024-07 — Configurare la spedizione e i resi direttamente in Search Console (11 lug 2024)
Fonte: https://developers.google.com/search/blog/2024/07/configure-shipping-and-returns-search-console?hl=it
- **[GSC][NUOVO]** Impostazioni di spedizione e reso configurabili direttamente in Search Console (sincronizzate con Merchant Center).
- **Precedenza**: le impostazioni in Search Console **prevalgono** sulla configurazione del sito, compreso il markup merchant listing a livello di prodotto.
- Pertinenza: solo e-commerce.

## 2024-08 — I nuovi consigli in Google Search Console (5 ago 2024)
Fonte: https://developers.google.com/search/blog/2024/08/search-console-recommendations?hl=it
- **[GSC][NUOVO]** "Consigli" (Recommendations) nella pagina Panoramica: suggerimenti basati su dati di indicizzazione, scansione e pubblicazione (es. usare dati strutturati, aggiungere sitemap, individuare query e pagine di tendenza). Calcolati regolarmente, possono scadere/variare. Sperimentale, rollout graduale, solo se disponibili per il sito.

## 2024-08 — Cosa devi sapere sull'aggiornamento principale di agosto 2024 (15 ago 2024)
Fonte: https://developers.google.com/search/blog/2024/08/august-2024-core-update?hl=it
- Core update agosto 2024: più contenuti davvero utili, meno contenuti creati solo per il ranking. Tiene conto dei feedback dei creator; obiettivo di mostrare anche **siti piccoli o indipendenti** con contenuti utili e originali; mira a "acquisire meglio i miglioramenti" fatti dai siti.
- Aggiornata la pagina di assistenza sui core update con indicazioni per chi nota cali.

## 2024-08 — Search Central Live Kuala Lumpur e Taipei (annuncio evento)
Fonte: https://developers.google.com/search/blog/2024/08/search-central-live-kl-tpe-2024?hl=it
- KL 17 ottobre 2024 (inglese), Taipei 1 novembre 2024 (mandarino). Nessun contenuto tecnico.

## 2024-08 — Supporto di AVIF nella Ricerca Google (30 ago 2024)
Fonte: https://developers.google.com/search/blog/2024/08/happy-avifriday?hl=it
- **[NUOVO]** **AVIF** è un tipo di file supportato in Google Search, Google Immagini e ovunque la Ricerca usi immagini. Nessuna azione speciale per l'indicizzazione.
- Cautela: non fare cambi radicali di formato senza valutazione; se il cambio formato modifica gli URL/nomi file delle immagini, configurare **redirect lato server**.

## 2024-09 — Google Trends Tutorials su YouTube (12 set 2024)
Fonte: https://developers.google.com/search/blog/2024/09/google-trends-tutorials?hl=it
- Nuova serie YouTube sull'uso di Google Trends (tendenze locali e globali, interesse di ricerca su Google e YouTube, "Trending Now" aggiornato con più tendenze/paesi, operatori di ricerca avanzati e filtri di confronto). Utile per strategia contenuti. Nessuna modifica tecnica.

## 2024-09 — Nuove esperienze della Ricerca in Sudafrica: badge e chip di perfezionamento (16 set 2024)
Fonte: https://developers.google.com/search/blog/2024/09/search-experiences-in-sa?hl=it
- Badge "Sudafrica" e chip di perfezionamento per piattaforme sudafricane idonee (viaggi, acquisti, poi noleggio auto, autobus, consegna cibo — agg. 21/01/2026). Il badge **non modifica il ranking**; nessun markup richiesto. Agg. 28/08/2025: dati strutturati per caroselli (beta) disponibili anche in Sudafrica. Non pertinente per siti italiani.

## 2024-10 — Introduzione delle valutazioni negozio nella Ricerca in altri paesi (9 ott 2024)
Fonte: https://developers.google.com/search/blog/2024/10/store-ratings?hl=it
- Valutazioni negozio (store ratings) estese a ricerche di shopping in inglese in Australia, Canada, India, Regno Unito (prima USA). Partecipazione: programma gratuito Recensioni dei clienti Google o recensioni su siti indipendenti. Solo e-commerce.

## 2024-10 — È terminata Search Central Live a Giacarta e Bangkok 2024 (recap, 15 ott 2024)
Fonte: https://developers.google.com/search/blog/2024/10/scl-2024-jkt-bkk?hl=it
- Recap eventi (335 e 310 partecipanti); temi: funzionamento Ricerca, qualità e aggiornamenti, AI e Ricerca, analisi cali di traffico con GSC, siti multilingue, Google Trends per SEO. Lightning talk community (tra cui "sopravvivere nell'era AI Overview", markup VideoObject). Feedback: più Q&A, più contenuti tecnici. Nessuna novità tecnica ufficiale.

## 2024-10 — Addio alla casella di ricerca dei sitelink (21 ott 2024)
Fonte: https://developers.google.com/search/blog/2024/10/sitelinks-search-box?hl=it
- **[DEPRECATO]** La **sitelinks search box** viene rimossa dai risultati **dal 21 novembre 2024**, a livello globale, in tutte le lingue e paesi, per calo di utilizzo.
- Non influisce sul ranking né sugli altri sitelink; non elencata nella Status Dashboard.
- Rimossi il relativo report "risultati avanzati" in GSC e l'evidenziazione nel Test dei risultati avanzati.
- Il markup `WebSite` + `potentialAction`/`SearchAction` **può essere rimosso ma non è necessario**: i dati strutturati non supportati non causano problemi né errori in GSC.
- Attenzione: i **nomi dei siti (site names)** usano una variante dei dati strutturati `WebSite`, **che resta supportata** → non rimuovere il blocco `WebSite` usato per il nome del sito.

## 2024-11 — Aggiornamento delle norme relative all'abuso della reputazione del sito (19 nov 2024)
Fonte: https://developers.google.com/search/blog/2024/11/site-reputation-abuse?hl=it
- **[SPAM] Aggiorna/irrigidisce la norma di marzo 2024**: dopo casi con white-label, licenze, proprietà parziale, Google chiarisce che **nessun livello di coinvolgimento/supervisione del sito host** cambia la natura di terze parti dei contenuti. Nuovo testo (in vigore dal 19/11/2024): *l'abuso della reputazione del sito è la pratica di pubblicare pagine di terze parti su un sito nel tentativo di manipolare i ranking sfruttando gli indicatori di ranking del sito host.* → **Supera** la formulazione di marzo 2024 che faceva riferimento a contenuti pubblicati "con supervisione minima o nulla".
- Google valuta molti fattori e non si fida delle dichiarazioni del sito su come sono prodotti i contenuti. Azioni manuali via GSC + riconsiderazione.
- **Sezioni molto diverse dal sito principale** possono essere trattate **come siti autonomi** (non beneficiano più degli indicatori a livello di sito): possibile calo di traffico senza che sia una penalizzazione.
- FAQ: contenuti di terze parti = creati da entità distinte (utenti, freelance, white-label…). Non sono violazione di per sé; i contenuti di **freelance** non violano di per sé; **affiliazione** non è target se i link sono qualificati correttamente (attributi `rel` per link in uscita).
- `noindex` non rimuove automaticamente l'azione manuale: occorre rispondere in GSC. Spostare i contenuti in sottocartella/sottodominio dello stesso sito **non** risolve (può essere visto come elusione); spostarli su un altro sito affermato può spostare il problema lì; su un nuovo dominio senza reputazione in genere non è un problema. **Non reindirizzare** dal vecchio al nuovo sito; eventuali link dal vecchio sito → `nofollow`. Serve comunque richiesta di riconsiderazione.
- Aggiornamenti: 06/12/2024 FAQ aggiunte; 21/01/2025 testo delle norme e doc del report Azioni manuali allineati alle FAQ (nessuna modifica sostanziale).

## 2024-11 — Search Central Live Zurigo (annuncio evento)
Fonte: https://developers.google.com/search/blog/2024/11/search-central-live-zurich?hl=it
- 12 dicembre 2024 presso Google Zurigo, lightning talk di 15 minuti della community. Nessun contenuto tecnico.

## 2024-12 — Dicembre dedicato alla scansione: come e perché Googlebot esegue il crawling (3 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/crawling-december-resources?hl=it
- Flusso: Googlebot scarica l'HTML → lo passa al **Web Rendering Service (WRS)** → WRS, tramite Googlebot, scarica le risorse referenziate (JS, CSS, immagini…) → costruisce la pagina come un browser. Tra i passaggi possono passare tempi lunghi (vincoli di pianificazione/carico server).
- La scansione delle risorse di rendering **consuma il crawl budget dell'host che le ospita**.
- **WRS mette in cache JS e CSS fino a 30 giorni, ignorando le direttive HTTP di cache.**
- Consigli: usare **il minor numero di risorse possibile**; usare **con cautela i parametri di cache-busting** (se l'URL della risorsa cambia, Google deve riscaricarla anche se il contenuto è identico); ospitare risorse su host diverso (CDN/sottodominio) sposta il carico — ma **aggiornamento 6/12/2024: sconsigliato per risorse critiche (JS/CSS necessari al rendering)** per l'overhead di connessione (impatto su LCP); ok per risorse non critiche grandi (video, download).
- Vale anche per media (`Googlebot-Image`, `Googlebot-Video`).
- **Non bloccare in robots.txt le risorse necessarie al rendering**: se WRS non può recuperare una risorsa critica, Google può non estrarre il contenuto.
- Analisi: fonte migliore = **log di accesso grezzi** (identificare Googlebot con gli intervalli IP pubblicati); seconda = report **Statistiche di scansione** di GSC (per tipo di risorsa e crawler).

## 2024-12 — Dicembre dedicato alla scansione: memorizzazione nella cache HTTP (9 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/crawling-december-caching?hl=it
- Le risposte memorizzabili in cache sono calate (0,026% dei recuperi 10 anni fa → 0,017% oggi).
- I crawler Google supportano caching HTTP standard (RFC 9111): **`ETag` / `If-None-Match`** e **`Last-Modified` / `If-Modified-Since`**. Consigliato **`ETag`** (meno soggetto a errori); se possibile **entrambi**.
- Se il valore corrisponde, il server deve rispondere **`304 Not Modified` senza body** (risparmio calcolo e banda).
- `ETag`: qualsiasi stringa ASCII univoca per rappresentazione (hash/versione); versioni diverse sullo stesso URL (es. mobile/desktop) → ETag diversi.
- `Last-Modified`: formato data HTTP, es. `Fri, 4 Sep 1998 19:15:56 GMT`; consigliato anche `Cache-Control: max-age=<secondi>` per indicare quando ricontrollare.
- Invalidare la cache solo per modifiche significative (non per l'anno del copyright nel footer).
- Particolarmente utile per siti grandi con contenuti che cambiano raramente. Chiedere a hosting/CMS/sviluppatori di attivarlo.

## 2024-12 — Un modo migliore per visualizzare i dati sul rendimento recenti in Search Console (12 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/recent-data-search-console?hl=it
- **[GSC][NUOVO]** Vista **"24 ore"** nei report Rendimento (Ricerca, Discover/Feed personalizzato, Google News): ultime 24 ore disponibili con ritardo di poche ore, **granularità oraria**, dati parziali indicati con linea tratteggiata, fuso orario locale del browser.
- Ritardo medio dei dati di rendimento **quasi dimezzato**. Rollout graduale.
- Utile per monitorare contenuti appena pubblicati.

## 2024-12 — Riepilogo di Search Central Live Kuala Lumpur e Taipei 2024 (13 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/scl-asia-h2-recap?hl=it
- Recap (600+ partecipanti): sessioni "Come funziona la Ricerca" approfondite, AI nella Ricerca, "miti da sfatare" (parole chiave in eccesso, strategie di backlink, tattiche discutibili, siti multilingue, scansione). Nessuna novità tecnica.

## 2024-12 — Dicembre dedicato alla scansione: navigazione per facet (17 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/crawling-december-faceted-nav?hl=it
- Nuovo documento di best practice sulla **faceted navigation** (sostituisce post 2014). È **la fonte più comune di over-crawling**: combinazioni infinite di filtri → scansione eccessiva e scoperta lenta dei contenuti nuovi.
- **Se non servono indicizzati**: bloccarli con **robots.txt**, oppure usare **frammenti URL (`#`)** per i filtri (in genere ignorati dai motori).
- **Se si vogliono scansionati**: separatore `&` standard; ordine dei filtri coerente; **404 per combinazioni senza risultati**; evitare redirect dei risultati vuoti a una pagina generica "non trovato" — salvo non ci siano alternative (es. **app a pagina singola / SPA**).
- `rel="canonical"` aiuta a consolidare (richiede tempo); `rel="nofollow"` sui link dei filtri funziona solo se applicato **a tutti** i link (interni ed esterni). La scansione dei facet consuma sempre risorse server.

## 2024-12 — Dicembre dedicato alla scansione: CDN e scansione (24 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/crawling-december-cdns?hl=it
- Benefici CDN: cache (meno carico, pagine più veloci), protezione da flood/DDoS, affidabilità (servire contenuti statici anche con origine giù).
- **Crawl rate**: Google rileva la CDN dall'IP e consente **frequenze di scansione più alte**. Ma al primo accesso la cache è "fredda": l'origine deve servire ogni URL almeno una volta (attenzione nei lanci di molti URL contemporaneamente).
- **Rendering**: risorse su hostname separato (`cdn.example.com`) aiutano il WRS ma costano overhead di connessione (page experience); alternativa: mettere l'host principale dietro CDN. Google supporta entrambe.
- **Quando la CDN è troppo protettiva (WAF)**:
  - *Blocchi rigidi*: **503/429 = modo migliore** per segnalare blocco temporaneo; **timeout di rete** → URL rimossi dall'indice (errori "irreparabili") e riduzione della frequenza di scansione; **messaggio d'errore con HTTP 200 (soft error)** → rimozione o deduplicazione come duplicati (recupero lento).
  - *Blocchi flessibili*: interstitial di verifica "sei una persona?" → i crawler vedono solo quello; servire **503** ai client automatici.
- Debug: **Controllo URL di GSC** (screenshot renderizzato: pagina vuota/errore/verifica bot = problema CDN). Usare gli IP pubblicati dei crawler per sbloccarli/allowlist nel WAF; controllare periodicamente le blocklist (gli IP possono finirci automaticamente). Link a doc bot management di Cloudflare, Akamai, Fastly, F5, Google Cloud Armor.

## 2024-12 — Fine del mese di dicembre dedicato alla scansione: riepilogo del 2024 (31 dic 2024)
Fonte: https://developers.google.com/search/blog/2024/12/crawling-out-of-december?hl=it
- Recap 2024: 10 eventi SCL; temi più richiesti: come funziona la Ricerca, Shopping, AI e Ricerca. Documentazione sui crawler ampliata anche a seguito del **workshop IAB AI Control**. Elenco dei 4 post "Crawling December" (consigliati soprattutto ai siti grandi). Nessuna novità ulteriore.

## 2025-01 — Search Central Live torna in Brasile nel 2025 (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/01/search-central-live-brazil?hl=it
- San Paolo 18/02/2025 e Recife 20/02/2025; temi: come funziona la Ricerca e gli update, AI nella Ricerca, misurare la SEO con Search Console e Google Analytics. Nessun contenuto tecnico.

## 2025-01 — Semplificare l'elemento URL visibile nei risultati di ricerca mobile (23 gen 2025)
Fonte: https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs?hl=it
- **[DEPRECATO parziale]** Dal 23/01/2025 i **breadcrumb non vengono più mostrati nei risultati di ricerca su mobile** (tutte le lingue e regioni): su mobile l'URL visibile mostra **solo il dominio**. Su **desktop** restano dominio + breadcrumb.
- Il markup `BreadcrumbList` **resta supportato** (per desktop): nessuna azione richiesta; il report breadcrumb in GSC e il Test dei risultati avanzati restano disponibili.

## 2025-02 — Search Central Live arriva a New York (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/02/search-central-live-nyc?hl=it
- 20 marzo 2025; temi: priorità del team, come funziona la Ricerca e miti SEO, novità Search Console. Nessun contenuto tecnico.

## 2025-02 — Ripasso su robots: presentazione di una nuova serie (24 feb 2025)
Fonte: https://developers.google.com/search/blog/2025/02/intro-robots-refresher?hl=it
- `robots.txt` = file di testo su `/robots.txt` che indica ai crawler quali parti del sito possono essere scansionate; quasi tutti i siti ne hanno uno, spesso generato dal CMS. Esiste dal 1994; **standard IETF (RFC 9309) dal 2022**.
- È estendibile: es. direttiva `Sitemap` (2007); nuovi **user-agent** vengono regolarmente aggiunti dagli operatori, **inclusi quelli usati per scopi di AI**.
- La maggior parte degli operatori commerciali di crawler lo rispetta.

## 2025-03 — Primo Search Central Live in Sudafrica (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/03/first-search-central-live-in-south-africa?hl=it
- Johannesburg, 2 aprile 2025. Nessun contenuto tecnico.

## 2025-03 — Search Central Live va a Madrid (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/03/search-central-live-madrid?hl=it
- 9 aprile 2025, Google Campus Madrid; temi: best practice SEO, Search Console e Google Trends, Google News. Nessun contenuto tecnico.

## 2025-03 — Ripasso su robots: robots.txt, un modo flessibile per controllare l'esplorazione del sito (7 mar 2025)
Fonte: https://developers.google.com/search/blog/2025/03/robotstxt-flexible-way-to-control?hl=it
- File vuoto o assente = tutto scansionabile. Esempi di regole:
  - più user-agent nello stesso gruppo (`user-agent: examplebot` + `user-agent: otherbot` → `disallow: /search`);
  - pattern (`disallow: *.pdf`);
  - `allow: /blog/` + `disallow: /blog/drafts/`;
  - **bloccare un crawler AI di training lasciando passare i motori di ricerca**: `user-agent: *` `allow: /` + `user-agent: aicorp-trainer-bot` `disallow: /` `allow: /$` (solo home);
  - commenti con `#`.
- Usi: problemi tecnici (es. paginazione non necessaria), motivi redazionali/personali.
- Molti CMS permettono di modificarlo da UI/plugin. Test: strumenti community (TametheBots robots.txt checker, realrobotstxt.com) basati sul **parser open source di Google**.

## 2025-03 — Ripasso su robots: granularità a livello di pagina (14 mar 2025)
Fonte: https://developers.google.com/search/blog/2025/03/robots-refresher-page-level?hl=it
- **Meta tag robots** (1996) e intestazione HTTP **`X-Robots-Tag`** (per contenuti non HTML: PDF, documenti, immagini). Insieme a robots.txt formano il **REP**.
- **Le istruzioni a livello di pagina vengono lette solo se l'URL non è bloccato da robots.txt** (un `noindex` su pagina bloccata in robots.txt non viene visto).
- Esempi: `<meta name="robots" content="noindex">` / `X-Robots-Tag: noindex`; `nosnippet`; regole per un singolo crawler (`<meta name="examplebot-news" content="noindex">`, `X-Robots-Tag: examplebot-news: noindex`); **si applica la combinazione più restrittiva** delle istruzioni valide.
- Verifica: sorgente pagina / DevTools Elements (meta), DevTools Network (header).
- Scelta del meccanismo: robots.txt per bloccare la **scansione** di ampie sezioni (es. risultati di ricerca infiniti, FTP); controlli a livello di pagina per **indicizzazione/snippet** di singole pagine (lo snippet si controlla solo a livello di pagina).
- Valori storici: `noindex`, `nofollow`, poi `nosnippet`, `noarchive`, `max-snippet:`; **`noodp` ritirato** (DMOZ chiuso).

## 2025-03 — Preparati a Search Central Live Asia Pacifico 2025 (17 mar 2025)
Fonte: https://developers.google.com/search/blog/2025/03/search-central-live-deep-dive-apac-2025?hl=it
- Annuncio del nuovo formato **SCL Deep Dive** (più giorni, sessioni tecniche: meta robots, workshop robots.txt, rendering ed errori comuni, indicizzazione con paginazione/scroll/navigazione, AI e automazione SEO, workshop GSC e Google Trends). Nessuna novità tecnica.

## 2025-03 — Ripasso su robots: un protocollo di esclusione robot a prova di futuro (28 mar 2025)
Fonte: https://developers.google.com/search/blog/2025/03/robots-future?hl=it
- REP standardizzato come **RFC 9309** (2022). Unica regola aggiunta universalmente nel tempo: `allow`.
- Regole non standard: **`crawl-delay` e `clean-param` NON sono supportate da Google** (lo sono da altri motori). **`sitemap`** non è nell'RFC ma è supportata da tutti i principali motori.
- Google ha reso open source il proprio parser robots.txt. REP (robots.txt, `X-Robots-Tag`, meta robots) è estendibile per nuove preferenze di opt-out (contesto AI): le modifiche richiedono consenso pubblico, nessuna entità può cambiarlo unilateralmente.

## 2025-04 — L'API Search Analytics ora supporta i dati orari (9 apr 2025)
Fonte: https://developers.google.com/search/blog/2025/04/san-hourly-data?hl=it
- **[GSC][NUOVO]** API Search Analytics: nuova dimensione **`HOUR`** e nuovo `dataState` **`HOURLY_ALL`** (dati orari, possibilmente parziali). L'API restituisce dati orari **fino a 10 giorni** (la UI solo ultime 24 ore) → confronti con lo stesso giorno della settimana precedente.
- Esempio richiesta: `{"startDate":"2025-04-07","endDate":"2025-04-07","dataState":"HOURLY_ALL","dimensions":["HOUR"]}`.

## 2025-04 — Iscrivetevi ora a Search Central Live Deep Dive 2025 (29 apr 2025)
Fonte: https://developers.google.com/search/blog/2025/04/search-central-live-deep-dive-2025?hl=it
- Primo SCL Deep Dive, Bangkok 23–25 luglio 2025 (giorno 1: ricerca e sistemi AI, scansione con GSC; giorno 2: indicizzazione anche non testuale, e-commerce, internazionalizzazione; giorno 3: ranking, funzionalità, diagnosi rendimento in GSC, Google Trends). Nessuna novità tecnica.

## 2025-05 — Link diretti delle app: collega il tuo sito web e la tua app (2 mag 2025)
Fonte: https://developers.google.com/search/blog/2025/05/app-deep-links?hl=it
- Deep link: Android **App Links** (associazione nel manifest) e iOS **Universal Links** (file `apple-app-site-association`); entrambi supportati da Google Search.
- **Indicizzazione e ranking continuano a usare i contenuti della pagina web**; aggiungere deep link solo se la pagina dell'app ha **gli stessi contenuti** della pagina web (layout/UX diversi ok), altrimenti titolo/snippet sarebbero ingannevoli.
- GSC: report Rendimento con filtro "Aspetto nella ricerca" per **app Android**. Strumenti: Play Console (Deep links), Android Studio App Links Assistant, debug Universal Links Apple.
- Pertinenza: solo se il sito ha un'app nativa.

## 2025-05 — I modi migliori per avere un buon rendimento nelle esperienze di Google AI sulla Ricerca (21 mag 2025)
Fonte: https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search?hl=it
- Riguarda **AI Overviews (panoramiche AI) e la nuova AI Mode**. Principio: **gli stessi fondamentali SEO valgono per le esperienze AI**; non esistono requisiti speciali.
- Indicazioni:
  1. **Contenuti unici, non generici, di valore per le persone** (gli utenti AI fanno domande più lunghe/specifiche e follow-up). Autovalutazione con la guida "contenuti utili, affidabili, people-first".
  2. **Buona esperienza sulle pagine**: rendering corretto su più dispositivi, latenza, contenuto principale distinguibile.
  3. **Accessibilità tecnica**: Googlebot non bloccato, HTTP **200**, contenuto indicizzabile (requisiti tecnici della Ricerca valgono anche per i formati AI).
  4. **Controlli di anteprima**: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` limitano anche la presenza nelle esperienze AI.
  5. **Dati strutturati coerenti con i contenuti visibili**, seguire le linee guida, convalidare il markup.
  6. **Multimodalità**: affiancare al testo **immagini e video di alta qualità**; mantenere aggiornati Merchant Center e il **Profilo dell'attività** (Google Business Profile).
  7. **Valore delle visite**: i clic da pagine con AI Overviews sarebbero "di qualità superiore" (più tempo sul sito); misurare **conversioni** (vendite, registrazioni, coinvolgimento, ricerche sull'attività), non solo i clic.
  8. Evolvere con gli utenti: AI Overviews mostrano una gamma più ampia di fonti/link.
- Nuove pagine di doc: "Funzionalità di AI e il tuo sito" (`/search/docs/appearance/ai-features`) e "Indicazioni sull'uso di contenuti creati con l'AI generativa" (`/search/docs/fundamentals/using-gen-ai-content`).

## 2025-06 — Aggiunta del supporto del markup per i programmi fedeltà (10 giu 2025)
Fonte: https://developers.google.com/search/blog/2025/06/loyalty-program?hl=it
- **[NUOVO]** Programma fedeltà definibile nei dati strutturati `Organization` + vantaggi (prezzi per membri, punti) nei dati strutturati `Product` → idoneità a mostrare i vantaggi nei risultati prodotto. Senza Merchant Center usare il markup; con Merchant Center definirlo lì. Test con Rich Results Test. Solo e-commerce.

## 2025-06 — Semplificazione della pagina dei risultati di ricerca (12 giu 2025)
Fonte: https://developers.google.com/search/blog/2025/06/simplifying-search-results?hl=it
- **[DEPRECATO]** Ritiro graduale (settimane/mesi) del supporto nei risultati Google per questi dati strutturati poco usati: **Azioni relative ai libri (Book actions), Informazioni sui corsi (Course info), Verifica delle dichiarazioni (ClaimReview/Fact check), Stipendio stimato (Estimated salary), Video didattico (Learning video), Comunicazione speciale (SpecialAnnouncement), Scheda di veicoli (Vehicle listing)**.
- **Nessun impatto sul ranking**; l'uso di questi markup fuori da Google Search non è interessato.
- Aggiornamento 08/09/2025: dal **9 settembre 2025** rimossi dai report risultati avanzati di GSC, dal Rich Results Test e dai filtri "Aspetto nella ricerca" (Course info, Fact check, Estimated salary, Learning video, Special announcement, Vehicle listing); API GSC li supporta fino a **dicembre 2025**; nell'**export collettivo BigQuery** i campi ritirati diventano `NULL` dal 1/10/2025 → usare `IS NOT TRUE` invece di `NOT campo` nelle query.
- Rilevante per la professionista: il markup **Course info** non produce più risultati avanzati (se offre corsi/workshop, non contare su questo rich result).

## 2025-06 — SCL Deep Dive APAC 2025: relatori della community e un nuovo formato (23 giu 2025)
Fonte: https://developers.google.com/search/blog/2025/06/scl-dd-apac-2025-news?hl=it
- Introduzione delle **poster session** e presentazione di 31 relatori della community. Nessun contenuto tecnico.

## 2025-06 — È disponibile il nuovo report Approfondimenti (Insights) di Search Console (30 giu 2025)
Fonte: https://developers.google.com/search/blog/2025/06/search-console-insights?hl=it
- **[GSC][NUOVO]** **Search Console Insights** integrato nell'interfaccia principale di GSC (sostituisce la beta autonoma). Pensato per creator e piccoli proprietari non esperti di dati.
- Mostra: clic e impressioni totali vs periodo precedente; pagine top, **in tendenza** e **in calo**; query principali, **in aumento** (idee per contenuti) e in calo; **Obiettivi** (traguardi di clic sugli ultimi 28 giorni, con email). Rollout graduale.

## 2025-07 — Presentazione dell'API Google Trends (alpha) (24 lug 2025)
Fonte: https://developers.google.com/search/blog/2025/07/trends-api?hl=it
- **[NUOVO]** API Google Trends in **alpha** per un numero limitato di tester (candidatura). Dati di interesse di ricerca **scalati in modo coerente tra richieste** (non 0–100 per richiesta come sul sito; non numeri assoluti) → confronti di decine di termini (sito: max 5). Finestra mobile **1800 giorni (~5 anni)**, dati aggiornati a 2 giorni prima, aggregazioni giornaliere/settimanali/mensili/annuali, suddivisioni per regione/sottoregione (ISO 3166-2). Usi: strategia contenuti, prioritizzazione SEO.

## 2025-08 — Search Central Live torna a Città del Messico (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/08/search-central-live-mexico-2025?hl=it
- 25 settembre 2025. Nessun contenuto tecnico.

## 2025-09 — Search Central Live Hong Kong 2025 (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/09/scl-hkk?hl=it
- 31 ottobre 2025, in cinese, focus e-commerce internazionale, internazionalizzazione e localizzazione. Nessun contenuto tecnico.

## 2025-09 — Search Central Live Tokyo: il ritorno nel 2025 (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/09/scl-tok?hl=it
- 7 novembre 2025, Google Japan Shibuya, lightning talk. Nessun contenuto tecnico.

## 2025-09 — Annuncio del widget del negozio (18 set 2025)
Fonte: https://developers.google.com/search/blog/2025/09/store-widget?hl=it
- **[NUOVO]** Widget del negozio "basato su Google" incorporabile in qualsiasi pagina del sito del commerciante: mostra valutazione negozio, spedizione/resi, recensioni; tre livelli (Negozio di alta qualità / Valutazione negozio / generico). Dichiarato aumento vendite fino all'8% in 90 giorni. Solo e-commerce con Merchant Center.

## 2025-09 — Search Central Live Dubai 2025 (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/09/scl-dubai?hl=it
- 21 ottobre 2025; temi: scansione, indicizzazione e AI, aggiornamenti Ricerca e Discover, Search Console e Trends. Nessun contenuto tecnico.

## 2025-10 — Introduzione dei gruppi di query in Search Console Insights (27 ott 2025)
Fonte: https://developers.google.com/search/blog/2025/10/search-console-query-groups?hl=it
- **[GSC][NUOVO]** **Gruppi di query** nella scheda "Query che portano al tuo sito" del report Approfondimenti: raggruppamento **tramite AI** di query simili (varianti, refusi, lingue) per intento; mostra clic del gruppo, elenco query (troncabile), drill-down nel report Rendimento; viste Principali / In aumento / In calo. I gruppi possono cambiare nel tempo; **non influiscono sul ranking**.
- **Disponibile solo per proprietà con volume elevato di query** (probabilmente non per siti piccoli come un portfolio).

## 2025-11 — Aggiornamento sulle iniziative per semplificare la pagina dei risultati (5 nov 2025)
Fonte: https://developers.google.com/search/blog/2025/11/update-on-our-efforts?hl=it
- **[DEPRECATO]** Prosegue la rimozione graduale di funzionalità della SERP poco usate (senza elencarle nel post); aggiornamenti specifici nel **changelog della documentazione** (`/search/updates`). **Da gennaio 2026** rimozione del supporto per i tipi di dati strutturati interessati in Search Console e nella relativa API.
- Implicazione: prima di consigliare un markup per rich result, verificare nella documentazione/changelog attuale che sia ancora supportato.

## 2025-11 — Search Central Live torna a Zurigo (annuncio evento)
Fonte: https://developers.google.com/search/blog/2025/11/search-central-live-zurich-is-back?hl=it
- 9 dicembre 2025; lightning talk di 10 minuti. Nessun contenuto tecnico.

## 2025-11 — Altri modi per condividere le norme su spedizione e resi con Google (12 nov 2025)
Fonte: https://developers.google.com/search/blog/2025/11/more-ways-to-share-shipping?hl=it
- **[GSC][NUOVO]** "Spedizione e resi" nelle impostazioni GSC disponibile per **tutti i siti identificati come commercianti online**, anche **senza Merchant Center** (prima solo con Merchant Center). Le impostazioni GSC **prevalgono sui dati strutturati**. Rollout tutti i paesi/lingue.
- **[NUOVO]** Dati strutturati **norme di spedizione a livello di organizzazione** (`shippingPolicy` nidificato in `Organization`), da mettere nella pagina che descrive le norme di spedizione; le norme a livello di prodotto **hanno priorità** su quelle di organizzazione. Ribadito: usare sottotipi `OnlineStore` o `LocalBusiness`.
- Visibilità in knowledge panel, profili del brand, risultati prodotto. Solo e-commerce.

## 2025-11 — Annotazioni personalizzate nei grafici di Search Console (17 nov 2025)
Fonte: https://developers.google.com/search/blog/2025/11/custom-chart-annotations?hl=it
- **[GSC][NUOVO]** **Annotazioni personalizzate** sui grafici del report Rendimento: clic destro → "Aggiungi annotazione", nota fino a **120 caratteri** con data. Usi: migrazioni, aggiornamento template, nuovi plugin, ingaggio agenzia, cambi di contenuto/intento, festività. **Visibili a chiunque abbia accesso alla proprietà** → niente dati personali sensibili.

## 2025-11 — Presentazione del filtro per le query con brand in Search Console (20 nov 2025)
Fonte: https://developers.google.com/search/blog/2025/11/search-console-branded-filter?hl=it
- **[GSC][NUOVO]** Filtro **Con brand / Non correlate al brand** nel report Rendimento (web, immagini, video, notizie) + scheda nel report Approfondimenti con la ripartizione dei clic.
- Query con brand = nome del brand, varianti/refusi, prodotti/servizi unici del brand. Classificazione con **sistema interno assistito da AI** (non regex), multilingue; possibili errori; **nessun effetto sul ranking**.
- Disponibile solo per **proprietà di primo livello** (non proprietà con prefisso percorso né sottodominio) e con volume sufficiente. Aggiornamento 11/03/2026: disponibile per tutti i siti idonei.
- Rilevante per personal brand: il nome della persona è il "brand" → misurare quanto traffico arriva da ricerche del nome vs query non di brand (es. "sviluppatore Angular freelance", "orientamento professionale [città]").

## 2025-12 — Configurazione basata sull'AI nel report Rendimento di Search Console (4 dic 2025)
Fonte: https://developers.google.com/search/blog/2025/12/ai-powered-configuration?hl=it
- **[GSC][NUOVO, sperimentale]** Descrivere in **linguaggio naturale** l'analisi desiderata: l'AI imposta filtri (query, pagina, paese, dispositivo, aspetto nella ricerca, date), confronti e metriche (clic, impressioni, CTR, posizione). Solo report Rendimento dei risultati di Ricerca (non Discover/News); può fraintendere → verificare i filtri; non ordina né esporta. Rollout limitato.

## 2025-12 — Introduzione dei canali social in Search Console (8 dic 2025)
Fonte: https://developers.google.com/search/blog/2025/12/social-channels-search-console?hl=it
- **[GSC][NUOVO, esperimento]** Il report **Insights** include il rendimento nella Ricerca Google dei **canali social associati al sito** (identificati automaticamente da GSC): clic/impressioni, pagine del canale top/in aumento/in calo, query, paesi, sorgenti aggiuntive. Rollout limitato; GSC propone di aggiungere i canali identificati.
- Rilevante per personal brand. **Superato** dalle "proprietà della piattaforma" di luglio 2026, che però supportano solo Instagram, TikTok, X e YouTube (non LinkedIn né GitHub).

## 2025-12 — Visualizzazioni settimanali e mensili in Search Console (10 dic 2025)
Fonte: https://developers.google.com/search/blog/2025/12/weekly-monthly-views-search-console?hl=it
- **[GSC][NUOVO]** Selettore di granularità **Giornaliera / Settimanale / Mensile** nei grafici del report Rendimento (Ricerca, News, Discover): utile per tendenze e confronti tra periodi. Cambia leggermente la struttura dei file di **esportazione** (nomi file/schede, intestazioni, ordinamento). Rollout globale.

## 2025-12 — Riepilogo di Search Central Live APAC 2025 (31 dic 2025)
Fonte: https://developers.google.com/search/blog/2025/12/scl-eoy?hl=it
- Recap Deep Dive Bangkok (2500+ interessati), Hong Kong (hreflang e siti transfrontalieri), Tokyo (domande su **rendering e indicizzazione di siti JavaScript complessi**). Nella sessione "miti SEO" citato il **meta tag keywords** (mito). Interesse prioritario della community per l'AI (Gemini, AI Overviews, generazione contenuti); talk della community su GEO/LLMO, SEO per siti JS. Nessuna novità ufficiale.

## 2026-01 — Search Central Live torna in Sud America (annuncio evento)
Fonte: https://developers.google.com/search/blog/2026/01/search-central-live-brasil-argentina?hl=it
- San Paolo 24/02/2026 e Buenos Aires 26/02/2026; temi: come funziona la Ricerca e gli update, AI nella Ricerca, novità Search Console e Trends, Chrome e strumenti AI. Nessun contenuto tecnico.

## 2026-02 — Aggiornamento principale di Discover (Feed personalizzato) di febbraio 2026 (5 feb 2026)
Fonte: https://developers.google.com/search/blog/2026/02/discover-core-update?hl=it
- **[NUOVO]** Primo **core update dedicato a Discover** ("Feed personalizzato"). Effetti: più contenuti **rilevanti a livello locale da siti con sede nel paese dell'utente**; meno contenuti **sensazionalistici/clickbait**; più contenuti **approfonditi, originali, aggiornati da siti con competenza specifica** su un argomento.
- La competenza è valutata **per argomento**: un sito multi-tema con una sezione consolidata su un tema (es. giardinaggio) può avere competenza su quel tema; un sito con un solo articolo isolato su un tema no.
- Personalizzazione per preferenze di creator/fonti invariata. Possibili fluttuazioni. Rollout: inglese USA, poi tutti i paesi/lingue nei mesi successivi. Riferimenti: linee guida core update e pagina "come apparire su Discover".

## 2026-03 — Search Central Live arriva in Canada (annuncio evento)
Fonte: https://developers.google.com/search/blog/2026/03/scl-canada-2026?hl=it
- Toronto, 21 aprile 2026; temi: scansione, indicizzazione e AI, aggiornamenti recenti, dati strutturati e-commerce, Search Console e Trends. Nessun contenuto tecnico.

## 2026-03 — Search Central Live Asia Pacifico 2026 (annuncio eventi)
Fonte: https://developers.google.com/search/blog/2026/03/scl-apac-2026?hl=it
- Sydney 22/05/2026, Shanghai ~15/05/2026, India Q4 2026; Deep Dive spostato in EMEA nel 2026 ("non è cambiato molto nella Ricerca", contenuti in gran parte uguali al 2025). Nessun contenuto tecnico.

## 2026-03 — Dietro le quinte di Googlebot: scansione, recupero e byte elaborati (31 mar 2026)
Fonte: https://developers.google.com/search/blog/2026/03/crawler-blog-post?hl=it
- **Googlebot non è un singolo programma**: è uno dei client di una **piattaforma di scansione centralizzata** usata anche da Google Shopping, AdSense ecc. con nomi di crawler diversi; documentati sul sito dell'**infrastruttura dei crawler di Google** (`developers.google.com/crawling/...`).
- **Limiti di byte**:
  - **Googlebot (Ricerca) recupera fino a 2 MB per URL** (incluse le intestazioni HTTP); **PDF: 64 MB**; crawler immagini/video: soglie variabili per prodotto; altri crawler senza limite specificato: **15 MB** di default.
  - Oltre i 2 MB il recupero si **interrompe**: la parte scaricata viene passata a indicizzazione e WRS **come se fosse il file completo**; i byte successivi sono **ignorati** (non recuperati, non renderizzati, non indicizzati).
  - Ogni risorsa referenziata (JS, CSS, XHR; esclusi media, font e alcuni file "esotici") viene recuperata da WRS con un **contatore di byte separato** e lo stesso limite di 2 MB per risorsa.
- Rischi: immagini **base64 inline** grandi, enormi blocchi di **CSS/JS inline**, megabyte di menu prima del contenuto → contenuto testuale o dati strutturati oltre la soglia non esistono per Google.
- **WRS** esegue JS come un browser moderno (JS, CSS, richieste XHR; non immagini/video), può eseguire solo il codice effettivamente recuperato, ed è **stateless: cancella localStorage e dati di sessione tra le richieste**.
- Best practice: **HTML snello** (CSS/JS pesanti in file esterni); **ordine**: mettere meta tag, `<title>`, `<link>`, **canonical** e **dati strutturati essenziali in alto** nell'HTML; monitorare i tempi di risposta nei log (server lento → Google riduce la frequenza di scansione). Il limite può cambiare nel tempo.

## 2026-03 — Nuova posizione per i file degli intervalli IP dei crawler di Google (31 mar 2026)
Fonte: https://developers.google.com/search/blog/2026/03/crawler-ip-ranges?hl=it
- **[DEPRECATO/SPOSTATO]** I JSON con gli intervalli IP passano da `developers.google.com/search/apis/ipranges/` a **`developers.google.com/crawling/ipranges/`** (valgono per più crawler, non solo Ricerca). Vecchio percorso disponibile temporaneamente; **entro 6 mesi (cioè entro ~fine settembre 2026)** eliminato e reindirizzato. Aggiornare allowlist WAF/CDN, script di verifica Googlebot, analisi log.

## 2026-04 — Search Central Live Shanghai 2026 (annuncio evento)
Fonte: https://developers.google.com/search/blog/2026/04/scl-shanghai-2026?hl=it
- 15 maggio 2026, in mandarino, focus su siti rivolti a utenti fuori dalla Cina. Nessun contenuto tecnico.

## 2026-04 — Nuove norme antispam per la "compromissione del pulsante Indietro" (back button hijacking) (13 apr 2026)
Fonte: https://developers.google.com/search/blog/2026/04/back-button-hijacking?hl=it
- **[SPAM][NUOVO]** La **compromissione del pulsante Indietro** diventa violazione esplicita della norma sulle **"pratiche dannose"** (malicious practices). **In vigore dal 15 giugno 2026.**
- Definizione: il sito interferisce con la navigazione del browser impedendo all'utente di tornare **immediatamente** alla pagina di provenienza con "Indietro" (es. reindirizza a pagine mai visitate, mostra consigli/annunci non richiesti, blocca la navigazione). Inserire pagine ingannevoli nella **cronologia del browser** era già contrario alle "Nozioni di base sulla Ricerca Google" (2013).
- Conseguenze: **azioni manuali** antispam o **retrocessioni automatiche**.
- Cosa fare: rimuovere/disattivare script o tecniche che inseriscono o sostituiscono voci nella cronologia; controllare anche **librerie di terze parti e piattaforme pubblicitarie**. Dopo correzione: richiesta di riconsiderazione in GSC.
- Rilevante per **SPA**: verificare che router/librerie non manipolino `history` (pushState/replaceState) in modo da intrappolare l'utente.

## 2026-05 — Una nuova risorsa per l'ottimizzazione per l'AI generativa nella Ricerca Google (15 mag 2026)
Fonte: https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing?hl=it
- **[NUOVO]** Guida ufficiale **"Ottimizza il tuo sito web per le funzionalità di AI generativa nella Ricerca Google"** (`/search/docs/fundamentals/ai-optimization-guide`). Contenuti: importanza di contenuti **di valore, unici, non generici**; suggerimenti per contenuti **locali**, shopping, immagini e video; **chiarimenti sui miti di AEO (Answer Engine Optimization) e GEO (Generative Engine Optimization)**; indicazioni di base sugli **agenti AI**; perché le **best practice SEO restano pertinenti e fondamentali** per le funzionalità AI.
- Il post non elenca i singoli miti: consultare la guida per i dettagli.

## 2026-06 — Report sul rendimento dell'AI generativa della Ricerca in Search Console (3 giu 2026)
Fonte: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports?hl=it
- **[GSC][NUOVO]** Report dedicati alla visibilità nelle **funzionalità di AI generativa**: Ricerca (**AI Overviews e AI Mode**) e Discover. Metriche: **impressioni**, pagine (URL apparsi), paesi, dispositivi (solo Ricerca), date con granularità oraria/giornaliera/settimanale/mensile. I dati restano inclusi anche nel report Rendimento complessivo; questa è una vista separata. (Il post cita solo impressioni, non clic.)
- Rollout iniziale su un sottoinsieme; **dal 31 agosto 2026 disponibili per tutti i siti a livello globale**. Doc: support.google.com/webmasters/answer/16984139.

## 2026-06 — Aiutaci a scegliere la tappa europea di SCL Deep Dive 2026 (18 giu 2026)
Fonte: https://developers.google.com/search/blog/2026/06/scl-deep-dive-europe-2026?hl=it
- Sondaggio sulla città (Barcellona, Budapest, Berlino, Francoforte, Lisbona, Praga) e periodo. Nessun contenuto tecnico.

## 2026-07 — Search Central Live Deep Dive Europa 2026: Barcellona (6 lug 2026)
Fonte: https://developers.google.com/search/blog/2026/07/search-central-live-deep-dive-europe-2026?hl=it
- Barcellona 30/09–02/10/2026. Programma: giorno 1 basi e scansione (anche "alcuni sistemi di AI"), GSC per colli di bottiglia; giorno 2 indicizzazione, **rendering e contenuti con uso elevato di JavaScript**, uso dell'AI nell'indicizzazione, duplicazione e canonicalizzazione, internazionalizzazione; giorno 3 pubblicazione, ranking, funzionalità (incluse AI), Google Trends. Nessuna novità tecnica.

## 2026-07 — Rendimento dei contenuti delle piattaforme social e video nella Ricerca Google (7 lug 2026)
Fonte: https://developers.google.com/search/blog/2026/07/search-console-social-video-platforms?hl=it
- **[GSC][NUOVO]** **Proprietà della piattaforma** (platform properties): nuovo tipo di proprietà GSC per **Instagram, TikTok, X, YouTube**, utilizzabile anche **da creator senza sito web**. Evolve l'esperimento "canali social" di dicembre 2025.
- Report: Rendimento (clic, impressioni, post e query; esportazione), Insight (tendenze, post migliori, come le persone scoprono l'account), Obiettivi.
- Aggiunta: GSC → "Aggiungi proprietà" → scegliere piattaforma → verifica/autorizzazione della connessione. Rollout graduale.

## 2026-07 — Lancio globale delle proprietà della piattaforma e nuova guida social/video (29 lug 2026)
Fonte: https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide?hl=it
- Proprietà della piattaforma **disponibili globalmente per tutti** (Ricerca, Discover, Google News).
- Nuova guida "Analizzare il rendimento dei contenuti social e video" (`/search/docs/monitor-debug/analyze-social-video-content`): gruppi di query in Insight per idee di contenuto; filtro 24 ore per picchi; esportare più proprietà in un foglio per confronti cross-piattaforma; individuare video vecchi che tornano popolari; **annotazioni** per tracciare modifiche esterne (titolo YouTube, didascalia TikTok); confronto formati (shorts vs video lunghi, playlist).
- Chi ha già configurato il proprio **"profilo della Ricerca"** (Search profile, support.google.com/websearch/answer/16904498) dovrebbe avere accesso ai dati per la stessa piattaforma.

## 2026-08 — Aggiornamento delle norme relative alla reputazione del sito (28 ago 2026)
Fonte: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy?hl=it
- **[SPAM][MODIFICA]** A seguito del confronto con la **Commissione europea (DMA)**, **dal 30 agosto 2026** le azioni manuali per **abuso della reputazione del sito** hanno effetti diversi:
  - **utenti fuori dal SEE**: l'azione manuale incide direttamente sulla parte del sito interessata (il resto del sito non è toccato);
  - **utenti nel SEE (Italia inclusa)**: l'azione manuale **non ha effetto**; la sezione interessata può però essere **separata dai sistemi e classificata indipendentemente** dal resto del sito nel tempo.
- Notifiche GSC e richiesta di riconsiderazione invariate; in più, per i siti idonei, possibilità di **mediazione** (Google Search Mediation Scheme, CEDR). → Aggiorna la catena: marzo 2024 (introduzione) → novembre 2024 (irrigidimento) → gennaio 2025 (revisione testo) → agosto 2026 (applicazione differenziata SEE).

## 2026-09 — Search Central Live a Bogotá e Città del Messico (annuncio eventi)
Fonte: https://developers.google.com/search/blog/2026/09/search-central-live-mexico-and-colombia?hl=it
- Città del Messico 15/10/2026, Bogotá 19/10/2026. Nessun contenuto tecnico.

## 2026-09 — Search Central Live India 2026: Bengaluru (annuncio evento)
Fonte: https://developers.google.com/search/blog/2026/09/search-central-live-india-2026?hl=it
- Bengaluru 30/10/2026 (scansione, indicizzazione, dati strutturati, qualità). Nessun contenuto tecnico.

## 2026-09 — SCL Deep Dive Europa 2026: relatori della community (16 set 2026)
Fonte: https://developers.google.com/search/blog/2026/09/scl-dd-europe-2026-community-speakers?hl=it
- Elenco relatori (lightning talk 7 minuti, poster session ~40 minuti); contenuti in gran parte uguali a Bangkok 2025 ("le fondamenta della Ricerca non cambiano così tanto") più nuovi argomenti sull'AI. Nessuna novità tecnica.

## 2026-09 — Nuovi report sul rendimento della Ricerca multimodale sul web in Search Console (24 set 2026)
Fonte: https://developers.google.com/search/blog/2026/09/web-multimodal-in-sc?hl=it
- **[GSC][NUOVO]** Nuovo **filtro per tipo di ricerca "multimodale"** nel report Rendimento dei risultati di ricerca e nel report sulle funzionalità di AI generativa: dati su come i contenuti appaiono quando gli utenti cercano **con immagini** — **Google Lens, Cerchia e Cerca (Android), caricamento immagini nella Ricerca, "Cerca questa immagine" di Chrome**. Esportabile. Rollout globale dal 24/09/2026; i dati compaiono solo se il sito riceve traffico da queste query.

---

# Stato attuale (ottobre 2026)

Elenco delle differenze rispetto alla SEO "classica", da usare per non dare consigli obsoleti. Tra parentesi la fonte (data del post) e, se pertinente, la catena di aggiornamenti.

## Funzionalità rimosse o ridotte nella SERP
- **Casella di ricerca dei sitelink**: rimossa dal 21/11/2024 in tutto il mondo. Il markup `SearchAction` è inutile ma innocuo; il markup `WebSite` per il **nome del sito** resta supportato (2024-10).
- **Breadcrumb su mobile**: dal 23/01/2025 su mobile l'URL visibile mostra solo il dominio; breadcrumb visibili solo su desktop. Markup `BreadcrumbList` ancora supportato (2025-01).
- **Dati strutturati ritirati dai risultati Google** (2025-06): Book actions, **Course info**, ClaimReview/Fact check, Estimated salary, Learning video, SpecialAnnouncement, Vehicle listing. Rimossi da report GSC/Rich Results Test dal 9/09/2025; API GSC fino a dicembre 2025; export BigQuery con campi `NULL` dal 1/10/2025.
- **Ulteriore semplificazione** (2025-11): altre funzionalità poco usate in eliminazione; **da gennaio 2026** rimozione del supporto dei tipi di dati strutturati interessati in GSC e API. L'elenco puntuale è nel changelog della documentazione (`/search/updates`), non nel post → verificare sempre lì prima di proporre un markup.
- Nessuna di queste rimozioni influisce sul ranking.

## Sistemi di ranking e aggiornamenti
- **Core update marzo 2024**: l'utilità dei contenuti è valutata da più sistemi principali e segnali; non esiste più "un solo indicatore o un solo sistema" (il vecchio "helpful content system" separato non va più citato come tale). Core update agosto 2024: attenzione ai siti piccoli/indipendenti con contenuti originali.
- **Ranking prevalentemente a livello di pagina**, con alcuni segnali a livello di sito; **DA/DR e simili di terze parti non sono segnali Google** (2024-03).
- **Sezioni molto diverse dal sito principale** possono essere valutate come siti a sé (2024-11; ribadito per il SEE nel 2026-08).
- **Discover ha un proprio core update** (febbraio 2026): rilevanza locale per paese, meno clickbait, competenza per argomento.

## Norme antispam nuove o modificate
- **Abuso di domini scaduti** (2024-03).
- **Abuso di contenuti su larga scala** (2024-03): vale per contenuti creati con IA, persone o mix se lo scopo principale è manipolare il ranking. L'IA in sé non è spam.
- **Abuso della reputazione del sito**: introdotto 03/2024 (in vigore 05/05/2024) → **irrigidito 11/2024** (la supervisione del sito host non esclude la violazione) → testo rivisto 01/2025 → **dal 30/08/2026 nel SEE l'azione manuale non ha effetto sui risultati**, ma la sezione può essere classificata separatamente; fuori dal SEE la sezione viene colpita. Possibile mediazione.
- **Compromissione del pulsante Indietro** (back button hijacking): pratica dannosa, **in vigore dal 15/06/2026** (2026-04).

## AI nella Ricerca
- **AI Overviews e AI Mode** sono esperienze consolidate; Google dice che **valgono gli stessi fondamentali SEO** (contenuti unici e utili, page experience, accessibilità tecnica, dati strutturati coerenti, contenuti multimodali) (2025-05).
- I controlli di anteprima `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` limitano anche la presenza nelle funzionalità AI (2025-05).
- Guida ufficiale **"Ottimizza il tuo sito per le funzionalità di AI generativa"** (2026-05) con **chiarimenti sui miti AEO/GEO** e basi sugli **agenti AI**: la SEO resta la base.
- Google invita a misurare **conversioni/valore delle visite**, non solo i clic (2025-05).
- La ricerca **multimodale** (Lens, Cerchia e Cerca, immagini) ora è misurabile in GSC (2026-09).

## Crawler e infrastruttura
- **Googlebot è un client di una piattaforma di scansione centralizzata**; documentazione dei crawler spostata sul sito **"crawling"** (`developers.google.com/crawling/...`) (2026-03).
- **Limite di 2 MB per URL** per Googlebot (HTML e ciascuna risorsa JS/CSS), 64 MB per PDF, 15 MB default per altri crawler; il contenuto oltre la soglia è ignorato (2026-03).
- **WRS stateless** (niente localStorage/sessione tra richieste) e cache di JS/CSS **fino a 30 giorni ignorando gli header HTTP** (2024-12, 2026-03).
- **Intervalli IP** dei crawler: nuovo percorso `/crawling/ipranges/`; il vecchio `/search/apis/ipranges/` viene dismesso/reindirizzato entro ~fine settembre 2026 (2026-03).
- **Caching HTTP**: Googlebot supporta `ETag`/`If-None-Match` (preferito) e `Last-Modified`/`If-Modified-Since` con risposte 304 (2024-12).
- **CDN/WAF** possono bloccare i crawler: usare 503/429 per blocchi temporanei, mai pagine di errore con 200, mai interstitial anti-bot senza 503 (2024-12).
- **Risorse critiche (JS/CSS) su host separato**: sconsigliato per le prestazioni (correzione del 6/12/2024 al post del 3/12/2024).
- **robots.txt**: RFC 9309; `crawl-delay` e `clean-param` **non supportati da Google**; `sitemap` supportato; nuovi user-agent anche per scopi AI; esempio ufficiale di blocco di un crawler di training AI lasciando passare i motori di ricerca (2025-02/03).
- **AVIF** supportato in Ricerca e Immagini (2024-08).

## Novità Search Console (cronologia)
- Gestione **token di proprietà inutilizzati** con "Verifica rimozione" (2024-04).
- **Consigli** (Recommendations) in Panoramica, sperimentale (2024-08).
- Vista **24 ore** con dati orari, ritardo dei dati quasi dimezzato (2024-12) → **API Search Analytics con dimensione `HOUR`** fino a 10 giorni (2025-04).
- **Search Console Insights** integrato nell'interfaccia principale (2025-06) → **gruppi di query** (AI, solo siti ad alto volume) (2025-10) → **filtro query con brand/non brand** (2025-11; per tutti i siti idonei dall'11/03/2026; solo proprietà di primo livello) → **canali social** in Insights (esperimento, 2025-12) → **proprietà della piattaforma** per Instagram, TikTok, X, YouTube (07/2026, globale dal 29/07/2026).
- **Annotazioni personalizzate** sui grafici (2025-11).
- **Configurazione basata sull'AI** del report Rendimento (sperimentale, 2025-12).
- **Granularità settimanale/mensile** nei grafici (2025-12).
- **Report sul rendimento dell'AI generativa** (AI Overviews, AI Mode, Discover AI): impressioni, pagine, paesi, dispositivi; **globale dal 31/08/2026** (2026-06).
- **Filtro ricerca multimodale** (2026-09).
- E-commerce: **spedizione e resi configurabili in GSC** (2024-07, solo con Merchant Center → dal 2025-11 per tutti i commercianti online identificati); le impostazioni GSC **prevalgono** sui dati strutturati.

## Dati strutturati nuovi (prevalentemente e-commerce)
- `ProductGroup` + `hasVariant`/`variesBy`/`productGroupID` (2024-02); norme sui resi a livello di `Organization` (2024-06); programmi fedeltà `Organization` + `Product` (2025-06); norme di spedizione a livello di `Organization` (2025-11). Indicazione ricorrente: usare i sottotipi **`OnlineStore`** o **`LocalBusiness`** di `Organization`.
- Caroselli (beta) per aggregatori/fornitori nel SEE (2024-02) e in Sudafrica (2025-08).

## Documentazione/guide
- **SEO Starter Guide** riscritta (2024-02): rimossi glossario, dati strutturati, mobile, analisi prestazioni; aggiunti contenuti duplicati, video, miti SEO, tempi per vedere risultati.
- Nuova doc **faceted navigation** (2024-12); nuove pagine "Funzionalità di AI e il tuo sito" e "Uso di contenuti creati con AI generativa" (2025-05); guida ottimizzazione AI generativa (2026-05); guida analisi contenuti social/video (2026-07).

---

# Implicazioni per la skill SEO

## (a) Controlli da aggiungere a un audit
1. **Peso dell'HTML iniziale < 2 MB** (incluse intestazioni) e **ogni risorsa JS/CSS < 2 MB**; segnalare immagini base64 inline, CSS/JS inline voluminosi, menu enormi prima del contenuto (2026-03).
2. **Ordine nel `<head>`/HTML**: `<title>`, meta description/robots, `<link rel="canonical">`, hreflang, dati strutturati essenziali **il più in alto possibile** (2026-03).
3. **Accessibilità ai crawler**: HTTP 200 sulle pagine indicizzabili; Googlebot non bloccato da robots.txt, CDN o WAF; nessun interstitial anti-bot servito a Googlebot; blocchi temporanei con **503/429**, mai errori con 200 (soft error). Verifica con **Controllo URL** (screenshot renderizzato) di GSC (2024-12, 2025-05).
4. **Risorse di rendering non bloccate** in robots.txt (JS, CSS, endpoint XHR/API necessari al contenuto) (2024-12).
5. **robots.txt**: sintassi RFC 9309; segnalare `crawl-delay`/`clean-param` come inefficaci per Google; presenza di `Sitemap:`; valutare se/quali **crawler AI** bloccare (scelta editoriale del proprietario; esempio ufficiale con `allow: /$`) (2025-03).
6. **Coerenza meta robots/X-Robots-Tag con robots.txt**: un `noindex` su URL bloccato da robots.txt non viene letto; si applica la direttiva più restrittiva (2025-03).
7. **Controlli di anteprima** (`nosnippet`, `data-nosnippet`, `max-snippet`) verificati in funzione di AI Overviews/AI Mode (limitano anche lì la visibilità) (2025-05).
8. **Dati strutturati**: corrispondenza con il contenuto visibile; validazione con Rich Results Test; segnalare tipi **deprecati** (SearchAction della sitelinks search box, Course info, ClaimReview, Estimated salary, Learning video, SpecialAnnouncement, Vehicle listing, Book actions) come "inutili ma innocui"; mantenere `WebSite` (site name), `BreadcrumbList` (desktop), `Organization`/`LocalBusiness`; consultare il changelog `/search/updates` per le rimozioni post-novembre 2025.
9. **Caching HTTP**: presenza di `ETag` e/o `Last-Modified` coerenti e risposta **304** a richieste condizionali; `Cache-Control: max-age` (2024-12).
10. **Cache-busting**: evitare parametri di cache-busting che cambiano a ogni deploy senza modifiche reali ai file (2024-12).
11. **Faceted navigation/filtri/parametri** (se presenti): robots.txt o frammenti `#` se non da indicizzare; altrimenti `&`, ordine coerente, 404 per combinazioni vuote, canonical (2024-12).
12. **Back button hijacking**: verificare che nessuno script (inclusi router SPA, librerie terze, script pubblicitari) inserisca/sostituisca voci di cronologia impedendo il ritorno immediato alla pagina precedente (spam dal 15/06/2026) (2026-04).
13. **Norme antispam 2024–2026**: contenuti su larga scala (anche IA) senza valore, domini scaduti riutilizzati, sezioni di terze parti ospitate per sfruttare la reputazione del dominio (2024-03, 2024-11, 2026-08).
14. **Immagini**: testo alternativo presente (indicazione principale per principianti); formati moderni (AVIF supportato); in caso di cambio formato con cambio URL → redirect lato server (2024-02, 2024-08). **Immagini e video di qualità** a supporto del testo per la ricerca multimodale (2025-05).
15. **Search Console – setup**: proprietà di **dominio/primo livello** (necessaria per il filtro brand); pulizia **token di verifica** di ex proprietari/agenzie; annotazioni per deploy/migrazioni; uso del report Insights, filtro brand, report AI generativa, filtro multimodale, granularità settimanale/mensile (2024-04, 2025-11, 2026-06, 2026-09).
16. **IP dei crawler**: se il sito/CDN usa allowlist o verifica Googlebot, aggiornare all'endpoint `developers.google.com/crawling/ipranges/` (2026-03).
17. **Log del server**: verificare richieste Googlebot (per IP pubblicati) e tempi di risposta; report Statistiche di scansione (2024-12, 2026-03).
18. **Misurazione**: impostare conversioni (contatti, prenotazioni, download CV) oltre ai clic, come suggerito per il traffico da AI (2025-05).

## (b) Consigli obsoleti da evitare
- Implementare il markup **sitelinks search box** (`WebSite` + `SearchAction`) per ottenere la casella: funzionalità rimossa dal 21/11/2024.
- Promettere **breadcrumb visibili nei risultati mobile**.
- Promettere rich result per **Course info** (corsi), **Estimated salary**, **Learning video**, **Fact check**, **SpecialAnnouncement**, **Book actions**, **Vehicle listing**.
- Usare `crawl-delay` per Google; citare `noodp`; puntare sul **meta keywords** (citato come mito).
- Citare l'**"Helpful Content Update/System"** come sistema separato da "recuperare" (dal marzo 2024 l'utilità è valutata da più sistemi principali).
- Usare **Domain Authority/Domain Rating** come metrica Google.
- Consigliare di **spostare JS/CSS critici su un sottodominio/CDN separato** per risparmiare crawl budget (sconsigliato dal 6/12/2024 per le prestazioni).
- Considerare **sicuri i contenuti di terze parti "supervisionati"** ospitati per sfruttare la reputazione del sito (non più vero da novembre 2024).
- Comprare **domini scaduti** per sfruttarne la reputazione; produrre **pagine in massa** (con IA o manualmente) per intercettare query.
- Trattare **AEO/GEO** come discipline con tattiche separate che sostituiscono la SEO: Google afferma che le best practice SEO restano la base per le funzionalità AI e la guida 2026 chiarisce i miti AEO/GEO.
- Valutare il successo **solo sui clic** ignorando conversioni e impressioni nelle funzionalità AI.
- Riferirsi a **Search Console Insights** come strumento beta separato, o al percorso `/search/apis/ipranges/` per gli IP dei crawler.
- Presentare l'ottimizzazione mobile e i dati strutturati come "primi passi indispensabili" per principianti: la Starter Guide 2024 li ha tolti dalla parte base (restano utili, ma non sono la priorità per un sito nuovo).

## (c) Note per personal brand (portfolio sviluppatore) e professionista locale (orientatrice di carriera)
**Comuni**
- Il nome della persona funziona da **"brand"**: con il **filtro query con brand** (proprietà di primo livello, volume sufficiente) separare le ricerche del nome (es. "Nome Cognome sviluppatore") da quelle non brand ("sviluppatore Angular freelance", "orientamento professionale online"). Su siti piccoli il filtro potrebbe non comparire per volume insufficiente; i **gruppi di query** quasi certamente non saranno disponibili (solo siti ad alto volume).
- **Proprietà della piattaforma** in GSC per **YouTube, Instagram, X, TikTok** (globali dal 29/07/2026), utili se la persona pubblica lì; collegate al **profilo della Ricerca** se configurato. **LinkedIn e GitHub non sono tra le piattaforme supportate** secondo i post letti.
- **Nome del sito**: mantenere il markup `WebSite` per il site name (ancora supportato).
- Contenuti **unici, non generici, people-first** (case study reali, progetti, esperienze): è la leva principale sia per la Ricerca classica sia per AI Overviews/AI Mode; evitare pagine prodotte in massa con l'IA.
- **Annotazioni GSC** per segnare lanci del sito, restyling, nuovi articoli, campagne LinkedIn.
- **Report AI generativa** in GSC per vedere se le pagine compaiono in AI Overviews/AI Mode (impressioni).
- **Conversioni**: per il portfolio contatti da recruiter/download CV; per la professionista richieste di consulenza/prenotazioni.
- **Discover**: il core update 2026 premia competenza **per argomento** e contenuti locali per paese; un blog focalizzato (es. carriera/orientamento in Italia, sviluppo Angular) è più adatto di articoli sparsi su temi diversi.

**Professionista locale + online**
- Mantenere aggiornato il **Profilo dell'attività su Google** (Google Business Profile): citato esplicitamente per la ricerca multimodale/AI (2025-05).
- Dati strutturati `Organization` con sottotipo **`LocalBusiness`** (indicazione ricorrente nei post merchant); non usare `Course`/Course info aspettandosi rich result (ritirato).
- Le **unità aggregatori/caroselli SEE** (2024-02) riguardano aggregatori e fornitori (attività locali, offerte di lavoro): una singola professionista non è un aggregatore; potrebbe però comparire *dentro* aggregatori/directory di settore.
- Contenuti locali: la guida AI 2026 include suggerimenti specifici per **contenuti locali** (consultare la guida per i dettagli).

**Portfolio sviluppatore**
- Immagini dei progetti con **alt text**, formati moderni (AVIF/WebP), e magari **video** dimostrativi (ricerca multimodale).
- Se il portfolio ospita contenuti di terzi (guest post, articoli sponsorizzati) per "far crescere" il dominio, attenzione alla norma sulla reputazione del sito.

## (d) Note per SPA JavaScript (Angular)
- **Rendering**: Google scarica l'HTML, poi il WRS esegue JS e scarica JS/CSS/XHR; tra i passaggi può esserci ritardo (2024-12). Per Angular conviene che **title, meta, canonical e contenuto principale siano già nell'HTML iniziale** (SSR/prerendering) — è un'inferenza coerente con le indicazioni "ordine dei byte" e "WRS esegue solo ciò che recupera", non un'affermazione testuale dei post.
- **Limite 2 MB per risorsa**: i bundle JS (es. `main.js`, `vendor`) oltre 2 MB **verrebbero troncati** per il WRS → rendering incompleto. Verificare le dimensioni dei bundle e usare code splitting/lazy loading (2026-03).
- **HTML iniziale**: non inlinare enormi CSS critici o stati serializzati (es. transfer state molto grande) che spingano i contenuti oltre 2 MB (2026-03).
- **WRS stateless**: non far dipendere il contenuto renderizzato da `localStorage`, `sessionStorage`, cookie di sessione o stato di navigazioni precedenti (2026-03).
- **Cache WRS di 30 giorni** sulle risorse: i nomi file con hash di contenuto (default Angular CLI) sono compatibili; evitare query string di cache-busting che cambiano senza modifiche reali (2024-12).
- **Non bloccare** in robots.txt `/assets/`, bundle JS, CSS o endpoint API necessari al rendering (2024-12).
- **Routing con frammento `#`** (HashLocationStrategy): Google indica che i frammenti `#` sono generalmente ignorati dai motori (usati apposta per i filtri da non indicizzare) → le route basate su `#` non vanno considerate URL indicizzabili distinti; usare `PathLocationStrategy` con URL reali per le pagine da indicizzare (inferenza dal post sulla faceted navigation, 2024-12).
- **Pagine "non trovate"/risultati vuoti**: preferire codice **404** reale; il post ammette il redirect a una pagina generica "non trovato" solo quando non ci sono alternative, citando proprio le **SPA** (2024-12). Con SSR/hosting si può restituire 404 vero; evitare soft 404 (pagina di errore con 200).
- **History API**: verificare che router, guard, librerie di terze parti e script ads non usino `pushState`/`replaceState` in modo da impedire il ritorno con "Indietro" (back button hijacking, spam dal 15/06/2026) (2026-04).
- **CDN/hosting** (Firebase, Netlify, Vercel, Cloudflare ecc.): controllare che le protezioni bot non servano challenge a Googlebot; usare Controllo URL per vedere lo screenshot renderizzato (2024-12).
- **Caching HTTP** per l'`index.html` e i prerender: `ETag`/`Last-Modified` + 304 (2024-12).
- Le domande su rendering/indicizzazione di **siti JavaScript complessi** sono un tema ricorrente negli eventi Google (Tokyo 2025, Deep Dive 2026): non esistono nei post letti nuove regole specifiche per le SPA oltre a quanto sopra.

