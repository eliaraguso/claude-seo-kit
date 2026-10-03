# Gruppo E — Dati strutturati parte 2 (local-business → video)

Appunti fedeli alla documentazione Google Search Central (versione IT). File letti: 22/22 dell'elenco E.list.
Ordine: prima le pagine più rilevanti per siti vetrina/portfolio/professionisti (sd-policies, galleria, local-business, organization, profile-page, review-snippet), poi gli altri tipi (QAPage, programmi fedeltà, risolutori matematici, film, paywall, famiglia Product, norme resi/spedizione, ricette, app software, speakable, case vacanze, video). In fondo: "Implicazioni per la skill SEO".

Elementi ricorrenti in TUTTE le pagine dei singoli tipi (non ripetuti ogni volta):
- Flusso standard: aggiungi proprietà obbligatorie → segui linee guida → valida con **Test dei risultati avanzati** (https://search.google.com/test/rich-results), correggi errori critici; i problemi non critici conviene correggerli ma non servono per l'idoneità → pubblica alcune pagine e verifica con **strumento Controllo URL** (pagina non bloccata da robots.txt, `noindex` o login) → richiedi nuova scansione (non immediata, possono passare diversi giorni) → invia **Sitemap** (automatizzabile con API Search Console Sitemap).
- Se si usa JavaScript: rimando a "generare dati strutturati con JavaScript". Se CMS: plug-in.
- Violazione linee guida → possibile **azione manuale**; dopo la correzione si chiede **riconsiderazione**.
- Risoluzione problemi: Google non garantisce la visualizzazione; elenco errori dati strutturati; report "dati strutturati non analizzabili"; se c'è un'azione manuale sui dati strutturati questi vengono **ignorati** (la pagina può comunque comparire nella Ricerca); report Azioni manuali; spam di contenuti/markup non rilevabile dal Test; guida per cali di risultati avanzati; forum Search Central.
- Monitoraggio con Search Console (dove presente): report sullo stato dei risultati avanzati dopo il primo deploy (aumento elementi validi, nessun aumento non validi; correggi → Controllo URL → "Richiedi convalida"); dopo nuovi template monitorare aumento di errori o calo di elementi validi (calo senza aumento di non validi = probabilmente il markup non viene più incorporato); analisi periodica con report Rendimento / API Search Console.

---

## Linee guida generali sui dati strutturati
Fonte: https://developers.google.com/search/docs/appearance/structured-data/sd-policies?hl=it

**Principio generale**
- Per l'idoneità ai risultati avanzati, i dati strutturati non devono violare le **norme relative ai contenuti per la Ricerca Google** (che includono le **norme relative allo spam**) + le linee guida generali di questa pagina.
- Un problema relativo ai dati strutturati può comportare un'**azione manuale**: la pagina **perde l'idoneità ai risultati multimediali** ma **il ranking non è influenzato**. Verifica nel report Azioni manuali di Search Console.
- **Google non garantisce** la visualizzazione anche con markup corretto secondo il Test dei risultati avanzati. Motivi possibili:
  - i dati strutturati abilitano una funzionalità ma non la garantiscono; l'algoritmo adatta i risultati (cronologia ricerche, posizione, dispositivo); a volte un semplice risultato di testo è ritenuto migliore;
  - dati strutturati non rappresentativi dei contenuti principali o potenzialmente fuorvianti;
  - dati non corretti e non rilevati dal Test;
  - contenuti a cui fanno riferimento nascosti all'utente;
  - pagina non conforme a queste linee guida, alle linee guida della singola funzionalità, alle Nozioni di base sulla Ricerca o alle norme sui contenuti.

**Linee guida tecniche** (verificabili con Test dei risultati avanzati + Controllo URL)
- **Formato**: uno dei tre formati supportati: **JSON-LD (consigliato)**, Microdati, RDFa.
- **Accesso**: non bloccare le pagine con dati strutturati a Googlebot tramite robots.txt, `noindex` o altri controlli d'accesso.

**Norme sulla qualità** (non facilmente verificabili automaticamente; la violazione può impedire i risultati avanzati anche con sintassi corretta o far contrassegnare come spam)
- *Contenuti*:
  - seguire le norme relative allo spam;
  - fornire informazioni **aggiornate** (niente risultati avanzati per contenuti obsoleti);
  - contenuti **originali** generati da te o dai tuoi utenti;
  - **non** fare markup di contenuti **non visibili** ai lettori (es. se il JSON-LD descrive un artista, il corpo HTML deve descrivere lo stesso artista);
  - **non** fare markup di contenuti irrilevanti o fuorvianti (es. **recensioni fittizie**, contenuti estranei all'argomento);
  - **non** usare i dati strutturati per ingannare; non rubare l'identità di persone/organizzazioni, non rappresentare in modo ingannevole proprietà, affiliazione o scopo principale;
  - rispettare anche le norme specifiche della funzionalità (es. `JobPosting` → norme contenuti offerte di lavoro).
- *Pertinenza*: rappresentazione fedele dei contenuti della pagina. Esempi non pertinenti: sito di live streaming sportivo che etichetta le trasmissioni come eventi locali; sito di lavorazione del legno che etichetta istruzioni come ricette.
- *Completezza*: specificare **tutte le proprietà obbligatorie** della funzionalità (altrimenti non idonei). Più proprietà consigliate = migliore qualità. Recensioni/valutazioni non provenienti da utenti reali possono comportare un'**azione manuale**. Il ranking dei risultati avanzati considera informazioni aggiuntive.
- *Località*: inserire i dati strutturati nella pagina che descrivono (salvo diversa indicazione). Con pagine duplicate, mettere gli stessi dati strutturati su **tutte** le pagine duplicate, non solo sulla canonica.
- *Specificità*: usare il **tipo e le proprietà schema.org più specifici** applicabili; seguire le linee guida aggiuntive di ogni tipo.
- *Immagini*: l'immagine indicata deve essere pertinente alla pagina; tutti gli URL immagine devono essere **scansionabili e indicizzabili** (verifica con Controllo URL).

**Più elementi in una pagina**
- Google comprende più elementi sia **nidificati** (un elemento principale con altri raggruppati sotto, es. `Recipe` con `aggregateRating` e `video`) sia come **singoli elementi** separati (es. array JSON-LD con `Recipe` e `BreadcrumbList`).
- Se elementi separati sono collegati (es. ricetta e video), usare **`@id`** in entrambi per collegarli; altrimenti Google potrebbe non sapere che il video riguarda la ricetta.
- Includere sempre il **tipo principale** che rispecchia lo scopo della pagina (se la pagina è una ricetta, includere `Recipe` oltre a `Video` e `Review`; con solo `Video` non sarebbe idonea al risultato ricetta).
- Completezza degli elementi: se si includono più recensioni, fare markup di **tutte** quelle visibili; ometterne alcune è fuorviante.

---

## Markup dei dati strutturati supportato dalla Ricerca Google (galleria)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/search-gallery?hl=it

Elenco delle funzionalità presenti nella galleria (con categoria filtro):
- **Articolo** (Notizie, Sport) — titolo e immagini più grandi della miniatura.
- **Breadcrumb** (Generico) — posizione della pagina nella gerarchia del sito.
- **Carosello** (Cibi e bevande, Istruzione e scienza, Intrattenimento) — galleria/elenco sequenziale da un singolo sito; va usato con Ricetta, Elenco di corsi, Ristorante o Film.
- **Elenco di corsi** (Istruzione e scienza) — corsi dello stesso fornitore (titolo, fornitore, breve descrizione).
- **Set di dati** (Istruzione e scienza) — in Ricerca Google per set di dati.
- **Forum di discussione** — contenuti generati dagli utenti seguiti da discussione.
- **Domande e risposte didattiche** (Istruzione e scienza) — flashcard.
- **Valutazione complessiva del datore di lavoro** (Opportunità di lavoro).
- **Evento** (Intrattenimento) — eventi in un giorno e luogo specifici.
- **Metadati immagine** — autore, licenza, crediti in Google Immagini.
- **Offerta di lavoro** (Opportunità di lavoro).
- **Attività locali** (Organizzazioni) — dettagli nella scheda informativa: orari, valutazioni, indicazioni stradali, azioni per appuntamenti/ordini.
- **Risolutore matematico** (Istruzione e scienza).
- **Film** (Intrattenimento) — carosello film.
- **Organizzazione** (Organizzazioni) — logo, nome legale, indirizzo, contatti, identificatori aziendali; mostrate in schede informative e altri elementi visivi (es. attribuzione).
- **Prodotto** (E-commerce) — prezzo, disponibilità, valutazioni.
- **Pagina del profilo** — pagina incentrata su una singola persona o organizzazione affiliata al sito.
- **Domande e risposte** (QAPage).
- **Ricetta** (Cibi e bevande).
- **Snippet recensione** (Organizzazioni, E-commerce, Cibi e bevande, Intrattenimento) — per Libro, Ricetta, Film, Prodotto, App software, Attività locale.
- **App software**.
- **Speakable** (Notizie) — lettura vocale con Assistente Google.
- **Contenuti in abbonamento e protetti da paywall** (Notizie) — per distinguerli dal cloaking.
- **Casa vacanze**.
- **Video** (Cibi e bevande, Notizie, Istruzione e scienza, Sport) — riproduzione, segmenti, live streaming.
- Nota: in questa versione della galleria **non compaiono** FAQ né HowTo (osservazione sull'elenco letto, non un'affermazione della pagina).
- L'aspetto effettivo può differire; anteprima con il test dei risultati avanzati.

---

## Dati strutturati per attività locali (`LocalBusiness`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/local-business?hl=it

**A cosa serve / dove appare**
- Quando si cercano attività su Ricerca Google o Maps può comparire una **scheda informativa** in evidenza; per ricerche di categoria (es. "i migliori ristoranti di New York") un **carosello** di attività.
- Con il markup si comunicano a Google orari di apertura, reparti, recensioni (se il sito raccoglie recensioni su **altre** attività) e altro.
- Per prenotazioni/ordini direttamente dai risultati: **API Maps Booking** (non il markup).
- Non sono indicate limitazioni di paese/lingua per la scheda base. Il **carosello dei ristoranti** è ad **accesso limitato** (piccolo gruppo di ristoratori; modulo per manifestare interesse).

**Dove metterlo**
- Si può aggiungere a qualsiasi pagina, ma è più utile su una pagina con informazioni sull'attività.
- Definire **ogni sede** come `LocalBusiness`; usare il **sottotipo più specifico** (`Restaurant`, `DaySpa`, `HealthClub`, ...).
- `LocalBusiness` è sottotipo di `Organization` → seguire anche i campi di Organization.
- Più tipi: specificarli in **array** in `@type` (es. `["Electrician", "Plumber", "Locksmith"]`); **`additionalType` non è supportato**.

**Proprietà obbligatorie**
- `address` (`PostalAddress`) — sede fisica; includere quante più sottoproprietà possibile (`streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`).
- `name` (`Text`) — nome dell'attività.

**Proprietà consigliate**
- `aggregateRating` (`AggregateRating`) — **solo per siti che acquisiscono recensioni su altre attività locali**; seguire le linee guida snippet recensione.
- `department` (`LocalBusiness`) — elemento nidificato per reparto; può avere qualsiasi proprietà della tabella. Nome nel formato `{store name} {department name}` (es. `gMart` e `gMart Pharmacy`); se il reparto ha un brand proprio, solo il nome del reparto (es. `Best Buy` e `Geek Squad`).
- `geo` (`GeoCoordinates`) con `geo.latitude` e `geo.longitude` (`Number`) — **precisione di almeno 5 cifre decimali**.
- `menu` (`URL`) — per attività alimentari, URL completo del menu.
- `openingHoursSpecification` (array o singolo oggetto `OpeningHoursSpecification`):
  - `opens` / `closes` (`Time`, formato hh:mm:ss; negli esempi "11:30");
  - `dayOfWeek` (`DayOfWeek`): `https://schema.org/Monday` … `Sunday`; supportati anche i nomi brevi (`Monday`);
  - `validFrom` / `validThrough` (`Date`, AAAA-MM-GG) — inizio/fine di chiusura/orario stagionale.
- `priceRange` (`Text`) — es. "10-15 $" o "$$$"; **deve contenere meno di 100 caratteri** (≥100 → Google non mostra la fascia di prezzo).
- `review` (`Review`) — **solo per siti che acquisiscono recensioni su altre attività locali**.
- `servesCuisine` — tipo di cucina (ristoranti).
- `telephone` (`Text`) — numero principale di contatto per i clienti, **con codice paese e prefisso**.
- `url` (`URL`) — URL completo della **sede specifica**; deve essere un link funzionante.

**Regole orari (esempi)**
- Senza `validFrom`/`validThrough` gli orari valgono tutto l'anno.
- Orari dopo mezzanotte: singolo `OpeningHoursSpecification` (es. sabato opens 18:00, closes 03:00).
- Aperto 24h: `opens` "00:00" e `closes` "23:59". Chiuso tutto il giorno: `opens` e `closes` entrambi "00:00".
- Orari stagionali/chiusure festive: `validFrom` + `validThrough` con opens/closes "00:00".
- Google accetta sia la notazione ufficiale dayOfWeek (URL) sia la forma breve.

**Carosello dei ristoranti (accesso limitato)**
- Richiede pagina di riepilogo con markup Carousel + pagine di dettaglio. Proprietà obbligatorie: `image` (URL o ImageObject ripetuto) e `name`; consigliate: `address`, `servesCuisine`.
- Linee guida immagini: URL scansionabili e indicizzabili; immagini rappresentative; formato supportato da Google Immagini; più immagini ad alta risoluzione (**minimo 50.000 pixel** larghezza×altezza) nei formati **16x9, 4x3, 1x1**.

**Linee guida**
- Nozioni di base sulla Ricerca + linee guida generali sui dati strutturati + linee guida Carosello (se pertinenti). Violazione → azione manuale.

---

## Dati strutturati per organizzazioni (`Organization`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/organization?hl=it

**A cosa serve / dove appare**
- Markup sulla **home page** che aiuta Google a capire i dettagli amministrativi dell'organizzazione e a distinguerla.
- Alcune proprietà servono "dietro le quinte" per disambiguare (es. `iso6523Code`, `naics`); altre influenzano elementi visivi: quale **`logo`** viene mostrato nei risultati e nella **scheda informativa** (knowledge panel).
- Per i commercianti: influenza **scheda informativa del commerciante** e **profilo del brand** (norme resi, indirizzo, contatti).
- **Nessuna proprietà obbligatoria**: aggiungere tutte quelle pertinenti.
- Nessuna limitazione di paese/lingua indicata.

**Linee guida tecniche**
- Inserire le informazioni nella **home page** o in una **singola pagina** che descrive l'organizzazione (es. **Chi siamo**). **Non serve** includerle in ogni pagina.
- Usare il **sottotipo più specifico** di `Organization` (es. `OnlineStore` invece di `OnlineBusiness` per e-commerce).
- Per attività locali (ristorante, negozio fisico): usare i sottotipi di `LocalBusiness` rispettando i campi obbligatori/consigliati di Local Business, **oltre** a quelli di questa guida.
- Concentrarsi sulle proprietà utili agli utenti: `name`/`alternateName`, presenza fisica (`address`, `telephone`), presenza online (`url`, `logo`).

**Proprietà consigliate (nessuna obbligatoria)**
- `address` (`PostalAddress`, anche multipli per sedi in più città/paesi): `addressCountry` (**ISO 3166-1 alpha-2**, due lettere), `addressLocality`, `addressRegion`, `postalCode`, `streetAddress`.
- `alternateName` (`Text`) — altro nome comune.
- `contactPoint` (`ContactPoint`) — miglior modo per contattare (seguire best practice assistenza clienti di Google): `contactPoint.email`, `contactPoint.telephone` (con codice paese e prefisso). Con `LocalBusiness`, specificare **prima** email/telefono principali a livello `LocalBusiness` e poi `contactPoint` per metodi aggiuntivi.
- `description` (`Text`) — descrizione dettagliata.
- `duns` (`Text`) — DUNS; consigliato invece `iso6523Code` con prefisso `0060:`.
- `email` (`Text`).
- `foundingDate` (`Date`, ISO 8601).
- `globalLocationNumber` (`Text`) — GLN GS1.
- `hasMerchantReturnPolicy` (`MerchantReturnPolicy` ripetuto) — norme resi (vedi pagina return-policy); può essere usato anche nella scheda commerciante per override a livello prodotto.
- `hasMemberProgram` (`MemberProgram` ripetuto) — programma fedeltà.
- `hasShippingService` (`ShippingService` ripetuto) — norme di spedizione; override possibile a livello prodotto.
- `iso6523Code` (`Text`) — formato `ICD:identificatore` separati da due punti (U+003A). ICD comuni: `0060` DUNS, `0088` GLN GS1, `0199` LEI.
- `legalName` (`Text`) — nome legale registrato se diverso da `name`.
- `leiCode` (`Text`) — ISO 17442; consigliato invece `iso6523Code` con prefisso `0199:`.
- `logo` (`URL` o `ImageObject`): immagine **almeno 112x112 px**; URL scansionabile e indicizzabile; formato supportato da Google Immagini; deve apparire bene su **sfondo bianco**; con `ImageObject` serve `contentUrl` o `url` valido.
- `naics` (`Text`) — codice NAICS.
- `name` (`Text`) — usare lo **stesso `name` e `alternateName` del nome del sito** (site names).
- `numberOfEmployees` (`QuantitativeValue`) — `value` oppure `minValue`/`maxValue`.
- `sameAs` (`URL`, multipli) — profili su social media o siti di recensioni.
- `taxID` (`Text`) — deve corrispondere al paese in `address`.
- `telephone` (`Text`) — recapito principale, con codice paese e prefisso.
- `url` (`URL`) — sito web dell'organizzazione; aiuta a identificarla univocamente.
- `vatID` (`Text`) — partita IVA; **importante indicatore di fiducia** (verificabile nei registri pubblici).

**Esempi**: `Organization` base (url, sameAs, logo, name, description, email, telephone, address, vatID, iso6523Code); `OnlineStore` con `hasShippingService` + `hasMerchantReturnPolicy`.

---

## Dati strutturati per pagine del profilo (`ProfilePage`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/profile-page?hl=it

**A cosa serve / dove appare**
- Per tutti i siti in cui autori di contenuti (persone o organizzazioni) condividono **prospettive in prima persona**. Aiuta Google a capire i creator di una community e a mostrarne meglio i contenuti, inclusa la funzionalità **Discussioni e forum**.
- Altre funzionalità possono collegarsi a pagine `ProfilePage` (autori di `Article`, `Recipe`, forum di discussione, QAPage).
- Nessuna limitazione di paese/lingua indicata.

**Linee guida relative ai contenuti**
- L'elemento principale della pagina deve essere **una singola persona o organizzazione affiliata al sito web nel suo complesso**.
- Casi validi: profilo utente su forum/social; **pagina dell'autore** su sito di notizie; **pagina "Chi sono" su un blog**; **pagina del dipendente** sul sito di un'azienda.
- Casi non validi: **home page principale di un negozio** (molte informazioni non di profilo); sito di recensioni di un'organizzazione (organizzazione non associata al sito).

**Linee guida tecniche**
- Se il profilo mostra attività recenti dell'autore, si possono includere con `hasPart` (es. `Article` con `headline`, `url`, `datePublished`, `author` che punta a `{"@id": "#main-author"}`), riferendosi con URL alla pagina con contenuto completo e markup.

**`ProfilePage` — obbligatorie**
- `mainEntity` (`Person` o `Organization`) — l'entità di cui tratta la pagina. Usare il tipo corretto se noto; altrimenti default `Person`.

**`ProfilePage` — consigliate**
- `dateCreated` (`DateTime`, ISO 8601) — creazione del profilo.
- `dateModified` (`DateTime`, ISO 8601) — modifica dei metadati del profilo fatta da persone (aggiungere link esterni che puntano al profilo non conta come modifica).

**`Person`/`Organization` (mainEntity) — obbligatorie**
- `name` (`Text`) — nome reale consigliato (handle social in `alternateName`); si può usare l'handle se è l'unico identificativo sul sito. Se `name` non è disponibile, `alternateName` soddisfa il requisito.

**`Person`/`Organization` — consigliate**
- `agentInteractionStatistic` (`InteractionCounter`) — comportamento dell'entità: `FollowAction` (account seguiti), `LikeAction` (Mi piace dati), `WriteAction` (numero post), `ShareAction` (ricondivisioni).
- `alternateName` (`Text`) — es. handle social.
- `description` (`Text`) — riga dell'autore o **qualifiche pertinenti**.
- `identifier` (`Text`) — ID univoco interno (stabile anche se cambia l'handle).
- `image` (`URL` o `ImageObject`) — immagine del profilo; **non** usare immagini predefinite/segnaposto/icone se non c'è una foto. Linee guida immagini: scansionabili/indicizzabili, rappresentative, formato supportato, alta risoluzione (min **50.000 pixel**), formati 16x9, 4x3, 1x1.
- `interactionStatistic` (`InteractionCounter`) — statistiche ricevute **solo sulla piattaforma che ospita il profilo** (non follower di altri siti): `FollowAction` (follower), `LikeAction` (Mi piace ricevuti), `BefriendAction` (relazione bidirezionale).
- `sameAs` (`URL`) — altri profili esterni o home page del profilo.

Formati negli esempi: JSON-LD e Microdati.

---

## Dati strutturati per snippet recensione (`Review`, `AggregateRating`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/review-snippet?hl=it

**A cosa serve / dove appare**
- Breve estratto di recensione/valutazione da un sito di recensioni, in genere media dei punteggi. Può mostrare un **rich snippet con stelle** e info di riepilogo; può apparire nei risultati avanzati o nelle **schede informative**.
- Funzionalità che supportano le valutazioni: Libri, Elenco di corsi, Evento, **Attività locale (solo siti che acquisiscono recensioni su ALTRE attività locali)**, Film, Prodotto, Ricette, App software.
- Supportate anche per tipi schema.org (e sottotipi): `CreativeWorkSeason`, `CreativeWorkSeries`, `Episode`, `Game`, `MediaObject`, `MusicPlaylist`, `MusicRecording`, **`Organization` (solo siti che acquisiscono recensioni su altre organizzazioni)**.
- Recensioni su altri datori di lavoro → `EmployerAggregateRating`.

**Modalità di markup**
- Recensione semplice (`Review` con `itemReviewed`); recensione nidificata (proprietà `review` in un altro tipo); valutazione complessiva (`AggregateRating` con `itemReviewed`); valutazione complessiva nidificata (proprietà `aggregateRating`).
- Si può omettere la valutazione di una singola recensione se il contenuto ha autore e data; per le recensioni complessive la **valutazione media è necessaria** per i rich snippet.

**Linee guida tecniche**
- Valutazione di molte persone → `AggregateRating`.
- Riferirsi chiaramente a un prodotto/servizio specifico, nidificando la recensione o usando `itemReviewed`.
- I contenuti delle recensioni devono essere **prontamente visibili** sulla pagina: l'utente deve vedere testo e valutazione; con `AggregateRating` deve vedere la valutazione aggregata.
- Consigliato (non obbligatorio) accettare solo valutazioni con commento e nome dell'autore.
- Recensioni su un **elemento specifico**, non su una categoria o un elenco.
- Se ci sono più recensioni singole, includere anche la valutazione complessiva.
- **Non aggregare recensioni o valutazioni da altri siti web.**
- **Non includere recensioni false o incentivate non divulgate**: non basate su esperienza reale; scritte in cambio di vantaggi (denaro, sconti, voucher, prodotti gratis) senza indicare chiaramente l'incentivo.
- **Attività locali/organizzazioni — regole aggiuntive (recensioni "self-serving")**:
  - se l'entità recensita **controlla le recensioni su se stessa**, le sue pagine con `LocalBusiness` o qualsiasi `Organization` **non sono idonee** alle stelle. Es.: recensione dell'entità A pubblicata sul sito di A, direttamente nel markup **o tramite widget di terze parti incorporato** (recensioni Google Business, widget recensioni Facebook);
  - le valutazioni devono provenire **direttamente dagli utenti**;
  - non affidarsi a editor umani per creare/curare/compilare le valutazioni di attività locali.

**`Review` — obbligatorie**
- `author` (`Person` o `Organization`) — nome valido (es. "50% di sconto fino a sabato" non è valido); **meno di 100 caratteri**, altrimenti non idoneo allo snippet basato sull'autore. Seguire best practice markup autori (pagina Article).
- `itemReviewed` (se non nidificata) — tipi validi: `Book`, `Course`, `CreativeWorkSeason`, `CreativeWorkSeries`, `Episode`, `Event`, `Game`, `HowTo`, `LocalBusiness`, `MediaObject`, `Movie`, `MusicPlaylist`, `MusicRecording`, `Organization`, `Product`, `Recipe`, `SoftwareApplication`.
- `itemReviewed.name` o `name` dell'elemento principale se nidificata.
- `reviewRating` (`Rating`).
- `reviewRating.ratingValue` (`Number` o `Text`) — numero, frazione o percentuale (`4`, `60%`, `6 / 10`); scala predefinita **1–5** per i numeri; per altre scale usare `bestRating`/`worstRating`. **Decimali con punto** (`4.4`, non `4,4`); in Microdati/RDFa si può usare l'attributo `content` per mostrare la virgola all'utente.

**`Review` — consigliate**
- `datePublished` (`Date`, ISO 8601).
- `reviewRating.bestRating` (`Number`, default 5).
- `reviewRating.worstRating` (`Number`, default 1).

**`AggregateRating` — obbligatorie**
- `itemReviewed` (se non nidificata; stessi tipi validi) + `itemReviewed.name` / `name` dell'elemento principale.
- `ratingCount` (`Number`) **o** `reviewCount` (`Number`) — almeno uno dei due.
- `ratingValue` (`Number` o `Text`) — stesse regole di scala e punto decimale.

**`AggregateRating` — consigliate**: `bestRating` (default 5), `worstRating` (default 1).

Formati negli esempi: JSON-LD, RDFa, Microdati.

---

## Dati strutturati per domande e risposte (`QAPage`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/qapage?hl=it

**A cosa serve / dove appare**
- Pagine con **una domanda seguita dalle relative risposte**; tipi `QAPage`, `Question`, `Answer` (+ `Comment`). Possono ottenere un risultato avanzato (es. query "Come faccio a rimuovere un cavo bloccato in una porta USB?"). Aiuta anche a generare uno **snippet** migliore; il contenuto delle risposte può comparire nel risultato di base se il risultato avanzato non viene mostrato.
- Nessuna limitazione di paese/lingua indicata.

**Norme relative ai contenuti**
- Usare solo se la pagina è in formato domanda→risposte e **gli utenti possono inviare risposte**.
- Validi: pagina di forum con risposte degli utenti a una singola domanda; pagina di assistenza prodotti con risposte degli utenti a una singola domanda.
- **Non validi**: **pagina FAQ scritta dal sito stesso** senza risposte alternative degli utenti; pagina prodotto con più domande e risposte; guida illustrativa, blog post o saggio che rispondono a una domanda.
- Non applicare `QAPage` a tutto il sito/forum se non tutte le pagine sono idonee. **Non usarlo per FAQ** o pagine con più domande: è per pagine incentrate su **una singola domanda**.
- Non usarlo a scopi pubblicitari. `Question` deve contenere l'intero testo della domanda, `Answer` l'intero testo della risposta. I commenti vanno in `comment`/`Comment`, non in `Answer`.
- Contenuti osceni, volgari, sessualmente espliciti, violenti, che promuovono attività pericolose/illegali o con linguaggio d'odio possono non essere mostrati.
- Le pagine Q&A didattiche (risposte a compiti) possono essere idonee al carosello "Domande e risposte didattiche" anche con un'unica risposta selezionata da esperti interni.

**Proprietà**
- `QAPage` — obbligatoria: `mainEntity` (`Question`). **Una sola** `QAPage` e **una sola** `Question` per pagina.
- `Question` — obbligatorie: `answerCount` (`Integer`; totale risposte anche se impaginate; 0 se nessuna; `answerCount` + `commentCount` = totale risposte di ogni tipo), `acceptedAnswer` **o** `suggestedAnswer` (almeno una per l'idoneità; domande senza risposte non idonee), `name` (testo completo della forma breve della domanda). Consigliate: `author` (+ `author.url` verso una pagina del profilo con markup `ProfilePage`), `comment`, `commentCount`, `dateModified`, `datePublished` (ISO 8601), `digitalSourceType` (`TrainedAlgorithmicMediaDigitalSource` = LLM; `AlgorithmicMediaDigitalSource` = processo algoritmico semplice; se assente si presume contenuto umano), `image` (niente segnaposto/icone/foto autore), `text` (forma estesa), `upvoteCount` (aggregato positivi meno negativi, es. 5-2=3), `video`.
- `acceptedAnswer`: risposta accettata (dall'autore della domanda, moderatore o sistema di voto; non per semplice ordinamento cronologico).
- `Answer` — obbligatoria: `text` (testo completo). Consigliate: `author`, `author.url`, `comment`, `commentCount`, `dateModified`, `datePublished`, `digitalSourceType`, `image`, `upvoteCount`, `url` (link diretto alla risposta, es. `#answer1`, vivamente consigliato), `video`.
- `Comment` — obbligatoria: `text`. Consigliate: `author`, `author.url`, `comment` (thread), `commentCount`, `dateModified`, `datePublished`, `digitalSourceType`, `image`, `video`.
- Formati negli esempi: JSON-LD, Microdati.

---

## Dati strutturati per programmi fedeltà (`MemberProgram`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/loyalty-program?hl=it

- **A cosa serve**: mostrare i vantaggi del programma fedeltà (prezzi per membri, punti) insieme a prodotti e schede informative.
- **Disponibilità**: Australia, Brasile, Canada, Francia, Germania, Messico, Regno Unito, Stati Uniti; desktop e mobile.
- **Dove**: `MemberProgram` nidificato in `Organization` (`hasMemberProgram`) nella pagina con dettagli amministrativi/norme. Vantaggi per singolo prodotto: `UnitPriceSpecification` in `Offer` con `validForMemberTier` e `membershipPointsEarned` (scheda commerciante).
- `MemberProgram` obbligatorie: `description`, `hasTiers` (almeno un `MemberProgramTier`), `name`. Consigliata: `url` (pagina di iscrizione; un solo URL; default URL della pagina).
- `MemberProgramTier` obbligatorie: `hasTierBenefit` (`TierBenefitLoyaltyPoints` → specificare anche `membershipPointsEarned`; `TierBenefitLoyaltyPrice`; nomi brevi ammessi), `name`. Consigliate: `hasTierRequirement` (`CreditCard`; `MonetaryAmount` = spesa minima; `UnitPriceSpecification` = tariffa periodica con `billingDuration`, `billingIncrement`, `unitCode` es. "MON"; oppure `Text`; se assente, adesione libera e gratuita), `membershipPointsEarned` (`QuantitativeValue`, punti per unità di valuta), `url` (uno solo).
- Alternativa: configurare il programma in **Google Merchant Center**; se presenti entrambi, **prevale Merchant Center**.

---

## Dati strutturati per risolutori matematici (`MathSolver`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/math-solvers?hl=it

- **A cosa serve**: indicare tipologie di problemi matematici risolvibili e link a procedure dettagliate; aspetto soggetto a modifiche. Nessuna limitazione di paese indicata (multilingua via `inLanguage`).
- **Linee guida tecniche**: markup sulla **home page**; Googlebot deve scansionare in modo efficiente; copie identiche su URL diversi → URL canonici; **vietati risolutori che richiedono login o paywall** per la soluzione del problema iniziale (contenuti aggiuntivi possono esserlo).
- **Contenuti**: niente contenuti promozionali celati (es. programmi di affiliazione); responsabilità di accuratezza su tipi di problemi e soluzioni; violazioni → azione manuale e rimozione dalla funzionalità.
- `MathSolver` obbligatorie: `potentialAction` (`SolveMathAction`), `potentialAction.mathExpression-input` (es. "required name=math_expression_string"; formati LaTeX, AsciiMath ecc.; derivate inviate come `(expr)'` o `d/dx expr`; integrali `\int expr` o `\int_{from}^{to} expr`; limiti `\lim expr` o `\lim_{x\rightarrow0} expr`), `url`, `usageInfo` (URL norme privacy), `potentialAction.target` (`EntryPoint` con `{math_expression_string}`). Consigliate: `inLanguage`, `assesses` (se usato con `HowTo`), `potentialAction.eduQuestionType`.
- `LearningResource` obbligatoria: `learningResourceType` con valore fisso **`Math Solver`** (`@type: ["MathSolver","LearningResource"]`).
- Tipi di problema (elenco non esaustivo): Absolute Value Equation, Algebra, Arc Length, Arithmetic, Biquadratic Equation, Calculus, Characteristic Polynomial, Circle, Derivative, Differential Equation, Distance, Eigenvalue, Eigenvector, Ellipse, Exponential Equation, Function, Function Composition, Geometry, Hyperbola, Inflection Point, Integral, Intercept, Limit, Line Equation, Linear Algebra, Linear Equation, Linear Inequality, Logarithmic Equation/Inequality, Matrix, Midpoint, Parabola, Parallel, Perpendicular, Polynomial Equation/Expression/Inequality, Quadratic Equation/Expression/Inequality, Radical Equation/Inequality, Rational Equation/Expression/Inequality, Slope, Statistics, System of Equations, Trigonometry.
- Nota: il file letto termina con la tabella dei tipi di problemi (nessuna sezione di risoluzione problemi).

---

## Dati strutturati per carosello di film (`Movie`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/movie?hl=it

- **Disponibilità**: carosello di film **solo su dispositivi mobili**. Rivendicare un film nella scheda informativa → verifica su Google; pulsante "Guarda" → Azioni multimediali.
- Struttura: pagina di riepilogo (`ItemList` con `ListItem` `position` + `url`) + pagine di dettaglio, oppure unica pagina elenco con `ListItem.item` di tipo `Movie`. Seguire anche le **linee guida Carosello**.
- Obbligatorie: `image` (URL o ImageObject; scansionabile/indicizzabile; formato **.jpg, .png o .gif**; alta risoluzione con proporzioni **6:9**; immagini con proporzioni molto diverse non idonee), `name`.
- Consigliate: `aggregateRating`, `dateCreated` (data di uscita), `director` (`Person`), `review`.
- Tecniche non ammesse → possibile azione manuale.

---

## Dati strutturati per contenuti in abbonamento e protetti da paywall (`CreativeWork`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/paywalled-content?hl=it

- **A cosa serve**: indicare i contenuti dietro paywall per distinguerli dal **cloaking** (violazione norme spam). Solo per contenuti che si vogliono scansionati e indicizzati.
- **Linee guida**: formati accettati **JSON-LD e Microdati**; non nidificare le sezioni di contenuto; `cssSelector` solo con selettori **`.class`**; se i contenuti non devono arrivare al browser, scegliere un paywall che non li serva; per paywall JavaScript lato client vedere le indicazioni JS. Violazioni → pagina potenzialmente non idonea (markup spam).
- **Procedura**: classe CSS su ogni sezione protetta → markup (es. `NewsArticle`) → `isAccessibleForFree: false` + `hasPart` (`WebPageElement`, `isAccessibleForFree: false`, `cssSelector: ".paywall"`); più sezioni = array in `hasPart`. Applicare a tutte le versioni (AMP e non AMP).
- **Tipi supportati**: `CreativeWork` o `Article`, `NewsArticle`, `Blog`, `Comment`, `Course`, `HowTo`, `Message`, `Review`, `WebPage`; ammessi più tipi (es. `["Article","LearningResource"]`).
- Obbligatoria: `isAccessibleForFree` (`Boolean`). Consigliate: `hasPart.cssSelector`, `hasPart.@type` = `WebPageElement`, `hasPart.isAccessibleForFree`.
- **AMP**: usare `amp-subscriptions`; endpoint di autorizzazione che concede accesso ai bot Google; stessi criteri di accesso bot per AMP e non AMP (altrimenti errori di contenuti non corrispondenti).
- **AI generativa**: AI Overview e AI Mode sono soggetti ai **controlli di anteprima** della Ricerca.
- Googlebot (e `Googlebot-News` se pertinente) devono accedere alla pagina; verifica con Controllo URL. Per escludere sezioni dagli snippet: attributo **`data-nosnippet`**; limitare lo snippet con meta robots **`max-snippet`**.

---

## Introduzione ai dati strutturati `Product`
Fonte: https://developers.google.com/search/docs/appearance/structured-data/product?hl=it

- I dati prodotto possono apparire in Ricerca, **Google Immagini** e **Google Lens** (prezzo, disponibilità, valutazioni, spedizione...).
- Due classi: **Snippet prodotto** (pagine dove non si può acquistare direttamente, es. recensioni editoriali con pro/contro) e **Schede del commerciante** (pagine dove si acquista; taglie, spedizione, resi). Sovrapposizione: le proprietà obbligatorie della scheda del commerciante rendono idonei anche agli snippet prodotto.
- Varianti → `ProductGroup`. Norme e-commerce da nidificare in `Organization`: resi (`MerchantReturnPolicy`), programma fedeltà (`MemberProgram`).
- Esperienze: snippet prodotto (risultato testuale arricchito), prodotti più apprezzati, scheda informativa Shopping, Google Immagini. Miglioramenti: valutazioni, pro e contro, spedizione, disponibilità, **riduzione di prezzo** (calcolata da Google sullo storico dei prezzi, non garantita), resi.
- Dati via markup e/o feed **Merchant Center** (schede gratuite); usarli entrambi massimizza l'idoneità; alcune esperienze combinano le fonti (es. prezzo dal feed se assente nel markup).

---

## Dati strutturati per snippet prodotto (`Product`, `Review`, `Offer`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/product-snippet?hl=it

- **A cosa serve**: risultato testuale con valutazioni, recensioni, prezzo, disponibilità. Per pagine di recensioni prodotto, recensioni editoriali con pro e contro, aggregatori di Shopping.
- **Linee guida tecniche**: solo pagine incentrate su **un singolo prodotto** (o varianti dello stesso), non pagine di categoria/elenco ("scarpe nel nostro negozio"); un URL distinto per **valuta**; `Car` non è automaticamente sottotipo di Product → usare `["Product","Car"]`; **pro e contro solo per pagine di recensioni editoriali** (non pagine del commerciante né recensioni dei clienti); consigliato mettere `Product` nell'**HTML iniziale**; il markup generato da **JavaScript** può rendere le scansioni Shopping meno frequenti e affidabili (problema per prezzo/disponibilità) → server con risorse sufficienti.
- **Contenuti vietati**: prodotti ampiamente vietati/regolamentati (armi, droghe ricreative, tabacco/sigarette elettroniche, giochi e scommesse).
- `Product` obbligatorie: `name` + **uno tra** `review`, `aggregateRating`, `offers` (il Test può avvisare se c'è solo `offers`). Consigliate: `aggregateRating`, `offers` (`Offer` o `AggregateOffer`; per la riduzione di prezzo serve `Offer`), `review` (nome recensore valido di `Person` o `Team`, es. "Recensori di CNET"; non "50% di sconto durante il Black Friday").
- **Pro e contro**: `positiveNotes`/`negativeNotes` (`ItemList` con `itemListElement` `ListItem` → `name` obbligatorio, `position` consigliato); obbligatorie almeno **due affermazioni** (positive/negative in qualsiasi combinazione). Disponibile in francese, giapponese, inglese, italiano, olandese, polacco, portoghese, spagnolo, tedesco, turco, in tutti i paesi con Ricerca Google.
- `Offer` obbligatoria: `price` o `priceSpecification.price` (per lo snippet prodotto c'è un esempio di prodotto disponibile senza pagamento; se presenti entrambi vince `offers.price`). Consigliate: `availability` (BackOrder, Discontinued, InStock, InStoreOnly, LimitedAvailability, OnlineOnly, OutOfStock, PreOrder, PreSale, SoldOut; nomi brevi ammessi), `priceCurrency` (ISO 4217; consigliata qui, obbligatoria per scheda commerciante → indicarla sempre), `priceValidUntil` (data passata → lo snippet potrebbe non comparire).
- `UnitPriceSpecification`: obbl. `price`; consigl. `priceCurrency`.
- `AggregateOffer` (offerte di più commercianti; **non** per varianti): obbl. `lowPrice` (separatore decimale `.`), `priceCurrency`; consigl. `highPrice`, `offerCount`.
- Search Console: report **Schede del commerciante** (pagine dove si acquista) e report **Snippet prodotto** (altre pagine prodotto: recensioni, aggregatori).

---

## Dati strutturati per schede del commerciante (`Product`, `Offer`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing?hl=it

- **A cosa serve**: idoneità a scheda informativa Shopping, Google Immagini, prodotti più apprezzati, snippet prodotto; prezzo, disponibilità, spedizione, resi.
- **Linee guida tecniche**: solo pagine dove **l'acquirente può acquistare** (non pagine con link ad altri siti venditori); Google può verificare i dati; pagine su singolo prodotto/varianti; URL distinto per valuta; `Car`+`Product`; `Product` nell'HTML iniziale consigliato; avvertenza sul markup generato con JavaScript (scansioni Shopping meno frequenti/affidabili). Linee guida aggiuntive: linee guida per le schede senza costi (Merchant Center). Contenuti vietati come per snippet prodotto.
- **Prezzi**: tre tipi — attivo (senza `priceType` né `validForMemberTier`), barrato (`priceType` = `StrikethroughPrice`, transitoriamente anche `ListPrice`), per membri (`validForMemberTier`); specifiche con entrambe le proprietà vengono **ignorate**. Durata promozione: `validFrom` + `validThrough`/`priceValidUntil` in ISO 8601 con ora e fuso (inizio ≤ fine; `priceValidUntil` non applicabile a `PriceSpecification`). Prezzo unitario con `referenceQuantity` (importante in UE, Nuova Zelanda, Australia).
- `Product` obbligatorie: `name`, `image` (scansionabile, formato supportato, min **50.000 pixel**, formati 16x9/4x3/1x1; preferibile sfondo bianco), `offers` (`Offer`, non `AggregateOffer`: il commerciante deve essere il venditore).
- `Product` consigliate: `aggregateRating`, `audience` (`PeopleAudience`: `suggestedGender` Male/Female/Unisex; `suggestedMaxAge`/`suggestedMinAge` mappati su valori fissi 0, 0.25, 1.0, 5.0, 13.0), `brand.name` (max un marchio), `category` (testo tipo prodotto < **750 caratteri** e/o `CategoryCode` con tassonomia Google e `codeValue`, separatore `>`), `color`, `description` (vivamente consigliata), `gtin`/`gtin8`/`gtin12`/`gtin13`/`gtin14`/`isbn` (numerici, non URL; `isbn` solo con `Book`+`Product`, preferibile ISBN-13), `hasAdultConsideration` (solo `SexualContentConsideration`), `hasCertification` (fino a **10**; `Certification` con `issuedBy` EC/European_Commission, ADEME, BMWK; `name` EPREL, Vehicle_CO2_Class, Vehicle_CO2_Class_Discharged_Battery; `certificationIdentification` o `certificationRating`; il vecchio `hasEnergyConsumptionDetails` è ancora supportato), `inProductGroupWithID`, `isVariantOf`, `material`, `mpn`, `pattern`, `review` (nome valido Person/Team), `size` (Text o `SizeSpecification` con `name`, `sizeGroup` max 2, `sizeSystem` AU/BR/CN/DE/Europe/FR/IT/JP/MX/UK/US), `sku` (un valore, senza spazi, preferibilmente ASCII), `subjectOf` (`3DModel` con `encoding.contentUrl` **.gltf/.glb**, solo glTF).
- `Offer` obbligatorie: `price`/`priceSpecification.price` (**prezzo > 0** per le schede del commerciante), `priceCurrency` (ISO 4217), `priceSpecification` (`UnitPriceSpecification`). Consigliate: `availability` (un valore), `hasMerchantReturnPolicy`, `itemCondition` (New/Refurbished/UsedCondition), `priceValidUntil`, `shippingDetails`, `url` (uno solo), `validFrom`, `validThrough`.
- `UnitPriceSpecification`: obbl. `price`, `priceCurrency`; consigl. `membershipPointsEarned` (beta), `priceType` (solo `StrikethroughPrice`; richiede anche il prezzo attivo), `referenceQuantity`, `validForMemberTier` (beta; riferimento via `@id` a un tier definito in `Organization` o in Merchant Center), `validFrom`, `validThrough`.
- `QuantitativeValue` per prezzo unitario: obbl. `unitCode` (UN/CEFACT o equivalenti; no `sheet`/`item`), `value`; consigl. `valueReference`.
- **Spedizione** `OfferShippingDetails` (facoltativo, ma se usato): obbl. `deliveryTime` (`ShippingDeliveryTime` con `handlingTime`, `transitTime`; uno solo), `shippingDestination` (`DefinedRegion`: `addressCountry` ISO 3166-1 alpha-2; `addressRegion` ISO 3166-2 solo AU, JP, US **oppure** `postalCode` solo AU, CA, US — mai entrambi), `shippingRate` (`value` o `maxValue` + `currency` uguale all'offerta; spedizione gratuita = `0`; niente simboli/separatori). Tempi: `QuantitativeValue` con `minValue`/`maxValue` interi non negativi e `unitCode` `DAY` o `d`.
- **Resi** `MerchantReturnPolicy` (prodotto): obbl. `applicableCountry` (fino a **50** paesi), `returnPolicyCategory` (FiniteReturnWindow → `merchantReturnDays` obbligatorio; NotPermitted; UnlimitedWindow). Consigl. `merchantReturnDays`, `returnFees` (FreeReturn, ReturnFeesCustomerResponsibility, ReturnShippingFees + `returnShippingFeesAmount`), `returnMethod` (ReturnAtKiosk, ReturnByMail, ReturnInStore), `returnShippingFeesAmount`. Se presenti sia livello organizzazione sia prodotto, **prevale il livello prodotto**.
- **Ordine di precedenza** spedizione/resi (dal più forte): feed prodotto Merchant Center → API Content for Shopping → impostazioni Merchant Center/Search Console → markup a livello prodotto → markup `Organization`. Alternativa: impostazioni a livello di account in Search Console.

---

## Dati strutturati per varianti di prodotto (`ProductGroup`, `Product`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/product-variants?hl=it

- **A cosa serve**: raggruppare varianti (taglia, colore, materiale, motivo) con `ProductGroup` + `variesBy`, `hasVariant`, `productGroupID`; idoneità alle info varianti nelle schede del commerciante; riduce duplicazioni.
- **Approcci**: sito a pagina singola (varianti via parametri di query; il markup non cambia dinamicamente) — varianti nidificate in `ProductGroup` (approccio consigliato) o separate con `isVariantOf`; sito a più pagine — `ProductGroup` ripetuto completo su ogni pagina, senza URL canonico, con riferimenti `url` alle varianti dell'altra pagina.
- **Linee guida tecniche**: ID univoco per ogni variante (`sku`/`gtin`); ID univoco del gruppo (`productGroupID` o `inProductGroupWithID`); includere anche le proprietà obbligatorie di scheda commerciante/snippet prodotto; pagina singola → un solo URL canonico per il `ProductGroup` (URL base senza variante); più pagine → markup completo e autonomo per pagina; ogni variante **preselezionabile con URL distinto** (immagine, prezzo, disponibilità corretti, aggiunta al carrello); `Product` nell'HTML iniziale; avvertenza JavaScript come sopra.
- `ProductGroup` obbligatoria: `name`. Consigliate: `aggregateRating`, `brand`/`brand.name`, `description`, `hasAdultConsideration`, `hasVariant`, `productGroupID` (deve coincidere con `inProductGroupWithID` se forniti entrambi), `review`, `url` (solo siti a pagina singola), `variesBy` (`https://schema.org/color`, `size`, `suggestedAge`, `suggestedGender`, `material`, `pattern`).

---

## Dati strutturati per norme sui resi del commerciante (`MerchantReturnPolicy`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/return-policy?hl=it

- **A cosa serve**: mostrare le norme sui resi insieme ai prodotti e nelle schede informative; link alla pagina norme o dettagli (condizioni, metodi, commissioni, rimborsi).
- **Dove**: norme standard in `Organization` via `hasMerchantReturnPolicy`, su **una singola pagina** che descrive le norme (non serve su ogni pagina). Eccezioni per singoli prodotti in `Offer` (sottoinsieme di proprietà).
- **Obbligatorie (scegliere un'opzione)**: *Opzione A* `applicableCountry` (ISO 3166-1 alpha-2, fino a **50** paesi) + `returnPolicyCategory` (`MerchantReturnFiniteReturnWindow` → `merchantReturnDays` obbligatorio; `MerchantReturnNotPermitted`; `MerchantReturnUnlimitedWindow`); *Opzione B* `merchantReturnLink` (URL della pagina norme, anche di terze parti).
- **Consigliate** (finestra finita/illimitata): `merchantReturnDays`, `returnFees` (FreeReturn, ReturnFeesCustomerResponsibility, ReturnShippingFees), `returnMethod` (ReturnAtKiosk, ReturnByMail, ReturnInStore), `returnShippingFeesAmount` (solo con ReturnShippingFees), `customerRemorseReturnFees`, `customerRemorseReturnLabelSource`, `customerRemorseReturnShippingFeesAmount`, `itemCondition` (Damaged/New/Refurbished/UsedCondition, più valori), `itemDefectReturnFees`, `itemDefectReturnLabelSource`, `itemDefectReturnShippingFeesAmount`, `refundType` (ExchangeRefund, FullRefund, StoreCreditRefund), `restockingFee` (`Number` = percentuale, `MonetaryAmount` = fisso), `returnLabelSource` (ReturnLabelCustomerResponsibility, ReturnLabelDownloadAndPrint, ReturnLabelInBox), `returnPolicyCountry` (paese di spedizione del reso, fino a 50).
- **Variazioni stagionali**: obbligatoria `returnPolicySeasonalOverride` (`MerchantReturnPolicySeasonalOverride`) con `returnPolicyCategory`; consigliate `startDate`, `endDate`, `merchantReturnDays`.
- **Alternativa**: Merchant Center o Search Console (livello account). **Precedenza** (dal più forte): API Content for Shopping → Merchant Center/Search Console → markup scheda commerciante a livello prodotto → markup a livello organizzazione. Es.: con markup + impostazioni Search Console, Google usa solo Search Console.

---

## Dati strutturati per norme di spedizione del commerciante (`ShippingService`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/shipping-policy?hl=it

- **A cosa serve**: mostrare le norme di spedizione con i prodotti e nelle schede informative (costi e tempi in base a peso, dimensioni, destinazione, valore ordine).
- **Dove**: `ShippingService` in `Organization` via `hasShippingService`, su una singola pagina dedicata; eccezioni di prodotto con `OfferShippingDetails` in `Offer` (`shippingDetails`, sottoinsieme di proprietà).
- `ShippingService` obbligatoria: `shippingConditions` (più condizioni ammesse; se ne valgono più, Google usa il **costo più basso** e, a parità, la **velocità maggiore**). Consigliate: `name`, `description`, `fulfillmentType` (`FulfillmentTypeDelivery` default, `FulfillmentTypeCollectionPoint`), `handlingTime` (`ServicePeriod`), `validForMemberTier` (beta; serve anche almeno un servizio standard per non membri).
- `ServicePeriod` (elaborazione): `businessDays`, `cutoffTime` (ISO 8601 con fuso, es. "23:30:00-05:00"; dopo l'orario limite +1 giorno), `duration` (`QuantitativeValue`: `value` oppure `maxValue` + `unitCode` `DAY`/`d`; `minValue` facoltativo; interi non negativi; con `value` non indicare min/max). Per i tempi di transito `cutoffTime` non si usa; `businessDays` non serve se lun-sab.
- `ShippingConditions` (consigliate): `doesNotShip` (Boolean), `numItems`, `orderValue` (`MonetaryAmount` con `currency` obbligatoria, `minValue` default 0, `maxValue` default infinito), `shippingDestination`, `shippingOrigin` (`DefinedRegion`), `seasonalOverride` (`OpeningHoursSpecification` con almeno `validFrom` o `validThrough`), `shippingRate` (`MonetaryAmount` con `value` (0 = gratis) o `maxValue` + `currency`; oppure `ShippingRateSettings` con `orderPercentage` o `weightPercentage` tra 0 e 1; solo se `doesNotShip` assente/false), `transitTime` (`ServicePeriod`), `weight` (`QuantitativeValue`, `unitCode` `LBR` o `KGM`; per numItems `H87` o omesso). Senza destinazione = valide per tutto il mondo.
- `DefinedRegion`: obbl. `addressCountry` (ISO 3166-1 alpha-2); consigl. `addressRegion` (ISO 3166-2, solo AU, JP, US) o `postalCode` (solo AU, CA, US) — non entrambi.
- **Precedenza**: API Content for Shopping → Merchant Center/Search Console → markup prodotto → markup organizzazione.

---

## Dati strutturati per ricette (`Recipe`, `HowTo`, `ItemList`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/recipe?hl=it

- **Dove appare**: risultati della Ricerca e Google Immagini; miglioramento "carosello host delle ricette" con `ItemList`. Nessuna limitazione di paese indicata.
- **Linee guida**: violazioni → niente risultato avanzato ma i contenuti restano nella Ricerca. `Recipe` solo per la preparazione di un piatto ("scrub viso", "idee per feste" non validi). Per carosello/griglia: `ItemList` + pagina di riepilogo con tutte le ricette.
- Obbligatorie: `image` (piatto completato; min 50.000 pixel, 16x9/4x3/1x1; non influisce sull'immagine del risultato di testo), `name`.
- Consigliate: `aggregateRating` (recensore singolo con nome valido), `author` (best practice autori), `cookTime` + `prepTime` (ISO 8601, sempre insieme) o `totalTime`, `datePublished`, `description`, `keywords` (separate da virgole, non duplicare categoria/cucina), `nutrition.calories` (richiede `recipeYield`), `recipeCategory`, `recipeCuisine`, `recipeIngredient` (solo testo necessario), `recipeInstructions` (`HowToStep` consigliato; `HowToSection` solo per ricette con sezioni; testo semplice viene suddiviso automaticamente; niente "Passaggio 1", "Guarda il video"), `recipeYield`, `video`.
- `HowToSection`: obbl. `itemListElement` (`HowToStep`), `name`; non usarlo per ricette diverse dello stesso piatto (usare più `Recipe`). `HowToStep`: obbl. `itemListElement` (`HowToDirection`/`HowToTip`) o `text`; consigl. `image` (.jpg/.png/.gif), `name` (descrittivo, non "Passaggio 1"), `url`, `video` (`VideoObject` o `Clip`). `HowToDirection`/`HowToTip`: obbl. `text`.
- `ItemList` (carosello host): obbl. `itemListElement` (`ListItem`), `ListItem.position`, `ListItem.url` (URL canonico univoco).

---

## Dati strutturati per app software (`SoftwareApplication`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/software-app?hl=it

- **A cosa serve**: migliorare la visualizzazione dei dettagli di un'app (valutazione, descrizione, link). Nessuna limitazione di paese indicata. Violazioni → azione manuale.
- Obbligatorie: `name`; `offers.price` (`Offer`; app gratuita → `0`; se > 0 consigliato `offers.priceCurrency`); **una tra** `aggregateRating` e `review` (secondo linee guida snippet recensione).
- Consigliate: `applicationCategory` (valori supportati: GameApplication, SocialNetworkingApplication, TravelApplication, ShoppingApplication, SportsApplication, LifestyleApplication, BusinessApplication, DesignApplication, DeveloperApplication, DriverApplication, EducationalApplication, HealthApplication, FinanceApplication, SecurityApplication, BrowserApplication, CommunicationApplication, DesktopEnhancementApplication, EntertainmentApplication, MultimediaApplication, HomeApplication, UtilitiesApplication, ReferenceApplication), `operatingSystem` (es. "Windows 7", "OSX 10.6", "Android 1.6").
- Sottotipi supportati: `MobileApplication`, `WebApplication`. Solo `VideoGame` → **nessun** risultato avanzato; usare `VideoGame` insieme a un altro tipo.
- Formati negli esempi: JSON-LD, RDFa, Microdati.

---

## Dati strutturati Speakable (`Article`, `WebPage`) — BETA
Fonte: https://developers.google.com/search/docs/appearance/structured-data/speakable?hl=it

- **Stato**: **beta**, requisiti soggetti a modifiche.
- **A cosa serve**: indicare le sezioni adatte alla sintesi vocale (TTS); l'Assistente Google le usa per rispondere a richieste di notizie sugli smart speaker (fino a **tre articoli**, attribuisce la fonte e invia l'URL al telefono).
- **Disponibilità**: solo utenti negli **Stati Uniti** con Google Home in **inglese** ed editori con contenuti in inglese.
- **Linee guida tecniche**: non marcare contenuti confusi in contesto solo vocale (dateline, didascalie, attribuzioni della fonte); concentrarsi sui punti chiave, non sull'intero articolo.
- **Contenuti**: titoli/riassunti concisi; riscrivere l'attacco in frasi singole; circa **20-30 secondi** per sezione (2-3 frasi).
- Proprietà: `speakable` ripetibile con `cssSelector` **o** `xPath` (mai entrambi).
- Troubleshooting: comandi vocali di prova ("Quali sono le ultime notizie su $topic?" ecc.); il ranking è algoritmico.

---

## Dati strutturati per case vacanze (`VacationRental`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/vacation-rental?hl=it

- **Accesso limitato**: per proprietari che hanno già un **Technical Account Manager** Google e accesso a **Hotel Center**; modulo di interesse (non garantisce l'invito al programma early adopter); criteri di idoneità e passaggi aggiuntivi. Seguire le **norme sulle case vacanze** + generali. Violazioni → azione manuale.
- Obbligatorie: `containsPlace` (`Accommodation`), `containsPlace.occupancy` + `.value` (ospiti max), `identifier` (stabile, indipendente dai contenuti, uguale tra lingue), `image` (almeno **8 foto**, almeno una di camera da letto, bagno e area comune), `latitude`/`longitude` (o `geo.*`, almeno **5 cifre decimali**), `name`.
- Consigliate: `additionalType` (Apartment, Bungalow, Cabin, Chalet, Cottage, Gite, HolidayVillageRental, House, Villa, VacationRental), `address` (indirizzo fisico completo; caselle postali non valide) con sottoproprietà, `aggregateRating`, `brand`, `checkinTime`, `checkoutTime` (ISO 8601, es. `14:30:00+08:00`), `containsPlace.additionalType` (EntirePlace, PrivateRoom, SharedRoom), `containsPlace.amenityFeature` (valori in **inglese**: booleani ac, airportShuttle, balcony, beachAccess, childFriendly, crib, elevator, fireplace, freeBreakfast, gymFitnessEquipment, heating, hotTub, instantBookable, ironingBoard, kitchen, microwave, outdoorGrill, ovenStove, patio, petsAllowed, pool, privateBeachAccess, selfCheckinCheckout, smokingAllowed, tv, washerDryer, wheelchairAccessible, wifi; non booleani internetType, parkingType, poolType, licenseNum), `containsPlace.bed` (`numberOfBeds`, `typeOfBed`), `containsPlace.floorSize` (FTK/SQFT o MTK/SQM), `numberOfBathroomsTotal` (convenzione RESO, es. 2,5), `numberOfBedrooms`, `numberOfRooms`, `description`, `knowsLanguage` (BCP 47), `review` (**`review.datePublished` obbligatorio** per case vacanze; `review.contentReferenceTime` obbligatorio per schede in **Francia**).

---

## Dati strutturati per i video (`VideoObject`, `Clip`, `BroadcastEvent`)
Fonte: https://developers.google.com/search/docs/appearance/structured-data/video?hl=it

- **A cosa serve / dove appare**: influenzare descrizione, miniatura, data, durata nei risultati video; aiuta Google a trovare il video. Posizioni: pagina principale dei risultati, modalità Video, Google Immagini, **Discover**. Markup da mettere sulle **pagine di visualizzazione** (dove il video si guarda).
- **Funzionalità**: badge **DAL VIVO** (`BroadcastEvent`, per qualsiasi video pubblico in live streaming; usare **API Indexing** a inizio/fine streaming e a ogni modifica; l'API supporta solo video in live streaming); **Momenti chiave**: rilevati automaticamente o indicati con `Clip` (tutte le lingue) o `SeekToAction` (cinese, coreano, francese, giapponese, inglese, italiano, olandese, portoghese, russo, spagnolo, tedesco, turco) o timestamp nella descrizione YouTube (tutte le lingue). Disattivare i momenti chiave: meta tag **`nosnippet`**.
- **Linee guida**: Nozioni di base + linee guida generali + **requisiti di indicizzazione dei video**; tecniche non ammesse → azione manuale. Live: niente linguaggio volgare/offensivo. `Clip`/`SeekToAction`: URL con deep link a un punto (es. `?t=30`), `VideoObject` su pagina dove si può guardare il video, durata totale **almeno 30 secondi**, proprietà obbligatorie `VideoObject` presenti, niente due clip con stesso inizio sulla stessa pagina; per `SeekToAction` Google deve poter recuperare il file video. Timestamp YouTube: formato `[hour]:[minute]:[second]`, etichetta sulla stessa riga, un timestamp per riga, ordine cronologico, etichetta di almeno una parola.
- `VideoObject` obbligatorie: `name` (univoco per video), `thumbnailUrl` (miniatura univoca, linee guida miniature), `uploadDate` (ISO 8601 con fuso orario consigliato; altrimenti fuso di Googlebot).
- `VideoObject` consigliate: `contentUrl` (URL dei byte del file video, modo più efficace; non la pagina), `creator`/`author` (+ `name` o `alternateName`, `url` verso profilo/home page), `description` (univoca; tag HTML ignorati), `duration` (ISO 8601, es. `PT00H30M5S`), `embedUrl` (URL del player, tipicamente `src` dell'embed; alternativa a `contentUrl`), `expires` (solo se scade), `hasPart` (`Clip`), `ineligibleRegion` o `regionsAllowed` (ISO 3166-1 a 2 o 3 lettere), `interactionStatistic` (`WatchAction`, `LikeAction`, `CommentAction`, `ShareAction`; dal 2019 preferito a `interactionCount`), `publication` (`BroadcastEvent`). Verifica di Googlebot via **ricerca DNS inversa** per proteggere i file.
- `BroadcastEvent` (per badge DAL VIVO): `publication`, `publication.endDate` (da fornire a fine diretta; approssimativo se ignoto), `publication.isLiveBroadcast` = true, `publication.startDate`.
- `Clip`: obbl. `name`, `startOffset` (secondi), `url` (stesso percorso del video con parametro del tempo); consigl. `endOffset`.
- `SeekToAction`: obbl. `potentialAction` con `startOffset-input` = "required name=seek_to_second_number" e `target` con segnaposto `{seek_to_second_number}`. Usare `Clip` se si vogliono definire i momenti chiave manualmente.

---

# Implicazioni per la skill SEO

## (a) Tipi da usare per i due casi d'uso

**Portfolio / personal brand di uno sviluppatore (target recruiter)**
- **`ProfilePage`** sulla pagina "Chi sono"/home profilo: caso d'uso esplicitamente valido ("pagina 'Chi sono' su un sito di blog"; la pagina deve riguardare **una singola persona affiliata al sito**). Attenzione: la doc indica come non valida la "home page principale di un negozio" perché contiene molte informazioni non di profilo → se la home del portfolio è una pagina mista (progetti, blog, servizi), preferire una pagina "Chi sono" dedicata per `ProfilePage`.
  - Obbligatorie: `mainEntity` (`Person`) con `name`.
  - Consigliate: `dateCreated`, `dateModified` (ISO 8601); su `Person`: `alternateName` (es. handle GitHub), `description` (qualifiche pertinenti, es. ruolo/stack), `identifier`, `image` (foto reale, niente segnaposto; scansionabile; ≥ 50.000 px; 16x9/4x3/1x1), `sameAs` (GitHub, LinkedIn, altri profili), `interactionStatistic`/`agentInteractionStatistic` solo se il sito ha davvero follower/post **sulla piattaforma stessa** (per un portfolio di solito non applicabile: non inserire follower di altri social).
  - Se la pagina elenca articoli/progetti recenti: `hasPart` con `Article` + `author: {"@id": "#main-author"}`.
- **`Organization`**: utile solo se lo sviluppatore opera con un brand/ditta; nessuna proprietà obbligatoria. Se presente: `name`/`alternateName` coerenti con il **nome del sito**, `url`, `logo` (≥ 112x112 px, leggibile su sfondo bianco), `sameAs`, `email`, `vatID` se c'è partita IVA (indicatore di fiducia).
- **`VideoObject`** se ci sono demo video ospitate sul sito (obbl. `name`, `thumbnailUrl`, `uploadDate`).
- **`SoftwareApplication`** (`WebApplication`/`MobileApplication`) per un'app pubblicata, **solo** se c'è una valutazione/recensione reale: obbligatori `name`, `offers.price` (0 se gratis) e `aggregateRating` o `review` → in assenza di recensioni autentiche non è idoneo al risultato avanzato.
- **Non usare** `Review`/`AggregateRating` per testimonianze di clienti/colleghi sul proprio sito (vedi errori comuni). **Non usare** `QAPage` per una sezione FAQ scritta dall'autore.

**Professionista/consulente locale + online (es. orientatrice di carriera)**
- **`LocalBusiness`** (sottotipo più specifico disponibile; più tipi in array `@type`, **non** `additionalType`) sulla pagina con le informazioni dell'attività (contatti/Chi siamo o home). Una entità per **ogni sede**.
  - Obbligatorie: `name`, `address` (`PostalAddress` il più completo possibile: `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`).
  - Consigliate: `telephone` (con prefisso internazionale), `url` (URL della sede, funzionante), `geo.latitude`/`geo.longitude` (≥ 5 decimali), `openingHoursSpecification` (`dayOfWeek`, `opens`, `closes`, `validFrom`/`validThrough` per chiusure stagionali), `priceRange` (< 100 caratteri), `image`; + campi di `Organization` (`logo`, `sameAs`, `email`, `description`, `vatID`, `contactPoint`).
  - `aggregateRating`/`review` **solo** se il sito raccoglie recensioni su **altre** attività: per il sito della professionista stessa le stelle **non** sono idonee (recensioni self-serving).
- **`Organization`** in alternativa/aggiunta se l'attività è prevalentemente online (nessun obbligo; home o pagina "Chi siamo", non su tutte le pagine).
- **`ProfilePage`** per la pagina biografica della professionista (`mainEntity` `Person`, `description` con qualifiche, `sameAs`).
- **`VideoObject`** per webinar/video ospitati; `BroadcastEvent` per eventuali dirette.
- Corsi/eventi: pertinenti `Course`/`Event` (fuori da questo gruppo; qui citati solo come tipi recensibili e nella galleria).

## (b) Controlli automatici per un audit dei dati strutturati
1. **Presenza e formato**: rilevare JSON-LD/Microdati/RDFa; preferire JSON-LD; JSON valido e analizzabile (report "dati strutturati non analizzabili").
2. **Accessibilità a Googlebot**: pagine con markup non bloccate da robots.txt, `noindex`, login; immagini (`logo`, `image`, `thumbnailUrl`) scansionabili e indicizzabili.
3. **Proprietà obbligatorie per tipo** (es. `LocalBusiness`: `name`+`address`; `ProfilePage`: `mainEntity`+`name`; `Review`: `author`, `itemReviewed` (se non nidificata), `reviewRating.ratingValue`; `AggregateRating`: `ratingValue` + `ratingCount` o `reviewCount`; `VideoObject`: `name`, `thumbnailUrl`, `uploadDate`; `SoftwareApplication`: `name`, `offers.price`, rating/review; `Product` snippet: `name` + uno tra review/aggregateRating/offers; scheda commerciante: `name`, `image`, `offers` con prezzo > 0 e `priceCurrency`).
4. **Valori e limiti numerici**: `priceRange` < 100 caratteri; `geo` ≥ 5 decimali; `author.name` < 100 caratteri e nome plausibile; `logo` ≥ 112x112 px; immagini ≥ 50.000 px; `ratingValue` con punto decimale e coerente con `bestRating`/`worstRating` (default 5/1); `telephone` con prefisso paese; `addressCountry` ISO 3166-1 alpha-2; date ISO 8601; `priceCurrency` ISO 4217; `priceValidUntil` non nel passato; durata video ≥ 30 s per Clip.
5. **Tipo più specifico**: segnalare `LocalBusiness`/`Organization` generici quando esiste un sottotipo più adatto; segnalare uso di `additionalType` su `LocalBusiness` (non supportato).
6. **Coerenza markup ↔ contenuto visibile**: ogni dato marcato (nome, indirizzo, orari, recensioni, valutazione aggregata, prezzi) deve comparire nel corpo HTML visibile; nessun contenuto nascosto.
7. **Recensioni self-serving**: se `Review`/`AggregateRating` hanno come `itemReviewed` (o elemento padre) la stessa `Organization`/`LocalBusiness` proprietaria del sito, o provengono da widget incorporati (Google, Facebook) → segnalare come non idonee/rischio azione manuale.
8. **Coerenza identità**: `Organization.name`/`alternateName` uguali al nome del sito; `url` corrispondente al dominio; `sameAs` validi; un'unica `ProfilePage` con `mainEntity` singolo per pagina; `@id` per collegare entità (es. `author` → `#main-author`).
9. **Località del markup**: `Organization` su home o "Chi siamo" (non obbligatorio ovunque); markup della pagina sulla pagina che descrive; pagine duplicate con stesso markup della canonica.
10. **Usi impropri**: `QAPage` su FAQ scritte dal sito o pagine con più domande; `Product` su pagine categoria; `Recipe` su contenuti non culinari; immagini segnaposto in `image` di `ProfilePage`/`Answer`.
11. **Validazione esterna**: Test dei risultati avanzati + Controllo URL (HTML renderizzato); monitoraggio Search Console (report stato risultati avanzati, Azioni manuali, Rendimento con filtro aspetto).

## (c) Note per SPA JavaScript / Angular
- Google accetta dati strutturati generati con JavaScript (rimando alla guida "generare dati strutturati con JavaScript"), ma va verificato con **Controllo URL** / **Test dei risultati avanzati** che il markup sia presente nell'**HTML renderizzato**.
- Per `Product` Google consiglia di inserire il markup nell'**HTML iniziale**: il markup generato dinamicamente può rendere le scansioni di Shopping **meno frequenti e affidabili** e richiede risorse server adeguate. Per estensione prudenziale (non detto esplicitamente per altri tipi), su Angular è preferibile prerender/SSR (es. Angular SSR/prerendering) che emetta il JSON-LD nell'HTML servito, soprattutto per `LocalBusiness`/`Organization`/`ProfilePage` che non cambiano spesso.
- In una SPA con routing client-side ogni route deve avere il **proprio** markup coerente con il contenuto di quella vista (principio di località); evitare di lasciare nel DOM il JSON-LD della route precedente (rischio di markup non rappresentativo della pagina).
- Paywall/contenuti riservati via JavaScript lato client: seguire le indicazioni JS dedicate; `cssSelector` solo con classi.
- Se dopo un rilascio calano gli elementi validi senza aumento di quelli non validi, probabile che il markup non venga più incorporato (tipico di regressioni nel rendering/SSR) → Controllo URL.

## (d) Errori comuni da evitare
- **Recensioni auto-pubblicate (self-serving)**: stelle su `LocalBusiness`/`Organization` relative alla propria attività, sia nel markup sia tramite widget di terze parti incorporati (recensioni Google, Facebook) → non idonee; recensioni/valutazioni non di utenti reali → possibile **azione manuale**.
- Aggregare recensioni da **altri siti**; recensioni false o **incentivate non dichiarate**; recensioni curate da editor umani per attività locali.
- Marcare contenuti **non visibili** o diversi da quelli della pagina; informazioni obsolete.
- Usare `QAPage` per **FAQ** scritte dal sito; usare `ProfilePage` su home page miste/negozio.
- Immagini **segnaposto/icone** in `image` di profili; logo non leggibile su sfondo bianco o < 112 px.
- `priceRange` ≥ 100 caratteri; coordinate con meno di 5 decimali; telefono senza prefisso internazionale; `ratingValue` con virgola decimale nel markup.
- `additionalType` su `LocalBusiness` invece di array in `@type`.
- `name`/`alternateName` di `Organization` diversi dal nome del sito; `sameAs` verso profili non propri (impersonificazione vietata).
- Bloccare con robots.txt/`noindex` le pagine con markup o le immagini referenziate.
- Ricordare: un'azione manuale sui dati strutturati fa **perdere i risultati avanzati** ma **non influisce sul ranking**; Google **non garantisce** la visualizzazione anche con markup valido.

