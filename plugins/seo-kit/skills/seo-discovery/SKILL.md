---
name: seo-discovery
description: Crea o aggiorna il profilo SEO di un sito (file SEO.md nella radice del progetto) - tipo di sito, obiettivo, pubblico, ricerche da presidiare e pagina che risponde a ciascuna, identità della persona o attività, profili esterni, area servita, accessi a Search Console e Business Profile, baseline. È il primo passo prima di audit, contenuti o interventi SEO, sia per un sito in costruzione sia per uno già online, con qualsiasi framework. Usa questa skill quando l'utente vuole iniziare a lavorare sulla SEO di un sito, vuole capire per quali ricerche farsi trovare, sta progettando le pagine di un sito nuovo, o quando un'altra skill SEO non trova SEO.md.
---

# Profilo SEO del sito

Questa skill produce `SEO.md`: la memoria SEO del progetto. Le altre skill del plugin lo leggono per sapere che tipo di sito è, chi deve trovarlo, con quali ricerche e quale pagina deve rispondere. Senza questo contesto un audit controlla regole generiche; con questo contesto controlla quello che conta per *quel* sito.

## Base di conoscenza
In `${CLAUDE_PLUGIN_ROOT}/knowledge/` (se la variabile non è espansa: la cartella `knowledge/` due livelli sopra questa skill):
- `archetypes.md` — tipi di sito, priorità e rischi tipici: leggilo sempre;
- `entity-personal-brand.md` e `local-seo.md` — per definire bene identità, profili e area servita;
- `content-quality-spam.md` — per non pianificare pagine che Google tratta come spam (es. pagine città clonate).

Il modello del file è in `assets/SEO-template.md`, nella cartella di questa skill.

## Procedura

### 1. Parti da ciò che esiste
- Se `SEO.md` esiste già, leggilo e lavora in **aggiornamento**: chiedi solo cosa è cambiato e non riscrivere le decisioni prese.
- Raccogli da solo tutto quello che puoi prima di fare domande, così l'utente risponde solo a ciò che non si può dedurre:
  - **dalla documentazione del progetto** (README, CLAUDE.md, stato, TODO, decisioni, brief, report precedenti): obiettivi, pubblico, scelte deliberate (es. cosa non pubblicare), strumenti già configurati;
  - **dal codice:** framework e versione, tipo di rendering, routing, pagine e route esistenti, title e testi, dati strutturati, contatti, lingue;
  - **dal sito online** (se c'è): `python "${CLAUDE_PLUGIN_ROOT}/skills/seo-audit/scripts/seo_fetch.py" <url> --sitemap 50 --no-ua --json seo-fetch.json` per pagine, title e sitemap;
  - **dalla pagina Chi sono/contatti:** nome esatto, ruolo, sede, profili collegati.

### 2. Intervista breve
Fai domande raggruppate (al massimo 2-3 giri) solo su ciò che manca. Proponi sempre una risposta di default ricavata dal sito, così l'utente può solo confermare. Temi:
1. **Obiettivo e conversione:** cosa deve succedere quando una persona arriva sul sito (contatto, prenotazione, download CV, acquisto)?
2. **Pubblico:** chi cerca e in che situazione si trova (es. recruiter tech, persona che vuole cambiare lavoro, azienda).
3. **Servizi/offerta** e **area**: in presenza, online o entrambi; quale città o zona.
4. **Identità:** nome esatto da usare ovunque, profili ufficiali, credenziali verificabili, omonimi noti.
5. **Accessi:** Search Console (proprietà Dominio?), Business Profile, analytics, Bing Webmaster Tools.
6. **Concorrenti** che oggi compaiono per le ricerche desiderate (se l'utente li conosce).

### 3. Archetipo
Scegli archetipo principale ed eventuali secondari con la tabella "Come scegliere" di `archetypes.md`. Spiega la scelta in una riga: l'archetipo cambia l'ordine delle priorità dell'audit.

### 4. Intenti di ricerca e mappa delle pagine
Costruisci la tabella degli intenti partendo dall'archetipo:
- **brand:** il nome della persona/attività, anche con ruolo o città;
- **servizio:** come il pubblico descrive l'offerta, con le sue parole e non con il gergo del settore;
- **locale:** servizio + zona, solo se c'è una presenza reale in quella zona;
- **informativo:** domande e problemi che il pubblico ha prima di cercare il servizio.

Regole:
- **una pagina per intento**, e ogni pagina deve avere contenuto davvero diverso;
- niente pagine fotocopia per città o varianti: Google le considera doorway/spam (`content-quality-spam.md`);
- se un intento non ha ancora una pagina, segnala "da creare" invece di inventare un URL.

**Indizi sulla domanda reale.** Le query restano **ipotesi** finché non ci sono dati, ma puoi ridurre l'incertezza:
- **Suggerimenti di ricerca di Google** (gratuiti, nessun volume): mostrano come le persone formulano le ricerche e quali varianti esistono.
  ```bash
  python "${CLAUDE_PLUGIN_ROOT}/skills/seo-discovery/scripts/suggest.py" "orientamento verona" "nome cognome" --expand
  ```
  Una formulazione che compare nei suggerimenti è usata davvero; l'assenza non prova nulla (volumi bassi).
- **Chi occupa oggi i risultati:** se hai uno strumento di ricerca web, guarda cosa esce per le query principali e dichiara quale motore hai usato (un motore diverso da Google, o di un altro paese, è solo un indizio). Capisci l'intento: se una ricerca è dominata da annunci di lavoro, portali o aggregatori, chi la fa cerca altro e il sito difficilmente compete. Altrimenti chiedi all'utente di controllare in finestra anonima su google.it.
- **Search Console:** se l'utente ha accesso, chiedi l'export delle query (Prestazioni → Query, ultimi 3-12 mesi): è la fonte migliore.
- Google Trends e il Keyword Planner di Google Ads sono alternative gratuite per confrontare formulazioni. Non inventare volumi.

**Ricerche da non inseguire.** Elenca anche le ricerche che sembrano pertinenti ma non lo sono: intento diverso (es. chi cerca "lavoro sviluppatore Verona" cerca un posto, non un candidato), nomi di altre persone o clienti, temi che il sito ha scelto di non trattare, ricerche dominate da portali. Evita lavoro sprecato e pagine forzate.

**Proposte per le pagine.** Per le pagine principali proponi title (circa 50-60 caratteri per evitare troncamenti, o il limite del progetto se ne ha uno; conta i caratteri con uno strumento), meta description e H1, scritti con le parole del pubblico e senza elenchi di parole chiave. Google può riscrivere i title, ma un title chiaro e specifico è la base.

### 5. Scrivi SEO.md
Compila il modello `assets/SEO-template.md` e salvalo come `SEO.md` nella radice del progetto. Indica la data. Lascia `{{...}}` solo dove l'informazione manca davvero e riportalo nel riepilogo finale.

Se l'utente ha dati di Search Console, registra la baseline (clic, impressioni, ricerche col proprio nome, ultimi 3 mesi): servirà a misurare l'effetto delle modifiche.

### 6. Chiudi con i prossimi passi
Riepiloga in poche righe, in linguaggio semplice: archetipo, 3-5 ricerche principali e la pagina che risponde a ciascuna, pagine da creare, ricerche da non inseguire, informazioni mancanti. Se durante la raccolta hai visto problemi evidenti (es. dominio che non reindirizza, profili che non linkano il sito), elencali come spunti per l'audit. Suggerisci il passo successivo: di solito `seo-audit` se il sito esiste, oppure le regole di costruzione se è in sviluppo.

## Note
- L'identità deve essere **vera e verificabile**: Google vieta autori, credenziali e recensioni fittizi. Se l'utente propone di "gonfiare" qualcosa, spiega il rischio.
- Dati personali: nel profilo metti solo ciò che è già pubblico o che l'utente vuole rendere pubblico (es. indirizzo di casa di una professionista che lavora a domicilio: chiedi prima).
- Scrivi il profilo nella lingua del sito/utente.
