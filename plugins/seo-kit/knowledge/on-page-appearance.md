# On-page e aspetto nei risultati di ricerca

> Aggiornato al 2026-10-03. Fonte primaria: Google Search Central. Secondaria: Search Engine Journal (ott 2025–ott 2026).
> Legenda: **[G]** = documentazione, blog o Office Hours (OH) di Google = fatto Google. **Deduzione:** = inferenza nostra dai documenti Google. **[SEJ …]** = fonte terza. **⚠** = va oltre o contro quanto dice Google.
> Ambito: tutto ciò che decide *come* una pagina appare nei risultati (title, snippet, immagini, video, favicon, nome del sito, sitelink, breadcrumb, Discover) e l'esperienza sulla pagina (CWV, mobile, HTTPS, interstitial). Qualità dei contenuti e spam: vedi `content-quality-spam.md`.

## Indice
- [Fatti e regole (Google)](#fatti-e-regole-google)
  - [Title link](#title-link) · [Meta description e snippet](#meta-description-snippet-e-controlli-di-anteprima) · [Head e peso HTML](#head-e-peso-dellhtml) · [Intestazioni](#intestazioni-heading) · [Link interni e anchor](#link-interni-e-anchor-text) · [URL](#url)
  - [Immagini](#immagini) · [Video](#video) · [Favicon](#favicon) · [Nome del sito](#nome-del-sito) · [Sitelink](#sitelink) · [Breadcrumb](#breadcrumb-e-url-visibile) · [Discover](#discover)
  - [Core Web Vitals ed esperienza](#core-web-vitals-ed-esperienza-sulla-pagina) · [Interstitial e annunci](#interstitial-e-annunci) · [Mobile](#mobile) · [HTTPS](#https) · [Date](#date-di-pubblicazione) · [Funzionalità AI](#funzionalità-ai-aspetto) · [Paywall](#contenuti-a-pagamento-solo-se-rilevante) · [Altro](#altri-elementi-di-aspetto)
- [Controlli per l'audit](#controlli-per-laudit)
- [Regole per chi costruisce / scrive contenuti](#regole-per-chi-costruisce--scrive-contenuti)
- [Note per tipo di sito](#note-per-tipo-di-sito)
- [Cosa dicono le fonti terze](#cosa-dicono-le-fonti-terze)
- [Miti e consigli obsoleti](#miti-e-consigli-obsoleti)

## Fatti e regole (Google)

### Title link
- Il title link è generato **automaticamente**; Google non lo modifica a mano e non esiste un modo per rifiutare la riscrittura. Fonti usate: `<title>`, titolo visivo principale, `<h1>`/intestazioni, `og:title`, testo grande e in risalto, altro testo della pagina, anchor text nella pagina e dei link in entrata, dati strutturati `WebSite`. [G](https://developers.google.com/search/docs/appearance/title-link)
- Ogni pagina deve avere un `<title>` **descrittivo e conciso**. **Nessun limite di caratteri**: viene troncato in base alla larghezza del dispositivo. [G](https://developers.google.com/search/docs/appearance/title-link)
- Cause tipiche di riscrittura: title semivuoti (`| Brand`), obsoleti (anno vecchio), imprecisi rispetto al contenuto, micro-boilerplate (stesso title su un gruppo di pagine), nessun titolo principale evidente, lingua o sistema di scrittura diversi dal contenuto, nome del sito ripetuto (può essere omesso se già mostrato come nome del sito). [G](https://developers.google.com/search/docs/appearance/title-link)
- Da evitare: title vaghi ("Home", "Profilo"), keyword stuffing ("Foobar, foo bar, foo-bar"), testo ripetuto tra pagine, prezzi dei voli. Aggiornare il title quando il contenuto cambia. [G](https://developers.google.com/search/docs/appearance/title-link)
- Brand: in home è ammessa una breve descrizione; nelle altre pagine nome del sito all'inizio o alla fine, separato da un delimitatore (`-`, `:`, `|`). Il title può includere nome dell'attività, sede fisica e dettagli dell'offerta. [G](https://developers.google.com/search/docs/appearance/title-link) [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- Serve un **titolo principale chiaro**: un'intestazione distinta (carattere più grande, primo `<h1>` visibile); più intestazioni con lo stesso peso visivo confondono. [G](https://developers.google.com/search/docs/appearance/title-link)
- Title, H1 e URL **non devono coincidere**: va bene una sovrapposizione naturale di parole. [G OH 2022-12](https://developers.google.com/search/help/office-hours/2022/december) [G OH 2024-06](https://developers.google.com/search/help/office-hours/2024/june)
- Una pagina bloccata da robots.txt può comunque essere indicizzata con un titolo ricavato da fonti esterne (es. anchor di altri siti): per escluderla serve `noindex` con scansione consentita. [G](https://developers.google.com/search/docs/appearance/title-link)
- Nelle sequenze paginate title e description possono essere uguali (eccezione alla regola dei title distinti). [G](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
- Le modifiche si vedono dopo una nuova scansione (giorni o settimane); si può richiederla con Controllo URL. [G](https://developers.google.com/search/docs/appearance/title-link)

### Meta description, snippet e controlli di anteprima
- Lo snippet è generato automaticamente, **soprattutto dal contenuto della pagina**, e cambia con la query; la meta description viene usata quando descrive la pagina meglio del contenuto. Nessuna garanzia d'uso. [G](https://developers.google.com/search/docs/appearance/snippet) [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january)
- Google la usa più spesso quando la pagina ha poco contenuto o quando la description è più pertinente alla query del testo. [G OH 2023-09](https://developers.google.com/search/help/office-hours/2023/september)
- Meta description: **nessun limite di lunghezza** (troncata per larghezza); **unica per pagina**; se manca tempo, priorità a home e pagine più visitate; può contenere fatti (autore, data, prezzo, produttore, orari, sede) senza forma discorsiva; generazione programmatica ammessa se distinta e leggibile. Da evitare: elenchi di parole chiave, stessa description ovunque, testi che non riassumono la pagina, testi troppo brevi. [G](https://developers.google.com/search/docs/appearance/snippet)
- Controlli: `nosnippet` (nessuno snippet), `max-snippet:[n]` (`0` = come nosnippet, `-1` = lunghezza scelta da Google; ignorato se il numero non è leggibile), attributo `data-nosnippet` (esclude parti di testo). Con regole in conflitto vince la **più restrittiva**. [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- `data-nosnippet` è valido solo su `span`, `div`, `section`, con HTML ben chiuso; non aggiungerlo o toglierlo via JavaScript su nodi esistenti (va messo quando l'elemento entra nel DOM). Le regole robots non limitano i dati strutturati (eccetto `description` di opere creative, limitabile con `max-snippet`). [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- `nosnippet`, `max-snippet`, `data-nosnippet` e `noindex` valgono anche per **AI Overview e AI Mode** (impediscono l'uso come input diretto). Google-Extended non riguarda la Ricerca. [G](https://developers.google.com/search/docs/appearance/ai-features) [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- Featured snippet: non si possono "marcare"; per escluderli `nosnippet` (sicuro) o ridurre `max-snippet` (nessuna soglia esatta). Se ci sono sia `nosnippet` sia `data-nosnippet`, prevale `nosnippet`. [G](https://developers.google.com/search/docs/appearance/featured-snippets)
- Link "Leggi tutto" verso sezioni: contenuto **immediatamente visibile** (non in tab o accordion chiusi), nessun JS che forza lo scroll al caricamento, non rimuovere il frammento `#` dall'URL. [G](https://developers.google.com/search/docs/appearance/snippet)
- `notranslate` (meta o `X-Robots-Tag`) disattiva i risultati tradotti. L'italiano non è tra le lingue di destinazione della traduzione. [G](https://developers.google.com/search/docs/appearance/translated-results)

### Head e peso dell'HTML
- Nel `<head>` sono validi solo `title`, `meta`, `link`, `script`, `style`, `base`, `noscript`, `template`. Un `img` o `iframe` nel head fa presumere a Google la **fine dell'head**: i metadati successivi possono essere ignorati. [G](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata)
- Googlebot (Ricerca) recupera fino a **2 MB per URL HTML** (intestazioni incluse) e 2 MB per ogni risorsa JS/CSS; i byte oltre la soglia sono ignorati. PDF: 64 MB. Mettere title, meta, canonical e dati strutturati essenziali **in alto**; evitare base64 e CSS/JS inline voluminosi. [G](https://developers.google.com/search/blog/2026/03/crawler-blog-post)
- Contenuti in `<canvas>`, in plug-in o generati con la proprietà CSS `content` non sono indicizzati; il testo dentro le immagini non serve per i risultati web. [G](https://developers.google.com/search/docs/fundamentals/get-started-developers) [G OH 2022-12](https://developers.google.com/search/help/office-hours/2022/december)

### Intestazioni (heading)
- Usare le parole che le persone cercano nelle posizioni in evidenza: titolo, intestazione principale, testo alternativo, testo dei link. [G](https://developers.google.com/search/docs/essentials)
- **Numero e ordine delle intestazioni non contano per la Ricerca** (contano per gli screen reader). [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) [G OH 2024-07](https://developers.google.com/search/help/office-hours/2024/july)
- Un HTML semantico (intestazioni come riepilogo) può aiutare a capire il contenuto, ma non è una "ricetta segreta"; la leggibilità per le persone conta più del codice perfetto. [G OH 2023-09](https://developers.google.com/search/help/office-hours/2023/september) [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Il ranking dei passaggi valuta singole sezioni di una pagina. Deduzione: intestazioni descrittive e sezioni autosufficienti facilitano la comprensione dei passaggi. [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide)
- Su mobile usare le stesse intestazioni chiare del desktop. [G](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)

### Link interni e anchor text
- Google estrae link in modo affidabile solo da `<a href>` che si risolve in un URL reale. Sconsigliati: `<span href>`, `<a onclick>` senza href, `href="javascript:…"`, attributi di routing senza `href` nell'HTML renderizzato. Link inseriti via JS vanno bene se il markup finale è corretto. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Googlebot **non clicca i pulsanti**; gli URL in `<select><option>` non sono link. [G OH 2023-09](https://developers.google.com/search/help/office-hours/2023/september) [G OH 2023-05](https://developers.google.com/search/help/office-hours/2023/may)
- Anchor text: descrittivo, ragionevolmente conciso, pertinente. Da evitare: "fai clic qui", "scopri di più", link vuoti, anchor lunghissimi, link uno accanto all'altro senza contesto, parole chiave forzate. Per link-immagine l'anchor è l'`alt`; se `<a>` è vuoto Google può usare `title`. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Ogni pagina importante deve avere un link da almeno un'altra pagina del sito; **nessun numero ideale** di link. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Google deduce l'importanza relativa da profondità (click necessari) e numero di link interni in entrata, non dalla struttura delle cartelle. [G](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- Anchor interni quasi identici (menu, schede) sono normali. [G OH 2022-11](https://developers.google.com/search/help/office-hours/2022/november)
- Scorrimento infinito/"carica altro": ogni blocco con URL univoco e stabile (es. `?page=12`) e link sequenziali; Google non scorre né clicca. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading)

### URL
- **Non usare frammenti `#`** per cambiare contenuti (es. `/#/potatoes`): la Ricerca in genere non li supporta; usare la History API. [G](https://developers.google.com/search/docs/crawling-indexing/url-structure)
- Parametri `chiave=valore` separati da `&`; il minor numero possibile; niente ID di sessione o valori temporanei nei link interni. [G](https://developers.google.com/search/docs/crawling-indexing/url-structure) [G](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites)
- Parole descrittive nella lingua del pubblico, codifica percentuale quando serve, **trattini** (non underscore) tra le parole; gli URL sono **sensibili a maiuscole/minuscole**. [G](https://developers.google.com/search/docs/crawling-indexing/url-structure)
- Parole chiave nel dominio o nel percorso: effetto **quasi nullo** sul ranking (servono soprattutto come breadcrumb). Non cambiare URL per "trucchi" SEO. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) [G OH 2023-05](https://developers.google.com/search/help/office-hours/2023/may)

### Immagini
- Usare `<img src>` (anche dentro `<picture>`, sempre con `src` di riserva). **Le immagini CSS (`background-image`) non vengono indicizzate.** [G](https://developers.google.com/search/docs/appearance/google-images)
- Formati in `img src`: **BMP, GIF, JPEG, PNG, WebP, SVG, AVIF** (AVIF dal 2024); estensione coerente con il tipo; Google riconosce il formato dall'header `Content-Type`. Data URI ammessi ma appesantiscono. [G](https://developers.google.com/search/docs/appearance/google-images) [G](https://developers.google.com/search/blog/2024/08/happy-avifriday) [G OH 2023-03](https://developers.google.com/search/help/office-hours/2023/march)
- `alt` è l'attributo **più importante**: descrittivo, nel contesto, senza stuffing (rischio spam). SVG inline: `<title>` con `aria-labelledby`. Immagini vicine a testo pertinente, didascalie utili, **nomi file descrittivi**, stesso URL per la stessa immagine. [G](https://developers.google.com/search/docs/appearance/google-images)
- Immagine preferita (miniatura in Ricerca e Discover, scelta comunque automatica): `primaryImageOfPage` su `WebPage`, oppure `image` dell'entità principale (`mainEntity`/`mainEntityOfPage`), oppure `og:image`. Evitare loghi, immagini generiche o con molto testo, proporzioni estreme; alta risoluzione. [G](https://developers.google.com/search/docs/appearance/google-images)
- `max-image-preview`: `none`, `standard`, `large` (fino alla larghezza dell'area visibile). Case study: +79% e +30% di CTR con `large`. [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) [G](https://developers.google.com/search/case-studies/large-images-case-study)
- Sitemap immagini: fino a **1.000** `<image:image>` per `<url>`; `<image:loc>` può stare su un altro dominio (verificare entrambi in Search Console); `caption`, `title`, `geo_location`, `license` sono ritirati. [G](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)
- Lazy loading: caricare quando l'elemento entra nell'area visibile (nativo o IntersectionObserver), mai legato a scroll o clic; **non applicarlo ai contenuti visibili subito**. [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading)
- EXIF non usato; i metadati usati sono IPTC. Se le immagini cambiano URL, redirect dai vecchi URL (le immagini sono scansionate meno spesso). [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january) [G OH 2023-12](https://developers.google.com/search/help/office-hours/2023/december)

### Video
- Incorporare con `<video>`, `<embed>`, `<iframe>` o `<object>`, presente nell'HTML renderizzato **senza azioni dell'utente** (scroll, clic, digitazione); mai caricare il video tramite `#`. [G](https://developers.google.com/search/docs/appearance/video)
- Per risultati video, momenti chiave e badge LIVE serve una **pagina di visualizzazione dedicata** (il video è lo scopo principale, in evidenza). Pagina indicizzata e ben posizionata; miniatura a URL stabile. [G](https://developers.google.com/search/docs/appearance/video) [G OH 2023-12](https://developers.google.com/search/help/office-hours/2023/december)
- Miniatura: formati BMP, GIF, JPEG, PNG, WebP, SVG, AVIF; **minimo 60x30 px**; accessibile a Googlebot e Googlebot-Image; con trasparenza almeno l'80% dei pixel con alfa > 250; stesso URL in tutte le fonti. [G](https://developers.google.com/search/docs/appearance/video)
- `VideoObject` con `name`, `description`, `thumbnailUrl` univoci per video; Sitemap video; `max-video-preview` (`0` = solo immagine statica, `-1` = nessun limite); data URL non supportati; `expires` nel passato esclude il video. Momenti chiave: `Clip` o `SeekToAction` (italiano supportato); disattivazione con `nosnippet`. [G](https://developers.google.com/search/docs/appearance/video)
- Video YouTube più lo stesso testo sulla pagina non è contenuto duplicato. [G OH 2024-08](https://developers.google.com/search/help/office-hours/2024/august)

### Favicon
- `<link rel="icon" href="…">` (anche `shortcut icon`, `apple-touch-icon`, `apple-touch-icon-precomposed`) **nell'head della home page**; `href` relativo o assoluto, anche su CDN. [G](https://developers.google.com/search/docs/appearance/favicon-in-search)
- **Una favicon per hostname** (dominio o sottodominio, non sottodirectory). Googlebot-Image deve poter scansionare il file e Googlebot la home. [G](https://developers.google.com/search/docs/appearance/favicon-in-search)
- **Quadrata 1:1, minimo 8x8 px, consigliata più grande di 48x48 px.** Formati elencati: BMP, GIF, ICO, PNG, JPEG, PPM, TIFF (SVG non compare nell'elenco della versione italiana letta). Deve rappresentare il brand; URL stabile. Aggiornamento in giorni o settimane. [G](https://developers.google.com/search/docs/appearance/favicon-in-search)
- Cambio favicon: aggiornare tutti i file dichiarati, redirect dal vecchio file al nuovo, attendere (anche ~un mese). [G OH 2023-05](https://developers.google.com/search/help/office-hours/2023/may) [G OH 2024-07](https://developers.google.com/search/help/office-hours/2024/july)

### Nome del sito
- Generato **automaticamente** da home page e riferimenti web. Segnale più importante: dati strutturati **`WebSite` nella home**; poi `og:site_name`, `<title>`, intestazioni e testo della home. [G](https://developers.google.com/search/docs/appearance/site-names)
- **Un nome per sito**, definito da dominio o sottodominio (`www` e `m` equivalgono al dominio); **sottodirectory non supportate**. `WebSite` va solo sulla home (URI radice), in un unico nodo (annidare lì altre proprietà). [G](https://developers.google.com/search/docs/appearance/site-names)
- Proprietà obbligatorie `name` e `url` (home canonica); consigliata `alternateName` (anche array in ordine di preferenza). Formati JSON-LD, RDFa, microdati. [G](https://developers.google.com/search/docs/appearance/site-names)
- Nome conciso, univoco, comunemente riconosciuto, **non generico** ("I migliori dentisti in Iowa" non va); usato in modo coerente in tutta la home; nessun limite di caratteri ma può essere troncato. [G](https://developers.google.com/search/docs/appearance/site-names)
- Home duplicate (HTTP/HTTPS, www/non-www): **stessi dati strutturati su tutte**; il nome riflette la destinazione dei redirect. Se il nome non viene scelto: verificare coerenza, poi aggiungere `alternateName`, poi il **dominio in minuscolo** come ultimo `alternateName`, come ultima risorsa come `name`. [G](https://developers.google.com/search/docs/appearance/site-names)
- Test con validator.schema.org: il **Test dei risultati avanzati non supporta i nomi dei siti**. [G](https://developers.google.com/search/docs/appearance/site-names)

### Sitelink
- Completamente automatici, ricavati dalla **struttura dei link**; mostrati solo se utili, nessuna garanzia. Aiutano: title e intestazioni informativi e compatti, link interni alle pagine importanti, anchor concisi, niente ripetizioni. Per toglierne uno: `noindex` o eliminare la pagina. [G](https://developers.google.com/search/docs/appearance/sitelinks)
- La **casella di ricerca dei sitelink è stata rimossa il 21/11/2024**: il markup `SearchAction` è inutile ma innocuo; **non rimuovere** il blocco `WebSite` usato per il nome del sito. [G](https://developers.google.com/search/blog/2024/10/sitelinks-search-box)

### Breadcrumb e URL visibile
- Attribuzione del risultato = favicon + nome del sito + URL visibile (dominio + breadcrumb). [G](https://developers.google.com/search/docs/appearance/visual-elements-gallery)
- Dal **23/01/2025 su mobile si vede solo il dominio**; i breadcrumb restano su desktop. `BreadcrumbList` (lista di `ListItem` con `position`, `name`, `item`; tracce multiple ammesse) resta supportato. [G](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs) [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)

### Discover
- Idoneità automatica se il contenuto è **indicizzato** e rispetta le norme di Discover; nessun tag o dato strutturato speciale; idoneità ≠ visualizzazione. [G](https://developers.google.com/search/docs/appearance/google-discover)
- Immagini: **larghezza ≥ 1200 px**, **> 300.000 pixel totali**, proporzioni **16:9**, abilitate da `max-image-preview:large` (o AMP); indicare un'immagine grande e rappresentativa via schema.org o `og:image`, non il logo, non con molto testo. [G](https://developers.google.com/search/docs/appearance/google-discover)
- Niente clickbait, dettagli ingannevoli o esasperati in titolo/snippet/immagine, niente sensazionalismo; titoli che catturano l'essenza; esperienza sulla pagina complessivamente ottima. Può non mostrare candidature, petizioni, moduli, **repository di codice**, satira senza contesto. Report Discover: 16 mesi, sopra una soglia di impressioni. [G](https://developers.google.com/search/docs/appearance/google-discover)
- Core update solo Discover (feb 2026): più contenuti locali per paese, meno clickbait, più competenza **per argomento**. [G](https://developers.google.com/search/blog/2026/02/discover-core-update)

### Core Web Vitals ed esperienza sulla pagina
- Soglie "buono": **LCP < 2,5 s** (dall'inizio del caricamento), **INP < 200 ms**, **CLS < 0,1**. [G](https://developers.google.com/search/docs/appearance/core-web-vitals)
- I CWV **sono usati dai sistemi di ranking**, ma buoni punteggi non garantiscono posizioni; inseguire il punteggio perfetto solo per la SEO può non valere il tempo. Non esiste un singolo "indicatore di esperienza sulla pagina"; gli altri aspetti non contribuiscono direttamente ma sono allineati a ciò che i sistemi premiano. Valutazione per pagina con alcune valutazioni a livello di sito. **La pertinenza prevale.** [G](https://developers.google.com/search/docs/appearance/page-experience)
- Autovalutazione: CWV buoni? HTTPS? Corretto su mobile? Annunci non eccessivi? Nessun interstitial invasivo? Contenuto principale facilmente distinguibile? [G](https://developers.google.com/search/docs/appearance/page-experience)
- Misurare con il report CWV di Search Console (dati reali), PageSpeed Insights, Lighthouse. PSI include test di laboratorio con varianza: contano i **dati di campo**. Resource hints contano solo se migliorano le metriche reali. [G](https://developers.google.com/search/docs/appearance/core-web-vitals) [G OH 2024-06](https://developers.google.com/search/help/office-hours/2024/june) [G OH 2023-08](https://developers.google.com/search/help/office-hours/2023/august)
- Risorse JS/CSS critiche su host separato: sconsigliato per l'overhead di connessione (impatto su LCP). [G](https://developers.google.com/search/blog/2024/12/crawling-december-resources)

### Interstitial e annunci
- Preferire **banner che occupano una piccola parte dello schermo** (anche per installazione app e newsletter). Evitare overlay a tutta pagina e redirect a una pagina separata per consenso o input. [G](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials)
- Interstitial obbligatori (es. verifica età): ammessi, meglio sovrapposti al contenuto e **senza redirect HTTP**; per contenuti adulti consentire a Googlebot verificato l'accesso senza verifica. [G](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials)
- Annunci su mobile: rispettare i Better Ads Standards; il contenuto principale deve restare distinguibile. [G](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)

### Mobile
- Indicizzazione **mobile-first** con Googlebot smartphone. Mobile e desktop devono avere **stessi contenuti principali, intestazioni, title e meta description, meta robots, dati strutturati, alt e qualità delle immagini**; non caricare il contenuto principale solo dopo un'interazione; video facili da trovare. [G](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- URL mobile separati complicano tutto: preferire il responsive. Con m-dot il desktop è il canonico. [G OH 2024-04](https://developers.google.com/search/help/office-hours/2024/april) [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january)

### HTTPS
- Servire il sito in HTTPS (domanda di autovalutazione; report HTTPS in Search Console). I siti HTTP possono essere segnalati come non sicuri in Chrome. [G](https://developers.google.com/search/docs/appearance/page-experience) [G](https://developers.google.com/search/docs/fundamentals/get-started)
- Il passaggio HTTP→HTTPS richiede una nuova proprietà Search Console (o una proprietà Dominio). HSTS non ha effetto sul ranking. [G OH 2024-04](https://developers.google.com/search/help/office-hours/2024/april) [G OH 2023-06](https://developers.google.com/search/help/office-hours/2023/june)

### Date di pubblicazione
- Google stima la data da più fattori; mostrarla non è garantito. Fornire una **data visibile** con etichetta ("Pubblicato", "Ultimo aggiornamento") e/o `datePublished`/`dateModified` in un tipo `CreativeWork` (`Article`, `BlogPosting`, `VideoObject`…). [G](https://developers.google.com/search/docs/appearance/publication-dates)
- Data obbligatoria, ora facoltativa (consigliata con fuso, ISO 8601); **coerenza** tra visibile e dati strutturati; **niente date future** né la data dell'evento descritto; ridurre altre date in pagina. [G](https://developers.google.com/search/docs/appearance/publication-dates)
- Cambiare la data senza modifiche sostanziali è un segnale di contenuti pensati per i motori. `lastmod` in Sitemap solo per modifiche significative. [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january)

### Funzionalità AI (aspetto)
- **Nessun requisito o markup aggiuntivo** per AI Overview e AI Mode. Requisito: pagina **indicizzata e idonea a mostrare uno snippet**; il sito deve essere incluso nelle funzionalità di AI generativa in Search Console. Contenuti importanti **in forma di testo**, dati strutturati coerenti con il testo visibile. [G](https://developers.google.com/search/docs/appearance/ai-features) [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- `llms.txt`, file o Markdown "per l'AI", chunking: **non usati** dalla Ricerca (né positivi né negativi). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Misura: traffico AI incluso nel tipo "Web" del report Rendimento; report sul rendimento dell'AI generativa (impressioni, nessun clic) per tutti dal 31/08/2026; filtro "multimodale" dal 24/09/2026. [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) [G](https://developers.google.com/search/blog/2026/09/web-multimodal-in-sc)

### Contenuti a pagamento (solo se rilevante)
- Un paywall non è cloaking se Google vede tutto il contenuto protetto e si seguono le linee guida del modello di accesso flessibile. Marcare con `isAccessibleForFree: false` e `hasPart` con `cssSelector` (solo selettori `.class`). [G](https://developers.google.com/search/docs/essentials/spam-policies) [G](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content)
- Quota mensile preferibile a quella giornaliera; per news 6–10 articoli/utente/mese, partenza consigliata 10; la soddisfazione cala se il paywall compare oltre il 10% delle volte. [G](https://developers.google.com/search/docs/appearance/flexible-sampling)

### Altri elementi di aspetto
- Tipi di risultato avanzato ritirati da Google nel 2025: Book actions, Course info, ClaimReview, Estimated salary, Learning video, SpecialAnnouncement, Vehicle listing (nessun impatto sul ranking). Altre rimozioni nel changelog `/search/updates`. [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) [G](https://developers.google.com/search/blog/2025/11/update-on-our-efforts)
- Fonti preferite (soprattutto news): solo domini/sottodomini; pulsante JS o deep link `google.com/preferences/source?q=dominio`. [G](https://developers.google.com/search/docs/appearance/preferred-sources)

## Controlli per l'audit
Gravità: **critica** = blocca indicizzazione/visibilità; **alta** = danno probabile o rischio policy; **media** = perdita di qualità o CTR; **bassa** = miglioria.

| ID | Controllo | Come verificarlo | Gravità | Fonte |
|---|---|---|---|---|
| OP-01 | Ogni pagina indicizzabile ha un `<title>` non vuoto | HTML grezzo (curl/view-source) e renderizzato (Controllo URL / headless); cercare `<title></title>` o assente | alta | [G](https://developers.google.com/search/docs/appearance/title-link) |
| OP-02 | Title unici, niente micro-boilerplate | Crawl: raggruppare i title identici; nei siti JS verificare che non restino tutti uguali al template | media | [G](https://developers.google.com/search/docs/appearance/title-link) |
| OP-03 | Title descrittivo: non vago ("Home", "Untitled", nome del framework), non semivuoto (`| Brand`), brand con delimitatore | Regex su title: inizia con delimitatore, lunghezza < 3 parole, parole generiche | media | [G](https://developers.google.com/search/docs/appearance/title-link) |
| OP-04 | Title senza keyword stuffing | Stessa parola/radice ripetuta ≥ 3 volte, liste di varianti separate da virgole | media | [G](https://developers.google.com/search/docs/appearance/title-link) |
| OP-05 | Title nella lingua del contenuto, anni aggiornati | Confronto con `lang`/testo; anno nel title ≠ anno in H1/testo | bassa | [G](https://developers.google.com/search/docs/appearance/title-link) |
| OP-06 | Un titolo principale chiaro (h1 visibile), coerente con title e `og:title` | Contare h1 visibili; segnalare 0 h1 o più intestazioni "principali" di peso uguale (più h1 non è errore di per sé) | media | [G](https://developers.google.com/search/docs/appearance/title-link) |
| OP-07 | Meta description presente almeno su home e pagine chiave | Estrarre `<meta name="description">` per pagina | bassa | [G](https://developers.google.com/search/docs/appearance/snippet) |
| OP-08 | Meta description unica, informativa, non lista di keyword né di 2–3 parole | Duplicati per hash; conteggio virgole/parole ripetute | media | [G](https://developers.google.com/search/docs/appearance/snippet) |
| OP-09 | Nessun `nosnippet`, `max-snippet` basso, `noindex` o `data-nosnippet` involontari sul contenuto principale | Meta robots/googlebot e header `X-Robots-Tag` (curl -I); grep `data-nosnippet`; ricordare l'effetto anche su AI Overview/AI Mode | alta | [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) |
| OP-10 | `data-nosnippet` solo su `span`/`div`/`section`, HTML chiuso, non aggiunto via JS a nodi esistenti | Parser HTML; diff DOM grezzo vs renderizzato | bassa | [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) |
| OP-11 | `<head>` valido: nessun `img`, `iframe` o elemento non ammesso prima di title/meta/canonical/JSON-LD | Parser HTML sull'HTML grezzo: primo elemento non valido nel head e cosa lo segue | alta | [G](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata) |
| OP-12 | HTML < 2 MB (header inclusi) e risorse JS/CSS < 2 MB; metadati e JSON-LD nei primi byte | `curl -s URL \| wc -c`; peso bundle; posizione di `<title>`, canonical, JSON-LD | alta | [G](https://developers.google.com/search/blog/2026/03/crawler-blog-post) |
| OP-13 | Contenuti chiave visibili al caricamento; nessuno script che rimuove `#` o forza lo scroll in cima | Ispezione tab/accordion chiusi; grep `history.replaceState`/`scrollTo(0` al load | bassa | [G](https://developers.google.com/search/docs/appearance/snippet) |
| OP-14 | Navigazione con `<a href>` risolvibili; niente link solo `onclick`, `button`, `select`, `javascript:` | DOM renderizzato: elementi cliccabili senza `href`; crawl con e senza JS | critica | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| OP-15 | Anchor descrittivi; nessun link vuoto; link-immagine con `alt` | Estrarre anchor: "clicca qui", "scopri di più", "qui", testo vuoto | media | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| OP-16 | Nessuna pagina importante orfana; profondità ridotta per le pagine chiave | Crawl dalla home vs Sitemap: URL in Sitemap senza link interni | alta | [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) |
| OP-17 | Nessun routing o contenuto distinto basato su `#` | URL interni con `#/`; contenuti che cambiano solo col frammento | critica | [G](https://developers.google.com/search/docs/crawling-indexing/url-structure) |
| OP-18 | URL leggibili: parole, trattini, minuscole coerenti, `key=value`, niente ID di sessione/timestamp nei link | Regex su URL interni (underscore, maiuscole miste, `sid=`, `?now=`) | bassa | [G](https://developers.google.com/search/docs/crawling-indexing/url-structure) |
| OP-19 | Immagini di contenuto in `<img src>`/`<picture>` con `src` di riserva, non `background-image` | CSS/DOM: elementi con `background-image` che mostrano contenuto (hero, card prodotto/progetto) | media | [G](https://developers.google.com/search/docs/appearance/google-images) |
| OP-20 | `alt` descrittivo sulle immagini significative, senza stuffing; SVG inline con `<title>` | `img` senza `alt` o con alt = nome file; alt con keyword ripetute | media | [G](https://developers.google.com/search/docs/appearance/google-images) |
| OP-21 | Formati supportati, estensione coerente con `Content-Type`; nomi file descrittivi | `curl -I` sulle immagini; pattern `IMG_1234`, `image1`, hash puri | bassa | [G](https://developers.google.com/search/docs/appearance/google-images) |
| OP-22 | Immagine preferita definita (`og:image`/`primaryImageOfPage`/`image` su mainEntity), non logo, alta risoluzione | Estrarre og:image e dimensioni; per Discover larghezza ≥ 1200 px e > 300.000 px | media | [G](https://developers.google.com/search/docs/appearance/google-images) |
| OP-23 | `max-image-preview:large` presente (salvo scelta di limitare) | Meta robots | bassa | [G](https://developers.google.com/search/docs/appearance/google-discover) |
| OP-24 | Nessun lazy loading sulle immagini visibili subito; lazy basato su viewport, non su scroll/clic | `loading="lazy"` su immagine LCP/above the fold; librerie che caricano su evento scroll | media | [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading) |
| OP-25 | Sitemap immagini valida (se le immagini non sono rilevabili dai link), ≤ 1.000 immagini per `<url>`, senza tag ritirati | Parsing XML | bassa | [G](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps) |
| OP-26 | Video incorporati senza interazione e non via `#`; pagina dedicata se il video è il contenuto principale | DOM renderizzato: iframe/video presenti al load (attenzione ai "facade" al clic) | media | [G](https://developers.google.com/search/docs/appearance/video) |
| OP-27 | `VideoObject` con name/description/thumbnailUrl univoci; miniatura ≥ 60x30, URL stabile; nessun `expires` passato | Test dei risultati avanzati; report Indicizzazione video | media | [G](https://developers.google.com/search/docs/appearance/video) |
| OP-28 | Favicon: `link rel="icon"` nella home, file 200 non bloccato, quadrata, > 48x48 consigliato, formato elencato, del brand, URL stabile | curl home + file; robots.txt per Googlebot-Image; dimensioni reali; confronto con icona di default del framework/CMS | media | [G](https://developers.google.com/search/docs/appearance/favicon-in-search) |
| OP-29 | `WebSite` JSON-LD solo in home con `name` + `url` (+ `alternateName`), un solo nodo, nome coerente con `og:site_name`/title/intestazione, non generico | Estrarre JSON-LD dalla home e da pagine interne; validator.schema.org | media | [G](https://developers.google.com/search/docs/appearance/site-names) |
| OP-30 | Varianti della home (http/https, www/non-www) reindirizzate alla canonica; nessuna pagina HTTP di default dimenticata | `curl -I http://dominio` (senza upgrade del browser) e varianti www | alta | [G](https://developers.google.com/search/docs/appearance/site-names) |
| OP-31 | `BreadcrumbList` valido e coerente con il breadcrumb visibile (se presente) | Test dei risultati avanzati | bassa | [G](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb) |
| OP-32 | Markup per funzionalità ritirate (SearchAction, Course info, ClaimReview, ecc.): segnalare come inutili, non come errori | Elenco `@type`/`potentialAction` vs elenco ritiri | bassa | [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results) |
| OP-33 | CWV di campo: LCP < 2,5 s, INP < 200 ms, CLS < 0,1 | Report CWV Search Console / CrUX; se mancano dati di campo, Lighthouse/PSI dichiarando che sono dati di laboratorio | media | [G](https://developers.google.com/search/docs/appearance/core-web-vitals) |
| OP-34 | Cause tipiche di CWV scadenti: immagine LCP lazy o scoperta tardi, immagini senza dimensioni (CLS), JS pesante sul main thread (INP) | Lighthouse "insight", DevTools Performance; elemento LCP reale | media | Deduzione da [G](https://developers.google.com/search/docs/appearance/core-web-vitals) + [SEJ 2026-07, caso web.dev] |
| OP-35 | HTTPS ovunque: redirect 301 http→https, certificato valido, niente mixed content | curl su http; console browser; report HTTPS | alta | [G](https://developers.google.com/search/docs/appearance/page-experience) |
| OP-36 | Mobile: viewport e layout responsive; stessi contenuti, intestazioni, metadati, robots, dati strutturati e alt tra mobile e desktop | Rendering con UA smartphone vs desktop; diff testo/metadati | alta | [G](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) |
| OP-37 | Nessun interstitial a tutta pagina al caricamento; consenso senza redirect a pagina separata; verifica età sovrapposta | Screenshot mobile al load; redirect verso `/consent` o simili | media | [G](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials) |
| OP-38 | Contenuto principale distinguibile; annunci non eccessivi | Screenshot above the fold; densità annunci | media | [G](https://developers.google.com/search/docs/appearance/page-experience) |
| OP-39 | Articoli: data visibile etichettata + `datePublished`/`dateModified` coerenti, ISO 8601 con fuso, nessuna data futura | Confronto testo visibile vs JSON-LD | media | [G](https://developers.google.com/search/docs/appearance/publication-dates) |
| OP-40 | Informazioni importanti come testo HTML (non solo in immagini, canvas, CSS `content`, video, PDF) | Estrarre testo dal DOM renderizzato e confrontarlo con ciò che si vede | alta | [G](https://developers.google.com/search/docs/fundamentals/get-started-developers) |
| OP-41 | Scroll infinito / "carica altro" affiancato da URL paginati con link `<a href>` | Crawl senza interazione: elementi raggiungibili solo con scroll/clic | media | [G](https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading) |
| OP-42 | Contenuti a pagamento marcati (`isAccessibleForFree`, `hasPart`, `cssSelector` `.class`) | JSON-LD delle pagine con paywall | alta (se c'è paywall) | [G](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content) |
| OP-43 | Titoli, snippet e immagini di anteprima non clickbait né sensazionalistici | Revisione manuale di title, og:title, og:image | bassa | [G](https://developers.google.com/search/docs/appearance/google-discover) |
| OP-44 | Nessun `notranslate` involontario | Meta robots/googlebot, `X-Robots-Tag` | bassa | [G](https://developers.google.com/search/docs/appearance/translated-results) |
| OP-45 | Dati strutturati coerenti con il contenuto visibile e validi | Test dei risultati avanzati; confronto valori JSON-LD vs testo | alta | [G](https://developers.google.com/search/docs/appearance/ai-features) |

## Regole per chi costruisce / scrive contenuti
1. **Template di pagina**: `<title>` unico e descrittivo (`Argomento – Brand`), meta description unica, un titolo principale visibile coerente con il title, `og:title`/`og:description`/`og:image` specifici per pagina, `max-image-preview:large`. [G](https://developers.google.com/search/docs/appearance/title-link)
2. **Head pulito e in alto**: title, meta, canonical, hreflang e JSON-LD essenziali all'inizio dell'HTML; niente `img`/`iframe` nel head; HTML ben sotto i 2 MB. [G](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata) [G](https://developers.google.com/search/blog/2026/03/crawler-blog-post)
3. **Siti JavaScript/SPA**: title, meta, canonical e contenuto principale presenti nell'HTML servito o renderizzato per ogni route (SSR/prerender riduce i rischi); verificare con Controllo URL. Deduzione dai documenti Google su rendering e limiti di byte. [G](https://developers.google.com/search/docs/fundamentals/get-started-developers)
4. **Un URL per ogni contenuto**, senza `#`, con parole nella lingua del pubblico e trattini; navigazione con `<a href>`. [G](https://developers.google.com/search/docs/crawling-indexing/url-structure)
5. **Nome del sito deciso subito**: identico in `WebSite.name`, `og:site_name`, title e intestazione della home; `alternateName` con forma breve/acronimo e dominio in minuscolo come riserva; sito su dominio o sottodominio proprio. [G](https://developers.google.com/search/docs/appearance/site-names)
6. **Favicon del brand** quadrata (più grande di 48x48; es. PNG grande + ICO), nell'head della home, URL senza hash che cambia a ogni build. [G](https://developers.google.com/search/docs/appearance/favicon-in-search)
7. **Immagini**: `<img>`/`<picture>` con `src`, `alt`, `width`/`height`; WebP/AVIF ammessi; nomi file descrittivi; niente lazy sull'immagine principale; niente testo importante dentro le immagini. [G](https://developers.google.com/search/docs/appearance/google-images)
8. **Video**: incorporati direttamente; pagina dedicata se il video è il contenuto principale; `VideoObject` + Sitemap video. [G](https://developers.google.com/search/docs/appearance/video)
9. **Link interni**: menu, footer e link contestuali verso le pagine importanti; anchor che si capiscono da soli fuori contesto. [G](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
10. **Scrivere per le persone**: parole che usano i lettori nel titolo, nell'intestazione principale, negli alt e nei link; ordine e numero delle intestazioni liberi; sezioni chiare. [G](https://developers.google.com/search/docs/essentials)
11. **Meta description** come riassunto fattuale (cosa offre la pagina + dati utili: sede, orari, prezzo, autore, data); niente elenchi di keyword. [G](https://developers.google.com/search/docs/appearance/snippet)
12. **Articoli**: data visibile + `datePublished`/`dateModified`; aggiornare la data solo con modifiche sostanziali. [G](https://developers.google.com/search/docs/appearance/publication-dates)
13. **Prestazioni**: budget per rispettare LCP < 2,5 s, INP < 200 ms, CLS < 0,1; JS e CSS critici sullo stesso host; misurare con dati reali dopo il lancio. [G](https://developers.google.com/search/docs/appearance/core-web-vitals)
14. **HTTPS dal primo giorno**, redirect 301 da http e dalla variante www/non-www non preferita. [G](https://developers.google.com/search/docs/fundamentals/get-started)
15. **Popup**: newsletter, consenso e promozioni come banner o dialog parziali, mai overlay a tutta pagina né redirect a pagine di consenso. [G](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials)
16. **Responsive** con gli stessi contenuti su mobile e desktop. [G](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
17. **Nessun markup "per l'AI"**: per AI Overview/AI Mode bastano indicizzazione, idoneità allo snippet, testo chiaro e dati strutturati coerenti. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
18. **Controlli di anteprima** solo per scelte consapevoli: `data-nosnippet` per parti da escludere (es. avvisi cookie, testi legali), sapendo che vale anche per le funzionalità AI. [G](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)

## Note per tipo di sito
**Personal brand / portfolio**
- Nome del sito = nome e cognome o brand personale (un ruolo generico come "Full Stack Developer" non verrebbe scelto); `alternateName` con varianti. [G](https://developers.google.com/search/docs/appearance/site-names)
- Title con nome + ruolo/competenza; evitare "Home", "Profilo", "Progetti" da soli (esempi negativi citati da Google). [G](https://developers.google.com/search/docs/appearance/title-link)
- Una pagina per progetto con testo, immagini `<img>` con alt, eventuale video demo incorporato: più pagine distinte = più query coperte e sitelink possibili. Deduzione. Discover può non consigliare repository di codice: meglio pagine progetto sul sito che solo link a GitHub. [G](https://developers.google.com/search/docs/appearance/google-discover)

**Professionista / attività locale**
- Meta description della home sul modello Google: cosa offre + orari + dove si trova. Title con città/zona dove pertinente. [G](https://developers.google.com/search/docs/appearance/snippet) [G OH 2023-03](https://developers.google.com/search/help/office-hours/2023/march)
- Indirizzo, telefono, orari e servizi come testo HTML (non solo immagini, PDF o widget JS). [G](https://developers.google.com/search/docs/fundamentals/get-started-developers)
- Popup di prenotazione o newsletter come banner, non interstitial. Profilo dell'attività su Google aggiornato (citato anche per le funzionalità AI). [G](https://developers.google.com/search/docs/appearance/ai-features)

**Blog / contenuti**
- Data visibile e coerente con i dati strutturati; immagini grandi (≥ 1200 px) e `max-image-preview:large` per Discover; titoli fedeli, non clickbait. [G](https://developers.google.com/search/docs/appearance/google-discover)
- Autore visibile con link alla pagina autore (dettagli in `content-quality-spam.md`). Meta description con autore/data se utile. [G](https://developers.google.com/search/docs/appearance/snippet)
- Paywall o contenuti riservati: dati strutturati per contenuti a pagamento. [G](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content)

**Ecommerce (breve)**
- Varianti con URL distinti (`/t-shirt/green` o `?color=green`), canonical coerente; immagini prodotto in `<img>` ad alta risoluzione; titoli e descrizioni unici e generabili in modo programmatico se distinti. [G](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) [G](https://developers.google.com/search/docs/appearance/snippet)
- Paginazione con `<a href>` e URL univoci; la prima pagina non è il canonical di tutte. [G](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

## Cosa dicono le fonti terze
- [SEJ 2026-03, news con conferma Google a The Verge] Google ha testato in modo "piccolo e ristretto" titoli riscritti con AI nei risultati di ricerca; analisi citate stimano riscritture "tradizionali" sul 61–76% dei title. Coerente con Google (title automatici); le percentuali sono di terzi.
- [SEJ 2025-10, Clarkson-Bennett, opinione da "Google leak"] ⚠ Regole "max 12 parole / 600 pixel" per i title: non sono limiti Google (nessun limite di caratteri, troncamento per larghezza).
- [SEJ 2026-06, Mueller su Reddit] La meta description non è un requisito ma vale la pena sulle pagine importanti; nessuna penalità. Coerente con Google.
- [SEJ 2026-06, Montti, opinione] ⚠ Description di ~120 caratteri, fattuale, senza CTA o keyword forzate: la parte "fattuale e unica" è in linea con Google; la lunghezza è una scelta dell'autore.
- [SEJ 2026-02, Mueller, caso reale] Una home HTTP di default rimasta attiva accanto a quella HTTPS ha causato nome del sito e favicon errati: Chrome fa l'upgrade, Googlebot no. Verificare con curl.
- [SEJ 2026-02, Bill Hunt, caso enterprise] `WebSite` messo su ogni pagina-sede ha fatto mostrare una sede come nome del sito: tenere `WebSite` solo in home (coerente con Google).
- [SEJ 2026-03, Mueller] Per nomi legacy dopo un rebrand di solito funziona il nome di dominio come nome alternativo (coerente con la doc).
- [SEJ 2026-03, news doc Google] Tre modi per indicare l'immagine preferita (`primaryImageOfPage`, `image` su mainEntity, `og:image`): coerente con Google.
- [SEJ 2026-07, caso web.dev Nuvemshop segnalato da Mueller] LCP migliorato togliendo transizioni CSS in alto, `loading="lazy"` dalla prima immagine e usando `fetchpriority="high"` su 1–2 immagini; verificare prima quale sia l'elemento LCP reale. Dati autodichiarati.
- [SEJ 2025-12 e 2026-05, HTTP Archive/CrUX] Quota di siti con CWV buoni per piattaforma (es. aprile 2026: Duda ~85%, Wix ~80%, Shopify ~79%, WordPress ~49%); peso pagina e punteggio Lighthouse non prevedono i CWV reali. Dati descrittivi, non causali.
- [SEJ 2025-12, news] Safari 26.2 espone LCP e INP via RUM; CrUX, PSI e Search Console restano basati su Chrome: per gli utenti Safari servono misure proprie.
- [SEJ 2025-11, Mueller] Un video hero pesante caricato in background dopo il contenuto non dovrebbe avere effetti SEO visibili.
- [SEJ 2026-05, news doc Google] Rich result FAQ non più mostrati dal 7/5/2026: il markup `FAQPage` è innocuo ma inutile per Google. ⚠ Contro i consigli che lo indicano come "critico per GEO". Da verificare nel changelog Google.
- [SEJ 2026-09, Mueller] Nel report AI di Search Console i link di un AI Overview ereditano la posizione del blocco: la "posizione" lì è poco utile, meglio misurare esiti.
- [SEJ 2025–2026, vari autori] ⚠ "Struttura citabile" (risposta in 2–3 frasi, paragrafi corti, H2 come domande) per farsi citare dalle AI: ipotesi da correlazioni su ChatGPT, non indicazione Google. Google: nessuna ottimizzazione speciale, chunking non necessario.
- [SEJ 2025-10, news Bing] Anche Bing supporta `data-nosnippet` per snippet e risposte Copilot.

## Miti e consigli obsoleti
- **"Il title deve stare sotto N caratteri/pixel"**: Google non fissa limiti; tronca in base al dispositivo. [G](https://developers.google.com/search/docs/appearance/title-link)
- **"La meta description deve avere 150–160 caratteri"**: nessun limite. [G](https://developers.google.com/search/docs/appearance/snippet)
- **Meta keywords**: non usato da Google. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- **"Un solo H1 e heading in ordine perfetto per il ranking"**: numero e ordine non contano per la Ricerca (contano per l'accessibilità). [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- **"Title = H1 = URL"**: non serve. [G OH 2024-06](https://developers.google.com/search/help/office-hours/2024/june)
- **Keyword nel dominio/URL come leva di ranking**: effetto quasi nullo; Google non dà troppo credito ai domini creati per corrispondere a una query. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide)
- **Casella di ricerca dei sitelink (`SearchAction`)**: rimossa dal 21/11/2024. [G](https://developers.google.com/search/blog/2024/10/sitelinks-search-box)
- **Breadcrumb visibili nei risultati mobile**: dal 23/01/2025 solo dominio su mobile. [G](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs)
- **Rich result per Course info, Fact check, Estimated salary, Learning video, SpecialAnnouncement, Book actions, Vehicle listing**: ritirati nel 2025. [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results)
- **"Nome del sito solo per il dominio, non per i sottodomini"** (OH maggio 2023): superato, oggi sono supportati anche i sottodomini. [G](https://developers.google.com/search/docs/appearance/site-names)
- **"INP non fa parte dei Core Web Vitals"** (OH settembre 2023): superato; la doc attuale elenca LCP, INP, CLS (FID non compare più). [G](https://developers.google.com/search/docs/appearance/core-web-vitals)
- **"Punteggio Lighthouse/PSI = ranking"**: contano i dati reali; il punteggio perfetto non è un obiettivo SEO. [G](https://developers.google.com/search/docs/appearance/page-experience) [G OH 2024-06](https://developers.google.com/search/help/office-hours/2024/june)
- **`rel="next"`/`rel="prev"`**: non più usati da Google. [G](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
- **Copia cache come indicatore**: link alla cache rimosso nel 2024, mai stato segnale di qualità. [G OH 2024-04](https://developers.google.com/search/help/office-hours/2024/april)
- **EXIF delle immagini come segnale**: non usato. [G OH 2023-01](https://developers.google.com/search/help/office-hours/2023/january)
- **Validazione W3C, ARIA, `<article>`, HSTS, HTTP/3 come fattori di ranking**: nessun effetto diretto (head valido sì, per leggere i metadati). [G OH 2023-08](https://developers.google.com/search/help/office-hours/2023/august) [G OH 2023-06](https://developers.google.com/search/help/office-hours/2023/june) [G](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata)
- **`llms.txt`, Markdown per bot, schema "per l'AI", chunking**: ignorati dalla Ricerca Google. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **Spostare JS/CSS critici su un sottodominio/CDN separato "per il crawl budget"**: sconsigliato dal 6/12/2024 per le prestazioni. [G](https://developers.google.com/search/blog/2024/12/crawling-december-resources)
- **"Il testo dentro le immagini basta, Google fa OCR"**: per i risultati web serve testo HTML (alt, didascalie, testo). [G OH 2022-12](https://developers.google.com/search/help/office-hours/2022/december)
