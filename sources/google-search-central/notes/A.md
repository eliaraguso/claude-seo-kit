# Gruppo A — Fondamentali, Essentials, Monitoraggio/debug, Settori specialistici, Indice docs

Appunti fedeli alla documentazione Google Search Central (versione IT, letta il 2026-10-03). 43 pagine.

---

## Google Search Central — indice documentazione
Fonte: https://developers.google.com/search/docs?hl=it
- Pagina indice. Definisce SEO come "processo di ottimizzazione del sito per i motori di ricerca" (e anche la persona che lo fa di mestiere). Utile conoscere le basi anche per siti su piattaforme ospitate (Blogger, Wix, Squarespace) o piccole attività. Rimanda a: Guida introduttiva SEO, controllo scansione/indicizzazione, galleria elementi visivi, dati strutturati, SEO JavaScript, Search Console (avvio, debug cali traffico).

## Nozioni di base sulla Ricerca Google (Search Essentials)
Fonte: https://developers.google.com/search/docs/essentials?hl=it
- Tre blocchi: **requisiti tecnici** (minimo per comparire), **norme sullo spam** (comportamenti che portano a ranking inferiore o rimozione), **best practice chiave**.
- Comparire su Google è **gratuito**, "indipendentemente da quello che puoi sentir dire". Soddisfare requisiti e best practice **non garantisce** scansione, indicizzazione o pubblicazione.
- Best practice chiave:
  - Contenuti utili, affidabili, pensati per le persone.
  - Usare le parole che le persone userebbero per cercare e collocarle in posizioni in evidenza: **titolo**, **intestazione principale**, **testo alternativo**, **testo dei link**.
  - **Link sottoponibili a scansione** per far scoprire le altre pagine.
  - Far conoscere il sito partecipando alle community.
  - Seguire best practice specifiche per immagini, video, dati strutturati, JavaScript.
  - Abilitare funzionalità di aspetto pertinenti.
  - Usare il metodo appropriato per escludere contenuti o disattivare funzionalità.

## Requisiti tecnici per la Ricerca Google
Fonte: https://developers.google.com/search/docs/essentials/technical?hl=it
- Requisiti minimi (indicizzazione comunque **non garantita**):
  1. **Googlebot non bloccato** (pagina pubblica, niente login, nessun meccanismo di blocco).
  2. **La pagina funziona**: Google riceve **HTTP 200 (success)**. Pagine di errore client (4xx) e server (5xx) **non** sono indicizzate.
  3. **Contenuti indicizzabili**: testo in un tipo di file supportato e non in violazione delle norme sullo spam.
- Pagine bloccate da robots.txt difficilmente compaiono nei risultati, ma **l'URL può comunque comparire** anche se bloccato da robots.txt. Per non indicizzare: usare **`noindex` e consentire la scansione** dell'URL (se è bloccato da robots.txt Google non vede il noindex).
- Strumenti: report **Indicizzazione delle pagine** + report **Statistiche di scansione** (Search Console, esaminare entrambi); **Controllo URL** per testare una pagina e il suo codice di stato.

## Norme relative allo spam per la Ricerca Google
Fonte: https://developers.google.com/search/docs/essentials/spam-policies?hl=it
- Spam = tecniche per ingannare utenti o manipolare la Ricerca, **incluso manipolare le risposte dell'AI generativa** nella Ricerca. Rilevamento tramite sistemi automatici e, se necessario, revisione umana → **azione manuale**. Conseguenze: ranking più basso o rimozione. Google può agire anche su pratiche non elencate. Segnalazioni spam via modulo per utenti.
- **Cloaking**: contenuti diversi a utenti e motori (es. keyword inserite solo se lo user agent è un motore). Siti compromessi usano spesso cloaking. Paywall **non** è cloaking se Google vede tutto il contenuto protetto e si seguono le linee guida del Modello di accesso flessibile (flexible sampling). Per JS/immagini seguire le best practice di accessibilità senza cloaking.
- **Abuso di doorway**: più siti/domini con piccole variazioni di URL/home; **più pagine o domini mirati a regioni o città che rimandano a un'unica pagina**; pagine per incanalare visitatori; pagine sostanzialmente simili che somigliano più a risultati di ricerca che a una gerarchia consultabile.
- **Abuso di dominio scaduto**: acquistare un dominio scaduto per riusarlo a fini di ranking con contenuti di scarso valore (es. casinò su ex sito di scuola).
- **Contenuti compromessi**: iniezione di codice (JS dannoso, iframe), di pagine, di contenuti (testo/link nascosti via CSS/HTML), reindirizzamenti dannosi (anche condizionati da referrer, user agent, dispositivo — es. redirect solo arrivando dai risultati di Google).
- **Testo e link nascosti** (vietato): testo bianco su sfondo bianco, testo dietro immagine, CSS che posiziona testo fuori schermo, **opacità o font-size a 0**, link nascosto in un carattere piccolo (es. un trattino).
  - **Consentiti**: contenuti a schede/accordion, slideshow/carousel, tooltip, **testo solo per screen reader** destinato a migliorare l'esperienza.
- **Parole chiave in eccesso** (keyword stuffing): elenchi di numeri di telefono senza valore, **blocchi di testo che elencano città e regioni** per cui si vuole posizionare, ripetizioni innaturali.
- **Link di spam**: acquisto/vendita di link per ranking (denaro, beni, servizi, prodotti in cambio di recensione con link); scambi eccessivi di link / pagine partner solo per crosslinking; programmi automatici di link building; link imposti da ToS/contratti senza consentire di qualificarli; pubblicità testuali che passano ranking; advertorial/guest post/comunicati stampa con anchor text ottimizzato; **directory o social bookmarking di bassa qualità**; link in widget distribuiti; **link diffusi in footer o template di vari siti** (es. "sito realizzato da"); commenti in forum con link ottimizzati in firma; contenuti di scarso valore per manipolare link.
  - Link pubblicitari/sponsorizzati **sono ammessi** se marcati con `rel="nofollow"` o `rel="sponsored"` sul tag `<a>`.
- **Traffico generato automaticamente**: query automatizzate a Google, scraping dei risultati per controllo ranking senza autorizzazione → viola norme spam e Termini di servizio.
- **Pratiche dannose**: malware, software indesiderato (Unwanted Software Policy), **compromissione del pulsante Indietro** (manipolare la cronologia per impedire il ritorno alla pagina precedente).
- **Funzionalità ingannevoli**: falsi generatori, siti che promettono strumenti (es. unione PDF, timer, dizionario) e invece mandano ad annunci.
- **Abuso di contenuti su larga scala**: molte pagine per manipolare il ranking "indipendentemente da come sono state create": AI generativa senza valore aggiunto, scraping con sinonimi/traduzione/offuscamento, aggregazione senza valore, più siti per nascondere la scala, pagine senza senso piene di keyword. Se li ospiti, **escluderli dalla Ricerca**.
- **Scraping**: ripubblicare senza valore aggiunto né citazione; copiare con minime modifiche; riprodurre feed; siti di soli embed (video, immagini) senza valore.
- **Reputazione del sito** (site reputation abuse): contenuti di terze parti (utenti, freelance, white-label…) pubblicati su un host principalmente per sfruttarne gli indicatori di ranking. La sola presenza di contenuti di terze parti non viola. Non violano: agenzie stampa/comunicati, syndication di notizie, UGC/forum/commenti, rubriche ed editoriali, advertorial destinati ai lettori, link di affiliazione usati correttamente, unità pubblicitarie.
  - Fattori valutati in revisione umana: coerenza di presentazione (design, UX), qualità rispetto al dominio, paternità dichiarata/implicita, presenza identica su più siti. Nessuno da solo è necessario o sufficiente.
  - Google presume che le singole pagine (anche nuove) rispecchino la qualità complessiva del dominio.
  - **Differenza SEE (aggiornamento agosto 2026)**: fuori dal SEE → possibile azione manuale; **dentro il SEE** → le pagine possono essere classificate separatamente dal dominio principale senza azione manuale; azioni manuali precedenti nel SEE revocate. Azione fuori SEE non influisce sul ranking nel SEE; nessun obbligo di `noindex`. Nel SEE: nuova procedura di riconsiderazione con risposte rapide e mediazione (CEDR). Notifiche nel report Azioni manuali e nel Centro messaggi di Search Console.
  - Esempi: sezione coupon integrata con disclaimer → azione improbabile; articolo affiliato senza autore non integrato e copiato → azione probabile; freelance firmato con supervisione editoriale → azione improbabile.
- **Reindirizzamenti non ammessi**: mostrare ai motori un contenuto e reindirizzare gli utenti altrove; redirect solo per utenti mobile verso dominio spam. Legittimi: trasferimento sito, unione pagine, redirect post-login.
- **Affiliazione senza valore aggiunto**: descrizioni/recensioni copiate dal commerciante. Buona affiliazione: info prezzo, recensioni originali, test rigorosi, confronti.
- **Spam generato dagli utenti**: account spam su hosting, post in forum, commenti blog, file su file hosting.
- **Altre pratiche** che portano a retrocessione/rimozione: rimozioni legali (molte richieste DMCA valide → retrocessione di altri contenuti del sito; analogo per diffamazione, contraffazione, ordini di tribunale; CSAM sempre rimosso); siti con pratiche abusive di rimozione di informazioni personali (doxxing, immagini intime non consensuali); **circonvenzione** (usare sottodomini/sottodirectory/nuovi siti per continuare a violare → perdita di idoneità a funzionalità come Notizie principali, Discover/Feed personalizzato, rimozione di altre sezioni); **frodi** (impersonare attività, falsa assistenza clienti, dati di contatto falsi).

## Ottimizza il tuo sito per le funzionalità di AI generativa nella Ricerca Google
Fonte: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide?hl=it
- Le funzionalità di AI generativa (**AI Overview**, **AI Mode**) si basano sui sistemi principali di ranking e qualità: **la SEO resta pertinente**. Tecniche: **RAG** (grounding: recupero di pagine dall'indice, risposte con link cliccabili) e **query fan-out** (query correlate simultanee generate dal modello).
- "AEO" (answer engine optimization) e "GEO" (generative engine optimization): per Google **è sempre SEO**. Per consulenze AEO/GEO valutare con le indicazioni sui consulenti SEO di terze parti.
- Contenuti: punto di vista unico (es. recensione di prima mano > riassunto), contenuti **non generici** basati su esperienza diretta (es. "Perché abbiamo rinunciato all'ispezione…" vs "7 consigli…"), organizzazione in paragrafi/sezioni con intestazioni, immagini e video di alta qualità. **Non** creare pagine separate per ogni variante di query/fan-out per manipolare → viola "abuso di contenuti su larga scala". Contenuti generati con AI devono rispettare Essentials e norme spam. Principio guida: "I miei visitatori considererebbero soddisfacente questo contenuto?".
- Tecnico:
  - Per essere idonea alle funzionalità AI una pagina deve essere **indicizzata e idonea a comparire con uno snippet** (rispettare requisiti tecnici). Inoltre il sito deve essere **incluso nelle funzionalità di AI generativa della Ricerca in Search Console** (impostazione in Search Console). Nessuna garanzia.
  - Contenuti sottoponibili a scansione e pubblici; per siti molto grandi → crawl budget.
  - HTML semantico: utile (screen reader), ma "la leggibilità per le persone conta più di un codice perfetto"; Google comprende anche HTML non valido.
  - **JavaScript**: Google elabora contenuti JS se non bloccati, ma la SEO di siti con framework JS è "generalmente più complessa"; seguire le best practice SEO JS.
  - Esperienza sulla pagina positiva (tutti i dispositivi, latenza ridotta, contenuto principale distinguibile). Ridurre contenuti duplicati.
  - Verificare il sito in Search Console.
- Attività locali/e-commerce: le risposte AI possono includere schede prodotto e info su attività locali; usare **Merchant Center** (feed) e **Profilo dell'attività su Google**. Possibile "Agente virtuale" (esperienza conversazionale con il brand).
- **Miti da ignorare** per la Ricerca Google:
  - **llms.txt** e altri file/markup/Markdown "speciali" per l'AI: **non usati** dalla Ricerca Google; né positivi né negativi; ok crearli per altri servizi.
  - **Dividere i contenuti in blocchi (chunking)**: non necessario; **nessuna lunghezza ideale** di pagina.
  - Riscrivere per l'AI / inseguire varianti long-tail: non necessario (sinonimi compresi).
  - Cercare **menzioni non autentiche**: poco utile.
  - **Dati strutturati**: non necessari per l'AI generativa, nessun markup schema.org speciale; restano utili per i risultati avanzati.
- Misurazione: **report sul rendimento dell'AI generativa** in Search Console (anche Feed personalizzato). Diffidare di strumenti terzi che dichiarano metriche "interne" di Google: nessuno ha accesso.
- Esperienze agentiche: agenti del browser analizzano screenshot, DOM, **albero di accessibilità**; guida web.dev "siti ottimizzati per agenti"; protocollo emergente **Universal Commerce Protocol (UCP)**.

## Crea contenuti utili, affidabili e pensati per le persone
Fonte: https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=it
- Autovalutazione — contenuti e qualità: informazioni/ricerche/analisi originali; descrizione completa; analisi non scontata; valore aggiunto se si attinge ad altre fonti; **titolo/intestazione principale descrittivi e utili, senza toni scioccanti o esagerati**; pagina da salvare/condividere; citabile in rivista/enciclopedia; valore rispetto ad altri risultati; niente errori ortografici/stilistici; cura nella produzione; non prodotto in serie.
- Competenze: fonti chiare, prove di competenza, **informazioni sull'autore o sul sito (link a pagina autore o pagina "chi siamo")**; reputazione verificabile cercando il sito; scritto/recensito da esperto; niente errori oggettivi.
- Esperienza sulla pagina: valutare molti aspetti, non uno o due.
- Contenuti per le persone: pubblico esistente/previsto; **esperienza in prima persona**; scopo principale del sito chiaro; l'utente raggiunge il suo obiettivo; esperienza soddisfacente.
- Segnali di contenuti per motori di ricerca (da evitare): pensati per attirare traffico; molti argomenti diversi sperando che qualcosa funzioni; automazione su vasta scala; riassunti senza valore; temi di tendenza estranei al pubblico; lettore costretto a cercare altrove; **scrivere per un numero di parole (Google non ha preferenze di lunghezza)**; nicchie senza competenza; promettere risposte inesistenti; **cambiare la data delle pagine senza modifiche sostanziali**; aggiungere/rimuovere contenuti per sembrare "aggiornati" (il ranking non migliora).
- **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness): **l'affidabilità è la più importante**. Non è un fattore di ranking specifico, ma i sistemi danno più peso a contenuti con EEAT elevato su argomenti **YMYL** (salute, stabilità finanziaria, sicurezza, benessere della società). I valutatori della qualità non controllano il ranking; i loro dati non entrano direttamente negli algoritmi (feedback). Linee guida dei valutatori consultabili (PDF).
- "Chi, come, perché":
  - **Chi**: è evidente chi è l'autore? Riga con nome autore (byline) dove i lettori se l'aspettano? La byline porta a una pagina con dettagli sull'autore? Google "consiglia vivamente" info accurate sull'autore.
  - **Come**: spiegare il processo (es. recensioni: quanti prodotti testati, risultati, foto). Per contenuti automatici/AI: informativa sull'uso dell'automazione, dettagli su come e perché, quando i lettori se lo aspettano.
  - **Perché**: principalmente aiutare le persone. Automazione/AI per manipolare il ranking = violazione spam.

## Hai bisogno di un esperto SEO?
Fonte: https://developers.google.com/search/docs/fundamentals/do-i-need-seo?hl=it
- Servizi legittimi di un SEO: revisione contenuti/struttura, consigli tecnici (hosting, redirect, pagine di errore, JavaScript), sviluppo contenuti, campagne, ricerca keyword, formazione, competenza su mercati geografici, ottimizzazione per AI generativa.
- **La pubblicità con Google non influisce** sui risultati organici; Google non accetta denaro per inclusione/posizionamento; essere inclusi è gratuito.
- Una **piccola attività locale** può fare gran parte del lavoro da sola partendo dalla Guida introduttiva SEO.
- Momento migliore per coinvolgere un SEO: **redesign o lancio di un nuovo sito** ("prima lo fai, meglio è").
- Domande da porre: esempi di lavoro, rispetto delle Search Essentials (ex "Istruzioni per i webmaster"), risultati e tempi attesi, esperienza nel settore/paese/città/internazionale, comunicazione delle modifiche.
- Per un audit concedere **solo accesso in lettura** a Search Console. Diffidare di garanzie di prima posizione, "rapporto speciale" con Google, "inclusione prioritaria", strumenti che si dichiarano "approvati da Google", email non richieste, reticenza, schemi di link, invio a "migliaia di motori di ricerca". **Non inserire mai un link al sito del SEO.** Il proprietario è responsabile delle azioni dei fornitori; contenuti ingannevoli possono far rimuovere il sito dall'indice.
- Consulenze AEO/GEO: verificare coerenza con la guida ufficiale sull'AI generativa.
- Reclami: FTC (USA, 1-877-FTC-HELP), econsumer.gov (altri paesi).

## Guida introduttiva alla Ricerca: una guida per gli sviluppatori
Fonte: https://developers.google.com/search/docs/fundamentals/get-started-developers?hl=it
- Oltre alla SEO: sito sicuro, rapido, accessibile, funzionante su tutti i dispositivi (indicizzazione mobile-first).
- Vedere il sito come Google: **Controllo URL** e **Test dei risultati avanzati**. Google non sempre vede ciò che vede l'utente (es. immagini caricate con una funzionalità JS non supportata).
- Link: Googlebot segue link, Sitemap e redirect e tratta ogni URL "come se fosse il primo e unico". Usare **elementi `<a>` scansionabili**; ogni pagina raggiungibile da un link in un'altra pagina rilevabile; il link deve avere **testo** o, per immagini, **attributo ALT** pertinente alla destinazione. Creare e inviare una **Sitemap**. **Nelle app JavaScript con una sola pagina HTML (SPA), ogni schermata/contenuto deve avere un proprio URL.**
- JavaScript: Google lo esegue ma ci sono differenze e limitazioni; vedere "SEO JS di base" e "risolvere problemi JS".
- Contenuti cambiati: inviare Sitemap, chiedere nuova scansione; controllare i log del server se i problemi persistono.
- Parole nella pagina: Googlebot trova solo contenuti **testuali** (non il testo dentro i video). Esprimere i contenuti visivi anche in testo (es. immagini di prodotti con spiegazione testuale). Ogni pagina con **titolo descrittivo e meta description univoci**. Usare HTML semantico. **Non indicizzati**: contenuti che richiedono plug-in (Java, Silverlight) o **disegnati in un canvas**. Contenuti inseriti tramite **proprietà CSS `content` non fanno parte del DOM e sono ignorati** (ok per decorazioni).
- Altre versioni: consolidare URL duplicati, hreflang per versioni localizzate, AMP rilevabili. Google non scopre automaticamente le versioni alternative.
- Bloccare Google: login/password (impedisce di trovare); **robots.txt impedisce la scansione ma non è un meccanismo per escludere dall'indice**; `noindex` per non indicizzare consentendo la scansione. Regole combinate possono andare in conflitto.
- Se una pagina non compare: Controllo URL, test robots.txt, verificare `noindex` nei meta tag.
- Risultati avanzati tramite **dati strutturati**; consultare la galleria.

## Gestione della SEO per il tuo sito web (get started avanzato)
Fonte: https://developers.google.com/search/docs/fundamentals/get-started?hl=it
- Capire la pipeline scansione/indicizzazione/pubblicazione e le **pagine canoniche**.
- **Risorse** (immagini, CSS, JS) non bloccate da robots.txt e accessibili ad utenti anonimi; se risorse importanti sono bloccate, Google può non elaborare correttamente la pagina. Verificare con il rendering in Controllo URL (le risorse bloccate si vedono solo a livello di singolo URL).
- robots.txt per impedire la scansione (es. duplicati, risorse poco importanti come icone/loghi piccoli usati spesso), Sitemap per incoraggiarla; **non usare robots.txt per impedire l'indicizzazione** (usare `noindex` o login).
- Sitemap: Google dà **priorità** agli URL elencati (non si limita a quelli); importanti per contenuti che cambiano spesso, pagine poco linkate e contenuti non testuali.
- Siti multilingue/multiregionali: guide dedicate, **hreflang**, pagine adattive per impostazioni locali.
- Migrazione URL singolo: **301** se permanente, **302** se temporaneo. Pagina rimossa: 404 personalizzata ma con **vero codice 404, non soft 404**. Migrazione sito: 301 + Sitemap + comunicare lo spostamento a Google.
- Best practice: link scansionabili; **`rel=nofollow`** per link a pagamento, link che richiedono accesso, contenuti non attendibili (UGC); crawl budget rilevante solo per siti molto grandi (**centinaia di milioni di pagine** che cambiano periodicamente o **decine di milioni** che cambiano spesso): elencare le pagine importanti nelle Sitemap e nascondere le meno importanti con robots.txt; articoli multipagina con link precedente/successivo visibili e scansionabili; **scorrimento infinito**: fornire versione impaginata; bloccare con robots.txt URL che cambiano stato (commenti, creazione account, carrello); verificare tipi di file indicizzabili; ridurre frequenza di scansione solo in casi rari; **migrare a HTTPS**.
- Informazioni chiave **in testo, non in grafica**. Dati strutturati (manuali, Assistente per il markup WYSIWYG, **Evidenziatore di dati** — può smettere di funzionare se cambia il layout).
- Search Essentials: alcune regole sono consigli, altre **obbligatorie** (pena rimozione dall'indice).
- Linee guida per contenuti specifici: video, immagini (metadati licenza; impedire indicizzazione immagini con `Disallow` in robots.txt), **siti per bambini** (tag trattamento minori, COPPA), siti per adulti (SafeSearch), notizie (Publisher Center, Sitemap News, prevenzione abusi, flexible sampling, paywall con dati strutturati, meta tag per limitare snippet, AMP/Storie web), altri servizi Google, galleria funzionalità (ricette, eventi, offerte di lavoro…).
- Esperienza utente "fattore importante per il ranking": **HTTPS** (siti HTTP possono essere segnalati come non sicuri in Chrome); velocità — **report Core Web Vitals** (sito) e **PageSpeed Insights** (pagina), web.dev; mobile: oltre il 60% degli utenti internet naviga da mobile; Google usa il **crawler mobile come predefinito**.
- Aspetto: funzionalità dei risultati, **favicon**, **data di pubblicazione**, link del titolo, snippet (limitabili/omettibili con meta tag).

## Guida approfondita sul funzionamento della Ricerca Google
Fonte: https://developers.google.com/search/docs/fundamentals/how-search-works?hl=it
- Motore completamente automatizzato; la maggior parte delle pagine è trovata dai crawler, non inviata. Google **non accetta pagamenti** per scansionare più spesso o migliorare il ranking; **nessuna garanzia** di scansione/indicizzazione/pubblicazione.
- Tre fasi: **scansione → indicizzazione → pubblicazione**; non tutte le pagine le superano.
- Scansione: "individuazione URL" tramite pagine già note, link da pagine note (es. hub/categoria), Sitemap. Googlebot decide algoritmicamente cosa, quanto spesso, quante pagine; evita di sovraccaricare (es. **HTTP 500 = rallenta**). Non scansiona pagine bloccate da robots.txt o dietro login. **Rendering con una versione recente di Chrome**, esegue JavaScript (senza rendering Google potrebbe non vedere i contenuti). Problemi comuni: server, rete, robots.txt.
- Indicizzazione: analizza testo, `<title>`, attributi ALT, immagini, video. **Canonicalizzazione**: clustering di pagine simili e scelta della più rappresentativa; le altre sono alternative servite in contesti diversi (es. mobile). Indicatori raccolti: lingua, paese, usabilità. Indicizzazione non garantita. Problemi: bassa qualità, meta robots che non consentono l'indicizzazione, design del sito che rende difficile l'indicizzazione (link a SEO JS).
- Pubblicazione: pertinenza con centinaia di fattori (posizione, lingua, dispositivo dell'utente); es. "officine riparazione biciclette" → risultati diversi a Parigi e Hong Kong; query locali mostrano risultati locali. Pagina indicizzata ma non visibile: contenuti non pertinenti, bassa qualità, meta robots che impediscono la pubblicazione.

## Guida introduttiva alla SEO (SEO Starter Guide)
Fonte: https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=it
- Non ci sono segreti per la prima posizione. Tempi: alcune modifiche in **poche ore**, altre in **diversi mesi**; attendere **alcune settimane** per valutare.
- Verificare se il sito è indicizzato con l'operatore **`site:`**. Google trova pagine soprattutto tramite link; promuovere il sito. **Sitemap non obbligatoria** (alcuni CMS la generano).
- Google deve vedere la pagina come un utente medio: **non nascondere/bloccare CSS e JavaScript**. Se i contenuti variano per posizione dell'utente, Google vede quelli della posizione del crawler, **in genere Stati Uniti**. Verifica con Controllo URL.
- Organizzazione:
  - **URL descrittivi** con parole utili (es. `/pets/cats.html`), non identificatori casuali; parti dell'URL appaiono come **breadcrumb** (influenzabili con dati strutturati Breadcrumb).
  - Raggruppare argomenti in **directory** (rilevante oltre **qualche migliaio di URL**: Google apprende la frequenza di modifica per directory).
  - **Contenuti duplicati**: non violano le norme spam ma sprecano scansione e confondono; ogni contenuto accessibile da **un solo URL**; preferire **redirect** dagli URL non preferiti, altrimenti `link rel="canonical"`; Google canonicalizza comunque in automatico.
- Contenuti: leggibili e ben organizzati (paragrafi, sezioni, intestazioni), senza errori; **unici**; **aggiornati** (aggiornare o eliminare se non più rilevanti); utili e affidabili (fonti esperte). Pensare ai termini usati dai lettori (esperti vs neofiti), ma non serve prevedere ogni variante.
- Evitare pubblicità che distraggono e **interstitial** che rendono difficile l'uso.
- Link: interni ed esterni a risorse pertinenti; **anchor text** descrittivo; per risorse non attendibili usare `nofollow` o simile; **link UGC con `nofollow` automatico** dal CMS.
- Aspetto in SERP:
  - **Link del titolo**: generato da `<title>` e altre intestazioni; titolo **unico, chiaro, conciso, accurato**; può includere **nome del sito/attività, sede fisica**, dettagli dell'offerta della pagina.
  - **Snippet**: estratto dai contenuti della pagina, a volte dalla **meta description** (breve, una-due frasi, unica per pagina, con i punti più significativi).
- Immagini: alta qualità, nitide, **vicino al testo pertinente**; **testo alternativo descrittivo** (`alt` su `img`).
- Video: pagina autonoma per il video con testo pertinente; titolo e descrizione descrittivi.
- Promozione: social, community, pubblicità online/offline, passaparola; **URL su biglietti da visita, carta intestata, manifesti**; newsletter con autorizzazione. Eccessi possono essere visti come manipolazione.
- **Miti / cose su cui non soffermarsi**:
  - **Meta tag keywords: non usato** da Google.
  - Keyword stuffing: violazione spam.
  - **Keyword nel dominio o nel percorso URL: effetto quasi nullo** sul ranking (solo breadcrumb). **TLD** conta solo per target paese ed è indicatore a basso impatto (es. `.ch` per la Svizzera); altrimenti indifferente (.com, .org, .asia…).
  - **Nessuna lunghezza minima/massima** di contenuto ("meglio almeno una parola").
  - Sottodomini vs sottodirectory: scegliere ciò che è meglio per il business.
  - **PageRank** è solo uno dei molti indicatori.
  - **Nessuna "penalità" per contenuti duplicati** interni (non causa azione manuale); copiare da altri siti è diverso.
  - **Numero e ordine delle intestazioni non importano** per Google (sì per screen reader); nessun numero ideale ("se ritieni che ci siano troppi link, probabilmente è così").
  - **EEAT non è un fattore di ranking.**
- Prossimi passi: Search Console, gestione nel tempo, dati strutturati (stelle recensioni, caroselli).

## Indicazioni su strumenti, servizi e consulenze SEO di terze parti
Fonte: https://developers.google.com/search/docs/fundamentals/third-party-seo?hl=it
- Valutare consigli di terzi (inclusi AEO/GEO) rispetto alla documentazione ufficiale; i consigli validi dichiarano di essere opinioni basate su dati o citano fonti ufficiali.
- Strumenti terzi (Sitemap, direttive di indicizzazione, contenuti "ottimizzati SEO", consigli di ranking, AEO/GEO): **Google non valuta né approva** servizi terzi; nessun accesso a dati di ranking interni; nessuna garanzia; previsioni personali. Usare comunque **Google Search Console** (consigliato vivamente).

## Indicazioni sull'utilizzo di contenuti creati con l'AI generativa
Fonte: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content?hl=it
- AI utile per ricerca e strutturare contenuti originali; generare molte pagine senza valore può violare "abuso di contenuti su larga scala". Rispettare Essentials e norme spam.
- Linee guida valutatori: sezioni **4.6.5** (abuso su larga scala) e **4.6.6** (contenuti con poco impegno/originalità/valore); le valutazioni non influiscono direttamente sul ranking.
- Accuratezza, qualità e pertinenza anche nei **metadati**: `<title>`, meta description, dati strutturati, alt text. Dati strutturati: rispettare linee guida generali e specifiche e **convalidare** il markup.
- Dare contesto: spiegare come sono stati creati i contenuti; metadati immagini.
- E-commerce (Merchant Center): immagini AI con metadati IPTC **`DigitalSourceType` = `TrainedAlgorithmicMedia`**; titoli/descrizioni prodotto generati con AI specificati a parte ed etichettati come AI.

---

# Monitoraggio e debug

## Analizza il rendimento dei contenuti sulle piattaforme social e video in Search Console
Fonte: https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content?hl=it
- I contenuti su **TikTok, Instagram, X, YouTube** possono essere trovati nella Ricerca Google. Search Console offre **proprietà della piattaforma** (account social) da aggiungere e verificare singolarmente; se hai **rivendicato il tuo profilo della Ricerca**, gli account verificati vengono aggiunti automaticamente come proprietà.
- Report **Approfondimenti**: clic ultimi **28 giorni** e distribuzione tra le superfici di Google; contenuti con miglior rendimento; query ("termini di ricerca") che portano al canale/profilo; paesi del pubblico. Dati su Ricerca, Feed personalizzato (Discover) e Google News.
- Report sul rendimento: filtri per paese, date, query, dispositivo; **gruppi di query** (in aumento/calo); **filtro 24 ore** per contenuti di tendenza; filtri per pagina (es. `playlist`); modalità confronto (YouTube `/watch` vs `/shorts/`; Instagram `/p/` vs `/reels/`); esportazione dati; **annotazioni** in Search Console per segnare la data di modifica di titoli/didascalie.
- Usare insight per riadattare didascalie, hashtag, nuove versioni video, promozione incrociata; abbinare a Google Trends.

## Migliorare la SEO con un grafico a bolle di Search Console
Fonte: https://developers.google.com/search/docs/monitor-debug/bubble-chart-analysis?hl=it
- Tecnica di analisi in **Looker Studio** (origine dati Search Console, tabella "Impressioni sito", aggregata per sito e query). Controlli: proprietà, intervallo date (default **28 giorni**), query (anche regex), paese, dispositivo.
- Assi: Y = posizione media (**invertito**, 1 in alto), X = CTR; **scala logaritmica** su entrambi; **linee di riferimento** (media/mediana/percentile) creano 4 quadranti. Bolla = query; dimensione = clic; colore = dispositivo.
- Quadranti: posizione alta + CTR alto → nulla da fare; **posizione bassa + CTR alto** → priorità SEO (creare pagina dedicata o arricchire quella esistente); CTR basso → distinguere query correlate (priorità) da non correlate; posizione alta + CTR basso → concorrenti con **risultati avanzati/dati strutturati**, query non desiderate, oppure l'utente trova già la risposta in SERP (orari, indirizzo, telefono) — comportamento atteso se l'obiettivo è portarli in negozio, altrimenti ottimizzare titolo e descrizione.
- Ottimizzazione per query: `title`, meta description e **ALT descrittivi, specifici e precisi**; intestazioni per struttura gerarchica; sinonimi e query correlate; **Strumento di pianificazione delle parole chiave** (Google Ads) per varianti e volumi; Google Trends.

## Eseguire il debug di cali del traffico nella Ricerca Google
Fonte: https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops?hl=it
- Strumenti: **report sul rendimento** di Search Console + **Google Trends**; controllare la pagina **Anomalie dei dati** di Search Console (errori di logging).
- Cause principali e forma del grafico: calo significativo (aggiornamento algoritmico, problemi di sicurezza, spam a livello di sito); stagionalità; problema tecnico/interessi mutevoli; segnalazione/anomalia.
  - **Aggiornamenti algoritmici** (core update): consultare la pagina con l'elenco degli aggiornamenti di ranking (Search Status Dashboard). Calo piccolo (es. **posizione 2 → 4**): fluttuazione normale, **evitare modifiche radicali**. Calo significativo (es. **dai primi 10 a 29**): valutare **l'intero sito** (utile, affidabile, per le persone); effetti in giorni o **parecchi mesi**; ricontrollare dopo **alcune settimane**; nessuna garanzia.
  - **Problemi tecnici**: server, recupero robots.txt, 404, `noindex` errato (calo più lento perché dipende dalla riscansione) → report **Statistiche di scansione** e **Indicizzazione delle pagine**.
  - **Sicurezza** (malware, phishing → avvisi/interstitial) → report **Problemi di sicurezza**.
  - **Spam** → norme spam e report **Azioni manuali**.
  - **Stagionalità/interessi** → filtrare una query alla volta e confrontare su Google Trends.
  - **Migrazioni**: fluttuazioni; sito medio richiede **alcune settimane**, più grandi di più.
- Pattern: impressioni e clic giù → cause sopra; **impressioni stabili ma clic giù** → titolo/snippet poco efficaci o concorrenti con risultati avanzati.
- Analisi: intervallo **16 mesi** (oltre: API Search Analytics o esportazione collettiva in BigQuery); confronto ultimi 3 mesi vs periodo precedente o anno precedente; esaminare schede query/pagine/paesi/dispositivi/aspetto; filtro **Tipo di ricerca** (Web, Immagini, Video, Notizie); posizione media (non ossessionarsi sull'assoluto); tabella Pagine ordinata per **Differenza di clic**; problema a livello di sito → report Indicizzazione; gruppo di pagine → Controllo URL.
- Google Trends: campione in gran parte non filtrato, anonimizzato, aggregato; interesse a livello mondiale fino a città. Confrontare le query principali della propria regione con quelle che portano traffico; cercare query correlate in crescita.

## Utilizza i dati di Search Console e Google Analytics per la SEO
Fonte: https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console?hl=it
- **Search Console** = cosa succede **prima** che l'utente arrivi (impressioni, clic, query); **Google Analytics** = comportamento **sul sito** (pagine, durata, azioni, canali). Fonte di verità: SC per il rendimento nella Ricerca, GA per il comportamento sul sito.
- Metriche più confrontabili: **clic** (SC) vs **sessioni** (GA); non coincideranno.
- Dashboard **Looker Studio** (modello ufficiale): SC tabella "Impressione URL"; GA filtrata `Session source = google` e `Session medium = organic`. Intervallo default **28 giorni**; dati SC ritardati di **un paio di giorni**. Unione avanzata via BigQuery (esportazioni collettive SC + export GA) o combinazione Looker Studio.
- Metriche: Sessioni; **Tasso di coinvolgimento** (sessione con evento chiave, **durata > 10 secondi**, o **≥ 2 visualizzazioni di pagina**); Utenti di ritorno; Clic; CTR (clic/impressioni). Nessuna percentuale "giusta" di traffico organico.
- Report GA utili: **Acquisizione traffico**, **Pagina di destinazione** filtrata su organico Google.
- Discrepanze (lievi = ignorabili): implementazione tag GA mancante su alcune pagine; **consenso cookie** rifiutato; **fuso orario** (SC fisso su **Pacific Time**); attribuzione (3 modelli GA, il predefinito è il più simile); SC riporta solo l'**URL canonico**; suddivisioni del traffico (web, immagini, video, notizie, Feed personalizzato); **pagine non HTML** (PDF) contate da SC ma non da GA (attivare misurazione avanzata); **traffico bot** escluso da GA, non necessariamente da SC.
- Risorse: collegare SC a GA; **Site Kit** per WordPress; BigQuery.

## Prevenire lo spam generato dagli utenti sul tuo sito e sulla tua piattaforma
Fonte: https://developers.google.com/search/docs/monitor-debug/prevent-abuse?hl=it
- Pubblicare norme chiare contro lo spam; permettere agli utenti attendibili di segnalare.
- Identificare account spam: tempo di compilazione moduli, richieste dallo stesso intervallo IP, user agent, nomi utente. Sistema di reputazione: **`noindex` sui post dei nuovi utenti** finché non hanno reputazione.
- **`rel="nofollow"` o `rel="ugc"`** su tutti i link nei contenuti non attendibili.
- Moderazione manuale (integrata nella maggior parte dei CMS); liste bloccate di IP (es. **Akismet** per WordPress, firewall); **reCAPTCHA** o simili nei moduli di registrazione.
- Monitoraggio: redirect, eccesso di annunci, keyword spam, JS codificato; operatore `site:` e **Google Alert**; log del server per picchi; **API Navigazione sicura** per testare URL; anomalie geografiche/linguistiche (librerie di rilevamento lingua, API Translate).

## Iniziare a usare Search Console
Fonte: https://developers.google.com/search/docs/monitor-debug/search-console-start?hl=it
- Non serve accedere ogni giorno: nuovi problemi arrivano via **email**; controllare **circa una volta al mese** o dopo modifiche al sito.
- Passi: **verificare la proprietà**; report **Copertura dell'indice / Indicizzazione pagine** (correggere errori e avvisi); valutare l'invio di una **Sitemap** (non obbligatoria, può velocizzare il rilevamento; report Sitemap); monitorare il **report sul rendimento** (query, pagine, paesi; impressioni, clic).
- Per SEO/marketing: **Azioni manuali**; **strumento Rimozioni** (nasconde temporaneamente, durata **circa 6 mesi**); **Cambio di indirizzo** (migrazione dominio/sottodominio); **report sullo stato dei risultati avanzati** (dati strutturati: errori e avvisi).
- Per sviluppatori: Copertura indice (errori, avvisi, esclusioni + impressioni); **Controllo URL** (stato indicizzazione, test URL live, richiesta scansione, risorse caricate); **Problemi di sicurezza**; **Core Web Vitals** (dati reali/sul campo).

## Panoramica degli operatori di ricerca di Google
Fonte: https://developers.google.com/search/docs/monitor-debug/search-operators?hl=it
- Gli operatori sono vincolati da limiti di indicizzazione e recupero: **Controllo URL è più affidabile** per il debug.
- `filetype:` (per `content-type` o estensione, es. `filetype:rtf galway`); `imagesize:` (solo Google Immagini, es. `imagesize:1200x800`); `site:` (dominio, URL o prefisso); `src:` (pagine che referenziano un URL immagine nell'attributo `src`, solo Google Immagini).

## Operatore di ricerca `site:`
Fonte: https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site?hl=it
- `site:example.com` include sottodomini (www, recipes…). `site:https://www.example.com/ramen tsukemen` filtra per prefisso + termine. Disponibile in tutte le proprietà della Ricerca.
- Un URL indicizzato **non è garantito** che compaia nella query `site:`; in caso di assenza usare Controllo URL. Attenzione: `site:https://www.example.com` ≠ `site:https://example.com/`.
- Usi: elenco URL indicizzati (non esaustivo; prefissi più specifici possono restituire più risultati); verificare un URL specifico; monitorare spam (`site:example.com viagra casino`); URL per un termine.
- Limiti: **non restituisce tutti gli URL indicizzati** (inadatto a contare le pagine indicizzate); senza query i risultati **non sono classificati** (in genere l'URL più breve in alto, poi ordine quasi casuale).

## Operatori di ricerca di Google Immagini
Fonte: https://developers.google.com/search/docs/monitor-debug/search-operators/image-search?hl=it
- Solo su Google Immagini. `src:URL` trova pagine (di qualsiasi dominio) che usano l'immagine → utile per scoprire **hotlink**. `imagesize:LARGHEZZAxALTEZZA`, combinabile con `src:` e `site:`. Risultati non completi per limiti di indicizzazione.

## Prevenire e monitorare gli abusi sul tuo sito (indice sicurezza)
Fonte: https://developers.google.com/search/docs/monitor-debug/security?hl=it
- Pagina indice: spam UGC, malware e software indesiderato, prevenzione malware, ingegneria sociale, Navigazione sicura per trasgressori recidivi.

## Malware e software indesiderato
Fonte: https://developers.google.com/search/docs/monitor-debug/security/malware?hl=it
- Google controlla se i siti ospitano binari/eseguibili dannosi; lista di file sospetti nel report **Problemi di sicurezza**. Nel report "Malware" = malware web senza intervento dell'utente; "Download dannosi" = da scaricare attivamente.
- Risoluzione: conformarsi alle linee guida e **richiedere una verifica** nel report Problemi di sicurezza (app mobile: ricorso Google Play).
- Linee guida (Unwanted Software Policy): niente dichiarazioni errate (annunci "Scarica"/"Riproduci" generici, pulsanti che avviano download, finti contenuti); comportamento coerente con quanto pubblicizzato; spiegare modifiche a browser/sistema; usare loghi solo con autorizzazione; non spaventare l'utente. Software: usare API Chrome Settings Override, non sopprimere avvisi, firma del codice consigliata, non indebolire TLS/SSL, proteggere/criptare i dati, non alterare il ripristino del browser, usare estensioni (no DLL, proxy, LSP), disinstallazione semplice e completa, responsabilità per i componenti integrati. Estensioni Chrome: ospitate nel Chrome Web Store, flusso di installazione autorizzato. App mobile: consenso alla raccolta dati, HTTPS, non impersonare brand, contenuti nel contesto dell'app, mantenere promesse, trasparenza.

## Come prevenire le infezioni causate da malware
Fonte: https://developers.google.com/search/docs/monitor-debug/security/prevent-malware?hl=it
- Monitoraggio: ricerche periodiche **`site:`** per scoprire pagine/contenuti non creati da te; report **Problemi di sicurezza**; notifiche nel riquadro messaggi di Search Console, **inoltrabili via email**.
- Proprietario: password sicure; fornitori terzi (app, annunci) attendibili; supporto dell'hosting; computer aggiornati con antivirus.
- Con accesso al server: configurazione sicura (Apache, IIS); backup di `.htaccess`; **aggiornamenti e patch** di CMS/plugin (errore comune: blog o forum dimenticati); inventario software e versioni; **log** (parametri sospetti come `=http:` o `=//` → **open redirect**); directory senza permessi aperti; verifiche **XSS** e **SQL injection**; **SSH/SFTP** invece di Telnet/FTP; Google Security Blog, US-CERT.

## Norme di Google Navigazione sicura relative alle trasgressioni ripetute
Fonte: https://developers.google.com/search/docs/monitor-debug/security/safe-browsing-repeat-offenders?hl=it
- Siti che alternano spesso conformità e non conformità in breve tempo → **trasgressori recidivi**; notifica all'email registrata in Search Console; per **30 giorni** non si possono richiedere verifiche.

## Ingegneria sociale (siti di phishing e ingannevoli)
Fonte: https://developers.google.com/search/docs/monitor-debug/security/social-engineering?hl=it
- Contenuti che inducono a azioni pericolose → avviso Chrome **"Sito ingannevole in vista"**. Tipi: phishing, contenuti ingannevoli (falsi avvisi di aggiornamento), **servizi di terze parti etichettati in modo insufficiente** (chi gestisce un sito per conto di altri deve dichiararlo).
- Anche contenuti **incorporati** (annunci, popup, pop-under, redirect) violano le norme per la pagina host.
- Risoluzione: verificare proprietà in Search Console e assenza di **proprietari sospetti aggiunti**; report Problemi di sicurezza (visitare gli URL d'esempio da una rete esterna, gli hacker possono nascondersi al proprietario); rimuovere contenuti; controllare risorse terze (le reti pubblicitarie ruotano gli annunci; annunci diversi mobile/desktop → Controllo URL); richiedere controllo (**diversi giorni**). Errori di classificazione segnalabili.
- Linee guida servizi terzi: brand della terza parte su ogni pagina; dichiarare il rapporto con link informativo (es. "Questo servizio è ospitato da … per conto di …"); per l'autenticazione usare standard come **OAuth**.

## Guida introduttiva a Google Trends
Fonte: https://developers.google.com/search/docs/monitor-debug/trends-start?hl=it
- Campione casuale aggregato e anonimizzato di ricerche su Google e YouTube; interesse da mondiale a città. Non scrivere su un argomento solo perché è di tendenza.
- Strumenti: **Esplora** (termini/argomenti, interesse regionale, correlati) e **Di tendenza ora** (tendenze attuali con volume approssimativo e notizie).
- Tendenze generali (Esplora con casella vuota + filtri; Di tendenza ora) e specifiche (lista di termini propri). Gli **argomenti** aggregano lingue, errori ortografici, varianti, acronimi.
- Ricerca keyword: fino a **5 termini** in Esplora; schede **Argomenti correlati / Query correlate** ("Più cercate", "In aumento"); valutare altre lingue (verificare anche in Search Console); idee dalle query del report sul rendimento. Concentrarsi su termini legati alla propria attività ed esperienza.
- Calendario contenuti: pubblicare **prima** dei picchi stagionali; analizzare i paesi separatamente (es. brie: due picchi l'anno in USA, uno in UK).
- Benchmark di settore (distinguere cali del sito da cali del settore; categorie; nomi dei concorrenti; sottoregioni/aree metropolitane/città).
- Notorietà del brand e sentiment: inserire il nome dell'attività, intervallo **30 o 90 giorni**, termini "In aumento"/"Più cercate"; scaricare periodicamente; per grandi volumi Natural Language AI.

---

# Settori specialistici — E-commerce

## Best practice per siti di e-commerce nella Ricerca Google (indice)
Fonte: https://developers.google.com/search/docs/specialty/ecommerce?hl=it
- Indice della serie e-commerce per sviluppatori (valida in parte anche per siti che elencano prodotti di soli negozi fisici): dove compaiono i dati, condivisione dati prodotto, dati strutturati, lancio, recensioni, struttura URL, struttura del sito, impaginazione.

## Progettare la struttura di un URL per i siti web di e-commerce
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites?hl=it
- (Se usi una piattaforma e-commerce probabilmente puoi saltare.) Problemi di URL scadenti: pagine non rilevate perché **i frammenti `#` sono ignorati** (`/product/t-shirt#black` = `#white` = stessa pagina); stessi contenuti recuperati più volte (`/product/black-t-shirt` vs `?sku=1234`); **spazi infiniti** con valori variabili (timestamp `?now=12:34am`).
- Regole: minimizzare URL alternativi per lo stesso contenuto; **uniformare maiuscole/minuscole** se il server le tratta allo stesso modo; URL univoco per ogni pagina impaginata; **parole descrittive nel percorso** (`/product/black-t-shirt-with-a-white-collar` sì, `/product/3243` no).
- Parametri: formato **`?key=value`** (non `?value`); non ripetere lo stesso parametro (`?type=candy,sweet` sì, `?type=candy&type=sweet` no); **niente link interni a parametri temporanei** (ID sessione, tracking, `location=nearby`, ora corrente).
- Varianti prodotto: URL distinto per variante (segmento di percorso `/t-shirt/green` o parametro `?color=green`); con parametri facoltativi, canonico = URL senza parametro.
- Uso degli URL: **stesso URL** in link interni, Sitemap e `rel="canonical"` (es. `?page=1` coerente); **canonical autoreferenziale su tutte le pagine indicizzabili** e incluse nella Sitemap; varianti con canonical al prodotto (Merchant Center `canonical_link`); **link con `<a href>`, non navigazione via JavaScript** (Googlebot potrebbe non rilevarla); anchor text significativo, **non "fai clic qui"**; categorie vuote → `noindex` o **404** se rimosse dalla navigazione.

## Aiutare Google a comprendere la struttura del tuo sito web di e-commerce
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure?hl=it
- Google deduce l'importanza relativa di una pagina da **numero di link necessari per raggiungerla (profondità)** e **numero di link che la puntano**. Google **in genere non esamina la struttura degli URL** per capire la struttura del sito, ma i collegamenti tra pagine.
- Navigazione: menu → categorie → sottocategorie → prodotti; **Googlebot in genere non usa le caselle di ricerca** interne; creare link a tutto ciò che va indicizzato, altrimenti Sitemap o feed Merchant Center. Usare `<a href>`, **non eventi JavaScript su altri elementi DOM**.
- Promuovere pagine importanti con link da home page, blog, newsletter. Vedere anche gestione della navigazione per facet.

## Come lanciare un nuovo sito web di e-commerce
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website?hl=it
- Passi: verificare la proprietà; chiedere l'indicizzazione (**pochi URL → Controllo URL; molti → Sitemap**); monitorare con report Indicizzazione delle pagine; se c'è un negozio fisico, fornire i dettagli dell'attività; registrarsi a Merchant Center (obbligatorio per la scheda Shopping, utile per badge prodotto in Google Immagini).
- Strategie di lancio:
  - **Grande inaugurazione** (sito protetto da password prima del lancio, poi pubblicazione): niente fughe, ma visibilità più lenta.
  - **Lancio della sola home page** (segnaposto "presto disponibile" con descrizione): permette di verificare la proprietà in anticipo, far conoscere il nome e ricevere link; dettagli non visibili finché non si lancia tutto.
  - **Lancio senza prodotti disponibili**: tutto indicizzato subito; **non disattivare l'aggiunta al carrello** (Google la usa per verificare prezzo finale, imposte, spedizione); usare `excluded_destination` in Merchant Center; comunicare la data di lancio.
  - **Lancio sperimentale** (soft launch): semplice, test con traffico reale; rischio di menzioni anticipate sui social.

## Includere dati strutturati pertinenti all'e-commerce
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce?hl=it
- Google supporta molti ma **non tutti** i tipi schema.org. CMS: usare plugin/estensioni.
- Tipi rilevanti: **`BreadcrumbList`** (gerarchia, breadcrumb in SERP); **`LocalBusiness`** (sede, orari; registrarsi a Google My Business/Profilo dell'attività; codici negozio per Merchant Center); **`Organization`** (logo, contatti, identificatori aziendali, norme sui resi); **`Product`/`ProductGroup`** (varianti); **`Review`** (snippet recensione); **`VideoObject`** (video preregistrati o live).

## Impaginazione, caricamento incrementale delle pagine e relativo impatto sulla Ricerca Google
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading?hl=it
- Modelli UX: **impaginazione**, **"Carica altro"**, **scorrimento continuo** (pro e contro: la paginazione dà orientamento; "carica altro" e scroll infinito non gestiscono numeri molto elevati di risultati).
- **Googlebot scansiona gli URL negli `href` degli `<a>`; non "fa clic" sui pulsanti e in genere non attiva funzioni JS che richiedono azioni dell'utente.** Usare Sitemap o feed Merchant Center come supporto.
- Best practice impaginazione: link sequenziali `<a href>` alla pagina successiva; valutare link di ogni pagina alla **prima pagina**; titoli/descrizioni possono essere uguali nella sequenza (eccezione alla regola dei titoli distinti); **URL univoco** per pagina (es. `?page=n`); **non usare la prima pagina come canonical** di tutte (ogni pagina canonical a sé); **non usare frammenti `#`** per i numeri di pagina; resource hints (preload, preconnect, prefetch).
- **`rel="next"`/`rel="prev"` non sono più usati da Google** (forse da altri motori).
- Filtri/ordinamenti alternativi (`?order=price`): `noindex` o blocco via robots.txt dei pattern.

## Condividere i dati di prodotto con Google
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google?hl=it
- Due canali: **dati strutturati** nelle pagine (non obbligatori ma migliorano idoneità ai risultati avanzati e precisione su prezzi/sconti/spedizioni) e **feed Merchant Center** (non obbligatorio per la Ricerca, **obbligatorio per la scheda Shopping**).
- `data-nosnippet` su un elemento HTML per escluderlo dagli snippet.
- Siti piccoli/poco aggiornati: **feed automatico** dai contenuti scansionati; siti grandi: feed periodici; aggiornamenti immediati: **Content API**. Vantaggi feed: completezza, controllo sui tempi (settimanale, giornaliero, orario), dati non presenti sul sito (inventario negozio).
- Tabella usi: risultati avanzati prodotti (SD o MC), annotazioni prodotto in Google Immagini, scheda Shopping (MC necessario), Google Lens (proprietà immagine nei dati strutturati, immagini MC). Varia per paese/dispositivo.
- Ritardi di sincronizzazione prezzo/disponibilità: attivare gli **aggiornamenti automatici degli articoli** in Merchant Center.

## Dove possono essere visualizzati i contenuti di e-commerce su Google
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google?hl=it
- Piattaforme: Ricerca Google, Google Immagini, Google Lens (Merchant Center + schede di prodotto), scheda Shopping (Merchant Center), **Profilo dell'attività** (rivendicarlo e collegarlo a Merchant Center), Google Maps (inventario locale).
- Contenuti utili oltre ai prodotti: storia dell'azienda, offerte stagionali, recensioni del commerciante (link a pagamento → linee guida), recensioni dei clienti, descrizioni di catalogo e di categoria, **opportunità di formazione (workshop/lezioni → dati strutturati Event)**, live streaming, **touchpoint di assistenza clienti** (resi, spedizioni, contatti in evidenza).

## Scrivere recensioni di alta qualità
Fonte: https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews?hl=it
- Valide per prodotti, servizi, destinazioni, giochi, film. Best practice: punto di vista dell'utente; dimostrare competenza; **prove** (immagini, audio, link) dell'esperienza diretta; misure quantitative; differenze dalla concorrenza; alternative per usi specifici; pro e contro da ricerca personale; evoluzione rispetto a modelli precedenti; fattori decisionali chiave; scelte progettuali oltre al produttore; link a risorse utili; link a più venditori; motivare i "migliore per…" con prove; elenchi di ranking autosufficienti.
- Link di affiliazione: vedere posizione Google sui programmi di affiliazione. **Qualità e originalità, non lunghezza.**

---

# Settori specialistici — Contenuti espliciti

## Linee guida per i siti con contenuti espliciti
Fonte: https://developers.google.com/search/docs/specialty/explicit/guidelines?hl=it
- **SafeSearch** filtra: contenuti sessuali espliciti, nudità, sex toy fotorealistici, escort/incontri sessuali, violenza/sangue, link a pagine esplicite; ammette contenuti con valore educativo, documentaristico, scientifico o artistico (EDSA). Basato su ML e indicatori (testo, immagini, video, link). Anche con SafeSearch disattivato, i sistemi limitano l'esposizione involontaria. Rimozione sempre per CSAM e su richiesta per immagini intime non consensuali/deepfake; retrocessione di siti con molte rimozioni valide.
- Best practice: moderazione/verifica publisher per UGC (hash matching e classificatori per CSAM); **consentire a Googlebot di recuperare i file video** (altrimenti rischio rimozione/filtraggio e ranking peggiore, specie in modalità Video; verificare Googlebot con DNS inverso); **consentire la scansione senza verifica dell'età** (altrimenti ranking scadente e rischio che contenuti non espliciti o l'intero sito siano classificati come espliciti); **separare le pagine esplicite in un dominio/sottodominio** distinto (non serve la parola "explicit"); metadati: `<meta name="rating" content="adult">` (o equivalente RTA `RTA-5042-1996-1400-1577-RTA`, anche come intestazione HTTP); Sitemap video `<video:family_friendly>no` solo per video espliciti; Shopping: attributo `adult` nel feed o `hasAdultConsideration` (non influisce sulla ricerca organica web).

## Che cosa fare se il tuo sito viene erroneamente segnalato come esplicito
Fonte: https://developers.google.com/search/docs/specialty/explicit/troubleshooting?hl=it
- Contenuti sfumati (lingerie, educazione sessuale, massaggi) possono essere filtrati per errore. Verifica: cercare la pagina con SafeSearch Off e poi "Filtra"; per l'intero sito usare `site:` + Filtra.
- Errori comuni: **meta rating adult su pagine non esplicite** (filtrate comunque); `family_friendly=no` applicato in modo generico; UGC non moderato; **verifica dell'età che blocca Googlebot** (seguire linee guida interstitial obbligatori, verificare con test URL live); pagine esplicite non separate.
- Dopo le correzioni attendere **almeno 2-3 mesi** prima di richiedere revisione (classificatori fino a 2-3 mesi); revisione immediata se le linee guida sono sempre state seguite. Immagini sfocate ma "sfocabili al contrario" restano esplicite. **Pagine esplicite non idonee** a risultati avanzati, snippet in primo piano, anteprime video.

---

# Settori specialistici — Siti internazionali

## Panoramica degli argomenti dei siti internazionali e multilingue
Fonte: https://developers.google.com/search/docs/specialty/international?hl=it
- Indice: siti multiregionali/multilingue, versioni localizzate (hreflang), pagine adattive alle impostazioni locali.

## Modalità di scansione delle pagine adattabili alle impostazioni internazionali
Fonte: https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages?hl=it
- Pagine che cambiano contenuto in base a paese/lingua del visitatore possono non essere scansionate/indicizzate per tutte le varianti: **gli IP predefiniti di Googlebot sembrano negli USA** e Googlebot **non invia l'header `Accept-Language`**.
- Consigliato: **URL separati per ogni locale + hreflang**.
- Googlebot scansiona anche da IP fuori USA; trattarlo come un utente di quel paese. Stessa stringa user agent; verifica con DNS inverso; regole robots (meta e robots.txt) **coerenti tra le versioni locali**.

## Informare Google dell'esistenza di versioni localizzate di una pagina (hreflang)
Fonte: https://developers.google.com/search/docs/specialty/international/localized-versions?hl=it
- Casi: solo template tradotto (UGC), varianti regionali della stessa lingua (en-US/GB/IE), traduzione completa. Le versioni localizzate sono **duplicati solo se il contenuto principale non è tradotto**.
- **Tre metodi equivalenti**: tag HTML `<link rel="alternate" hreflang>`, **intestazione HTTP `Link:`** (utile per PDF), **Sitemap** con `xhtml:link`. Usarne più di uno non porta vantaggi.
- **Google non usa `hreflang` né l'attributo `lang` per rilevare la lingua** (usa algoritmi sul contenuto).
- Regole: ogni versione elenca **se stessa e tutte le altre**; **URL assoluti con protocollo** (`https://example.com/foo`, non `//` o `/foo`); gli alternativi possono stare su domini diversi; URL catch-all per una lingua (es. `en`) accanto a `en-IE`, `en-CA`, `en-AU`; **link bidirezionali obbligatori** (altrimenti ignorati); se difficile, almeno collegare bidirezionalmente le nuove lingue alla lingua principale; **`x-default`** per pagine di selezione lingua/paese o home con redirect automatico.
- HTML: link nella `<head>` **ben formata** (verificare con validatore HTML); stesso insieme di link in ogni versione; **non combinare hreflang con altri attributi come `media`** nello stesso `<link>`. I sottodomini linguistici (`en`, `de`) **non** vengono usati per determinare il pubblico: serve mappatura esplicita.
- Sitemap: namespace `xmlns:xhtml="http://www.w3.org/1999/xhtml"`; un `<url>` per URL con `<loc>` e tutti gli `xhtml:link` (inclusa la pagina stessa); ordine indifferente; i `xhtml:link` non contano nel limite URL; la Sitemap può contenere solo URL discendenti della directory in cui è ospitata.
- Codici: lingua **ISO 639-1** + regione facoltativa **ISO 3166-1 Alpha 2**; **non supportati** codici come `es-419`; non si può indicare solo il paese (`be` = bielorusso, non Belgio); maiuscole indifferenti; sistema di scrittura ISO 15924 (`zh-Hant`, `zh-Hans`, `zh-Hans-US`); codici riservati come **`EU`, `UN`, `UK`** non hanno effetto (UK non è il codice ISO del Regno Unito: usare `GB`).
- Errori comuni: **assenza di link di ritorno**, codici lingua/regione errati. Strumenti terzi: generatore di Aleyda Solis, tester di Merkle (non gestiti da Google).

## Gestione dei siti multiregionali e multilingue
Fonte: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites?hl=it
- Multilingue = più lingue; multiregionale = target paesi diversi; possono coesistere.
- **URL diversi per ogni lingua** (non cookie o impostazioni del browser); hreflang. Contenuti dinamici o redirect basati sulla lingua → Google può non vedere le varianti (crawler dagli USA, senza `Accept-Language`).
- **Lingua determinata dal contenuto visibile**, non da `lang` o dall'URL: una sola lingua per contenuti e navigazione in ogni pagina; **evitare traduzioni affiancate**.
- **Non reindirizzare automaticamente** in base alla lingua presunta; offrire **link per cambiare lingua**.
- URL con parole localizzate o IDN ammessi; **UTF-8** ovunque e corretto escaping.
- Targeting geografico: URL specifici per locale e/o hreflang/Sitemap; mostrare selettori di regione/lingua. **Non usare l'analisi IP per adattare i contenuti** (inaffidabile, Google scansiona per lo più dagli USA).
- Strutture URL: **ccTLD** (`example.de`: targeting chiaro, server indifferente; costoso, un solo paese, requisiti), **sottodominio gTLD** (`de.example.com`), **sottodirectory gTLD** (`example.com/de/`: facile, stesso host), **parametri** (`?loc=de`: **non consigliati**).
- Segnali usati da Google: ccTLD; hreflang; posizione del server (non decisiva per CDN); altri indicatori: **indirizzi e numeri di telefono locali**, lingua e valuta locali, link da siti locali, **Profilo dell'attività**.
- Google **non** varia l'origine del crawler per scoprire varianti e **ignora meta tag geografici** (`geo.position`, `distribution`) e attributi HTML di geotargeting.
- Duplicati nella stessa lingua in regioni diverse: scegliere una versione preferita + `rel="canonical"` + hreflang.
- gTLD: .com, .org, .edu, .gov…; regionali trattati come generici: **.eu, .asia**; ccTLD trattati come generici: .ad, .ai, .as, .bz, .cc, .cd, .co, .dj, .fm, **.io**, .la, **.me**, .ms, .nu, .sc, .sr, .su, .tv, .tk, .ws (elenco variabile). Con un gTLD e un pubblico locale, definire esplicitamente il paese con i metodi indicati.

---

# Implicazioni per la skill SEO

## (a) Controlli verificabili automaticamente in un audit
Indicizzabilità e scansione
- [ ] Ogni URL pubblico importante risponde **HTTP 200**; URL rimossi rispondono **404/410 reali** (non soft 404: pagina "non trovata" con 200); spostamenti permanenti con **301**, temporanei con **302**.
- [ ] `robots.txt` non blocca pagine da indicizzare né **risorse CSS/JS/immagini** necessarie al rendering.
- [ ] Nessuna pagina da escludere affidata **solo a robots.txt** (serve `noindex` con scansione consentita); nessuna pagina bloccata da robots.txt che contenga anche `noindex` (conflitto: il noindex non viene letto).
- [ ] Nessun `noindex` accidentale (meta robots o header `X-Robots-Tag`) su pagine che devono comparire.
- [ ] Sitemap XML presente, raggiungibile, con URL canonici, assoluti, 200, coerenti con link interni e `rel="canonical"`.
- [ ] Ogni pagina indicizzabile ha `rel="canonical"` **autoreferenziale** (o verso la versione preferita); stesso formato URL ovunque (slash finale, maiuscole, `?page=1`, www/non-www, http/https).
- [ ] Un solo URL per ogni contenuto: redirect da varianti (http→https, www/non-www, maiuscole) all'URL preferito.
- [ ] Sito in **HTTPS**.
Link e struttura
- [ ] Navigazione realizzata con **`<a href="...">` scansionabili** (no `onclick`/router su `div`/`button`, no `href="javascript:"`, no `#` come link).
- [ ] **Nessun URL con frammento `#`** usato per distinguere contenuti/pagine (Google ignora i frammenti).
- [ ] Anchor text descrittivo (segnalare "clicca qui", "scopri di più", link vuoti); link-immagine con `alt` pertinente.
- [ ] Tutte le pagine raggiungibili da link interni (nessuna pagina orfana; profondità di click ridotta per le pagine chiave).
- [ ] Link a pagamento/affiliazione con `rel="sponsored"` o `nofollow`; link UGC con `rel="ugc"`/`nofollow`.
- [ ] Footer/credit link "sito realizzato da" verso siti terzi: valutare `nofollow` (link diffusi in template di più siti = esempio di link spam).
- [ ] URL descrittivi (parole, non ID casuali); parametri in formato `?key=value`, non ripetuti; niente ID sessione/timestamp nei link interni.
- [ ] Scroll infinito / "carica altro" affiancati da URL paginati con link `<a href>`; nessuna dipendenza da `rel=next/prev` (non usati da Google).
Contenuto on-page
- [ ] `<title>` presente, **unico** per pagina, descrittivo e conciso (nome sito/attività ed eventualmente sede).
- [ ] Meta description presente, unica, una-due frasi, con i punti chiave.
- [ ] Contenuti principali presenti come **testo nel DOM renderizzato** (non solo in immagini, canvas, video, plugin, né generati con CSS `content`).
- [ ] Immagini con `alt` descrittivo, posizionate vicino al testo pertinente.
- [ ] Assenza di testo nascosto manipolativo (testo colore=sfondo, `font-size:0`, `opacity:0`, posizionamento fuori schermo) — esclusi accordion/tab/testo per screen reader legittimi.
- [ ] Nessun blocco di keyword stuffing (liste di città/regioni, numeri di telefono ripetuti).
- [ ] Nessun meta `keywords` necessario (ignorato: può essere rimosso; non è un errore).
- [ ] Byline/autore e pagina "chi sono"/"about" collegate dove il lettore se le aspetta.
- [ ] Date di pubblicazione/aggiornamento non modificate senza cambi sostanziali (verificabile confrontando versioni nel repo).
Dati strutturati e aspetto
- [ ] JSON-LD sintatticamente valido; tipi supportati da Google; coerente con il contenuto visibile (convalidare con Test dei risultati avanzati).
- [ ] Favicon presente.
- [ ] Nessun interstitial/popup intrusivo che copra il contenuto.
Internazionale (se multilingue)
- [ ] URL separati per lingua (sottodirectory/sottodominio/ccTLD), non cookie/`Accept-Language`/IP.
- [ ] `hreflang` reciproco e completo (ogni pagina cita se stessa e tutte le alternative), URL assoluti con `https://`, codici ISO 639-1 (+ ISO 3166-1 alpha-2; `en-GB` non `en-UK`), `x-default` sulla pagina di selezione/home.
- [ ] Nessun redirect automatico per lingua/IP; presente un selettore di lingua con link.
- [ ] Una sola lingua per pagina (contenuto + navigazione); regole robots coerenti tra versioni.
Sicurezza / igiene
- [ ] Nessuno script/iframe di terze parti sconosciuto; dipendenze aggiornate (CMS, plugin, librerie); nessun open redirect (`?url=http...`).
- [ ] Assenza di file `llms.txt` **non** è un problema (Google Search non lo usa): non segnalarlo come errore.

## (b) Regole per chi costruisce un sito nuovo
- Progettare **un URL per ogni schermata/contenuto** fin dall'inizio, con parole descrittive, minuscole, senza frammenti `#` e senza parametri temporanei.
- Navigazione solo con link `<a href>` reali; menu, footer e breadcrumb scansionabili.
- Ogni pagina: `<title>` unico, meta description unica, un'intestazione principale chiara, contenuti testuali, immagini con `alt`, canonical autoreferenziale.
- HTTPS dal giorno uno; redirect 301 da http e dalla variante www/non-www non preferita.
- `robots.txt` minimale (non bloccare CSS/JS); `noindex` per pagine di servizio (ringraziamento form, staging); proteggere con password lo staging, non solo con robots.txt.
- Sitemap XML generata nel build e dichiarata in robots.txt/inviata in Search Console.
- Pagine 404 personalizzate ma con **status 404**.
- Lancio: verificare la proprietà in **Search Console** (anche prima del lancio, es. con home page segnaposto), inviare Sitemap, richiedere indicizzazione delle pagine principali con Controllo URL, attendere settimane per valutare.
- Contenuti: originali, basati su esperienza diretta, con autore chiaro; nessuna lunghezza minima; niente pagine "una per ogni città" fotocopia (doorway); niente produzione massiva con AI senza revisione.
- Dati strutturati pertinenti (es. `Organization`/`LocalBusiness`, `BreadcrumbList`, `Person` per l'autore — quest'ultimo da verificare nella doc dati strutturati di altri gruppi), sempre coerenti con il visibile.
- Dominio: scegliere il nome per il brand, non per le keyword (effetto quasi nullo); TLD rilevante solo per target paese (`.it` utile per pubblico italiano; `.io`, `.me`, `.dev`-tipo trattati come generici — `.io` e `.me` sono esplicitamente nella lista dei generici).
- Prevedere link "Cambia lingua" e hreflang se il sito è bilingue (es. IT/EN).
- Non serve `llms.txt`, chunking dei contenuti o markup "per l'AI" per Google Search.

## (c) Note specifiche per SPA JavaScript / Angular
- Google esegue JS con un **Chrome recente**, ma "Google non sempre vede ciò che vede l'utente" e la SEO di framework JS è "generalmente più complessa": preferire **SSR/prerendering** (Angular SSR/hydration o prerender statico) perché contenuti, `<title>`, meta, canonical e JSON-LD siano nell'HTML servito (deduzione coerente con le pagine lette; dettagli nella doc SEO JS di altri gruppi).
- **Ogni route deve avere un URL reale** (Angular Router con `PathLocationStrategy`, **non `HashLocationStrategy`**: gli URL con `#/...` sono visti come la stessa pagina perché Google ignora i frammenti).
- `routerLink` su elementi `<a>` produce `href`: OK. Evitare `(click)="router.navigate(...)"` su `div`/`button`/`span` per la navigazione: Googlebot **non clicca** e non attiva JS che richiede interazione.
- Il server deve restituire **404 reale** per route inesistenti (in una SPA pura la wildcard route restituisce 200 → soft 404); con SSR impostare lo status della risposta; in alternativa usare `noindex` sulla pagina "non trovata".
- Aggiornare `<title>`/meta description per ogni route (servizi `Title` e `Meta` di Angular) e canonical per route; idealmente lato server.
- Non bloccare in robots.txt i bundle JS/CSS, gli asset o gli endpoint API necessari al rendering.
- Contenuti "load more"/scroll infinito → affiancare URL paginati con `<a href>`.
- Testo inserito con CSS `content` o disegnato in `<canvas>` (es. animazioni hero, grafici) non è indicizzato: duplicare in testo HTML.
- Verificare il rendering con **Controllo URL → Testa URL live** (HTML renderizzato, screenshot, risorse bloccate) e il Test dei risultati avanzati.
- Nessun contenuto diverso servito a Googlebot rispetto agli utenti (il dynamic rendering/prerender deve produrre lo stesso contenuto, altrimenti è cloaking).
- Per siti bilingui: usare route/URL distinti per lingua (es. `/it/`, `/en/`, coerente con l'i18n di Angular che compila build per locale), **non** switch di lingua solo client-side senza cambio URL.

## (d) Note specifiche per personal brand (portfolio sviluppatore) e professionista locale (orientatrice di carriera)
Personal brand / portfolio (target recruiter)
- E-E-A-T: la "Chi" conta — pagina "about" con nome reale, ruolo, competenze, link ai profili; byline sugli articoli che rimanda alla pagina autore. Esperienza in prima persona: case study dei progetti con il "come" (stack, decisioni, risultati, screenshot/demo/repo come **prove**).
- Contenuti non generici: preferire post tecnici basati su problemi reali risolti a "10 consigli per…" (la guida AI cita proprio i contenuti generici come poco utili).
- Titoli che contengono il nome (query di brand "Nome Cognome developer") e il ruolo; nome sito = brand personale.
- Contenuti social (GitHub, LinkedIn, YouTube, X, Instagram, TikTok) possono comparire su Google: aggiungere le **proprietà della piattaforma** in Search Console / rivendicare il **profilo della Ricerca** per monitorarli.
- Monitoraggio della notorietà del nome con Google Trends (se c'è volume) e del report Rendimento (query brand).
- Attenzione ai link "realizzato da" nei siti dei clienti: link nei footer di molti siti = esempio di link spam → usare `nofollow`/`sponsored` o testo semplice.
- Dominio: `.dev`, `.io`, `.me` vanno bene (i ccTLD `.io`/`.me` sono trattati come generici); il dominio con keyword non aiuta.
Professionista locale + online (orientatrice di carriera)
- **Profilo dell'attività su Google** (rivendicato) è segnale locale e alimenta anche le risposte AI; dati strutturati `LocalBusiness` (sede, orari) — da approfondire nella doc dedicata.
- Mettere **indirizzo, telefono, città** come testo visibile (indicatori di targeting geografico); `<title>` può includere la sede fisica.
- **Non** creare molte pagine quasi identiche "orientamento al lavoro [città]" che rimandano allo stesso servizio (doorway abuse) né blocchi con elenchi di città (keyword stuffing). Pagine per sede solo se reali e con contenuti distinti.
- Argomenti di carriera/finanza personale possono essere vicini a **YMYL** (stabilità finanziaria): alzare il livello di affidabilità (credenziali, certificazioni, fonti, chi scrive, testimonianze reali).
- Workshop/corsi/webinar: pagine dedicate con dati strutturati **Event** (citato nella guida e-commerce per le opportunità di formazione).
- Recensioni: raccoglierle in modo autentico; mai scambiare servizi per recensioni con link; per recensioni scritte seguire le best practice (prove, esperienza diretta).
- Query con risposta già in SERP (orari, telefono): CTR basso ma comportamento atteso se l'obiettivo è il contatto.
- Pubblico italiano: TLD `.it` utile come segnale paese (basso impatto); se servizi anche in inglese → URL separati + hreflang `it`/`en` + `x-default`.
- Mettere l'URL del sito su biglietti da visita, materiali stampati, profili.

## (e) Cose che una skill NON può fare (azioni manuali/off-site)
- Verificare la proprietà in **Search Console** (può però generare il file HTML o il meta tag di verifica), inviare la Sitemap, usare Controllo URL / Richiedi indicizzazione, strumento Rimozioni, Cambio di indirizzo, leggere report (Rendimento, Indicizzazione, Core Web Vitals, Azioni manuali, Problemi di sicurezza, rendimento AI generativa), attivare l'inclusione nelle **funzionalità di AI generativa** in Search Console, richiedere riconsiderazione o revisioni di sicurezza/SafeSearch (salvo accesso via API/connettori forniti dall'utente).
- Creare/rivendicare il **Profilo dell'attività su Google**, account Merchant Center, rivendicare il **profilo della Ricerca** o aggiungere proprietà social.
- Promozione off-site: community, social, passaparola, newsletter, materiali stampati; ottenere link naturali.
- Raccogliere recensioni reali, testimonianze, prove di esperienza (foto, casi reali): la skill può strutturarle, non inventarle.
- Garantire indicizzazione o ranking (Google non garantisce nulla; tempi da ore a mesi).
- Analisi Google Trends, Keyword Planner, Looker Studio, Google Analytics, BigQuery: richiedono accesso dell'utente; la skill può guidare o interpretare dati esportati.
- Configurazioni lato hosting/server non presenti nel repo (redirect a livello CDN, header, certificati HTTPS, aggiornamenti del sistema operativo del server): la skill può solo proporre la configurazione.
- Valutare la qualità "umana" (utilità, originalità, EEAT) in modo definitivo: può applicare le domande di autovalutazione Google, ma serve giudizio dell'autore e di lettori esterni (Google suggerisce un parere onesto di persone non affiliate).
- Verificare come appare il sito da Googlebot reale (rendering, IP USA) senza Controllo URL: può solo simulare con un browser headless.
