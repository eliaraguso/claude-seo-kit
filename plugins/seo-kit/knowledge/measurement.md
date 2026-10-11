# Misurazione: Search Console, GA4, Bing, visibilità AI, diagnosi dei cali

> Aggiornato al 2026-10-03. Fonte primaria: Google. Secondaria: SEJ (ott 2025–ott 2026).
> Legenda: **[G](url)** = documentazione o blog ufficiale Google · **[D]** = deduzione di questo file · **[SEJ AAAA-MM, autore, tipo, campione]** = fonte terza riportata da Search Engine Journal · ⚠ = va oltre o contro Google.
> Forza dell'evidenza per le fonti terze: **Forte** (annuncio/doc ufficiale del fornitore riportato) · **Media** · **Debole** (campione piccolo, vendor, aneddoto) · **Opinione**.
> Una skill senza accesso ai dati del proprietario può solo preparare istruzioni, regex, checklist e leggere export forniti dall'utente. Ricerca AI: `ai-search.md`. Miti: `myths-deprecated.md`.

## Indice
- [Fatti e regole (Google)](#fatti-e-regole-google)
  - [Search Console: ruolo e uso](#search-console-ruolo-e-uso)
  - [Proprietà: Dominio, prefisso URL, piattaforma](#proprietà-dominio-prefisso-url-piattaforma)
  - [Report chiave](#report-chiave)
  - [Filtro query con brand](#filtro-query-con-brand)
  - [Report sul rendimento dell'AI generativa](#report-sul-rendimento-dellai-generativa)
  - [Affidabilità dei dati e limiti](#affidabilità-dei-dati-e-limiti)
  - [Oltre i 16 mesi: API ed esportazioni](#oltre-i-16-mesi-api-ed-esportazioni)
  - [Search Console + Google Analytics](#search-console--google-analytics)
  - [Tempi attesi](#tempi-attesi)
- [Controlli / procedure](#controlli--procedure)
  - [Tabella controlli](#tabella-controlli)
  - [Procedura: diagnosi di un calo di traffico](#procedura-diagnosi-di-un-calo-di-traffico)
  - [Procedura: misurare la visibilità negli assistenti AI](#procedura-misurare-la-visibilità-negli-assistenti-ai)
  - [Procedura: GA4 per traffico AI e contatti](#procedura-ga4-per-traffico-ai-e-contatti)
- [Cosa dicono le fonti terze](#cosa-dicono-le-fonti-terze)
- [Note per tipo di sito](#note-per-tipo-di-sito)

---

## Fatti e regole (Google)

### Search Console: ruolo e uso
- Strumento ufficiale per capire scansione, indicizzazione e rendimento nella Ricerca. Google consiglia di usarlo **vivamente**, con o senza strumenti terzi. [G](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- Non serve entrare ogni giorno: i nuovi problemi arrivano via **email**; controllare **circa una volta al mese** o dopo modifiche al sito. [G](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- Primi passi: verificare la proprietà → report di indicizzazione (correggere errori/avvisi) → valutare l'invio di una Sitemap (non obbligatoria, può velocizzare la scoperta) → monitorare il report sul rendimento. [G](https://developers.google.com/search/docs/monitor-debug/search-console-start)
- Verificare Search Console (o cambiare metodo di verifica) **non influisce** su indicizzazione o ranking; serve a ricevere notifiche su azioni manuali, sicurezza, rimozioni legali. [G](https://developers.google.com/search/help/office-hours/2023/january) · [G](https://developers.google.com/search/help/small-business-notifications)
- Solo le **azioni manuali** sono comunicate; le variazioni algoritmiche no. [G](https://developers.google.com/search/help/office-hours/2022/december)

### Proprietà: Dominio, prefisso URL, piattaforma
- **Proprietà Dominio**: copre http/https, www/non-www e tutti i sottodomini; è la scelta consigliata per avere un quadro completo. Con una proprietà **prefisso URL**, il passaggio HTTP→HTTPS richiede una nuova proprietà. [G](https://developers.google.com/search/help/office-hours/2024/april) · [G](https://developers.google.com/search/help/crawling-index-faq)
- Sottodomini e sottodirectory si possono aggiungere come proprietà separate senza nuova verifica se il dominio è già verificato. [G](https://developers.google.com/search/help/office-hours/2023/june)
- Il **filtro query con brand** è disponibile solo per proprietà **di primo livello** (non prefisso di percorso, non sottodominio). [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- I dati appartengono alla proprietà, non all'utente che verifica; se la verifica decade a lungo i dati mancanti non si recuperano; il limite di proprietà per account non si alza. Meglio non dipendere dall'account personale di un dipendente o di un'agenzia. [G](https://developers.google.com/search/help/office-hours/2024/august) · [G](https://developers.google.com/search/help/office-hours/2022/december) · [G](https://developers.google.com/search/help/office-hours/2024/april)
- Quando un ex proprietario (agenzia, sviluppatore) esce: **rimuovere anche i suoi token di verifica** (Utenti e autorizzazioni → Token di proprietà inutilizzati → Rimuovi → Verifica rimozione), altrimenti può riottenere l'accesso. [G](https://developers.google.com/search/blog/2024/04/search-console-ownership-token-management)
- A un consulente per un audit dare **solo accesso in lettura**. [G](https://developers.google.com/search/docs/fundamentals/do-i-need-seo)
- **Proprietà della piattaforma** (luglio 2026, globali dal 29/7/2026): account **Instagram, TikTok, X, YouTube** come proprietà, anche per creator senza sito; report Rendimento (clic, impressioni, post, query, export), Insights, Obiettivi. Chi ha rivendicato il **profilo della Ricerca** vede gli account aggiunti automaticamente. LinkedIn e GitHub non sono tra le piattaforme citate. [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) · [G](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content)

### Report chiave
| Report / funzione | A cosa serve | Note | Fonte |
|---|---|---|---|
| Rendimento (Risultati di ricerca) | Clic, impressioni, CTR, posizione media per query, pagina, paese, dispositivo, aspetto nella ricerca, data | Filtro **Tipo di ricerca**: Web, Immagini, Video, Notizie (+ filtro **multimodale** dal 24/9/2026). AI Overviews e AI Mode sono inclusi nel tipo **Web** | [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/blog/2026/09/web-multimodal-in-sc) |
| Rendimento Discover / Google News | Superfici separate | Discover: solo sopra una soglia minima di impressioni; ha core update propri (feb 2026) | [G](https://developers.google.com/search/docs/appearance/google-discover) |
| Vista **24 ore** | Dati orari, ritardo di poche ore | Linea tratteggiata = dati parziali; fuso del browser | [G](https://developers.google.com/search/blog/2024/12/recent-data-search-console) |
| Granularità giornaliera/settimanale/mensile | Tendenze e confronti | Cambia leggermente il formato dell'export | [G](https://developers.google.com/search/blog/2025/12/weekly-monthly-views-search-console) |
| **Annotazioni** | Segnare deploy, migrazioni, contenuti, campagne, update | Clic destro sul grafico, max 120 caratteri; visibili a tutti gli utenti della proprietà: niente dati personali | [G](https://developers.google.com/search/blog/2025/11/custom-chart-annotations) |
| Configurazione con AI (sperimentale) | Impostare filtri/confronti in linguaggio naturale | Solo Rendimento Ricerca; può sbagliare i filtri: verificarli | [G](https://developers.google.com/search/blog/2025/12/ai-powered-configuration) |
| Insights (Approfondimenti) | Clic/impressioni vs periodo precedente, pagine e query in crescita/calo, Obiettivi (28 giorni) | Integrato nell'interfaccia dal 2025; **gruppi di query** (AI) solo per proprietà ad alto volume | [G](https://developers.google.com/search/blog/2025/06/search-console-insights) · [G](https://developers.google.com/search/blog/2025/10/search-console-query-groups) |
| Indicizzazione delle pagine | Pagine indicizzate/escluse e motivi | Leggere come pattern; 404 previsti non sono un problema | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Controllo URL | Stato nell'indice, test live, HTML renderizzato, screenshot, richiesta di scansione | Più affidabile di `site:` | [G](https://developers.google.com/search/docs/monitor-debug/search-operators) |
| Statistiche di scansione | Richieste, risposte, tipo di Googlebot, tempi | Da guardare insieme a Indicizzazione per i problemi tecnici | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Azioni manuali · Problemi di sicurezza | Penalità manuali, malware/phishing | Controllo obbligato in ogni calo | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Core Web Vitals · HTTPS | Dati di campo reali | | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Stato risultati avanzati | Errori/avvisi sui dati strutturati letti | I tipi ritirati spariscono dai report | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Rimozioni · Cambio di indirizzo | Nascondere URL (~6 mesi) · migrazione di dominio/sottodominio | Cambio di indirizzo non serve per HTTP→HTTPS o www | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| Consigli (Recommendations) | Suggerimenti automatici in Panoramica | Sperimentale, solo se disponibili | [G](https://developers.google.com/search/blog/2024/08/search-console-recommendations) |
| Pagina **Anomalie dei dati** | Errori di logging e cambi di trattamento dati | Da controllare prima di interpretare un calo | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |

### Filtro query con brand
- Filtro **Con brand / Non correlate al brand** nel report Rendimento (web, immagini, video, notizie) e scheda in Insights. Query con brand = nome del brand, varianti e refusi, prodotti/servizi unici del brand. Classificazione con un **sistema interno assistito da AI** (non regex), multilingue, con possibili errori; **nessun effetto sul ranking**. Solo proprietà di primo livello con volume sufficiente; disponibile per tutti i siti idonei dall'11/3/2026. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Se il filtro non compare (sito piccolo, proprietà prefisso): usare un filtro regex sulle query con il nome e i suoi refusi, es. `(?i)mario ?rossi|rossi ?mario|m\.? ?rossi` [D] (metodo regex in [SEJ 2025-12, guida diagnosi cali, opinione]).

### Report sul rendimento dell'AI generativa
- Fatti Google: report dedicati alla visibilità nelle funzionalità di AI generativa di **Ricerca (AI Overviews e AI Mode)** e **Discover**; metriche: **impressioni**, pagine apparse, paesi, dispositivi (solo Ricerca), date con granularità oraria/giornaliera/settimanale/mensile. I dati restano anche nel report Rendimento complessivo. Lancio 3/6/2026 su un sottoinsieme, **disponibile per tutti i siti dal 31/8/2026**. [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) ([help](https://support.google.com/webmasters/answer/16984139)) Il post cita solo impressioni, non clic.
- È lo strumento indicato da Google per misurare la visibilità nelle funzioni generative (anche Discover). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Come leggerlo (dettagli da SEJ, fonti Google/Mueller riportate):
  - nessuna **query**, nessun **clic**, CTR, posizione, passaggio citato; nessuna API né BigQuery, solo export dalla UI; export per pagina limitato a 1.000 righe [SEJ 2026-08/09, news + Mueller, Forte];
  - un'impressione conta quando il link è visibile; i link dietro "mostra altro" contano solo se l'utente espande; nel grafico due URL nella stessa risposta valgono 1 per la proprietà, nella tabella 1 per pagina [SEJ 2026-08, news, Forte];
  - nel report Rendimento un link dentro un AI Overview **eredita la posizione del blocco**; i follow-up di AI Mode contano come nuove query (compaiono query tipo "yes go on") [SEJ 2026-08/09, Mueller, Forte];
  - dati recenti preliminari; non sommare impressioni AI e organiche né calcolare un CTR misto [SEJ 2026-08, opinione dell'autrice].
- ⚠ Discrepanza di date: un articolo SEJ indica il report "live per tutti dall'11/8/2026" [SEJ 2026-08]; il blog Google dice 31/8/2026. Usare la data Google.
- Regex per isolare gli artefatti conversazionali nel campo Query: `^(yes|yeah|ok|okay|sure)[?!.,]*$` [SEJ 2026-08, tattica di un autore].

### Affidabilità dei dati e limiti
- **Bug delle impressioni**: errore di logging che ha **gonfiato le impressioni dal 13/5/2025 al 27/4/2026** (clic non toccati), corretto senza ricalcolare lo storico. CTR e posizione media del periodo sono falsati. Trattare fine aprile 2026 come **discontinuità**; nei confronti usare i clic. [SEJ 2026-04/06/10, news sulla pagina Anomalie dei dati di Google, Forte] (Google invita a controllare quella pagina in ogni analisi. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops))
- Fuso orario fisso **Pacific Time**; dati in ritardo di **un paio di giorni** (vista 24 ore a parte); Search Console riporta solo l'**URL canonico**; separa web, immagini, video, notizie, Discover; non filtra necessariamente i bot. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- I totali filtrati possono superare il totale complessivo per l'uso di filtri di Bloom (velocità a scapito della precisione). [G](https://developers.google.com/search/help/office-hours/2023/september)
- Le query rare sono anonimizzate: a livello di query manca una quota grande dei dati (~75% delle impressioni e ~38% dei clic in 10 siti SaaS). [SEJ 2026-01, Indig, 10 siti B2B, Debole-Media] → confrontare sempre il totale aggregato con la somma delle query.
- Dopo la rimozione del parametro `num=100` (settembre 2025) le impressioni si sono normalizzate (meno impressioni "da tool"). [SEJ 2026-01, Indig, Debole]
- Query strane nel report: i dati sono reali (ciò che è stato mostrato); restringere per paese/tipo/periodo. [G](https://developers.google.com/search/help/office-hours/2023/may)
- Posizione media: non ossessionarsi sul valore assoluto; impressioni e clic sono le metriche principali. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)

### Oltre i 16 mesi: API ed esportazioni
- L'interfaccia mostra **16 mesi**. Per conservare di più: **API Search Analytics** o **esportazione collettiva in BigQuery**, archiviando i dati nei propri sistemi. [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
- API con dimensione `HOUR` e `dataState: HOURLY_ALL`: dati orari fino a **10 giorni** (la UI solo 24 ore). [G](https://developers.google.com/search/blog/2025/04/san-hourly-data)
- Nell'export BigQuery i campi dei rich result ritirati sono `NULL` dal 1/10/2025: nelle query usare `IS NOT TRUE` invece di `NOT campo`. [G](https://developers.google.com/search/blog/2025/06/simplifying-search-results)
- Per siti piccoli [D]: un export mensile (CSV o Sheets via API) di query, pagine, paesi, dispositivi è sufficiente come archivio.

### Search Console + Google Analytics
- Search Console = cosa accade **prima** della visita (impressioni, clic, query); Google Analytics = cosa accade **sul sito** (pagine, coinvolgimento, conversioni, canali). Fonte di verità: GSC per il rendimento in Ricerca, GA per il comportamento. Metriche più confrontabili: **clic GSC vs sessioni GA**, che non coincideranno: contano le tendenze. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Modello Looker Studio ufficiale: GSC tabella "Impressione URL"; GA filtrato `Session source = google` e `Session medium = organic`; intervallo predefinito 28 giorni. Metriche: sessioni, **tasso di coinvolgimento** (sessione con evento chiave, oppure >10 secondi, oppure ≥2 pagine viste), utenti di ritorno, clic, CTR. Nessuna percentuale "giusta" di traffico organico. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Cause di discrepanza: tag GA mancante su alcune pagine, consenso cookie rifiutato, fuso orario, modello di attribuzione (il predefinito di GA è il più simile), URL canonici, suddivisioni del traffico, pagine non HTML (PDF: attivare la misurazione avanzata), bot. Per la massima precisione: export GSC + export GA4 in BigQuery. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Google invita a misurare il **valore delle visite** (vendite, registrazioni, contatti), non solo i clic, anche per il traffico dalle funzioni AI. [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- Strumenti di collegamento: collegare GSC a GA; Site Kit per WordPress. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Google Trends per stagionalità e confronto con il settore (fino a 5 termini; intervalli 30/90 giorni per la notorietà di un nome). [G](https://developers.google.com/search/docs/monitor-debug/trends-start)

### Tempi attesi
| Evento | Tempo indicato | Fonte |
|---|---|---|
| Effetto di una modifica SEO | Da poche ore a diversi mesi; attendere alcune settimane per valutare | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| Ri-scansione dopo una correzione | Di solito alcuni giorni | [G](https://developers.google.com/search/help/debug) |
| Core update | Rollout fino a ~2 settimane; analizzare **almeno una settimana dopo la fine**, confrontando con una settimana prima dell'inizio; recupero in giorni o diversi mesi, a volte al core update successivo | [G](https://developers.google.com/search/docs/appearance/core-updates) |
| Miglioramenti dopo un calo significativo | Ricontrollare dopo alcune settimane; i sistemi possono impiegare mesi | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Migrazione di sito medio | Alcune settimane, di più per siti grandi | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| Controlli di anteprima (nosnippet ecc.) | Da giorni a mesi | [G](https://developers.google.com/search/docs/appearance/ai-features) |
| Recupero da spam | Mesi di conformità rilevata | [G](https://developers.google.com/search/docs/appearance/spam-updates) |
| Richiesta di riconsiderazione | Diverse settimane | [G](https://developers.google.com/search/help/site-position-in-search-faq) |
| Primo citazione AI di un contenuto nuovo | Mediana ~6,8 giorni | [SEJ 2026-07, Profound, vendor, Debole] |

---

## Controlli / procedure

### Tabella controlli
| ID | Cosa | Come (strumento, passi) | Priorità | Fonte |
|---|---|---|---|---|
| ME-01 | Proprietà Dominio verificata | Verifica via DNS; se esistono solo proprietà prefisso, aggiungere quella Dominio; tenere le prefisso per sezioni | Alta | [G](https://developers.google.com/search/help/office-hours/2024/april) |
| ME-02 | Accessi e token puliti | Utenti e autorizzazioni: proprietari attuali, ex agenzie rimosse, token inutilizzati rimossi; consulenti solo in lettura | Alta | [G](https://developers.google.com/search/blog/2024/04/search-console-ownership-token-management) |
| ME-03 | Sitemap inviata e letta | Report Sitemap: stato, URL rilevati; nessun URL non canonico o non 200 | Media | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| ME-04 | Baseline prima di ogni intervento | Export 16 mesi (query, pagine, paesi, dispositivi), brand vs non brand, report AI; annotazione "baseline" | Alta | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| ME-05 | Annotazioni sistematiche | Annotare lanci, migrazioni, template, plugin, campagne, core/spam update (dal Search Status Dashboard) | Media | [G](https://developers.google.com/search/blog/2025/11/custom-chart-annotations) |
| ME-06 | Brand vs non brand | Filtro con brand (se disponibile) o regex del nome; seguire le due curve separatamente | Alta | [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter) |
| ME-07 | Visibilità nelle funzioni AI di Google | Report AI generativa: pagine con impressioni AI, trend; non sommare a quelle organiche | Media | [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) |
| ME-08 | Discontinuità del bug impressioni | Nei confronti 2025–2026 usare i clic; segnalare nei report il periodo 13/5/2025–27/4/2026 | Alta | [SEJ 2026-04/10, news Google] |
| ME-09 | Archivio oltre 16 mesi | Export mensile via API o BigQuery | Media (Alta per siti grandi) | [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) |
| ME-10 | GSC collegato a GA4 | Collegamento in GA4; dashboard Looker Studio clic vs sessioni organiche | Media | [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console) |
| ME-11 | Eventi chiave di contatto in GA4 | Vedi procedura GA4: form, tel:, mailto:, prenotazione, download CV/PDF | Alta | [G](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search), [D] |
| ME-12 | Traffico AI segmentato | Canale predefinito "AI Assistant" + gruppo personalizzato per referrer non riconosciuti; controllare il "Direct" sulle pagine più citate | Media | [SEJ 2026-05, news Google Analytics, Forte] |
| ME-13 | Campo "Come ci hai conosciuto?" | Campo nel modulo di contatto/prenotazione (opzioni: Google, ChatGPT/altro assistente AI, social, passaparola, altro + testo libero); domanda al telefono | Alta per siti a lead | [SEJ 2026-07/08, Forrester e dati agenzia, Opinione/Debole] |
| ME-14 | Bing Webmaster Tools | Verificare il sito (anche import da GSC), sitemap, report AI Performance (citazioni, grounding query) | Media | [SEJ 2026-02/06, news Microsoft, Forte] |
| ME-15 | Microsoft Clarity (facoltativo) | Installare se accettabile per privacy/consenso: comportamento + citazioni Copilot e grounding query | Bassa | [SEJ 2026-05, news Microsoft, Forte] |
| ME-16 | Set fisso di prompt AI | Vedi procedura; frequenza mensile o trimestrale | Media | [SEJ 2026-07/09, più autori, Opinione] |
| ME-17 | Log del server per bot AI e Googlebot | 30 giorni di log; verifica IP/reverse DNS; pagine più scansionate | Bassa (Media per siti grandi) | [G](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests), [SEJ 2026-07, Pollitt] |
| ME-18 | Profilo dell'attività in GA4 | Collegare il Business Profile a GA4 (metriche di chiamate/indicazioni); profili raggruppati in un account manager vanno prima separati | Media (locale) | [SEJ 2026-06, news Google, Forte] |
| ME-19 | Controllo mensile | Email GSC, Indicizzazione, Azioni manuali, Sicurezza, Rendimento vs mese/anno precedente | Media | [G](https://developers.google.com/search/docs/monitor-debug/search-console-start) |
| ME-20 | Nessuna metrica "interna Google" da tool terzi | Etichettare DA/DR, "visibility score", "AI score" come metriche del vendor | Media | [G](https://developers.google.com/search/docs/fundamentals/third-party-seo) |
| ME-21 | Proprietà della piattaforma | Se il brand pubblica su YouTube/Instagram/TikTok/X: aggiungerle, confrontare formati e post | Bassa-Media | [G](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) |

### Procedura: diagnosi di un calo di traffico
Ordine pensato per escludere prima le cause banali. Fonti principali: [G](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) · [G](https://developers.google.com/search/docs/appearance/core-updates); integrazioni terze segnalate.
1. **È un problema di misura?** Il calo c'è in tutti i canali GA4? GSC e GA4 divergono? Tag mancante dopo un rilascio, consenso cookie cambiato, CDN che blocca script? [SEJ 2025-10/12, checklist di più autori] · pagina **Anomalie dei dati** di GSC e bug impressioni 2025–2026. [G]
2. **Incidenti e update noti**: Search Status Dashboard (incidenti, core/spam update con date). Se c'è un core update in corso, attendere la fine + una settimana. [G](https://developers.google.com/search/help/status-dashboard)
3. **Forma del grafico** (16 mesi): crollo improvviso → update, sicurezza, spam, problema tecnico a livello di sito; calo lento → `noindex` errato su pagine (dipende dalla riscansione) o interessi che cambiano; calo ricorrente → stagionalità. [G]
4. **Confronto**: ultimi 3 mesi vs periodo precedente e vs anno precedente; scorrere tutte le schede (query, pagine, paesi, dispositivi, aspetto nella ricerca). [G]
5. **Clic vs impressioni**: entrambi giù → cause sopra; impressioni stabili e clic giù → title/snippet poco efficaci o concorrenti con risultati più ricchi. [G] Considerare anche la comparsa di AI Overviews sulle query principali (CTR in calo con AIO) [SEJ 2026-03/05, più studi, Media].
6. **Brand vs non brand**: un calo solo non-brand indica concorrenza/ranking; un calo brand indica domanda o reputazione. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
7. **Tipo di ricerca**: Web, Immagini, Video, Notizie separati; Discover separato (ha core update propri). [G]
8. **Pagine colpite**: tabella Pagine ordinata per "Differenza di clic"; tutto il sito → report Indicizzazione; un gruppo di pagine → Controllo URL su alcune. [G]
9. **Entità della perdita di posizione**: piccola (es. 2→4) → fluttuazione, niente modifiche radicali; grande (es. top 10 → 29) su molti termini → valutare l'intero sito con le domande sui contenuti utili. [G]
10. **Tecnica**: Statistiche di scansione (picchi di errori, tempi di risposta), Indicizzazione, robots.txt, server/DNS, CDN/WAF che bloccano Googlebot, `noindex`/canonical da staging. [G]
11. **Sicurezza e spam**: report Problemi di sicurezza e Azioni manuali. [G]
12. **Domanda esterna**: una query alla volta su Google Trends per distinguere calo del sito da calo del settore. [G]
13. **Migrazione o redesign recente**: redirect 301 uno a uno, nessun `noindex` dimenticato, canonical aggiornati, contenuti/title non rimossi; Internet Archive per confrontare. [G](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [SEJ 2026-06, guida, Opinione]
14. **Decisione**: niente modifiche rapide "perché si dice"; miglioramenti sostanziali; eliminare contenuti solo come ultima risorsa; non comprare link. [G](https://developers.google.com/search/docs/appearance/core-updates)
15. **Annotare** le azioni e ricontrollare dopo alcune settimane. [G]

### Procedura: misurare la visibilità negli assistenti AI
Non esiste una metrica ufficiale di terzi; Google indica il proprio report AI e mette in guardia dagli strumenti che promettono metriche interne. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) La procedura sotto è una sintesi di pratiche SEJ (Opinione; risultati solo come tendenza).
1. **Accuratezza prima della visibilità**: 5–10 prompt di fatti (chi è / cos'è [nome], dove opera, cosa offre, prezzi, è affidabile?) per verificare che le risposte siano corrette; classificare ogni affermazione: corretta, obsoleta, non supportata, falsa, riferita a un altro soggetto. [SEJ 2026-07/09, Manic, Forrester]
2. **Set fisso di prompt decisionali**: 10–20 prompt reali del pubblico (da domande dei clienti, query GSC, recensioni), es. "migliore [servizio] a [città]", "alternative a…", "[servizio] online costi". Non cambiarli tra una rilevazione e l'altra. [SEJ 2026-08, consulente, ~12 startup]
3. **Motori**: AI Overviews/AI Mode, ChatGPT, Gemini, Perplexity, Copilot (e Claude se rilevante); misurare **per motore**, non con un punteggio unico (fonti citate quasi mai coincidenti). [SEJ 2026-05, Indig/Omnia]
4. **Ripetizioni**: almeno 3–5 esecuzioni per prompt e motore, in conversazioni nuove senza memoria; annotare data, account (free/a pagamento), modello, località, lingua. Le liste cambiano quasi a ogni richiesta (~1.500 ripetizioni servirebbero per due liste identiche; accordo sul primo brand tra 3 modelli 41,6%). [SEJ 2026-07, Fishkin/SparkToro; SEJ 2026-08]
5. **Registro** (foglio): per ogni esecuzione: citato con link / nominato senza link / assente; URL citato; concorrenti nominati; lunghezza della risposta e numero di brand (una risposta più lunga gonfia la presenza). [SEJ 2026-07, Manic]
6. **Lettura**: percentuale di presenza per motore e per gruppo di prompt; confrontare trimestre su trimestre, non singole risposte. Un esempio di soglia d'allarme proposto: presenza in meno di 12 esecuzioni su 20. [SEJ 2026-08, consulente, caso singolo] [D: soglia indicativa]
7. **Frequenza**: mensile per siti con attività di PR/contenuti, trimestrale per siti piccoli. [SEJ 2025-12/2026-06, più autori]
8. **Test di raggiungibilità**: cercare in ChatGPT una frase esatta della pagina per verificare che sia recuperabile. [SEJ 2026-10, Chris Green, tattica]
9. **Collegare a esiti**: incrociare con traffico AI in GA4, ricerche di brand in GSC e risposte "Come ci hai conosciuto?". La presenza nelle risposte non è un ranking né un KPI di business. [SEJ 2026-07, Forrester; Manic]

### Procedura: GA4 per traffico AI e contatti
- **Canale predefinito "AI Assistant"** (dal 13/5/2026, medium `ai-assistant`): assegna automaticamente i referrer riconosciuti (citati ChatGPT, Gemini, Claude); elenco completo non pubblico; nessun dato retroattivo. Secondo un autore non riconosce Perplexity. [SEJ 2026-05/07/10, news Google Analytics, Forte; Pollitt per Perplexity]
- **Gruppo di canali personalizzato** per i referrer non coperti [D, da verificare sui referrer reali della proprietà]: condizione "Sorgente sessione corrisponde a regex", posizionato **prima** di Referral:
  ```
  (^|\.)(chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|meta\.ai|grok\.com|chat\.mistral\.ai|chat\.deepseek\.com)$
  ```
  Domini di partenza indicati da [SEJ 2025-10, guida]: chatgpt.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com. ChatGPT aggiunge spesso `utm_source=chatgpt.com` ai link; anche Gemini aggiunge UTM [SEJ 2026-03/06/09]. Gli utenti dell'app o senza referrer finiscono in "Direct".
- **Eventi chiave** consigliati [D, coerenti con l'invito Google a misurare conversioni]: invio modulo contatti/prenotazione (`generate_lead`), clic su `tel:`, `mailto:`, WhatsApp, link di prenotazione esterna, download CV/PDF (misurazione avanzata `file_download`); per i locali, chiamate e indicazioni dal Business Profile collegato.
- **Esplorazioni**: canalizzazione con segmento organico/AI per vedere dove si perdono i contatti [SEJ 2025-12, tutorial, Opinione]; report Pagina di destinazione filtrato su organico Google. [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- Non pretendere che GA4, GSC e CRM coincidano: una fonte di verità per domanda (visibilità = GSC, comportamento = GA4, lead = CRM o registro contatti). [SEJ 2026-04, guida, Opinione] coerente con [G](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)

---

## Cosa dicono le fonti terze
- **Bing Webmaster Tools – AI Performance**: public preview da febbraio 2026 con citazioni totali, pagine citate al giorno, citazioni per pagina e **grounding query** (frasi usate dall'AI per recuperare i contenuti); mappatura grounding query → pagina (marzo); Citation Share, Intents, Topics, Compare (giugno, preview). Copre Copilot, riassunti Bing e partner, su campione; **niente clic**. Search Console non ha un equivalente per citazione. [SEJ 2026-02/03/06, news Microsoft, Forte]
- **Microsoft Clarity**: mostra grounding query e citazioni Copilot a tutti (maggio 2026) e approfondimenti sui referral AI; gratuito. [SEJ 2025-11, 2026-05, news Microsoft, Forte] Un autore ha visto 1–3 citazioni secondo Ahrefs e oltre 36.000 secondo Copilot/Clarity per lo stesso sito. [SEJ 2026-06, Taylor, caso singolo] → i tool terzi di citazioni vedono una parte minima.
- **IndexNow** (Bing, Yandex, Naver, Seznam, Yep; non Google) per segnalare aggiornamenti a Bing; beneficio sulle risposte AI non misurato. [SEJ 2026-04/05, opinione]
- **Prompt tracking**: utile solo come sondaggio ripetuto; come "rank tracking" è una metrica di vanità [SEJ 2026-07, Manic e altri, Opinione]; con GPT-5.3 i tool che leggevano i metadati delle sotto-query si sono rotti [SEJ 2026-03, Forrester]; le raccomandazioni cambiano nell'80,2% dei casi con la ricerca attiva, correlazione citazione–raccomandazione 0,4 [SEJ 2026-07, Visibility Labs, 20.000 risposte, vendor].
- **Menzione ≠ citazione ≠ clic ≠ conversione**: misurarle separatamente. [SEJ 2026-09, più autori, Opinione]
- **Ricerche di brand come proxy dell'influenza AI**: il 55,9% del traffico che segue una raccomandazione di ChatGPT passa da una ricerca del brand. [SEJ 2026-06, Similarweb, Debole-Media]
- **"Come ci hai conosciuto?"**: in un'agenzia l'80–90% dei lead arrivati da AI risultava organico o diretto in analytics. [SEJ 2026-08, dati di un'agenzia, Debole] Campo consigliato da più autori per l'influenza "dark funnel". [SEJ 2025-10, 2026-07]
- **Bot nei log**: nomi falsificati frequenti (81,8% dei fetch AI e ~87% dei "Googlebot" falsi in un sito nuovo; finti CCBot che cercavano file `.env`). Verificare IP e reverse DNS prima di trarre conclusioni; non riportare "fetch AI" come successo. [SEJ 2026-06/08, Forrester; caso nohacks, Debole]
- **Dati GA4 a zero**: segnalati report standard vuoti per molte proprietà il 1/9/2026 (Realtime funzionante). [SEJ 2026-09/10, news, Debole] → controllare buchi nei dati prima di leggere un calo.
- **Impressioni gonfiate da sistemi AI**: alcuni autori ipotizzano impressioni generate dal fan-out senza clic umani ("impressioni su, clic giù" non è sempre domanda umana). [SEJ 2026-07, Manic, ⚠ ipotesi]
- **Cadenza consigliata da un autore**: monitoraggio con avvisi di anomalia GA4; report mensile con confronto anno su anno; audit tecnico trimestrale (GSC e Bing), audit on-page, link e schede locali (NAP). [SEJ 2025-12, Opinione]
- ⚠ Numeri di vendor da non usare come benchmark: "AI = 15% del traffico" (BrightEdge), "conversioni AI 2–4x" (Forrester senza campione), "+393% traffico AI retail" (Adobe, retail USA). [SEJ 2026-03/06]

---

## Note per tipo di sito
Archetipi come in `archetypes.md`.

**personal-brand**
- KPI principali: impressioni e clic sulle **query del nome** (filtro brand o regex), CTR della SERP del nome, contatti/clic su LinkedIn/email/download CV come eventi chiave. Il volume non-brand sarà basso: misurarlo per nicchia (ruolo + competenza). [D]
- Il filtro brand e i gruppi di query potrebbero non comparire per volume insufficiente: usare la regex. [G](https://developers.google.com/search/blog/2025/11/search-console-branded-filter)
- Proprietà della piattaforma per YouTube/Instagram/TikTok/X se usati; prompt di accuratezza sul nome (omonimi) ogni trimestre. [G](https://developers.google.com/search/blog/2026/07/platform-properties-social-video-guide) · [SEJ 2026-07, opinione]

**professionista-servizi / attivita-locale**
- KPI: richieste di contatto/prenotazione, chiamate, indicazioni (Business Profile collegato a GA4), visualizzazioni dei post del Business Profile (nuova metrica, ultimi 18 mesi) [SEJ 2026-09, news Google, Forte], query non-brand "servizio + città".
- Campo "Come ci hai conosciuto?" e domanda al telefono: per un professionista è spesso la misura più affidabile dell'influenza di Google, AI e passaparola. [SEJ 2026-08/09, opinione]
- Traffico AI fuori orario (quasi due terzi) e ~1–2% delle chiamate da citazioni AI in un campione di attività locali. [SEJ 2026-09, CallRail/Wiideman, vendor, Debole]
- Il tracciamento chiamate con numeri dinamici lato browser non funziona per i bot AI che non eseguono script; tenere un numero canonico coerente ovunque. [SEJ 2026-09, opinione]

**editoriale**
- Separare Search, Discover e News; seguire il report AI per Discover; Discover ha core update propri. [G](https://developers.google.com/search/blog/2026/02/discover-core-update) Registrare la data del bug impressioni nei confronti anno su anno.

**ecommerce**
- Merchant Center ha un pilota "AI performance insights" (solo USA, solo chi ha feed): query raggruppate per AI Mode/AI Overviews e share of voice, senza clic. [SEJ 2026-07, news Google, Forte] Collegare GA4 con eventi di acquisto e confrontare con l'export GSC per pagina prodotto.

**prodotto-saas**
- Misurare iscrizioni/demo per canale incluso "AI Assistant"; il traffico AI B2B/SaaS è il più sensibile ai cambi di ChatGPT (salto del 7 maggio 2026 di +157,7% nei referral ChatGPT, B2B/SaaS +200%). [SEJ 2026-07, Profound/Similarweb, vendor, Debole]
