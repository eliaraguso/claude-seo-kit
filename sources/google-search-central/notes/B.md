# Gruppo B — Scansione e indicizzazione + documentazione crawler Google

Appunti fedeli alla documentazione ufficiale Google Search Central / Google Crawling (versione italiana, scaricata 2026-10). Le sezioni per pagina riportano solo quanto scritto nelle fonti; le valutazioni sono nella parte finale "Implicazioni per la skill SEO".

---

## Informazioni sulla scansione del web di Google
Fonte: https://developers.google.com/crawling/docs/about-crawling?hl=it

- La scansione è il processo con cui software automatizzati scoprono e comprendono le pagine; senza scansione una pagina non può comparire nei risultati.
- Googlebot è il crawler principale (Ricerca); esistono crawler specifici per altre piattaforme (Immagini, Shopping). Usano user agent identificabili e indirizzi IP noti (verificabili).
- Frequenza di nuova scansione variabile: da pochi minuti (home page di siti di notizie) a circa un mese per pagine che non cambiano. Le Sitemap informano Google di pagine nuove/aggiornate e influiscono sulla frequenza.
- Scansione frequente = buon segno (contenuti aggiornati/pertinenti).
- I crawler eseguono rendering (caricano la pagina come un utente reale). Dati citati: pagina mobile mediana passata da 816 KB a 2,3 MB, più di 60 file; per un'istantanea completa la stessa pagina può essere scansionata più volte.
- Ottimizzazione automatica: se il sito rallenta o restituisce errori, la frequenza di scansione cala automaticamente; uso della cache; sezioni infinite (es. calendari fino all'anno 9999) scansionate meno. Il proprietario può indicare ciò che non va scansionato (robots.txt).
- I crawler non accedono a contenuti dietro login/paywall senza autorizzazione; per i contenuti in abbonamento esistono indicazioni (flexible sampling) e dati strutturati per mostrare la schermata di accesso agli utenti senza violare le norme anti-spam; controlli di anteprima (snippet) per nasconderli nelle anteprime.
- Controllo del proprietario: robots.txt, meta tag robots, Sitemap, gestione budget di scansione.
- Google-Extended (token in robots.txt) controlla, tra l'altro, se i contenuti contribuiscono all'addestramento di future versioni dei modelli Gemini; NON influisce sull'inclusione nella Ricerca né è un segnale di ranking.
- Strumento: Google Search Console (gratuito) — volume di scansione e motivi, diagnosi di downtime/velocità, visibilità nella Ricerca.

## Log delle modifiche (documentazione scansione)
Fonte: https://developers.google.com/crawling/docs/changelog?hl=it

- Feed RSS degli aggiornamenti: `https://developers.google.com/crawling/docs/changelog/crawling_docs_updates.rss`.
- Set 2026: documentazione `Mediapartners-Google` generalizzata: incide su più prodotti pubblicitari (AdSense, Ad Manager), non solo AdSense.
- Lug 2026: guida budget di scansione chiarita; user agent NotebookLM rinominato `Google-GeminiNotebook` (il vecchio valore resta supportato per transizione; aggiornare stringhe hardcoded); corretta la stringa UA di `Google-InspectionTool` (conteneva erroneamente un punto e virgola).
- Mag 2026: aggiunta documentazione Web Bot Auth (fase sperimentale).
- Mar 2026: aggiunto user agent `Google-Agent` (agenti Google che navigano ed eseguono azioni su richiesta dell'utente) e relativi intervalli IP; nuova pagina panoramica sulla scansione.
- Feb 2026: intervalli IP spostati nella directory `/crawling/ipranges` (la vecchia `/search/apis/ipranges` funziona ancora per ora, aggiornare i link); limiti dimensione file spostati dalla pagina Googlebot alla panoramica crawler (valgono per tutti i crawler/fetcher).
- Gen 2026: aggiunto fetcher Google Messaggi (anteprime link nelle chat).
- Dic 2025 / Nov 2025: migrazione di documentazione (faceted navigation, crawl budget, codici HTTP, errori DNS, panoramica crawler, verifica richieste, riduzione frequenza, crawler comuni, specifica robots.txt) da Search Central al sito developers.google.com/crawling: contenuti invariati, perché l'infrastruttura è condivisa tra Ricerca, Shopping, News, Gemini, AdSense ecc. Read Aloud: rendering stateless, deve accedere alla pagina per vedere i meta tag.
- Nov 2025: aggiunti fetcher `Google-Pinpoint`, `Google-CWS`; Ott 2025: `Google-NotebookLM`; Lug 2025: UA Read Aloud aggiornato a browser più recenti.
- Apr 2025: chiarita descrizione Google-Extended; corretto `Googlebot-News`: le sue preferenze di scansione NON influiscono sulla scheda Notizie di Google.

## Ottimizza il budget di scansione
Fonte: https://developers.google.com/crawling/docs/crawl-budget?hl=it

- Non necessaria se il sito non ha moltissime pagine che cambiano spesso o se le pagine vengono scansionate il giorno stesso della pubblicazione: basta tenere aggiornata la Sitemap e controllare il report Indicizzazione delle pagine.
- Destinatari (stime, non soglie): siti > 1.000.000 pagine univoche con cambi ~settimanali; siti > 10.000 pagine con cambi giornalieri; siti con molti URL in "Rilevata, ma attualmente non indicizzata".
- "Sito" = nome host univoco: `www.example.com` e `code.example.com` hanno budget separati.
- Budget = limite di capacità di scansione (connessioni simultanee + ritardo tra recuperi, alias "carico host") + domanda di scansione. Ogni sito parte da un limite predefinito conservativo che cresce se il sito regge.
- Il limite sale con risposte stabili/veloci (latenza, TTFB); scende con rallentamenti, errori `5xx`, `429`.
- Domanda per Googlebot: dimensioni sito, frequenza aggiornamento, qualità, pertinenza. Fattori controllabili: inventario percepito (duplicati/URL inutili sprecano tempo — il fattore più controllabile), popolarità, mancato aggiornamento. Gli spostamenti di sito aumentano la domanda.
- Il limite di capacità è condiviso tra tutti i crawler Google: domanda alta di uno riduce la capacità per gli altri.
- Non tutte le pagine scansionate vengono indicizzate.
- Best practice:
  - Gestire l'inventario URL; accorpare duplicati.
  - Bloccare con robots.txt URL non importanti (scroll infinito che duplica, versioni ordinate diversamente). NON usare `noindex` per risparmiare budget (Google richiede comunque la pagina). NON usare robots.txt per "riallocare temporaneamente" budget: il budget liberato non viene trasferito ad altre pagine salvo che il sito sia già al limite di capacità.
  - Pagine rimosse definitivamente: `404` o `410`. Gli URL bloccati da robots restano in coda di scansione.
  - Eliminare i soft 404 (continuano a consumare budget).
  - Sitemap aggiornate, con `<lastmod>` se i contenuti si aggiornano.
  - Evitare lunghe catene di redirect.
  - Pagine efficienti/veloci; supportare `304 Not Modified` (cache HTTP).
- Aumentare il budget: aggiungere risorse server (se Controllo URL mostra "Carico host superato"); migliorare qualità (per la Ricerca: popolarità, valore per l'utente, unicità, capacità di servire).

## User agent APIs-Google
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/apis-user-agent?hl=it

- User agent usato dalle API Google per consegnare notifiche push (POST HTTPS), con retry a backoff esponenziale per alcuni giorni al massimo. Richiede verifica della proprietà del dominio da parte dello sviluppatore.
- Richiede certificato SSL valido (non validi: autofirmati, firmati da fonte non attendibile, revocati). Rispondere entro pochi secondi.
- Blocco: annullare la registrazione oppure robots.txt con user agent `APIs-Google` (non segue le regole per Googlebot); ritardo nel recepire le modifiche.
- Verifica: DNS inverso su googlebot.com o google.com.
- Poco pertinente per siti vetrina.

## Feedfetcher
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/feedfetcher?hl=it

- Recupera feed RSS/Atom per Google News e WebSub su richiesta degli utenti. Solo i feed dei podcast vengono indicizzati nella Ricerca.
- Ignora robots.txt (agisce per conto dell'utente). Per bloccarlo: rispondere `404`, `410` o altro errore allo user agent `Feedfetcher-Google`.
- Frequenza: in media non più di una volta all'ora per la maggior parte dei siti.
- Non scopre link: elabora solo l'URL fornito. IP in `user-triggered-fetchers-google.json`.
- Poco pertinente per siti vetrina.

## Elenco dei crawler comuni di Google
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers?hl=it

- I crawler comuni rispettano SEMPRE robots.txt nelle scansioni automatiche. IP in `common-crawlers.json`; DNS inverso `crawl-***-***-***-***.googlebot.com` o `geo-crawl-***-***-***-***.geo.googlebot.com`. Lo user agent può essere falsificato (spoofing) → verificare.
- Se un crawler ha più token, basta che una regola corrisponda a uno dei token.
- Token robots.txt → prodotti interessati:
  - `Googlebot` (Smartphone e Desktop, stringa con `Chrome/W.X.Y.Z`): Ricerca Google (incluso Feed personalizzato/Discover e tutte le funzionalità), Immagini, Video, News.
  - `Googlebot-Image` (anche `Googlebot`): Google Immagini, Feed personalizzato, Video e funzionalità di Ricerca che mostrano immagini, loghi e favicon.
  - `Googlebot-Video` (anche `Googlebot`): funzionalità video.
  - `Googlebot-News` (nessuna stringa UA dedicata, usa quelle di Googlebot): Google News (news.google.com e app).
  - `Storebot-Google`: tutte le piattaforme Google Shopping.
  - `Google-InspectionTool` (anche `Googlebot`): solo strumenti di test (Test dei risultati avanzati, Controllo URL di Search Console); nessun effetto sulla Ricerca.
  - `GoogleOther`, `GoogleOther-Image`, `GoogleOther-Video`: crawler generici (ricerca interna/sviluppo), nessun prodotto specifico.
  - `Google-CloudVertexBot` (anche `Googlebot`): scansioni richieste dai proprietari per Vertex AI Agents; nessun effetto sulla Ricerca.
  - `Google-Extended`: nessuna stringa UA propria; token di controllo per l'uso dei contenuti nell'addestramento delle future generazioni di Gemini (app Gemini, API Vertex AI per Gemini) e per la "fondatezza" (grounding) nelle app Gemini e in Grounding con Ricerca Google su Vertex AI. Non influisce sull'inclusione nella Ricerca né sul ranking.
- `Chrome/W.X.Y.Z` è un segnaposto per la versione Chrome (evergreen, segue l'ultima release Chromium). Nei filtri di log usare caratteri jolly per la versione.

## Elenco dei crawler per casi speciali di Google
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers?hl=it

- Usati quando esiste un accordo tra sito e prodotto; possono ignorare robots.txt. IP in `special-crawlers.json`; DNS inverso `rate-limited-proxy-***-***-***-***.google.com`.
- `APIs-Google`, `AdsBot-Google-Mobile`, `AdsBot-Google`, `Mediapartners-Google`: ignorano lo user agent globale `*` → per bloccarli vanno nominati esplicitamente.
- AdsBot: controllo qualità degli annunci nelle pagine web per Google Ads. Mediapartners-Google: annunci pertinenti per AdSense, Ad Manager e altri prodotti pubblicitari.
- `Google-Safety`: ignora robots.txt (rilevamento abusi/malware).
- Ritirati (solo storico): AdsBot Mobile Web iPhone, Duplex web (`DuplexWeb-Google`), Google Favicon (token `Googlebot-Image`/`Googlebot`), `AdsBot-Google-Mobile-Apps`, Web Light (`googleweblight`, controllava l'intestazione `no-transform`).

## Elenco dei fetcher attivati dall'utente di Google
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers?hl=it

- Avviati da un'azione dell'utente → in genere ignorano robots.txt. IP in `user-triggered-fetchers.json`, `user-triggered-fetchers-google.json`, `user-triggered-agents.json`; DNS inverso `***.gae.googleusercontent.com` o `google-proxy-***.google.com`.
- Elenco: Chrome Web Store (`Google-CWS`); Feedfetcher (`FeedFetcher-Google`); Gemini Notebook (`Google-GeminiNotebook`; vecchio `Google-NotebookLM` supportato fino ad agosto 2026); `Google-Agent` (agenti Google che navigano/eseguono azioni per l'utente; IP `user-triggered-agents.json`; sperimenta Web Bot Auth con identità `https://agent.bot.goog`); Google Messaggi (`GoogleMessages`, anteprime link in chat); `Google-Pinpoint`; Google Publisher Center (`GoogleProducer`); Google Read Aloud (`Google-Read-Aloud`; vecchio `google-speakr` deprecato); Google Site Verifier (`Google-Site-Verification/1.0`, recupera i token di verifica di Search Console).

## Panoramica dei crawler e dei fetcher di Google (user agent)
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers?hl=it

- Tre categorie: crawler comuni (rispettano sempre robots.txt), crawler per casi speciali, fetcher attivati dall'utente.
- Crawler distribuiti su migliaia di macchine e data center → IP diversi nei log. Scansione principalmente da IP USA; se il sito blocca gli USA, Google potrebbe provare da IP di altri paesi.
- Protocolli: HTTP/1.1 (predefinito) e HTTP/2. HTTP/2 fa risparmiare risorse ma NON dà vantaggi di ranking. Per disattivare la scansione HTTP/2: rispondere `421`. Supportati anche FTP (RFC959) e FTPS (RFC4217), raramente usati.
- Compressioni supportate: gzip, deflate, Brotli (br), annunciate in `Accept-Encoding`.
- Limite dimensione file: per impostazione predefinita vengono scansionati solo i primi 15 MB di un file; il resto è ignorato. I singoli progetti possono avere limiti diversi (es. Googlebot potrebbe avere un limite inferiore, ad es. 2 MB, o un limite maggiore per i PDF rispetto all'HTML).
- Codici HTTP inappropriati possono influire sulla presenza nei prodotti Google.
- Cache HTTP (RFC 9111): supportati `ETag`/`If-None-Match` e `Last-Modified`/`If-Modified-Since`. Consigliato impostare entrambi; se presenti entrambi Google usa `ETag` (consigliato: niente problemi di formato data). Formato data `Last-Modified` consigliato: "Fri, 4 Sep 1998 19:15:56 GMT". Consigliato anche `Cache-Control: max-age=<secondi>` (es. `max-age=94043`). Altre direttive di cache non supportate. Googlebot usa la cache nelle riscansioni per la Ricerca; Storebot solo in certe condizioni.
- Identificazione: header `user-agent`, IP di origine, hostname DNS inverso.

## User agent di Google Read Aloud
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/read-aloud-user-agent?hl=it

- `Google-Read-Aloud`: sintesi vocale (TTS) su richiesta dell'utente; usato da Google Go, Google Read it, Read Aloud nell'app Google e altri servizi.
- Non è un crawler, non segue i link; rendering stateless senza cookie dell'utente; usa cache ma possono esserci più richieste.
- Non bloccabile con robots.txt. Disattivazione: `<meta name="google" content="nopagereadaloud">` (può accedere proattivamente alla pagina per leggere i meta tag, poi riduce le richieste).
- Contenuti con paywall: dati strutturati per contenuti in abbonamento con `isAccessibleForFree` = `False`.
- `google-speakr` = vecchio nome deprecato.

## Riduci la frequenza di scansione di Google
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate?hl=it

- Cause comuni di picchi: navigazione per facet/filtri/ordinamenti, calendari con molti URL per date, target dell'annuncio dinamico della rete di ricerca. Esaminare i log del server e contattare l'hosting.
- Emergenza (poche ore o 1-2 giorni): rispondere `500`, `503` o `429` invece di `200`. La riduzione vale per l'intero hostname, sia per gli URL in errore sia per quelli con contenuti; la frequenza risale automaticamente quando gli errori calano.
- Avvisi: effetti generalizzati (meno pagine nuove scoperte, aggiornamenti più lenti, pagine rimosse restano più a lungo nell'indice, campagne Ads sospese/annunci non pubblicati). NON farlo per più di 1-2 giorni: se lo stesso URL restituisce questi codici per più giorni può essere eliminato dall'indice.
- Se non si possono servire errori: richiesta speciale (modulo Googlebot report) indicando la frequenza ottimale. Non si può chiedere un AUMENTO della frequenza; valutazione in diversi giorni.

## Verifica le richieste dei crawler e dei fetcher di Google
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests?hl=it

- Categorie → DNS inverso → file IP: comuni (`googlebot.com`, `common-crawlers.json`); speciali (`rate-limited-proxy-*.google.com`, `special-crawlers.json`, possono rispettare o meno robots.txt); fetcher utente (`gae.googleusercontent.com` / `google-proxy-*.google.com`; `user-triggered-fetchers.json`, `user-triggered-fetchers-google.json`, `user-triggered-agents.json`; ignorano robots.txt).
- Metodo manuale (sufficiente nella maggior parte dei casi): 1) `host <IP>` (DNS inverso); 2) il dominio deve essere `googlebot.com`, `google.com` o `googleusercontent.com`; 3) `host <nome>` (DNS diretto); 4) l'IP deve coincidere con quello nei log.
- Metodo automatico (larga scala): confronto IP con gli elenchi JSON (formato CIDR). Altri IP Google (es. Apps Script): `https://www.gstatic.com/ipranges/goog.json`.

## Autentica le richieste con Web Bot Auth (sperimentale)
Fonte: https://developers.google.com/crawling/docs/crawlers-fetchers/web-bot-auth?hl=it

- Google sperimenta l'Internet Draft IETF Web Bot Auth (firma crittografica delle richieste dei bot) con alcuni agenti AI. Non tutte le richieste né tutti gli user agent sono firmati → continuare a usare IP/DNS inverso/user agent.
- Un sottoinsieme delle richieste di `Google-Agent` è firmato con identità `https://agent.bot.goog`; header `Signature-Agent: g="https://agent.bot.goog"`.
- Verifica autonoma: chiavi pubbliche da `https://agent.bot.goog/.well-known/http-message-signatures-directory` (cache secondo `Cache-Control`, eliminare le chiavi non più presenti); verificare `Signature` rispetto a `Signature-Input` (etichetta `g`) secondo RFC 9421. La finestra di scadenza della firma è distinta dal `Cache-Control` del set di chiavi. Per richieste sensibili alla latenza si può rispondere subito e validare entro la finestra di scadenza.
- Molti CDN/WAF/servizi di bot detection supportano già il protocollo.
- Poco pertinente per siti vetrina (gestione lato infrastruttura).

## Gestire la scansione degli URL di navigazione per facet
Fonte: https://developers.google.com/crawling/docs/faceted-navigation?hl=it

- Facet basate su parametri URL generano URL quasi infiniti → scansione eccessiva e scoperta più lenta dei nuovi URL utili.
- Se non servono in Ricerca: bloccarle con robots.txt (es. `disallow: /*?*products=`, `allow: /*?products=all$`), lasciando scansionabili solo le pagine dei singoli articoli e una pagina elenco senza filtri; oppure usare frammenti URL (`#...`), che la Ricerca in genere non supporta in scansione/indicizzazione (nessun impatto).
- Metodi meno efficaci a lungo termine: `rel="canonical"` verso la versione non filtrata; `rel="nofollow"` sui link alle pagine filtrate (ogni link a quell'URL deve averlo).
- Se devono essere indicizzabili: usare `&` come separatore (non `,` `;` `[` `]`); se i filtri sono nel path, ordine logico sempre uguale e nessun filtro duplicato; combinazioni senza risultati, filtri duplicati/insensati e paginazione inesistente → `404` sull'URL stesso (non redirect a una pagina 404 comune). Nelle SPA potrebbe non essere possibile: seguire le best practice SPA.

## Miti e fatti sulla scansione
Fonte: https://developers.google.com/crawling/docs/myths-about-crawling?hl=it

Quiz vero/falso. Esiti:
- FALSO: comprimere le Sitemap aumenta il budget di scansione (vanno comunque recuperate dal server).
- FALSO: conviene fare continue piccole modifiche per sembrare aggiornati. I contenuti sono classificati per qualità, non per data; modifiche banali e date aggiornate artificiosamente valgono poco.
- FALSO: Google preferisce contenuti vecchi. Una pagina utile resta utile a prescindere dall'età.
- FALSO: Google preferisce URL puliti senza parametri ("possiamo eseguire la scansione dei parametri").
- VERO: caricamento/rendering più veloci → più capacità di scansione. Il tempo di rendering conta quanto quello di richiesta. Però Google può dedicare più tempo a un sito lento ma con informazioni importanti; è più importante la velocità per gli utenti; più facile aiutare Google a scansionare i contenuti giusti che tutti.
- FALSO: i siti piccoli sono scansionati meno spesso. Contenuti importanti e che cambiano spesso vengono scansionati spesso a prescindere dalle dimensioni.
- PARZIALMENTE VERO: contenuti vicini alla home sono più importanti. Le pagine linkate direttamente dalla home possono essere scansionate più spesso, ma questo non significa ranking più alto.
- PARZIALMENTE VERO: URL con versione per forzare riscansione. Può funzionare ma spesso non è necessario e spreca risorse; cambiare URL solo per modifiche sostanziali.
- VERO: velocità ed errori incidono sul budget. Molti `5xx` o timeout rallentano la scansione; controllare il report Statistiche di scansione in Search Console.
- FALSO: la scansione è un fattore di ranking. È necessaria per comparire, non è un indicatore di ranking.
- VERO: URL alternativi (AMP, hreflang) e contenuti incorporati (CSS, JS, recuperi XHR) consumano budget.
- FALSO: `crawl-delay` controlla i crawler Google (regola non standard, non elaborata).
- PARZIALMENTE VERO: `nofollow` incide sul budget: un URL nofollow può essere comunque scansionato se linkato altrove senza nofollow.
- PARZIALMENTE VERO: `noindex` per controllare il budget: la pagina va scansionata per vedere il noindex; però nel lungo periodo rimuovere URL dall'indice può liberare budget indirettamente. Usare noindex per non indicizzare senza preoccuparsi del budget.
- FALSO: le pagine `4xx` sprecano budget (eccetto `429`).

## Come scrivere e inviare un file robots.txt
Fonte: https://developers.google.com/crawling/docs/robots-txt/create-robots-txt?hl=it

- Su hosting gestiti (Wix, Blogger) spesso non si modifica direttamente: usare le impostazioni di visibilità del provider.
- Posizione: radice dell'host (`https://www.example.com/robots.txt`); NON in sottodirectory. Un solo robots.txt per sito. Valido anche su sottodominio o porta non standard. Si applica solo a protocollo+host+porta in cui è pubblicato (`https://example.com/robots.txt` non vale per `m.example.com` né per `http://example.com`).
- Se non si può accedere alla radice: usare meta tag (`noindex`).
- Formato: file di testo UTF-8 (incluso ASCII); caratteri non UTF-8 possono invalidare le regole. Usare editor di testo semplici, non programmi di videoscrittura (virgolette curve ecc.).
- Senza regole contrarie, la scansione è implicitamente autorizzata.
- Gruppi: ogni gruppo inizia con `User-agent`; un crawler segue un solo gruppo (il più specifico); gruppi multipli per lo stesso UA vengono uniti. Regole sensibili alle maiuscole (`/file.asp` ≠ `/FILE.asp`). `#` = commento.
- Regole supportate: `user-agent` (obbligatoria, una o più per gruppo; `*` vale per tutti tranne AdsBot, che va nominato), `disallow` / `allow` (almeno una per gruppo; devono iniziare con `/`; directory terminano con `/`; per pagina usare il percorso completo), `sitemap` (facoltativa, zero o più; URL completo; Google non deduce varianti http/https/www). Carattere jolly `*` supportato in tutte tranne `sitemap`. Righe non riconosciute ignorate.
- Test: aprire `https://example.com/robots.txt` in navigazione privata; report robots.txt di Search Console (solo per file già online); libreria open source di Google `github.com/google/robotstxt` per test locale.
- Invio: non serve fare nulla, Google lo trova automaticamente. Per aggiornare la cache in fretta vedere la pagina "Aggiorna il file robots.txt".

## In che modo Google interpreta la specifica del file robots.txt
Fonte: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec?hl=it

- Google segue il REP (RFC 9309). Non si applica ai fetcher controllati dagli utenti (es. iscrizioni ai feed) né ai crawler di sicurezza (malware).
- Posizione: directory di primo livello, protocolli supportati HTTP, HTTPS, FTP (per la Ricerca). URL del file sensibile alle maiuscole. Recupero con `GET` non condizionale (FTP: `RETR` anonimo).
- Validità: solo stesso host, protocollo e porta. Esempi: `https://example.com/robots.txt` non vale per `other.example.com`, `http://example.com`, `:8181`; `https://www.example.com/robots.txt` non vale per `example.com` né per `shop.www.example.com`; `/folder/robots.txt` non è valido; IDN = punycode; robots su IP vale solo per quell'IP come host; porte standard (80, 443, 21) equivalgono all'host predefinito.
- Codici HTTP del robots.txt:
  - `2xx`: elaborato.
  - `3xx`: Google segue almeno 5 hop (RFC 1945), poi lo tratta come `404`. Non segue redirect "logici" (frame, JavaScript, meta refresh).
  - `4xx` (tranne `429`): come se non esistesse robots.txt → nessuna restrizione. NON usare `401`/`403` per limitare la frequenza di scansione.
  - `5xx`: prime 12 ore scansione del sito interrotta (riprova il robots); poi per 30 giorni usa l'ultima versione valida in cache (se assente: nessuna restrizione); `503` genera tentativi frequenti; dopo 30 giorni: se il sito è disponibile si comporta come se non ci fosse robots.txt, se il sito ha problemi di disponibilità interrompe la scansione.
  - Errori rete/DNS (timeout, risposte non valide, connessioni interrotte, errori di chunking) = errore del server.
- Cache: in genere fino a 24 ore, di più se non aggiornabile (timeout, `5xx`); condivisa tra crawler; può variare in base a `Cache-Control max-age`.
- Formato: testo UTF-8, righe separate da CR, CR/LF o LF. Righe non valide ignorate, incluso il BOM iniziale; se scarica HTML prova a estrarre regole. Limite dimensione: 500 KiB; il contenuto oltre è ignorato (ridurre raggruppando, es. directory separate per il materiale escluso).
- Sintassi: `<field>:<value><#commento>`; nomi campo case-insensitive; spazi facoltativi. Campi supportati: `user-agent`, `allow`, `disallow`, `sitemap`. NON supportati: `crawl-delay` e altri. Regole senza path ignorate. Il path deve iniziare con `/` ed è case-sensitive. Valore `user-agent` case-insensitive.
- `disallow`: Google non indicizza il contenuto delle pagine bloccate, ma può indicizzare l'URL e mostrarlo senza snippet.
- `sitemap`: supportato da Google, Bing e altri; URL assoluto con protocollo e host, non URL-encoded; può stare su un host diverso; numero illimitato; non legato a uno user agent.
- Raggruppamento: più righe `user-agent` consecutive condividono le regole. Le righe diverse da allow/disallow/user-agent (es. `sitemap`) non interrompono il gruppo: `user-agent: a` / `sitemap: ...` / `user-agent: b` / `disallow: /` → a e b entrambi bloccati.
- Precedenza user agent: vale un solo gruppo, quello con UA più specifico; l'ordine nel file è irrilevante; testo non corrispondente ignorato (`googlebot/1.2` e `googlebot*` = `googlebot`). Gruppi specifici dello stesso UA vengono uniti; gruppi specifici e `*` NON vengono combinati. Es.: Storebot-Google senza gruppo dedicato segue `*`.
- Matching path: confronto su forma con codifica percentuale (UTF-8 grezzo e `%E3%83%84` equivalenti). Caratteri jolly: `*` (0 o più caratteri) e `$` (fine URL). `/` e `/*` = tutto; `/$` = solo radice; `/fish` corrisponde a `/fish.html`, `/fishheads`, `/fish.php?id=` ma non a `/Fish.asp`, `/catfish`, `/?id=fish`; `/fish/` solo la cartella; `/*.php$` solo URL che terminano in .php (non con parametri).
- Precedenza regole: vince la più specifica (path più lungo); in caso di conflitto a parità, vince la meno restrittiva (`allow`). Es.: `allow: /folder` vs `disallow: /folder` → allow; `allow: /page` vs `disallow: /*.htm` su `/page.htm` → disallow (più lunga); `allow: /$` + `disallow: /` → solo la home consentita.

## Aggiorna il file robots.txt
Fonte: https://developers.google.com/crawling/docs/robots-txt/submit-updated-robots-txt?hl=it

- Procedura: scaricare il file (browser, `curl https://example.com/robots.txt -o robots.txt`, o report robots.txt di Search Console), modificarlo (sintassi corretta, UTF-8), ricaricarlo nella root.
- Se il sito è in una sottocartella (es. `subdomain.example.com/site/example/`) probabilmente non si può modificare il robots della root: contattare il proprietario del dominio.
- Google aggiorna la cache del robots.txt ogni 24 ore; per accelerare: "Richiedi una nuova scansione" nel report robots.txt di Search Console.

## Regole utili per i file robots.txt
Fonte: https://developers.google.com/crawling/docs/robots-txt/useful-robots-txt-rules?hl=it

- Bloccare tutto: `User-agent: *` / `Disallow: /` (gli URL possono essere comunque indicizzati senza scansione; non vale per AdsBot).
- Consentire tutto: `Disallow:` vuoto = nessun robots.txt = `Allow: /`.
- Bloccare directory: `Disallow: /calendar/`. ATTENZIONE: non usare robots.txt per contenuti privati (usare autenticazione): gli URL bloccati possono essere indicizzati e il file è pubblico (rivela percorsi).
- Bloccare singola pagina: `Disallow: /useless_file.html`.
- Tutto tranne una sottodirectory: `Disallow: /` + `Allow: /public/`.
- Consentire un solo crawler / tutti tranne uno: gruppi dedicati.
- Bloccare tutto tranne `Storebot-Google` (prodotti su Shopping ma non in Ricerca).
- Bloccare tutte le immagini: `User-agent: Googlebot-Image` / `Disallow: /` (Google non indicizza immagini e video senza scansionarli). Immagine singola: `Disallow: /images/dogs.jpg`.
- Tipo di file: `Disallow: /*.gif$`; `$` = fine URL, quindi `cats.xls?personality=loki` NON è bloccato da `/*.xls$`.
- Più user agent in un gruppo: righe `User-agent` consecutive.

## Esegui il debug degli errori di rete e DNS per i crawler di Google
Fonte: https://developers.google.com/crawling/docs/troubleshooting/dns-network-errors?hl=it

- Timeout di rete, reset della connessione ed errori DNS sono trattati come errori `5xx`: la scansione rallenta subito; per la Ricerca gli URL già indicizzati non raggiungibili vengono rimossi dall'indice entro pochi giorni. Search Console può generare messaggi.
- Errori di rete: controllare firewall e log (regole troppo generiche, IP Google bloccati); analizzare traffico con tcpdump/Wireshark; contattare l'hosting. Cause: interfacce sovraccariche (pacchetti persi → timeout), porte chiuse (pacchetti `RST`).
- Errori DNS: firewall che blocca le query DNS di Google (consentire `UDP` e `TCP`); verificare record `A` e `CNAME` (`dig +nocmd example.com a +noall +answer`); verificare che tutti i name server (`dig ... ns`) puntino agli IP corretti; modifiche DNS delle ultime 72 ore possono non essere propagate (si può fare flush della cache di Google Public DNS); server DNS personalizzati devono funzionare e non essere sovraccarichi.
- Se si usa hosting/CDN, rivolgersi a loro.

## In che modo i codici di stato HTTP influenzano i crawler di Google
Fonte: https://developers.google.com/crawling/docs/troubleshooting/http-status-codes?hl=it

- Search Console segnala errori per `4xx`-`5xx` e redirect `3xx` non riusciti. Un `2xx` NON garantisce l'indicizzazione. Funzionalità sperimentali dei protocolli non supportate.
- `2xx`: contenuti valutati; se sembrano un errore (pagina vuota, messaggio di errore) → `soft 404` in Search Console.
  - `200`: passa alla pipeline di indicizzazione (non garantita). `201`/`202`: attesa limitata, poi elabora ciò che ha (timeout dipende dallo UA). `204`: nessun contenuto, non elaborabile.
- `3xx`: per impostazione predefinita fino a 10 hop (Googlebot di solito 10; `Google-InspectionTool` non segue i redirect). Contenuto dell'URL che reindirizza ignorato; si elabora la destinazione finale.
  - `301`/`308`: indicatore FORTE che la destinazione va elaborata (canonica). `302`/`303`/`307`: indicatore DEBOLE. `304`: contenuto invariato dall'ultima scansione; nessun effetto sull'indicizzazione (possibile ricalcolo segnali).
  - Usare comunque il codice semanticamente corretto per altri client (e-reader, altri motori).
- `4xx` (400, 401, 403, 404, 410, 411…): contenuto ignorato; URL non indicizzati e quelli già indicizzati rimossi; nuovi 404 non elaborati; frequenza di scansione di quegli URL diminuisce gradualmente. Tutti trattati allo stesso modo (tranne `429`). NON usare `401`/`403` per limitare la scansione.
- `429`: trattato come server sovraccarico = errore del server.
- `5xx` e `429`: rallentamento temporaneo della scansione, proporzionale al numero di URL in errore; URL indicizzati conservati ma eliminati se l'errore persiste; contenuti ignorati. Con il ritorno a `2xx` la frequenza risale gradualmente. (`500`, `502`, `503`.)

## Panoramica degli argomenti relativi a scansione e indicizzazione
Fonte: https://developers.google.com/search/docs/crawling-indexing?hl=it

- Pagina indice: elenca tipi di file indicizzabili, struttura URL, Sitemap, gestione crawler (recrawl, facet, budget, codici HTTP/errori), robots.txt, canonicalizzazione, siti mobile, AMP, JavaScript, metadati (HTML valido, meta tag, robots meta/data-nosnippet/X-Robots-Tag, noindex, link scansionabili, attributi rel), rimozioni, modifiche e spostamenti di siti (redirect, site move, test A/B, pausa sito).

## Reindirizzamenti e la Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/301-redirects?hl=it

- Usi: cambio dominio; più URL per la stessa pagina (es. `https://example.com/home`, `http://home.example.com`, `https://www.example.com` → scegliere un canonico e reindirizzare gli altri); unione di siti; pagina rimossa con sostituto. Piattaforme (Blogger, Shopify) possono avere redirect integrati.
- Permanenti → nei risultati compare la destinazione; temporanei → compare la pagina di origine.
- Tipi in ordine di probabilità di corretta interpretazione:
  - Permanenti (indicatore che la destinazione è canonica; usarli solo se il redirect non verrà annullato): `301`, `308` (lato server); `meta refresh` a 0 secondi e HTTP `Refresh: 0`; JavaScript `location` (solo se non si può lato server o meta refresh); "crypto redirect" (link testuale "ci siamo trasferiti"), da non usare salvo mancanza di alternative.
  - Temporanei (destinazione non usata come indicatore di canonicità, ma può comunque essere indicizzata se altri segnali lo indicano): `302`, `303`, `307`; `meta refresh` / HTTP refresh con più di 0 secondi.
- Raccomandato: per cambiare l'URL mostrato nei risultati, redirect lato server permanente quando possibile. Temporaneo utile ad es. per servizio momentaneamente non disponibile (l'URL originale resta nei risultati).
- Esempi: PHP `header('HTTP/1.1 301 Moved Permanently'); header('Location: ...'); exit();` (header prima di qualunque output); Apache `mod_alias` (`Redirect permanent "/old" "https://example.com/new"`, `Redirect temp`), `mod_rewrite` (`[R=301]`, `[R]`); NGINX `return 301 ...` / `return 302 ...`, `rewrite ... permanent|redirect`.
- `meta refresh` va nel `<head>` (es. `<meta http-equiv="refresh" content="0; url=...">`) o come header HTTP `Refresh`. Istantaneo = permanente, ritardato (es. 5 s) = temporaneo.
- Redirect JavaScript: `window.location.href = "..."` in uno script nell'head. Google esegue JS con il Web Rendering Service dopo la scansione; il rendering può fallire → Google potrebbe non vedere mai il redirect.
- Versioni alternative: Google tiene traccia di origine e destinazione; una diventa canonica, l'altra un "nome alternativo" che può comparire nei risultati se la query suggerisce che il vecchio URL è più riconoscibile (normale dopo un cambio dominio; scompare da sé).

## Informazioni su AMP nella Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/amp?hl=it

- Le pagine AMP sono indicizzate come le altre e soggette agli stessi standard. Possono comparire come risultati avanzati (con dati strutturati, nessuna garanzia) e come Storie web.
- Linee guida: seguire la specifica HTML AMP; stessi contenuti e azioni della pagina canonica ove possibile; schema URL significativo e coerente col dominio (es. `amp.example.com/giraffes` o `example.com/amp/giraffes`, non `test.com/giraffes`); pagina AMP valida; rispettare le norme sui dati strutturati.
- AMP non è solo mobile: usare responsive design. Su desktop appaiono identiche; consigliate pagine AMP autonome se il formato basta; su desktop però le AMP non hanno le funzionalità specifiche nei risultati della Ricerca.

## Migliora i contenuti AMP nella Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/amp/enhance-amp?hl=it

- Pagina AMP di base: collegarla a una pagina canonica (obbligatorio per scansione e indicizzazione; la canonica può essere la stessa AMP); stessi contenuti/azioni; validare con Test delle pagine AMP; stesso markup di dati strutturati su canonica e AMP; robots.txt non deve bloccare l'AMP; usare robots meta/data-nosnippet/X-Robots-Tag dove opportuno; seguire hreflang.
- CMS: plugin (WordPress, Drupal, Joomla) o personalizzazione; schemi URL consigliati `https://www.example.com/myarticle/amp` o `https://www.example.com/myarticle.amp.html`; modello di dati strutturati per tipo di contenuto.
- Risultati avanzati (es. carosello Notizie principali, carosello host): implementare dati strutturati, verificare con Test dei risultati avanzati e Test AMP.
- Monitoraggio: report Stato AMP e report sullo stato dei risultati avanzati in Search Console. Codelab e risorse (AdSense, Tag Manager, Analytics per AMP).

## Rimuovere le pagine AMP dalla Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/amp/remove-amp?hl=it

- Configurazioni: AMP canonica (unica versione) o non-AMP canonica + AMP abbinata.
- Rimuovere tutto rapidamente: eliminare entrambe le versioni dal server/CMS, strumento "Rimuovi contenuti obsoleti", verificare con ricerca o report Stato AMP (grafico "pagine AMP indicizzate" in calo). Durante il ritardo di rilevamento Google può mostrare un errore all'utente.
- Rimuovere solo l'AMP: NON svuotare il file (documento vuoto = non valido, Google continua a servire l'ultima versione valida). Togliere `rel="amphtml"` dalla canonica; rispondere `301` o `302` sull'URL AMP e reindirizzare alla canonica; per renderla inaccessibile anche altrove `404`; per mantenere i permalink `301` verso la canonica.
- CMS: annullare la pubblicazione/eliminare la pagina rimuove entrambe le versioni; disattivare AMP nel CMS rimuove tutte le AMP (guide WordPress.com, Drupal, Squarespace).

## Convalida i contenuti AMP
Fonte: https://developers.google.com/search/docs/crawling-indexing/amp/validate-amp?hl=it

- Strumenti: Test delle pagine AMP, Test dei risultati avanzati, report Stato AMP.
- Se l'AMP non compare: renderla rilevabile tramite link; `rel="amphtml"` sulla canonica (e su altre versioni non AMP, es. mobile); `rel="canonical"` sulla pagina AMP; robots.txt deve consentire canonica, AMP e link nei dati strutturati; rimuovere meta robots / `X-Robots-Tag` che bloccano; dati strutturati conformi. L'indicizzazione può richiedere tempo.
- Altri motivi: alcune funzionalità non disponibili nel paese; sito non ancora indicizzato.

## Chiedere a Google una nuova scansione di URL
Fonte: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl?hl=it

- Su CMS ospitati (Blogger, WordPress) spesso l'invio è automatico.
- Si possono chiedere solo URL che si gestiscono. La scansione può richiedere da alcuni giorni ad alcune settimane; monitorare con report Stato dell'indicizzazione / Controllo URL. La richiesta non garantisce l'inclusione né l'inclusione immediata; priorità ai contenuti utili e di alta qualità.
- Pochi URL: Controllo URL di Search Console (serve accesso completo alla proprietà); esiste una quota; richiedere più volte lo stesso URL non accelera.
- Molti URL: inviare una Sitemap (utile per siti appena lanciati o dopo spostamento; può includere metadati su lingue, video, immagini, notizie).

## Bloccare l'indicizzazione della Ricerca con noindex
Fonte: https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=it

- `noindex` (meta tag o header HTTP) fa eliminare completamente la pagina dai risultati, anche se altri siti la linkano.
- IMPORTANTE: la pagina NON deve essere bloccata da robots.txt e deve essere accessibile, altrimenti il crawler non vede il `noindex` e l'URL può comparire comunque (es. se linkato).
- Utile senza accesso root (controllo pagina per pagina).
- Meta: `<meta name="robots" content="noindex">` nel `<head>` (tutti i motori che lo supportano); `<meta name="googlebot" content="noindex">` solo Google. Combinabile: `content="noindex, nofollow"`. Altri motori potrebbero interpretarlo diversamente.
- Header: `X-Robots-Tag: noindex` (o `none`), anche per PDF, video, immagini.
- `noindex` in robots.txt NON è supportato.
- CMS (Wix, WordPress, Blogger): usare le impostazioni del CMS per i meta tag.
- Debug: la pagina deve essere riscansionata dopo l'aggiunta (può richiedere mesi per pagine poco importanti); Controllo URL per richiedere riscansione e verificare l'HTML ricevuto da Googlebot; report Indicizzazione delle pagine per vedere le pagine con noindex estratto; per rimozioni rapide vedere la documentazione sulle rimozioni; verificare che robots.txt non blocchi l'URL.

## Risolvi i problemi di canonicalizzazione
Fonte: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting?hl=it

- Google può scegliere un canonico diverso da quello dichiarato (qualità, contenuti, indicatori tecnici).
- Passi: 1) Controllo URL per vedere il canonico scelto da Google (se il canonico è in una proprietà Search Console non propria, non si vede il traffico del duplicato); 2) cercare problemi tecnici; 3) rendere le pagine raggruppate sufficientemente diverse: la rivalutazione può tenerle nel cluster fino a 2 settimane; differenze chiare e significative separano più rapidamente; 4) "Richiesta di indicizzazione" in Controllo URL (soggetta a quote, riservarla agli URL più importanti).
- Problemi comuni:
  - Varianti linguistiche/regionali senza `hreflang` (es. siti EN per USA, UK, Australia con stessi contenuti).
  - Elementi canonici errati generati da CMS/plugin (`rel="canonical"` o redirect `3xx` sbagliati) → verificare HTML con DevTools, segnalare al provider.
  - Server mal configurati: contenuti di `example.com` serviti su `other.example`; server diversi con pagine soft 404 identiche.
  - Compromissione (hacking): redirect `3xx` o `rel="canonical"` cross-domain verso spam.
  - Syndication: il canonical è sconsigliato; meglio che i partner blocchino l'indicizzazione.
  - Sito emulatore (copia non autorizzata): contattare l'host o richiesta DMCA.

## Che cos'è la canonicalizzazione
Fonte: https://developers.google.com/search/docs/crawling-indexing/canonicalization?hl=it

- Canonicalizzazione (deduplicazione) = scelta dell'URL più rappresentativo tra duplicati; solo quello viene mostrato.
- Cause di duplicati: varianti regionali (hreflang, stessa lingua), varianti dispositivo (mobile/desktop), protocollo (HTTP/HTTPS), funzioni di ordinamento/filtro, varianti accidentali (sito demo accessibile ai crawler).
- Un po' di duplicazione è normale e NON viola le norme anti-spam; ma peggiora UX e tracciamento del rendimento.
- Processo: Google individua il contenuto principale, raggruppa pagine uguali/molto simili, sceglie la più completa e utile come canonica. La canonica è scansionata più spesso dei duplicati.
- Fattori: HTTP vs HTTPS, redirect, presenza in Sitemap, `rel="canonical"`. La preferenza dichiarata è un suggerimento, non una regola.
- Versioni linguistiche sono duplicati solo se il contenuto principale è nella stessa lingua (solo header/footer tradotti = duplicato). Varianti regionali nella stessa lingua: usare sia canonicalizzazione sia `hreflang`.
- La canonica è la fonte principale per valutare contenuti e qualità; i risultati puntano di solito alla canonica, salvo duplicati più adatti (es. pagina mobile per utenti mobile).

## Come specificare un URL canonico con rel="canonical" e altri metodi
Fonte: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls?hl=it

- Metodi in ordine di forza: redirect (forte), `rel="canonical"` (forte), inclusione in Sitemap (debole). Combinarli aumenta l'efficacia. Nessuno è obbligatorio: senza indicazione Google sceglie da sé.
- CMS (WordPress, Wix, Blogger): usare le impostazioni SEO del CMS.
- Motivi: scegliere l'URL mostrato (es. pulito vs `?gclid=ABCD`); consolidare gli indicatori (link) su un URL; semplificare le metriche; non sprecare scansione su duplicati.
- Best practice:
  - NON usare robots.txt per la canonicalizzazione (gli URL bloccati possono essere indicizzati senza contenuto).
  - NON usare lo strumento Rimozioni URL per la canonicalizzazione (nasconde tutte le versioni).
  - NON indicare canonici diversi per la stessa pagina con tecniche diverse (es. Sitemap vs `rel="canonical"`).
  - NON usare frammenti URL (`#`) come canonici.
  - Includere un canonical autoreferenziale nella pagina canonica.
  - Sconsigliato `noindex` per evitare la scelta di una canonica all'interno di un sito (blocca la pagina del tutto): preferire `rel="canonical"`.
  - Con `hreflang`: canonica nella stessa lingua (o miglior sostituto).
  - Link interni sempre verso l'URL canonico.
  - Rendering lato client JS: specificare il canonico nell'HTML sorgente e fare in modo che JavaScript NON lo modifichi; se non si può nel sorgente, ometterlo e impostarlo solo via JS.
- Confronto metodi: elemento `<link rel="canonical">` (infinite pagine; complesso su siti grandi; solo HTML); header HTTP `Link: <...>; rel="canonical"` (non aumenta il peso pagina; utile per PDF/docx; supportato solo per risultati web); Sitemap (facile su siti grandi ma segnale più debole; Google deve comunque individuare i duplicati); redirect permanenti (solo quando si dismette un duplicato); varianti AMP (seguire linee guida AMP).
- `rel="canonical"` (RFC 6596): ignorato se usato per indicare alternative, in particolare con attributi `hreflang`, `lang`, `media`, `type` (usare `rel="alternate"`). Usare un solo metodo tra elemento HTML e header (entrambi supportati ma rischio incoerenze).
- Elemento: nel `<head>`, URL ASSOLUTI (relativi supportati ma sconsigliati: es. `https://www.example.com/dresses/green/green-dress.html`, non `/dresses/...`). Accettato solo nel `<head>` → l'head deve essere HTML valido. Con versione mobile separata: `<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.example.com/...">` sulla canonica. Se aggiunto con JS, seguire le linee guida JS.
- Header HTTP (RFC5988): es. per `.docx` → `Link: <https://www.example.com/downloads/white-paper.pdf>; rel="canonical"`; URL assoluti.
- Sitemap: tutte le pagine elencate sono suggerite come canoniche; Google decide quali sono duplicati.
- Redirect: per eliminare duplicati esistenti; tutti i redirect permanenti hanno lo stesso effetto, ma quelli HTTP lato server agiscono più rapidamente. Es. `https://example.com/home`, `https://home.example.com`, `https://www.example.com` → sceglierne uno e reindirizzare.
- Altri indicatori: Google preferisce HTTPS a HTTP salvo: certificato non valido, dipendenze non protette (diverse dalle immagini), HTTPS che reindirizza a/tramite HTTP, HTTPS con canonical verso HTTP. Rafforzare: redirect HTTP→HTTPS, canonical HTTP→HTTPS, HSTS. Evitare: certificati non validi e redirect HTTPS→HTTP (HSTS non compensa), URL HTTP in Sitemap o hreflang, certificato per la variante host sbagliata (deve corrispondere all'host o essere wildcard).
- Google preferisce come canonici gli URL che fanno parte di cluster `hreflang` reciproci.

## Controllare i contenuti che condividi con Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/control-what-you-share?hl=it

- Motivi per nascondere contenuti: limitare dati (visibili solo agli utenti già sul sito; attenzione ai metadati dei file); nascondere contenuti di bassa qualità/spam (es. UGC), che possono penalizzare il ranking del sito; concentrare Google sui contenuti importanti (siti molto grandi, > centinaia di migliaia di URL, o con molti duplicati).
- Metodi: rimuovere i contenuti dal sito (il modo migliore, tutti i tipi); protezione con password (contenuti riservati; li rimuove anche se già indicizzati); `noindex` (tutti i tipi; la pagina resta raggiungibile da link ma non nei risultati); robots.txt (efficace per immagini e video: Google indicizza solo media scansionabili); disattivazione di specifiche proprietà Google (Shopping, Hotel e case vacanze) per pagine web.
- Contenuti già presenti: richiesta di rimozione (vedi pagina rimozioni).

## Googlebot
Fonte: https://developers.google.com/search/docs/crawling-indexing/googlebot?hl=it

- Due tipi: Googlebot Smartphone e Googlebot Desktop; stesso token robots.txt (`Googlebot`) → non si possono targetizzare separatamente via robots.txt. Sottotipo identificabile dallo user agent.
- Indicizzazione principalmente mobile: la maggior parte delle richieste usa il crawler mobile.
- Frequenza: in media non più di una volta ogni pochi secondi per la maggior parte dei siti (brevi picchi possibili).
- Limiti dimensione per la Ricerca: primi 2 MB di un tipo di file supportato e primi 64 MB di un PDF. Ogni risorsa referenziata nell'HTML (CSS, JS) è recuperata separatamente con lo stesso limite (eccetto i PDF). Oltre il limite Googlebot interrompe e indicizza solo la parte scaricata. Il limite si applica ai dati NON compressi. Googlebot Video/Image possono avere limiti diversi.
- Fuso orario di Googlebot per scansioni da IP USA: Pacifico.
- Scoperta URL principalmente dai link; è quasi impossibile tenere segreto un sito (gli URL possono finire nei log referrer di altri siti).
- Scansione ≠ indicizzazione: per non scansionare → robots.txt; per non indicizzare → `noindex`; per bloccare utenti e crawler → password. Bloccare Googlebot incide su Ricerca (incl. Discover), Immagini, Video, News.
- Verificare Googlebot (spoofing frequente) con DNS inverso o intervalli IP prima di bloccarlo.

## Tipi di file indicizzabili da Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/indexable-file-types?hl=it

- Il tipo di file è determinato dall'header `Content-Type`; se mancante/errato Google può usare l'estensione o un altro parser.
- Flat file: CSV, KML/KMZ, GPX, HTML, SVG, TeX/LaTeX, testo (incl. codice sorgente .bas, .c/.cpp/.h, .cs, .java, .pl, .py), WML, XML.
- Codificati: PDF, PostScript, EPUB, Hanword (.hwp), Excel, PowerPoint, Word, OpenOffice (.odp, .ods, .odt), RTF.
- Immagini: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF. Video: 3GP, 3G2, ASF, AVI, DivX, M2V, M3U, M3U8, M4V, MKV, MOV, MP4, MPEG, OGV, QVT, RAM, RM, VOB, WebM, WMV, XAP.
- Operatore di ricerca `filetype:` (es. `filetype:rtf galway`).

## Il rendering dinamico come soluzione alternativa
Fonte: https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering?hl=it

- DEPRECATO come approccio: il rendering dinamico era una soluzione alternativa, NON consigliata a lungo termine (complessità e risorse). Consigliati invece: rendering lato server (SSR), rendering statico, hydration.
- La Ricerca Google vede i contenuti generati da JS, con alcune limitazioni; altri motori potrebbero ignorare JavaScript.
- Funzionamento: il server rileva i crawler (es. user agent) e serve una versione pre-renderizzata statica; gli utenti ricevono la versione client-side.
- Non è cloaking se i contenuti sono simili; le pagine di errore generate non sono cloaking. Mostrare contenuti completamente diversi a utenti e crawler (gatti vs cani) È cloaking.

## Risolvere i problemi con JavaScript relativi alla Ricerca
Fonte: https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript?hl=it

- Googlebot e il Web Rendering Service (WRS) possono non recuperare risorse non essenziali (es. richieste di beacon/errore). Le analytics lato client non rappresentano fedelmente l'attività di Googlebot: usare il report Statistiche di scansione di Search Console.
- Checklist:
  - Testare con Test dei risultati avanzati o Controllo URL (risorse caricate, console JS, eccezioni, DOM renderizzato). Facoltativo: raccogliere gli errori JS con un handler `window.addEventListener('error', ...)` (non cattura errori di parsing) e inviarli a un endpoint di logging.
  - Evitare soft 404 nelle SPA (difficile): redirect JS verso un URL con `404` dal server (es. `/not-found`) e/o aggiungere `<meta name="robots" content="noindex">` via JS. Le SPA che gestiscono errori lato client spesso restituiscono `200` → pagine di errore indicizzate.
  - Googlebot rifiuta le richieste di autorizzazione (es. Camera API): offrire accesso ai contenuti senza obbligare a consentire permessi.
  - NON usare frammenti URL (`#/products`) per caricare contenuti diversi: lo schema di scansione AJAX è deprecato dal 2015; usare l'API History.
  - Non fare affidamento sulla persistenza dei dati: WRS cancella localStorage, sessionStorage e cookie HTTP tra un caricamento e l'altro (segue redirect server e client come un browser).
  - Fingerprinting dei contenuti nei nomi file (es. `main.2bb85551.js`): Googlebot fa cache aggressiva e WRS può ignorare gli header di cache → rischio di JS/CSS obsoleti.
  - Feature detection per API critiche con fallback/polyfill (es. Googlebot non supporta WebGL → saltare l'effetto o pre-renderizzare lato server).
  - Contenuti recuperabili via HTTP: Googlebot non supporta WebSockets né WebRTC → fornire fallback HTTP.
  - Web component: WRS appiattisce light DOM e shadow DOM; usare `<slot>` per proiettare il light DOM; verificare l'HTML renderizzato.
  - Paywall JS che include tutto il contenuto nella risposta e lo nasconde via JS non è affidabile: fornire il contenuto completo solo dopo verifica dell'abbonamento.
  - Ritestare con Test dei risultati avanzati / Controllo URL; in caso di problemi, community di Search Central.

## Guida di base sulla SEO per JavaScript
Fonte: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics?hl=it

- Google esegue JS con Chromium evergreen. Tre fasi: scansione → rendering → indicizzazione; code separate per scansione e rendering.
- Se robots.txt blocca un URL, Googlebot salta la richiesta; Google non esegue il rendering di JS da file bloccati o su pagine bloccate.
- Googlebot estrae gli URL dagli attributo `href` dei link HTML; link inseriti via JS sono ammessi se rispettano le best practice dei link scansionabili. Per impedire il rilevamento: `nofollow`.
- Modello "app shell": l'HTML iniziale non contiene i contenuti → serve il rendering JS.
- Tutte le pagine con `200` vanno in coda di rendering (con o senza JS), salvo meta robots/header che indichino di non indicizzare. Attesa da secondi a più a lungo. Chromium headless esegue il rendering; i link dell'HTML renderizzato sono aggiunti alla coda; l'HTML renderizzato è usato per l'indicizzazione. Con status diverso da `200` (es. `404`) il rendering può essere saltato.
- SSR o pre-rendering restano un'ottima soluzione: più veloci per utenti e crawler e non tutti i bot eseguono JS.
- Titoli e meta description univoci e descrittivi: si possono impostare/modificare via JS.
- Canonical: meglio nell'HTML; se via JS, stesso valore dell'HTML originale; non usare JS per cambiarlo in un URL diverso; se non si può nell'HTML, ometterlo e impostarlo solo via JS. Deve esserci UN SOLO `rel="canonical"` (implementazioni errate ne creano più d'uno o modificano quello esistente → risultati imprevisti). Esempio inserimento JS con `document.createElement('link')` e URL assoluto.
- Codice compatibile: seguire la guida troubleshooting; pubblicazione differenziale e polyfill (non tutto è polyfillabile).
- Codici HTTP significativi: `404` per non trovato, `401` per pagine dietro login; redirect per pagine spostate.
- Soft 404 nelle SPA con routing client: redirect JS a URL con `404` dal server (es. `/not-found`) oppure meta `noindex` via JS (esempi di codice con `fetch`).
- API History invece dei frammenti: Google rileva solo link `<a href>`; esempio sbagliato `<a href="#/products">` + `hashchange`; esempio corretto `<a href="/products">` + `event.preventDefault()` + `history.pushState`.
- Meta robots: `<meta name="robots" content="noindex, nofollow">`. Si può aggiungere/modificare via JS (es. aggiungere noindex se l'API restituisce errore). ATTENZIONE: se Google trova `noindex` può saltare rendering ed esecuzione JS → rimuovere/modificare via JS un `noindex` presente nell'HTML originale potrebbe non funzionare. Se si vuole indicizzare la pagina, non mettere `noindex` nel codice originale.
- Cache di lunga durata: fingerprinting dei nomi file (es. `main.2bb85551.js`).
- Dati strutturati: JSON-LD generabile e inseribile via JS; testare.
- Web component: supportati; shadow DOM e light DOM uniti; Google vede solo ciò che è nell'HTML renderizzato; usare `<slot>`; verificare con Test dei risultati avanzati / Controllo URL.
- Immagini e contenuti a caricamento lento: seguire le linee guida lazy-loading.

## Correggere i contenuti a caricamento lento
Fonte: https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading?hl=it

- Il lazy loading mal implementato può nascondere contenuti a Google. Caricare i contenuti quando entrano nell'area visibile (viewport) con: lazy loading nativo del browser (immagini, iframe), API IntersectionObserver (+ polyfill), librerie JS che caricano all'ingresso nel viewport. NON basarsi su azioni dell'utente (scroll, clic): la Ricerca Google non interagisce con la pagina.
- NON applicare lazy loading ai contenuti visibili subito all'apertura (rallenta la visualizzazione).
- Scorrimento continuo (infinite scroll) indicizzabile: ogni blocco con URL univoco e permanente; contenuto stabile per URL (numeri di pagina assoluti, es. `?page=12`; evitare relativi come `?date=yesterday`); link sequenziali ai singoli URL (impaginazione); aggiornare l'URL con l'API History quando un nuovo blocco diventa principale.
- Test: Controllo URL; cercare i contenuti nell'HTML renderizzato; se gli URL di immagini/video compaiono nell'attributo `src` di `<img>`/`<video>`, funziona.

## Escludere le informazioni oscurate dalla Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/keep-redacted-information-out?hl=it

- Documenti e immagini possono contenere informazioni non visibili (testo coperto, cronologia modifiche, immagini non ritagliate, metadati con nomi degli autori) che restano anche dopo esportazione/conversione; screen reader e OCR le rendono rilevabili. Testo minuscolo, coperto da immagini o dello stesso colore dello sfondo NON è oscurato per i motori.
- Immagini: ritagliare/oscurare PRIMA di incorporarle (alcuni editor conservano l'originale non ritagliato); rimuovere completamente il testo (OCR); rimuovere metadati; esportare in formati raster semplici (PNG, WebP).
- Testo: rimuoverlo prima di generare il file pubblico; usare formati che non conservano la cronologia; strumenti di redazione dedicati (non rettangoli neri sopra il testo); controllare i metadati; attenzione a URL e nomi file (gli URL bloccati da robots.txt possono comunque essere indicizzati): usare hash nei parametri invece di email o nomi; usare autenticazione per i contenuti riservati con pagina di login `noindex`; verificare il sito in Search Console per poter rimuovere rapidamente.
- Se indicizzati per errore: rimuovere il documento; strumento Rimozioni per il sito verificato (prefisso URL per molti documenti; di solito meno di un giorno); pubblicare la versione corretta a un URL DIVERSO e aggiornare i link; chiedere ad altri siti di rimuoverli (o strumento Rimuovi contenuti obsoleti); le richieste di rimozione scadono dopo l'aggiornamento dell'indice o dopo circa 6 mesi.

## Best practice di Google per i link
Fonte: https://developers.google.com/search/docs/crawling-indexing/links-crawlable?hl=it

- I link servono a Google per pertinenza e scoperta di nuove pagine.
- Link scansionabili: elemento `<a>` con attributo `href` (assoluto, relativo `/...` o `./...`; ammessi anche con `onclick` o classi). Link inseriti via JS sono scansionabili se usano questo markup.
- Sconsigliati (Google potrebbe comunque tentare): `<a routerLink="products/category">`, `<span href="...">`, `<a onclick="goto(...)">`. L'`href` deve risolversi in un URL reale: sconsigliati `href="javascript:goTo('products')"` e `href="javascript:window.location.href='/products'"`.
- Anchor text: testo visibile dentro `<a>`; non vuoto. Fallback: attributo `title` se `<a>` vuoto; per link-immagine Google usa l'`alt` dell'`<img>` (alt descrittivo, non vuoto). Se l'anchor è inserito via JS verificare l'HTML renderizzato con Controllo URL.
- Anchor efficace: descrittivo, conciso, pertinente. Evitare generici ("Fai clic qui", "Scopri di più", "sito web", "articolo") e troppo lunghi. Test: deve avere senso letto da solo. Niente keyword stuffing (viola le norme anti-spam). Fornire contesto attorno al link; non concatenare link adiacenti.
- Link interni: ogni pagina importante dovrebbe avere un link da almeno un'altra pagina del sito. Nessun numero ideale di link per pagina ("se ti sembrano troppi, probabilmente lo sono").
- Link esterni: non averne paura; citare fonti aumenta l'affidabilità. `nofollow` solo per fonti non attendibili, non per tutti i link esterni. Link pagati → `sponsored` o `nofollow`; link inseriti dagli utenti (forum, Q&A) → `ugc` o `nofollow`.

## Best practice per l'indicizzazione di siti mobile e mobile-first
Fonte: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing?hl=it

- Google usa la versione mobile (scansionata con l'agente smartphone) per indicizzazione e ranking (mobile-first indexing). Versione mobile non obbligatoria ma vivamente consigliata.
- Configurazioni: responsive design (stesso HTML e URL; CONSIGLIATO da Google, più semplice); pubblicazione dinamica (stesso URL, HTML diverso via sniffing user agent + `Vary: user-agent`); URL distinti (m-dot, con `user-agent` e `Vary`). La guida riguarda soprattutto dinamica e URL distinti; nel responsive contenuti e metadati coincidono. CMS (Wix, Blogger): eventualmente cambiare tema.
- Accesso: stessi meta robots su mobile e desktop (un `noindex`/`nofollow` sul mobile blocca indicizzazione); niente lazy loading dei contenuti principali che dipende da interazione (scroll, clic, digitazione: Google non li esegue); non bloccare con `disallow` le risorse mobile.
- Contenuti uguali su mobile e desktop (anche differenze di DOM/layout possono cambiare l'interpretazione). Contenuti spostabili in accordion o schede; meno contenuti su mobile = attesa perdita di traffico. Stesse intestazioni chiare.
- Dati strutturati: stessi su entrambe le versioni (priorità: `Breadcrumb`, `Product`, `VideoObject`); URL mobile nei dati strutturati mobile; Evidenziatore di dati addestrato sul mobile.
- Stessi `title` e meta description.
- Annunci: rispettare i Better Ads Standards (es. annunci in alto che occupano troppo spazio su mobile).
- Immagini: alta qualità (non troppo piccole o a bassa risoluzione); formati e tag supportati (es. SVG supportato, ma un .jpg dentro `<image>` in un SVG incorporato NON è indicizzabile); URL immagini stabili (non che cambiano a ogni caricamento); stesso alt, titoli, didascalie, nomi file. URL immagine diversi tra desktop e mobile → possibile perdita temporanea di traffico immagini.
- Video: URL stabili; formati supportati e tag `<video>`, `<embed>`, `<object>`; stessi dati strutturati; video facile da trovare su mobile (se serve scorrere troppo il ranking può risentirne).
- URL distinti (m-dot): stesso stato di errore su entrambe le versioni; niente frammenti `#` negli URL mobile; equivalenti mobile per ogni pagina desktop (non reindirizzare più URL desktop alla stessa pagina/home mobile, altrimenti escono dall'indice); verificare entrambe le versioni in Search Console; `hreflang` separati (mobile→mobile, desktop→desktop); capacità del server mobile sufficiente per l'aumento di scansione; stesse regole robots.txt; desktop = canonico, mobile = alternate (`<link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.example.com/">` sulla desktop; `<link rel="canonical" href="https://example.com/">` sulla mobile).
- Errori comuni (troubleshooting): dati strutturati mancanti; `noindex` sulla pagina mobile; immagine mancante; immagine bloccata da robots.txt; immagine di bassa qualità; alt mancante; title mancante; meta description mancante; URL mobile = pagina di errore; URL mobile con frammento; pagina mobile bloccata da robots.txt; più pagine desktop → stessa pagina mobile; desktop che reindirizza alla home mobile; problemi di qualità (annunci, contenuti mancanti, intestazioni, immagini); problemi video; carico host insufficiente. Strumento: Controllo URL per vedere la pagina renderizzata.

## Disattivare o mettere in pausa temporaneamente un sito web
Fonte: https://developers.google.com/search/docs/crawling-indexing/pause-online-business?hl=it

- Opzione CONSIGLIATA per pause temporanee (settimane/mesi): mantenere il sito online limitandone le funzionalità: disattivare il carrello; banner/popup su tutte le pagine con lo stato (ritardi, spedizioni, ritiro) usando `data-nosnippet` per non farlo finire negli snippet e rispettando le linee guida sugli interstitial; aggiornare i dati strutturati (`Product`, `Book`, `Event` → disponibilità/evento annullato; `LocalBusiness` → orari attuali); Merchant Center: attributo disponibilità; informare Google (Controllo URL per poche pagine, Sitemap per molte).
- Opzione NON consigliata: disattivare l'intero sito; solo per brevissimo tempo (alcuni giorni al massimo). La rimozione completa dall'indice ha tempi di ripristino non prevedibili e non accelerabili. Conseguenze: clienti non informati; informazioni di prima mano sostituite da terze parti; schede informative possono perdere telefono e logo; verifica Search Console fallisce e i report perdono dati; reindicizzazione difficile.
- Se si procede: 1-2 giorni → pagina di errore informativa con `503`; periodo più lungo → home segnaposto indicizzabile con `200`; per nascondere subito → rimozione temporanea dalla Ricerca.
- Best practice disattivazione: con `503` Google non può aggiornare titoli, descrizioni, metadati, dati strutturati. Continuare a consentire la scansione in robots.txt; NON servire robots.txt con `503` (blocca completamente la scansione); verificare il `503` con `curl -I -X GET "https://www.example.com/"`; header `Retry-After`; HTML statico, risorse minime (CSS inline, immagini base64); indicazioni chiare agli utenti (link, data di ritorno, contatti). NON bloccare tutto in robots.txt (contenuti e URL possono essere rimossi); NON usare `403`, `404`, `410`, `X-Robots-Tag` o meta `noindex` (rimozione URL); NON usare lo strumento di rimozione temporanea per le chiusure.
- FAQ: anche poche settimane di chiusura completa possono avere conseguenze negative; escludere prodotti non essenziali va bene (limitando acquisti); ridurre la frequenza di scansione è possibile ma sconsigliato salvo problemi critici di risorse (ricordarsi di ripristinarla); Google scansiona generalmente dagli USA → bloccare gli USA impedisce alla Ricerca di accedere; non bloccare aree geografiche, limitare le funzionalità; non usare lo strumento Rimozioni per prodotti non disponibili (meglio segnarli come non disponibili).

## Rimuovere dai risultati di ricerca le immagini ospitate sul tuo sito
Fonte: https://developers.google.com/search/docs/crawling-indexing/prevent-images-on-your-page?hl=it

- Urgente: strumento Rimozioni (temporaneo; senza rimozione/blocco sul sito le immagini possono riapparire alla scadenza).
- Non urgente: robots.txt `disallow` oppure header `X-Robots-Tag: noindex`. Stesso effetto; NON combinarli (con robots.txt Googlebot non vede l'header). Se non si controlla l'host (CDN) o il CMS, può servire eliminare le immagini.
- robots.txt nella root dell'host che serve le immagini; più lento dello strumento Rimozioni ma più flessibile (wildcard) e vale per tutti i motori. Esempi: `User-agent: Googlebot-Image` + `Disallow: /images/dogs.jpg`; `Disallow: /images/animal-picture-*.jpg`; `Disallow: /` (tutte); `Disallow: /*.gif$`. `Googlebot-Image` esclude da Google Immagini; `Googlebot` esclude da tutte le ricerche Google.
- `X-Robots-Tag: noindex` richiede che l'URL immagine sia scansionabile. Il meta `noimageindex` su una pagina blocca le immagini di quella pagina, ma possono essere indicizzate tramite altre pagine; per bloccare un'immagine ovunque usare l'header.
- Immagini non proprie / che ritraggono la persona: procedure di rimozione di informazioni personali.

## Rendere i link in uscita idonei per Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links?hl=it

- Link normali: nessun `rel` necessario.
- `rel="sponsored"`: link pubblicitari/a pagamento (`nofollow` ancora accettabile ma `sponsored` preferibile).
- `rel="ugc"`: link in contenuti generati dagli utenti (commenti, forum); si può togliere per collaboratori di fiducia.
- `rel="nofollow"`: quando gli altri non si applicano e non si vuole associare il sito alla pagina o farla scansionare dal proprio sito. Per link interni al proprio sito usare invece `disallow` in robots.txt.
- Valori multipli separati da spazio o virgola (`rel="ugc nofollow"`, `rel="ugc,nofollow"`).
- I link con questi `rel` in genere non vengono seguiti, ma le pagine possono essere scoperte altrimenti (Sitemap, link esterni). Valgono solo su `<a>` scansionabili (eccetto `nofollow`, disponibile anche come meta robots).
- Per impedire l'indicizzazione: consentire la scansione e usare `noindex`.

## Rimuovere da Google una pagina ospitata sul tuo sito
Fonte: https://developers.google.com/search/docs/crawling-indexing/remove-information?hl=it

- Rimozione rapida: strumento Rimozioni (entro un giorno). Proteggere/rimuovere tutte le varianti URL (es. `example.com/puppies`, `example.com/PUPPIES`, `example.com/petchooser?pet=puppies`).
- Le richieste durano circa 6 mesi. Rimozione definitiva: rimuovere/aggiornare i contenuti (unico modo sicuro anche per motori che non rispettano `noindex`); password; `noindex`. NON usare robots.txt per bloccare la pagina.
- Altre proprietà: disattivazione proprietà specifiche (Shopping ecc.); Profilo dell'attività (modificare le informazioni); scheda informativa (Knowledge Panel) da aggiornare tramite la procedura dedicata. Contenuti su siti altrui: procedura di rimozione informazioni personali.

## Specifiche relative al meta tag Robots, a data-nosnippet e X-Robots-Tag
Fonte: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag?hl=it

- Le regole sono lette solo se il crawler può accedere alla pagina. `<meta name="robots" content="noindex">` vale per i crawler di ricerca; per crawler non di ricerca (es. `AdsBot-Google`) servono regole dedicate (`<meta name="AdsBot-Google" content="noindex">`).
- Meta robots nel `<head>`; `name` e `content` case-insensitive. Token supportati nel meta: `robots` (tutti), `googlebot` (tutti i risultati di testo), `googlebot-news` (notizie); altri valori ignorati. Più crawler → più meta tag. Google rispetta il meta robots anche se è nel `<body>`. Per risorse non HTML (PDF, video, immagini) usare `X-Robots-Tag`.
- `X-Robots-Tag`: ogni regola del meta è utilizzabile come header; più header o regole separate da virgole; user agent facoltativo prima delle regole (`X-Robots-Tag: googlebot: nofollow`); senza UA vale per tutti; case-insensitive.
- Conflitti: vince la regola più restrittiva (es. `max-snippet:50` + `nosnippet` → `nosnippet`). Più crawler con regole diverse: somma delle regole negative (`robots: nofollow` + `googlebot: noindex` → `noindex, nofollow` per Googlebot).
- Regole valide (case-insensitive; elenco anche in formato JSON `robots-tags.json`; altri motori possono trattarle diversamente):
  - `all`: predefinito, nessun effetto.
  - `noindex`: non mostrare pagina/media/risorsa nei risultati.
  - `nofollow`: non seguire i link della pagina.
  - `none` = `noindex, nofollow`.
  - `nosnippet`: niente snippet testuale né anteprima video (la miniatura statica può restare); vale per ricerca web, Immagini, Discover, AI Overview, Modalità AI e impedisce l'uso dei contenuti come input diretto per AI Overview e Modalità AI. Per parti specifiche: `data-nosnippet`.
  - `indexifembedded`: consente l'indicizzazione dei contenuti se incorporati via iframe nonostante `noindex`; efficace solo insieme a `noindex`.
  - `max-snippet:[numero]`: max caratteri dello snippet; vale anche per AI Overview e Modalità AI (limita l'input diretto); non si applica dove il publisher ha concesso altri permessi (dati strutturati in-page, licenze). `0` = nosnippet; `-1` = scelta di Google; ignorata se il numero non è analizzabile.
  - `max-image-preview:[none|standard|large]` (large = larga fino al viewport). Per evitare miniature grandi con AMP/canonica: `standard` o `none`.
  - `max-video-preview:[numero]` secondi; `0` = solo immagine statica; `-1` = nessun limite.
  - `notranslate`: non offrire la traduzione del risultato.
  - `noimageindex`: non indicizzare le immagini della pagina.
  - `unavailable_after:[data/ora]` (RFC 822, RFC 850, ISO 8601): dopo la data la pagina non viene mostrata e la scansione dell'URL cala molto; ignorata se data non valida.
- Regole storiche/ignorate: `noarchive` (link Copia cache non esiste più), `nocache`, `nositelinkssearchbox` (casella di ricerca sitelink non esiste più).
- Combinazioni: `content="noindex, nofollow"` o più meta; es. `max-snippet:20, max-image-preview:large`.
- `data-nosnippet`: attributo booleano solo su `span`, `div`, `section` (valori ignorati; su tag personalizzati NON valido); HTML valido con tag chiusi (un `div` non chiuso include tutto il resto). L'estrazione può avvenire prima o dopo il rendering → NON aggiungere/rimuovere `data-nosnippet` via JS su nodi esistenti; se si crea il nodo via JS includerlo subito. Custom element: avvolgerli in div/span/section.
- Dati strutturati: le restrizioni dei meta robots non incidono sui dati strutturati, salvo `article.description` e `description` di altre opere creative (limitabili con `max-snippet`). I dati strutturati restano utilizzabili anche dentro un elemento `data-nosnippet`. Per limitarli, modificare i dati stessi.
- `X-Robots-Tag` lato server: Apache (`.htaccess`/`httpd.conf`, es. `<Files ~ "\.pdf$"> Header set X-Robots-Tag "noindex, nofollow" </Files>`), NGINX (`location ~* \.pdf$ { add_header X-Robots-Tag "noindex, nofollow"; }`); esempi per immagini `\.(png|jpe?g|gif)$` e file singoli.
- Combinazione con robots.txt: se l'URL è bloccato in robots.txt le regole meta/header non vengono viste e sono ignorate → non bloccare in robots.txt gli URL di cui si vuole far rispettare le regole.

## Introduzione ai file robots.txt
Fonte: https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=it

- robots.txt indica a quali URL i crawler possono accedere; serve principalmente a evitare sovraccarichi; NON è un meccanismo per escludere pagine da Google (usare `noindex` o password). CMS (Wix, Blogger): usare le impostazioni del CMS.
- Effetti per tipo di file:
  - Pagine web (HTML, PDF e altri formati testuali): gestire traffico o evitare la scansione di pagine simili/non importanti. NON usarlo per nascondere pagine: l'URL può essere indicizzato (es. se linkato con testo descrittivo) e appare senza descrizione. Le risorse incorporate nella pagina bloccata sono escluse salvo riferimenti da pagine scansionabili.
  - File multimediali (immagini, video, audio): gestisce traffico e impedisce la comparsa nei risultati (non impedisce che altri li linkino).
  - File di risorse (immagini, script, stili non importanti): bloccabili solo se la pagina resta comprensibile senza; altrimenti non bloccarli.
- Limiti: non tutti i motori supportano le regole; i crawler possono interpretare la sintassi diversamente; i crawler non affidabili possono ignorarlo (per informazioni riservate usare password); una pagina bloccata può essere indicizzata se linkata (URL e anchor text possono comparire). Combinare regole di scansione e indicizzazione può creare conflitti.

## Modificare l'hosting (spostamento senza modifiche agli URL)
Fonte: https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes?hl=it

- Per cambio di provider host o passaggio a CDN SENZA cambi agli URL visibili (altrimenti vedere "Come spostare un sito").
- Fasi: preparare la nuova infrastruttura → cambiare il DNS → monitorare il traffico → spegnere la vecchia infrastruttura quando il traffico (incluso Googlebot) è zero.
- Preparazione: copiare il sito (file o export DB) e testarlo (ambiente di test con accesso limitato per IP; controllare pagine, immagini, moduli, download PDF); test pubblico con hostname temporaneo (es. `beta.example.com`) con `noindex` per evitare indicizzazione accidentale; Search Console (verificare anche l'hostname temporaneo) e Controllo URL per accertare che Googlebot raggiunga la nuova infrastruttura; controllare firewall/protezione DoS che potrebbe bloccare Googlebot su DNS o server; ridurre il TTL DNS a poche ore almeno una settimana prima; mantenere la verifica Search Console (file HTML, meta tag o Google Analytics nei template).
- Avvio: rimuovere blocchi temporanei (robots.txt, `noindex` meta/header) dalla nuova copia; aggiornare i record DNS.
- Monitoraggio: log di vecchio e nuovo server; strumenti di verifica DNS pubblici da più ISP; report di copertura dell'indice.
- Normale un calo temporaneo della frequenza di scansione subito dopo, poi aumento nei giorni successivi (anche oltre i livelli precedenti) se la nuova infrastruttura non ha problemi.

## Come spostare un sito (con modifiche agli URL)
Fonte: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes?hl=it

- Casi: HTTP→HTTPS; cambio dominio (`example.com`→`example.net`) o unione di domini/host; cambio percorsi (`page.php?id=1`→`/widget`, `.html`→`.htm`).
- Fasi: best practice → preparare e testare il nuovo sito → mappatura URL vecchi→nuovi → redirect lato server → monitoraggio.
- Best practice generali:
  - Siti grandi: eventualmente spostare prima una sezione di prova (stabile, poco soggetta a eventi), non necessariamente indicativa del totale.
  - Una modifica alla volta (prima dominio, poi layout/CMS).
  - Spostare nei periodi di minor traffico.
  - Attendersi fluttuazioni temporanee di posizionamento: per siti medi alcune settimane o più prima che Google mostri i nuovi URL (di più per i grandi); dipende da numero di URL e velocità dei server; la Sitemap aiuta.
  - I redirect `301` e altri permanenti NON causano perdita di PageRank.
  - Usare Search Console (proprietà separate; report Stato dell'indicizzazione; report Sitemap).
  - Pazienza: Googlebot deve visitare ogni URL vecchio e nuovo almeno una volta; lo spostamento avviene URL per URL.
- Preparare il nuovo sito: CMS (meglio lo stesso) e import dei contenuti; trasferire immagini e download (PDF); certificati TLS per HTTPS; robots.txt del nuovo sito pronto come dovrà essere al lancio (se si blocca tutto in sviluppo) ed elenco degli URL da cui togliere `noindex`; contenuti eliminati/uniti → `404` o `410`; verificare in Search Console vecchio e nuovo sito e tutte le varianti (www/non-www, HTTP/HTTPS); verifica che resti valida (token diversi se cambia l'URL; file HTML, meta tag, GA nei template); replicare impostazioni (frequenza di scansione "Consenti a Googlebot di determinarla"; file di disavow ricaricato nel nuovo account); dominio acquistato di recente: controllare azioni manuali (richiesta di riconsiderazione) e rimozioni URL del vecchio proprietario; analytics su entrambi i siti (eventualmente nuovo profilo GA); risorse server sufficienti (scansione temporaneamente più intensa; avvisare l'hosting per siti grandi).
- Mappatura URL: spostamenti semplici (solo dominio) → redirect con caratteri jolly lato server; complessi → elenco URL vecchi: partire dagli importanti (Sitemap, log/analytics per traffico, report "Link che rimandano al tuo sito"), elenco dal CMS, log recenti (considerare stagionalità), includere immagini, video, JS e CSS. Salvare la mappatura in DB o regole di rewrite.
- Aggiornare il nuovo sito: canonical autoreferenziale su ogni nuovo URL; `hreflang` aggiornati; link interni aggiornati; salvare una Sitemap dei nuovi URL e l'elenco dei siti che linkano ai vecchi URL.
- Strategia redirect: permanenti lato server (`301`, `308`) vecchio→nuovo; redirect client-side solo come ultima risorsa. Siti piccoli/medi: spostare tutto insieme (l'algoritmo rileva lo spostamento più facilmente); siti grandi: per sezioni. Evitare catene: Googlebot segue fino a 10 hop, ma reindirizzare direttamente alla destinazione finale; se impossibile, idealmente non più di 3 e meno di 5 hop (latenza; non tutti i client supportano catene lunghe).
- Avvio: attivare i redirect; NON reindirizzare molti URL a un'unica destinazione (es. home): confonde e può essere trattato come soft 404 (ok solo se contenuti uniti in una pagina); controllare canonical e meta robots (togliere `noindex` di sviluppo); testare i redirect (Controllo URL, script/CLI); strumento "Cambio di indirizzo" in Search Console SOLO per cambio dominio/sottodominio (es. `example.com`→`example.net`, `a.example.com`→`b.example.com`), non per HTTP→HTTPS, www↔non-www o cambi di percorso; inviarlo per tutte le varianti verificate del vecchio dominio (sottodomini, www/non-www) anche se inutilizzate; mantenere i redirect il più a lungo possibile, in genere almeno 1 anno (per gli utenti valutare a tempo indeterminato); inviare la nuova Sitemap (la vecchia si può rimuovere). Tempi: alcune settimane per siti piccoli/medi; visibilità che varia temporaneamente è normale.
- Aggiornare i link: interni; esterni (contattare i siti, priorità per traffico); profili social (Facebook, Twitter, LinkedIn); campagne pubblicitarie.
- Monitoraggio: Search Console (Sitemap vecchia e nuova: le pagine indicizzate passano dalla vecchia alla nuova; gli avvisi di redirect sulla Sitemap vecchia sono normali; report copertura indice; query di ricerca); log server ed errori; analytics (GA tempo reale).
- Risorse esterne citate: checklist di migrazione di Aleyda Solis, guida Screaming Frog.
- Errori comuni: `noindex`/robots.txt di migrazione non rimossi (se robots.txt non esiste deve restituire `404` corretto); redirect verso URL sbagliati/inesistenti (molti "Non trovato" in Search Console; verificare con Screaming Frog); picchi di altri errori di scansione; capacità server insufficiente; Sitemap non aggiornate.

## Creare e inviare una Sitemap
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=it

- Formati supportati (protocollo sitemaps.org; Google non ha preferenze): XML (il più versatile; estensioni immagini, video, notizie, versioni localizzate; generato da molti CMS/plugin; complesso su siti grandi o URL che cambiano spesso); RSS 2.0 / mRSS / Atom 1.0 (spesso automatici nei CMS; oltre a HTML/testo solo info video, non immagini né notizie; forniscono solo URL recenti); testo (un URL per riga, solo URL, estensione `.txt`, file UTF-8; solo pagine HTML/testuali).
- Limiti: 50 MB non compressi o 50.000 URL per Sitemap (tutti i formati) → oltre, dividere; facoltativo indice Sitemap. Si possono inviare più Sitemap/indici (utile per monitorare il rendimento per Sitemap in Search Console).
- Codifica UTF-8. Posizione: ovunque, ma senza invio via Search Console una Sitemap copre solo i discendenti della directory padre → consigliata la root.
- URL assoluti e completi (es. `https://www.example.com/mypage.html`, non `/mypage.html`); Google scansiona gli URL esattamente come indicati.
- Includere gli URL che si vogliono nei risultati (canonici). Desktop/mobile separati: preferibilmente una sola versione; se entrambe, annotarle.
- XML: `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`, `<url><loc>…</loc><lastmod>2022-06-04</lastmod></url>`; valori con escape XML. Google IGNORA `<priority>` e `<changefreq>`. Usa `<lastmod>` se coerentemente e verificabilmente corretto; deve riflettere l'ultimo aggiornamento significativo (contenuti principali, dati strutturati, link — non la data del copyright).
- Creazione: dal CMS (WordPress, Wix, Blogger spesso già la forniscono); manuale se meno di qualche decina di URL; generata automaticamente oltre (meglio dal software del sito/database). L'ordine degli URL è indifferente.
- Invio (solo un suggerimento, nessuna garanzia): report Sitemap di Search Console (mostra accessi ed errori); API Search Console; riga `Sitemap: https://example.com/my_sitemap.xml` in robots.txt (illimitate); WebSub per RSS/Atom.
- Più siti: un'unica Sitemap con URL di più siti verificati (anche domini diversi) o Sitemap separate nello stesso percorso; invio via Search Console (proprietà verificate) o via robots.txt di ciascun sito che punta alla Sitemap ospitata altrove (es. `sitemap: https://sitemaps.example.com/sitemap-example-com.xml`).
- Errori: report Sitemap di Search Console.

## Come combinare le estensioni Sitemap
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/combine-sitemap-extensions?hl=it

- Namespace: `image:` `http://www.google.com/schemas/sitemap-image/1.1`; `news:` `http://www.google.com/schemas/sitemap-news/0.9`; `video:` `http://www.google.com/schemas/sitemap-video/1.1`; `xhtml:` (per `hreflang`) `http://www.w3.org/1999/xhtml`. Dichiararli con `xmlns:` su `<urlset>`.
- I tag delle estensioni si aggiungono uno dopo l'altro dentro `<url>`; ordine irrilevante dopo `<loc>`. Esempio `hreflang`: `<xhtml:link rel="alternate" hreflang="de" href="..."/>`.
- Combinare estensioni aumenta molto la dimensione: rispettare i limiti.

## Sitemap di immagini
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps?hl=it

- Utili per immagini che Google non troverebbe altrimenti (es. caricate via JavaScript). Sitemap separata o tag aggiunti a quella esistente.
- Tag obbligatori: `<image:image>` (fino a 1000 per `<url>`), `<image:loc>` (URL immagine; può essere su un altro dominio, es. CDN, purché entrambi i domini siano verificati in Search Console e robots.txt non blocchi).
- Ritirati: `<image:caption>`, `<image:geo_location>`, `<image:title>`, `<image:license>`.

## Gestire le Sitemap con un file indice Sitemap
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps?hl=it

- Per Sitemap oltre i limiti: dividerle e usare un indice (stesso formato/requisiti delle Sitemap).
- Le Sitemap referenziate devono stare sullo stesso sito dell'indice (salvo invio tra siti) e nella stessa directory o in una inferiore.
- Fino a 500 file indice Sitemap per sito in un account Search Console. Un indice può contenere fino a 50.000 tag `loc`.
- Tag obbligatori: `sitemapindex`, `sitemap`, `loc`. Facoltativo: `lastmod` (formato W3C Datetime). Esempio con Sitemap `.xml.gz`.

## Sitemap per Google News
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap?hl=it

- Per editori giornalistici. Aggiornare la stessa Sitemap man mano (non crearne una nuova a ogni aggiornamento). Includere solo articoli degli ultimi 2 giorni; poi rimuovere URL o metadati `<news:news>`; una Sitemap vuota genera un avviso in Search Console ma non crea problemi.
- Tag obbligatori: `<news:news>` (uno per `<url>`, max 1000 per Sitemap), `<news:publication>`, `<news:name>` (identico al nome su news.google.com, escluso testo tra parentesi), `<news:language>` (ISO 639, 2-3 lettere; `zh-cn`/`zh-tw`), `<news:publication_date>` (W3C; data di prima pubblicazione, non di aggiunta alla Sitemap), `<news:title>` (titolo com'è sul sito, senza autore, testata o data).
- Non pertinente per siti vetrina/portfolio.

## Informazioni sulle Sitemap
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview?hl=it

- Una Sitemap informa su pagine, video, file e loro relazioni (ultimo aggiornamento, versioni linguistiche); aiuta una scansione più efficiente. Voci per video (durata, rating, età), immagini (posizione), notizie (titolo, data). CMS spesso la forniscono già.
- Con un buon linking interno Google trova gran parte dei contenuti; la Sitemap non garantisce scansione/indicizzazione ma è un vantaggio nella maggior parte dei casi.
- Utile se: sito grande; sito NUOVO con pochi link esterni; molti contenuti rich media o presenza in Google News.
- Potrebbe non servire se: sito piccolo (circa 500 pagine al massimo, contando solo quelle da mostrare nei risultati); linking interno completo dalla home; pochi media/notizie da mostrare.

## Sitemap per i video e alternative
Fonte: https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps?hl=it

- Consigliate le Sitemap video; supportati anche feed mRSS. Separata o integrata.
- Requisiti: non elencare video non correlati al contenuto della pagina host; tutti gli URL accessibili a Googlebot (consentiti da robots.txt, senza metafile né login, non bloccati da firewall, protocolli HTTP/FTP — streaming non supportato). Per proteggere `player_loc`/`content_loc` dagli spammer verificare Googlebot.
- Obbligatori: `<video:video>`, `<video:thumbnail_loc>`, `<video:title>` (escape o CDATA; consigliato uguale al titolo in pagina), `<video:description>` (max 2048 caratteri; coerente con la pagina), e almeno uno tra `<video:content_loc>` (preferito; formati supportati; non HTML/Flash; ≠ `<loc>`; = `VideoObject.contentUrl`) e `<video:player_loc>` (≠ `<loc>`; per YouTube/Vimeo/iframe; = `VideoObject.embedUrl`).
- Facoltativi: `duration` (1–28800 s, 8 ore), `expiration_date` (W3C), `rating` (0.0–5.0), `view_count`, `publication_date`, `family_friendly` (yes/no; SafeSearch), `restriction` (ISO 3166, `relationship` allow/deny; solo risultati di ricerca), `platform` (web, mobile, tv; allow/deny), `requires_subscription`, `uploader` (max 255 caratteri; `info` sullo stesso dominio di `<loc>`), `live`, `tag` (max 32 per video).
- Ritirati: `<video:category>`, `<video:gallery_loc>`, attributi `autoplay`/`allow_embed` di `player_loc`, `<video:price>`, `<video:tvshow>`.
- mRSS: obbligatori `<media:content>` (`medium="video"`, `url` o in alternativa `<media:player>`, `duration` consigliato), `<media:player>` (≠ `<link>`), `<media:title>` (max 100 caratteri), `<media:description>` (max 2048), `<media:thumbnail>`; facoltativi `<dcterms:valid>`, `<media:restriction>` (`type="country"`, allow/deny), `<media:price>` (ISO 4217; rent/purchase/package/subscription; non usarlo per video gratuiti).
- Esempi di embed YouTube (`https://www.youtube.com/embed/...`) e Vimeo (`https://player.vimeo.com/video/...`) come `player_loc`.

## Meta tag e attributi supportati da Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/special-tags?hl=it

- I meta tag vanno nel `<head>`; i client ignorano quelli non supportati. CMS: usare le impostazioni.
- Supportati:
  - `description`: breve descrizione; a volte usata nello snippet.
  - `robots` (tutti i motori) / `googlebot` (solo Google): in conflitto vince il più restrittivo; default `index, follow` (non va specificato). Equivalente header `X-Robots-Tag` (utile per non-HTML).
  - `<meta name="googlebot" content="notranslate">`: niente titolo/snippet tradotti (altrimenti le interazioni passano da Google Traduttore).
  - `<meta name="google" content="nopagereadaloud">`: blocca i servizi TTS di Google.
  - `google-site-verification`: verifica Search Console nella pagina di primo livello; `name` e `content` devono corrispondere esattamente (case-sensitive); indifferente HTML/XHTML.
  - `Content-Type`/`charset` (`<meta http-equiv="Content-Type" content="...; charset=...">` con valore tra virgolette, o `<meta charset="...">`): consigliato UTF-8.
  - `refresh` (meta refresh): non supportato da tutti i browser e può confondere; consigliato sostituirlo con `301` lato server.
  - `viewport`: indica a Google che la pagina è ottimizzata per il mobile.
  - `rating` (`adult` o `RTA-5042-1996-1400-1577-RTA`): contenuti per adulti filtrati da SafeSearch.
- Attributi HTML: `src` e `href` per scoprire risorse/URL; attributi `rel` per qualificare i link; `data-nosnippet` su `div`, `span`, `section`.
- Note: Google legge meta HTML e XHTML; `<head>` deve essere HTML valido con tag chiusi; maiuscole/minuscole irrilevanti nei meta tranne `google-site-verification`; meta non supportati ignorati; evitare se possibile di inserire/modificare meta con JavaScript (se necessario testare a fondo); verificare con Controllo URL.
- NON supportati/ignorati: `<meta name="keywords">` (nessun effetto su indicizzazione e ranking); attributo `lang` (Google rileva la lingua dal testo); `<link rel="next">`/`rel="prev"` (non più usati); `nositelinkssearchbox` (funzionalità non più esistente).

## Risolvi i problemi relativi agli errori di scansione della Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors?hl=it

- Passi: problemi di disponibilità; pagine che dovrebbero essere scansionate e non lo sono; aggiornamenti scansionati con poca tempestività; efficienza; scansione eccessiva.
- Disponibilità: migliorarla non aumenta necessariamente il budget (dipende dalla domanda) ma i problemi limitano la scansione. Diagnosi: report Statistiche di scansione (grafici disponibilità host, linea rossa); Controllo URL con avviso "Carico host superato". Gestione: bloccare pagine inutili, velocizzare caricamento/rendering, aumentare capacità server (es. per un mese e verificare se aumentano le richieste).
- Pagine non scansionate: verificare nei log del server (Search Console non filtra la cronologia per URL). Per la maggior parte dei siti servono diversi giorni per scoprire nuove pagine (eccetto siti di notizie). Cause: pagine non note, bloccate, capacità esaurita, budget esaurito. Azioni: aggiornare Sitemap; controllare robots.txt; gestire inventario; capacità server. Le pagine scansionate possono non apparire se valore/domanda insufficienti.
- Tempestività: per la maggior parte dei siti attesa minima di 3 giorni; non aspettarsi indicizzazione in giornata (salvo news o contenuti time-sensitive). Diagnosi: log, Controllo URL. Consigliato: Sitemap News (se news); `<lastmod>`; struttura URL semplice; link `<a>` standard; se HTML mobile/desktop separati, stesso insieme di link (altrimenti includerli in Sitemap) perché Google indicizza solo la versione mobile. Sconsigliato: inviare la stessa Sitemap invariata più volte al giorno; aspettarsi scansione completa/immediata della Sitemap; includere in Sitemap URL che non si vogliono nella Ricerca.
- Efficienza: velocità di risposta e rendering contano, ma velocizzare pagine di scarsa qualità non aumenta la scansione; bloccare con robots.txt solo risorse grandi non critiche (es. immagini decorative); evitare catene di redirect; attenzione a risorse voluminose/lente necessarie all'indicizzazione.
- `If-Modified-Since`/`If-None-Match`: non inviati sempre (AdsBot più spesso); si può rispondere `304` senza corpo se il contenuto non è cambiato (anche a prescindere dagli header della richiesta).
- Nascondere URL inutili (non trasferisce budget salvo limite di capacità): facet e ID di sessione, duplicati, soft 404 (rispondere `404`), pagine compromesse (report Problemi di sicurezza), spazi infiniti e proxy (robots.txt), contenuti di scarsa qualità/spam, carrello, scroll infinito, pagine-azione (registrazione, acquisto). Consigliato: robots.txt per ciò che non si vuole scansionare; stesso URL per risorse condivise tra pagine (cache). Sconsigliato: modificare spesso robots.txt o alternare Sitemap/occultamenti temporanei per riallocare budget.
- Soft 404: URL che mostra "pagina inesistente" (o pagina vuota/senza contenuto principale) con `200`. Cause: include server mancante, DB disconnesso, ricerca interna vuota, file JS non caricato. Escluse dalla Ricerca; segnalate nel report Indicizzazione delle pagine. Correzioni: contenuto rimosso senza sostituto → `404`/`410` (pagina 404 personalizzata utile: messaggio chiaro e cordiale, stesso layout e navigazione, link ai contenuti popolari e alla home, modo per segnalare link rotti; ma il server deve restituire `404`); contenuto spostato → `301`; pagina valida segnalata come soft 404 → controllare con Controllo URL rendering e codice: risorse non caricate (bloccate da robots.txt, troppe, errori server, troppo grandi/lente) possono renderla vuota.
- Scansione eccessiva (emergenza): restituire temporaneamente `503` o `429`; Googlebot riprova per circa 2 giorni; oltre 2 giorni gli URL vengono eliminati dall'indice e la scansione rallenta/si interrompe; monitorare capacità. AdsBot: target per annunci dinamici della rete di ricerca → scansione ripetuta ogni 3 settimane; limitare i target o aumentare la capacità.

## Best practice per la struttura degli URL per la Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/url-structure?hl=it

- Requisiti per URL scansionabili (altrimenti scansione inefficiente: frequenze altissime o nessuna scansione):
  - Seguire IETF STD 66; i caratteri riservati vanno codificati in percentuale.
  - NON usare frammenti (`https://example.com/#/potatoes`) per cambiare contenuto: generalmente non supportati; con JS usare l'API History.
  - Parametri: `=` per chiave/valore, `&` tra parametri; più valori per una chiave con carattere compatibile (es. virgola: `color=purple,pink,salmon`). Sconsigliati `?[category:dresses][sort:...]` o `?category,dresses,,sort,...`.
- Best practice di leggibilità:
  - URL descrittivi con parole (es. `/wiki/Aviation`) invece di lunghi ID.
  - Parole nella lingua del pubblico (anche traslitterate), es. tedesco `/lebensmittel/pfefferminz`, giapponese.
  - Negli `href` codificare in percentuale i caratteri non ASCII (es. `gem%C3%BCse` invece di `gemüse`; emoji codificate); ASCII non riservati possono restare non codificati.
  - Trattini `-` per separare le parole, NON trattini bassi `_` (usati per tenere insieme concetti, es. `format_date`) e non parole unite (`/greendress`).
  - Meno parametri possibile (eliminare quelli che non cambiano il contenuto).
  - URL case-sensitive (`/APPLE` ≠ `/apple`): se il server tratta maiuscole/minuscole allo stesso modo, uniformare.
  - Multiregionali: ccTLD (`https://example.de`) o sottodirectory per paese su gTLD (`https://example.com/de/`).
- Problemi comuni (troppi URL per contenuti identici/simili → spreco di banda, indicizzazione incompleta): filtri combinabili (es. hotel); parametri irrilevanti (referral, ordinamento, ID sessione: preferire cookie; bloccare con robots.txt); calendari infiniti (`nofollow` sui link a pagine future generate dinamicamente); link relativi alla directory superiore (`../../category/stuff`) che generano spazi infiniti se il server non risponde con il codice corretto → usare URL relativi alla root.
- Soluzioni: robots.txt per URL dinamici (risultati di ricerca interni), spazi infiniti (calendari), ordinamento e filtri; guida facet.

## Utilizzare codice HTML valido per specificare i metadati della pagina
Fonte: https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata?hl=it

- Google tenta di capire anche HTML non valido, ma errori nel markup possono impedire l'uso dei metadati. Se nell'`<head>` c'è un elemento non valido, Google ignora tutti gli elementi successivi (presuppone la fine dell'head).
- Elementi validi nell'`<head>`: `title`, `meta`, `link`, `script`, `style`, `base`, `noscript`, `template`.
- Non validi frequenti: `iframe`, `img`. Evitarli; se proprio necessari, metterli DOPO gli elementi che Google deve leggere.

## Ridurre al minimo l'impatto dei test A/B nella Ricerca Google
Fonte: https://developers.google.com/search/docs/crawling-indexing/website-testing?hl=it

- Test A/B e multivariati: con URL diversi (redirect di parte degli utenti) o sullo stesso URL con varianti inserite via JavaScript. Piccole modifiche (colore/posizione pulsanti, testo CTA) hanno impatto minimo o nullo su snippet/ranking.
- Best practice: NO cloaking (mostrare URL/contenuti diversi a Googlebot e utenti viola le norme anti-spam, anche via robots.txt; rischio retrocessione/rimozione); Googlebot in genere non supporta i cookie (vede la versione per browser senza cookie); `rel="canonical"` sulle varianti verso l'URL originale (preferito a `noindex`, che può avere effetti negativi imprevisti); redirect `302` (temporanei), non `301`; ammessi anche redirect JavaScript; durata solo quella necessaria, poi rimuovere URL, script e markup di test (esperimenti prolungati senza motivo, specie se una variante è servita a una quota elevata di utenti, possono essere considerati tentativi di inganno).
- Risorse: articoli e strumenti Google Analytics, forum di assistenza.

---

# Implicazioni per la skill SEO

Sezione ragionata, ancorata alle pagine sopra. Tra parentesi la pagina di riferimento.

## (a) Controlli verificabili automaticamente in un audit

robots.txt
- [ ] `GET /robots.txt` sulla root di OGNI host/protocollo servito (es. `https://www.`, `https://` apex): risponde `200` con `Content-Type` testuale, oppure `404` se assente (ok). Segnalare `5xx`/timeout (blocco scansione 12 h, poi cache 30 gg), `401`/`403` (trattati come "nessun robots"), catene di redirect > 5 hop (→ trattato come 404). (robots-txt-spec)
- [ ] Dimensione ≤ 500 KiB; codifica UTF-8; niente BOM problematico; niente HTML al posto delle regole. (robots-txt-spec)
- [ ] Nessun `Disallow: /` per `*` o `Googlebot` in produzione (residuo di staging). (site-move, robots useful rules)
- [ ] Nessun blocco di risorse necessarie al rendering (`.js`, `.css`, cartelle bundle/asset, endpoint API usati per il contenuto principale). (robots intro, javascript-seo-basics, mobile-first)
- [ ] Nessun URL con `noindex` (meta o header) anche bloccato da robots.txt (il noindex non sarebbe mai letto). (block-indexing, robots-meta-tag)
- [ ] Segnalare direttive non supportate: `crawl-delay`, `noindex:` in robots.txt. (myths, block-indexing)
- [ ] Riga `Sitemap:` con URL assoluto (protocollo + host) e raggiungibile. (create-robots-txt, build-sitemap)
- [ ] Ricordare: AdsBot/Mediapartners ignorano `*` (solo nota). Google-Extended non influisce sulla Ricerca (solo nota, scelta del proprietario). (common/special crawlers)
- [ ] Test regole con matching Google: path case-sensitive, `*` e `$`, precedenza = regola più lunga, a parità vince `allow`. Si può usare la libreria `google/robotstxt` o una reimplementazione. (robots-txt-spec, create-robots-txt)

Sitemap
- [ ] Esiste (consigliata per siti nuovi con pochi backlink anche se piccoli); XML valido, UTF-8, namespace corretto; ≤ 50.000 URL e ≤ 50 MB non compressi per file; indice ≤ 50.000 `loc`. (sitemaps overview, build-sitemap, large-sitemaps)
- [ ] Solo URL assoluti, canonici, indicizzabili, con risposta `200` (niente redirect, 404, noindex, URL bloccati da robots, varianti http/www sbagliate). (build-sitemap, troubleshoot-crawling-errors, consolidate-duplicate-urls)
- [ ] `<lastmod>` presente e plausibile (non tutte le date uguali alla data di build; riflette modifiche significative); segnalare `<priority>`/`<changefreq>` come ignorati (non errore). (build-sitemap)
- [ ] Sitemap nella root (o dichiarata in robots.txt/Search Console); coerenza tra URL in Sitemap e `rel=canonical` della pagina. (build-sitemap, consolidate-duplicate-urls)
- [ ] Image sitemap: max 1000 `<image:image>` per `<url>`; niente tag ritirati (`image:caption`, `image:title`, `image:license`, `image:geo_location`). Video: `description` ≤ 2048, `duration` 1–28800, max 32 `tag`. (image/video sitemaps)

Codici HTTP e redirect
- [ ] Pagine inesistenti → `404`/`410` reali (testare un URL casuale tipo `/questa-pagina-non-esiste-xyz`): se risponde `200` = rischio soft 404 (tipico SPA). (http-status-codes, troubleshoot-crawling-errors, javascript-seo-basics)
- [ ] Varianti host/protocollo (`http://`, `www`/non-www, slash finale, maiuscole) → un solo redirect permanente `301`/`308` verso la canonica; nessuna catena (> 1 hop segnalare; > 3 avviso; 10 = limite Googlebot). (301-redirects, site-move-with-url-changes, http-status-codes)
- [ ] Nessun redirect HTTPS→HTTP; certificato TLS valido e corrispondente all'host. (consolidate-duplicate-urls)
- [ ] Redirect temporanei (`302/307`, meta refresh > 0 s) usati dove si intende uno spostamento permanente → segnalare. Meta refresh in genere → suggerire `301` lato server. (301-redirects, special-tags)
- [ ] Molti URL vecchi rediretti alla home → possibile soft 404. (site-move-with-url-changes)
- [ ] Supporto `ETag`/`Last-Modified` e risposta `304` a richieste condizionali; header `Cache-Control: max-age`. (overview-google-crawlers, crawl-budget)
- [ ] Compressione gzip/br attiva; HTML iniziale e ogni risorsa sotto 2 MB non compressi (limite Googlebot; 15 MB default infrastruttura; PDF 64 MB). (googlebot, overview-google-crawlers)
- [ ] Il sito non blocca IP USA / non ha firewall-WAF che rifiuta Googlebot (verifica via UA Googlebot + note su DNS inverso). (overview-google-crawlers, pause-online-business, dns-network-errors)

Head, meta e canonical
- [ ] `<head>` valido: solo `title`, `meta`, `link`, `script`, `style`, `base`, `noscript`, `template`; nessun `img`/`iframe` prima di meta/canonical (Google smette di leggere). (valid-page-metadata)
- [ ] Un solo `<link rel="canonical">`, URL assoluto, nell'head, autoreferenziale sulle pagine canoniche; nessun conflitto tra HTML iniziale e DOM renderizzato; nessun canonical con `hreflang`/`media`/`lang`/`type` usato come canonical; nessun canonical verso frammento `#`. (consolidate-duplicate-urls, javascript-seo-basics)
- [ ] Meta robots: nessun `noindex` involontario (anche nella versione mobile); nessun `noindex` nell'HTML iniziale "rimosso poi via JS" (non funziona). Segnalare `noarchive`, `nocache`, `nositelinkssearchbox`, `meta keywords`, `rel=next/prev` come ignorati. (robots-meta-tag, special-tags, javascript-seo-basics)
- [ ] Header `X-Robots-Tag` coerente con i meta; regole valide (`max-snippet`, `max-image-preview`, ecc.) con sintassi corretta. (robots-meta-tag)
- [ ] `<meta charset="utf-8">` e `<meta name="viewport">` presenti. (special-tags)
- [ ] `data-nosnippet` solo su `div`/`span`/`section` e presente già nell'HTML (non aggiunto via JS). (robots-meta-tag)
- [ ] `title` e `meta description` presenti e univoci per pagina, identici tra mobile e desktop. (javascript-seo-basics, mobile-first)

Link e URL
- [ ] Tutti i link di navigazione sono `<a href="...">` risolvibili; segnalare `<a>` senza `href`, `href="javascript:..."`, `<span>`/`div` cliccabili, `routerLink` senza `href` renderizzato, link `#/route`. (links-crawlable, javascript-seo-basics)
- [ ] Anchor text non vuoto (o `alt` sull'immagine-link); segnalare anchor generici ("clicca qui", "scopri di più"). (links-crawlable)
- [ ] Ogni pagina importante raggiungibile da almeno un link interno; link interni puntano agli URL canonici (non a varianti/redirect). (links-crawlable, consolidate-duplicate-urls)
- [ ] URL: minuscole coerenti, trattini non underscore, niente ID sessione, niente frammenti per contenuti diversi, parametri `=`/`&`, link relativi alla root (non `../`). (url-structure)
- [ ] Link a pagamento/affiliati con `sponsored`, UGC con `ugc`. (qualify-outbound-links)

Rendering JS (con browser headless)
- [ ] Confronto HTML grezzo vs DOM renderizzato: contenuto principale, title, description, canonical, robots, JSON-LD presenti dopo il rendering; nessun errore JS in console; nessuna dipendenza da localStorage/sessionStorage/cookie o permessi (camera, geolocalizzazione) per mostrare contenuti; contenuti non dipendenti da WebSocket/WebRTC. (fix-search-javascript)
- [ ] Lazy loading: immagini sotto la piega con `loading="lazy"` o IntersectionObserver; nessun contenuto caricato solo a scroll/click; immagini above-the-fold NON lazy. Dopo rendering senza scroll gli `src` reali sono presenti. (lazy-loading)
- [ ] Bundle JS/CSS con hash nel nome file (fingerprinting). (fix-search-javascript, javascript-seo-basics)
- [ ] Web component con shadow DOM: contenuto visibile nel DOM renderizzato (uso di `<slot>`). (javascript-seo-basics)

Ambienti e staging
- [ ] Staging/preview/demo non indicizzabili (noindex o autenticazione) e non linkati; canonical non puntano allo staging (rischio con URL relativi). (canonicalization, consolidate-duplicate-urls, site-move-no-url-changes)
- [ ] File privati (CV con dati personali, PDF) senza metadati sensibili; nessuna email/nome in parametri URL. (keep-redacted-information-out)

## (b) Regole per chi costruisce un sito nuovo

1. Scegliere UN host canonico (es. `https://www.dominio.it` o apex) e reindirizzare con `301` tutte le altre varianti (http, www/non-www). HTTPS con certificato valido, nessun contenuto misto non protetto (salvo immagini), opzionale HSTS. (301-redirects, consolidate-duplicate-urls)
2. Responsive design (stesso HTML e URL per tutti i dispositivi) — è la configurazione consigliata; evitare m-dot e pubblicazione dinamica. Meta viewport. (mobile-first, special-tags)
3. Contenuti, intestazioni, immagini, alt, title, description e dati strutturati identici tra mobile e desktop (con responsive è automatico); usare accordion/schede invece di eliminare testo su mobile. (mobile-first)
4. URL descrittivi, nella lingua del pubblico (italiano per siti italiani), minuscoli, con trattini, senza parametri inutili né ID di sessione; nessun routing a hash. (url-structure)
5. Ogni pagina indicizzabile: `<title>` e meta description univoci, canonical assoluto autoreferenziale nell'head, head valido. (javascript-seo-basics, consolidate-duplicate-urls, valid-page-metadata)
6. Navigazione con veri `<a href>` e anchor descrittivi; ogni pagina importante linkata almeno da un'altra. (links-crawlable)
7. robots.txt minimale: consentire tutto ciò che serve (incluse risorse JS/CSS), bloccare solo spazi inutili (ricerca interna, parametri di filtro/ordinamento, carrello) e dichiarare la Sitemap. Non usarlo per nascondere pagine o dati privati. (robots intro, useful rules, troubleshoot-crawling-errors)
8. Sitemap XML generata automaticamente in build (solo URL canonici `200`, `lastmod` reale); anche per siti piccoli è utile perché un sito nuovo ha pochi link esterni. (sitemaps overview, build-sitemap)
9. 404 vera (codice `404`) con pagina personalizzata utile (stesso layout, link a home e contenuti principali). Pagine rimosse → `404`/`410`; spostate → `301`. (troubleshoot-crawling-errors)
10. Pagine di servizio (grazie, login, area riservata, risultati di ricerca interna) → `noindex` o autenticazione; staging protetto da password + `noindex`. (block-indexing, control-what-you-share)
11. Lazy loading solo sotto la piega e basato su viewport; immagini con URL stabili e formati supportati (JPEG, PNG, WebP, AVIF, SVG, GIF). (lazy-loading, mobile-first, indexable-file-types)
12. Cache HTTP: `ETag` (preferito) + `Last-Modified` + `Cache-Control: max-age`; asset con hash nel nome. (overview-google-crawlers, fix-search-javascript)
13. Al lancio: rimuovere ogni `noindex`/`Disallow: /` di sviluppo, verificare la proprietà in Search Console, inviare la Sitemap, usare Controllo URL sulle pagine chiave. (site-move-with-url-changes, ask-google-to-recrawl)
14. Non aspettarsi indicizzazione in giornata: tipicamente da alcuni giorni ad alcune settimane (min. ~3 giorni per aggiornamenti). Non ripetere richieste di indicizzazione dello stesso URL. (ask-google-to-recrawl, troubleshoot-crawling-errors)
15. Non fare finte modifiche o aggiornare date per sembrare "freschi": irrilevante per il ranking. (myths-about-crawling)

## (c) Note specifiche per SPA JavaScript / Angular

- Google esegue il rendering con Chromium evergreen, ma in coda separata (secondi o più); altri motori/bot (e molti fetcher di anteprima link) potrebbero non eseguire JS. SSR o pre-rendering (Angular SSR / prerender statico delle route) sono indicati da Google come "ottima soluzione"; il rendering dinamico (servire HTML diverso ai bot) è DEPRECATO come approccio. Per un portfolio o un sito professionale con poche route, il prerender statico in build è la scelta più semplice e coerente con le indicazioni. (javascript-seo-basics, dynamic-rendering)
- Routing: usare `PathLocationStrategy` (API History), MAI `HashLocationStrategy` (`/#/route`): i frammenti non sono supportati e i link `#/...` non vengono risolti. (javascript-seo-basics, url-structure, fix-search-javascript)
- Link: `routerLink` su elemento `<a>` produce un `href` nel DOM renderizzato — verificare che l'`href` ci sia; `<a routerLink>` senza href, `(click)` su `div`/`button` per navigare, `href="javascript:..."` sono sconsigliati. (links-crawlable)
- Soft 404: con routing client il server restituisce `200` per qualsiasi route (fallback a `index.html`). Soluzioni Google: (1) redirect JS a un URL che il server serve con `404` (es. `/not-found`), oppure (2) aggiungere via JS `<meta name="robots" content="noindex">` nella route wildcard `**`/pagina "non trovato". Con SSR/prerender è preferibile far restituire al server lo status `404` reale per route sconosciute. Stesso discorso per risorse dinamiche inesistenti (es. `/progetti/slug-inesistente`). (javascript-seo-basics, fix-search-javascript)
- Metadati per route (Angular `Title`/`Meta` service): title, description e canonical impostati per ogni route. Il canonical dovrebbe stare nell'HTML (meglio se prerenderizzato); se impostato via JS: un solo tag, stesso valore dell'HTML originale o assente dall'HTML; attenzione a non duplicarlo navigando tra route (rimuovere/aggiornare quello esistente). (javascript-seo-basics, consolidate-duplicate-urls)
- `noindex`: NON metterlo nell'`index.html` di base sperando di toglierlo via JS: Google può saltare il rendering quando vede `noindex`. (javascript-seo-basics)
- `data-nosnippet` non va aggiunto/rimosso via JS su nodi esistenti. Meta tag in generale: evitare di inserirli/modificarli via JS quando possibile, oppure testare a fondo. (robots-meta-tag, special-tags)
- WRS è stateless: niente dipendenza da localStorage, sessionStorage, cookie, service worker state, permessi (geolocalizzazione per mostrare uno studio locale, ecc.); niente contenuto principale via WebSocket. (fix-search-javascript)
- Cache aggressiva di Googlebot: output Angular con `outputHashing: all` (fingerprinting) per evitare JS/CSS obsoleti. (fix-search-javascript)
- Limite 2 MB non compressi per file (HTML e ogni risorsa JS/CSS scaricata separatamente): controllare la dimensione del bundle principale e dell'HTML prerenderizzato (stato inline/transfer state). (googlebot)
- robots.txt non deve bloccare `/assets/`, `*.js`, `*.css`, né gli endpoint API da cui l'app carica i testi. Le chiamate XHR/fetch consumano budget di scansione (irrilevante su siti piccoli). (robots intro, myths-about-crawling)
- Lazy loading di moduli/immagini: il contenuto deve comparire senza interazioni; `@defer` / caricamenti `on interaction` o `on hover` non sono visibili a Google; usare trigger `on viewport` o rendere subito il contenuto testuale importante. (lazy-loading, mobile-first) [deduzione applicata ad Angular dalle regole sul lazy loading]
- Dati strutturati JSON-LD possono essere iniettati via JS, ma vanno testati (Test dei risultati avanzati / Controllo URL). (javascript-seo-basics)
- Strumenti di verifica: Controllo URL (HTML renderizzato, risorse, console) e Test dei risultati avanzati; la telemetria lato client non riflette Googlebot. (fix-search-javascript)

## (d) Note specifiche per personal brand (portfolio sviluppatore) e professionista locale (orientatrice di carriera)

Comuni
- Sono siti piccoli: il budget di scansione NON è un problema (le guide crawl budget/facet sono per siti > 10.000/1.000.000 pagine). Concentrarsi su accessibilità alla scansione, canonical, 404 reali, link interni e Sitemap. (crawl-budget, myths-about-crawling)
- Sito nuovo con pochi backlink → Sitemap consigliata anche sotto le 500 pagine. (sitemaps overview)
- La scansione/frequenza non è un fattore di ranking; modifiche cosmetiche o date aggiornate non aiutano. (myths-about-crawling)
- Link esterni a fonti autorevoli (certificazioni, enti, pubblicazioni) aiutano l'affidabilità; non mettere `nofollow` su tutto. Link a profili social/LinkedIn/GitHub con anchor descrittivi. (links-crawlable)
- Contenuti uguali su mobile: recruiter e clienti cercano da smartphone; Google indicizza la versione mobile. (mobile-first)

Portfolio sviluppatore (target recruiter)
- Una pagina con URL proprio, descrittivo e stabile per ogni progetto (`/progetti/nome-progetto`), non un'unica SPA a schede o con modali/hash: ogni progetto diventa una pagina indicizzabile e condivisibile. (url-structure, javascript-seo-basics, lazy-loading)
- CV in PDF: è indicizzabile (fino a 64 MB per Googlebot); se lo si vuole nella Ricerca, collegarlo; se contiene dati personali (indirizzo, telefono) valutare versione pubblica ripulita, controllare metadati del PDF; per escluderlo usare `X-Robots-Tag: noindex` (non robots.txt). Per HTML e PDF con lo stesso contenuto si può indicare il canonical via header `Link`. (indexable-file-types, keep-redacted-information-out, robots-meta-tag, consolidate-duplicate-urls)
- Demo/progetti ospitati su sottodomini o servizi esterni (es. `demo.dominio.it`): ogni host ha il proprio robots.txt e il proprio budget; demo duplicate o ambienti di test vanno resi non indicizzabili se non devono comparire. (crawl-budget, robots-txt-spec, canonicalization)
- Video di presentazione/demo: eventuale Sitemap video o `player_loc` YouTube/Vimeo; la pagina deve riguardare quel video. (video-sitemaps)
- Se in futuro cambia dominio (es. da `nome.github.io` o `nome.vercel.app` a dominio proprio): redirect `301` 1:1, mantenere ≥ 1 anno, strumento Cambio di indirizzo (solo cambio dominio), aggiornare link su LinkedIn/GitHub/CV. Nota: su hosting dove non si controllano i redirect lato server, valutare prima. (site-move-with-url-changes, 301-redirects)

Orientatrice di carriera (locale + online)
- Pagine distinte per ciascun servizio (orientamento individuale, bilancio di competenze, consulenza online, ecc.) e per l'eventuale sede/zona, con URL in italiano descrittivi. (url-structure)
- Se si chiude temporaneamente (ferie, maternità): NON spegnere il sito né usare `noindex`/`404`/`503` prolungati; mostrare un banner con `data-nosnippet`, aggiornare orari nei dati strutturati `LocalBusiness`; `503` solo per 1–2 giorni. (pause-online-business)
- Prenotazioni/moduli: pagine "grazie" e aree riservate con `noindex`; i calendari di prenotazione con URL per data creano spazi infiniti → robots.txt o `nofollow` sui link a date future. (url-structure, reduce-crawl-rate)
- Eventuali articoli/blog: una normale Sitemap XML basta; la Sitemap News non è pertinente (solo editori). (news-sitemap)
- Se ha versioni in più lingue: canonical nella stessa lingua e `hreflang` reciproci. (consolidate-duplicate-urls, canonicalization)

## (e) Cose che una skill NON può fare (azioni manuali / off-site)

- Verificare la proprietà in Search Console, inviare la Sitemap dal report Sitemap, usare Controllo URL / "Richiedi indicizzazione" (quota, richiede accesso completo), leggere i report Indicizzazione delle pagine, Statistiche di scansione, Stato AMP, Problemi di sicurezza, Azioni manuali. La skill può solo preparare istruzioni, file di verifica/meta tag e checklist. (ask-google-to-recrawl, troubleshoot-crawling-errors)
- Richiedere "Rinnova scansione" del robots.txt nel report robots.txt (cache di 24 h altrimenti). (submit-updated-robots-txt)
- Strumento Rimozioni (temporaneo ~6 mesi), "Rimuovi contenuti obsoleti", strumento Cambio di indirizzo, file di disavow, richieste di riconsiderazione, richieste DMCA, modulo di riduzione frequenza Googlebot. (remove-information, site-move-with-url-changes, canonicalization-troubleshooting, reduce-crawl-rate)
- Garantire tempi o esito dell'indicizzazione: la Sitemap e le richieste sono suggerimenti; Google decide canonica e indicizzazione. (build-sitemap, canonicalization)
- Configurare DNS (TTL, record A/CNAME), certificati, firewall/WAF/CDN, server di hosting: la skill può suggerire configurazioni (`.htaccess`, NGINX, header) ma l'applicazione è a carico dell'utente/hosting, specie su hosting gestiti (Wix, Blogger) dove robots.txt non è modificabile. (dns-network-errors, site-move-no-url-changes, create-robots-txt)
- Verificare l'identità reale dei crawler nei log di produzione (DNS inverso) senza accesso ai log del server. (verify-google-requests)
- Aggiornare link esterni (LinkedIn, GitHub, profili, siti di terzi) dopo uno spostamento; aggiornare Profilo dell'attività Google e scheda informativa (Knowledge Panel). (site-move-with-url-changes, remove-information)
- Testare come Googlebot vede la pagina "dall'interno di Google": la skill può simulare con un browser headless e UA Googlebot, ma l'unico riscontro ufficiale è Controllo URL / Test dei risultati avanzati.
