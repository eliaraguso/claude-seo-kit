---
name: seo-entity-local
description: Costruisce un'identità chiara e coerente di una persona o di un'attività per Google e per gli assistenti AI, e cura la presenza locale - definizione unica di nome/ruolo/servizi, pagina "chi sono", dati strutturati Person/ProfilePage/Organization/LocalBusiness con @id e sameAs, coerenza di profili (LinkedIn, GitHub, social) e di nome/indirizzo/telefono, Google Business Profile, Bing Places, Apple, directory di settore, recensioni. Produce testi pronti da incollare e una checklist delle azioni fuori dal sito. Usa questa skill per personal brand, portfolio, professionisti e attività locali, quando l'utente vuole farsi trovare cercando il proprio nome, comparire su Google Maps, aprire o sistemare la scheda Google, raccogliere recensioni o allineare i profili online.
---

# Identità e presenza locale

Per un sito piccolo, ciò che Google e gli assistenti AI sanno della persona o dell'attività conta quanto il sito stesso. Lo ricavano incrociando il sito, i dati strutturati, i profili e le schede esterne, le recensioni e le menzioni. Se queste fonti dicono cose diverse (ruolo, servizi, città, "solo online" contro "anche in presenza"), il risultato è confusione. Questa skill crea **una definizione unica** e la porta ovunque.

## Base di conoscenza
In `${CLAUDE_PLUGIN_ROOT}/knowledge/` (se la variabile non è espansa: la cartella `knowledge/` due livelli sopra questa skill):
- `entity-personal-brand.md` — entity home, Person/ProfilePage, sameAs, omonimie, menzioni, rischi spam;
- `local-seo.md` — Business Profile, NAP, recensioni, pagine località, funzioni per paese;
- `structured-data.md` — schede WebSite, Organization, LocalBusiness, Person/ProfilePage, Review (con i vincoli sulle auto-recensioni);
- `archetypes.md` — per capire se la parte locale si applica.

Le regole operative del Business Profile marcate [GBP*] nella base di conoscenza non vengono dalla documentazione di Search: verificale sulla guida ufficiale di Google Business Profile prima di darle come certe.

Leggi `SEO.md` del progetto (sezione Entità) e la documentazione del progetto: spesso contiene già scelte (es. cosa non pubblicare) da rispettare.

## Procedura

### 1. Definizione unica
Scrivi con l'utente (o proponi, ricavandola dal sito) la **scheda d'identità**:
- nome esatto da usare ovunque e varianti ammesse;
- ruolo/professione in parole comprensibili al pubblico;
- frase di presentazione breve (circa 150 caratteri) e bio lunga (circa 600-800 caratteri), in prima o terza persona coerentemente;
- servizi o competenze principali (3-6), con le parole del pubblico;
- modalità (in presenza dove, online, entrambe), area servita, sede se pubblica;
- contatti pubblici (solo quelli che l'utente vuole pubblicare);
- credenziali verificabili (ente, anno): niente titoli vaghi o inventati.

Salvala in `SEO.md` (sezione 3) e usala come fonte per tutto il resto.

### 2. Verifica la coerenza delle fonti
Controlla da solo ciò che è pubblico e annota ogni differenza dalla definizione:
- **sito:** home, chi sono, contatti, footer, dati strutturati, sull'HTML **servito online** e non solo sul codice (`python "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" <url> --sitemap 20 --full-text`): CDN e plugin possono alterare contatti e testi (es. email offuscate che diventano illeggibili);
- **profili pubblici:** GitHub (API pubblica `https://api.github.com/users/<utente>`), pagine pubbliche raggiungibili, altri siti dello stesso proprietario che dovrebbero linkare;
- **documenti pubblici** collegati (CV, brochure): dati personali esposti, ruolo e date coerenti;
- **cosa non puoi vedere** (LinkedIn dietro login, Business Profile, risultati reali di Google): istruzioni precise all'utente per controllarlo.

### 3. Sul sito
- **Entity home:** una pagina "chi sono" (o la home, se il sito è di una sola pagina) con foto reale, bio, credenziali, modalità e area, link ai profili. È la pagina a cui puntano `sameAs`, `author` e i profili esterni.
- **Dati strutturati** a grafo con `@id` stabili: `WebSite` in home; `Person` (personal brand) dentro `ProfilePage` sulla pagina profilo, oppure `Organization` / sottotipo specifico di `LocalBusiness` per un'attività; `sameAs` solo verso profili ufficiali; nessuna proprietà con dati non visibili in pagina; niente stelle `aggregateRating` su recensioni raccolte o mostrate dall'attività stessa. Usa le schede e gli esempi di `structured-data.md`.
- **NAP e modalità** in testo HTML, identici ovunque nel sito (footer, contatti, dati strutturati).

### 4. Fuori dal sito: testi pronti e checklist
Prepara testi già adattati ai campi di ciascuna piattaforma, partendo dalla definizione unica:
- **LinkedIn:** headline, sezione Informazioni, link al sito;
- **GitHub** (personal brand tecnico): bio, sito web, eventuale README del profilo;
- **Google Business Profile** (solo se c'è una sede o un'area servita in cui si incontrano i clienti): nome reale senza parole chiave aggiunte, categoria principale più specifica, area servita oppure indirizzo, servizi, orari, descrizione, link al sito e alla prenotazione, foto reali;
- **Bing Places e Apple Business Connect** con gli stessi dati;
- **directory e albi di settore** pertinenti (associazioni professionali, ordini, enti locali): valgono per la credibilità e per le persone, non come "link SEO".

Recensioni: chiedile ai clienti reali, una persona alla volta, senza incentivi e senza filtrare solo i soddisfatti; rispondi a tutte. Mai recensioni scritte da sé o comprate.

### 5. Report
Scrivi `seo-reports/AAAA-MM-GG-identita.md` nella radice del progetto:
1. **In sintesi** (linguaggio semplice): quanto è coerente oggi l'identità e cosa fare per primo;
2. **Definizione unica** (la scheda del passo 1);
3. **Incoerenze trovate**, fonte per fonte, con la correzione;
4. **Testi pronti** per ogni piattaforma;
5. **Codice pronto** per il sito (JSON-LD a grafo, testi della pagina chi sono);
6. **Checklist fuori dal sito**, in ordine, con chi la fa e il tempo stimato;
7. **Da verificare** (accessi privati) e **cosa monitorare**: ricerca del nome in finestra anonima, domande fisse agli assistenti AI ("Chi è …?", "… a Verona") ogni 3 mesi, query col nome in Search Console.

## Note
- Il nome deve essere quello reale: aggiungere parole chiave al nome della scheda Google viola le sue regole.
- Le pagine "servizio + città" clonate per comparire in più zone sono doorway: una pagina località solo dove c'è presenza reale e contenuto diverso.
- Per un lavoratore dipendente il Business Profile non serve: la parte locale si riduce alla città nel testo e nei dati strutturati.
- Rispetta le scelte di riservatezza dell'utente: segnala i rischi (es. dati personali in un PDF pubblico), decide lui.
