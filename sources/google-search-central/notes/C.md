# Gruppo C — Aspetto nella Ricerca, Indexing API, case study

Appunti fedeli alla documentazione Google Search Central (versione italiana, scaricata il 2026-10-03). Ogni sezione riassume una pagina; le implicazioni operative sono in fondo.

---

## Panoramica degli argomenti relativi all'aspetto nella Ricerca
Fonte: https://developers.google.com/search/docs/appearance?hl=it
- Pagina indice: elenca gli argomenti su come influire sull'aspetto nella Ricerca (funzionalità AI, dettagli attività, date di pubblicazione, favicon, snippet in primo piano, accesso flessibile, Discover, immagini, fonti preferite, differenze regionali, cerca nei profili, nomi dei siti, sitelink, snippet, title link, luoghi più apprezzati, risultati tradotti, video, galleria elementi visivi, Storie web) e i tipi di dati strutturati supportati (tra cui Breadcrumb, Evento, Attività locali, Organizzazione, Pagina del profilo, Snippet recensione, Video, Domande e risposte, Corso...).
- "Programma per early adopter": monitoraggio delle spedizioni e dati strutturati per caroselli (beta) sono progettati con un numero limitato di organizzazioni.

## Abilitare la rete pubblicitaria per le funzionalità di traduzione
Fonte: https://developers.google.com/search/docs/appearance/ad-network-and-translation?hl=it
- Rivolta a chi gestisce una rete pubblicitaria: quando l'utente apre un risultato tradotto, Google recupera la pagina, riscrive l'URL sull'host `*.translate.goog` e la traduce.
- Per far funzionare/attribuire gli annunci bisogna riconvertire l'hostname: togliere il suffisso `.translate.goog`; dividere `_x_tr_enc` per virgola; anteporre `_x_tr_hp` se presente; togliere prefisso `1-` (se encoding contiene 1) e `0-` (se contiene 0 → IDN, poi aggiungere `xn--`); sostituire `/\b-\b/` con `.` e `--` con `-`. Poi ricostruire l'URL sostituendo l'host e rimuovendo tutti i parametri `_x_tr_*`, conservando percorso, frammento e parametri originali.
- Fornisce codice JS di esempio (`decodeHostname`) e tabella di test (es. `example-com.translate.goog` → `example.com`; `foo--example-com` → `foo-example.com`).
- Poco pertinente per siti vetrina (rilevante solo se il sito usa una rete pubblicitaria propria basata sull'URL di origine).

## Differenze regionali nell'esperienza della Ricerca
Fonte: https://developers.google.com/search/docs/appearance/aggregator-features?hl=it
- Tabella delle funzionalità regionali per Servizi di ricerca verticale (VSS), Servizi di shopping comparativo (CSS), fornitori diretti e fornitori di contenuti:
  - Unità di aggregatori (SEE): hotel, voli, trasporto via terra, attività locali, prodotti.
  - Unità di fornitori (SEE): stesse categorie.
  - Carosello di ecosistemi (SEE): meteo, sport, finanza, traduzioni.
  - Funzionalità dei siti di offerte di lavoro (SEE): carosello "Siti di offerte di lavoro" + chip.
  - Funzionalità dei siti di luoghi (Turchia): hotel e attività locali.
  - Badge e chip Sudafrica: viaggi, prodotti, noleggio auto, consegna cibo, trasporto via terra.
  - Caroselli di dati strutturati (host carousel, richiedono markup): SEE (hotel, attività locali, cose da fare, prodotti, trasporto, voli, case vacanze), Sudafrica, Turchia (hotel, attività locali, case vacanze).

## Unità di aggregatori nella Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/aggregator-unit?hl=it
- Disponibile solo per utenti nel SEE, query su hotel, voli, treni/autobus a lunga percorrenza, prodotti, attività locali. Pensata per VSS (OTA, CSS, metamotori, directory). Una sola unità di aggregatori alla volta; il fornitore col ranking più alto è espanso di default; clic diretti al sito dell'aggregatore. Accanto viene mostrata l'unità di fornitori.
- Idoneità: approvazione come VSS + dati + standard di qualità. Passi: esprimere interesse tramite modulo (modulo funzionalità aggregatori per trasporti/voli/hotel/attività locali; modulo CSS per prodotti); contenuti pertinenti alla query; fornire dati via feed diretti o API in tempo reale (feed punti d'interesse alloggi, API Transport Features, API Live per voli, feed punti d'interesse locali); rispettare le norme sui contenuti della Ricerca.
- Best practice: dettagli completi sulle entità (immagini, descrizioni, valutazioni verificate e numero recensioni, categorie specifiche, servizi e orari); titoli oggettivi con iniziale maiuscola, evitare tutto maiuscolo, punteggiatura eccessiva, emoji, testo promozionale ("MIGLIORI OFFERTE", "Spedizione gratuita"); immagini originali ad alta risoluzione, sfondi puliti, niente filigrane/badge; prezzi e disponibilità allineati alla landing page e feed aggiornati; monitorare con Search Console.
- Non pertinente per portfolio/professionista singola.

## Funzionalità di AI e il tuo sito web (AI Overview, AI Mode)
Fonte: https://developers.google.com/search/docs/appearance/ai-features?hl=it
- Le best practice SEO restano valide; **non ci sono requisiti aggiuntivi né ottimizzazioni speciali** per comparire in AI Overview o AI Mode.
- AI Overview: compaiono solo quando aggiungono valore rispetto alla ricerca classica (spesso non si attivano). AI Mode: utile per query che richiedono analisi, ragionamento, confronti complessi.
- Entrambe possono usare il "fan-out delle query": più ricerche correlate simultanee su sottoargomenti e più origini dati → insieme più ampio e diversificato di link di supporto. AI Mode e AI Overview possono usare modelli/tecniche diverse → risposte e link diversi.
- Requisiti tecnici per essere link di supporto: la pagina deve essere **indicizzata e idonea a comparire con uno snippet** e rispettare i requisiti tecnici della Ricerca. Nessun requisito aggiuntivo. Indicizzazione e pubblicazione non garantite.
- Best practice elencate: consentire la scansione in robots.txt **e da hosting/CDN**; contenuti rilevabili tramite link interni; buona esperienza sulla pagina; **contenuti importanti disponibili in forma di testo**; supportare il testo con immagini/video di qualità; dati strutturati corrispondenti al testo visibile; Merchant Center e profilo dell'attività aggiornati.
- Mito smentito: **non serve creare nuovi file leggibili dalle macchine, file di testo o "markup AI"**, né dati strutturati schema.org speciali.
- Misurazione: il traffico da AI Overview/AI Mode è incluso nel report Rendimento di Search Console, tipo di ricerca "Web" (non separato). Google afferma che i clic da pagine con AI Overview sono "di qualità superiore" (più tempo sul sito). Suggerito anche Google Analytics per conversioni/tempo.
- Controllo: l'AI è parte della Ricerca, quindi il controllo d'accesso è robots.txt per Googlebot. Per limitare ciò che viene mostrato: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`. Per limitare training/grounding in **altri** sistemi Google: Google-Extended (non riguarda la Ricerca).
- Troubleshooting controlli di anteprima: verificare con Controllo URL che il controllo sia nell'HTML visto da Googlebot; attendere la nuova scansione (da giorni a mesi) o richiederla.

## Evitare finestre di dialogo e interstitial invasivi
Fonte: https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials?hl=it
- Interstitial = overlay che copre l'intera pagina; finestra di dialogo = copre una parte. Quelli invasivi rendono difficile a Google comprendere i contenuti → possibili prestazioni di ricerca scadenti.
- Fare: usare **banner che occupano una piccola parte dello schermo** invece di interstitial a pagina intera (anche per installazione app: Smart App Banners Safari, esperienza install Chrome, o banner HTML); riutilizzarli per newsletter ecc.; usare plugin/librerie comuni dei CMS.
- Evitare (salvo obbligo): oscurare l'intera pagina; reindirizzare l'utente a una pagina separata per consenso o input.
- Interstitial obbligatori (es. verifica età): esentati, ma consigliato che siano sovrapposti ai contenuti (così Google indicizza almeno parte del contenuto) e **non reindirizzare le richieste HTTP a un'altra pagina** (se tutti gli URL reindirizzano a una pagina, le altre spariscono dai risultati). Per contenuti adulti con verifica età: consentire a Googlebot (verificato) di accedere senza verifica.

## Aggiornamenti principali (core update) della Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/core-updates?hl=it
- Diverse volte l'anno; annunciati nell'elenco degli aggiornamenti del ranking (Search Status Dashboard). Non mirano a siti o pagine specifici. Calare non significa essere "scadenti": altri contenuti sono diventati più pertinenti (analogia della top 20 ristoranti).
- Diagnosi in Search Console: verificare che il rollout sia terminato (dashboard di stato, date inizio/fine); **attendere almeno una settimana completa** dalla fine, poi confrontare con una settimana precedente all'inizio; esaminare pagine e query principali.
  - Calo piccolo (dalla 2ª alla 4ª posizione): nessun intervento drastico; evitare di modificare contenuti che rendono bene.
  - Calo significativo (dalla 4ª alla 29ª): valutazione approfondita.
  - Analizzare separatamente i tipi di ricerca (Web, Immagini, Video, Notizie).
- Calo significativo e prolungato: usare le domande di autovalutazione sui contenuti utili, sul sito nel suo complesso; chiedere a persone fidate non affiliate; esaminare le pagine più colpite.
- Evitare modifiche "rapide" (es. rimuovere elementi perché "si dice" siano un problema SEO); migliorare in modo sostanziale e sostenibile; l'eliminazione di contenuti è l'ultima risorsa.
- Tempi: alcuni effetti in pochi giorni, ma possono servire **diversi mesi**; eventualmente il prossimo core update. Esistono anche core update minori non annunciati. Nessuna garanzia; ranking dinamico.

## Core Web Vitals e i risultati di ricerca di Google
Fonte: https://developers.google.com/search/docs/appearance/core-web-vitals?hl=it
- Metriche di esperienza utente reale: caricamento, interattività, stabilità visiva. Google "consiglia vivamente" buoni CWV; sono in linea con ciò che i sistemi di ranking principali cercano di premiare.
- Soglie "buono":
  - **LCP < 2,5 secondi** (dall'inizio del caricamento).
  - **INP < 200 millisecondi**.
  - **CLS < 0,1**.
- Strumenti: report Core Web Vitals in Search Console; guide web.dev; strumenti di misurazione (web.dev/vitals-tools).

## Carosello di ecosistemi nella Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/ecosystem-carousel?hl=it
- Solo SEE, query su meteo, sport, finanza, traduzioni (desktop e mobile). Clic diretto al sito; ordine stabilito da algoritmi con principi non discriminatori (pertinenza per località e lingua).
- Requisiti: servizi per utenti SEE; contenuti pertinenti in quei domini; essere fonte autorevole/fornitore specializzato. Nessun markup o feed specifico; si esprime interesse tramite modulo. Non pertinente per siti vetrina.

## Attivare le Storie web su Google
Fonte: https://developers.google.com/search/docs/appearance/enable-web-stories?hl=it
- Storie web = formato "storie" basato sul web (video, audio, immagini, animazione, testo) in AMP. Visualizzabili come singolo risultato nella Ricerca (tutte le regioni/lingue) e come scheda in Discover (più probabile in USA, India, Brasile).
- Passi: creare (editor no-code o AMP); verificare AMP valido (Strumento di test Storie web, Controllo URL, AMP Linter); verificare metadati; verificare indicizzazione; seguire le norme sui contenuti.
- Metadati obbligatori per ogni Storia: `publisher-logo-src`, `poster-portrait-src`, `title`, `publisher`.
- Indicizzazione: linkare le storie dal sito o inserirle nella Sitemap; **ogni Storia deve essere canonica** (`link rel="canonical"` autoreferenziale); versioni localizzate segnalate con hreflang; non bloccata da robots.txt o `noindex`.

## Risultati di ricerca estesi (enriched)
Fonte: https://developers.google.com/search/docs/appearance/enriched-search-results?hl=it
- Sottoinsieme interattivo dei risultati avanzati implementato via dati strutturati; consente ricerca per proprietà (es. ricette < 200 calorie). Tipi supportati: **Offerte di lavoro, Ricette, Eventi**.
- Devono rispettare norme sui dati strutturati, nozioni di base della Ricerca e norme di qualità specifiche; se gran parte del sito non le soddisfa, l'intero sito può essere escluso.
- Norme: proprietà obbligatorie (senza → non idoneo); **completezza** (più proprietà consigliate = qualità migliore; uno dei più importanti indicatori di ranking per questi risultati; es. retribuzione nelle offerte di lavoro); pertinenza (es. non etichettare streaming come eventi locali); **solo pagine foglia**, non pagine di elenco/categoria; norme sui contenuti per tipo.
- Dati strutturati duplicati su più pagine (es. stessa offerta in più località) non sono considerati duplicati.

## Definire le informazioni sull'attività su Google
Fonte: https://developers.google.com/search/docs/appearance/establish-business-details?hl=it
- Obiettivo: far riconoscere il sito ufficiale e le informazioni dell'attività nei risultati, nella scheda informativa (Knowledge Panel) e in Google Maps.
- **Rivendicare il Profilo dell'attività** (business.google.com): dopo la verifica si gestiscono indirizzo, contatti, tipo di attività, foto → scheda informativa e Maps.
- **Verificare il sito in Search Console** per stabilirlo come presenza ufficiale e monitorare come Google lo visualizza.
- **Aggiornare la scheda informativa**: Google trova automaticamente nome del sito, contatti, profili social; un rappresentante ufficiale verificato può sovrascriverle.
- Dati strutturati utili a tutti i siti: **`Organization`** (logo del sito nei risultati e nella scheda informativa) e **`BreadcrumbList`** (posizione nella gerarchia).
- Mettere in evidenza i metodi di assistenza clienti (best practice dal blog 2021).
- Troubleshooting: se è passata **almeno una settimana** dall'ultima scansione della pagina con markup, segnalare errori tramite link "Feedback" in fondo alla scheda; testare il markup con il Test dei risultati avanzati; il sistema impiega **circa una settimana** per aggiornare i dettagli.

## Favicon nei risultati di ricerca
Fonte: https://developers.google.com/search/docs/appearance/favicon-in-search?hl=it
- Implementazione: `<link rel="icon" href="/path/to/favicon.ico">` **nell'head della home page**. Valori `rel` supportati: `icon` (anche il legacy `shortcut icon`), `apple-touch-icon`, `apple-touch-icon-precomposed`. `href` relativo o assoluto; può stare su CDN/altro host.
- Ri-scansione: da diversi giorni a parecchie settimane; si può richiedere indicizzazione della home con Controllo URL.
- Linee guida (obbligatorie per l'idoneità; nessuna garanzia):
  - **Una sola favicon per sito, definito dal nome host** (dominio e sottodominio sì; sottodirectory `example.com/news` no).
  - Googlebot-Image deve poter scansionare il file favicon e Googlebot la home page (non bloccati).
  - Deve rappresentare visivamente il brand.
  - **Quadrata (1:1), minimo 8x8 px; consigliata più grande di 48x48 px**. Formati: **BMP, GIF, ICO, PNG, JPEG, PPM, TIFF** (SVG non compare nell'elenco).
  - URL stabile (non cambiarlo spesso).
  - Favicon inappropriate (pornografia, simboli d'odio) sostituite con icona predefinita.
- Per i loghi in Google Ads valgono altre specifiche. Esiste un modulo di feedback (nessuna azione individuale garantita).

## Snippet in primo piano (featured snippet)
Fonte: https://developers.google.com/search/docs/appearance/featured-snippets?hl=it
- Box che mostra prima lo snippet descrittivo; possono comparire anche in "Le persone hanno chiesto anche".
- Disattivazione: `nosnippet` blocca tutti gli snippet (normali e in primo piano); il testo con `data-nosnippet` non compare in nessuno snippet; se ci sono entrambi, prevale `nosnippet`.
- Solo featured snippet: ridurre `max-snippet` (più basso il valore, minore la probabilità); nessuna lunghezza minima esatta (varia per contenuto, lingua, piattaforma); non garantito → per certezza usare `nosnippet`.
- **Non è possibile marcare una pagina come featured snippet**: decidono i sistemi di Google.
- Al clic l'utente viene portato direttamente alla sezione citata (scroll automatico, senza annotazioni del sito); fallback: inizio pagina.

## Modello di accesso flessibile (paywall)
Fonte: https://developers.google.com/search/docs/appearance/flexible-sampling?hl=it
- Per editori con paywall. Due modelli: **monitoraggio** (quota di articoli gratuiti, poi paywall) e **introduzione** (parte iniziale dell'articolo visibile).
- Preferibile quota **mensile** anziché giornaliera; per editori giornalistici previsto **6-10 articoli/utente/mese**, punto di partenza consigliato **10 al mese** per utenti da Ricerca Google.
- La soddisfazione cala notevolmente quando il paywall è mostrato **oltre il 10% delle volte** (circa il 3% del pubblico lo ha visto).
- Contenuti protetti da paywall vanno indicati con dati strutturati per distinguerli dal cloaking; se non si vuole che i contenuti arrivino al browser, scegliere un paywall che non li invii. Rimando alla guida su JavaScript e paywall.
- Poco pertinente per portfolio/professionista (rilevante solo se si mettono contenuti dietro registrazione).

## Discover (Feed personalizzato) e il tuo sito web
Fonte: https://developers.google.com/search/docs/appearance/google-discover?hl=it
- Contenuti idonei automaticamente se **indicizzati** e conformi alle norme sui contenuti di Discover; **nessun tag o dato strutturato speciale**. Idoneità non significa pubblicazione. Possono comparire anche contenuti meno recenti. Violazioni → azioni manuali in Search Console.
- Usa molti indicatori/sistemi della Ricerca (contenuti utili, pensati per le persone).
- Consigli: evitare clickbait e dettagli ingannevoli/esasperati in titolo, snippet, immagini; titoli che catturano l'essenza; evitare sensazionalismo; contenuti attuali, ben raccontati o con prospettiva unica; immagini grandi e di qualità:
  - **larghezza almeno 1200 px**;
  - **oltre 300.000 pixel totali** (es. 1280x720 = 921.600);
  - **proporzioni 16:9** (Google ritaglia automaticamente; se ritagli tu, assicurati che i dettagli importanti siano nella versione indicata in `og:image`);
  - abilitate da **`max-image-preview:large`** o AMP.
- Specificare un'immagine grande e rappresentativa via schema.org o `og:image`; **evitare immagini generiche (es. logo)** e immagini con molto testo.
- Esperienza sulla pagina complessivamente buona.
- Discover può non consigliare: candidature di lavoro, petizioni, moduli, **repository di codice**, satira senza contesto; usa SafeSearch e filtra contenuti scioccanti.
- Il traffico Discover è meno prevedibile, complementare alla ricerca per parole chiave; varia per interessi mutevoli, tipi di contenuto, aggiornamenti della Ricerca.
- Report sul rendimento di Discover in Search Console: impressioni, clic, CTR, **ultimi 16 mesi**, solo sopra una soglia minima di impressioni; include traffico da Chrome.

## Best practice SEO per Google Immagini
Fonte: https://developers.google.com/search/docs/appearance/google-images?hl=it
- Valgono i requisiti tecnici generali, più requisiti specifici per le immagini.
- **Usare elementi HTML `<img>` con `src`** (anche dentro `<picture>`). **Google non indicizza le immagini CSS** (`background-image`).
- **Sitemap di immagini**: per immagini altrimenti non rilevabili; `<image:loc>` può contenere URL di altri domini (CDN); verificare in Search Console anche il dominio della CDN.
- Immagini adattabili: `srcset`/`<picture>` ma **sempre un `src` di riserva**; in `<picture>` fornire un `<img>` con `src` come fallback (HTML 4.8.1).
- **Formati supportati in `img src`: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF**; l'estensione del file deve corrispondere al tipo. Data URI Base64 ammessi ma possono gonfiare la pagina.
- Velocità e qualità: immagini nitide, ottimizzate, adattabili; misurare con PageSpeed Insights.
- **Immagine preferita** (influenza miniatura nei risultati di testo e in Discover; selezione comunque automatica): `primaryImageOfPage` (URL o ImageObject) su `WebPage`, oppure `image` collegata all'entità principale via `mainEntity`/`mainEntityOfPage`, oppure meta `og:image`. Best practice: pertinente e rappresentativa; evitare logo/immagini generiche o con testo; evitare proporzioni estreme; alta risoluzione.
- Title e meta description influenzano come l'immagine appare (seguire linee guida title link e snippet).
- Dati strutturati: possono abilitare risultati avanzati e badge in Google Immagini; la proprietà immagine è obbligatoria per l'idoneità.
- **Testo descrittivo**: immagini vicino a testo pertinente; didascalie e titoli usati; **nomi file brevi e descrittivi** (`my-new-black-kitten.jpg` meglio di `IMG00023.JPG`; evitare `image1.jpg`, `pic.gif`, `1.jpg`); tradurre i nomi file se si localizza (rispettando codifica URL).
- **`alt` è l'attributo più importante**: descrittivo, coerente col contesto, parole chiave usate in modo appropriato; mancante = non valido; keyword stuffing = rischio spam. Esempio ottimale: "Cucciolo dalmata che gioca al riporto". Per `<svg>` inline usare `<title>` (con `aria-labelledby`). L'alt di un'immagine-link funge da anchor text.
- Testare accessibilità e connessioni lente (DevTools). Usare **sempre lo stesso URL per la stessa immagine** (cache, crawl budget).
- Disattivare l'inline linking in Google Immagini: se il referrer è un dominio Google rispondere `200` o `204` senza contenuto; non è cloaking. In alternativa bloccare del tutto l'immagine.
- SafeSearch: etichettare le pagine affinché Google applichi i filtri se opportuno.

## Siti di offerte di lavoro: carosello di aggregatori e chip
Fonte: https://developers.google.com/search/docs/appearance/job-sites?hl=it
- Solo SEE, query su offerte di lavoro. Carosello "Siti di offerte di lavoro" + chip di perfezionamento + "Altri siti". Nessun markup necessario; si esprime interesse via modulo. Non pertinente per siti vetrina.

## Programma di monitoraggio della spedizione (early adopter)
Fonte: https://developers.google.com/search/docs/appearance/package-tracking?hl=it
- **Il programma non accetta più nuovi partner.** API del corriere interrogata da Google: disponibilità quasi totale, risposta media **700 ms**, 95° percentile entro **1000 ms**. Campo obbligatorio `CurrentStatus`; consigliati `DeliveredDate`, `PromisedDate`, `TrackingNumber`, `TrackingURL`, `SupportPhoneNumbers`, `TransitEvents`, `CreateDate`, `PickupDate`, `TimestampEvent`, `LocationEvent`, `CanReschedule`. Vietati dati personali e geografici di mittente/destinatario. Non pertinente.

## Esperienza sulle pagine (page experience)
Fonte: https://developers.google.com/search/docs/appearance/page-experience?hl=it
- I sistemi di ranking principali cercano di premiare una buona esperienza complessiva; non concentrarsi su uno o due aspetti.
- Domande di autovalutazione: CWV buoni? Pagine servite in modo sicuro (HTTPS)? Visualizzazione corretta su mobile? Niente annunci eccessivi che distraggono/interferiscono? Niente interstitial invasivi? Contenuto principale facilmente distinguibile dal resto?
- Risorse: report CWV e **report HTTPS** di Search Console; verifica connessione sicura in Chrome; guida interstitial; **Lighthouse** (anche usabilità mobile); metriche annunci CrUX (sperimentali).
- FAQ:
  - **Non esiste un singolo "indicatore di esperienza sulle pagine"**.
  - **I Core Web Vitals sono usati dai sistemi di ranking**; buoni punteggi non garantiscono posizioni alte; inseguire il punteggio perfetto solo per SEO "potrebbe non essere il modo migliore per impiegare il tuo tempo".
  - Gli altri aspetti dell'esperienza (oltre ai CWV) non contribuiscono direttamente al ranking, ma sono in linea con ciò che i sistemi premiano.
  - Valutazione in genere **per pagina**, con alcune valutazioni a livello di sito.
  - La pertinenza prevale: Google mostra il contenuto più pertinente anche con esperienza scadente; l'esperienza conta quando ci sono molti contenuti utili equivalenti.

## Siti di luoghi: carosello di aggregatori e chip
Fonte: https://developers.google.com/search/docs/appearance/places-sites?hl=it
- Solo Turchia, query su attività locali e hotel. Nessun markup; modulo di interesse. Non pertinente.

## Fonti preferite (Preferred sources)
Fonte: https://developers.google.com/search/docs/appearance/preferred-sources?hl=it
- Se un utente seleziona il sito come fonte preferita, i contenuti hanno più probabilità di comparire in "Notizie principali" con badge "preferita"; anche in AI Mode e AI Overview possono avere il badge "preferita".
- Disponibile globalmente per "Notizie principali" in tutte le lingue della Ricerca; in AI Mode/AI Overview dove disponibili. Per AI Mode/Overview il sito deve essere **incluso nelle funzionalità di AI generativa della Ricerca in Search Console**.
- Idonei solo siti a livello di **dominio o sottodominio** (non sottodirectory come `/blog`). Verificare la presenza nello strumento Preferenze fonti (google.com/preferences/source).
- Metodi (non obbligatori né sequenziali):
  - **JS standard (consigliato)**: `<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>` (preferibilmente nell'head) + `<div google-add-preferred-source-btn></div>`; attributi `data-theme="light|dark"` (default light) e `data-lang` (override lingua; default lingua del browser).
  - **JS avanzato**: import ESM da `publisher.mjs` con `preferredSource.init({theme, lang})` e `preferredSource.addPreferredSource()` su un trigger custom; oppure script con `preferred-sources-control="manual"` + coda `self.PREFERRED_SOURCE`. Senza l'attributo manual, gli elementi con l'attributo vengono inizializzati subito.
  - **Deep link** (se non si può usare JS, anche su social/newsletter): `https://www.google.com/preferences/source?q=example.com`, come link testuale o immagine; asset ufficiali scaricabili.
- Rilevante soprattutto per publisher di notizie; per i siti d'esempio è marginale.

## Date di pubblicazione nella Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/publication-dates?hl=it
- Google stima la data di pubblicazione/aggiornamento da **molteplici fattori** (nessuno singolo) e può mostrarla nei risultati se utile. Nessuna garanzia di visualizzazione.
- Come fornirla: **data visibile e in evidenza** con etichette ("Pubblicazione", "Data di pubblicazione", "Ultimo aggiornamento", "Aggiornamento"); si può fornire una o entrambe. Inoltre dati strutturati di un sottotipo di `CreativeWork` (`Article`, `BlogPosting`, `VideoObject`...) con `datePublished` e/o `dateModified`.
- Best practice:
  - La data è obbligatoria, l'ora no; consigliato fornire ora e fuso orario (ISO 8601, considerando l'ora legale).
  - **Coerenza** tra data visibile e dati strutturati (ora e fuso facoltativi nel testo visibile).
  - **Niente date future** né la data dell'evento descritto (per gli eventi usare il markup Event).
  - Ridurre al minimo altre date nella pagina se Google sceglie date sbagliate.
  - Per Google News, linee guida aggiuntive.

## Guida ai sistemi di ranking della Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/ranking-systems-guide?hl=it
- I sistemi funzionano **a livello di pagina**, con anche indicatori/classificatori **a livello di sito** (positivi o negativi non determinano da soli il ranking di tutte le pagine).
- Sistemi attivi descritti:
  - **BERT**: comprensione di come le combinazioni di parole esprimono significati e intenti.
  - **Sistemi per le emergenze**: crisi personali (numeri di emergenza per query su suicidio, violenza, veleni, droghe), Allerte SOS.
  - **Deduplicazione**: mostra solo i risultati più pertinenti tra pagine molto simili; una pagina promossa a featured snippet non viene ripetuta nella prima pagina.
  - **Domini a corrispondenza esatta**: le parole nel dominio sono uno dei tanti fattori, ma non viene dato troppo credito a domini creati per corrispondere a query (es. "posti migliori dove pranzare").
  - **Contenuti aggiornati (freshness)**: per query dove ci si aspetta freschezza.
  - **Analisi dei link e PageRank**: i link tra pagine aiutano a capire argomento e utilità; PageRank evoluto ma ancora parte dei sistemi principali.
  - **Notizie locali**.
  - **MUM**: non usato per il ranking generale, solo applicazioni specifiche (vaccini COVID-19, callout dei featured snippet).
  - **Corrispondenza neurale**: rappresentazioni di concetti in query e pagine.
  - **Contenuti originali**: promuovono contenuti originali (anche reportage) rispetto a chi li cita; supporto al markup canonical.
  - **Retrocessione basata sulla rimozione**: molte richieste valide per copyright, diffamazione, contraffazione, ordini del tribunale, informazioni personali/doxxing/immagini intime non consensuali → retrocessione di altri contenuti del sito.
  - **Ranking dei passaggi**: AI che identifica singole sezioni/passaggi di una pagina per valutarne la pertinenza.
  - **RankBrain**: correlazione tra parole e concetti (pertinenza anche senza le parole esatte).
  - **Informazioni affidabili**: promuovono pagine autorevoli, retrocedono contenuti scadenti; avvisi sui contenuti per argomenti in rapida evoluzione.
  - **Sistema delle recensioni**.
  - **Diversità dei siti**: in genere **non più di due schede dello stesso sito** nei risultati principali (salvo particolare pertinenza); i sottodomini di solito contano come lo stesso sito.
  - **Rilevamento dello spam** (incluso SpamBrain).
- Sistemi ritirati (integrati nel core): **Contenuti utili** (helpful content, 2022 → integrato nel core a **marzo 2024**), Hummingbird (2013), Panda (2011 → core nel 2015), Penguin (2012 → core nel 2016).

## Sistema delle recensioni
Fonte: https://developers.google.com/search/docs/appearance/reviews-system?hl=it
- Premia recensioni di alta qualità: analisi approfondita, ricerca originale, scritte da esperti/appassionati; penalizza contenuti scarni che riassumono prodotti/servizi.
- Valuta articoli, post, pagine proprietarie che danno consigli, opinioni o analisi; **non valuta recensioni di terze parti** (es. recensioni degli utenti nella pagina prodotto). Qualsiasi argomento (prodotti, media, servizi, attività).
- Valutazione principalmente a livello di pagina; possibile valutazione a livello di sito se ci sono molte recensioni.
- Lingue: inglese, spagnolo, tedesco, francese, **italiano**, vietnamita, indonesiano, russo, olandese, portoghese, polacco.
- I dati strutturati Product possono aiutare a identificare le recensioni prodotto, ma Google non si basa solo su di essi. Recupero possibile nel tempo dopo i miglioramenti.

## Badge del profilo della Ricerca (Search profiles)
Fonte: https://developers.google.com/search/docs/appearance/search-profiles?hl=it
- Il **profilo della Ricerca** riunisce contenuti dal web e dai social (Instagram, TikTok, YouTube, X, Facebook, sito) in un'unica destinazione su Google; chi lo segue ha più probabilità di vedere quei contenuti in Discover.
- Dopo aver rivendicato il profilo: URL `https://profile.google.com/@handle`; scaricare gli asset del badge; snippet: `<a href="https://profile.google.com/@example" aria-label="Find us on Google Search"><img src="/path/to/google-search-badge.svg" alt="Google Search"></a>`, oppure link testuale (firme, newsletter, bio).
- Linee guida del brand: touch target almeno **48x48 dp su Android e 44x44 px su iOS/web**; non alterare l'icona "Super G"; non mescolare badge monocromatici e colorati; se usato insieme al badge Fonti preferite, dare più enfasi al pulsante del profilo e non usare la "Super G" associata al badge Fonti preferite.
- Potenzialmente rilevante per personal brand e creator (rivendicazione del profilo: azione manuale off-site).

## Nome del sito nella Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/site-names?hl=it
- Il nome del sito (diverso dal title link) rappresenta l'intero sito; generazione **completamente automatica** da contenuti della home page e riferimenti sul web. Disponibile in tutte le lingue, mobile e desktop, per siti a livello di dominio e sottodominio.
- Segnali: **dati strutturati `WebSite` nella home page (il più importante)**, poi `og:site_name`, `<title>`, intestazioni e altro testo della home. Google non modifica manualmente i nomi.
- Scelta del nome: univoco, non fuorviante, conforme alle norme; conciso e comunemente riconosciuto ("Google" e non "Google LLC"); nessun limite di caratteri ma può essere troncato; **evitare nomi generici** ("I migliori dentisti in Iowa"); usarlo **coerentemente** in tutta la home; fornire `alternateName`. Google in genere non usa lo stesso nome per due siti globali diversi; può preferire un acronimo.
- Linee guida tecniche:
  - **Un solo nome per sito** (dominio o sottodominio); `www` e `m` sono equivalenti al dominio; **sottodirectory non supportate**.
  - `WebSite` deve stare **nella home page** (URI radice; `example.com/de/index.html` non lo è). Se il sottodominio non ha markup, può essere usato come riserva il nome del dominio.
  - Home page scansionabile (non bloccata).
  - Home page duplicate (HTTP/HTTPS, www/non-www): **stessi dati strutturati su tutti i duplicati**, non solo sulla canonica.
  - Se esiste già un nodo `WebSite`, nidificare lì le proprietà (evitare un secondo blocco).
- Proprietà obbligatorie: **`name`** (Text) e **`url`** (URL della home page canonica, es. `https://example.com/`). Consigliata: **`alternateName`** (Text, anche array in ordine di preferenza). Formati: JSON-LD, RDFa, microdati; serve solo sulla home page.
- Test: validator.schema.org (**il Test dei risultati avanzati non supporta i nomi dei siti**); Controllo URL (home non bloccata da robots.txt, `noindex` o login); richiedere nuova scansione; tempi da giorni a settimane.
- Se il nome preferito non viene scelto: verificare markup, errori, coerenza con altre fonti della home, non usare sottodirectory, redirect funzionanti (il nome riflette la destinazione del redirect), stesso nome su HTTP/HTTPS; attendere ri-elaborazione anche per le pagine interne. Poi: aggiungere `alternateName`; aggiungere il **dominio in minuscolo** (`example.com`) come ultimo `alternateName` di riserva; come ultima istanza usare il dominio in minuscolo come `name`.

## Sitelink
Fonte: https://developers.google.com/search/docs/appearance/sitelinks?hl=it
- Link dello stesso dominio raggruppati sotto un risultato; derivati dall'analisi della **struttura dei link** del sito; mostrati solo quando utili. **Completamente automatici** (in futuro forse suggerimenti dei proprietari).
- Best practice: titoli di pagina e intestazioni informativi, pertinenti, compatti; struttura logica con link alle pagine importanti da altre pagine pertinenti; **anchor text interni concisi e pertinenti**; evitare ripetizioni nei contenuti.
- Per rimuovere un sitelink: eliminare la pagina o usare `noindex`.

## Controllare gli snippet nei risultati di ricerca
Fonte: https://developers.google.com/search/docs/appearance/snippet?hl=it
- Lo snippet è generato **automaticamente, principalmente dai contenuti della pagina**, in base alla query (può variare per ricerca); Google usa la **meta description** quando descrive la pagina meglio del contenuto. Google non modifica manualmente gli snippet.
- Controlli: `nosnippet` (nessuno snippet), `max-snippet:[number]` (lunghezza massima), attributo `data-nosnippet` (esclude parti della pagina).
- Meta description: **nessun limite di lunghezza**, ma troncata in base alla larghezza del dispositivo. Nei CMS (Wix, WordPress, Blogger) usare le impostazioni SEO/head.
- Best practice:
  - **Descrizioni univoche per ogni pagina**; descrizioni a livello di sito per home/aggregazioni; se manca tempo, dare priorità a home e pagine più visitate.
  - Includere informazioni pertinenti (autore, data, fonti; per prodotti prezzo, età, produttore); non serve forma discorsiva.
  - Generazione programmatica appropriata e consigliata per grandi siti basati su database, purché distinte e leggibili.
  - Evitare lunghe stringhe di parole chiave (meno probabile che vengano usate).
  - Esempi da evitare: elenco di keyword, stessa descrizione per ogni articolo, testo che non riassume la pagina, troppo breve ("Matita meccanica"). Da preferire: cosa offre + orari + sede; riassunto specifico e dettagliato.
- Deep link "Leggi tutto" (link a sezioni nello snippet): contenuti **immediatamente visibili** (non nascosti in sezioni espandibili o tab); non usare JS per forzare la posizione di scroll al caricamento; se si usa History API o `window.location.hash` al caricamento, **non rimuovere il frammento hash** dall'URL.

## Esperienze della Ricerca in Sudafrica: badge e chip
Fonte: https://developers.google.com/search/docs/appearance/south-africa-features?hl=it
- Solo piattaforme sudafricane idonee: badge "Sudafrica" (non modifica il ranking) e chip di perfezionamento per viaggi, noleggio auto, autobus, prodotti, consegna cibo; anche per annunci viaggi/shopping. Nessun markup; modulo di interesse. Non pertinente.

## Aggiornamenti relativi allo spam
Fonte: https://developers.google.com/search/docs/appearance/spam-updates?hl=it
- I sistemi antispam (incluso **SpamBrain**, basato su AI) sono sempre attivi; i miglioramenti significativi sono "spam update", annunciati nell'elenco degli aggiornamenti del ranking.
- I siti che violano le norme sullo spam possono avere ranking più basso o non comparire. Il recupero è possibile se i sistemi rilevano **per un periodo di mesi** la conformità.
- Negli aggiornamenti sui **link di spam**, il vantaggio di ranking dato da quei link viene neutralizzato e **non è recuperabile** (le modifiche potrebbero non portare miglioramenti).

## Unità di fornitori
Fonte: https://developers.google.com/search/docs/appearance/supplier-unit?hl=it
- Solo SEE; compare **solo se è mostrata l'unità di aggregatori** (hotel, voli, treni/autobus a lunga percorrenza, prodotti, attività locali). Per fornitori diretti (singoli hotel, compagnie aeree, attività fisiche, fornitori di servizi es. idraulici).
- Requisiti: servire utenti SEE ed essere fornitore diretto per quelle query. **Non servono dati aggiuntivi oltre a quelli ottenuti dalla scansione web**; i feed possono migliorare i risultati. Marginalmente pertinente per una professionista locale nel SEE (query "attività locali"), senza azioni specifiche richieste.

## Link dei titoli (title link)
Fonte: https://developers.google.com/search/docs/appearance/title-link?hl=it
- Il title link è il titolo cliccabile del risultato; generazione **completamente automatica** da contenuti della pagina e riferimenti sul web. Google non lo modifica manualmente.
- Best practice:
  - **Ogni pagina deve avere un `<title>`**.
  - Testo **descrittivo e conciso**; evitare titoli vaghi come "Home" o "Profilo"; evitare testi inutilmente lunghi (nessun limite di lunghezza, ma troncato in base alla larghezza del dispositivo).
  - Evitare keyword stuffing ("Foobar, foo bar, foo-bar").
  - Evitare testo ripetuto/boilerplate: titolo distinto per ogni pagina; aggiornare dinamicamente il title per rispecchiare i contenuti effettivi.
  - Brand conciso: in home si può aggiungere una breve descrizione; nelle altre pagine nome del sito all'inizio o alla fine, separato da delimitatore (trattino, due punti, barra verticale).
  - **Titolo principale chiaro**: intestazione principale distinta (carattere più grande, nel primo `<h1>` visibile); più intestazioni con lo stesso peso confondono.
  - Attenzione al blocco robots.txt: una pagina bloccata può comunque essere indicizzata e il titolo sarà generato da fonti esterne (es. anchor text di altri siti); per non indicizzare usare `noindex`.
  - Stessa **lingua e sistema di scrittura** del contenuto principale (niente traslitterazioni).
  - Evitare prezzi dei voli nei title.
- Fonti usate da Google: `<title>`, titolo visivo principale, intestazioni (`<h1>`), **`og:title`**, testo grande/in risalto, altro testo, anchor text nella pagina, testo dei link che puntano alla pagina, dati strutturati `WebSite`.
- Aggiornamenti rilevati dopo nuova scansione (giorni o settimane); si può richiedere la scansione.
- Problemi comuni che portano Google a riscrivere il titolo: `<title>` semivuoti (es. `| Nome del sito`); `<title>` obsoleti (anno non aggiornato); imprecisi rispetto al contenuto; micro-boilerplate (stesso title per più pagine di un sottoinsieme); nessun titolo principale evidente (Google può usare la prima intestazione); lingua/script non corrispondenti; nome del sito duplicato (Google può ometterlo se già mostrato come nome del sito).

## Elenco dei luoghi più apprezzati
Fonte: https://developers.google.com/search/docs/appearance/top-places-list?hl=it
- Risultato avanzato che mostra gli elenchi online "luoghi più apprezzati" in cui un'attività è menzionata; **solo per attività con sede fisica**.
- Requisiti per il sito che pubblica l'elenco: curato, autentico, indipendente, **non sponsorizzato**; non composto da frasi basate su modelli da dati automatici; niente linguaggio volgare/offensivo.
- Opt-out: disattivare la visualizzazione nei risultati di ricerca locali e altre proprietà Google. Per la professionista locale: dipende da menzioni su siti terzi (off-site).

## Risultati tradotti
Fonte: https://developers.google.com/search/docs/appearance/translated-results?hl=it
- Google può tradurre title link e snippet di risultati in lingua diversa dalla query. Lingue di destinazione: arabo, bengalese, coreano, francese, gujarati, hindi, indonesiano, inglese, kannada, malayalam, marathi, persiano, portoghese, spagnolo, tamil, tedesco, telugu, thailandese, turco, urdu, vietnamita (**l'italiano non è nell'elenco**). Mobile e desktop.
- Al clic viene mostrata la pagina tradotta automaticamente (Google non ospita le pagine; JS e immagini di solito funzionano); possibile vedere l'originale.
- Monitoraggio: filtro "Aspetto nella ricerca" nel report Rendimento.
- Attiva di default; opt-out da tutte le funzionalità di traduzione con `notranslate` via `<meta name="robots" content="notranslate">`, `<meta name="googlebot" content="notranslate">` o `X-Robots-Tag: notranslate`.

## Best practice SEO per i video
Fonte: https://developers.google.com/search/docs/appearance/video?hl=it
- I video possono comparire nella pagina principale dei risultati, modalità Video, Google Immagini, Discover.
- **Farli trovare**: usare elementi `<video>`, `<embed>`, `<iframe>`, `<object>`; **non usare identificatori di frammento (#) per caricare il video**; se inserito via JS deve comparire nell'HTML renderizzato visto in Controllo URL; con API multimediali (Media Source) inserire comunque il contenitore video anche se l'API fallisce; **non richiedere azioni dell'utente (scroll, clic, digitazione) per caricare il video**. Metadati: dati strutturati (`VideoObject`), Sitemap video, Open Graph.
- **Indicizzazione**: pagina di visualizzazione indicizzata **e con buona posizione** (indicizzata non basta); video incorporato nella pagina; non nascosto dietro altri elementi (paywall → dati strutturati per contenuti protetti); **miniatura valida a URL stabile**.
- Formati video supportati: 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, QVT, RAM, RM, VOB, WebM, WMV, XAP. **Data URL non supportati.**
- URL stabili per miniatura e file video (alcune CDN usano URL a scadenza rapida); si può mostrare `contentUrl` solo a Googlebot verificato.
- **Pagina di visualizzazione dedicata** per ogni video (scopo principale = guardare un video) per idoneità a risultati video, momenti chiave, badge DAL VIVO. Non sono pagine di visualizzazione: post che recensisce un video incorporato, pagina prodotto con video 360°, pagine categoria con più video, recensione film con trailer. Titolo e descrizione univoci per ogni pagina. Lo stesso video può stare anche in altre pagine (idonee come risultato di testo o immagine con badge video).
- Player di terze parti (YouTube, Vimeo, Facebook): Google può indicizzare il video sia sulla tua pagina sia sulla piattaforma; fornire comunque dati strutturati e Sitemap video; verificare che l'host consenta il recupero del file.
- URL: pagina di visualizzazione (`<loc>`), player (`embedUrl` / `<video:player_loc>`), file video (`contentUrl` / `<video:content_loc>`).
- **Miniatura**: tramite `poster` di `<video>`, `<video:thumbnail_loc>`/`<media:thumbnail>`, `thumbnailUrl`, `og:video:image`; stesso URL in tutte le fonti. Formati BMP, GIF, JPEG, PNG, WebP, SVG, AVIF; **minimo 60x30 px**; accessibile a Googlebot e Googlebot-Image; **almeno l'80% dei pixel con alfa > 250**.
- Dati strutturati coerenti con il video; `thumbnailUrl`, `name`, `description` **univoci per ogni video**. Nessuna garanzia delle funzionalità.
- Funzionalità: **anteprime video** (consentire il recupero del file; durata massima con `max-video-preview`); **momenti chiave** (rilevamento automatico, oppure `Clip` — tutte le lingue — o `SeekToAction` — lingue: cinese, coreano, francese, giapponese, inglese, italiano, olandese, portoghese, russo, spagnolo, tedesco, turco — oppure timestamp nella descrizione YouTube; disattivazione con `nosnippet`); **badge DAL VIVO** con `BroadcastEvent`.
- Consentire il recupero del file: non bloccare l'URL dei byte (es. M3U8) con `noindex`/robots.txt; URL stabile; `contentUrl` di tipo supportato; sia l'host della pagina sia lo streaming server devono avere capacità adeguata; verificare in Search Console lo spazio CDN.
- Rimozione: richiesta di rimozione per la pagina; permanente con `404`, `noindex` o autenticazione; oppure data di scadenza (`expires` / `<video:expiration_date>`): con data passata il video non appare nei risultati video (attenzione a non impostarla per errore). Restrizioni per paese: `regionsAllowed` / `ineligibleRegion` o `<video:restriction relationship="allow|deny">` (un solo tag per video, codici ISO 3166-1).
- SafeSearch; Search Console: report Indicizzazione video, report risultati avanzati video, report Rendimento con filtro aspetto video.

## Galleria degli elementi visivi della Ricerca Google
Fonte: https://developers.google.com/search/docs/appearance/visual-elements-gallery?hl=it
- Tipi principali di risultato: **risultato di testo**, **risultato avanzato** (in genere da dati strutturati), **risultato di immagini**, **risultato video**, **funzionalità di esplorazione**. L'aspetto varia per dispositivo, paese, lingua, ecc.
- **Attribuzione**: favicon, nome del sito, URL visibile (dominio + breadcrumb). Controllabili rispettivamente via favicon, `WebSite`, dati strutturati breadcrumb.
- Risultato di testo: attribuzione, title link, snippet, data di pubblicazione, gruppo di sitelink (2+ link dallo stesso dominio o varianti localizzate; anche intestazioni/anchor della pagina), **immagine del risultato di testo** (immagine più pertinente della pagina per la query; seguire best practice immagini), **attributi avanzati** (es. stelle recensioni, info ricette; da dati strutturati).
- Risultato immagini: miniatura + attribuzione. Risultato video: miniatura, title link, attribuzione, data di caricamento (dai metadati).
- Funzionalità di esplorazione: ricerche correlate e domande correlate ("Le persone hanno chiesto anche", con featured snippet all'espansione); **non controllabili**, ma utili per scegliere argomenti da trattare.

## Norme relative ai contenuti delle Storie web
Fonte: https://developers.google.com/search/docs/appearance/web-stories-content-policy?hl=it
- Per Discover e Ricerca devono rispettare norme Discover, nozioni di base e norme generali; per esperienze più complete (carosello) anche queste norme aggiuntive. Violazioni gravi → esclusione permanente dalle esperienze più complete.
- Vietato: violazione di copyright; storie con molto testo (**la maggior parte delle pagine oltre 180 caratteri** → possibile non idoneità; consigliati video brevi, **< 60 s per pagina**); risorse sgranate/pixelate; mancanza di narrazione; storie incomplete o che richiedono clic su altri siti/app per informazioni essenziali; storie troppo commerciali (affiliazione ammessa solo in piccola parte; annunci secondo linee guida AMP).

## Best practice per la creazione di Storie web
Fonte: https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices?hl=it
- Storytelling: video prima di tutto; offrire la propria prospettiva; arco narrativo.
- Progettazione: **circa 280 caratteri per pagina**; non nascondere il testo; evitare testo in immagine; animazioni con criterio; CTA specifici per Storie (togliere quelli di Instagram/Snapchat/YouTube); risorse a tutto schermo; niente risorse a bassa risoluzione; logo in copertina; video **< 15 s per pagina, max 60 s**; audio di qualità di almeno 5 s; avanzamento automatico per storie solo video.
- SEO (una Storia è una pagina web): contenuti di qualità; **titolo < 90 caratteri, consigliato < 70**; niente `noindex`, aggiungerle alla Sitemap; **auto-canoniche**; metadati (title, description, dati strutturati, OGP, Twitter Card); consigliati dati strutturati (Article), alt alle immagini, linkarle dal sito (home/categorie o pagina `/stories`), URL coerenti con la strategia del sito (non serve indicare "story" nell'URL), allegati di pagina AMP, sottotitoli (non incorporati nel video), testo nel `title` di `amp-video` se la storia è solo video, supporto orientamento orizzontale per comparire su desktop.
- Tecnico: AMP valido (validator.ampproject.org); niente testo nell'immagine poster; **poster `poster-portrait-src` almeno 640x853 px, 3:4**; **logo `publisher-logo-src` almeno 96x96 px, 1:1**; consigliato `og:image`.

---

# API Indexing (v3)

> Nota trasversale: **l'API Indexing può essere usata SOLO per pagine con `JobPosting` o con `BroadcastEvent` incorporato in un `VideoObject`** (offerte di lavoro e live streaming). Non è uno strumento generico per far indicizzare pagine di un portfolio o di un sito professionale.

## Autorizzare le richieste
Fonte: https://developers.google.com/search/apis/indexing-api/v3/authorizing?hl=it
- Ogni richiesta deve includere un token di autorizzazione; **solo OAuth 2.0** (nessun altro protocollo). Flusso: registrare l'app nella Google API Console (ID client, secret), attivare l'API Indexing, richiedere l'ambito, consenso, token di accesso a breve durata (eventuali refresh token).
- Ambito: **`https://www.googleapis.com/auth/indexing`** (lettura/scrittura). Le librerie client gestiscono parte del processo.

## Errori dell'API Indexing
Fonte: https://developers.google.com/search/apis/indexing-api/v3/core-errors?hl=it
- Elenco degli errori globali delle API Google per codice HTTP (301, 303, 304, 307, 400, 401, 402, 403, 404, 405, 409, 410, 412, 413, 416, 417, 428, 429, 500, 501, 503) con i relativi `reason` (es. `badRequest`, `invalidParameter`, `authError`, `expired`, `accessNotConfigured`, `insufficientPermissions`, `rateLimitExceeded`, `quotaExceeded`, `backendError`...). Formato JSON con `error.errors[].domain/reason/message/locationType/location`, `code`, `message`.
- Errori specifici Indexing API (in tutti i casi la richiesta è respinta e Google **non** scansiona l'URL):
  - 400: `'url' attribute is required`; `'url' is not in standard URL format`; `'type' attribute is required and must be 'URL_REMOVED' or 'URL_UPDATED'`; `Invalid value at 'url_notification.type'`.
  - 403: `Permission denied. Failed to verify the URL ownership.` (verifica di proprietà non completata o URL non posseduto).
  - 429: `Insufficient tokens for quota 'indexing.googleapis.com/default_requests'` (quota superata).

## Installare librerie client
Fonte: https://developers.google.com/search/apis/indexing-api/v3/libraries?hl=it
- API basata su HTTP+JSON (qualsiasi client HTTP va bene); librerie client Google disponibili per Go, Java (Maven/Gradle), JavaScript, .NET (NuGet `Google.Apis`), Node.js, Objective-C, PHP, Python (`pip install --upgrade google-api-python-client`; v1 richiede Python 2.7+, v2 Python 3.7+; su App Engine vanno copiate nell'app), Ruby (`gem install google-api-client`). Explorer API per prove dal browser.

## Prerequisiti per l'API Indexing
Fonte: https://developers.google.com/search/apis/indexing-api/v3/prereqs?hl=it
- Passi: creare un progetto nella Google API Console e attivare l'API; creare un **account di servizio** e una chiave (consigliato JSON; è l'unica copia, custodirla in modo sicuro); **verificare la proprietà del sito in Search Console** (proprietà Dominio o prefisso URL) e **aggiungere l'email dell'account di servizio come proprietario (delegato)** (`client_email` del JSON, formato `...@...iam.gserviceaccount.com`); ottenere un token OAuth dalla chiave privata.
- Requisiti richiesta: ambito `https://www.googleapis.com/auth/indexing`, endpoint documentati, token dell'account di servizio, corpo come da guida. Esempi in Python, Java, PHP, Node.js (endpoint `https://indexing.googleapis.com/v3/urlNotifications:publish`, corpo `{"url": ..., "type": "URL_UPDATED"}`).

## Guida rapida all'API Indexing
Fonte: https://developers.google.com/search/apis/indexing-api/v3/quickstart?hl=it
- Consente di notificare a Google aggiunta/rimozione di pagine con offerte di lavoro o video in live streaming, così Google pianifica una nuova scansione. **Solo pagine con `JobPosting` o `BroadcastEvent` in `VideoObject`.**
- Operazioni: aggiornare un URL, rimuovere un URL, conoscere lo stato della notifica, batch fino a **100 chiamate** per richiesta HTTP.
- Per siti con molte pagine di breve durata è consigliata rispetto alle Sitemap, ma va comunque inviata una Sitemap per l'intero sito.
- Tutti i contenuti inviati sono soggetti a rigoroso rilevamento dello spam; abusi (più account per superare le quote) → revoca dell'accesso.
- Quota predefinita **200** per onboarding/test; uso reale richiede approvazione.

## Quota e prezzi
Fonte: https://developers.google.com/search/apis/indexing-api/v3/quota-pricing?hl=it
- Quote predefinite: `DefaultPublishRequestsPerDayPerProject` = **200/giorno** (include `URL_UPDATED` e `URL_DELETED`; reset a mezzanotte ora del Pacifico, fino a 24 h per una nuova quota); `DefaultMetadataRequestsPerMinutePerProject` = **180/minuto**; `DefaultRequestsPerMinutePerProject` = **380/minuto**.
- Quota visibile nella console API. Quota superiore e approvazione (per pagine `JobPosting`/`BroadcastEvent`) tramite modulo; la quota può aumentare o diminuire in base alla qualità dei documenti. **Uso gratuito.**

## Risorsa REST urlNotifications
Fonte: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rest/v3/urlNotifications?hl=it
- `UrlNotification`: `url` (deve essere di proprietà di chi notifica; per `URL_UPDATED` deve essere scansionabile), `type` (`URL_NOTIFICATION_TYPE_UNSPECIFIED`, `URL_UPDATED`, `URL_DELETED`), `notifyTime` (timestamp RFC3339 UTC, ignorato in richiesta).
- Metodi: `getMetadata` (metadati di un documento), `publish` (notifica aggiornamento/eliminazione).

## Usare l'API Indexing
Fonte: https://developers.google.com/search/apis/indexing-api/v3/using-api?hl=it
- Linee guida: norme sullo spam applicate; `Content-Type: application/json` obbligatorio su `publish`; un URL per richiesta o batch fino a 100; non eludere i limiti con più account.
- Aggiornare: `POST https://indexing.googleapis.com/v3/urlNotifications:publish` con `{"url": "...", "type": "URL_UPDATED"}`; risposta `HTTP 200` = Google potrebbe ri-scansionare a breve (corpo `UrlNotificationMetadata`); inviare nuova notifica se il contenuto cambia.
- Rimuovere: prima la pagina deve restituire **404 o 410** o avere `<meta name="robots" content="noindex" />`; poi `type: "URL_DELETED"`.
- Stato: `GET https://indexing.googleapis.com/v3/urlNotifications/metadata?url=ENCODED_URL` (URL codificato); indica solo l'ultima notifica ricevuta (`latest_update`, `latest_remove`), **non** quando Google indicizza/rimuove.
- Batch: endpoint `https://indexing.googleapis.com/batch`, multipart/mixed; ogni parte max **1 MB**; **la quota è conteggiata per URL** (10 richieste in un batch = 10 di quota).

---

# Case study

## Case study (indice)
Fonte: https://developers.google.com/search/case-studies?hl=it
- Pagina indice dei case study SEO, senza contenuto sostanziale.

## SEO per i video: tre publisher internazionali (2023)
Fonte: https://developers.google.com/search/case-studies/cross-regional-video-seo-case-study?hl=it
- Strumenti: best practice video, report Indicizzazione dei video, report Stato dei risultati avanzati, report Rendimento, Test dei risultati avanzati.
- Weather.com: dopo il markup video, **pagine video indicizzate più che raddoppiate (2x)**.
- Italiaonline: dati strutturati video → **+841% clic** sui video, **+353% impressioni**, **-85% errori di indicizzazione** video.
- ABP News (8 lingue): dati strutturati, best practice, momenti chiave → **+30% traffico** da Google.

## Eventbrite (2018)
Fonte: https://developers.google.com/search/case-studies/eventbrite-case-study?hl=it
- Dati strutturati `Event` (dal 2015) su tutti gli eventi, con modello di base, poche modifiche; proprietà consigliate aggiunte; verifica con Search Console e (allora) Strumento di test per i dati strutturati. Risultati estesi per eventi (USA).
- Risultato: circa **+100%** della crescita tipica anno su anno del traffico da Google verso le pagine eventi (Google Analytics); differenze visibili in **2-3 settimane**.

## Jobrapido (2018)
Fonte: https://developers.google.com/search/case-studies/jobrapido-case-study?hl=it
- Markup `JobPosting` per l'esperienza offerte di lavoro: **+182% traffico organico**, **+395% registrazioni** da organico, **-35% frequenza di rimbalzo**.

## Immagini grandi in Discover (2021)
Fonte: https://developers.google.com/search/case-studies/large-images-case-study?hl=it
- `max-image-preview:large` (introdotto nel 2020) consente a Google di mostrare immagini in formato grande (es. Discover).
- Kirbie's Cravings (food blog personale): **+79% CTR** con una riga di HTML. Istoé: **+30% CTR**, **+332% clic** in 6 mesi.
- Consiglio esplicito: se il sito ha immagini grandi, aggiungere `max-image-preview:large`.

## Monster India (2019)
Fonte: https://developers.google.com/search/case-studies/monster-india-case-study?hl=it
- `JobPosting` da progetto pilota (aprile 2018) a tutte le offerte: **+94% traffico organico** sulle pagine dettaglio, **+10% candidature**; esteso ad altri paesi.

## MX Player (2021)
Fonte: https://developers.google.com/search/case-studies/mx-case-study?hl=it
- Dati strutturati video + invio frequente di Sitemap video → **3x traffico** da Google, **+100% visualizzazioni di pagina video per sessione** in 6 mesi (ricerca web, scheda Video, Discover).

## Rakuten Recipe (2018)
Fonte: https://developers.google.com/search/case-studies/rakuten-case-study?hl=it
- `Recipe` (dal 2012) implementato via CMS in due settimane; uso di Search Console e test dei dati strutturati (anche su AMP). Risultato: **traffico da motori di ricerca 2,7x**, **durata sessione 1,5x**.

## Saramin (2020)
Fonte: https://developers.google.com/search/case-studies/saramin-case-study?hl=it
- Primo anno: registrazione in Search Console e correzione errori di scansione → **+15% traffico organico**.
- Poi: **rimozione dei meta tag pieni di parole chiave inutili**, URL canonici, rimozione contenuti duplicati, dati strutturati `JobPosting`, breadcrumb, stipendio stimato; uso di guide per sviluppatori e Centro assistenza; strumenti: test dati strutturati, test ottimizzazione mobile, test AMP, PageSpeed Insights.
- Risultati: errori del grafico Copertura progressivamente risolti; **+102% traffico organico** anno su anno nel picco di settembre 2019; **+93% nuove registrazioni**, **+9% conversioni**.

## Vidio (2024)
Fonte: https://developers.google.com/search/case-studies/vidio-case-study?hl=it
- `VideoObject` sul catalogo esistente mantenendo M3U8/HLS (formato supportato), ma M3U8 può essere difficile da recuperare (riferimenti a parti inaccessibili) → **URL stabili e accessibili a Googlebot** per ogni file video; `contentUrl` corretto; verifica con la sezione miglioramenti video di Controllo URL.
- Risultati in un anno (video pubblicati +30%): **impressioni video circa 3x, clic circa 2x**.

## Vimeo (2023)
Fonte: https://developers.google.com/search/case-studies/vimeo-case-study?hl=it
- Per player incorporabili via iframe: `VideoObject` su ogni pagina del player di origine + **`<meta name="robots" content="noindex, indexifembedded" />`** sulla pagina indicata da `embedUrl`, così solo i video incorporati nelle pagine dei clienti diventano idonei all'indicizzazione (oltre 750 milioni di video).
- Momenti chiave: markup `Clip` per i capitoli, `SeekToAction` quando non ci sono capitoli; per embed iframe serve comunicare il tempo di inizio al player (es. wrapper `postMessage`); non serve per embed JavaScript.
- Implicazione: chi incorpora video Vimeo/YouTube beneficia di quanto fatto dalla piattaforma.

## Wix (2024)
Fonte: https://developers.google.com/search/case-studies/wix-case-study?hl=it
- Integrazione nella UI Wix di: API Site Verification + API Search Console (verifica automatica e invio Sitemap), API Controllo URL (strumento Ispezione del sito: stato e errori di indicizzazione aggregati), API Search Console Search Analytics (4 report: clic, impressioni, traffico, query principali).
- Risultati: oltre 2 milioni di siti collegati; **+15% traffico medio** in un anno per chi ha collegato Search Console (luglio 2022-luglio 2023); +15% GPV vs utenti simili; **+24% GPV mensile** per e-commerce; chi ha usato Ispezione del sito: **+5% traffico**, +16% GPV.
- Rilevante come modello: una skill può sfruttare API pubbliche (Search Console, URL Inspection, Site Verification) se l'utente fornisce credenziali/consenso.

## ZipRecruiter (2018)
Fonte: https://developers.google.com/search/case-studies/ziprecruiter-case-study?hl=it
- `JobPosting` (dal 2012, nuovi campi aggiunti e testati quando Google li consiglia). Risultati: conversioni da Google **3x** rispetto ad altri motori, tasso di conversione organico da Google **4,5x** rispetto a prima, rimbalzo **-10%**, traffico organico non-brand **+35%**; aggiornamento annunci quasi in tempo reale.

---

# Implicazioni per la skill SEO

> Sezione di ragionamento, ancorata a quanto letto nel gruppo C. Dove servono informazioni di altri gruppi (robots, canonical, JS SEO, dati strutturati specifici) è indicato.

## (a) Controlli verificabili automaticamente in un audit

**Title link**
- [ ] Ogni pagina/route ha un `<title>` non vuoto nell'HTML renderizzato.
- [ ] Nessun `<title>` duplicato tra pagine diverse (anche "micro-boilerplate" su sottoinsiemi di pagine).
- [ ] Nessun title vago: "Home", "Profilo", "Pagina", "Untitled", nome del framework (es. il nome del progetto Angular generato).
- [ ] Nessun title semivuoto (es. inizia con un delimitatore `| Nome`).
- [ ] Nessuna ripetizione di parole/frasi nel title (keyword stuffing, es. stessa parola 3+ volte).
- [ ] Brand nel title in modo conciso, all'inizio o alla fine con delimitatore (`-`, `:`, `|`).
- [ ] Lingua/sistema di scrittura del title coerente con `lang` e con il contenuto principale.
- [ ] Anni nel title coerenti con l'anno nell'H1/contenuto (title "obsoleti").
- [ ] Un solo titolo principale evidente: un primo `<h1>` visibile, distinto dalle altre intestazioni; segnalare pagine con 0 o più H1 dello stesso peso.
- [ ] Coerenza tra `<title>`, `<h1>` e `og:title` (Google li usa tutti come fonti).

**Snippet / meta description**
- [ ] Presenza di `<meta name="description">` almeno su home e pagine principali.
- [ ] Descrizioni univoche per pagina; segnalare duplicati.
- [ ] Descrizioni che non sono elenchi di parole chiave e non troppo brevi (es. 2-3 parole).
- [ ] Rilevare `nosnippet`, `max-snippet`, `data-nosnippet` e avvisare: escludono/limitano anche AI Overview/AI Mode e featured snippet.
- [ ] Contenuti chiave non nascosti in tab/accordion al caricamento (impatta i deep link "Leggi tutto").
- [ ] Nessuno script che rimuove il frammento `#...` dall'URL o forza lo scroll in cima al caricamento.

**Nome del sito**
- [ ] Home page con JSON-LD `WebSite` contenente `name` e `url` (URL canonico della home); `alternateName` consigliato.
- [ ] Un solo nodo `WebSite` in home (niente blocchi duplicati).
- [ ] `name` coerente con `og:site_name`, `<title>` della home e H1/intestazione della home.
- [ ] `name` non generico (es. "Sviluppatore web Milano", "Orientamento al lavoro").
- [ ] Stessi dati strutturati su tutti i duplicati della home (http/https, www/non-www) o, meglio, redirect verso la canonica.
- [ ] Il nome del sito non può essere impostato per una sottodirectory: segnalare tentativi del genere.

**Favicon**
- [ ] `<link rel="icon" ...>` (o `shortcut icon` / `apple-touch-icon`) nell'head della **home page**.
- [ ] File raggiungibile (HTTP 200), non bloccato da robots.txt per Googlebot-Image; home non bloccata per Googlebot.
- [ ] Quadrato 1:1, almeno 8x8 px, consigliato **> 48x48 px**; formato tra BMP, GIF, ICO, PNG, JPEG, PPM, TIFF (se c'è solo SVG, segnalare che SVG non compare tra i formati elencati per la favicon in Ricerca).
- [ ] Non è la favicon di default del framework (es. icona predefinita del boilerplate Angular/CLI): deve rappresentare il brand.
- [ ] URL della favicon stabile (senza hash di build che cambia a ogni deploy, se possibile).

**Immagini**
- [ ] Immagini di contenuto in `<img src>` (anche dentro `<picture>`), non come `background-image` CSS (non indicizzate).
- [ ] Ogni `<img>` di contenuto ha `alt` descrittivo; segnalare `alt` mancante, vuoto su immagini significative o con keyword stuffing.
- [ ] `<svg>` inline significativi con `<title>` (+ `aria-labelledby`).
- [ ] `srcset`/`<picture>` sempre con `src` di fallback.
- [ ] Formati supportati: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF; estensione coerente con il tipo MIME.
- [ ] Nomi file descrittivi (segnalare `IMG_1234.jpg`, `image1.jpg`, `1.jpg`, hash puri).
- [ ] Stessa immagine sempre allo stesso URL.
- [ ] `og:image` presente, non è il logo, senza molto testo, proporzioni non estreme, alta risoluzione; per Discover larghezza ≥ 1200 px, > 300.000 pixel totali, 16:9 consigliato.
- [ ] `<meta name="robots" content="max-image-preview:large">` presente (case study: +30%/+79% CTR in Discover).

**Video**
- [ ] Video incorporati tramite `<video>`, `<iframe>`, `<embed>`, `<object>` presenti nell'HTML renderizzato **senza interazione dell'utente** (attenzione ai "facade" che caricano l'iframe solo al clic).
- [ ] Nessun video caricato tramite frammento `#`.
- [ ] `VideoObject` con `name`, `description`, `thumbnailUrl` univoci, `uploadDate` (vedi gruppo dati strutturati), `contentUrl`/`embedUrl`.
- [ ] Miniatura ≥ 60x30 px, formato supportato, URL stabile, non bloccata; con trasparenza: ≥ 80% dei pixel con alfa > 250.
- [ ] Nessuna data `expires` nel passato per video ancora disponibili.

**Date**
- [ ] Articoli/post con data visibile etichettata ("Pubblicato", "Aggiornato") e `datePublished`/`dateModified` in JSON-LD coerenti con quella visibile.
- [ ] Nessuna data futura; fuso orario ISO 8601 corretto se presente.

**Esperienza sulla pagina / CWV**
- [ ] HTTPS ovunque (niente mixed content, redirect http→https).
- [ ] LCP < 2,5 s, INP < 200 ms, CLS < 0,1 (dati di campo CrUX se disponibili, altrimenti lab con Lighthouse/PageSpeed Insights, segnalando che il ranking usa dati reali).
- [ ] Viewport mobile corretto, layout responsive (Lighthouse).
- [ ] Nessun interstitial/overlay a tutta pagina al caricamento (newsletter, promo); banner piccoli al loro posto; il consenso non deve reindirizzare a una pagina separata.
- [ ] Contenuto principale chiaramente distinguibile; nessun eccesso di annunci.

**Sitelink / struttura**
- [ ] Navigazione interna con link `<a href>` verso le pagine importanti; anchor text concisi e pertinenti (segnalare "clicca qui", "scopri di più" ripetuti).
- [ ] Contenuti non ripetuti tra pagine.

**Funzionalità AI**
- [ ] Pagine importanti indicizzabili e idonee allo snippet (nessun `noindex`/`nosnippet` involontario; robots.txt e CDN/WAF che non bloccano Googlebot).
- [ ] Contenuti importanti presenti come testo nell'HTML (non solo in immagini, canvas, video o PDF).
- [ ] Dati strutturati coerenti con il testo visibile.
- [ ] Segnalare come non necessari (ma non dannosi) file "per l'AI" o markup speciali: Google dice esplicitamente che non servono.

**Indexing API**
- [ ] Se il sito/progetto usa l'Indexing API per pagine che non sono `JobPosting` né `BroadcastEvent` in `VideoObject`, segnalarlo come uso non previsto (rischio revoca, spam).

**Traduzione**
- [ ] Rilevare `notranslate` (meta robots/googlebot o `X-Robots-Tag`) e avvisare che disattiva i risultati tradotti.

## (b) Regole per chi costruisce un sito nuovo
1. Decidere subito un **nome del sito** univoco e non generico, usarlo identico in `WebSite.name`, `og:site_name`, title della home e intestazione della home; prevedere `alternateName` (acronimo, forma breve, e come riserva il dominio in minuscolo).
2. Il sito deve stare su **dominio o sottodominio proprio** (non in sottodirectory di un altro sito): nome del sito, favicon e fonti preferite funzionano solo a livello di host.
3. Favicon del brand, quadrata, almeno 48x48 (meglio multipli, es. 192x192 PNG + ICO), linkata nell'head della home, a URL stabile.
4. Template di pagina con: title unico e descrittivo (`Argomento pagina - Brand`), meta description unica, un solo H1 visibile coerente col title, `og:title`/`og:description`/`og:image` specifici per pagina, `max-image-preview:large`.
5. Immagini sempre con `<img>`/`<picture>` + `src` + `alt` + dimensioni esplicite (aiuta anche CLS), nomi file descrittivi, formati moderni (WebP/AVIF) con fallback.
6. Video in pagine dedicate se il video è il contenuto principale; incorporamento diretto (non dietro clic); `VideoObject`.
7. Blog/articoli: data visibile + `datePublished`/`dateModified`.
8. HTTPS dal primo giorno; budget prestazioni per rispettare le soglie CWV.
9. Niente popup a tutta pagina; per newsletter/consensi usare banner piccoli o dialog parziali.
10. Struttura di link interna chiara (menu, footer, link contestuali) con anchor descrittivi: è la base dei sitelink.
11. `Organization` (logo) e `BreadcrumbList` dove ha senso (rimando al gruppo dati strutturati).
12. Al lancio: verificare in Search Console, inviare Sitemap, controllare home con Controllo URL. Non serve nulla di speciale per AI Overview/AI Mode o Discover.
13. Non scegliere un dominio a "corrispondenza esatta" sperando nel ranking: Google limita il credito a questi domini.

## (c) Note specifiche per SPA JavaScript / Angular
- **Tutto ciò che Google usa per titoli, snippet, nome del sito e favicon deve essere nell'HTML renderizzato** che Googlebot vede (verificabile con Controllo URL). Con Angular è preferibile **SSR o prerendering** (Angular SSR / SSG) così title, meta, JSON-LD e contenuti sono già nella risposta HTML; in alternativa assicurarsi che i servizi `Title` e `Meta` aggiornino head per ogni route. (Dettagli su rendering JS nel gruppo crawling/JS.)
- **Title per route**: usare la proprietà `title` delle route o una `TitleStrategy` personalizzata per evitare che tutte le route mantengano il title di `index.html` (causa title duplicati/boilerplate che Google riscrive).
- **Meta description, `og:*`, canonical e robots per route**: aggiornarli a ogni navigazione; con SSR verificarli nell'HTML iniziale. `og:image` assoluto e specifico per pagina.
- **`WebSite` JSON-LD e favicon** possono stare staticamente in `index.html` (servono solo in home): è il modo più robusto in una SPA. Sostituire la `favicon.ico` generata dalla CLI con quella del brand; evitare che il nome file della favicon contenga hash che cambiano a ogni build.
- **HashLocationStrategy (`/#/route`) da evitare**: la documentazione video ricorda che la Ricerca in genere non supporta i frammenti URL; usare `PathLocationStrategy` con fallback server su `index.html` (o SSR).
- **Frammenti e scroll**: per i deep link "Leggi tutto" e per i featured snippet (scroll alla sezione), non rimuovere l'hash al caricamento e non forzare lo scroll in cima; con il Router abilitare `anchorScrolling` e valutare attentamente `scrollPositionRestoration` per non sovrascrivere la posizione al primo caricamento.
- **Contenuti in tab/accordion** (es. Angular Material tabs/expansion panel) chiusi al caricamento riducono la probabilità di deep link: tenere i contenuti importanti visibili; se servono tab, assicurarsi che il testo sia comunque nel DOM.
- **Immagini**: evitare hero e card con `background-image` CSS per immagini di contenuto; `NgOptimizedImage` genera `<img>` con `src`/`srcset` e aiuta LCP (priority) e CLS (width/height).
- **Video**: i pattern "lite embed/facade" che inseriscono l'iframe YouTube solo al clic violano "non fare affidamento su azioni dell'utente per caricare il video"; se si vuole il video indicizzato sulla propria pagina, incorporarlo direttamente o fornire comunque `VideoObject` + Sitemap video e verificare nel report Indicizzazione video.
- **Dati strutturati generati via JS** sono ammessi (rimando alla guida dedicata), ma vanno verificati con Controllo URL / Test risultati avanzati; per il nome del sito usare validator.schema.org (il Test risultati avanzati non lo supporta).
- **CWV in una SPA**: bundle JS pesanti peggiorano LCP e INP; caricamenti tardivi di componenti/font/immagini senza dimensioni peggiorano CLS. Usare lazy loading delle route, defer dei componenti non critici, SSR + hydration.
- **Interstitial**: dialog di consenso/newsletter implementati come overlay a schermo intero o come redirect a route dedicata (`/consent`) sono da evitare.
- **Routing e status**: pagine rimosse in una SPA devono restituire un vero 404/410 (SSR) o `noindex`, anche per il caso Indexing API/rimozioni video (rimando a gruppo crawling per soft 404).

## (d) Note specifiche per personal brand e professionista locale

**Portfolio sviluppatore (personal brand, target recruiter)**
- Nome del sito = nome e cognome (o brand personale) in `WebSite.name`, con `alternateName` (es. iniziali, nome + ruolo, dominio in minuscolo come ultima riserva). Un nome generico tipo "Full Stack Developer" non verrebbe scelto.
- Title delle pagine: evitare "Home", "Profilo", "Progetti" da soli (Google cita proprio "Home" e "Profilo" come esempi negativi); es. "Nome Cognome - Sviluppatore Angular | Portfolio", "Progetto X: dashboard in Angular - Nome Cognome".
- Una pagina per progetto (case study) con testo descrittivo, immagini `<img>` con alt, eventuale video demo incorporato direttamente: più pagine distinte = più possibilità di sitelink e di rispondere a query diverse.
- Discover può **non consigliare repository di codice**: le pagine progetto sul proprio sito, con immagini grandi e testo, sono più adatte rispetto al solo link a GitHub.
- Search Console per verificare il dominio; eventuale rivendicazione della **scheda informativa** e del **profilo della Ricerca** (`profile.google.com/@handle`) che aggrega sito e social; badge del profilo sul sito con touch target ≥ 44x44 px.
- Se si scrive un blog tecnico: data visibile + `datePublished`/`dateModified`; meta description con autore/data; testi originali (sistemi di contenuti originali).
- La diversità dei siti limita in genere a due risultati per sito nei risultati principali: la presenza su più piattaforme (sito + profili esterni) è il modo naturale per occupare più spazio per la query col proprio nome (deduzione, non affermazione di Google).

**Orientatrice di carriera (locale + online)**
- **Profilo dell'attività su Google** rivendicato e aggiornato (indirizzo o area servita, contatti, categoria, foto): è citato anche tra le best practice per le funzionalità AI ("profilo dell'attività aggiornato").
- Meta description della home sul modello dell'esempio Google: cosa offre + orari + dove si trova (es. "Orientamento professionale a Milano e online. Colloqui individuali, bilancio di competenze... Su appuntamento lun-ven 9-18.").
- Nome del sito: brand o nome della professionista, non "Orientamento al lavoro Milano" (generico).
- `Organization` con logo (o dati strutturati locali/persona del gruppo dati strutturati) + `BreadcrumbList`.
- Recensioni: il sistema delle recensioni (attivo anche in italiano) valuta contenuti di recensione scritti dal sito (articoli, guide, confronti), **non** le recensioni dei clienti; i contenuti di tipo "recensione/confronto" (es. di corsi, piattaforme di ricerca lavoro) devono essere approfonditi e basati su esperienza reale.
- Elenco dei luoghi più apprezzati: solo per attività **con sede fisica** e dipende da menzioni in elenchi curati non sponsorizzati su siti terzi.
- Unità di fornitori (SEE): per query su "attività locali" quando compare l'unità di aggregatori; non servono dati oltre alla scansione del sito.
- Newsletter/lead magnet: banner, non interstitial a tutta pagina.
- Articoli del blog (consigli di carriera, CV, colloqui): titoli non clickbait (Discover), immagini grandi 1200 px+, data visibile, contenuti utili e originali; questi temi sono adatti a featured snippet e "Le persone hanno chiesto anche": strutturare con domande come intestazioni e risposte testuali chiare (il featured snippet non si può forzare).
- Le funzionalità "Siti di offerte di lavoro" (SEE) e i risultati estesi Jobs riguardano aggregatori/pagine foglia di offerte reali: non applicabili a un sito di orientamento salvo pubblichi vere offerte di lavoro.

## (e) Ottimizzazione per le funzionalità AI di Google (AI Overview, AI Mode)
- Nessun requisito o markup aggiuntivo: **non creare** file "per l'AI", file di testo speciali o schema.org "AI". Condizione necessaria: pagina **indicizzata e idonea a mostrare uno snippet**.
- Controlli di esclusione: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` limitano anche la presenza nelle funzionalità AI; Google-Extended non riguarda la Ricerca.
- Fattori utili citati: scansione consentita (robots.txt **e** CDN/hosting), link interni, buona esperienza sulla pagina, **contenuti importanti in forma testuale**, immagini/video di qualità a supporto, dati strutturati coerenti con il testo, profilo dell'attività e Merchant Center aggiornati.
- Il **fan-out delle query** cerca pagine di supporto su sottoargomenti: coprire in modo chiaro le sotto-domande del proprio tema (es. per l'orientatrice: costi, durata, differenze tra servizi, modalità online) aumenta le occasioni di essere link di supporto (ragionamento).
- Il **ranking dei passaggi** valuta singole sezioni: intestazioni descrittive e paragrafi autosufficienti aiutano.
- Misurazione: il traffico AI è dentro il report Rendimento, tipo "Web"; non è separabile. Integrare con Analytics per conversioni/tempo.
- Fonti preferite: badge "preferita" anche in AI Mode/AI Overview, ma richiede l'inclusione nelle funzionalità di AI generativa in Search Console e il sito a livello di dominio/sottodominio; rilevanza maggiore per publisher di notizie.

## (f) Cose che una skill NON può fare (azioni manuali/off-site)
- Verificare la proprietà in Search Console (la skill può preparare meta tag/file di verifica o record DNS, ma la conferma la fa l'utente); aggiungere utenti/account di servizio.
- Richiedere l'indicizzazione/ri-scansione con lo strumento Controllo URL; leggere i report (Rendimento, CWV, HTTPS, Indicizzazione video, Discover) senza accesso API concesso dall'utente.
- Rivendicare e aggiornare il Profilo dell'attività su Google, la scheda informativa (Knowledge Panel), il profilo della Ricerca.
- Ottenere menzioni in elenchi "luoghi più apprezzati", recensioni, link da altri siti.
- Compilare i moduli di interesse (aggregatori, fornitori, ecosistemi, offerte di lavoro SEE, fonti preferite) o il modulo di feedback favicon.
- Garantire comparsa di favicon, nome del sito, sitelink, featured snippet, date, AI Overview: sono tutti automatici e non garantiti.
- Misurare i CWV di campo (CrUX) senza traffico reale sufficiente; la skill può solo misurare in laboratorio.
- Monitorare i rollout dei core/spam update (dashboard di stato) e attendere i tempi di ri-elaborazione (giorni-settimane per title/favicon/nome del sito; mesi dopo un core update).
- Usare l'Indexing API per un portfolio o un sito professionale: non è consentito (solo `JobPosting` e `BroadcastEvent`).
- Valutare in modo oggettivo la qualità/utilità dei contenuti come farebbe un revisore umano non affiliato (la skill può applicare le domande di autovalutazione, ma Google suggerisce anche giudizi di persone esterne).
- Nota sui case study: alcuni strumenti citati (Strumento di test per i dati strutturati, Test di ottimizzazione mobile, report "Copertura") compaiono in case study del 2018-2020; nelle pagine più recenti del gruppo gli strumenti di riferimento sono Test dei risultati avanzati, validator.schema.org, Controllo URL, report Indicizzazione delle pagine, Lighthouse e PageSpeed Insights.
