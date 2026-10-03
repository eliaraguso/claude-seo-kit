# SEO locale

> Aggiornato al 2026-10-03. Fonte primaria: Google. Secondaria: SEJ (ott 2025–ott 2026).
> Legenda fonti: **[G](url)** = documentazione Google Search Central (fatto). **[GBP\*]** = regola della Guida di Google Business Profile (support.google.com/business), **non presente nel corpus letto**: la skill la presenta come "da verificare sulla guida ufficiale". **Deduzione** = ragionamento da fatti Google, non affermato da Google. **[SEJ …]** = fonte terza (opinione, studio di vendor, caso singolo).
> File collegati: `structured-data.md` (sintassi JSON-LD), `entity-personal-brand.md` (identità, autore), `content-quality-spam.md` (doorway, contenuti in serie), `ai-search.md` (misurazione AI), `crawling-indexing.md`.

## Indice
- [Fatti e regole (Google)](#fatti-e-regole-google)
- [Controlli per l'audit](#controlli-per-laudit)
- [Checklist off-site](#checklist-off-site-azioni-manuali-che-la-skill-può-solo-guidare)
- [Regole per contenuti e struttura del sito](#regole-per-contenuti-e-struttura-del-sito)
- [Cosa dicono le fonti terze](#cosa-dicono-le-fonti-terze)
- [Miti e consigli obsoleti](#miti-e-consigli-obsoleti)

## Fatti e regole (Google)

### 1. Business Profile e schede locali
- La presenza nella mappa e nei risultati locali passa dal **Profilo dell'attività su Google** (Google Business Profile, GBP): se l'attività non compare per una query locale, il primo controllo è che sia stata aggiunta e rivendicata. [G](https://developers.google.com/search/help/site-appearance-faq)
- Dopo la rivendicazione (business.google.com) il proprietario gestisce **indirizzo, contatti, tipo di attività e foto**, che alimentano scheda informativa e Maps. Google consiglia anche di **verificare il sito in Search Console** per stabilirlo come presenza ufficiale. [G](https://developers.google.com/search/docs/appearance/establish-business-details)
- La scheda informativa può essere corretta con il link **Feedback** se è passata almeno una settimana dall'ultima scansione della pagina con markup; un rappresentante verificato vede più opzioni. Il sistema impiega **circa una settimana** ad aggiornare i dettagli. [G](https://developers.google.com/search/docs/appearance/establish-business-details)
- Rivendicare il GBP serve anche a ricevere avvisi diretti (restrizioni Maps, rimozioni legali, restrizioni di massa sulle recensioni); verificare Search Console dà avvisi su azioni manuali e sicurezza. [G](https://developers.google.com/search/help/small-business-notifications)
- Le funzionalità AI (AI Overview, AI Mode) possono mostrare informazioni su attività locali: Google indica di tenere aggiornato il **Profilo dell'attività** (e Merchant Center per i prodotti). [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [G](https://developers.google.com/search/docs/appearance/ai-features)
- Le immagini del GBP sono un canale per mostrare prodotti e servizi nei prodotti Google. [G](https://developers.google.com/search/help/site-appearance-faq)
- Collegare **tutti i profili** (GBP, social, schede) al sito ufficiale: caso Office Hours di un'attività di servizi non trovata perché il "sito" non era referenziato dalle altre schede. [G](https://developers.google.com/search/help/office-hours/2023/december)
- Attività chiusa definitivamente: **segnarla come chiusa** nel GBP e rimuovere/redirigere il vecchio sito. [G](https://developers.google.com/search/help/office-hours/2023/december)

**Regole del Business Profile [GBP\*]** (non nel corpus: verificare sulla guida ufficiale prima di presentarle come obbligo)
- Idoneità: l'attività deve avere **contatto di persona** con i clienti negli orari dichiarati (in sede o presso il cliente). Un'attività **solo online** non è idonea.
- **Attività con area servita** (va dai clienti, non li riceve): nascondere l'indirizzo e impostare l'area servita. Indirizzi non presidiati (caselle postali, uffici virtuali) non ammessi.
- **Nome**: quello reale usato nel mondo fisico (insegna, documenti, brand), senza parole chiave o città aggiunte.
- **Categoria principale**: la più specifica che descrive l'attività nel suo complesso; poche categorie secondarie pertinenti.
- **Recensioni**: vietati incentivi, richieste selettive solo ai clienti soddisfatti, recensioni di proprietari/dipendenti, contenuti falsi.
- **Chiusure**: esiste lo stato "temporaneamente chiuso" e gli **orari speciali** (festività, ferie); non eliminare la scheda.

### 2. Dati strutturati `LocalBusiness` [G](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- Abilitano dettagli nella scheda informativa (orari, reparti, contatti). Prenotazioni/ordini dai risultati: **API Maps Booking**, non il markup. Il carosello ristoranti è ad accesso limitato. Nessun limite di paese indicato per la scheda base.
- Si può mettere su qualsiasi pagina, ma è più utile sulla pagina con le informazioni dell'attività. **Una entità per ogni sede**; usare il **sottotipo più specifico**; più tipi in **array** su `@type` (**`additionalType` non supportato**).
- `LocalBusiness` è sottotipo di `Organization`: valgono anche i campi Organization (`logo`, `sameAs`, `email`, `vatID`, `contactPoint`…). [G](https://developers.google.com/search/docs/appearance/structured-data/organization)
- **Obbligatorie**: `name`, `address` (`PostalAddress`, il più completo possibile; `addressCountry` ISO 3166-1 alpha-2, es. `IT`).
- **Consigliate**: `telephone` (con prefisso internazionale, es. `+39`), `url` (URL della **sede specifica**, funzionante), `geo` (latitudine/longitudine con **almeno 5 decimali**), `openingHoursSpecification`, `priceRange` (**meno di 100 caratteri**, altrimenti non mostrato), `department`, `menu`/`servesCuisine` (solo ristorazione); `aggregateRating`/`review` **solo per siti che raccolgono recensioni su altre attività**.
- **Orari**: `dayOfWeek` in inglese (anche forma breve `Monday`); senza `validFrom`/`validThrough` valgono tutto l'anno; dopo mezzanotte in un solo blocco; 24 h = `00:00`–`23:59`; chiuso tutto il giorno = `00:00`–`00:00`; **chiusure stagionali/festive** = `validFrom` + `validThrough` con `00:00`–`00:00`. Gli enum vanno in inglese anche su siti in altra lingua. [G](https://developers.google.com/search/help/office-hours/2023/august)
- Servizi con prezzo su preventivo: usare `LocalBusiness` (che ammette fascia di prezzo), **non `Product`**. [G](https://developers.google.com/search/help/office-hours/2023/january)
- Violazioni → possibile azione manuale; con azione manuale i dati strutturati vengono **ignorati** (la pagina resta in Ricerca). Google non garantisce la visualizzazione. [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Dati strutturati **non necessari** per comparire nelle funzionalità AI; nessun markup speciale "per l'AI". [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

### 3. Recensioni
- **Self-serving**: se l'entità recensita controlla le recensioni su se stessa, le sue pagine con `LocalBusiness` o qualsiasi `Organization` **non sono idonee alle stelle** — vale sia per markup diretto sia per **widget incorporati** (recensioni Google, Facebook). [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- Valutazioni di attività locali: devono venire **direttamente dagli utenti**, non da editor umani che le creano o curano. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- **Non aggregare** recensioni da altri siti; **niente recensioni false o incentivate non dichiarate** (incentivo = denaro, sconti, voucher, prodotti gratis), né nel markup né nella pagina; recensioni non da utenti reali possono portare ad **azione manuale**. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) · [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Ogni recensione/valutazione deve riferirsi a **un elemento specifico** (un solo bersaglio), essere **visibile in pagina**; se si marcano più recensioni, marcarle tutte. [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- Il **sistema delle recensioni** (attivo anche in italiano) valuta contenuti di recensione scritti dal sito (guide, confronti), **non** le recensioni dei clienti in pagina. [G](https://developers.google.com/search/docs/appearance/reviews-system)
- Scambiare prodotti/servizi con recensioni che contengono link = **link spam**. [G](https://developers.google.com/search/docs/essentials/spam-policies)

### 4. Pagine località, doorway e keyword stuffing [G](https://developers.google.com/search/docs/essentials/spam-policies)
- **Doorway**: più pagine o domini mirati a regioni/città che portano a un'unica destinazione; pagine quasi uguali che somigliano a risultati di ricerca più che a una gerarchia consultabile.
- **Keyword stuffing**: blocchi di testo che elencano città e regioni per cui ci si vuole posizionare; elenchi di numeri di telefono senza valore.
- **Abuso di contenuti su larga scala**: molte pagine generate (con AI o a mano) per manipolare il ranking, incluse pagine per ogni variante di query. [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Il **sistema di deduplicazione** mostra solo il risultato più pertinente tra pagine molto simili; la **diversità dei siti** limita in genere a due risultati per sito. [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide)

### 5. Segnali e aspetto
- Query locali → risultati locali: la pertinenza dipende anche dalla **posizione dell'utente**; la mappa non compare per tutte le query e non va "inseguita". [G](https://developers.google.com/search/docs/fundamentals/how-search-works) · [G](https://developers.google.com/search/help/office-hours/2023/march)
- Il `<title>` può includere **nome dell'attività e sede fisica**; per un'attività locale Mueller suggerisce città/località nei title. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G](https://developers.google.com/search/help/office-hours/2023/march)
- Esempio Google di buona meta description: **cosa offre + orari + dove si trova**. [G](https://developers.google.com/search/docs/appearance/snippet)
- Query con posizione alta ma CTR basso perché l'utente trova già orari/indirizzo/telefono in SERP: comportamento atteso se l'obiettivo è il contatto. [G](https://developers.google.com/search/docs/monitor-debug/bubble-chart-analysis)
- **ccTLD** (es. `.it`): segnale di paese a basso impatto; la lingua conta di più. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [G](https://developers.google.com/search/help/office-hours/2024/july)
- Il crawler vede i contenuti dalla propria posizione, in genere USA: non far dipendere orari/prezzi/contatti dalla geolocalizzazione IP. [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- **Elenco dei luoghi più apprezzati**: mostra elenchi editoriali di terzi in cui l'attività è menzionata; **solo attività con sede fisica**; gli elenchi devono essere curati, indipendenti, non sponsorizzati. [G](https://developers.google.com/search/docs/appearance/top-places-list)

### 6. Funzioni disponibili solo in certi paesi
| Funzione | Dove | Note | Fonte |
|---|---|---|---|
| Unità di aggregatori + unità di fornitori (anche query su attività locali dal 18/09/2026) | Solo SEE (Italia inclusa) | Il fornitore diretto non deve inviare dati oltre a quelli scansionati; l'unità fornitori compare solo con quella aggregatori; le directory devono essere approvate come servizi di ricerca verticale | [G](https://developers.google.com/search/docs/appearance/supplier-unit) · [G](https://developers.google.com/search/docs/appearance/aggregator-unit) |
| Caroselli di dati strutturati per attività locali | SEE, Sudafrica, Turchia | Per siti che elencano più entità (aggregatori), non per la singola attività | [G](https://developers.google.com/search/docs/appearance/aggregator-features) |
| "Siti di luoghi" (carosello + chip) | Solo Turchia | Nessun markup; modulo di interesse | [G](https://developers.google.com/search/docs/appearance/places-sites) |
| Abuso reputazione del sito: azione manuale | Effetto solo fuori SEE dal 30/08/2026 | Nel SEE la sezione può essere classificata separatamente | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| Ask Maps, chiamate AI ai negozi, booking agentico servizi locali | USA (Ask Maps anche India) | Solo da fonti SEJ; non in Italia a ottobre 2026 | [SEJ 2026-03/05/06] |
| Strumenti GBP nell'app Gemini | Globale **tranne SEE e UK** | Analisi, bozze risposte recensioni | [SEJ 2026-06] |
| Annunci Apple Maps (divieti per alcune categorie) | USA/Canada | Solo pubblicità | [SEJ 2026-07] |

### 7. AI e ricerca locale (posizione Google)
- AI Overview e AI Mode usano i sistemi principali di ranking; non esistono requisiti aggiuntivi: pagina **indicizzata e idonea allo snippet**, scansione consentita in robots.txt **e da CDN/hosting**, contenuti importanti **in testo**, dati strutturati coerenti col visibile, GBP aggiornato. [G](https://developers.google.com/search/docs/appearance/ai-features)
- Controlli disponibili: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`; esclusione del sito dalle funzionalità di AI generativa tramite impostazione in Search Console (rollout progressivo); Google-Extended **non** riguarda la Ricerca. [G](https://developers.google.com/search/docs/appearance/ai-features) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Misura: report sul rendimento dell'AI generativa in Search Console (**solo impressioni**, per pagina/paese/dispositivo; globale dal 31/08/2026). [G](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)
- Manipolare le risposte AI (menzioni o recensioni inautentiche) rientra nelle norme sullo spam; cercare menzioni inautentiche è "poco utile". [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **ChatGPT, Perplexity, Copilot, Apple**: nessuna documentazione Google; solo fonti terze (vedi sotto). Bing Places e Apple Business Connect sono schede separate, gratuite (fonti terze).

### 8. Directory locali (posizione Google)
- **Non** iscriversi a directory per migliorare la SEO; usarle eventualmente per traffico diretto. "La ricerca locale è diversa." [G](https://developers.google.com/search/help/office-hours/2022/november)
- Directory e social bookmarking di **bassa qualità** per i link = link spam; per la SEO off-page "non sprecare tempo". [G](https://developers.google.com/search/docs/essentials/spam-policies) · [G](https://developers.google.com/search/help/office-hours/2023/may)
- **Deduzione**: la coerenza dei dati sulle schede (GBP, Bing, Apple, directory di settore) serve agli utenti, al GBP e ai sistemi che leggono il web; non è una tattica di link.

## Controlli per l'audit

Gravità: **Critica** = rischio azione manuale o informazione sbagliata ai clienti · **Alta** = perdita di visibilità locale probabile · **Media** = miglioramento importante · **Bassa** = rifinitura. "Auto" = verificabile dal codice/HTML; "Manuale" = serve l'utente o uno strumento esterno.

| ID | Controllo | Come verificarlo | Gravità | Fonte |
|---|---|---|---|---|
| LO-01 | NAP (nome, indirizzo o area, telefono) in **testo HTML** visibile, identico su home, contatti, footer e JSON-LD | Auto: estrarre testo da HTML iniziale e renderizzato; confrontare stringhe normalizzate | Alta | [G](https://developers.google.com/search/docs/appearance/ai-features) · deduzione |
| LO-02 | NAP del sito = GBP = Bing Places = Apple Business Connect = directory di settore | Manuale: l'utente incolla i dati delle schede; la skill confronta campo per campo | Alta | [SEJ 2026-08, Uberall/AthenaHQ] · [GBP\*] |
| LO-03 | Orari/contatti/servizi non solo in immagine, PDF o widget JS | Auto: cercare orari e telefono nel DOM; segnalare `<img>` di volantini, iframe, widget | Alta | [G](https://developers.google.com/search/docs/fundamentals/get-started-developers) |
| LO-04 | Telefono come link `tel:` con prefisso `+39`/internazionale | Auto: regex su `href="tel:"` | Bassa | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-05 | `LocalBusiness` presente sulla pagina info/contatti se c'è una **sede che riceve clienti** | Auto: parse JSON-LD; Manuale: chiedere se la sede riceve clienti | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-06 | Sottotipo più specifico; più tipi in array `@type`; nessun `additionalType` | Auto | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-07 | Obbligatorie `name` + `address` completo (`streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` ISO-2) | Auto | Alta | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-08 | `telephone` con prefisso paese; `geo` ≥ 5 decimali; `priceRange` < 100 caratteri; `url` della sede = 200 | Auto | Bassa | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-09 | `openingHoursSpecification` coerente con gli orari visibili; `dayOfWeek` in inglese; formato orario valido | Auto: confronto JSON-LD ↔ testo pagina | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| LO-10 | Nessun `aggregateRating`/`review` sulla **propria** `LocalBusiness`/`Organization` (anche via widget Google/Facebook) | Auto: JSON-LD + ricerca di script di widget recensioni | Alta | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| LO-11 | Testimonianze reali; incentivi dichiarati; nessuna recensione inventata o "curata"; nessuna aggregata da altri siti | Manuale: chiedere l'origine; Auto: cercare markup con autori ripetuti/generici | Critica | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| LO-12 | Ogni rating ha **un solo** `itemReviewed` ed è visibile in pagina | Auto | Alta | [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) |
| LO-13 | Pagine città/zona **quasi identiche** (doorway) | Auto: similarità del testo principale tra pagine con pattern `/{servizio}-{città}`; segnalare se cambia solo il toponimo | Critica | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| LO-14 | Blocchi di elenchi di città/quartieri o numeri ripetuti | Auto: liste di toponimi > ~10 senza frase di contesto (soglia euristica) | Alta | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| LO-15 | Una pagina per ogni **servizio** reale con contenuto distinto, CTA e prossimo passo | Auto: mappa pagine/servizi; Manuale: elenco servizi reali | Media | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [SEJ 2025-12, Riddall] |
| LO-16 | `<title>` di home/contatti/pagine servizio con attività + luogo (o "online"); niente "Home"/"Contatti" nudi | Auto | Media | [G](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| LO-17 | Meta description di home/contatti con cosa offre + orari/modalità + dove | Auto | Bassa | [G](https://developers.google.com/search/docs/appearance/snippet) |
| LO-18 | Area servita / modalità online descritte in frasi (non liste di città) | Auto + giudizio | Media | [G](https://developers.google.com/search/docs/essentials/spam-policies) |
| LO-19 | Chiusure temporanee/ferie: avviso visibile + `validFrom`/`validThrough` + orari speciali GBP; sito **non** spento né in `noindex` | Auto (testo/JSON-LD), Manuale (GBP) | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) · [GBP\*] · deduzione |
| LO-20 | Vecchie pagine con NAP obsoleto (`-old`, `v2`, duplicati post-redesign) ancora indicizzabili | Auto: crawl + ricerca vecchi numeri/indirizzi; Manuale: `site:` | Media | [SEJ 2026-09, Shaw/Jeffery] |
| LO-21 | Googlebot non bloccato da robots.txt/CDN/WAF; decisione **esplicita** sui bot di ricerca AI (es. impostazioni Cloudflare) | Auto: robots.txt; Manuale: pannello CDN, Controllo URL | Alta | [G](https://developers.google.com/search/docs/appearance/ai-features) · [SEJ 2026-09] |
| LO-22 | Modulo contatto/prenotazione accessibile: `<label>`, pulsanti con nome, nessun CAPTCHA o overlay che blocchi il flusso | Auto: albero di accessibilità | Media | [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| LO-23 | Contenuti chiave nell'**HTML iniziale** (SPA: SSR/prerender) per crawler che non eseguono JS | Auto: confronto HTML grezzo vs renderizzato | Media (Alta per visibilità su assistenti terzi) | [SEJ 2026-09, CallRail] · ⚠ Google esegue JS |
| LO-24 | Numeri di call tracking lato browser non sostituiscono il numero canonico visto dai crawler | Auto: diff numero in HTML grezzo vs DOM | Media | [SEJ 2026-09, CallRail] · deduzione |
| LO-25 | Se **nessuna sede aperta al pubblico**: niente `LocalBusiness` con indirizzo che nel GBP è nascosto; usare `Organization`/`Person` | Manuale + Auto | Media | Deduzione da [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) + [GBP\*] |
| LO-26 | `FAQPage` presente solo per gli utenti: nessuna attesa di risultati avanzati | Auto | Bassa | [SEJ 2026-05] (rich result FAQ rimossi) |
| LO-27 | JSON-LD valido e analizzabile; nessun errore nel Test dei risultati avanzati | Auto: parse; Manuale: Rich Results Test | Media | [G](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| LO-28 | Link dal sito al GBP (es. "Lasciaci una recensione") e campo sito del GBP verso home/pagina sede canonica (https, senza parametri incoerenti) | Auto (link uscenti); Manuale (GBP) | Media | [G](https://developers.google.com/search/help/office-hours/2023/december) |
| LO-29 | Search Console verificata (proprietà Dominio) e GBP rivendicato | Manuale | Alta | [G](https://developers.google.com/search/help/small-business-notifications) |
| LO-30 | Conversioni misurate: clic su `tel:`/email/prenotazione come eventi; collegamento GBP → GA4 | Auto (eventi nel codice); Manuale (GA4) | Media | [SEJ 2026-06, news Google] |
| LO-31 | Prezzi/fasce e modalità (in presenza/online, durata) dichiarati in testo | Auto + giudizio | Media | [SEJ 2026-07, Heitzman] · [G](https://developers.google.com/search/docs/appearance/structured-data/local-business) (`priceRange`) |
| LO-32 | Credenziali e iscrizioni professionali verificabili sulla pagina del professionista (temi vicini a lavoro/denaro) | Manuale | Alta | [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |

## Checklist off-site (azioni manuali che la skill può solo guidare)
La skill prepara testi, campi e verifiche; l'utente esegue.

**Google Business Profile**
- [ ] Verificare l'**idoneità** [GBP\*]: incontri di persona (studio o presso il cliente)? Se il servizio è **solo online**, il GBP non è idoneo: puntare su sito, entità e menzioni.
- [ ] Rivendicare/verificare la scheda; un solo profilo per sede reale; nessuna scheda duplicata.
- [ ] **Nome** reale senza keyword o città aggiunte [GBP\*].
- [ ] **Categoria principale** più specifica + poche secondarie pertinenti; verificare che i **servizi** elencati coincidano con le pagine servizio del sito [SEJ 2025-12, Riddall].
- [ ] **Sede vs area servita**: se si ricevono clienti → indirizzo visibile; se si va dai clienti → indirizzo nascosto + area servita [GBP\*]. Mai indirizzi di uffici virtuali.
- [ ] **Orari** reali + orari speciali per festività/ferie impostati in anticipo; stato "temporaneamente chiuso" per chiusure lunghe [GBP\*]; per SEJ "aperto al momento della ricerca" è tra i fattori più citati del local pack [SEJ 2026-03, Heitzman, sondaggio Whitespark].
- [ ] **Descrizione** con il linguaggio dei clienti (non elenco di keyword).
- [ ] **Foto** autentiche (studio, persona, contesto), non stock; aggiornarle periodicamente [SEJ 2026-03, opinione].
- [ ] **Post** per novità/eventi; da settembre 2026 il GBP mostra le **visualizzazioni per post** (ultimi 18 mesi) [SEJ 2026-09, news Google].
- [ ] **Link di prenotazione/appuntamento** e link al sito con parametri UTM coerenti (canonical al URL senza UTM [G](https://developers.google.com/search/help/office-hours/2024/august)).
- [ ] Collegare **GBP → Google Analytics** (7 metriche, conservazione 6 mesi) [SEJ 2026-06, news Google].
- [ ] Controllare il **profilo pubblico**, non solo la dashboard (bug luglio 2026 con dashboard recensioni vuote) [SEJ 2026-07].

**Recensioni**
- [ ] Chiedere recensioni a **tutti** i clienti (niente filtro sui soddisfatti), con link/QR semplice; nessun incentivo non dichiarato; per SEJ/Moz da aprile 2026 le norme Maps vietano di chiedere dettagli prestabiliti (es. nome del collaboratore) o un numero fisso di recensioni [SEJ 2026-09, relatori Moz — verificare].
- [ ] Ricordare che si può recensire con **nickname** (utile in ambiti personali come carriera, salute, legale) [SEJ 2025-12, news Google].
- [ ] Rispondere a tutte, anche negative, pensando al lettore successivo.
- [ ] Analizzare i **temi** delle recensioni proprie e di 2–3 concorrenti per scrivere H1, FAQ, descrizione GBP [SEJ 2026-06, opinione].

**Altre schede (coerenza NAP)**
- [ ] **Bing Places** (gratuito, import da GBP) [SEJ 2025-10, news Microsoft].
- [ ] **Apple Business Connect** / scheda Apple Maps [SEJ 2026-07/08].
- [ ] Directory **di settore** e associazioni professionali credibili (per utenti e reputazione, non per link) [G](https://developers.google.com/search/help/office-hours/2022/november).
- [ ] Censire schede vecchie/duplicate (vecchi indirizzi, numeri) e chiederne correzione o chiusura.

**Reputazione e menzioni locali**
- [ ] Menzioni da stampa locale, associazioni, enti, partner, eventi (talk, workshop) [SEJ 2026-08, Uberall/AthenaHQ; SEJ 2026-07, Montti].
- [ ] Mai liste "migliori di [città]" a pagamento o auto-pubblicate.

**AI e assistenti (monitoraggio, non ottimizzazione)**
- [ ] Lista fissa di 10–20 domande (orari, servizi, prezzi, "chi consiglieresti per … a [città]") su AI Overview/AI Mode, ChatGPT, Gemini, Perplexity, Copilot; ripetere più volte, registrare data/luogo/dispositivo; correggere le **fonti** sbagliate (vecchie directory, thread) [SEJ 2026-07, Searchable].
- [ ] Bing Webmaster Tools (report AI Performance) come fonte gratuita di citazioni Copilot [SEJ 2026-03].

## Regole per contenuti e struttura del sito
1. **Pagine servizio prima delle pagine città.** Una pagina per ogni servizio reale (cosa, per chi, come si svolge, durata, prezzo o fascia, in presenza/online, prossimo passo). Le pagine località sono legittime solo se esiste una **sede reale** o un contenuto davvero locale (casi, partner, normative, logistica); altrimenti è doorway [G](https://developers.google.com/search/docs/essentials/spam-policies).
2. **Test anti-doorway** (deduzione): se sostituendo il nome della città la pagina resta vera, non deve esistere come pagina separata.
3. **Area servita in prosa**: "ricevo a [città]; consulenze online in tutta Italia" — non elenchi di comuni.
4. **Professionista locale + online** (deduzione da [G] + [GBP\*]):
   - sede fisica che riceve clienti → GBP con indirizzo + `LocalBusiness` (sottotipo più specifico) sulla pagina contatti;
   - va dai clienti → GBP con area servita; nel sito nessun indirizzo che nel GBP è nascosto;
   - solo online → niente GBP; `Organization` o `Person`/`ProfilePage` (vedi `entity-personal-brand.md`); pagina "Consulenza online" unica, non una per città;
   - stessa offerta in presenza e online → una pagina servizio con due modalità, non due pagine quasi uguali.
5. **Pagina contatti completa in HTML**: nome, indirizzo o area, telefono `tel:`, email, orari, modalità di prenotazione, mappa opzionale (l'iframe non sostituisce il testo).
6. **Chiusure temporanee** (deduzione + [G]): avviso visibile in alto, orari aggiornati nel JSON-LD (`validFrom`/`validThrough`), GBP con orari speciali o "temporaneamente chiuso"; non mettere `noindex`, non spegnere il sito, non redirigere.
7. **Recensioni sul sito**: mostrarle come testo con nome/data e fonte; **niente stelle nel markup** della propria attività; nessuna recensione modificata o selezionata in modo ingannevole [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
8. **Fatti verificabili in testo**: prezzi o fasce con le variabili, tempi, modalità, credenziali; sono le informazioni che gli assistenti cercano e che Google suggerisce di avere in forma testuale [G](https://developers.google.com/search/docs/appearance/ai-features).
9. **Temi vicini a YMYL** (lavoro, carriera, denaro, salute): niente garanzie di risultato, autore con credenziali reali, fonti citate, aggiornamenti datati [G](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
10. **Contenuti informativi** (blog, guide) collegati alle pagine servizio, basati su domande reali dei clienti, non una pagina per ogni variante di query [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
11. **Dati strutturati minimi e mantenuti**: meglio un `LocalBusiness` corretto e aggiornato che un markup ricco ma obsoleto (rischio: telefono vecchio nello schema) [SEJ 2026-09, Shaw/Jeffery].
12. **Italia (nota fuori corpus, verificare con consulente)**: per attività con partita IVA la sua indicazione sul sito è un obbligo di legge; Google la considera un indicatore di fiducia (`vatID`) [G](https://developers.google.com/search/docs/appearance/structured-data/organization).

## Cosa dicono le fonti terze
Formato: [SEJ AAAA-MM, autore, tipo evidenza e campione]. ⚠ = va oltre o contro Google.

**Business Profile e ranking locale**
- [SEJ 2026-03, Heitzman, opinione + sondaggio Whitespark 2026 e BrightLocal su 50 attività] Categoria principale = fattore n. 1 del local pack, poi prossimità e **parole chiave nel nome**; "aperto ora" tra i primi 5; recensioni +peso (16%→20%). ⚠ Le keyword nel nome violano le linee guida GBP [GBP\*]: non raccomandarle. Cadenze (post settimanali, foto bisettimanali, risposta entro 48 h) = opinione.
- [SEJ 2025-11, Riddall, checklist d'esperienza] Audit locale in 11 punti (GBP completo, recensioni con risposta, NAP, link locali, contenuti per fase, AI Mode). ⚠ Raccomanda schema `Review` e `FAQPage`: il primo è vietato sulla propria attività, il secondo non dà più risultati avanzati.
- [SEJ 2025-12, Riddall, opinione + dati terzi] GBP come "fonte verificata" per AI Mode; servizi GBP coerenti col sito; CTA above the fold; KPI = chiamate, indicazioni, prenotazioni.
- [SEJ 2026-06, Southern, news] Ask Maps (USA/India): risposte multi-condizione basate su dati completi del profilo; Google ha chiuso l'API Q&A (nov 2025); stato del Q&A pubblico incerto.
- [SEJ 2025-10, news Microsoft] Bing Places rinnovato, gratuito, import da GBP.

**Recensioni**
- [SEJ 2026-06, Southern, studio peer-reviewed su 251 PMI USA, dati auto-dichiarati] Le stelle da sole non predicono i risultati; li predice la **gestione attiva** della reputazione.
- [SEJ 2026-06, vendor SOCi, 350.000 sedi] ChatGPT raccomanda l'1,2% delle sedi (Gemini 11%, Perplexity 7,4%) contro 35,9% di presenza nel 3-pack; rating medio delle sedi raccomandate ~4,3. Correlazione, dati di vendor.
- [SEJ 2026-07, news Google] Le linee guida snippet recensione esplicitano recensioni false/incentivate non dichiarate → azione manuale.
- [SEJ 2026-06, Wiideman, caso n=1] ⚠ Proposta di recensioni con frasi suggerite ("semantic triples"): recensioni pilotate, contrarie alle norme; non usare.

**Coerenza dei dati e directory**
- [SEJ 2026-07, vendor Searchable, 165 aziende di Londra, 13.365 domande] 93% con almeno un fatto sbagliato/mancante negli assistenti AI; piccole imprese più colpite.
- [SEJ 2026-08, vendor Uberall/AthenaHQ, 7 modelli] Coerenza NAP/orari/categorie tra GBP, Apple, Bing, directory; conferme esterne con criteri editoriali, non liste a pagamento.
- ⚠ Contro Google: diversi autori trattano le "citazioni" in directory come fattore di ranking; Google dice che le directory non servono alla SEO. Sintesi per la skill: coerenza sì, iscrizione massiva per link no.
- [SEJ 2026-01, van Berkel/Schema App, caso singolo di vendor, nessun controllo] ⚠ `areaServed`/`sameAs` verso Wikidata nelle pagine sede con "causazione completa" del +25% click: affermazione non sostenibile; `areaServed` non è tra le proprietà documentate da Google per `LocalBusiness` (lecito in schema.org, effetto non documentato).

**AI e ricerca locale**
- [SEJ 2026-07/08, Whitespark citato, 540 query in 3 città USA] AI Overview nel 15% delle query locali dirette, 92% informative, 97% ibride; un altro articolo riporta 68% per query "tipo di attività": numeri dipendenti dal tipo di query, citare con cautela.
- [SEJ 2026-09, CallRail, webinar sponsorizzato] Click da citazioni AI ~1–2% delle chiamate; i bot AI non eseguono JS → NAP nell'HTML iniziale; scambio numeri lato browser invisibile ai bot.
- [SEJ 2026-09, Shaw/Jeffery, webinar senza dati] Cloudflare blocca spesso i crawler AI di default; widget recensioni JS invisibili; schema "dannoso" solo se non mantenuto. Pannello diviso sull'utilità dello schema.
- [SEJ 2026-09, news] Dal 18/09/2026 unità aggregatori/fornitori SEE anche per query locali: monitorare, nessuna azione specifica.
- [SEJ 2026-05, Southern su I/O] USA: Google può telefonare alle attività per conto dell'utente; orari, prezzi e disponibilità chiari diventano requisito pratico.
- [SEJ 2026-08, Kris Jones, opinione] Audit: chiedere a un assistente di consigliare un fornitore della propria categoria; correggere fonti obsolete (caso thread Reddit con prezzi vecchi).

**Pagine località**
- [SEJ 2026-07, Heitzman, esperienza di agenzia su 15+ mercati] Pagine sede non fotocopia con NAP/orari, FAQ locali, casi reali; guide ai costi con fasce. ⚠ "3 foto di monumenti per provare la località" e "finestra di 12–18 mesi": nessuna base.
- [SEJ 2026-02, Forrester, modello concettuale] Pagine locali con prova di presenza reale e confini di servizio; rimuovere doorway a livello di template.

## Miti e consigli obsoleti
- **"Iscriversi a tante directory migliora il ranking"** → no per Google; directory di bassa qualità per link = spam [G](https://developers.google.com/search/help/office-hours/2022/november).
- **"Una pagina per ogni città aumenta la copertura"** → doorway [G](https://developers.google.com/search/docs/essentials/spam-policies).
- **"Elenco di città in footer"** → keyword stuffing [G](https://developers.google.com/search/docs/essentials/spam-policies).
- **"Stelle in SERP con il widget delle recensioni Google sul sito"** → non idonee (self-serving) [G](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **"`FAQPage` per ottenere spazio in SERP"** → risultati avanzati FAQ rimossi nel 2026 [SEJ 2026-05].
- **"Lo schema `LocalBusiness` fa comparire nel local pack / nelle AI"** → il local pack dipende dal GBP; nessun markup speciale per l'AI [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"`llms.txt` o versioni Markdown aiutano gli assistenti locali"** → ignorati dalla Ricerca Google [G](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **"Keyword nel dominio (es. orientamento-milano.it)"** → effetto quasi nullo; i sistemi non premiano i domini a corrispondenza esatta [G](https://developers.google.com/search/docs/appearance/ranking-systems-guide).
- **"Geotag/EXIF nelle foto"** → Google non usa gli EXIF delle immagini nella Ricerca [G](https://developers.google.com/search/help/office-hours/2023/january); per il GBP non documentato (deduzione).
- **"Durante le ferie metto il sito in manutenzione/noindex"** → si perde visibilità; usare orari speciali e avvisi (deduzione + [G]).
- **"Comprare liste 'migliori di [città]'"** → l'elenco dei luoghi più apprezzati richiede liste non sponsorizzate [G](https://developers.google.com/search/docs/appearance/top-places-list); menzioni inautentiche = spam.
- **"Prezzi variabili con `Product` per servizi"** → usare `LocalBusiness` con `priceRange` [G](https://developers.google.com/search/help/office-hours/2023/january).
- **Consigli USA trasferiti all'Italia**: Ask Maps, chiamate AI, booking agentico, annunci Apple Maps, strumenti GBP in Gemini non sono disponibili in Italia/SEE a ottobre 2026.
