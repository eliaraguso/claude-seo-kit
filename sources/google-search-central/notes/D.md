# Gruppo D — Dati strutturati parte 1 (intro, JavaScript, article → job-posting)

Appunti fedeli alla documentazione Google Search Central (versione IT scaricata). Ordine: prima le pagine trasversali (intro, JavaScript), poi i tipi in ordine alfabetico.

---

## Introduzione al markup dei dati strutturati nella Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=it

- **Cosa sono**: formato standardizzato per fornire informazioni su una pagina e classificarne il contenuto. Google li usa per capire la pagina e per raccogliere info sul mondo (persone, libri, aziende presenti nel markup). Possono attivare **risultati avanzati** (rich results).
- **Case study citati** (dati Google): Rotten Tomatoes +25% CTR su 100.000 pagine con DS; Food Network +35% visite convertendo l'80% delle pagine; Rakuten 1,5x tempo sulla pagina e 3,6x interazione su pagine AMP con funzionalità; Nestlé +82% CTR per pagine mostrate come risultati avanzati.
- **CMS** (Wix, WordPress, Shopify): usare impostazioni SEO o plug-in del CMS.
- **Regola di base**: i DS sono markup in-page sulla pagina a cui si riferiscono e ne descrivono i contenuti. **Non creare pagine vuote solo per i DS** e **non marcare informazioni non visibili all'utente**, anche se accurate.
- **Vocabolario**: per lo più schema.org, ma il riferimento definitivo per il comportamento in Google è la documentazione Search Central, non schema.org. schema.org ha molti attributi non necessari a Google (utili forse ad altri motori).
- **data-vocabulary.org non è più idoneo** per i risultati avanzati.
- **Obbligatorie vs consigliate**: tutte le proprietà obbligatorie sono necessarie per l'idoneità. Più consigliate aumentano la probabilità di visualizzazione, ma **meglio meno proprietà consigliate complete e accurate che molte incomplete/errate**.
- Google può fare uso generale di **`sameAs`** e di altri dati schema.org anche non documentati (possibili funzionalità future).
- **Formati supportati** (tutti e tre ok se validi):
  - **JSON-LD (consigliato)**: `<script type="application/ld+json">` in `<head>` o `<body>`; non interlacciato col testo visibile; facile per oggetti nidificati; **Google legge JSON-LD inserito dinamicamente** (JavaScript, widget del CMS).
  - **Microdati**: attributi HTML, di solito nel `<body>` (usabile anche in `<head>`).
  - **RDFa**: estensione HTML5, in `<head>` e `<body>`.
  - Google consiglia JSON-LD perché più semplice da implementare e gestire su larga scala, meno soggetto a errori.
- **Linee guida**: seguire le linee guida generali sui DS + quelle specifiche del tipo, altrimenti niente idoneità.
- **Strumenti**: Test dei risultati avanzati (sviluppo; validazione e in alcuni casi anteprima); report sullo stato dei risultati avanzati in Search Console (post-deploy: le pagine possono rompersi per problemi di template o pubblicazione); Controllo URL per verificare che Google abbia trovato i DS.
- **Misurare l'effetto**: test prima/dopo su alcune pagine: scegliere pagine senza DS, stabili, non stagionali ma abbastanza popolari; raccogliere dati per diversi mesi in Search Console; aggiungere DS, verificare con Controllo URL; poi registrare per alcuni mesi nel report Rendimento filtrando per URL.

---

## Generare dati strutturati con JavaScript
Fonte: https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript?hl=it

- Metodi più comuni: **Google Tag Manager** e **JavaScript personalizzato**; in alternativa **rendering lato server**.
- **Avviso `Product`**: il markup generato dinamicamente può rendere le scansioni di Shopping **meno frequenti e meno affidabili** (problema per prezzo/disponibilità che cambiano spesso); assicurare risorse server sufficienti per il traffico di Google.
- **Google Tag Manager**: installare GTM → nuovo tag **HTML personalizzato** → incollare blocco JSON-LD → installare contenitore → pubblicare contenitore → verificare.
  - Usare le **variabili GTM** per estrarre i dati dalla pagina (es. variabile `recipe_name` = `function() { return document.title; }` e poi `{{recipe_name}}` nel tag) **invece di duplicare le informazioni in GTM**: la duplicazione aumenta il rischio di mancata corrispondenza tra pagina e DS.
- **JavaScript personalizzato**: si può generare tutto il JSON-LD via JS o arricchire quello reso lato server. **Google comprende ed elabora i DS presenti nel DOM al momento del rendering.** Esempio: `fetch` di un'API → creazione di `<script type="application/ld+json">` con `textContent` → `document.head.appendChild(script)`.
- **SSR**: si possono includere i DS nell'output renderizzato; vedere la documentazione del framework.
- **Verifica**:
  - Test dei risultati avanzati con **input via URL (consigliato) anziché via codice**, perché l'input codice ha limitazioni JavaScript (es. restrizioni **CORS**).
  - Esito positivo: "La pagina è idonea per i risultati avanzati".
  - Per tipi non supportati dal test: controllare **l'HTML sottoposto a rendering**; se contiene i DS, Google può elaborarli.
  - Errori/avvisi: di solito sintassi o proprietà mancante; poi guida "risoluzione problemi JavaScript relativi alla ricerca".

---

## Dati strutturati per articoli (`Article`, `NewsArticle`, `BlogPosting`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/article?hl=it

- **A cosa serve**: pagine di notizie, blog, articoli sportivi. Aiuta Google a capire la pagina e a mostrare meglio **testo del titolo, immagini e informazioni sulla data** nella Ricerca, Google News e Assistente Google. Non è richiesto per l'idoneità alle funzionalità di Google News (es. Notizie principali), ma comunica esplicitamente tipo, autore, titolo.
- **Tipi**: `Article`, `NewsArticle`, `BlogPosting`.
- **Proprietà obbligatorie: nessuna.** Aggiungere quelle applicabili.
- **Proprietà consigliate**:
  - `author` (`Person` o `Organization`), `author.name` (Text), `author.url` (URL: pagina che identifica univocamente l'autore, es. profilo social, pagina "Chi sono"/Biografia; se è una pagina profilo interna, marcarla con dati strutturati **ProfilePage**; in alternativa `sameAs` — Google capisce entrambi per differenziare gli autori).
  - `dateModified` (DateTime ISO 8601, consigliato fuso orario; altrimenti fuso di Googlebot). Il Test non avvisa se manca.
  - `datePublished` (DateTime ISO 8601, idem).
  - `headline` (Text; conciso, i titoli lunghi possono essere troncati su alcuni dispositivi).
  - `image` (ripetuta, `ImageObject` o URL): immagini pertinenti, **non loghi o didascalie**; URL scansionabili e indicizzabili; formato supportato da Google Immagini; ideale più immagini ad alta risoluzione, **minimo 50.000 pixel (larghezza × altezza)**, rapporti **16x9, 4x3 e 1x1**.
- **Linee guida tecniche**:
  - Articoli in più parti: `rel=canonical` verso ogni singola pagina o verso una pagina panoramica (**non** verso la prima pagina della serie).
  - Contenuti in abbonamento / dietro registrazione: aggiungere DS per contenuti con paywall.
  - Violazioni → possibile **azione manuale**; dopo la correzione, richiesta di riconsiderazione.
- **Best practice markup autori**:
  - Includere nel markup **tutti** gli autori mostrati in pagina.
  - Più autori: un oggetto per autore nell'array `author`; **non** unire più nomi in un solo `name`.
  - Usare `@type` e `url` (o `sameAs`) con URL validi; persona → pagina dell'autore; organizzazione → home page.
  - `author.name` solo il nome: niente editore (usa `publisher`), niente qualifica (usa `jobTitle`), niente titoli di cortesia (usa `honorificPrefix`/`honorificSuffix`), niente frasi tipo "pubblicato da".
  - `Person` per persone, `Organization` per organizzazioni; **non usare `Thing`** né il tipo sbagliato.
- **Flusso consigliato**: aggiungere proprietà → seguire linee guida → Test dei risultati avanzati (correggere errori critici, valutare i non critici) → Controllo URL (pagina non bloccata da robots.txt, `noindex`, login) → richiesta di nuova scansione → Sitemap (automatizzabile con API Search Console Sitemap).
- **Troubleshooting**: Google non garantisce la visualizzazione; elenco errori DS e report "dati strutturati non analizzabili"; con un'azione manuale sui DS questi vengono **ignorati** (la pagina può restare nei risultati) → report Azioni manuali; problemi di spam possono non essere rilevati dal Test; la nuova scansione richiede giorni.

---

## Dati strutturati per azioni relative ai libri (`Book`) — poco pertinente
Fonte: https://developers.google.com/search/docs/appearance/structured-data/book?hl=it

- **A cosa serve**: azioni "acquista" (`ReadAction`) e "prendi in prestito" (`BorrowAction`) nella scheda informativa del libro; link diretti verso la pagina del fornitore. Ordine dei fornitori personalizzato/dinamico per utente, **non controllabile**.
- **Disponibilità limitata**: riservata ai fornitori di libri con **ampia selezione**; serve compilare un **modulo di interesse** e completare l'onboarding (la richiesta non garantisce la partecipazione). Non è markup in pagina ma un **feed JSON** (`DataFeed`) ospitato e recuperato da Google.
- **Concetti**: Opera (`Book` Work, primo livello) vs Edizione (`Book` Edition in `workExample`, almeno una per opera); raggruppare le edizioni; ogni opera separata con `@id` diverso e almeno un'edizione con ISBN o identificatore supportato. `LibrarySystem` (astratto) con almeno un `Library` (member, con indirizzo fisico).
- **Identificatori**: ISBN-13 preferito; alternative OCLC, LCCN, JP e-code. **ISBN-10 non accettato** (convertire).
- **Link**: URL canonici; il link d'azione deve portare a una pagina che consente direttamente acquisto/prestito (non pagine risultati o riepiloghi).
- **Feed**: < 1 GB non compresso per file (altrimenti dividere); compressione zip/gz/tar/tar.gz/jar/ar/arj/cpio/dump; estensione `.json`; più file anche via indice Sitemap; niente entità inattive; solo URL di produzione e canonici; ogni entità con `@id`, `url`, `urlTemplate` univoci. Validazione con **Data Feed Validation Tool** (opzione "Books Action"). Hosting: Google Cloud Storage, HTTPS, SFTP, AWS S3. Aggiornamento consigliato quotidiano; nessun tempo reale; Google recupera il feed **1 volta al giorno** e indicizza in genere **entro 2 giorni**.
- **Obbligatorie**:
  - `DataFeed`: `@context`, `@type`, `dataFeedElement` (solo `Book` o solo `LibrarySystem`, mai misti; feed separati); `dateModified` (nella tabella).
  - `Book` (Work): `@context`, `@id`, `@type`, `author`, `name`, `url`, `workExample`. Consigliata: `sameAs`.
  - `Book` (Edition): `@id`, `@type`, `bookFormat` (AudiobookFormat/EBook/Hardcover/Paperback), `inLanguage` (ISO 639-1), `isbn`, `potentialAction`. Consigliate: `author`, `bookEdition`, `datePublished`, `identifier`, `name`, `sameAs`, `url`.
  - `author`: `@type`, `name`; consigliata `sameAs`. `identifier` (PropertyValue): `@type`, `propertyID` (OCLC_NUMBER/LCCN/JP_E-CODE), `value`.
  - `ReadAction`: `@type`, `expectsAcceptanceOf` (Offer; `category` = nologinrequired/free/subscription/purchase/rental; `eligibleRegion` Country ISO 3166-1 alpha-2), `target` (EntryPoint con `actionPlatform` Desktop/Android/IOS e `urlTemplate`). Consigliate: `availabilityStarts`, `availabilityEnds`, `price` (necessario per purchase/rental), `priceCurrency` (ISO 4217).
  - `BorrowAction`: `@type`, `lender` (`LibrarySystem` con `@id`), `target`.
  - `LibrarySystem`: `@context`, `@id`, `@type`, `additionalProperty` (`librarytype` = public/academic/corporate/government/school/special), `member`, `name`, `url`. `Library` (member): `@id`, `@type`, `location` (PostalAddress con addressCountry, addressLocality, addressRegion, postalCode, streetAddress), `name`.

---

## Dati strutturati di breadcrumb (`BreadcrumbList`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb?hl=it

- **A cosa serve**: indica la posizione della pagina nella gerarchia del sito; Google usa il markup breadcrumb nel corpo della pagina per classificare le informazioni nei risultati di ricerca (il breadcrumb contestualizza la pagina rispetto alla query).
- **Disponibilità**: **su computer** (desktop), in tutte le regioni e lingue in cui è disponibile la Ricerca Google.
- **Struttura**: `BreadcrumbList` con **almeno due `ListItem`**. Sono ammesse **tracce multiple** sulla stessa pagina (in JSON-LD: array di più `BreadcrumbList`).
- **Proprietà obbligatorie**:
  - `BreadcrumbList.itemListElement` (array ordinato di `ListItem`).
  - `ListItem.item`: URL della pagina del breadcrumb, come URL o come `Thing` con ID (JSON-LD `@id`; Microdati `href`/`itemid`; RDFa `about`/`href`/`resource`). **Per l'ultimo elemento non è obbligatorio**: se assente Google usa l'URL della pagina corrente.
  - `ListItem.name`: titolo mostrato all'utente (non obbligatorio se `item` è un `Thing` con `name`).
  - `ListItem.position` (Integer; 1 = inizio della traccia).
- **Linee guida**: rappresentare un **percorso utente tipico**, non riprodurre la struttura dell'URL. **Non serve** un `ListItem` per il livello radice (dominio/hostname) né per la pagina stessa. data-vocabulary.org non più idoneo. Tecniche non ammesse → possibile azione manuale.
- **Monitoraggio Search Console**: dopo il primo deploy (report stato risultati avanzati: aumentano i validi, non gli invalidi; correggere, Controllo URL, richiedere convalida); dopo nuovi template (aumento errori = template rotto; calo dei validi senza aumento invalidi = DS non più incorporati → Controllo URL); analisi periodica con report Rendimento / API Search Console.

---

## Dati strutturati Carosello (`ItemList`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/carousel?hl=it

- **A cosa serve**: risultato avanzato a elenco scorrevole **su dispositivi mobili**, con più schede dello **stesso sito** ("carosello host"). Si ottiene combinando `ItemList` con uno dei tipi supportati: **Corsi (elenco di corsi), Film, Ricette, Ristoranti** (LocalBusiness). Altri caroselli multi-sito (es. Notizie principali) **non** sono controllabili con questo markup.
- **Due modalità**:
  1. **Pagina di riepilogo + pagine di dettaglio**: nell'`ItemList` ogni `ListItem` ha **solo** `@type` (`ListItem`), `position`, `url` (URL canonico della pagina di dettaglio). Le pagine di dettaglio contengono i DS del tipo specifico (es. `Recipe`).
  2. **Unica pagina elenco**: tutto il contenuto in una pagina; ogni `ListItem` ha `item` con tutte le proprietà del tipo; `item.url` = pagina corrente + **anchor** (es. `#apple_pie`), con anchor HTML (`<a>`, `name` o `id`) accanto al testo visibile.
- **Proprietà obbligatorie**:
  - `ItemList.itemListElement`: **almeno due** `ListItem`, tutti dello stesso tipo.
  - Riepilogo: `position` (Integer, base 1), `url` (canonico, URL univoci ma sullo **stesso dominio** — stesso dominio, sottodominio o superdominio).
  - Pagina unica: `item` (Thing, con `item.name`, `item.url` e le obbligatorie del tipo; es. per ricetta `prepTime` e `image`), `item.name` (titolo dell'elemento; formattazione HTML ignorata), `item.url`, `position`.
- **Linee guida**: tutti gli elementi dello **stesso tipo** (non mescolare); DS completi con **tutti** gli elementi elencati in pagina; testo visibile simile ai DS; ordine di visualizzazione = `position`.
- **Convalida**: Test dei risultati avanzati; per pagine riepilogo verificare ≥2 `ListItem`, stesso tipo, e convalidare **ogni URL** elencato (ogni pagina deve avere DS validi del tipo).

---

## Dati strutturati per caroselli (beta)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/carousels-beta?hl=it

- **A cosa serve**: nuovo carosello host in **beta**, scorrevole in orizzontale, con riquadri che possono mostrare prezzo, valutazione, immagini delle entità di un sito. `ItemList` + almeno uno tra **`LocalBusiness` e sottotipi** (es. `Restaurant`, `Hotel`, `VacationRental`), **`Product`**, **`Event`**.
- **Disponibilità (beta, requisiti possono cambiare)**: solo **SEE, Turchia, Sudafrica**, su computer e mobile.
  - SEE: query su hotel, case vacanze, trasporto via terra, voli, **attività locali**, cose da fare (eventi, tour, attività), prodotti.
  - Turchia: solo hotel, case vacanze, attività locali.
  - Sudafrica: hotel, case vacanze, Things to Do, voli, prodotti, consegna cibo, noleggio auto, prenotazione bus.
  - Moduli di interesse: aggregatori SEE/Turchia (trasporto via terra, hotel, case vacanze, attività locali, cose da fare); voli; prodotti → programma CSS; Sudafrica → modulo badge/chip.
- **Come**: una **pagina di riepilogo/categoria** con info su ogni entità e link a pagine di dettaglio; si possono **combinare tipi diversi** (es. eventi + attività locali). Markup **solo sulla pagina di riepilogo** (non obbligatorio sulle pagine di dettaglio), ma con gli URL delle pagine di dettaglio.
- **Linee guida**: tipi generici ammessi, ma per le proprietà consigliate serve il tipo specifico (es. `amenityFeature` richiede `LodgingBusiness`); campi extra ammessi ma potrebbero non comparire; serve riepilogo + più pagine di dettaglio (**anchor nella stessa pagina non supportati**); la pagina di riepilogo deve contenere **almeno tre entità**; marcare **tutti** gli elementi della pagina; categorie impaginate → un `ItemList` per ogni pagina con le sue entità; scorrimento continuo → marcare le entità caricate inizialmente nell'area visibile. Ordine dei riquadri = ordine del markup.
- **Proprietà obbligatorie**:
  - `itemListElement` (≥ **3** `itemListElement.item`); `itemListElement.item` (sottotipo di LocalBusiness, Product o Event); `itemListElement.position` (base 1). URL degli elementi verso pagine diverse dello stesso dominio.
  - Comuni a tutti gli item: `image` (URL/ImageObject ripetuti; **no loghi**; scansionabili; formato Google Immagini; consigliate più immagini ad alta risoluzione **min 50.000 pixel**, rapporti 16x9, 4x3, 1x1), `name` (HTML ignorato), `url` (canonico della pagina di dettaglio, univoco, stesso dominio/sottodominio/superdominio).
- **Proprietà consigliate**:
  - Comuni: `aggregateRating.bestRating` (default 5), `aggregateRating.ratingCount`, `aggregateRating.ratingValue` (numero, frazione o percentuale; scala default 1–5; **punto decimale** non virgola; in Microdati/RDFa usare `content` per override, es. `content="4.4"` con testo "4,4").
  - `LocalBusiness`: `amenityFeature` (solo `LodgingBusiness`, `LocationFeatureSpecification`), `priceRange` (es. "$", "$$", "$-$$"; **meno di 12 caratteri**, altrimenti non mostrato), `servesCuisine` (solo ristoranti).
  - `Product`/`Event`: `offers` (`Offer` con `price` + `priceCurrency`, o `AggregateOffer` con `highPrice`, `lowPrice`, `priceCurrency`); valuta ISO 4217, **default USD** se assente; per eventi `price` include costi di servizio/commissioni; evento gratuito → `price: 0`; non usare `price` insieme a `lowPrice`/`highPrice`.

---

## Dati strutturati per elenco di corsi (`Course`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/course?hl=it

- **A cosa serve**: far trovare i corsi a potenziali studenti; mostra nome del corso, chi lo offre, breve descrizione (risultato "elenco di corsi", tipicamente in carosello).
- **Disponibilità**: **solo in inglese**, in tutte le regioni in cui è disponibile la Ricerca Google.
- **Struttura**: pagina di dettaglio del singolo corso abbinata a una **pagina di riepilogo con `ItemList`** (vedi Carosello), oppure **unica pagina elenco** con `ItemList` + dettagli dei corsi (URL con anchor). Nel Test dei risultati avanzati guardare le sezioni "Voce del corso" (e "Caroselli" per pagina unica); gli errori di altri tipi si possono ignorare.
- **Linee guida contenuti**: `Course` solo per una **serie o unità di apprendimento** (seminari, lezioni, moduli) su una materia, con risultato esplicito di apprendimento, tenuta da uno o più insegnanti con un certo numero di studenti. **Non sono corsi**: un evento pubblico generico (es. "Giornata dell'astronomia") o un singolo video di 2 minuti ("Come fare un panino").
- **Linee guida tecniche**: markup di **almeno 3 corsi** (pagine dettaglio separate o pagina elenco unica); **markup Carosello obbligatorio** su riepilogo o pagina unica; ogni corso deve avere `name` e `provider` **validi**. Nomi non validi: frasi promozionali ("La migliore scuola al mondo"), prezzi nel titolo ("…a soli 30 $!"), titolo non sul tema ("Guadagna velocemente…"), sconti/opportunità d'acquisto ("…25% di sconto!"). Violazioni → possibile azione manuale.
- **Proprietà `Course`**:
  - Obbligatorie: `description` (Text; **limite di visualizzazione 60 caratteri**), `name`.
  - Consigliata (in tabella): `provider` (`Organization`, es. UC Berkeley). Nota: le linee guida tecniche dicono comunque che ogni corso "deve avere" `name` e `provider` validi.
- **Proprietà `ItemList`** (obbligatorie): `itemListElement`, `ListItem.position`, `ListItem.url` (canonico, univoco per elemento).

---

## Dati strutturati per i set di dati (`Dataset`, `DataCatalog`, `DataDownload`) — poco pertinente
Fonte: https://developers.google.com/search/docs/appearance/structured-data/dataset?hl=it

- **A cosa serve**: far trovare i set di dati nello strumento **Ricerca per set di dati** (Dataset Search): scienze, machine learning, dati civici/amministrativi. Esempi di dataset: tabella/CSV, raccolte di tabelle, file proprietari, raccolte di file, dati di immagini, file ML (parametri addestrati, definizioni di reti neurali).
- **Disponibilità**: nella pagina non sono indicate restrizioni di paese/lingua. Per escludere un dataset: meta tag robots (applicazione in giorni o settimane).
- **Formati**: schema.org `Dataset` (JSON-LD preferito; anche RDFa 1.1/Microdati) o W3C **DCAT** (l'esempio DCAT in RDFa non è supportato dal Test dei risultati avanzati); supporto sperimentale/beta a **CSVW** per dati tabulari.
- **Linee guida / best practice**:
  - Sitemap; DS sulle **pagine canoniche** (di destinazione) del dataset; se marcate più copie (es. schede in pagine di risultati) usare `sameAs` verso la canonica.
  - Provenienza: `sameAs` per semplice ripubblicazione (valore univoco per dataset; mai lo stesso `sameAs` per due dataset diversi); `isBasedOn` se modificato significativamente o se aggregazione di più originali; `identifier` per DOI/identificatori compatti (ripetibile, lista JSON).
  - Proprietà di testo: max **5000 caratteri** (oltre vengono ignorati).
  - Avvisi noti ignorabili: richiesta di `contactType` per organizzazioni (valori utili: customer service, emergency, journalist, newsroom, public engagement); `csvw:Table` come valore imprevisto per `mainEntity`.
- **Proprietà obbligatorie**: `description` (**50–5000 caratteri**; Markdown ammesso; immagini con URL assoluti; a capo con `\n` in JSON-LD), `name` (descrittivo; nomi univoci per dataset distinti). Per `DataDownload`: `distribution.contentUrl` obbligatoria.
- **Consigliate**: `alternateName`, `creator` (Person/Organization; ORCID in `sameAs` per persone, ROR per organizzazioni), `citation` (articoli accademici correlati, non la citazione del dataset stesso; includere DOI), `funder`, `hasPart`/`isPartOf` (URL o `Dataset` completo), `identifier`, `isAccessibleForFree`, `keywords`, `license` (URL di una **versione specifica**, es. `.../by/4.0`), `measurementTechnique` (proposta pending), `sameAs`, `spatialCoverage` (Place con GeoCoordinates o GeoShape — coppie "lat long"; o testo), `temporalCoverage` (ISO 8601, intervalli aperti con `..`), `variableMeasured` (pending), `version`, `url`; `includedInDataCatalog` (DataCatalog); `distribution` (DataDownload), `distribution.encodingFormat`.
- **Troubleshooting specifico**: dataset assente → verificare markup con Test dei risultati avanzati o stato della scansione in Search Console; logo azienda mancante → aggiungere DS logo (Organization) e definire le informazioni dell'attività su Google.

---

## Dati strutturati per la valutazione complessiva del datore di lavoro (`EmployerAggregateRating`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/employer-rating?hl=it

- **A cosa serve**: siti che pubblicano **valutazioni generate dagli utenti** su organizzazioni che assumono; fornisce valutazioni ai candidati e migliora la presenza del brand nell'**esperienza di ricerca di lavoro** di Google. Chi usava lo snippet recensione (fase beta) dovrebbe passare a `EmployerAggregateRating`. Per offerte di lavoro → `JobPosting`.
- **Disponibilità**: nella pagina non sono indicate restrizioni di paese/lingua.
- **Linee guida tecniche**: le valutazioni devono essere visibili/disponibili sulla pagina col markup e deve essere subito evidente che la pagina contiene valutazioni; valutazioni di una **specifica organizzazione**, non di categorie/elenchi ("I dieci migliori posti di lavoro", "Aziende tecnologiche" non validi); scala default **1–5**, altre scale ammesse indicando migliore/peggiore.
- **Norme contenuti**: gli utenti devono poter pubblicare valutazioni sul sito e il sito deve ospitarle; il numero di valutazioni deve riflettere quelle reali; punteggio ricavato con precisione. Si applicano anche le **norme sulla qualità dei risultati di ricerca estesi**. Violazioni → azione manuale.
- **Obbligatorie**: `itemReviewed` (`Organization`), `ratingCount` **o** `reviewCount` (almeno uno), `ratingValue` (numero, frazione, percentuale; default scala 1–5).
- **Consigliate**: `bestRating` (default 5), `worstRating` (default 1).

---

## Dati strutturati per forum di discussione (`DiscussionForumPosting`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/discussion-forum?hl=it

- **A cosa serve**: siti in stile forum dove le persone condividono prospettive in prima persona; aiuta Google a identificare le discussioni e ad usarle in funzionalità come **"Discussioni e forum"**. Forum a domande e risposte → usare `QAPage`.
- **Disponibilità**: nella pagina non sono indicate restrizioni di paese/lingua.
- **Struttura**: commenti nidificati sotto il post (albero `comment` per thread; per forum lineari tutte le risposte come `comment` del post originale). Nelle pagine successive di thread multipagina includere il post originale con `url` della prima pagina. Se l'URL riguarda un singolo post: `WebPage` con `mainEntity` (o `mainEntityOfPage`) = `DiscussionForumPosting`. Pagine elenco (profilo, argomento, categoria): si può includere solo ciò che è in pagina + URL dei post; **non marcare un solo post come entità principale** se la pagina non è la pagina di quel post; si possono collegare a `Collection` o `ItemList`.
- **Linee guida contenuti**: solo per **post generati dagli utenti**; **non** per contenuti creati principalmente dal publisher o suoi agenti. Piattaforme social generiche → `SocialMediaPosting` (tipo padre, stessi requisiti). Validi: forum di community, piattaforme forum generiche, social. **Non validi**: articolo/blog scritto dal sito (anche con commenti), recensioni utenti di prodotti. Per `Article`, `ImageObject`, `VideoObject` con commenti usare i loro tipi, non `DiscussionForumPosting`. Ogni post/commento deve includere **l'intero testo** presente in pagina.
- **Linee guida tecniche**: per questo tipo Google **consiglia Microdati o RDFa** (evita di duplicare grandi blocchi di testo), ma JSON-LD resta pienamente supportato.
- **`DiscussionForumPosting` obbligatorie**: `author` (Person/Organization; seguire best practice autori di Article e ProfilePage), `author.name`, `datePublished` (ISO 8601), uno tra `text`, `image`, `video` (non necessari se il post è rappresentato su un'altra pagina con `url` esterno).
- **Consigliate**: `author.url` (profilo forum, marcato con ProfilePage), `comment` (in ordine di pagina), `commentCount`, `creativeWorkStatus` (`Deleted`), `dateModified` (non duplicare la data di pubblicazione se nessuna modifica), **`digitalSourceType`** (`TrainedAlgorithmicMediaDigitalSource` = contenuti da modello addestrato/LLM; `AlgorithmicMediaDigitalSource` = processo algoritmico semplice/bot; se assente Google presume contenuti umani), `headline` (non duplicare/troncare il testo se non c'è titolo; sconsigliato per `SocialMediaPosting`), `image` (no immagini predefinite, segnaposto, icone o foto autore; anteprima link → `image` del `WebPage` in `sharedContent`), `interactionStatistic` (LikeAction, DislikeAction, ViewAction, CommentAction/ReplyAction, ShareAction), `isPartOf`, `sharedContent` (`WebPage`, `ImageObject`, `VideoObject`, `DiscussionForumPosting`/`Comment`), `text`, `url` (canonico; per thread multipagina URL della prima pagina), `video`.
- **`Comment` obbligatorie**: `author`, `datePublished`, uno tra `text`/`image`/`video`. Consigliate: analoghe (`author.url`, `comment`, `commentCount`, `creativeWorkStatus`, `dateModified`, `digitalSourceType`, `image`, `interactionStatistic`, `sharedContent`, `url` del commento specifico — non includerlo se è solo l'URL del post, `video`).
- **`InteractionCounter` obbligatorie**: `userInteractionCount`, `interactionType`. Usabile anche su `author` (`agentInteractionStatistic`).

---

## Dati strutturati per Domande e risposte didattiche (`Quiz`, `Question`, `Answer`) — poco pertinente
Fonte: https://developers.google.com/search/docs/appearance/structured-data/education-qa?hl=it

- **A cosa serve**: pagine con **flashcard**; idoneità al carosello Domande e risposte didattiche nella Ricerca, Assistente Google e Google Lens. Pagina con una sola domanda + risposte degli utenti → `QAPage`.
- **Disponibilità**: solo per query di argomento **istruzione**, computer e mobile. Lingue: inglese, portoghese, vietnamita (tutte le regioni); **spagnolo solo Messico**. (L'italiano non è elencato.)
- **Linee guida tecniche**: DS sulla pagina foglia più dettagliata; niente DS su pagine senza domande; tutte le domande con `eduQuestionType` = `Flashcard` (altri tipi → non idonea); scansione efficiente; domande visibili in pagina (non solo in file dati o PDF).
- **Contenuti**: stesse linee guida di QAPage; almeno una coppia domanda/risposta pertinente; responsabilità di accuratezza (contenuti non accurati possono rendere non idonee **tutte** le pagine Q&A del sito); violazioni → azione manuale.
- **Standard didattici** in `educationalAlignment` (es. Common Core, TEKS, UK National Curriculum…).
- **`Quiz`**: obbligatoria `hasPart` (Question, una per flashcard); consigliate `about`, `about.name`, `educationalAlignment`, `educationalAlignment.alignmentType` (`educationalSubject` / `educationalLevel`, standard LRMI), `educationalAlignment.targetName`.
- **`Question`** (obbligatorie): `acceptedAnswer` (una sola per Question), `eduQuestionType` (`Flashcard`), `text`.

---

## Dati strutturati per eventi (`Event`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/event?hl=it

- **A cosa serve**: esperienza di ricerca eventi su Google (Ricerca e altri prodotti, es. **Google Maps**), con logo, descrizione ecc. Case study: Eventbrite +100% nella crescita tipica del traffico anno su anno.
- **Tre vie**: (1) se pubblichi eventi su piattaforme terze (biglietterie, social) già integrate con Google, continua lì; (2) CMS senza accesso HTML → plug-in o **Evidenziatore di dati** di Search Console; (3) modifica diretta HTML con DS.
- **Disponibilità (paesi/lingue)**: Australia (inglese), Brasile (portoghese), Canada (inglese), Germania (tedesco), India (inglese), America Latina (spagnolo), Spagna (spagnolo), Regno Unito (inglese), Stati Uniti (inglese). **Italia/italiano non elencati.**
- **Linee guida tecniche**: pagina di destinazione con tipi evento schema.org; **ogni evento DEVE avere un URL univoco (pagina foglia)** con markup su quell'URL; supportate **solo pagine dedicate a un singolo evento** (non pagine calendario/programmi multipli); eventi multi-giorno → `startDate` e `endDate`; più esibizioni in giorni diversi con biglietti propri → un `Event` per esibizione.
- **Norme contenuti**: nome, data di inizio e luogo precisi; **non** marcare come eventi: prodotti/servizi (pacchetti viaggio), sconti o promozioni brevi ("acquista subito", "50% fino a sabato"), orari di apertura, coupon/voucher. Evento **prenotabile dal pubblico generale** (no eventi solo su abbonamento/invito). Esclusi eventi con partecipanti e pubblico minorenni in una scuola. **Esperienze virtuali senza componente fisica non supportate: l'evento deve svolgersi in un luogo fisico.** Violazioni → azione manuale (anche "markup strutturato contenente spam").
- **Data e ora**: ISO 8601 con offset UTC (es. `2019-09-05T19:00:00-05:00`); senza fuso Google usa quello della `location`. Multi-giorno: inizio e fine; ora sconosciuta → solo data (`2019-07-20`); giornata intera → solo data in `startDate` ed `endDate`. **Non usare mezzanotte** (`T00:00:00`) o `T23:59:59+00:00` come finto "giorno intero": Google le interpreta come orari reali (es. `2019-08-15T00:00:00+00:00` diventa il 14 alle 17:00 in California).
- **Proprietà obbligatorie**:
  - `location` (`Place`, con `location.address` e `location.name`).
  - `location.address` (`PostalAddress`, indirizzo fisico preciso — non "Sydney" ma indirizzo completo). Più strade → posizione iniziale + dettagli in descrizione; luogo non definito → città/luogo più rappresentativo; più luoghi simultanei → eventi separati.
  - `name` (titolo completo dell'evento; **non** il nome del luogo; niente promo, prezzi, URL, artisti; non usare il tipo "Concerto" come nome; evidenziare un aspetto esclusivo).
  - `startDate` (DateTime ISO 8601).
- **Proprietà consigliate**: `description` (concisa, sui dettagli dell'evento; non ripetere data/luogo; Google mostra solo uno snippet), `endDate`, `eventStatus` (`EventScheduled` default, `EventCancelled`, `EventPostponed`, `EventRescheduled`; **non rimuovere `startDate`/`location`** quando cambia lo stato; postponed → mantenere data originale finché non nota), `image` (larghezza consigliata **1920 px, minima 720 px**; min 50.000 pixel; 16x9, 4x3, 1x1), `location.name` (nome della sede, non città salvo eventi cittadini, non il titolo), `offers` (uno per tipo di biglietto), `offers.availability` (`InStock`, `SoldOut`, `PreOrder`), `offers.price` (prezzo più basso incluse commissioni; gratuito → `0`), `offers.priceCurrency` (ISO 4217), `offers.validFrom` (inizio vendita), `offers.url` (pagina d'acquisto chiara e predominante per il pubblico, link cliccabile dalla pagina evento, scansionabile — non bloccata da robots.txt), `organizer` (Organization/Person, con `organizer.name`, `organizer.url`), `performer` (Person/PerformingGroup) + `performer.name`, `previousStartDate` (solo con `eventStatus` = `EventRescheduled`; ripetibile).
- **Troubleshooting**: sede mancante/errata (verificare `addressLocality`/`addressRegion`, non mettere il nome evento in `location.name`; anteprima del Test mostra "false" se la località non è reale); sito non mostrato come opzione biglietti (manca `offers.url` o non conforme → recrawl e modulo di (ri)valutazione); ora/data errate (offset mancante, mezzanotte).

---

## Dati strutturati Fact check (`ClaimReview`) — in dismissione nella Ricerca
Fonte: https://developers.google.com/search/docs/appearance/structured-data/factcheck?hl=it

- **Stato**: Google **sta eliminando gradualmente il supporto a `ClaimReview` nella Ricerca Google**; resta supportato dallo strumento **Fact Check Explorer**. Disponibile lo strumento Fact Check Markup per generare il markup senza codice.
- **A cosa serve**: pagine che verificano una dichiarazione fatta da altri; mostrava un riepilogo del fact check nei risultati per quella dichiarazione.
- **Idoneità** (abilita ma non garantisce): più pagine con `ClaimReview`; nessuna discrepanza tra DS e contenuto; standard di responsabilità/trasparenza delle norme Google News; norme di correzione o meccanismo di segnalazione errori; **esclusi siti di entità politiche** (campagne, partiti, eletti); dichiarazione e verifica facilmente identificabili; dichiarazione attribuita a una fonte distinta e tracciabile; analisi trasparente con citazioni alle fonti primarie.
- **Tecniche**: **un solo `ClaimReview` per pagina** (con più non è idonea); la pagina deve contenere almeno un breve riepilogo del fact check e della valutazione; uno stesso `ClaimReview` su una sola pagina (salvo varianti mobile/desktop); aggregatori: tutti i fact check conformi + elenco pubblico dei siti aggregati.
- **Obbligatorie `ClaimReview`**: `claimReviewed` (consigliato < **75 caratteri**; non includere la valutazione), `reviewRating` (Rating; oggi viene mostrato solo il valore testuale; scala esempio 1=Falso … 5=Vero), `url` (stesso dominio/sottodominio; redirect e URL abbreviati non risolti). Consigliate: `author` (publisher del fact check, con `name`/`url`), `itemReviewed` (`Claim`; supportato ancora il vecchio `CreativeWork`).
- **`Claim`** (consigliate): `appearance` o `firstAppearance` (una delle due), `author` (autore della dichiarazione; `name` obbligatoria se presente, `sameAs` consigliata), `datePublished`.
- **`Rating`**: obbligatoria `alternateName` (es. "Vero", "Per lo più vero"; inizio della frase significativo se troncata); consigliate `bestRating` (> worstRating), `name` (fallback di alternateName), `ratingValue`, `worstRating` (min 1).

---

## Metadati delle immagini in Google Immagini (`ImageObject` / IPTC)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata?hl=it

- **A cosa serve**: Google Immagini può mostrare autore, modalità d'uso e crediti; le info di licenza rendono l'immagine idonea al **badge "Su licenza"** (link alla licenza e alla pagina per ottenerla).
- **Disponibilità**: mobile e desktop, tutte le regioni e lingue in cui è disponibile la Ricerca Google.
- **Prerequisiti**: pagine con immagini accessibili senza login; non bloccate da robots.txt o meta robots (report Indicizzazione pagine / Controllo URL); best practice SEO immagini; Sitemap.
- **Due metodi (ognuno sufficiente)**:
  - **Dati strutturati**: associano immagine e pagina; vanno aggiunti **per ogni istanza/pagina** in cui l'immagine compare, anche se uguale.
  - **Metadati IPTC** incorporati nel file: una sola volta per immagine, viaggiano con il file.
  - In caso di conflitto tra i due, **prevalgono i dati strutturati**.
- **`ImageObject` obbligatorie**: `contentUrl` (URL dell'immagine; `url` supportato ma meno preciso) + **almeno una** tra `creator`, `creditText`, `copyrightNotice`, `license` (incluse una, le altre diventano consigliate nel Test).
- **Consigliate**: `acquireLicensePage` (pagina su come ottenere la licenza: pagamento o contatti), `creator` (Person/Organization) + `creator.name`, `creditText`, `copyrightNotice`, `license` (URL della licenza, es. termini del sito o Creative Commons BY-NC 4.0). **Per il badge "Su licenza" serve `license`** (consigliato anche `acquireLicensePage`).
- Esempi coprono anche immagini in `srcset` (`contentUrl` = URL del `src`) e più immagini per pagina (array JSON-LD di `ImageObject`).
- **IPTC estratti da Google**: Copyright Notice, Creator, Credit Line, **Digital Source Type** (`trainedAlgorithmicMedia`, `compositeSynthetic`, `algorithmicMedia`, `compositeWithTrainedAlgorithmicMedia` — per immagini generate/composte con IA), Licensor URL (proprietà dell'oggetto Licensor), **Web Statement of Rights** (necessario per il badge "Su licenza" via IPTC).
- **C2PA**: se presenti metadati C2PA (firmatario con C2PA **≥ 2.1** e certificato in trust list C2PA), Google può mostrarli in "Informazioni su questa immagine" (es. creata/modificata con IA).
- **Rimozione metadati**: riduce il peso ma può essere illegale in alcune giurisdizioni; Google consiglia di conservare almeno autore, riga dei riconoscimenti e nota sul copyright.


---

## Dati strutturati per offerte di lavoro (`JobPosting`) per Ricerca lavoro
Fonte: https://developers.google.com/search/docs/appearance/structured-data/job-posting?hl=it

- **A cosa serve**: offerte di lavoro idonee all'**esperienza di ricerca lavoro** di Google (logo, recensioni, valutazioni, dettagli; filtri per località/qualifica). In alternativa ci si integra tramite siti terzi di annunci. Recensioni su datori di lavoro → `EmployerAggregateRating`.
- **Disponibilità geografica**: Asia (Bangladesh, Hong Kong, India, Indonesia, Giappone, Kazakistan, Kirghizistan, Malaysia, Pakistan, Filippine, Singapore, Sri Lanka, Taiwan, Thailandia, Uzbekistan, Vietnam); **Europa** (Austria, Bielorussia, Belgio, Danimarca, Francia, Germania, Grecia, **Italia**, Paesi Bassi, Portogallo, Russia, Spagna, Svizzera, Regno Unito); America Latina (intera); MENA (Algeria, Bahrein, Egitto, Iraq, Giordania, Kuwait, Libano, Libia, Marocco, Oman, Palestina, Qatar, Arabia Saudita, Tunisia, EAU); Nord America (intera); Africa subsahariana (intera).
- **Flusso**: scansione efficiente; copie della stessa offerta su URL diversi → canonical; Test dei risultati avanzati (con anteprima); **API Indexing consigliata al posto delle Sitemap per gli URL delle offerte** (Googlebot scansiona prima), ma Sitemap comunque consigliata per tutto il sito (Google ricrawla le pagine con `lastmod` più recente dell'ultima scansione).
- **Rimozione offerta** (non intervenire in tempo sulle scadute può portare ad azione manuale): `validThrough` nel passato, **oppure** pagina rimossa con **404/410**, **oppure** rimozione del markup `JobPosting`; poi notificare con API Indexing.
- **Lavoro da remoto**: `jobLocationType` = `TELECOMMUTE` solo per lavori **100% da remoto** (non per smart working occasionale o negoziabile); `applicantLocationRequirements` (almeno un paese; obbligatoria se 100% remoto con vincoli geografici); `jobLocation` solo se esiste un luogo fisico (con `addressCountry`); senza `applicantLocationRequirements` l'annuncio viene mostrato nel paese di `jobLocation`. Supportato ancora `TELECOMMUTE` come `additionalProperty` di `jobLocation` (schema vecchio).
- **Logo**: Google usa il logo della scheda Knowledge Graph dell'azienda; si può suggerire una modifica (via DS Organization); siti terzi possono usare `hiringOrganization.logo` (non diventa logo canonico); rapporto larghezza/altezza tra **0,75 e 2,5**.
- **Linee guida tecniche**: DS sulla **pagina foglia** della singola offerta, **mai su pagine elenco/risultati**; un `JobPosting` per offerta; DS sulla stessa pagina con la descrizione leggibile; la maggior parte delle proprietà una sola volta per pagina. Sitemap: URL accessibili (no firewall/robots), `<lastmod>`/`<pubDate>`/`<updated>` precisi, niente pagine di ricerca/elenchi/dinamiche, solo URL canonici.
- **Norme contenuti** (violazioni → azione manuale e rimozione): markup solo su pagine con una singola offerta; niente descrizioni incomplete; niente rappresentazione ingannevole (posizioni false, raccolta dati candidati senza assunzione, keyword stuffing, località false, offerte senza autorizzazione, uso di più account per eludere norme); niente linguaggio volgare; niente pubblicità/affiliazioni mascherate; niente offerte scadute; niente offerte senza possibilità di candidatura (es. inviti a fiere, descrizione dietro login); raccolta CV solo per posizioni aperte; **non sono ammesse "richieste di lavoro" in cui il candidato si offre di lavorare**; niente pagamento richiesto ai candidati; niente spam editoriale, annunci invadenti, testo tutto maiuscolo o con errori grammaticali.
- **Obbligatorie**: `datePosted` (ISO 8601), `description` (HTML completo: responsabilità, qualifiche, competenze, orari, formazione, esperienza; **diversa da `title`**; almeno interruzioni di paragrafo `<br>`, `<p>` o `\n`; riconosciuti `<p>`, `<ul>`, `<li>`; non riconosciuti `<h1>`, `<strong>`, `<em>`), `hiringOrganization` (nome dell'azienda, non della sede; anonimo → `"confidential"`), `jobLocation` (luogo fisico di lavoro; **`addressCountry` obbligatorio**; più sedi in array; non obbligatoria se 100% remoto con `applicantLocationRequirements`), `title` (solo denominazione del lavoro: niente codici, indirizzi, date, stipendi, aziende; niente abuso di `!` e `*` → rischio "markup strutturato contenente spam"; `name` non sostituisce `title`; siti terzi: mantenere il titolo ricevuto).
- **Consigliate**: `applicantLocationRequirements` (AdministrativeArea), `baseSalary` (MonetaryAmount, **solo i datori di lavoro**, stipendio effettivo non stimato; `unitText` = `HOUR`/`DAY`/`WEEK`/`MONTH`/`YEAR`, case-sensitive; fascia con `minValue`/`maxValue`), `directApply` (Boolean; candidatura diretta senza passaggi inutili; effetti non ancora immediati), `employmentType` (`FULL_TIME`, `PART_TIME`, `CONTRACTOR`, `TEMPORARY`, `INTERN`, `VOLUNTEER`, `PER_DIEM`, `OTHER`; più valori ammessi), `identifier` (PropertyValue), `jobLocationType` (`TELECOMMUTE`), `validThrough` (obbligatoria se l'offerta ha scadenza; omettere se ignota; rimuovere l'offerta se coperta prima).
- **Beta istruzione/esperienza**: `educationRequirements` (`credentialCategory`: `high school`, `associate degree`, `bachelor degree`, `professional certificate`, `postgraduate degree`; oppure `no requirements`), `experienceRequirements` (`monthsOfExperience` = minimo; `no requirements`), `experienceInPlaceOfEducation` (true → servono entrambe le precedenti). Continuare comunque a descriverli in `description`.
- **Troubleshooting / messaggi Search Console**: DS su pagina elenco ("Una pagina di offerte di lavoro non deve includere dati strutturati per singole offerte"); contenuti diversi dai DS (es. **stipendio nel markup ma non visibile in pagina**: tutte le info del markup devono essere visibili); offerte scadute attive; candidatura impossibile; logo errato; località mancante ("false" nell'anteprima). Dopo correzione → richiesta di riconsiderazione.
- **UTM** per tracciare il traffico da Google Jobs: `utm_campaign=google_jobs_apply`, `utm_source=google_jobs_apply`, `utm_medium=organic`.

---

# Implicazioni per la skill SEO

Nota: i tipi `Person`/`ProfilePage`, `Organization`, `LocalBusiness`, `FAQPage`, ecc. sono trattati in altri gruppi; qui sono citati solo dove le pagine del gruppo D vi rimandano. Le voci marcate *(deduzione)* non sono testo Google ma inferenze operative.

## (a) Tipi da usare per i due casi d'uso

### Portfolio / personal brand di uno sviluppatore (target recruiter)
- **`BlogPosting` / `Article`** su articoli, case study, post tecnici. Nessuna proprietà obbligatoria; consigliate: `headline` (conciso), `image` (immagini pertinenti, non loghi; ≥ 50.000 px; 16x9, 4x3, 1x1), `datePublished`, `dateModified` (ISO 8601 con fuso), `author` = `Person` con `name` (solo il nome), `url` verso la pagina "Chi sono" (da marcare con ProfilePage) e/o `sameAs` (profili esterni), eventuale `jobTitle` separato; `publisher` se serve.
- **`BreadcrumbList`** su pagine profonde (es. Progetti › Nome progetto): `itemListElement`, `ListItem.position`, `ListItem.name`, `ListItem.item` (non serve per l'ultimo elemento). Effetto visibile solo **su desktop**.
- **`ImageObject` con metadati licenza** (facoltativo) per foto/screenshot/illustrazioni originali: `contentUrl` + almeno uno tra `creator`, `creditText`, `copyrightNotice`, `license`; `license` (+ `acquireLicensePage`) per il badge "Su licenza". In alternativa IPTC nei file; non rimuovere i metadati di autore/copyright in fase di ottimizzazione immagini.
- **Uso generale di `sameAs`**: Google può usarlo anche fuori dai tipi documentati (intro) → utile per collegare l'identità dello sviluppatore ai profili esterni.
- **Da NON usare**: `JobPosting` per dire "sono disponibile/cerco lavoro" (le "richieste di lavoro" in cui il candidato si offre sono esplicitamente vietate; il markup è solo per pagine con una singola offerta di un datore di lavoro); `DiscussionForumPosting` per il proprio blog anche se ha commenti (contenuti del publisher non ammessi); `Course` per un singolo tutorial/video breve; `EmployerAggregateRating`; `Dataset` salvo veri dataset pubblicati.

### Libera professionista orientatrice di carriera (locale + online)
- **`BlogPosting` / `Article`** per contenuti editoriali (guide al CV, colloqui, orientamento) con le stesse best practice autore (`Person`, `url` verso la pagina bio/ProfilePage, `sameAs`).
- **`BreadcrumbList`** per servizi/articoli annidati.
- **`ImageObject`** con metadati di licenza per le proprie foto (stesse proprietà sopra).
- **`Event`** per workshop/seminari **solo se**: evento in luogo fisico (virtuale puro non supportato), prenotabile dal pubblico generale, una pagina per evento con URL univoco. Obbligatorie: `name`, `startDate`, `location` (`Place` con `name` e `address` PostalAddress completo). Consigliate: `description`, `endDate`, `eventStatus`, `image` (1920 px consigliati, min 720 px), `offers` (`price`, `priceCurrency`, `availability`, `validFrom`, `url`), `organizer` (`name`, `url`), `performer`. **Attenzione: l'esperienza eventi non è disponibile in Italia/italiano** (paesi: AU, BR, CA, DE, IN, America Latina, ES, UK, US) → in Italia oggi nessun rich result eventi; utile solo se si targettizzano quei paesi.
- **`Course` + `ItemList`**: solo se offre veri percorsi formativi (serie/unità con lezioni o moduli, docenti e studenti), almeno 3 corsi marcati, con carosello obbligatorio. Obbligatorie `name`, `description` (display 60 caratteri); `provider` di fatto richiesto dalle linee guida. **Disponibile solo in inglese** → irrilevante per contenuti in italiano. Una consulenza 1:1 non è un corso.
- **Caroselli beta (`ItemList` + `LocalBusiness`/`Product`/`Event`)**: disponibili nel SEE (Italia inclusa) ma pensati per pagine di riepilogo con ≥ 3 entità e pagine di dettaglio separate, e per query di aggregatori (hotel, attività locali, cose da fare…) con modulo di interesse → di norma **non applicabile** a una singola professionista.
- **`JobPosting`**: solo se pubblica davvero offerte di lavoro di un datore di lavoro (Italia supportata); non per promuovere i propri servizi.
- **Da NON usare**: `Quiz`/Education Q&A (italiano non supportato; serve contenuto flashcard), `ClaimReview` (in dismissione), `EmployerAggregateRating` (richiede recensioni utenti su datori di lavoro ospitate dal sito).

## (b) Controlli automatici per un audit dei dati strutturati
1. **Parsing**: ogni blocco `application/ld+json` è JSON valido; `@context` = `https://schema.org`; nessun uso di `data-vocabulary.org`.
2. **Formato**: preferire JSON-LD; Microdati/RDFa ok se validi. Eccezione: per `DiscussionForumPosting` Microdati/RDFa sono consigliati.
3. **Tipo corretto per il contenuto**: `Article/BlogPosting/NewsArticle` solo su pagine articolo; `JobPosting` ed `Event` solo su pagine foglia di **un singolo** elemento (mai su pagine elenco/calendario/risultati); `Course` con ≥ 3 corsi + `ItemList`; `DiscussionForumPosting` solo per contenuti generati dagli utenti.
4. **Proprietà obbligatorie per tipo** (tabelle sopra), es.: Breadcrumb (`itemListElement` con ≥ 2 `ListItem`, `position`, `name`, `item` tranne l'ultimo); Event (`name`, `startDate`, `location.address`); JobPosting (`datePosted`, `description`, `hiringOrganization`, `jobLocation`+`addressCountry` o remoto con `applicantLocationRequirements`, `title`); ImageObject (`contentUrl` + uno tra creator/creditText/copyrightNotice/license); ItemList carosello (≥ 2 elementi stesso tipo; ≥ 3 per la beta); EmployerAggregateRating (`itemReviewed`, `ratingValue`, `ratingCount` o `reviewCount`).
5. **Coerenza con il contenuto visibile**: ogni valore marcato deve comparire nella pagina renderizzata (titolo, autore, date, stipendio, prezzo, valutazioni); niente DS su informazioni invisibili né pagine vuote create solo per i DS.
6. **Date**: ISO 8601; presenza di offset di fuso orario; segnalare `T00:00:00` o `T23:59:59+00:00` usati come "giorno intero" negli eventi; `dateModified` coerente con `datePublished`; `validThrough` nel passato su offerte ancora online.
7. **Autori**: `author` con `@type` `Person`/`Organization` (mai `Thing`), un oggetto per autore, `name` senza titoli/ruoli/"di", presenza di `url` o `sameAs` validi; tutti gli autori visibili presenti nel markup.
8. **Immagini**: URL assoluti, scansionabili (non bloccati da robots.txt), formato supportato da Google Immagini, risoluzione ≥ 50.000 px (L×A), idealmente tre rapporti 16x9/4x3/1x1; niente loghi dove il tipo li esclude (Article, carosello beta); Event: larghezza ≥ 720 px (consigliati 1920).
9. **Limiti numerici**: `priceRange` < 12 caratteri; `Course.description` mostrata fino a 60 caratteri; `claimReviewed` < 75 caratteri; Dataset `description` 50–5000 caratteri; `hiringOrganization.logo` rapporto 0,75–2,5; un solo `ClaimReview` per pagina.
10. **Valori enumerati** case-sensitive: `employmentType`, `unitText`, `eventStatus`, `offers.availability`, `eduQuestionType`=`Flashcard`, `bookFormat`; valute ISO 4217 (default USD se mancante — segnalare); paesi ISO 3166-1; numeri decimali con il punto.
11. **URL**: canonici; stesso dominio/sottodominio per `ItemList`/carosello e `ClaimReview.url`; niente redirect/short URL; `offers.url` cliccabile dalla pagina e scansionabile.
12. **Indicizzabilità**: pagina con DS non bloccata da robots.txt, `noindex` o login; articoli multipagina con canonical corretto (non verso la prima pagina della serie).
13. **Disponibilità geografica/lingua**: avvisare quando il tipo non è disponibile per il mercato del sito (es. Event e Course per Italia/italiano; Education Q&A; caroselli beta solo SEE/TR/ZA; ClaimReview in dismissione; Breadcrumb visibile solo su desktop).
14. **Post-deploy**: Test dei risultati avanzati in modalità **URL**; Controllo URL; report di stato dei risultati avanzati e "dati strutturati non analizzabili" in Search Console; monitorare aumenti di invalidi o cali di validi dopo rilasci di template.

## (c) Note per SPA JavaScript / Angular
- Google **legge JSON-LD inserito dinamicamente** e comprende ed elabora i DS presenti nel DOM quando esegue il rendering della pagina → in una SPA Angular il JSON-LD generato lato client è accettabile.
- Alternativa indicata dalla doc: **rendering lato server** con JSON-LD già nell'output renderizzato (vedere la documentazione del framework, es. Angular SSR/prerendering).
- **Verifica con input via URL** nel Test dei risultati avanzati (l'input via codice ha limiti JavaScript, es. CORS); per tipi non supportati dal Test controllare l'**HTML renderizzato** (Controllo URL).
- Con GTM usare **variabili che leggono dalla pagina** invece di duplicare i dati, per evitare discrepanze contenuto/markup.
- `Product` (e dati che cambiano spesso) generato via JS → scansioni Shopping meno frequenti/affidabili: preferire markup lato server.
- *(deduzione)* Se il JSON-LD dipende da un `fetch` a un'API (come nell'esempio Google), l'endpoint deve essere raggiungibile durante il rendering di Googlebot (non bloccato da robots.txt, risposta rapida).
- *(deduzione)* In una SPA con router: un blocco JSON-LD per route, **sostituito/rimosso** a ogni navigazione, per non lasciare markup di un'altra vista né duplicati; il contenuto visibile corrispondente deve essere nello stesso DOM renderizzato.
- Dopo ogni release monitorare il report di stato: un calo dei validi senza aumento degli invalidi indica DS non più incorporati (tipico se il rendering JS si rompe).

## (d) Errori comuni da evitare (dalle pagine lette)
- Marcare contenuti **non visibili** o creare pagine vuote solo per i DS; stipendio/prezzi nel markup ma non in pagina.
- Usare il tipo sbagliato: `JobPosting` per autocandidature o pagine elenco; `Event` per promozioni, orari di apertura, coupon, eventi solo online o su invito; `DiscussionForumPosting` per articoli del publisher o recensioni di prodotto; `Course` per eventi singoli o video brevi.
- Più autori in un solo `name`; titoli/ruoli dentro `author.name`; `Organization` per una persona; uso di `Thing`.
- Nome evento = nome del luogo (o viceversa); promozioni, prezzi, "acquista subito" nel `name`/`title`; abuso di `!` e `*` (markup spam).
- Date a mezzanotte come "giornata intera"; date senza fuso orario; rimuovere `startDate`/`location` quando un evento viene annullato/posticipato.
- Offerte di lavoro scadute lasciate online senza `validThrough` passato / 404-410 / rimozione markup (rischio azione manuale).
- `TELECOMMUTE` su lavori non 100% remoti; `jobLocation` senza `addressCountry`.
- Carosello con elementi di tipi diversi, elenco incompleto rispetto alla pagina, URL su domini diversi; caroselli beta con anchor nella stessa pagina (non supportati).
- Più `ClaimReview` per pagina; `claimReviewed` che contiene il verdetto.
- Immagini troppo piccole, loghi al posto di immagini rappresentative, URL immagini bloccati.
- Breadcrumb che ricalca l'URL invece del percorso utente; meno di 2 `ListItem`.
- Testare JSON-LD generato da JS incollando il codice invece dell'URL; duplicare dati in GTM invece di leggerli dalla pagina.
- Rimuovere i metadati IPTC di copyright/autore comprimendo le immagini (può essere illegale in alcune giurisdizioni).
- Ricordare: con un'azione manuale sui DS, **i DS della pagina vengono ignorati**; il Test dei risultati avanzati non rileva problemi di spam/policy (non sintattici).
