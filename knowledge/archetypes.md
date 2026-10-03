# Archetipi di sito

> Aggiornato al 2026-10-03. Serve a scegliere priorità e controlli in base al tipo di sito.
> Un sito può avere un archetipo principale e uno o più secondari (es. professionista con blog).
> I principi tecnici (indicizzazione, rendering, on-page) valgono per tutti: cambia l'ordine delle priorità e cosa conta come "conversione".

## Indice
- [Come scegliere](#come-scegliere)
- [personal-brand](#personal-brand)
- [professionista-servizi](#professionista-servizi)
- [attivita-locale](#attivita-locale)
- [editoriale](#editoriale)
- [ecommerce](#ecommerce)
- [prodotto-saas](#prodotto-saas)
- [Matrice priorità](#matrice-priorità)

## Come scegliere
| Domanda | Se sì |
|---|---|
| Il sito presenta una persona (portfolio, CV, autore) e il "prodotto" è la persona stessa? | personal-brand |
| Vende servizi professionali di una persona o di uno studio, anche online? | professionista-servizi |
| I clienti vanno in una sede fisica o il servizio si svolge in un'area geografica? | attivita-locale (spesso insieme a professionista-servizi) |
| Il valore principale sono articoli, guide, notizie? | editoriale |
| Si comprano prodotti dal sito? | ecommerce |
| Si vende un software/app? | prodotto-saas |

## personal-brand
- **Obiettivo tipico:** essere trovati e scelti cercando il nome (recruiter, clienti, organizzatori di eventi) e associati a competenze precise.
- **Query chiave:** nome e cognome; nome + ruolo/competenza; nome + città.
- **Priorità:** SERP del proprio nome · entità chiara (pagina Chi sono = entity home, `ProfilePage` + `Person` con `sameAs`) · coerenza nome/bio su LinkedIn, GitHub e social · progetti/casi con esperienza diretta · menzioni esterne (talk, articoli, community).
- **Rischi tipici:** omonimi; title generici ("Home", "Portfolio"); link "realizzato da" nei footer dei siti clienti (link spam); credenziali non verificabili.
- **Conversioni:** contatto, click su LinkedIn/email, download CV.
- **File da leggere:** `entity-personal-brand.md`, `structured-data.md`, `on-page-appearance.md`, `ai-search.md`.

## professionista-servizi
- **Obiettivo tipico:** richieste di consulenza da chi cerca il servizio o un problema che il servizio risolve.
- **Query chiave:** servizio (+ città se in presenza, + "online" se a distanza); problema/domanda del cliente; nome del professionista.
- **Priorità:** una pagina per servizio con contenuto unico · pagina Chi sono con credenziali vere · risposte chiare ai dubbi dei clienti · recensioni reali · Business Profile se c'è un'area servita o una sede.
- **Rischi tipici:** pagine "servizio + città" clonate (doorway); promesse e garanzie nei temi vicini a salute/lavoro/denaro; stelle di recensioni auto-pubblicate (non idonee).
- **Conversioni:** modulo contatti, prenotazione, telefono, email.
- **File da leggere:** `local-seo.md` (se presenza locale), `content-quality-spam.md`, `entity-personal-brand.md`, `structured-data.md`.

## attivita-locale
- **Obiettivo tipico:** comparire nel pacchetto locale e su Maps, e far arrivare chiamate/visite.
- **Query chiave:** servizio/categoria + città o "vicino a me"; nome dell'attività.
- **Priorità:** Business Profile completo e aggiornato · NAP identico ovunque · `LocalBusiness` col sottotipo più specifico · orari, servizi, contatti in testo HTML · recensioni reali con risposta.
- **Rischi tipici:** dati diversi tra sito e schede; pagine località fotocopia; chiusure temporanee gestite spegnendo il sito.
- **File da leggere:** `local-seo.md`, `structured-data.md`, `crawling-indexing.md` (chiusure temporanee).

## editoriale
- **Priorità:** contenuti non generici e con esperienza diretta · autori reali con pagina profilo · date corrette · link interni e struttura per argomenti · Discover e immagini grandi.
- **Rischi tipici:** contenuti in serie generati con AI (abuso di contenuti su larga scala); refresh finti delle date.
- **File da leggere:** `content-quality-spam.md`, `on-page-appearance.md`, `structured-data.md` (Article).

## ecommerce
- **Priorità:** schede prodotto uniche · `Product`/`Offer` e Merchant Center · navigazione a faccette controllata · paginazione · varianti.
- **File da leggere:** `structured-data.md`, `crawling-indexing.md`; la documentazione Google ecommerce in `sources/` per i dettagli.

## prodotto-saas
- **Priorità:** pagine funzionalità e casi d'uso · documentazione indicizzabile · `SoftwareApplication` se pertinente · confronto onesto con alternative.
- **File da leggere:** `content-quality-spam.md`, `structured-data.md`, `rendering-javascript.md` (spesso SPA).

## Matrice priorità
Ordine suggerito delle aree d'audit per archetipo (1 = prima). Indicizzazione e rendering restano sempre bloccanti: se falliscono, il resto non conta.

| Area | personal-brand | professionista-servizi | attivita-locale | editoriale | ecommerce | prodotto-saas |
|---|---|---|---|---|---|---|
| Accesso bot e indicizzazione | 1 | 1 | 1 | 1 | 1 | 1 |
| Rendering JavaScript | 2 | 2 | 2 | 2 | 2 | 2 |
| On-page e aspetto nei risultati | 3 | 3 | 4 | 3 | 4 | 3 |
| Entità e personal brand | 4 | 5 | 6 | 6 | 7 | 6 |
| Locale | 8 | 4 | 3 | 8 | 8 | 8 |
| Contenuti, qualità e spam | 5 | 6 | 7 | 4 | 5 | 4 |
| Dati strutturati | 6 | 7 | 5 | 5 | 3 | 7 |
| Prestazioni (Core Web Vitals) | 7 | 8 | 8 | 7 | 6 | 5 |
| Ricerca AI e misurazione | 9 | 9 | 9 | 9 | 9 | 9 |
