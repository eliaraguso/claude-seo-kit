# Dati strutturati

> Aggiornato al 2026-10-03. Serve a scegliere, generare e validare JSON-LD per qualsiasi sito (nuovo o esistente, qualsiasi framework).
> Fonti: documentazione Google Search Central (copia italiana scaricata il 2026-10-03), blog Google 2024–2026, sintesi Search Engine Journal (SEJ, secondaria).
> Legenda: **[G]** fatto dalla documentazione Google · **[G-blog]** annuncio sul blog Google · **[D]** deduzione operativa (non testo Google) · **[T]** fonte terza/opinione · **⚠** affermazione da non trasformare in raccomandazione.
> Regola d'oro: Google non garantisce mai un risultato avanzato, anche con markup valido [G]. Prima di proporre un tipo, controllare la sezione "Tipi ritirati" e, per novità successive a questa data, il changelog `https://developers.google.com/search/updates`.

## Indice
- [Regole generali (Google)](#regole-generali-google)
- [Matrice di scelta per tipo di sito](#matrice-di-scelta-per-tipo-di-sito)
- [Schede per tipo](#schede-per-tipo)
- [Tipi ritirati o non disponibili in Italia/italiano](#tipi-ritirati-o-non-disponibili-in-italiaitaliano)
- [Controlli per l'audit](#controlli-per-laudit)
- [Note per SPA/JavaScript](#note-per-spajavascript)
- [Cosa dicono le fonti terze](#cosa-dicono-le-fonti-terze)

## Regole generali (Google)

### Formati
- Tre formati supportati: **JSON-LD (consigliato)**, Microdati, RDFa. Tutti validi se corretti; JSON-LD è preferito perché più facile da gestire su larga scala e meno soggetto a errori [G].
- JSON-LD va in `<script type="application/ld+json">`, in `<head>` o `<body>`; non si mescola al testo visibile. Google legge anche il JSON-LD **inserito dinamicamente** (JavaScript, widget CMS) [G].
- Eccezione: per `DiscussionForumPosting` Google consiglia Microdati/RDFa (evita di duplicare lunghi testi), ma JSON-LD resta supportato [G].
- Vocabolario: quasi sempre schema.org, ma **il riferimento per Google è Search Central, non schema.org**; molte proprietà schema.org non servono a Google [G]. `data-vocabulary.org` non è più idoneo [G].
- `@context`: `https://schema.org`. Un solo valore per campo quando la proprietà è un identificatore (es. GTIN): niente liste separate da virgole [G, Office Hours 2022].
- CMS (WordPress, Wix, Shopify…): usare le impostazioni SEO o un plug-in invece di scrivere a mano [G]. [D] Prima di aggiungere markup manuale, verificare che il CMS/plug-in non ne generi già (evitare doppioni contraddittori).

### Obbligatorie e consigliate
- Tutte le proprietà **obbligatorie** servono per l'idoneità; le **consigliate** aumentano la probabilità di visualizzazione [G].
- Meglio **poche consigliate complete e accurate** che molte incomplete o errate [G].
- Google può fare un uso generale di `sameAs` e di altri dati schema.org non documentati, anche per funzionalità future [G].

### Contenuto visibile e norme di qualità
- Il markup descrive **la pagina in cui si trova**: niente pagine vuote create solo per i dati strutturati, niente markup di informazioni **non visibili** all'utente, anche se vere [G].
- Norme sulla qualità (non verificabili da strumenti; violarle può bloccare i risultati avanzati o far marcare il markup come spam) [G]:
  - rispettare le norme sullo spam; informazioni **aggiornate**; contenuti **originali** (tuoi o dei tuoi utenti);
  - niente contenuti irrilevanti o fuorvianti (es. **recensioni fittizie**); niente impersonificazione di persone/organizzazioni né falsa rappresentazione di proprietà, affiliazione o scopo;
  - **pertinenza**: il markup rappresenta fedelmente la pagina (esempi di errori: streaming sportivo marcato come evento locale; istruzioni di falegnameria marcate come ricetta);
  - **località**: markup sulla pagina che descrive; con pagine duplicate, **stesso markup su tutte**, non solo sulla canonica;
  - **specificità**: tipo e proprietà schema.org **più specifici** applicabili;
  - **immagini**: pertinenti alla pagina, URL scansionabili e indicizzabili.
- Più elementi in una pagina: si possono **nidificare** (un elemento principale con gli altri dentro) o dichiarare **separati** (array JSON-LD). Includere sempre il **tipo principale** che rispecchia lo scopo della pagina; se si marcano più recensioni, marcarle **tutte** quelle visibili [G].
- Accesso: non bloccare le pagine con markup con robots.txt, `noindex` o login [G].

### Azioni manuali
- Un problema di dati strutturati può causare un'**azione manuale**: la pagina perde l'idoneità ai risultati avanzati, **ma il ranking non cambia**; il markup della pagina viene **ignorato** [G].
- Si verifica nel report Azioni manuali di Search Console; dopo la correzione si chiede la riconsiderazione [G].
- Il Test dei risultati avanzati **non rileva** problemi di spam o di norme (solo sintassi e campi) [G].

### Generato con JavaScript
- Metodi: Google Tag Manager, JavaScript personalizzato, rendering lato server [G].
- Google elabora i dati strutturati **presenti nel DOM al momento del rendering** [G].
- Con GTM usare **variabili che leggono la pagina** invece di copiare i dati nel tag (la duplicazione crea discrepanze) [G].
- `Product`: il markup generato via JS può rendere le scansioni Shopping **meno frequenti e affidabili**; Google consiglia `Product` nell'**HTML iniziale** [G]. Dettagli in [Note per SPA/JavaScript](#note-per-spajavascript).

### Test e validazione
| Strumento | Quando | Note |
|---|---|---|
| Test dei risultati avanzati (`search.google.com/test/rich-results`) | Sviluppo e verifica | Usare l'input **via URL** (l'input via codice ha limiti JS, es. CORS) [G]. Non supporta i nomi dei siti né i tipi ritirati [G]. |
| Validatore schema.org (`validator.schema.org`) | Sintassi di tipi non coperti dal Test (es. `WebSite` per il nome del sito) | [G] lo indica per i nomi dei siti. |
| Controllo URL (Search Console) | Dopo il deploy | Verifica HTML renderizzato, blocchi robots/noindex/login; richiesta di nuova scansione (giorni) [G]. |
| Report sullo stato dei risultati avanzati, "Dati strutturati non analizzabili", Azioni manuali | Post-deploy e dopo ogni nuovo template | Aumento di errori = template rotto; **calo dei validi senza aumento degli invalidi** = markup non più incorporato [G]. |
| Report Rendimento (filtro aspetto/URL) | Misura dell'effetto | Test prima/dopo su pagine stabili per alcuni mesi [G]. |
- Gli errori "critici" del Test vanno corretti; i "non critici" migliorano la qualità ma non servono per l'idoneità [G]. Sitemap consigliata per segnalare le modifiche [G].

### @id e grafo
- Google: se elementi separati sono collegati (es. ricetta e video), usare **`@id`** per collegarli, altrimenti Google potrebbe non capire la relazione [G]. L'esempio `ProfilePage` usa `"@id": "#main-author"` per collegare l'autore ai suoi articoli [G]. In `BreadcrumbList`, `item` può essere un oggetto con `@id` [G].
- In home un **solo nodo `WebSite`**: nidificare lì le proprietà (nome del sito incluso) invece di creare blocchi multipli [G, Office Hours 2022 + doc nomi dei siti].
- [D] Convenzione consigliata: `@id` **assoluti e stabili** per entità, riusati in tutto il sito: `https://example.com/#website`, `https://example.com/#organization`, `https://example.com/chi-sono/#person`. Altre pagine referenziano (`"author": {"@id": ".../#person"}`) invece di ridefinire l'entità con dati diversi.
- [D] Un array JSON-LD (documentato da Google) e `@graph` (sintassi JSON-LD standard, non citata nella doc letta) sono equivalenti; scegliere uno stile per sito e non mescolare entità duplicate con `@id` diversi per la stessa cosa.

## Matrice di scelta per tipo di sito
Gli archetipi corrispondono a `knowledge/archetypes.md`. "Rich result in Italia" = esiste una funzionalità visibile per utenti italiani / pagine in italiano secondo la doc al 2026-10-03.

| Sito / pagina | Tipi consigliati | Rich result ottenibile in Italia |
|---|---|---|
| Qualsiasi sito – home | `WebSite` (`name`, `url`, `alternateName`) + `Organization` (o sottotipo) se c'è un brand/azienda | **Sì**: nome del sito nei risultati; logo in risultati/scheda informativa possibile (non garantito) |
| personal-brand – pagina Chi sono | `ProfilePage` con `mainEntity` `Person` (`sameAs`, `image`, `description`) | **No** risultato avanzato dedicato; aiuta comprensione dell'entità e collegamento autore [G] [D] |
| personal-brand / editoriale – articoli | `BlogPosting`/`Article`/`NewsArticle` con `author` → `@id` della persona + `BreadcrumbList` | **Sì** (titolo, immagine, data meglio rappresentati; breadcrumb solo desktop) |
| professionista-servizi senza sede aperta al pubblico | `Organization` (o `Person` via `ProfilePage`) con `contactPoint`; `LocalBusiness` solo se c'è un indirizzo reale mostrato [D] | Logo/scheda possibili; **no stelle** da recensioni proprie |
| attivita-locale (una o più sedi) | `LocalBusiness` sottotipo specifico, **uno per sede**, su pagina contatti/sede o home | **Sì** (dettagli nella scheda informativa; il Profilo dell'attività su Google resta la fonte principale [G]); **no stelle** per auto-recensioni; caroselli beta SEE solo per aggregatori/accesso su modulo |
| ecommerce – scheda prodotto | `Product` + `Offer` (o `ProductGroup` per varianti), `BreadcrumbList`, `Review`/`AggregateRating` di utenti reali | **Sì** (snippet prodotto, schede del commerciante, pro e contro in italiano); programmi fedeltà **no** in Italia |
| ecommerce – pagina "Chi siamo"/norme | `OnlineStore` con `hasMerchantReturnPolicy`, `hasShippingService` | Sì (schede commerciante) — le impostazioni Merchant Center/Search Console **prevalgono** sul markup [G] |
| Sito di recensioni (di terzi) | `Review`/`AggregateRating` nidificati nel tipo recensito (`Product`, `LocalBusiness` altrui, `Book`…) | **Sì** |
| prodotto-saas / app | `SoftwareApplication` (`WebApplication`/`MobileApplication`) + `Organization` | **Sì solo con valutazioni/recensioni reali** (obbligatorie) |
| Pagina evento | `Event` (una pagina per evento) | **No** (Italia/italiano non tra i mercati); utile solo per mercati supportati |
| Corsi / formazione | `Course` + `ItemList` (≥ 3 corsi) | **No** per contenuti in italiano (elenco di corsi solo in inglese; "Course info" ritirato) |
| Pagina con video ospitato | `VideoObject` (+ `Clip`/`SeekToAction`, `BroadcastEvent` per dirette) | **Sì** (risultati video, momenti chiave; `SeekToAction` supporta l'italiano) |
| Offerte di lavoro (datore o portale) | `JobPosting` su pagina della singola offerta | **Sì** (Italia supportata) |
| Ricette | `Recipe` (+ `ItemList` per carosello) | **Sì** |
| Forum / community | `DiscussionForumPosting` o `QAPage` (una domanda) + `ProfilePage` utenti | **Sì** |
| Foto/illustrazioni originali | `ImageObject` con `license`, `acquireLicensePage`, `creator` | **Sì** (badge "Su licenza" in Google Immagini) |
| Contenuti a pagamento | `isAccessibleForFree: false` + `hasPart` con `cssSelector` | Non è un rich result: serve a distinguere il paywall dal cloaking [G] |
| Pagina FAQ / guida "come fare" | Nessun markup per rich result (`FAQPage`, `HowTo` ritirati); `QAPage` **non** va usato per FAQ scritte dal sito | **No** |

## Schede per tipo

### WebSite (nome del sito)
- **Disponibilità**: tutte le lingue, mobile e desktop; siti a livello di **dominio o sottodominio** (`www` e `m` equivalgono al dominio); **sottodirectory non supportate** [G].
- **Dove**: solo nella **home page** (URI radice; `example.com/it/index.html` non è la home). Su tutte le home duplicate (http/https, www/non-www) [G]. Se il sottodominio non ha markup può ereditare il nome del dominio [G].
- **Obbligatorie**: `name`, `url` (home canonica, es. `https://example.com/`). **Consigliata**: `alternateName` (anche array, in ordine di preferenza) [G].
- **Scelta del nome** [G]: univoco, non fuorviante, conciso e comunemente riconosciuto ("Google", non "Google LLC"); nessun limite di caratteri ma può essere troncato; evitare nomi generici ("I migliori dentisti di X"); **coerente** con `<title>`, `og:site_name`, intestazioni della home; `Organization.name` uguale al nome del sito [G].
- **Se il nome non viene scelto** [G]: verificare errori e coerenza; aggiungere `alternateName`; aggiungere il **dominio in minuscolo** come ultimo `alternateName`; come ultima istanza usare il dominio minuscolo come `name`. Tempi: giorni o settimane.
- **Test**: validatore schema.org (il Test dei risultati avanzati non supporta i nomi dei siti) + Controllo URL [G].
- **Errori comuni**: `WebSite` su pagine interne o sottocartelle; due nodi `WebSite` in home; rimuovere `WebSite` credendo che serva solo alla casella di ricerca (ritirata nel 2024: il nodo serve ancora al nome del sito) [G-blog 2024-10].
- **Favicon** (attribuzione, non dati strutturati) [G]: `<link rel="icon" href="...">` nell'`<head>` della **home**; una per hostname; quadrata, **min 8x8 px, consigliata > 48x48 px**; formati BMP, GIF, ICO, PNG, JPEG, PPM, TIFF (SVG non elencato); URL stabile; file e home non bloccati a Googlebot/Googlebot-Image.
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://example.com/#website",
  "name": "Nome Sito",
  "alternateName": ["NS"],
  "url": "https://example.com/",
  "publisher": { "@id": "https://example.com/#organization" }
}
```
(`publisher` e `@id` sono [D]: collegamento di grafo, non richiesto da Google.)

### Organization
- **Disponibilità**: nessuna limitazione indicata. Influenza logo nei risultati e nella scheda informativa; per i commercianti anche scheda del commerciante e profilo del brand [G].
- **Dove**: **home** o una **singola pagina** che descrive l'organizzazione (Chi siamo); **non serve in ogni pagina** [G].
- **Obbligatorie: nessuna**. Concentrarsi su `name`/`alternateName`, presenza fisica (`address`, `telephone`), presenza online (`url`, `logo`) [G].
- **Consigliate (nomi esatti)** [G]: `address` (`PostalAddress`, anche multipli: `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` ISO 3166-1 alpha-2), `alternateName`, `contactPoint` (`telephone`, `email`), `description`, `duns`, `email`, `foundingDate` (ISO 8601), `globalLocationNumber`, `hasMerchantReturnPolicy`, `hasMemberProgram`, `hasShippingService`, `iso6523Code` (`ICD:identificatore`, es. `0060:` DUNS, `0088:` GLN, `0199:` LEI), `legalName`, `leiCode`, `logo`, `naics`, `name`, `numberOfEmployees` (`QuantitativeValue`), `sameAs`, `taxID` (coerente col paese di `address`), `telephone` (con prefisso internazionale), `url`, `vatID` (partita IVA: "importante indicatore di fiducia").
- **Vincoli**: `logo` **≥ 112x112 px**, scansionabile, formato supportato da Google Immagini, leggibile su **sfondo bianco**; con `ImageObject` serve `contentUrl` o `url` [G].
- **Sottotipo**: il più specifico (es. `OnlineStore` invece di `OnlineBusiness`); per sedi fisiche usare `LocalBusiness` e i suoi requisiti [G].
- **Errori comuni**: `name` diverso dal nome del sito; `sameAs` verso profili non propri (impersonificazione); logo bianco/trasparente illeggibile; Organization ripetuta in ogni pagina con dati diversi [G] [D].
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Nome Sito",
  "url": "https://example.com/",
  "logo": "https://example.com/img/logo-512.png",
  "email": "info@example.com",
  "telephone": "+39-000-0000000",
  "vatID": "IT00000000000",
  "sameAs": ["https://social.example/nomesito", "https://altro.example/nomesito"]
}
```

### LocalBusiness (+ sottotipi)
- **Disponibilità**: nessuna limitazione indicata per la scheda; carosello ristoranti ad **accesso limitato**; prenotazioni/ordini dai risultati via API Maps Booking, non via markup [G]. Caroselli beta (`ItemList` + `LocalBusiness`) solo SEE/Turchia/Sudafrica, per pagine di riepilogo con ≥ 3 entità e modulo di interesse [G].
- **Dove**: qualsiasi pagina, meglio quella con le informazioni dell'attività; **un'entità per sede** [G].
- **Tipo**: sottotipo **più specifico** (`Restaurant`, `Dentist`, `HealthClub`, `LegalService`…); più categorie → array in `@type` (es. `["Electrician","Plumber"]`); **`additionalType` non supportato** [G]. È sottotipo di `Organization`: valgono anche i campi Organization [G].
- **Obbligatorie**: `name`, `address` (`PostalAddress` il più completo possibile) [G].
- **Consigliate**: `aggregateRating` e `review` (**solo** se il sito raccoglie recensioni su **altre** attività), `department`, `geo` (`latitude`/`longitude` **≥ 5 decimali**), `menu`, `openingHoursSpecification` (`dayOfWeek`, `opens`, `closes`, `validFrom`, `validThrough`), `priceRange`, `servesCuisine`, `telephone` (prefisso paese), `url` (URL della **sede specifica**, funzionante) [G]. Email/telefono principali a livello `LocalBusiness`, poi `contactPoint` per canali aggiuntivi [G].
- **Vincoli** [G]: `priceRange` **< 100 caratteri** (≥ 100 non viene mostrato); orari `hh:mm:ss` (gli esempi Google usano `"09:00"`); giorni `https://schema.org/Monday` o forma breve `Monday`; aperto 24h = `00:00`–`23:59`; chiuso tutto il giorno = `00:00`–`00:00`; dopo mezzanotte = singolo oggetto (es. 18:00–03:00); chiusure stagionali con `validFrom`/`validThrough` (AAAA-MM-GG). Reparti: nome nel formato "{negozio} {reparto}".
- **Errori comuni**: stelle sulle proprie recensioni (anche via widget Google/Facebook incorporato) [G]; `additionalType`; coordinate approssimate; telefono senza prefisso; indirizzo/orari diversi dal Profilo dell'attività o dalla pagina [D]; una sola entità per più sedi.
- [D] Attività senza indirizzo pubblico (servizio a domicilio/online): `address` è obbligatorio per questo tipo → usare `Organization` oppure `LocalBusiness` solo con un indirizzo reale visibile in pagina. `areaServed` è schema.org valido ma non documentato da Google.
- ⚠ [D] `ProfessionalService` è spesso consigliato da terzi [T], ma schema.org lo descrive come tipo generico deprecato per confusione con `Service` (da verificare su schema.org): preferire un sottotipo specifico o `LocalBusiness`.
```json
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "@id": "https://example.com/sedi/citta/#localbusiness",
  "name": "Nome Attività",
  "url": "https://example.com/sedi/citta/",
  "telephone": "+39-000-0000000",
  "image": "https://example.com/img/sede-1200x900.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Via Esempio 1",
    "addressLocality": "Città",
    "addressRegion": "XX",
    "postalCode": "00000",
    "addressCountry": "IT"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 45.00000, "longitude": 9.00000 },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00", "closes": "18:00"
  }]
}
```

### Person / ProfilePage
- **Disponibilità**: nessuna limitazione indicata. Non produce un risultato avanzato dedicato: aiuta Google a capire i creator (es. "Discussioni e forum") ed è il bersaglio di `author.url` in Article, Recipe, forum, QAPage [G]. Il "profilo della Ricerca" (badge `profile.google.com`) è un'altra cosa e non si ottiene con il markup [G].
- **Casi validi**: profilo utente su forum/social, pagina autore di un sito di notizie, **pagina "Chi sono" di un blog**, pagina dipendente sul sito aziendale. **Non validi**: home di un negozio (troppe informazioni non di profilo), pagina di recensioni su un'organizzazione non affiliata [G]. L'entità principale deve essere **una sola persona/organizzazione affiliata al sito** [G].
- **ProfilePage – obbligatoria**: `mainEntity` (`Person` o `Organization`; se ignoto, `Person`). **Consigliate**: `dateCreated`, `dateModified` (ISO 8601; solo modifiche umane ai metadati) [G].
- **Person/Organization – obbligatoria**: `name` (o `alternateName` se manca). **Consigliate**: `agentInteractionStatistic`, `alternateName` (handle), `description` (riga dell'autore/qualifiche), `identifier` (ID interno stabile), `image`, `interactionStatistic`, `sameAs` [G].
- **Vincoli**: `image` reale (mai segnaposto/icona), ≥ 50.000 px, 16x9/4x3/1x1 consigliati; `interactionStatistic` **solo** con dati della piattaforma che ospita il profilo (non follower di altri social) [G]. Attività recenti: `hasPart` con `Article` che punta all'autore via `@id` [G].
- [D] Un `Person` senza `ProfilePage` (es. in home) è lecito ma non abilita funzionalità documentate; per un personal brand mettere `ProfilePage` sulla pagina Chi sono e riusarne l'`@id` come `author` ovunque. `jobTitle`, `honorificPrefix` sono proprietà citate da Google per gli autori [G].
```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "dateModified": "2026-01-15T10:00:00+01:00",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://example.com/chi-sono/#person",
    "name": "Nome Cognome",
    "jobTitle": "Ruolo professionale",
    "description": "Breve bio con qualifiche verificabili.",
    "image": "https://example.com/img/nome-cognome-800x800.jpg",
    "sameAs": ["https://profilo1.example/nomecognome", "https://profilo2.example/nomecognome"]
  }
}
```

### Article / BlogPosting / NewsArticle
- **Disponibilità**: nessuna limitazione indicata; migliora titolo, immagini e data in Ricerca, Google News, Assistente. Non obbligatorio per le funzionalità di Google News [G].
- **Obbligatorie: nessuna**. **Consigliate**: `author` (`Person`/`Organization`), `author.name`, `author.url` (pagina che identifica l'autore; se interna, marcarla `ProfilePage`; in alternativa `sameAs`), `dateModified`, `datePublished` (ISO 8601 **con fuso**, altrimenti fuso di Googlebot), `headline` (concisa), `image` [G].
- **Immagini**: pertinenti, **non loghi o didascalie**, ≥ 50.000 px (larghezza × altezza), ideale 16x9, 4x3, 1x1 [G].
- **Best practice autori** [G]: tutti gli autori visibili nel markup; **un oggetto per autore** (mai "Nome A, Nome B" in un solo `name`); `name` solo il nome (editore in `publisher`, ruolo in `jobTitle`, titoli in `honorificPrefix`/`honorificSuffix`, niente "di"/"pubblicato da"); `Person` per persone, `Organization` per enti, **mai `Thing`**.
- **Tecniche**: articoli in più parti → canonical a ogni pagina o a una pagina panoramica (non alla prima); contenuti in abbonamento → markup paywall [G].
- **Date** [G, pagina date di pubblicazione]: data visibile ed etichettata ("Pubblicato", "Aggiornato") coerente con il markup; niente date future.
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Titolo conciso dell'articolo",
  "image": ["https://example.com/img/articolo-1x1.jpg", "https://example.com/img/articolo-4x3.jpg", "https://example.com/img/articolo-16x9.jpg"],
  "datePublished": "2026-03-10T09:00:00+01:00",
  "dateModified": "2026-04-02T14:30:00+02:00",
  "author": [{ "@type": "Person", "@id": "https://example.com/chi-sono/#person", "name": "Nome Cognome", "url": "https://example.com/chi-sono/" }],
  "publisher": { "@id": "https://example.com/#organization" }
}
```

### BreadcrumbList
- **Disponibilità**: **solo desktop** dal 23/01/2025 (su mobile l'URL visibile mostra solo il dominio); tutte le regioni e lingue; markup ancora supportato, report e Test attivi [G] [G-blog 2025-01].
- **Struttura**: `BreadcrumbList` con **almeno 2 `ListItem`**; più tracce ammesse (array di `BreadcrumbList`) [G].
- **Obbligatorie**: `itemListElement`; per ogni `ListItem`: `position` (intero, 1 = inizio), `name`, `item` (URL o oggetto con `@id`) — `item` **non serve per l'ultimo elemento** (Google usa l'URL della pagina) [G].
- **Linee guida**: percorso utente **tipico**, non copia della struttura dell'URL; non serve un elemento per la radice (dominio) né per la pagina stessa [G]. [D] Deve corrispondere a un breadcrumb visibile in pagina (regola del contenuto visibile).
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Servizi", "item": "https://example.com/servizi/" },
    { "@type": "ListItem", "position": 2, "name": "Nome servizio" }
  ]
}
```

### Review / AggregateRating
- **Disponibilità**: nessuna limitazione indicata; stelle in risultati avanzati o schede informative [G].
- **Tipi recensibili** (`itemReviewed`): `Book`, `Course`, `CreativeWorkSeason`, `CreativeWorkSeries`, `Episode`, `Event`, `Game`, `HowTo`, `LocalBusiness`, `MediaObject`, `Movie`, `MusicPlaylist`, `MusicRecording`, `Organization`, `Product`, `Recipe`, `SoftwareApplication` [G] (vedi contraddizioni: alcuni corrispondono a funzionalità ritirate).
- **Review – obbligatorie**: `author` (nome valido, **< 100 caratteri**), `itemReviewed` (se non nidificata) + `itemReviewed.name` (o `name` del padre), `reviewRating`, `reviewRating.ratingValue`. **Consigliate**: `datePublished`, `reviewRating.bestRating` (default 5), `reviewRating.worstRating` (default 1) [G].
- **AggregateRating – obbligatorie**: `itemReviewed` (se non nidificata) + nome, `ratingValue`, **`ratingCount` o `reviewCount`**. **Consigliate**: `bestRating`, `worstRating` [G].
- **Vincoli** [G]: valore numero/frazione/percentuale (`4`, `6 / 10`, `60%`); scala default 1–5; **punto decimale** (`4.4`, non `4,4`); recensione su un **elemento specifico**, non su categorie/elenchi; con più recensioni singole includere anche l'aggregato; testo e valutazione **visibili** in pagina.
- **Divieti** [G]: aggregare recensioni **da altri siti**; recensioni false o **incentivate non dichiarate**; per `LocalBusiness`/`Organization`: se l'entità **controlla le recensioni su se stessa** (sul proprio sito, nel markup o tramite **widget incorporati** di Google/Facebook) le sue pagine **non sono idonee** alle stelle; valutazioni devono venire direttamente dagli utenti, non da editor. Recensioni non di utenti reali → possibile azione manuale.
- [D] Testimonianze di clienti sul sito di un professionista/azienda: **non** marcarle come `Review`/`AggregateRating` dell'attività stessa.
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "Restaurant",
    "name": "Nome Attività Recensita",
    "address": { "@type": "PostalAddress", "streetAddress": "Via Esempio 1", "addressLocality": "Città", "addressCountry": "IT" }
  },
  "author": { "@type": "Person", "name": "Nome Cognome" },
  "datePublished": "2026-05-20",
  "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": 5 }
}
```
(Valido per un sito che recensisce attività **di terzi**.)

### Event
- **Disponibilità**: esperienza eventi in Australia (inglese), Brasile (portoghese), Canada (inglese), Germania (tedesco), India (inglese), America Latina (spagnolo), Spagna (spagnolo), Regno Unito (inglese), Stati Uniti (inglese). **Italia/italiano non elencati** [G].
- **Linee guida** [G]: **una pagina con URL univoco per evento** (no calendari/elenchi); evento **in luogo fisico** (esperienze solo virtuali non supportate), prenotabile dal pubblico generale; esclusi eventi scolastici con minori; non marcare promozioni, orari di apertura, coupon, pacchetti viaggio.
- **Obbligatorie**: `name` (titolo dell'evento, non del luogo, senza prezzi/promozioni), `startDate` (ISO 8601 con offset), `location` (`Place`) con `location.address` (`PostalAddress` completo) [G].
- **Consigliate**: `description`, `endDate`, `eventStatus` (`EventScheduled`, `EventCancelled`, `EventPostponed`, `EventRescheduled`; mai togliere `startDate`/`location` cambiando stato), `image` (larghezza consigliata 1920 px, min 720 px; ≥ 50.000 px), `location.name`, `offers` (`availability` `InStock`/`SoldOut`/`PreOrder`, `price` minimo con commissioni, `0` se gratuito, `priceCurrency`, `validFrom`, `url`), `organizer` (`name`, `url`), `performer` (`name`), `previousStartDate` (solo con `EventRescheduled`) [G].
- **Errori comuni**: `T00:00:00` o `T23:59:59+00:00` usati come "tutto il giorno" (Google li tratta come orari reali: per un giorno intero usare solo la data); date senza fuso; nome del luogo in `name` [G].
```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Titolo dell'evento",
  "startDate": "2026-11-14T18:30:00+01:00",
  "endDate": "2026-11-14T21:00:00+01:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "Place",
    "name": "Nome della sede",
    "address": { "@type": "PostalAddress", "streetAddress": "Via Esempio 1", "addressLocality": "Città", "postalCode": "00000", "addressCountry": "IT" }
  },
  "offers": { "@type": "Offer", "price": 0, "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": "https://example.com/eventi/titolo/" }
}
```

### Course
- **Stato**: "**Course info**" (informazioni sui corsi) **ritirato** dal giugno 2025, rimosso da report e Test dal 9/09/2025 [G-blog]. Resta documentato il risultato "**elenco di corsi**" (carosello), **solo in inglese** [G].
- **Linee guida (elenco di corsi)** [G]: `Course` solo per una **serie/unità di apprendimento** con docenti e studenti (non un evento singolo né un video di 2 minuti); **almeno 3 corsi** marcati; **markup carosello `ItemList` obbligatorio** su pagina di riepilogo o pagina unica; `name` e `provider` validi (niente promozioni, prezzi, sconti nel nome).
- **Obbligatorie**: `name`, `description` (visualizzazione max **60 caratteri**). `provider` (`Organization`) è "consigliata" in tabella ma "deve" essere valida secondo le linee guida → includerla sempre [G].
- [D] Per siti in italiano: nessun rich result; il markup è facoltativo e non va promesso come leva di visibilità.
```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Nome del percorso formativo",
  "description": "Descrizione breve, entro 60 caratteri.",
  "provider": { "@type": "Organization", "name": "Nome Ente", "sameAs": "https://example.com/" }
}
```

### VideoObject
- **Disponibilità**: risultati principali, modalità Video, Google Immagini, Discover; momenti chiave con `Clip` (tutte le lingue) o `SeekToAction` (12 lingue, **italiano incluso**); badge DAL VIVO con `BroadcastEvent` [G].
- **Dove**: sulla **pagina di visualizzazione** (dove il video si guarda) [G].
- **Obbligatorie**: `name` (univoco per video), `thumbnailUrl`, `uploadDate` (ISO 8601 con fuso consigliato) [G].
- **Consigliate**: `contentUrl` (file video, metodo più efficace), `embedUrl` (player), `description`, `duration` (ISO 8601, es. `PT2M30S`), `expires`, `hasPart` (`Clip`: `name`, `startOffset`, `url`, consigliato `endOffset`), `interactionStatistic`, `regionsAllowed`/`ineligibleRegion`, `publication` (`BroadcastEvent` con `isLiveBroadcast`, `startDate`, `endDate`), `creator`/`author` [G].
- **Vincoli**: `Clip`/`SeekToAction` richiedono video ≥ **30 secondi** e deep link temporali (es. `?t=30`); due clip non possono iniziare nello stesso punto; disattivare i momenti chiave con `nosnippet` [G]. Dirette: API Indexing a inizio/fine [G].
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Titolo univoco del video",
  "description": "Descrizione univoca del video.",
  "thumbnailUrl": "https://example.com/video/miniatura-1280x720.jpg",
  "uploadDate": "2026-02-05T08:00:00+01:00",
  "duration": "PT4M12S",
  "contentUrl": "https://example.com/video/file.mp4",
  "embedUrl": "https://example.com/player?video=123"
}
```

### Product (breve)
- **Due famiglie** [G]: **snippet prodotto** (pagine senza acquisto diretto: recensioni editoriali, comparatori) e **schede del commerciante** (pagine dove si compra). Solo pagine su **un singolo prodotto** (o sue varianti), mai pagine categoria; un URL distinto per valuta; `Product` nell'**HTML iniziale**.
- **Snippet prodotto – obbligatorie**: `name` + **uno tra** `review`, `aggregateRating`, `offers` [G]. Pro e contro (`positiveNotes`/`negativeNotes`, ≥ 2 affermazioni) solo per recensioni editoriali; disponibili anche in **italiano** [G].
- **Scheda del commerciante – obbligatorie**: `name`, `image` (≥ 50.000 px), `offers` (`Offer`, non `AggregateOffer`) con `price` **> 0** e `priceCurrency` ISO 4217 [G]. Consigliate principali: `description`, `brand.name`, `gtin*`/`mpn`/`sku`, `aggregateRating`, `review`, `offers.availability`, `itemCondition`, `priceValidUntil` (non nel passato), `shippingDetails`, `hasMerchantReturnPolicy` [G].
- Varianti → `ProductGroup` (`productGroupID`, `variesBy`, `hasVariant`) [G]. Norme resi/spedizione anche a livello `Organization`; precedenza: feed/API Merchant Center → impostazioni Merchant Center/Search Console → markup prodotto → markup organizzazione [G]. Programmi fedeltà: non disponibili in Italia [G].
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Nome prodotto",
  "image": "https://example.com/img/prodotto-1200x1200.jpg",
  "sku": "SKU-0001",
  "offers": { "@type": "Offer", "price": 49.90, "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": "https://example.com/prodotto/" }
}
```

### JobPosting (breve)
- **Disponibilità**: Italia inclusa (e gran parte di Europa, Asia, Americhe, MENA, Africa subsahariana) [G].
- **Regole** [G]: solo sulla **pagina della singola offerta**, mai su elenchi; un `JobPosting` per offerta; **vietate le "richieste di lavoro"** (persona che si propone): non usarlo per dire "sono disponibile"; niente pagamenti richiesti ai candidati; offerte scadute → `validThrough` passato, 404/410 o rimozione del markup (+ API Indexing consigliata).
- **Obbligatorie**: `datePosted`, `description` (HTML completo, diversa dal titolo), `hiringOrganization`, `jobLocation` (con `addressCountry`; non necessaria se 100% remoto con `applicantLocationRequirements`), `title` (solo il nome del ruolo) [G].
- **Consigliate**: `applicantLocationRequirements`, `baseSalary` (`unitText` `HOUR`/`DAY`/`WEEK`/`MONTH`/`YEAR`), `directApply`, `employmentType` (`FULL_TIME`, `PART_TIME`, `CONTRACTOR`, `TEMPORARY`, `INTERN`, `VOLUNTEER`, `PER_DIEM`, `OTHER`), `identifier`, `jobLocationType` (`TELECOMMUTE` solo se 100% remoto), `validThrough` [G]. Stipendio nel markup → deve essere visibile in pagina [G].
```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "Nome del ruolo",
  "description": "<p>Responsabilità, requisiti, orario.</p>",
  "datePosted": "2026-09-01",
  "validThrough": "2026-10-31T23:59:00+01:00",
  "employmentType": "FULL_TIME",
  "hiringOrganization": { "@type": "Organization", "name": "Nome Azienda", "sameAs": "https://example.com/" },
  "jobLocation": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Città", "addressCountry": "IT" } }
}
```

## Tipi ritirati o non disponibili in Italia/italiano
Nessun ritiro influisce sul ranking; il markup ritirato è **innocuo ma inutile** per Google (non genera errori in Search Console) [G-blog 2024-10, 2025-06].

| Tipo / funzionalità | Stato | Data | Fonte | Indicazione |
|---|---|---|---|---|
| Casella di ricerca sitelink (`WebSite` + `potentialAction`/`SearchAction`) | Rimossa ovunque | dal 21/11/2024 | [G-blog 2024-10] | Non proporla; si può togliere `SearchAction` ma **non** il nodo `WebSite` (nome del sito) |
| Breadcrumb nei risultati mobile | Non mostrati (solo dominio) | dal 23/01/2025 | [G-blog 2025-01] | `BreadcrumbList` resta valido per desktop |
| `FAQPage` (risultato FAQ) | Limitato a siti governativi/sanitari dal 2023; rich result non mostrato dal 7/05/2026, report/Test rimossi a giugno 2026, API Search Console fino ad agosto 2026 | 2023 → 2026 | [T] SEJ che riporta la doc Google; la galleria Google scaricata non elenca più FAQ | Non raccomandare per rich result; `QAPage` non è un sostituto |
| `HowTo` | Ritirato | 2023 | [T] SEJ; assente dalla galleria Google | Non raccomandare |
| Course info | Ritiro graduale; fuori da report/Test/filtri | giugno 2025; 9/09/2025 | [G-blog 2025-06] | L'"elenco di corsi" resta, solo inglese |
| `ClaimReview` (fact check) | Eliminato dalla Ricerca; resta in Fact Check Explorer | giugno 2025 | [G-blog] + doc factcheck | Solo per Fact Check Explorer |
| Estimated salary, Learning video, `SpecialAnnouncement`, Vehicle listing | Ritirati | giugno 2025; fuori dai report 9/09/2025 | [G-blog 2025-06] | Non proporre |
| Book actions | Annunciato ritiro (giugno 2025); secondo SEJ l'avviso di deprecazione è stato tolto (nov 2025); doc ancora presente, accesso solo su modulo + feed | incerto | [G-blog] vs [T] | Stato da verificare nel changelog; comunque non applicabile a siti comuni |
| Practice problem | Supporto rimosso | da gennaio 2026 | [T] SEJ (changelog Google) | Non proporre |
| Altri tipi "poco usati" | Rimozione progressiva; supporto in Search Console/API tolto da gennaio 2026 | nov 2025 → | [G-blog 2025-11] | Controllare `/search/updates` prima di proporre tipi marginali |
| `data-vocabulary.org` | Non idoneo | 2020 | [G] | Migrare a schema.org |
| Event | Attivo ma **non in Italia/italiano** | — | [G] | Utile solo per mercati elencati |
| Elenco di corsi | Attivo **solo in inglese** | — | [G] | Nessun effetto su pagine in italiano |
| Domande e risposte didattiche (flashcard) | Inglese, portoghese, vietnamita; spagnolo solo Messico | — | [G] | Non per l'italiano |
| Speakable (beta) | Solo USA, inglese | — | [G] | Non per l'italiano |
| Programmi fedeltà (`MemberProgram`) | AU, BR, CA, FR, DE, MX, UK, US | — | [G] | Non in Italia |
| Carosello ristoranti; case vacanze | Accesso limitato (modulo / Hotel Center) | — | [G] | Non proporre di default |
| Caroselli beta (`ItemList` + LocalBusiness/Product/Event) | SEE (Italia inclusa), Turchia, Sudafrica; beta, per aggregatori, modulo di interesse | dal 2024 | [G] [G-blog 2024-02] | Solo pagine di riepilogo con ≥ 3 entità |
| `Dataset` | Usato solo da Dataset Search | — | [G] [T] | Non è un rich result della Ricerca |

## Controlli per l'audit
Gravità: **Critico** (markup inefficace o rischio azione manuale su molte pagine) · **Alto** · **Medio** · **Basso** · **Info**.

| ID | Controllo | Come verificarlo | Gravità | Fonte |
|---|---|---|---|---|
| SD-01 | Ogni blocco `application/ld+json` è JSON valido e analizzabile | Parser JSON sull'HTML renderizzato; report "Dati strutturati non analizzabili" | Critico | [G] |
| SD-02 | `@context` `https://schema.org`; nessun `data-vocabulary.org` | Ricerca nel sorgente | Alto | [G] |
| SD-03 | Ogni valore marcato è visibile nella pagina renderizzata (nomi, prezzi, orari, recensioni, date, stipendi) | Confronto JSON-LD ↔ testo DOM renderizzato | Critico | [G] |
| SD-04 | Proprietà obbligatorie presenti per ogni tipo usato | Tabelle di questa scheda; Test dei risultati avanzati (URL) | Alto | [G] |
| SD-05 | Tipo corretto e più specifico; tipo principale della pagina incluso | Revisione tipo vs contenuto (es. `Article` solo su articoli, sottotipo LocalBusiness) | Medio | [G] |
| SD-06 | Tipi ritirati presenti (`FAQPage`, `HowTo`, `SearchAction` sitelink, `ClaimReview`, `SpecialAnnouncement`, Course info…) | Ricerca `@type`; confronto con tabella ritiri | Basso (innocuo; segnalare che non produce effetti) | [G-blog] [T] |
| SD-07 | Tipo non disponibile nel mercato/lingua del sito (Event e Course in italiano, Education Q&A, loyalty, Speakable) | Lingua/paese del sito vs tabella | Info | [G] |
| SD-08 | Pagine con markup non bloccate da robots.txt, `noindex`, login | Controllo URL; robots.txt; meta robots | Alto | [G] |
| SD-09 | Immagini del markup scansionabili, pertinenti, ≥ 50.000 px; niente loghi in `Article`; `logo` ≥ 112x112 e leggibile su bianco | Fetch degli URL immagine e dimensioni | Medio | [G] |
| SD-10 | `WebSite` in home con `name` + `url`; un solo nodo `WebSite`; nome coerente con `<title>`, `og:site_name`, `Organization.name` | Analisi della home; validatore schema.org | Alto | [G] |
| SD-11 | Stesso markup `WebSite` su tutte le home duplicate (http/https, www/non-www) e redirect funzionanti | Fetch delle varianti | Basso | [G] |
| SD-12 | `WebSite` non su sottodirectory o pagine interne come "home" alternativa | Mappa delle pagine con `WebSite` | Medio | [G] |
| SD-13 | `Organization` su home o Chi siamo, sottotipo specifico, dati coerenti tra pagine | Confronto dei nodi Organization nel sito | Medio | [G] [D] |
| SD-14 | `LocalBusiness`: `name` + `address` completo, un'entità per sede, `telephone` con prefisso, `geo` ≥ 5 decimali, `priceRange` < 100 caratteri, nessun `additionalType` | Validazione campi | Alto | [G] |
| SD-15 | Orari `openingHoursSpecification` coerenti con pagina e Profilo dell'attività; formati giorni/ore validi | Confronto manuale/automatico | Medio | [G] [D] |
| SD-16 | Auto-recensioni: `Review`/`AggregateRating` sulla propria `Organization`/`LocalBusiness` (markup o widget incorporati) | `itemReviewed`/nodo padre = entità proprietaria del sito | Alto | [G] |
| SD-17 | Recensioni: non aggregate da altri siti, non incentivate non dichiarate; `ratingValue` con punto; scala coerente con `bestRating`/`worstRating`; `ratingCount` o `reviewCount`; `author.name` < 100 caratteri | Validazione campi + revisione fonte | Alto | [G] |
| SD-18 | `ProfilePage`: `mainEntity` con `name`; pagina dedicata a una sola persona/organizzazione affiliata; `image` non segnaposto; `interactionStatistic` solo della piattaforma | Revisione pagina | Medio | [G] |
| SD-19 | Autori `Article`: `@type` `Person`/`Organization` (mai `Thing`), un oggetto per autore, `name` senza ruoli/titoli, `url` o `sameAs` validi, tutti gli autori visibili presenti | Validazione campi | Medio | [G] |
| SD-20 | Date ISO 8601 con fuso; `datePublished`/`dateModified` coerenti con la data visibile; niente date future; niente `T00:00:00` come "giorno intero" negli eventi | Parsing date + confronto testo | Medio | [G] |
| SD-21 | `BreadcrumbList`: ≥ 2 `ListItem`, `position` da 1 senza salti, `item` su tutti tranne l'ultimo, coerente col breadcrumb visibile | Validazione struttura | Medio | [G] [D] |
| SD-22 | `Event`, `JobPosting`, `Product` solo su pagine foglia di un singolo elemento (non elenchi/calendari/categorie) | Classificazione pagina vs tipo | Alto | [G] |
| SD-23 | `JobPosting`: offerte scadute rimosse/`validThrough` passato; `addressCountry`; `TELECOMMUTE` solo 100% remoto; nessuna autocandidatura | Validazione + data corrente | Alto | [G] |
| SD-24 | `Product`: `price` > 0 e `priceCurrency` ISO 4217 per schede commerciante; `priceValidUntil` non passato; `Product` nell'HTML iniziale | Validazione + HTML grezzo | Alto | [G] |
| SD-25 | `VideoObject` su pagina di visualizzazione con `name`, `thumbnailUrl`, `uploadDate`; `contentUrl` o `embedUrl` | Validazione | Medio | [G] |
| SD-26 | Enumerazioni con URL schema.org o forme brevi accettate (`availability`, `eventStatus`, `dayOfWeek`); codici ISO (paese alpha-2, valuta 4217) | Validazione valori | Medio | [G] |
| SD-27 | `sameAs` verso profili ufficiali dell'entità, URL validi (non pagine di terzi a caso) | Fetch e revisione | Medio | [G] |
| SD-28 | Nessuna entità duplicata o contraddittoria (due `Organization` con dati diversi, plug-in + markup manuale) | Raggruppare i nodi per tipo/`@id` | Medio | [D] |
| SD-29 | `@id` stabili e riutilizzati; riferimenti `@id` risolvibili nella pagina o nel sito | Analisi del grafo | Basso | [G] [D] |
| SD-30 | Markup generato via JS presente nel DOM renderizzato, aggiornato a ogni route, non condizionato al consenso cookie | Test dei risultati avanzati via URL; Controllo URL; confronto HTML grezzo/renderizzato | Alto | [G] [T] |
| SD-31 | Search Console: stato dei risultati avanzati, dati non analizzabili, Azioni manuali; trend dopo i rilasci | Report Search Console | Alto | [G] |
| SD-32 | Nessuna pagina creata solo per ospitare dati strutturati; nessun markup "per l'AI" promesso come leva | Revisione | Medio | [G] |

## Note per SPA/JavaScript
- Google legge il JSON-LD inserito dinamicamente ed elabora i dati presenti nel DOM al rendering [G]. Le alternative documentate sono GTM, JS personalizzato e **rendering lato server** [G].
- [D] Preferire SSR/prerendering/SSG che emettono il JSON-LD nell'HTML iniziale, soprattutto per `Product` (indicazione esplicita Google), `WebSite`, `Organization`, `LocalBusiness`, `ProfilePage`. Motivi: scansioni Shopping più affidabili [G]; molti crawler AI non eseguono JavaScript [T].
- Verifica: Test dei risultati avanzati **in modalità URL** e Controllo URL (HTML renderizzato); per tipi non supportati dal Test controllare l'HTML renderizzato [G].
- [D] Router client-side: **un blocco JSON-LD per route**, sostituito o rimosso a ogni navigazione; mai lasciare il markup della vista precedente né duplicarlo.
- [D] Se il JSON-LD dipende da un `fetch` (come nell'esempio Google), l'endpoint deve essere raggiungibile da Googlebot (non bloccato da robots.txt, veloce).
- [T] Non caricare il JSON-LD tramite GTM dietro il banner dei cookie: se lo script parte solo dopo il consenso, i crawler potrebbero non vederlo.
- Limite di **2 MB** per HTML e per ogni risorsa JS/CSS per Googlebot: stati serializzati enormi inline possono spingere il markup oltre la soglia; mettere metadati e dati strutturati essenziali presto nel documento [G-blog 2026-03].
- Dopo un rilascio: un calo degli elementi validi senza aumento degli invalidi indica markup non più incorporato (regressione di rendering/SSR) [G].
- Dettagli generali sul rendering: `knowledge/rendering-javascript.md`.

## Cosa dicono le fonti terze
- **Posizione Google sull'AI** [G]: per AI Overviews e AI Mode non ci sono requisiti aggiuntivi; **non servono** file, "markup AI" o schema.org speciali; i dati strutturati devono solo corrispondere al testo visibile. La guida Google di maggio 2026 sull'ottimizzazione per l'AI generativa ribadisce che AEO/GEO sono "ancora SEO" e che i dati strutturati non sono richiesti per le funzionalità AI (restano utili per i rich result) [G-blog 2026-05; dettagli via SEJ].
- ⚠ **"Schema per AI/GEO"** [T]: molte fonti (spesso vendor con conflitto di interessi) sostengono che JSON-LD, FAQPage o HowTo aumentino le citazioni negli assistenti AI. Nessuna conferma Google; diversi autori SEJ le classificano come ipotesi o "snake oil". Circa 168.000 pagine affermerebbero che "FAQ schema è critico per GEO" (dato riportato da SEJ), mentre Google ha ritirato il rich result FAQ.
- **Studio Ahrefs (maggio 2026)** [T]: su ~6 milioni di URL le pagine citate dall'AI hanno circa 3 volte più JSON-LD (**correlazione**). Nel test causale (1.885 pagine che hanno aggiunto JSON-LD tra ago 2025 e mar 2026, confrontate con ~4.000 controlli, finestra ±30 giorni) l'effetto è nullo o negativo: AI Overviews −4,6%, AI Mode +2,4%, ChatGPT +2,2% (questi ultimi non distinguibili dal caso). Limiti dichiarati: solo pagine già molto citate, solo schema presente nell'HTML (non iniettato via JS), tipi aggregati, Bing/Copilot/Perplexity/Claude non misurati.
- Esperimento Williams-Cook [T]: un JSON-LD **non valido** veniva comunque letto come testo dagli LLM → per gli LLM il markup è soprattutto testo, non una struttura privilegiata.
- Opinioni diffuse e plausibili, **non provate** [T]: `Person`/`Organization` con `sameAs` e `@id` coerenti aiutano la **disambiguazione dell'entità** (omonimi, personal brand); mantenere identici nome/NAP/orari tra sito, schema e Profilo dell'attività. È coerente con i principi Google (dati accurati e coerenti), ma nessun effetto su ranking o citazioni è dimostrato. Il rischio concreto citato è lo schema **non aggiornato** (es. vecchio telefono) [T].
- Microsoft/Bing (riportato di seconda mano) afferma che lo schema aiuta Copilot [T]: non verificato nelle fonti lette.
- John Mueller: i tipi di markup "vanno e vengono", pochi vale la pena mantenerli [T, citazione riportata da SEJ].
- **Regola per le skill** [D]: proporre JSON-LD solo (1) per rich result documentati e disponibili nel mercato del sito, o (2) per descrivere entità (`WebSite`, `Organization`, `LocalBusiness`, `Person`/`ProfilePage`, `Article`). Mai promettere citazioni AI, ranking o visibilità "GEO" dal markup; mai raccomandare `FAQPage`/`HowTo` per risultati avanzati; `llms.txt` e markup "per AI" fuori ambito (vedi `knowledge/ai-search.md`).
