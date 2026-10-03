---
name: seo-audit
description: Audit SEO completo di un sito web, nuovo o già online, con qualsiasi framework (Angular, React/Next, Vue/Nuxt, Astro, WordPress, HTML statico). Controlla l'accesso dei bot e l'indicizzazione, il rendering JavaScript, title/meta/canonical, i testi visibili, i dati strutturati, le prestazioni, la qualità dei contenuti, l'identità (personal brand) e la SEO locale, la visibilità nella ricerca AI. Produce un piano d'azione in linguaggio semplice con correzioni concrete sul codice e testi già riscritti. Usa questa skill ogni volta che l'utente chiede perché il sito non si trova su Google, vuole un controllo SEO, vuole migliorare il posizionamento o la visibilità su ChatGPT/AI Overviews, sta per mettere online un sito o ha cambiato qualcosa che potrebbe toccare l'indicizzazione, anche se non usa la parola "audit".
---

# Audit SEO

Questa skill verifica un sito contro le regole attuali della Ricerca Google (ottobre 2026) e produce un report che dice **cosa sistemare, in che ordine e come**. Funziona su un sito online, su un repository in sviluppo, o meglio su entrambi.

Chi legge il report spesso non è un esperto SEO: il valore sta nel trovare i problemi veri *e* nel renderli chiari e pronti da applicare.

## Base di conoscenza

Le regole e le tabelle dei controlli stanno in `${CLAUDE_PLUGIN_ROOT}/knowledge/` (se la variabile non è espansa: la cartella `knowledge/` due livelli sopra la cartella di questa skill). Ogni file ha una sezione **"Controlli per l'audit"** con ID stabili.

| File | Quando leggerlo |
|---|---|
| `archetypes.md` | sempre, all'inizio: stabilisce l'ordine delle priorità |
| `crawling-indexing.md` | sempre (accesso bot, robots, sitemap, canonical, codici HTTP) |
| `rendering-javascript.md` | sempre se il sito usa un framework JS; contiene gli adattatori per framework |
| `on-page-appearance.md` | sempre (title, snippet, heading, immagini, favicon, nome sito, Core Web Vitals) |
| `structured-data.md` | sempre |
| `content-quality-spam.md` | sempre; è il filtro anti-penalizzazioni |
| `entity-personal-brand.md` | archetipi personal-brand e professionista-servizi |
| `local-seo.md` | archetipi attivita-locale e professionista-servizi con presenza locale |
| `ai-search.md`, `measurement.md` | sezione finale del report |
| `myths-deprecated.md` | prima di scrivere qualsiasi raccomandazione, per non consigliare cose superate |

Leggi i file per intero quando servono: le tabelle sono la checklist, il resto spiega il perché. Se una regola manca, i testi originali Google sono in `${CLAUDE_PLUGIN_ROOT}/sources/google-search-central/pages/` (se presenti in locale).

**Gerarchia delle fonti.** La documentazione Google è la fonte primaria. Le opinioni di terzi (marcate SEJ nella base di conoscenza) valgono come indizi: riportale come tali. Ciò che è marcato ⚠ o compare in `myths-deprecated.md` non va raccomandato.

## Procedura

### 1. Contesto
1. Cerca `SEO.md` nella radice del progetto e leggilo: archetipo, URL, ricerche target, entità, accessi e audit precedenti cambiano cosa controllare.
2. **Leggi la documentazione del progetto** (README, CLAUDE.md, file di stato, TODO, decisioni, report SEO precedenti, `docs/`). Serve a tre cose: non raccomandare ciò che è già fatto (es. sitemap già inviata), capire le scelte deliberate (es. "non nominare il datore di lavoro") e trovare i documenti che contraddicono la realtà. Se un documento interno porta a una scelta sbagliata, segnalalo: una sessione futura potrebbe "correggere" il sito nella direzione sbagliata.
3. Se `SEO.md` non esiste, proponi `seo-discovery`. Se l'utente vuole procedere subito, ricava il minimo (URL, archetipo, obiettivo, 3-5 ricerche probabili) e dichiaralo come profilo provvisorio.
4. Modalità: **online + codice** (ideale), **solo online**, **solo codice** (sito in costruzione: i controlli che richiedono il sito online vanno in "da verificare al lancio").

### 2. Stack e rendering
Riconosci il framework (`angular.json`, `package.json`, `next.config.*`, `nuxt.config.*`, `astro.config.*`, `wp-content/`, solo `.html`) e leggi l'adattatore in `rendering-javascript.md`. Stabilisci come viene servito davvero ogni route: CSR, SSR a runtime, prerender/SSG (anche con `outputMode: "server"` le route possono essere prerenderizzate) e dove gira (hosting statico, server, edge). Se configurazione e comportamento reale non coincidono a prima vista, spiegalo nel report (sezione Contesto dell'appendice) e non solo nelle note di lavoro. Se l'HTML del server è un guscio vuoto, il resto conta poco.

### 3. Raccolta dati sul sito online
```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" https://dominio.it --sitemap 30 \
  --terms "termine 1;termine 2;città" --json seo-fetch.json
```
Lo script restituisce per l'HTML grezzo: stato e redirect, dimensione, title, description, robots, canonical, hreflang, H1 e struttura delle intestazioni (con i salti di livello), JSON-LD, elenco completo dei link interni, documenti collegati (PDF, DOC), immagini senza alt, testo visibile, possibili errori di accento (`typo_suspects`), sospetto "guscio SPA". A livello di sito: robots.txt, sitemap, varianti http/www, risposta a un URL inesistente, **nameserver e record TXT** (Cloudflare in modalità solo DNS non si vede dagli header; un TXT `google-site-verification` indica una proprietà Search Console di tipo Dominio) e confronto tra user agent di browser, Googlebot e bot AI. Con `--terms` dice in quali pagine compaiono le parole del pubblico (vedi passo 5). Usa `--full-text` quando ti serve il testo completo delle pagine.

**DOM renderizzato:** con strumenti browser (Chrome DevTools MCP, browser integrato) esegui `scripts/extract_dom.js` con `evaluate_script` sulle stesse pagine e confronta. Senza browser, indica il Controllo URL di Search Console.

**Prestazioni:** `lighthouse_audit` / `performance_start_trace` se disponibili, altrimenti PageSpeed Insights (`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=...&strategy=mobile`). Se la quota è esaurita, dillo e rimanda a https://pagespeed.web.dev/. Soglie in `on-page-appearance.md`; solo i dati reali (CrUX) sono quelli usati da Google.

**Verifica tu ciò che è pubblico** invece di lasciarlo "da verificare": profili GitHub (API pubblica), pagine pubbliche che dovrebbero linkare il sito (es. altri siti dello stesso proprietario), schede pubbliche, documenti PDF collegati. Resta "da verificare" solo ciò che richiede un accesso privato (Search Console, Business Profile, analytics) o che non puoi osservare in modo affidabile (la SERP reale di Google).

### 4. Analisi del codice (se disponibile)
Cerca le cause dei problemi visti online e quelli non ancora visibili (dettagli per framework in `rendering-javascript.md`):
- configurazione SSR/prerender e routing; title, description e canonical per ogni route; route 404 con vero 404;
- navigazione con `<a href>` (es. `routerLink` su `<a>`), non con `(click)` su `div`/`button`;
- `robots.txt`, sitemap, favicon, header (es. `_headers`, `staticwebapp.config.json`, `vercel.json`) e redirect lato hosting;
- JSON-LD valido, coerente con il contenuto **visibile** (prezzi, indirizzi, recensioni che non si vedono in pagina sono un problema);
- testi chiave in HTML e non solo in immagini, PDF o componenti caricati al click;
- script di terzi o router che manipolano la cronologia (dirottamento del tasto Indietro, spam dal 15/6/2026).

### 5. Lettura dei contenuti, come li legge una persona
Lo script trova la struttura, non la qualità. Leggi tu il testo delle pagine principali (home, chi sono, servizi/progetti, contatti, 2-3 articoli) e verifica:
- **Errori visibili in title, H1, description e testi:** parti da `typo_suspects` dello script (errori di accento frequenti in italiano, per ogni pagina) e riportali **tutti**, uno per pagina; poi leggi tu title e H1 di ogni pagina per refusi che l'euristica non copre. Finiscono nei risultati di Google e costano fiducia.
- **L'H1 e il title della home dicono chi/cosa/dove** in modo comprensibile a chi non conosce il sito? Uno slogan va bene accanto, non al posto del mestiere.
- **Vocabolario del pubblico** (procedura, non a sensazione):
  1. elenca i servizi/temi del sito e le ricerche di `SEO.md` (o quelle ipotizzate);
  2. per ciascuno chiedi i suggerimenti di ricerca, con la città se c'è una presenza locale:
     ```bash
     python "${CLAUDE_PLUGIN_ROOT}/skills/seo-discovery/scripts/suggest.py" "orientamento verona" "bilancio di competenze" "nome cognome"
     ```
  3. passa a `--terms` le formulazioni suggerite pertinenti all'offerta e i sinonimi di settore;
  4. metti nel report (appendice) una tabella con **ogni** suggerimento pertinente all'offerta: formulazione · query di partenza · presente/assente nei testi. Nel piano e nei testi pronti usa le formulazioni assenti più rilevanti, citando la fonte (es. "suggerito da Google per 'orientamento verona'"). Così nessun dato raccolto si perde.
  I suggerimenti sono un indizio, non un volume. Un servizio offerto ma mai nominato con le parole del pubblico è un problema concreto.
- **Link interni:** usa l'elenco `internal_links` di ogni pagina; non affermare che una pagina linka o non linka un'altra senza averlo controllato lì.
- **Struttura delle intestazioni:** i salti (es. H1 → H3) non incidono sul ranking secondo Google, ma peggiorano chiarezza e accessibilità: segnalali come bassa priorità.
- **Coerenza tra le fonti:** sito, documenti interni, CV/brochure, profili esterni e dati strutturati dicono le stesse cose (ruolo, servizi, modalità in presenza/online, città, anni)?
- **Documenti pubblici collegati** (CV, brochure, listini in PDF): sono indicizzabili, quindi controlla dati personali esposti (data di nascita, telefono, indirizzo) e informazioni che il sito ha scelto di non pubblicare (es. nomi di clienti o datori di lavoro). La decisione resta all'utente: tu segnali il rischio.

### 6. Verifica dei controlli
Percorri le tabelle "Controlli per l'audit" dei file pertinenti, nell'ordine dato da `archetypes.md`. Stato per ogni controllo: **OK**, **Problema** (con evidenza), **Da verificare** (con istruzioni), **N/A**. Non inventare evidenze. Per siti piccoli puoi raggruppare i controlli OK in una riga.

### 7. Report
Scrivi `seo-reports/AAAA-MM-GG-audit.md` nella radice del progetto. La prima parte è per l'utente, la seconda per chi implementa:

```markdown
# Audit SEO — <sito> — <data>

## In sintesi
3-6 righe in linguaggio semplice: com'è messo il sito, il problema più importante, cosa fare per primo,
cosa aspettarsi realisticamente (tempi in mesi, nessuna garanzia).

## Piano d'azione
### Questa settimana
### Nelle prossime settimane
### Nel tempo
Ogni voce: cosa fare, perché in una frase, chi la fa (tu / sviluppatore / su un sito esterno), sforzo.
Metti la legenda dello sforzo in testa al piano (⏱ minuti · ⏱⏱ ore · ⏱⏱⏱ giorni).
Nessun codice: né ID dei controlli né riferimenti ai documenti interni del progetto (es. "A-18", "RF-23"); descrivi la cosa a parole. I riferimenti stanno in appendice.

## Testi pronti
Testi da copiare così come sono: title e meta description riscritti per le pagine chiave
(con numero di caratteri contato con uno strumento, non a occhio), H1 proposti, frasi da aggiungere alle pagine.
Il codice va in appendice. Lunghezze: Google non fissa limiti, ma per evitare troncamenti punta a circa
50-60 caratteri per il title e 120-160 per la description; se il progetto ha un suo controllo, rispetta quello.

## Cose fuori dal sito
Checklist di ciò che solo una persona può fare (Search Console, Business Profile, profili, recensioni, menzioni).

## Da verificare
Ciò che richiede un accesso che non hai, con le istruzioni passo passo.

## Ricerca AI e misurazione
Stato, cosa monitorare, baseline da registrare oggi.

---
## Appendice tecnica
### Problemi per priorità
| # | ID | Problema | Evidenza | Correzione | Gravità | Sforzo |
### Codice e configurazione pronti
Snippet JSON-LD, righe di configurazione (hosting, redirect, header), modifiche ai file con percorso.
### Vocabolario del pubblico
Tabella dei suggerimenti di ricerca pertinenti: formulazione · query di partenza · presente/assente.
### Dettaglio dei controlli per area
Tabelle per area (ordine di archetypes.md) con ID, stato ed evidenza.
### Contesto e limiti
URL, archetipo, stack/rendering, modalità, profilo provvisorio, strumenti non disponibili.
```

**Lunghezza.** La parte per l'utente (dalla sintesi a "Ricerca AI e misurazione") deve leggersi in pochi minuti: frasi brevi, niente ripetizioni dell'appendice, al massimo una decina di voci nel piano (le altre in appendice). L'appendice può essere lunga.

Gravità: **critica** = blocca l'indicizzazione o espone a penalizzazioni; **alta** = limita molto la visibilità; **media**; **bassa**. Niente punteggi numerici inventati. Aggiorna `SEO.md` ("Storico audit": data, link, conteggi per gravità) se esiste.

### 8. Correzioni
Proponi di applicare le correzioni partendo dalle più importanti e chiedi conferma prima di modificare file: scelte come SSR, routing o URL toccano hosting e struttura. Dopo ogni correzione importante ripeti la verifica pertinente.

## Cose da tenere a mente
- **Nessuna promessa di posizionamento.** Il report dice cosa rimuove ostacoli e cosa aumenta le probabilità.
- **Fuori dal sito conta**: per siti piccoli, Business Profile, recensioni reali, profili coerenti e menzioni esterne spesso pesano più del codice.
- **Bot AI**: distingui bot di addestramento e di ricerca; la scelta su cosa bloccare è dell'utente, i blocchi involontari (CDN/WAF) vanno sempre segnalati.
- **Rispetta le scelte deliberate** trovate nella documentazione del progetto: se ne sconsigli una, spiega perché e lascia decidere.
