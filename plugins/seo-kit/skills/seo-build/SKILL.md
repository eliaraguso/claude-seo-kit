---
name: seo-build
description: Regole SEO mentre si costruisce o si modifica un sito, con qualsiasi framework (Angular, React/Next, Vue/Nuxt, Astro, WordPress, HTML statico) - impostazione delle basi di un progetto nuovo (rendering, route, title/meta/canonical per pagina, robots, sitemap, 404 reali, dati strutturati di base), controllo di ogni pagina o route aggiunta, verifica dei file generati dalla build e checklist di lancio o di migrazione. Usa questa skill quando l'utente crea un sito o un progetto web, aggiunge pagine/route/sezioni, cambia URL o routing, prepara un deploy o la messa online, migra dominio o framework, anche se non nomina la SEO.
---

# SEO durante la costruzione

Correggere la SEO dopo il lancio costa di più che impostarla bene mentre si scrive il codice: URL cambiati, pagine già indicizzate male, redirect da gestire. Questa skill porta le regole di Google dentro il lavoro di sviluppo, nei tre momenti in cui contano.

## Base di conoscenza
In `${CLAUDE_PLUGIN_ROOT}/knowledge/` (se la variabile non è espansa: la cartella `knowledge/` due livelli sopra questa skill):
- `rendering-javascript.md` — leggi la sezione **"Adattatori per framework"** per lo stack del progetto;
- `crawling-indexing.md`, `on-page-appearance.md`, `structured-data.md` — le sezioni "Regole per chi costruisce";
- `archetypes.md` — priorità per tipo di sito;
- `myths-deprecated.md` — per non introdurre pratiche superate (es. `meta keywords`, `priority` nelle sitemap, rendering dinamico).

Se esiste `SEO.md` nella radice del progetto, leggilo: dice quali pagine servono e per quali ricerche.

## Momento 1 — Basi di un progetto nuovo (o adozione su un progetto esistente)
Verifica e, con l'accordo dell'utente, imposta:
1. **Rendering:** il contenuto principale deve essere nell'HTML che arriva dal server. Per i framework JS: SSR o prerender/SSG (es. Angular `@angular/ssr` con route `Prerender` dove possibile). Il CSR puro va bene solo per aree private.
2. **URL e routing:** URL a percorso (History API, niente `#/`), minuscoli con trattini, stabili. Navigazione con `<a href>` veri.
3. **Head per ogni route:** title unico, meta description, un solo canonical assoluto e autoreferenziale nell'HTML, `lang` su `<html>`. Centralizza in un servizio/componente SEO invece di ripeterlo a mano.
4. **404 veri:** le route inesistenti devono rispondere con stato 404 lato server/hosting, non 200 con una pagina "non trovato".
5. **File di sito:** `robots.txt` (che non blocchi CSS/JS) con riga `Sitemap:`; sitemap generata dalle route reali, con `lastmod` vero; favicon del progetto (non quella di default del framework).
6. **Dominio canonico:** una sola versione (con o senza www, https) e redirect 301 dalle altre, configurati sull'hosting.
7. **Dati strutturati di base:** `WebSite` in home; `Person`/`ProfilePage` o `Organization`/`LocalBusiness` secondo l'archetipo, con `@id` stabile (schede ed esempi in `structured-data.md`). L'immagine di una persona deve essere una foto reale: se non c'è, ometti la proprietà `image` invece di usare logo, grafica social o screenshot.
8. **Misurazione:** eventi sulle conversioni (contatto, telefono, download, prenotazione). Vedi `measurement.md`.
9. **Prestazioni:** immagini dimensionate e non lazy sopra la piega, font precaricati, bundle iniziale contenuto. Le soglie sono in `on-page-appearance.md`.

## Momento 2 — Ogni pagina o route nuova
Prima di considerare finita una pagina, controlla:
- risponde a **un intento** preciso (se c'è `SEO.md`, aggiungila alla tabella degli intenti) e non duplica un'altra pagina;
- title, description e H1 specifici, scritti con le parole del pubblico, senza refusi;
- è raggiungibile da un link interno `<a href>` e compare nella sitemap;
- immagini di contenuto in `<img>` con `alt`, testi importanti in HTML (non solo in immagini o PDF);
- dati strutturati pertinenti e coerenti con ciò che è visibile;
- se sostituisce un URL esistente, redirect 301 dal vecchio.

Per i testi della pagina usa la skill `seo-content`.

## Momento 3 — Prima del deploy e al lancio
1. **Controlla la build** (siti prerenderizzati o statici):
   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/skills/seo-build/scripts/check_build.py" <cartella-output> --base https://dominio.it
   ```
   Segnala title/description mancanti o duplicati, canonical assenti o multipli, H1, JSON-LD non valido, possibili errori di accento, pagine quasi vuote (prerender non avvenuto) e HTML oltre 2 MB. Le pagine `noindex` e i file di fallback del framework (es. `index.csr.html`) sono riportati solo come informazione. Riporta l'esito in una tabella per URL (title, canonical, H1, JSON-LD, stato), non solo come giudizio complessivo.
2. **Controlla l'ambiente online** (anche di staging, se raggiungibile): `python "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" https://staging... --sitemap 20`. Attenzione: lo staging deve essere protetto o `noindex`, e quel `noindex` **non deve arrivare in produzione**.
3. **Al lancio:** proprietà Search Console di tipo Dominio, invio della sitemap, Controllo URL della home; Bing Webmaster Tools (può importare da Search Console). Registra la data di lancio in `SEO.md`.
4. **Migrazione da un sito precedente:** mappa vecchi URL → nuovi URL e redirect 301 uno a uno (niente redirect di massa alla home), mantieni i redirect almeno un anno, usa lo strumento Cambio di indirizzo di Search Console se cambia dominio. Dettagli in `crawling-indexing.md`.

## Come lavorare
- Applica le modifiche al codice solo con l'accordo dell'utente quando toccano architettura, hosting o URL; per le correzioni locali (un title, un alt, un link) procedi e riepiloga.
- Dopo una modifica, ripeti il controllo pertinente (build o script) e riporta l'esito.
- Se un requisito non si può soddisfare con l'hosting attuale (es. niente redirect lato server), dillo chiaramente e proponi l'alternativa meno dannosa, annotandola in `SEO.md` (sezione "Decisioni e vincoli").
