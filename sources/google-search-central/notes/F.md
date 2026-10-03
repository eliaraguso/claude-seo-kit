# Gruppo F — Help: FAQ, debug, notifiche, segnalazioni, dashboard stato, Office Hours 2022–2024

Appunti fedeli alla documentazione Google Search Central (versione IT, letta integralmente). Dove si riporta un'opinione/risposta del team Google nelle Office Hours, è indicata come tale.

---

## Ricevi assistenza per il tuo sito dalla Ricerca Google (hub Help)
Fonte: https://developers.google.com/search/help?hl=it

- Pagina indice delle risorse di assistenza: Nozioni di base sulla Ricerca (requisiti tecnici + norme spam), Centro assistenza Search Console, Guida introduttiva alla SEO, canale YouTube Google Search Central, Community di assistenza (multi-lingua: scansione, indicizzazione, ranking, dati strutturati, Search Console).
- Percorso consigliato: prima consultare risorse Google e post esistenti nella Community, poi pubblicare una domanda nella Community (risposte da "esperti di prodotto" e altri professionisti).
- Dashboard dello stato (status.search.google.com) per verificare se la Ricerca funziona regolarmente + dati storici.
- Office Hours ("sessioni di consulenza sulla SEO"): registrate mensilmente, pubblicate su YouTube; domande inviabili tramite modulo.
- **Moduli per segnalare problemi direttamente a Google (richiedono accesso all'account Search Console):**
  - Problema di verifica del sito (proprietà Dominio).
  - Problema di sicurezza persistente e non risolvibile.
  - Bug di indicizzazione (se si continua a riscontrare problemi di indicizzazione e si sospetta un bug).

## Domande frequenti sulla scansione e sull'indicizzazione
Fonte: https://developers.google.com/search/help/crawling-index-faq?hl=it

- **Aggiungere il sito su Google**: scansione e indicizzazione richiedono tempo e dipendono da molti fattori; Google **non può fare previsioni né dare garanzie** su se/quando un URL sarà scansionato o indicizzato.
  - In Search Console verificare **entrambe le versioni "www" e "non www"**.
  - Una **Sitemap aiuta a rilevare il sito ma non garantisce l'indicizzazione né migliora il ranking**.
- **Perché il sito non è indicizzato** — motivo più comune: il sito è **troppo recente** → pazienza + richiedere scansione/indicizzazione. Altri motivi:
  - sito poco collegato da altri siti tramite link multipli;
  - struttura del sito che rende difficile scansione/indicizzazione; il sito stesso blocca esplicitamente scansione/indicizzazione;
  - sito momentaneamente non disponibile durante la scansione (vedi errori di scansione in Search Console);
  - non conformità alle Nozioni di base sulla Ricerca, sito compromesso/modificato da terzi;
  - in rarissimi casi, problemi dovuti a contenuti precedentemente ospitati sul dominio → richiesta di riconsiderazione citando cambio di contenuti e proprietà;
  - spostamento recente del sito → seguire istruzioni di spostamento siti;
  - un proprietario precedente o altra persona con accesso ha richiesto una **rimozione tramite Search Console** → annullabile con lo strumento Rimozioni.
- **Stessi contenuti su due domini**: usare **redirect 301** dal dominio alternativo a quello preferito. È il metodo migliore; gli indicatori di ranking (PageRank, link in entrata) **vengono trasferiti correttamente** con i 301.
- **Contenuti duplicati**: in genere **non** violano le norme spam ("sanzione per contenuti duplicati" è un concetto da chiarire/mito). Gestione: canonical per pagine simili/duplicate, parametri URL, scraper, duplicazione tra domini.
- **Sottocartelle vs sottodomini**: scegliere la soluzione più facile da gestire; **Google non ha preferenze** per indicizzazione e ranking.
- **Validazione W3C**: **non** migliora il ranking (almeno non direttamente); un HTML pulito aiuta compatibilità browser e accessibilità.
- **Hosting con frame / "redirect mascherati" / "inoltro mascherato"**: ospitare sempre i contenuti direttamente sul proprio dominio; un servizio di inoltro con frame in genere **rende impossibile** scansione, indicizzazione e ranking dei contenuti con il proprio dominio.
- **Testo modificato non aggiornato nei risultati**: non si può forzare l'aggiornamento. Suggerimenti: richiedere nuova scansione degli URL; aggiornare la **data di ultima modifica (lastmod) nella Sitemap**; risolvere i duplicati interni (più URL per stesso contenuto) per far trovare prima i contenuti aggiornati.
- **PHP, ASP, CGI, JSP, CFM ecc.**: indicizzabili se producono pagine visibili nel browser **senza plug-in**; nessuna preferenza tra tecnologie per scansione/indicizzazione/ranking, purché scansionabili.
- **Dominio acquistato con passato di spam**: verificare il sito in Search Console e controllare il **report Azioni manuali**.

## Eseguire il debug delle pagine
Fonte: https://developers.google.com/search/help/debug?hl=it

- Google **non riscansiona subito** dopo una correzione: Search Console e la Ricerca possono mostrare l'errore finché la pagina non viene riscansionata. Scansione rapida richiedibile a volte (Controllo URL), ma **di solito servono alcuni giorni**.
- **Strumenti per proprietari verificati** (Search Console, dati riservati):
  - Report stato risultati avanzati (non testa URL arbitrari; permette di chiedere nuova scansione dopo la correzione).
  - Controllo URL: come la pagina appare nell'indice, test live di un URL pubblicato, come Google esegue il **rendering**, invio URL per indicizzazione.
  - Report robots.txt: se Google può elaborare i robots.txt; richiesta di nuova scansione del robots.txt in emergenza.
  - Report stato pagine AMP (non testa URL arbitrari).
- **Strumenti anonimi** (qualsiasi URL, senza permessi SC; alcuni accettano codice incollato): Test pagine AMP; **Test dei risultati avanzati** (valida dati strutturati in tempo reale, da codice incollato o URL pubblicato).
- **Test di pagine locali o dietro firewall**: usare un tunnel (es. `ngrok`) per ottenere un URL pubblico.
  - Esempio: `python3 -m http.server 5326` poi `./ngrok http 5326 --request-header-add ngrok-skip-browser-warning:1`; passare l'URL ngrok allo strumento (es. `https://search.google.com/test/rich-results/result?url=<URL codificato>`).
  - Alcune soluzioni di tunneling (non ngrok) proteggono l'URL temporaneo con robots.txt → **gli strumenti di test Google rispettano robots.txt** e non potranno testarlo.
- **Errori di accesso negli strumenti**: verificare che la pagina non sia bloccata da robots.txt e non richieda login; provare l'accesso fuori dal firewall, da altro computer o in incognito.

## Inviare un'idea di domanda per le Office Hours
Fonte: https://developers.google.com/search/help/office-hours?hl=it

- Office Hours = Googler del Team per la qualità della Ricerca rispondono a domande; pubblicazione mensile su YouTube.
- **Non adatte a domande specifiche per un sito**; non rispondono a tutte. Per domande sul proprio sito: **forum di Google Search Central** (Community).
- Esempi di domande generali: .com vs .nl per un sito olandese; molti redirect e scansione/ranking; sistema contenuti utili e soddisfazione; URL e pagina in lingue diverse.

## Segnalare spam, phishing o malware
Fonte: https://developers.google.com/search/help/report-quality-issues?hl=it

- Moduli per segnalare risultati dovuti a spam, link a pagamento, malware o altri problemi di qualità; servono a migliorare i sistemi antispam.
- **Spam/pagine ingannevoli/bassa qualità**: le tecniche di manipolazione del ranking violano le norme spam e possono influire negativamente sul ranking; Google **può** usare la segnalazione per **azioni manuali**.
  - **Non includere dati personali identificativi**: il testo della segnalazione viene inviato al proprietario del sito (contesto dell'eventuale azione manuale); le segnalazioni con PII **non vengono elaborate**.
- **Malware**: modulo Safe Browsing "report badware".
- **Phishing**: modulo Navigazione sicura (pagine che imitano altre per carpire dati personali).

## Domande frequenti sull'aspetto dei siti nei risultati
Fonte: https://developers.google.com/search/help/site-appearance-faq?hl=it

- **Link del titolo**: in genere preso dall'elemento `<title>`; **può anche essere estratto dai link che rimandano alla pagina**. Titoli utili e pertinenti aiutano Google e gli utenti a scegliere su cosa cliccare.
- **Snippet**: Google estrae automaticamente la parte più pertinente alla query. Per impedirlo: `<meta name="robots" content="nosnippet">`; oppure aiutare con **meta description utili**.
- **Prezzi, recensioni, stelle**: tramite **dati strutturati** (markup strutturato dei contenuti: recensioni, dati prodotto, dati di contatto).
- **Risultati locali (mappa)**: se la query è basata su località, Google mostra una mappa con attività pertinenti; se l'attività non compare, assicurarsi che sia stata aggiunta a **Profilo dell'attività (Google Business Profile)**.
- **Reintegro di un sito**:
  - malware rimosso → richiesta di controllo malware;
  - spam / violazione norme spam corretta → **richiesta di riconsiderazione**;
  - rimozione richiesta dal proprietario e poi ripensata → richiesta di reintegro contenuti;
  - avviso phishing ritenuto errato → segnalazione avviso phishing errato.
- **Immagini nei prodotti Google**: seguire best practice Google Immagini; Storie web; foto/video su Google Maps (Local Guides); immagini tramite **Profilo dell'attività** (foto aziendali per mostrare prodotti e servizi).

## Domande frequenti sulla posizione dei siti nei risultati
Fonte: https://developers.google.com/search/help/site-position-in-search-faq?hl=it

- **Ottenere link**: creare contenuti unici e interessanti che le persone vogliano linkare. Google rileva link non naturali (scambio link, link a pagamento, link generati automaticamente) → partecipare a questi schemi può essere più negativo che positivo.
- **Calo di ranking**: il web è un ecosistema in mutamento; il rendimento varia per diversi motivi → partire da "Perché non vedo la mia pagina nella Ricerca Google".
- **TLD (.com, .org, .gov, .ponies)**: **non** influisce sul rendimento; un nuovo gTLD può essere restituito se è il risultato migliore.
- **Concorrenti**: Google fa del suo meglio perché i concorrenti non possano danneggiare il ranking; per link indesiderati da un altro sito → contattare il proprietario.
- **Azioni manuali antispam**: es. testo o link nascosti, cloaking, redirect non ammessi (vedi norme spam).
- **Dopo la correzione**: inviare **richiesta di riconsiderazione**; la procedura può richiedere **diverse settimane**.
- Immagini → best practice Google Immagini; video → best practice video.
- **Annunci a pagamento**: **non** migliorano né peggiorano il ranking organico; inserimento e ranking sono gratuiti; Google non accetta pagamenti per velocizzare l'inserimento o migliorare il ranking.

## Legge SB 2262 del Tennessee (2026): notifiche per piccole imprese
Fonte: https://developers.google.com/search/help/small-business-notifications?hl=it

- La legge dà diritto a certe piccole imprese del Tennessee di ricevere notifica se schede digitali o recensioni vengono rimosse/limitate sui motori di ricerca. Indicazioni valide in generale per ricevere notifiche da Google:
- **Verificare il sito in Search Console** → notifiche automatiche per: spam e violazioni delle norme (azioni manuali), rimozioni per motivi legali, problemi di sicurezza (malware, contenuti compromessi).
- **Rivendicare/gestire il Profilo dell'attività su Google** (vetrine locali): aggiornamenti diretti su restrizioni Maps, rimozioni legali, restrizioni di massa sulle recensioni, violazioni norme.
- **Merchant Center** per chi vende prodotti online: avvisi su problemi/rimozioni delle schede prodotto.

## Utilizzare la dashboard dello stato della Ricerca Google
Fonte: https://developers.google.com/search/help/status-dashboard?hl=it

- status.search.google.com: stato dei sistemi della Ricerca; mostra problemi che interessano **molti siti o utenti** (un'annotazione può spiegare una variazione di rendimento). Mostra anche gli **ultimi aggiornamenti di ranking** rilevanti. Feed RSS/Atom: `status.search.google.com/en/feed.atom`.
- Ciclo di vita di un problema: rilevamento e risposta iniziale → indagine → follow-up → attenuazione o correzione.
- **Stati**: Disponibile; Informazioni sul sistema (aggiornamento/modifica, es. inizio rollout di un update di ranking o Googlebot che inizia a scansionare su HTTP/2); Malfunzionamento del sistema (prestazioni inferiori per una terza parte comune, es. DNS); Interruzione del sistema (non funziona in larga misura, molti siti/utenti).
- Un problema è "risolto" solo quando Google è certa che le modifiche metteranno fine all'impatto; **i siti possono risentirne finché Google non li rielabora**. "Mitigazione" = riduzione di impatto/ambito; "soluzioni alternative" = passi che il proprietario può fare (es. usare un DNS diverso).
- Aggiornamento di ranking segnalato → seguire il link per indicazioni; **spesso non è richiesto alcun intervento**.
- Problema non elencato → probabilmente limitato alle proprie pagine o a pochi siti → Community di Search Central.
- Cronologia disponibile per **5 anni** (pagina Riepilogo e cronologia).

---

# Office Hours (sessioni di consulenza SEO) — trascrizioni 2022–2024

Nota: le Office Hours **non** trattano casi specifici di siti; per quelli Google rimanda alla Community di Search Central. Relatori ricorrenti: John (Mueller), Gary (Illyes), Lizzi (Sassman), Alan (Kent), Duy (Nguyen), Martin (Splitt) e altri.

## Office Hours — novembre 2022
Fonte: https://developers.google.com/search/help/office-hours/2022/november?hl=it

**Dati strutturati**
- Più valori separati da virgola in un campo schema? → In generale **un solo valore per campo**; GTIN è un identificatore, quindi uno solo. Se hai GTIN e ISBN usa le rispettive proprietà distinte. Controllare sempre la documentazione della singola funzionalità.
- Schema WebSite + SoftwareApplication/Organization in home? → Dipende, sono funzionalità diverse. Se il sito riguarda un'app si può aggiungere SoftwareApplication. **Nidificare in modo che ci sia un solo nodo WebSite sulla home page**, non più nodi (la cosa più importante).
- Snippet FAQ con solo HTML? → Per il risultato avanzato FAQ **serve il markup schema FAQ**; alcune altre funzionalità possono estrarre dal contenuto, verificare la documentazione specifica.
- Key moments (video) non solo YouTube: disponibili e usati da diversi fornitori di video.
- Paywall: usare i dati strutturati del paywall; se si vuole evitare del tutto la presenza in Ricerca → `noindex` su quelle pagine.

**Canonical, noindex, scansione**
- Google non rileva il canonical desiderato → la canonicalizzazione usa **rel=canonical + redirect, Sitemap, link interni, link esterni e altro**: far puntare **tutti gli indicatori** allo stesso URL. La canonicalizzazione riguarda quale URL viene mostrato, **non influisce sul ranking**.
- Canonical autoreferenziale → secondo John "non fanno nulla" di per sé, ma diventano utili quando la pagina compare sotto altri URL (es. con parametri UTM).
- La lunghezza dei contenuti **non** incide su frequenza di scansione/indicizzazione; i contenuti di nicchia non sono penalizzati; i contenuti popolari con molti link vengono scansionati/indicizzati più facilmente.
- Molte pagine `noindex` **non** causano effetti indesiderati su scansione e indicizzazione del sito; anche milioni di URL `noindex` (es. ricerche interne linkate da spam) → continuare con `noindex`, non preoccuparsi del crawl budget.
- Rapporto pagine indicizzate/non indicizzate in Search Console: **nessun rapporto magico**. Per siti con **meno di ~1 milione di pagine** probabilmente non serve preoccuparsi del crawl budget; rimuovere link interni inutili è più pulizia che SEO.
- "Google ruota le pagine indicizzate per giorno della settimana?" → **No**.
- Molti 404 interrompono la scansione? → **No**: era un refuso nella documentazione (doveva essere "errori del certificato HTTPS"). I 404 sono una parte normale del web e non incidono sulla scansione del sito nel complesso.
- Pagine create automaticamente tipo `/page/2` in WordPress: per limitare scansione/indicizzazione meglio **Disallow in robots.txt** che link `nofollow` (meno lavoro, meno vulnerabile: non controlli come altri linkano).
- Link `rel="ugc"` non rimuovono la pagina di destinazione dall'indice; per impedire l'indicizzazione usare **meta robots `noindex`**.
- La copia cache **non** è necessaria per comparire in Ricerca; assenza di cache non è un segnale di qualità.
- URL di riferimento "sconosciuto" nei 4xx di Search Console → la pagina referente è stata trovata ma non indicizzata.
- Parametri URL (es. add-to-cart) non sono un problema SEO di per sé; contano per crawl budget solo su siti **molto grandi** se generano aumenti esponenziali di URL. Per siti piccoli/medi: occuparsene in seguito.

**Contenuti e qualità**
- Siti che accettano guest post a pagamento senza valutare contenuti/link → rischio ranking più basso (sistema contenuti utili e altri sistemi).
- Articolo lungo diviso in più parti: il **numero di parole non indica contenuti scarni**; entrambi gli approcci sono legittimi; puntare a valore sufficiente su ogni pagina.
- Eliminare 10.000 pagine senza valore: basta eliminarle; **eliminare pagine scadenti non rende automaticamente il sito più importante**, il sito deve avere valore di per sé.
- Contenuti copiati/riscritti con AI da altri siti → violazione norme spam; segnalare con il modulo spam.
- Meta description su 10.000+ pagine: si possono **generare programmaticamente** (es. siti grandi basati su database), ma devono essere uniche, specifiche e pertinenti; non ripetere la stessa.
- Testo intorno alle immagini (didascalie, titoli) aiuta a comprendere l'immagine: deve essere pertinente e descrittivo.
- Recensioni prodotto: focus sui prodotti fisici ma a volte anche digitali; link di affiliazione **non necessari**; utile linkare risorse utili. Impatto su tutto il sito probabilmente dovuto ad altro aggiornamento.
- Pagine prodotto definitivamente esaurite: si possono eliminare; per usabilità mantenere per un po' o redirect se linkate/salvate.
- Rimuovere contenuti vecchi: **404 o 410**, oppure redirect a una pagina che aiuti l'utente; deve avere senso per il sito, non per i motori.

**Link**
- Disavow (esclusione link) per proprietà Dominio non disponibile → verificare la proprietà a livello di prefisso (senza token aggiuntivi se dominio già verificato). **Sconsigliato rifiutare link casuali "strani" o segnalati da tool**: usare il disavow solo se hai pagato link e non riesci a farli rimuovere.
- Backlink: impatto **molto meno significativo** rispetto ai primi anni; centinaia di indicatori di ranking; campagne di link building solo per creare link = link spam; algoritmi li rilevano e li annullano su larga scala.
- Acquistare backlink? → spreco di denaro; meglio investire in un ottimo sito, esperienza utente, contenuti utili.
- Anchor text interni quasi tutti uguali (menu, prodotti) → **normale**, nulla da fare.
- "Spam score" di tool terzi → **Google non usa punteggi di tool SEO di terze parti**.
- Siti di schede locali (directory) per la SEO locale: **non** aggiungere il sito a directory per migliorare la SEO; usarle eventualmente per traffico non da Ricerca. "La ricerca locale è diversa".

**Internazionale / lingua**
- URL in lingua diversa dai contenuti: nessun effetto negativo SEO; possibile problema per gli utenti (condivisione).
- hreflang senza tag di ritorno: Google usa le annotazioni valide e ignora quelle non funzionanti, senza altri effetti negativi sul sito; comunque correggerle.
- hreflang su molti siti nazionali non controllati → gestirli da un'unica posizione con le **Sitemap** (cross-submit, sitemaps.org).
- Sitemap hreflang: sono normali Sitemap con annotazioni; posizionabili ovunque (robots.txt o Search Console nei siti verificati). Vale anche per Sitemap immagini/video.
- `x-default` può variare per set di pagine; indica la pagina mostrata a chi cerca in lingue non specificate; decidere in base all'utente.

**Varie**
- HTTP/3 **non** è un fattore di ranking né usato in scansione (a novembre 2022); improbabile impatto significativo sui Core Web Vitals.
- Migrazione su nuovo dominio: fluttuazioni normali, **nessuna tempistica stabilita** di stabilizzazione; spostare una sola sezione non equivale a uno spostamento completo.
- Discover: nessuna azione per abilitarlo; criteri diversi dalla Ricerca; traffico Ricerca non garantisce traffico Discover.
- Nuovo sito con nome simile a un'entità famosa (es. "Weird All" vs "Weird Al") → molto difficile distinguersi; **scegliere un nome che non sia un errore di battitura di qualcosa di molto noto**; Google tende a correggerlo come refuso.
- Casualità nei risultati per i siti meno noti? → lo scopo è fornire i risultati più utili.
- Report Rendimento confuso: differenze tra dati per query e per pagina, **filtri privacy** sui dati per query; le tendenze tendono a coincidere.
- Sito non indicizzato: controllare errori in Search Console; **Google non indicizza tutto il web**, i contenuti devono distinguersi in qualità.

## Office Hours — dicembre 2022
Fonte: https://developers.google.com/search/help/office-hours/2022/december?hl=it

**Redirect, migrazioni, URL**
- Riduzione da 30.000 a 2.500 prodotti (400.000 redirect 301): in genere **mantenere il dominio esistente**; cambio dominio supportato via 301 ma rischio maggiore di perdere traffico se si sbaglia. Le vecchie pagine possono dare 404 o redirect.
- Troppi 301? → **Nessun limite**, anche milioni; non serve redirigere ogni 404. 404 in Search Console non sono un problema se le pagine devono dare 404.
- Molti redirect (es. doppio degli URL) → nessun problema; evitare **troppi hop nelle catene di redirect**.
- Migrazione tra piattaforme (Blogger → WordPress): non serve mantenere gli stessi URL; importante che **ogni vecchio URL rediriga al nuovo URL specifico pertinente**; **non redirigere tutto alla home** del nuovo dominio.
- Cambiare spesso gli URL (es. stagionali) → sconsigliato; se necessario, redirect appropriati.
- Vecchio sito/pagina gratuita dopo il passaggio a un nuovo dominio → idealmente **redirect del vecchio al nuovo** o almeno eliminarlo; tenere online un sito obsoleto confonde motori e utenti.
- Link verso una pagina che era 404: tornano a contare quando la pagina torna online, dopo la riscansione delle pagine che linkano e se ancora ritenuti pertinenti.
- Redirect tramite pagina bloccata da robots.txt: metodo valido per impedire il passaggio di segnali (PageRank) da un link.

**Velocità / CWV**
- Velocità conta: Google usa i **Core Web Vitals** come parte del fattore di ranking dell'esperienza sulle pagine; non sostituisce la pertinenza.
- GTMetrix buono ma CWV scadenti → "forse": esistono dati di laboratorio e dati reali (field); capire l'approccio appropriato.

**JavaScript, link, scansione**
- Menu al `mouseover`: Google può seguirne i link se il menu è nell'HTML e i link sono **tag `<a>` con `href`**; verificare con Controllo URL.
- Selettore negozio popup in JavaScript: Google segue `a href`; se implementato in JS, Google potrebbe non vedere gli altri negozi e non trovare le relative pagine.
- Sito Google con pagine generate dinamicamente e indicizzazione lenta: problema principale = **non usa normali link HTML**, la scansione è affidata "al caso"; per siti JS seguire le linee guida JavaScript SEO.
- Velocità di scansione/indicizzazione: dipende da come il sito è percepito su internet (noto a molti → più veloce) e dalla **qualità costante dei contenuti**.
- Pagine impaginate (`?page=2`) in Sitemap: possibili ma spesso nessun vantaggio (scoperte via link); Google potrebbe indicizzare solo la prima. Numero di pagina nel title: effetto minimo, solo se aiuta l'utente.
- Indicizzazione mobile-first: Google si concentra sulla versione mobile; con URL desktop/mobile separati è normale che il desktop risulti "pagina con redirect"; nessun trucco per indicizzare solo il desktop; se contenuti equivalenti, nessun impatto significativo sul ranking.

**Deindicizzazione, sicurezza, staging**
- Deindicizzare URL: rimuovere la pagina con **404/410** oppure **`noindex` consentendo a Googlebot di scansionarla**; serve una riscansione; per poche pagine si può richiedere l'indicizzazione in Search Console.
- Sito hackerato: rimuovere con 404 o `noindex`; dopo la risoluzione, i 404 residui nei report non sono un problema (spariscono col tempo).
- Milioni di URL creati da bot: 404 o `noindex` vanno bene anche su milioni di pagine; eventualmente robots.txt; i report SC mostreranno effetti più a lungo.
- Sito segnalato come virus/ingannevole: possibile infezione nascosta → registrare il sito in Search Console, controllare avvisi di sicurezza, rimuovere file dannosi, richiedere revisione.
- **Sito di staging** con accesso solo da IP sviluppatori: Search Console non può verificarlo così. Per rimuoverlo dalla Ricerca: strumento Rimozioni; consentire a Googlebot (lista IP pubblicata) l'accesso al file di verifica; lo staging deve restituire **404 o 410**.
- Dati mancanti in Search Console: accade se il sito perde la verifica a lungo; non recuperabili.

**Contenuti, titoli, link**
- URL, title e H1 **non devono essere uguali**; sovrapposizione naturale di parole, usare termini descrittivi.
- Anchor "qui" da evitare (interni ed esterni): usare parole correlate all'argomento.
- Link a Wikipedia "per giustificare": aggiungere link solo se danno valore.
- Frequenza di pubblicazione: **nessuna frequenza ottimale**, dipende da come interagire con gli utenti.
- Contenuti aggiornati: Google **non garantisce la frequenza di reindicizzazione**; una pagina di qualità che non cambia può restare pertinente; non perdere tempo a rendere "dinamiche" pagine statiche.
- Infografiche: Google può teoricamente leggere testo nelle immagini, **ma non per i risultati web** → il testo da far riconoscere va inserito come testo (alt, didascalie, testo nella pagina).
- Un post in spagnolo su un sito in inglese: nessun effetto negativo.
- Numero di link in uscita (interni/esterni) e PageRank: "stai pensando troppo"; i link interni aiutano a scoprire pagine e capire il sito, limitarli può essere più dannoso.
- Domini con due trattini: nessun effetto negativo.
- Author come Organization nel markup Article: ammesso (Person o Organization, quello più adatto).
- Schema validator vs Test risultati avanzati: il primo controlla la sintassi schema.org generale; il **Test dei risultati avanzati controlla solo i tipi supportati da Google (circa 25–30 funzionalità)**.
- Sitelink: **nessuna garanzia**; mostrati solo se pertinenti e utili. Aiuta: struttura logica del sito, titoli, intestazioni e testo dei link descrittivi.
- Nome del sito ancora del vecchio brand → seguire la sezione di troubleshooting "nome del sito"; nome **coerente in tutto il sito** non solo nel markup; aggiornare tutte le versioni (http/https).

**Spam e sanzioni**
- SpamBrain (sistema AI antispam); segnalazioni di spam degli utenti **non portano ad azioni manuali immediate**, servono a migliorare i sistemi.
- Contenuti copiati da concorrenti senza valore originale → modulo spam; DMCA tramite strumento "Segnalazioni di contenuti su Google"; Community per altre soluzioni.
- Azioni manuali (revisori umani) vs azioni algoritmiche (SpamBrain ecc.): **solo le azioni manuali vengono comunicate in Search Console**.
- Penalità algoritmica per contenuti scarni: rimuovere contenuti di bassa qualità/spam; la rivalutazione può richiedere **diversi mesi**.
- Deindicizzazione dopo spam update → esaminare e migliorare significativamente i contenuti; leggere norme spam.
- SafeSearch non riguarda solo contenuti per adulti; richiesta di revisione disponibile nella documentazione.

**Altro**
- Sistema contenuti utili: domande di autovalutazione (contenuti pensati per le persone? molta automazione? diventato improvvisamente esperto di un argomento?).
- Creare un sito: Google non lo fa; per chi non è tecnico usare piattaforme di hosting (Blogger, Wix, Squarespace, Shopify…) che funzionano bene con la Ricerca.
- Fluttuazioni di traffico periodiche (stagionalità, interesse per argomenti) sono normali.

## Office Hours — gennaio 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/january?hl=it

**Miti / segnali**
- Meta tag `keywords` → **non serve**, Google non lo usa (post del 2009).
- Densità delle parole chiave → **Google non sa quale sia la densità ottimale**; i sistemi capiscono l'argomento anche senza le parole chiave, **ma è meglio essere espliciti**: dire chiaramente cosa offri (es. "dipingiamo case" invece di frasi vaghe), usare la **terminologia che usano gli utenti**; non serve menzionare tutte le varianti (mito).
- Verifica in Search Console o cambio del metodo di verifica → **nessun effetto** su indicizzazione o ranking.
- Dati EXIF delle immagini → **Google non li usa** per nulla; gli unici metadati immagine usati sono **IPTC**.
- Profondità dell'URL di un'immagine → irrilevante; usare struttura logica e **nomi file descrittivi** (es. `/photos/Molly-Havanese-dog.png`). `srcset`/dimensioni: aggiungerli se sensato, consigliati per immagini adattabili (responsive).

**Brand e nomi**
- Brand con nome simile a un refuso di una parola comune (es. "Quoality" → "quality"): gli algoritmi inizialmente correggono la query; man mano che il brand cresce imparano il nome, **ma ci vuole tempo**.
- Account social/attività con lo stesso nome di concorrenti → risultati "sostanzialmente legittimi"; per essere trovati per nome serve un **identificatore chiaro**, non un termine usato da molti.

**Sitemap, date**
- `lastmod` → deve riflettere quando il contenuto è cambiato abbastanza da meritare una nuova scansione (commenti inclusi se parte fondamentale). Usare le date in modo **coerente** e includerle nei dati strutturati **con fuso orario**.
- Sitemap News + Sitemap generale: possibile un'unica Sitemap con estensioni news, ma le estensioni vanno tolte dagli URL più vecchi di **30 giorni** → spesso più semplice tenerle separate; URL in entrambe non crea problemi.

**Snippet e titoli**
- Meta description non usata → **nessuna garanzia** che Google la usi; snippet generati automaticamente e variabili per query; più probabile che venga usata se descrive la pagina con precisione.
- Snippet uguale al title → verificare HTML valido e rendering con Controllo URL; poi forum.
- Feedback su elementi SERP non pertinenti (es. ricerche correlate) → link "feedback" in fondo alla SERP; riguarda la funzionalità, non il singolo sito.

**Indicizzazione / problemi tecnici**
- Sito non visibile: caso reale in cui la home restituiva **404 solo agli user agent Googlebot** (configurazione server errata) → verificabile con il selettore di user agent di Chrome DevTools; dopo la correzione, visibile **entro circa una settimana**.
- Sottodominio di staging indicizzato: farlo restituire **404/410**; se ancora visibile, richiesta di rimozione in Search Console (dopo aver verificato lo staging).
- Strumento Rimozioni approvato ma URL ancora visibile → di solito URL errato (verificare dove porta il risultato effettivo); lo strumento agisce in genere **entro poche ore**.
- Vecchi URL spostati con 301 ancora visibili (anche dopo 10 anni) → normale, non serve rimozione/reindicizzazione; li mostriamo se cercati esplicitamente.
- Sito regionale deindicizzato mentre vecchi sottodomini 404 restano → Google non ha ancora riscansionato i vecchi URL; se il sito non è indicizzato, possibili problemi tecnici e di **qualità**.
- Mobile-first: fornire **gli stessi contenuti** su mobile e desktop, accessibili a utenti e Google.
- Siti m-dot: l'URL **desktop è sempre canonico**; sul desktop `rel=canonical` a se stesso + `rel=alternate` verso m-dot; sulla m-dot solo `rel=canonical` verso il desktop.
- Contenuti tradotti non visibili: servono **URL distinti per ogni lingua** (anche solo parametro `?hl=de`); i sistemi che cambiano lingua sullo stesso URL **non funzionano** per i motori; **link interni** tra le versioni linguistiche (idealmente ognuna verso tutte); `hreflang` utile ma facoltativo.
- Cluster hreflang: formati dai link hreflang validati (link di ritorno); link non validi esclusi; URL `noindex` non idonei al cluster.

**Spostamento sito / rebranding**
- Cambio nome azienda e URL: fondamentale **redirect dai vecchi ai nuovi URL**; verificare il nuovo dominio in Search Console, controllare report Sicurezza; poi richiesta di **spostamento del sito** (Change of Address). Lo spostamento funziona anche senza la richiesta se i redirect sono corretti.

**Link**
- Backlink spam da siti porno → non prioritario, Google sa ignorarli; disavow solo se dubbi seri o **azione manuale**.
- Disavow per recuperare da penalità algoritmica: utile solo se hai **creato attivamente** link spam e non puoi rimuoverli; non ripristina il ranking precedente, nessun trucco magico.
- Link nel footer "Realizzato da …" (designer/CMS) → non preoccuparsi; se controllabili, aggiungere `nofollow`; anchor sensato, non pieno di keyword (es. "realizzato dal miglior esperto SEO della Florida").
- Dominio usato con "spam score" → fare due diligence prima dell'acquisto; ripulire non è compito di Google.

**Dati strutturati**
- Sito di servizi (prezzo su preventivo) con errori nei dati Product → usare i dati strutturati **LocalBusiness** (consentono una **fascia di prezzo** per i servizi).

## Office Hours — marzo 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/march?hl=it

- Aggiornare risultati dopo il passaggio a WordPress: niente di speciale, Google rielabora automaticamente; i vecchi URL dovrebbero **redirigere** ai nuovi, altrimenti **404/410**; rimozioni urgenti con Search Console. Suggerimento di John per un'attività locale: migliorare title e description inserendo **località, città, nomi degli stati** nei titoli.
- WebP: Google riconosce il formato dall'**header `Content-Type`** della risposta HTTP, non dall'estensione.
- "Google non ha potuto stabilire il video in evidenza": può essere comportamento previsto; "in evidenza" = video visibile al primo caricamento (above the fold) e di dimensioni adeguate.
- Stessa lingua in due mercati: **nessuna sanzione per contenuti duplicati**; una pagina può essere scelta come canonica; con `hreflang` Google può comunque scambiare gli URL nei risultati; Search Console riporta principalmente URL canonici. Utile un **banner** per indirizzare gli utenti di altri paesi.
- .com vs .nl per sito olandese: restare su **.nl** se possibile (lo spostamento comporta rischi; il ccTLD è un segnale diretto di localizzazione nei Paesi Bassi, il .com no).
- Spostare molte pagine su altro sito: **isolare la modifica** (no redesign o cambio architettura contemporanei), redirect, **elenco URL prima/dopo** per monitorare.
- Statistiche di scansione in Search Console includono **AdsBot** (stessa infrastruttura e limiti di frequenza).
- Aggiornamento URL indicizzato: dopo scansione e rielaborazione; tempi dipendono dalla popolarità.
- hreflang in più Sitemap o in una sola: entrambi gli approcci vanno bene.
- Reindicizzazione massiccia di un intero sito: **non esiste un pulsante**; usare Sitemap (pagine cambiate), feed Merchant Center per prodotti/prezzi, Controllo URL per singole pagine.
- URL considerato duplicato: perché lo era o è quasi duplicato; vedere documentazione canonicalizzazione.
- `<strong>` vs `<b>`: entrambi indicano importanza; `<strong>` per cose più importanti/urgenti/serie.
- Sito non indicizzato con robots.txt corretto: caso di contenuti scarsi (descrizioni con link di download affiliati, testo copiato) → **non è un problema tecnico ma di contenuti**; consiglio di ricominciare con un argomento di cui si ha conoscenza.
- Cambiamenti drastici nei risultati con l'operatore `site:` **non** sono segnale di un core update.
- Testo nelle immagini: Google può estrarlo con **OCR**, ma è meglio fornirlo nel **testo `alt`** (utile anche per screen reader e contesto).
- Velocità "solo above the fold": Google usa i **Core Web Vitals** per l'esperienza sulle pagine; **LCP** = tempo per visualizzare l'immagine o blocco di testo più grande nell'area visibile.
- Sitemap non recuperata: spesso legata alla qualità del feed/pagine inviate; una Sitemap non deve per forza "comparire".
- hreflang `de` vs `de-de`: dipende dagli obiettivi di targeting per paese.
- **Sito non ancora lanciato protetto da password (401)**: pratica **comune e consigliata** per gli staging; Google riprova periodicamente; quando accessibile, recupera e indicizza. Errori di scansione occasionali per contenuti rimossi sono normali.
- Sitelink verso app store: provengono in genere dal **Knowledge Graph**, se l'app è associata al sito (link diretti/app links, sito indicato negli store).
- Dati strutturati annidati: consentiti e utili a capire l'argomento principale (es. Recipe con Review annidata). Carosello supportato solo per Corsi, Film, Ricette, Ristoranti (a marzo 2023).
- Assenza della mappa locale per alcune query: le funzionalità SERP variano per query, posizione dell'utente, qualità dei dati; non preoccuparsene.
- **Soft 404**: si verifica quando la pagina sembra un errore (risorse mancanti, messaggio di errore, es. "Nessuna offerta trovata" perché un widget non si è caricato). Verificare con Controllo URL. Se davvero non c'è contenuto, la pagina non dovrebbe essere indicizzata; a volte il soft 404 è corretto e si può ignorare.
- Due siti per servizi diversi: decisione di business; due siti = costi di manutenzione maggiori; può avere senso per localizzazione.
- Errore Sitemap "Non è consentito utilizzare questo URL…": verificare entrambi i siti in Search Console; l'URL deve essere a un livello pari o inferiore al percorso della Sitemap.
- Immagine diversa nei risultati: Google mostra quella più pertinente alla query, non necessariamente la principale.
- **Scorrimento infinito senza paginazione**: Google usa "espansione dell'area visibile" (come smartphone molto lungo), poco efficiente e può non vedere i contenuti infiniti → **includere link di paginazione** oltre allo scroll infinito.

## Office Hours — aprile 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/april?hl=it

- Sottodirectory `/eu` con più hreflang (`en-fr`, `en-de`…): possibile; hreflang è per pagina e ammette più annotazioni; oppure `en` generico. Consigliato banner dinamico per utenti di paese "sbagliato".
- Solo 1–2 pagine indicizzate su ~200 della Sitemap → **Google non indicizza ogni URL**; verificare accessibilità con Controllo URL; Google tende a indicizzare URL di **alta qualità** (vedi contenuti utili).
- Recensioni di terze parti per risultati avanzati prodotto: possibile; le recensioni devono essere **visibili nella pagina** e riguardare **un singolo prodotto**, non una categoria.
- Sito indicizzato ma invisibile: se c'è un'azione manuale si vede in Search Console; altrimenti è ranking algoritmico → documentazione qualità dei contenuti.
- URI di thesaurus (es. NALT) come strategia SEO: **non supportati** dalla Ricerca Google.
- "robots.txt non raggiungibile" nel Controllo URL: problema di impostazioni del sito (firewall, CDN che blocca IP, hosting); **non serve inviare il robots.txt per l'indicizzazione**.
- Eliminare vecchie landing: redirect alla home solo se ha senso per l'utente; altrimenti **404** è spesso la soluzione migliore (redirect a contenuto non correlato confonde).
- Eliminare vecchio sito dopo il passaggio a nuovo dominio → **redirect** (non eliminarlo: ha accumulato segnali utili); sostituzione dei vecchi URL in qualche settimana, talvolta mesi.
- 1,2 milioni di URL non validi generati da un annuncio con percorso relativo: Google sa gestire questi incidenti; possibile **aumento temporaneo della scansione** e del carico server per alcune settimane; **molti URL non indicizzati non sono un problema** né per indicizzazione né per valutazioni di qualità.
- 410 a Googlebot e 200 agli utenti = **cloaking dei codici di stato, pessima idea**; usare `noindex`.
- **308 = 301** per Google (spostamento permanente, segnale chiaro di canonicalizzazione).
- Velocità di indicizzazione: dipende da quante sezioni Google può raggiungere e dalla **qualità** dei contenuti.
- Sito mai individuato da Google: incoraggiare altri a **menzionare il sito**, aggiungerlo a **Search Console**, inviare una **Sitemap**, inviare singole pagine (es. home) per l'indicizzazione.
- "Wifi" vs "Wi-Fi": stesso significato per Google, risultati leggermente diversi per corrispondenza precisa.
- `reviewCount` = 0 / `ratingValue` mancante su prodotti senza recensioni: **non è un problema**; semplicemente nessuna stella mostrata.
- Sparito per una keyword: raro perdere il ranking per una sola keyword; controllare da altre località; rivedere azioni recenti (struttura link interni, layout, link acquisiti, disavow).
- Strumento "Rimuovi contenuti obsoleti": per pagine esistenti da cui è stato tolto qualcosa (es. nome, telefono); rifiuta se il testo non è più indicizzato.
- Tempo per comparire dopo migrazione dominio: da giorni a molti mesi; più veloce per siti di qualità.
- Dati strutturati Recipe: compilare le **proprietà obbligatorie** (es. `name`, `image`); facoltative vuote ammesse ma limitano i miglioramenti mostrati (es. senza `cookTime`); recensioni vuote normali.
- Spam nella descrizione del sito non proveniente dal sito → probabile **compromissione** (vedi web.dev siti compromessi).

## Office Hours — maggio 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/may?hl=it

**JavaScript / rendering (Martin Splitt)**
- HTML visualizzato in Controllo URL vs Test risultati avanzati: generati allo stesso modo con la stessa infrastruttura. "Visualizza pagina sottoposta a scansione" usa la **pipeline di indicizzazione**; i **test live** (SC o Rich Results Test) **ignorano la cache** → possibili **timeout** che cambiano l'HTML renderizzato.
- Googlebot esegue il rendering di ogni pagina? → Non di tutte (es. un 404 non viene renderizzato), ma **ogni pagina che risulta corretta in scansione viene sottoposta a rendering**.
- **SSR per i bot e CSR per gli utenti = "rendering dinamico"**: ammesso, aggiunge complessità; **non consigliato per nuovi progetti**; se già funziona non serve cambiarlo.
- Evitare che Googlebot chiami un'API esterna costosa durante il rendering: si può bloccare l'API con robots.txt, **ma se i contenuti della pagina (CSR) dipendono da quell'API, Googlebot deve accedervi** per vederli; per API di terze parti non bloccabili, caricarle condizionalmente ed evitarle quando la richiesta è di Googlebot.
- Backend (WordPress, CMS custom, linguaggio) → **non influisce** sul ranking in genere; contano prestazioni e comportamento (server molto lento può impattare).

**Indicizzazione / meta**
- Pagine di raccolta escluse per `noindex`: caso con **due meta robots distinti**, il secondo con `noindex` (probabile plugin/piattaforma). Come verificare: "Visualizza sorgente" e cercare "robots" e "googlebot"; per casi avanzati emulazione mobile di Chrome + Ispeziona elemento sul **DOM caricato**, oppure Controllo URL.
- 16.000 pagine indicizzate in 6+ mesi (5–15 a settimana): velocità dipende soprattutto dalla **qualità**, poi dalla **popolarità** del sito; promuovere il sito (es. social) per farlo conoscere.
- **Link nei `<select><option value="URL">`** → **non considerati link** (al massimo l'URL può essere riconosciuto e scansionato a parte). Per essere un link deve essere un **link normale** (`<a href>`), vedi linee guida sui link.
- robots.txt non raggiungibile → problema del sito/server (firewall, configurazione server, hosting); Google non può farci nulla.
- hreflang in Sitemap e `lastmod`/`priority`: hreflang va confermato in tutti gli URL dell'insieme; `lastmod` è per singolo URL ed è **solo un indicatore approssimativo**; più scansioni **non significano ranking migliore**.
- Link di affiliazione: bloccarli con **robots.txt Disallow** è sensato (controllo e risparmio di crawl budget).
- Redirect 302 → 301: da fare con hoster/registrar; **Google tratta i redirect temporanei di lunga durata come permanenti**.

**Link**
- Link in uscita da domini penalizzati: Google **non si fida dei link da siti noti come spam**.
- **Directory e social bookmarking** per SEO off-page → **non sprecare tempo**.
- Link spam da siti russi / backlink spam che puntano al sito → **ignorarli**, i sistemi li riconoscono; disavow solo se infastidiscono davvero.

**Contenuti / URL / immagini**
- Parole negli URL (es. "wont" vs "will-not") → **effetto minimo**; essere coerenti; non cambiare gli URL di un sito per un "trucco SEO".
- URL immagine con molti livelli → nessun problema.
- **Nomi file descrittivi per le immagini**: aiutano un po'; con pochi file usarli, con milioni valutare costo/beneficio.
- Molto testo boilerplate → in genere nessun effetto in Ricerca, ma valutare la percezione degli utenti.
- Calo graduale di traffico dopo un redesign: se il redesign cambia URL va trattato come **spostamento del sito con redirect** (altrimenti calo immediato); un calo lento indica invece cambiamenti di comportamento/aspettative di utenti e web.
- Markup Product senza offer/review/aggregateRating: non dannoso; ciò che non è analizzabile viene ignorato, si perdono solo funzionalità.
- Post multilingua: indifferente se parametro (`?hl=ja`) o codice lingua nel percorso; **un URL univoco per versione linguistica**.

**Search Console / brand**
- Query "errate" nel report Rendimento: i dati sono reali (ciò che è stato mostrato); restringere per paese, tipo di ricerca, periodo; a volte non riproducibili.
- **Nome del sito**: possibile a livello di dominio, **non per i sottodomini** (a maggio 2023).
- **Favicon** vecchia (es. Webflow) ancora visibile: seguire la documentazione favicon; rimuovere/non linkare la vecchia, **redirect dal vecchio file al nuovo**, tutto coerente; servono tempo (~un mese).
- Cambio dominio senza perdere ranking: se lo spostamento è eseguito correttamente non c'è perdita di traffico duratura.

## Office Hours — giugno 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/june?hl=it

- Contenuti in **syndication** che compaiono al posto dell'originale in Discover: `rel=canonical` è solo un suggerimento; se non vuoi che le versioni in syndication appaiano in Ricerca, il partner deve usare **meta robots `noindex`**.
- Due domini con TLD diversi sullo stesso paese e stesse keyword → può confondere gli utenti e potrebbe essere **manipolazione** (controllare norme spam).
- Avvisi Lighthouse su librerie JS vulnerabili → **nessun effetto sul ranking**, ma vanno risolti per sicurezza.
- Bloccare la scansione di una **sezione di pagina**: **non è possibile**; alternative: attributo **`data-nosnippet`** (esclude dallo snippet) oppure iframe/JS con origine bloccata da robots.txt (di solito **sconsigliato**: problemi difficili da diagnosticare). Contenuti riutilizzati/duplicati in pagina: non serve bloccarli.
- Sitemap inviata ma URL non in Ricerca: le Sitemap indicano dove sono i contenuti, **non garantiscono scansione né indicizzazione** (dipendono da qualità e popolarità).
- schema.org valido ma errori in Search Console (es. enum `returnFees`): Google, come fornitore, ha **requisiti più specifici** di schema.org per le sue funzionalità.
- **HSTS** → nessun effetto sul ranking; la canonicalizzazione non si basa su queste intestazioni; utile agli utenti.
- Sitemap: Google confronta versioni; non rielabora una Sitemap invariata; ogni modifica (URL o `lastmod`) la fa rianalizzare. **Rimuovere un URL dalla Sitemap non lo elimina dall'indice** né ne prioritizza la scansione.
- **Sitemap XML vs HTML**: XML per i crawler, HTML per gli utenti; errore "Sembra che la tua Sitemap sia una pagina HTML" = inviato formato non supportato. Per John una Sitemap HTML è spesso segnale di **navigazione troppo confusa** → meglio risolvere la navigazione.
- Dati strutturati con errori di analisi → **ignorati**.
- **Numeri negli URL** → nessun problema (anche lettere non latine, Unicode). Evitare **identificatori temporanei** che cambiano a ogni visita (es. ID di sessione).
- URL "bloccato"? → non bloccato, semplicemente non mostrato; leggere la Guida introduttiva SEO (citati anche Moz e Aleyda Solis come risorse).
- **"Index bloat" non esiste** in Google; nessun limite artificiale al numero di pagine indicizzate per sito; le pagine devono essere utili.
- Bloccare Googlebot per sempre: robots.txt `User-agent: Googlebot` + `Disallow: /`; per bloccare la rete, firewall con gli intervalli IP di Googlebot.
- **Nessuna certificazione SEO ufficiale di Google** (esistono certificazioni per prodotti come Google Ads).
- Più menu di navigazione → molto improbabile un impatto negativo.
- Estensioni `.html` / `.aspx` → nessun problema; nasconderle non cambia nulla.
- **Gruppi host** (due risultati dello stesso dominio, il secondo rientrato): non influenzabili con markup; indicano più pagine che si posizionano bene per la query; eventualmente accorparle.
- Googlebot falso: chiunque può usare lo user agent "Googlebot"; verificare con gli **intervalli IP pubblicati** / metodo di verifica.
- Disavow per indirizzi IP → **non esiste**.
- Meta `NOODP` → obsoleto (DMOZ), nessun effetto, innocuo.
- Video come "contenuto principale" per mostrare la miniatura: non deve essere il primissimo elemento, ma deve essere **in primo piano** senza che l'utente debba cercarlo (riferimento: pagine video di YouTube/Vimeo).

## Office Hours — luglio 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/july?hl=it

- Sito non visibile: restituiva **HTTP 403 a Googlebot smartphone** → nulla da indicizzare; verificare con Controllo URL.
- Milioni di 404 o milioni di 301 (prodotti venduti → scheda principale)? → **entrambi innocui**, scegliere ciò che è meglio per il caso.
- URL/canonical per categorie e-commerce, CSR vs SSR: canonicalizzazione usa `rel=canonical`, link da altre posizioni del web e altri segnali; URL più breve ideale ma non indispensabile; **nessuna differenza di canonicalizzazione tra siti CSR e non-CSR**.
- Prezzi solo in $ nei risultati: il sito cambiava valuta in base alla provenienza dell'utente; **Google esegue la scansione principalmente dagli Stati Uniti** → vede i prezzi USA. Per più valute servono **URL separati per valuta**, mostrati a tutti gli utenti di quell'URL. (Principio generale: non adattare il contenuto per geolocalizzazione IP se si vuole che Google veda le varianti.)
- Dominio acquistato che dà 404 → serve un hosting (WordPress.com, Wix, Blogger…) associato al dominio, poi contenuti di qualità.
- Canonical scelto su altro dominio nazionale nonostante hreflang: hreflang dice "stesse pagine in lingue/regioni diverse", la canonicalizzazione sceglie l'URL principale; gli altri URL **possono comunque comparire** per lingua/regione. Pagine molto simili (DE/AT) possono non funzionare al 100% → far scegliere la regione all'utente.
- Link da siti cinesi → nessun problema avere link da siti in altre lingue; spam casuale si può ignorare; il disavow non li rimuove dal web.
- Contenuto unico su prodotto venduto da molti: aggiungere **punto di vista, recensione autentica, test, informazioni utili** oltre la scheda del produttore.
- Search Console per sottodominio/sottodirectory: verificabili separatamente (senza verifica extra se il dominio è già verificato); dati in qualche giorno.
- Molti 404 in Search Console danneggiano le pagine 200? → **No**.
- Discover: funzionalità organica basata su interessi/abitudini; contenuti indicizzati e conformi alle linee guida possono comparire; traffico difficile da prevedere e fluttuante.
- Sito affiliato: nessuno schema speciale per affiliazione; affiliati sono validi se i contenuti sono utili; etichettare i link di affiliazione con **`rel="sponsored"`** (o `nofollow`).
- robots.txt "efficace": non esiste un modello universale; dipende dalle esigenze (es. bloccare risultati di ricerca interni, consentire un JS specifico).
- **Quality rater**: valutano siti ma **non modificano il ranking in tempo reale**; le valutazioni servono a valutare modifiche agli algoritmi, nessun impatto diretto sul ranking.
- 1 milione di "pagine con reindirizzamento" un anno dopo la migrazione → normale; Google conserva i vecchi URL a lungo; non c'è nulla da fare finché i redirect funzionano.
- Dominio non visibile → verificarlo in Search Console e seguirne i suggerimenti.
- Dominio usato solo per email: senza sito non c'è nulla da mostrare; robots.txt blocca la scansione **ma non impedisce necessariamente la comparsa** degli URL; per non comparire usare **`noindex` (meta robots o header HTTP `X-Robots-Tag`)**.
- Scansione desktop in Search Console: probabilmente il sito è già mobile-first (verificare in Statistiche di scansione il tipo di Googlebot prevalente); i siti scansionati solo da desktop sono quelli che non funzionano su mobile.
- Stringa di query nell'URL hreflang: non dovrebbe creare grossi problemi; essere **coerenti** per evitare sorprese di canonicalizzazione.
- Moduli (form): nessun ruolo speciale nel ranking; design irrilevante; la **posizione** nel sito può indicare importanza; **overlay/interstitial** possono impattare l'esperienza utente.
- Ridurre 8M → 2M pagine: impossibile dirlo; ciò che conta di più è la **qualità complessiva** del sito, non il numero di pagine indicizzabili.
- **.ai trattato come gTLD** da giugno 2023 (utilizzabile per presenza globale).
- Eliminare errori 404 in Search Console: non esiste funzione; si aggiornano da soli; **i 404 non sono un problema**.
- Il team Ricerca **non fa riunioni private** di consulenza.
- Pubblicazione accademica (Google Scholar) non trovata: stessi contenuti su più URL, indicizzata un'altra versione; verificare cercando un pezzo di testo; la pagina deve essere **accessibile senza login**.
- Redirect di PDF, video, immagini: **stesse regole** delle pagine web.
- hreflang solo in una sezione del sito: va bene, è a livello di pagina; prima verificare che ci sia davvero un problema di pagine sbagliate; hreflang implementabile via Sitemap.

## Office Hours — agosto 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/august?hl=it

- **Sitemap XML: max 50.000 URL**; vale anche per i file indice Sitemap (che contengono solo altre Sitemap).
- **Attributi ARIA** → **nessun vantaggio SEO intrinseco**; usarli correttamente per l'accessibilità.
- Redirect `dominio/en` → `dominio`: nessun vantaggio SEO, ma utile coerenza; la versione senza codice lingua può essere `x-default` in hreflang; canonical e link interni coerenti fanno scegliere quella versione.
- **Frammenti `#` negli URL** → in genere **ignorati** dalla Ricerca (Google guarda l'intera pagina); usare i frammenti per mostrare contenuti diversi è **pratica rara e sconsigliata**. (Rilevante per SPA con routing hash.)
- Sito non tra i primi 200 nonostante "buona SEO" (Sitemap, indicizzazione, contenuti aggiornati, backlink, on-page): i dettagli tecnici non bastano (analogia: copertina bella e cucina pulita non fanno un best seller/ristorante pieno).
- Sanzioni su un sito acquistato: verificare in Search Console lo stato delle **azioni manuali** (quelle scadute/risolte non sono mostrate); gli algoritmi possono reagire a problemi di qualità **senza azione manuale**.
- Dati strutturati `Product` per immobili: non supportati (Merchant Center); non è abuso ma **non ha effetto**; usare dati strutturati con effetto visibile.
- hreflang per contenuti simili ma non traduzioni dirette (varianti per paese) → **sì**.
- Testo bianco su sfondo colorato → ok, con **buon contrasto**.
- Tag `<article>` → nessun effetto specifico in Ricerca; usare HTML corretto per accessibilità/semantica.
- **Link relativi e assoluti misti** → nessuna differenza (i motori leggono i link come un browser).
- Dati strutturati in sito francese: testi devono corrispondere a ciò che l'utente vede; ma i **campi enumerati** (es. `dayOfWeek`) vanno in **inglese** come da schema.org.
- Verificare se un IP è Googlebot: **DNS inverso** → hostname → DNS diretto per confermare l'IP; oppure WHOIS. Gli scraper che fingono di essere Googlebot si possono bloccare.
- `prefetch`, `prerender`, `dns-prefetch` come segnale UX? → conta solo se migliorano davvero le **metriche utente reali dei Core Web Vitals**; conta l'esperienza effettiva, non il tentativo.
- Pagina cache 404 → la cache **non è importante** per l'indicizzazione; usare Search Console (Controllo URL).
- Contenuti di giochi/scommesse sul proprio dominio: **Google non inventa contenuti**, li fornisce il server → probabile **compromissione**. Consiglio: **Google Alert** su `site:` del dominio + parole chiave tipiche di spam (farmaci, gioco d'azzardo).

## Office Hours — settembre 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/september?hl=it

- www vs non-www: entrambe compatibili con la Ricerca; il caso reale era corretto (redirect non-www → www + `rel=canonical` coerente; Chrome nasconde il "www" nella barra).
- Dati filtrati più numerosi del totale in Search Console: dovuto all'uso di **filtri di Bloom** (velocità a scapito della precisione).
- **Google Sites**: indicizzabile ma "non ideale per la SEO"; URL pubblici diversi da quelli visti da loggati, monitoraggio complesso; meglio usare il **proprio dominio** (facilita migrazioni e verifica Dominio in SC).
- **Pulsanti che caricano link al clic** → **"In generale, Googlebot non fa clic sui pulsanti"**.
- Guest post per ottenere backlink (anche con contenuto di valore) → **violazione delle norme spam**; i link devono essere qualificati con `rel="nofollow"` o `rel="sponsored"`; la pubblicità è ammessa con link qualificati.
- Testo nelle pagine categoria e-commerce: non usare testi brevi di bassa qualità **generati automaticamente e ripetuti**; aggiungere solo informazioni realmente utili per le persone.
- **HTML semantico**: un uso corretto (es. intestazioni) può aiutare i motori a capire contenuti e contesto; non è una "ricetta segreta"; intestazioni come riepilogo chiaro aiutano se il testo è poco chiaro. Un `<hr>` usato solo per design non crea problemi. Risposta: "dipende".
- 404 da URL estratti per errore da JSON/JS → ignorarli o header HTTP `noindex`.
- File indice Sitemap con Sitemap su altri domini: "forse", sconsigliato; ammesso se Sitemap inviata via robots.txt o tutti i domini verificati in Search Console; aggiungere commento XML per ricordarlo.
- Quando Google usa la meta description: di solito quando **la pagina ha pochi contenuti** o quando la description è **più pertinente alla query** del contenuto della pagina.
- Bloccare parti di pagina (es. mega-menu duplicati): **non necessario per header, menu, sidebar, footer**; per altri contenuti: iframe o JS con origine bloccata da robots.txt; per lo snippet `data-nosnippet`. Evitare complessità non necessarie (rischio errori).
- **Scorrimento infinito**: va bene se **ogni parte/pagina virtuale è accessibile e trovabile tramite un URL univoco**.
- Link visibili su mobile ma nascosti su desktop dietro toggle JS: con mobile-first conta la **versione mobile** per indicizzazione e scoperta dei link; se il mobile è completo, va bene.
- PDF pubblici su Google Drive: indicizzabili come qualsiasi URL (da secondi a mai).
- **Scrolljacking**: non vietato, nessun effetto diretto, ma possibili **problemi di rendering**: Google rende la pagina come un dispositivo mobile molto alto; se il contenuto appare solo con eventi di scroll, i sistemi possono ritenerlo non visibile.
- URL bloccato da robots.txt ma indicizzato: Google può indicizzare **solo l'URL senza contenuti** (raro, se molto linkato). Per evitarlo: **consentire la scansione e usare `noindex`** (header HTTP o meta tag).
- Contenuti AI di bassa qualità pubblicati senza revisione: rimuoverli o correggerli; domanda chiave: il sito apporta **valore aggiunto unico** o ricicla contenuti già presenti sul web? Servono strategia e processi.
- Picco di URL indicizzati: difficile dire il motivo.
- Favicon multi-dimensione in .ico: meglio specificare dimensioni e file singolarmente; Google supporta più dimensioni di favicon in HTML.
- CMS diversi per parti di sito → **nessuna valutazione diversa**.
- Home non indicizzata (al suo posto un PDF): la home aveva **meta robots `noindex`** → rimuoverlo.
- Pagina prodotto che compare prima della home per il nome del sito: dipende dall'**intento percepito** dell'utente, che può cambiare; soddisfare gli utenti su ogni punto d'ingresso.
- **INP**: avviso in Search Console; documentazione su web.dev; (a settembre 2023) INP **non ancora parte dei Core Web Vitals**; migliorarlo aiuta l'UX ma John non si aspetta cambi visibili di ranking.
- Hack "parole chiave giapponesi" (30.000 URL): spesso **cloaked** verso Google → verificare rimozione completa; concentrarsi sulle pagine più visibili (rimozione o reindicizzazione manuale), il resto si risolve da sé.
- Pagine deindicizzate dopo richiesta di indicizzazione: i sistemi **non sono convinti del valore** del sito; Google non indica quasi mai tutte le pagine; **non continuare a reinviarle**, migliorare la qualità complessiva e il valore unico.

## Office Hours — dicembre 2023
Fonte: https://developers.google.com/search/help/office-hours/2023/december?hl=it

**JavaScript / SPA (Martin Splitt)**
- **`<meta name="prerender-status-code" content="404">`** → **ignorato** da Googlebot. In una SPA con CSR, per evitare soft 404: aggiungere **`<meta name="robots" content="noindex">`** oppure **redirect a una pagina per cui il server risponde 404**.
- Sito che restituisce **HTTP 200 per pagine 404** → di solito **soft 404, non cloaking**; nessun problema SEO grave ma non auspicabile. Soluzioni: impostare lo stato 404 nell'app; configurare il server/router per rispondere 404 e usare **redirect JavaScript** verso una pagina che dà davvero 404; oppure aggiungere **dinamicamente via JS un meta robots `noindex`**.
- Impedire a Googlebot di cercare link in `<script>` JSON/JS: bloccare gli URL (file JS) in **robots.txt** — Googlebot non richiede il file, non vede gli URL.
- Aumento di 404 da **percorsi API trovati nel JSON** → non preoccuparsi; si può bloccare via robots.txt; i 404 non finiscono nell'indice.
- `noindex` + blocco robots.txt insieme: se blocchi la scansione, **Googlebot non vede il `noindex`** → consentire la scansione degli URL da non indicizzare.
- Accessibilità: non direttamente fattore di ranking, ma alcune funzioni (es. **attributo `alt`**) sono informazioni utili per Googlebot; importante per raggiungere più persone.

**Indicizzazione / struttura**
- **iframe**: Google prova ad associare il contenuto dell'iframe alla pagina principale, senza garanzia. Per indicizzare la pagina incorporata solo come parte della principale: **`noindex` + `indexifembedded`** sulla pagina figlia. Per impedirlo del tutto: header **`X-Frame-Options`**.
- Struttura gerarchica vs piatta: per **siti grandi** meglio gerarchica (sezioni trattabili diversamente, es. `/notizie/` scansionata più spesso di `/archivi/`).
- Sito indicizzato senza www: cercare con `site:dominio.com`.
- Slug non inglese (es. caratteri cinesi): poca differenza; usare la **lingua dei contenuti negli URL** a volte aiuta Ricerca e utenti.
- Doppia barra `//` nell'URL: tecnicamente valida (RFC 3986), ma poco usabile e può confondere alcuni crawler.
- **Redesign**: mappare tutte le modifiche in un documento annotando le implicazioni SEO; se cambiano gli URL → linee guida sulle migrazioni; contenuti/UI influiscono sulla SEO; farsi aiutare da esperti; correggere una migrazione fallita costa più che prepararla bene.
- "Video esterno all'area visibile" → spostare il video in alto; dal dicembre 2023 la modalità Video mostra solo pagine in cui **il video è il contenuto principale**.
- URL immagini spostati su altro server: aggiornare gli elementi `<img>` ai nuovi URL e **redirect dai vecchi URL immagine**; le immagini sono scansionate **meno spesso** → tempi più lunghi.
- Molti 404 → parte integrante del web; attenzione solo se una **pagina importante** diventa 404.
- Aggiornare contenuti (es. per studenti): rendere chiaro l'aggiornamento in evidenza sul sito; se si sposta contenuto, redirect dalla vecchia alla nuova pagina.
- Sitemap che rimanda a se stessa: inutile; per non farla indicizzare header **`X-Robots-Tag: noindex`**.
- Rimuovere contenuti dall'indice: eliminarli e attendere la riscansione; oppure `noindex`; oppure strumento Rimozioni.
- **Codifica caratteri**: caratteri speciali mostrati male → specificare `<meta charset>` nell'HTML.
- Punti in URL (SKU) → tecnicamente accettati.

**Attività locale / brand**
- **Attività di servizi non visibile** (es. sgombero neve, nome "Whiteout"): nome molto comune difficile da trovare; il **Profilo dell'attività su Google** compare cercando il nome; il sito (in realtà una pagina Facebook) non era referenziato dalle altre schede → **far sì che tutti i profili dell'attività rimandino al sito web**.
- Attività chiusa ancora visibile: rimozione del sito in Search Console; **segnare come chiuso** il Profilo dell'attività.
- PDF in SERP: non si può reindirizzare l'utente dopo il download; inserire un **link al sito in cima al PDF**.

**Link / spam**
- Link a pagamento: violazione invariata da tempo (norme spam, sezione link di spam).
- Segnalazioni di backlink a pagamento: usate per migliorare gli algoritmi, **nessuna azione individuale**.

**Search Console / altro**
- Impressioni in calo nonostante nuovi prodotti: non basta aggiungere pagine; servono **valore nuovo e unico** e un sito complessivamente di qualità; nessun segreto semplice.
- Posizione SC diversa da quella osservata: dati reali ma Ricerca dinamica; usare i filtri (es. paese) per riprodurre.
- GA4 vs Search Console: raccolgono dati in modo molto diverso; esaminarli separatamente.
- Blog aziendali in Google News: nessuna regola specifica contro (chiedere nella community editori); verificare presenza in News nei report Rendimento.
- "Gestire la SEO direttamente con Google gratis?" → **No**.
- "SEO perfetta?" → **non esiste**; Internet, motori e comportamenti cambiano continuamente (tecnica e qualità).

## Office Hours — aprile 2024
Fonte: https://developers.google.com/search/help/office-hours/2024/april?hl=it

- Ranking peggiorato perché si possiedono **due siti**? → **Improbabile**; avere più siti non è un problema. Effetto indiretto: con molti siti è difficile renderli tutti davvero ottimi, e questo può pesare.
- **Trattini vs trattini bassi** negli URL: keyword negli URL contribuiscono **minimamente** al ranking; i **trattini sono migliori** perché separano chiaramente le parole.
- Paginazione con `noindex, follow`: l'indicizzazione non è garantita; Google può seguire i link prima di eliminare la pagina dall'indice oppure non usare nulla della pagina — esito **non definito** e variabile nel tempo. Se le pagine di dettaglio sono linkate **solo** da pagine instabili come queste, la loro scoperta non è garantita.
- Continuare a contare impressioni/clic del vecchio dominio dopo il trasloco → decisione tua, nessun effetto SEO.
- `#color` vs `?color` per varianti condivisibili: i frammenti per cambiare contenuto possono essere un modo per gestire i facet; in alternativa bloccare la scansione di URL con certi parametri (doc e-commerce).
- **Rimuovere il sito dalla Ricerca**: robots.txt o **meta robots `noindex`**; per certezza usare `noindex` (con robots.txt il sito può essere comunque trovato **cercandolo per nome**). Urgenze: strumento Rimozioni (proprietà verificata; rimozione solo **temporanea**). CMS come Wix/WordPress rendono facile il `noindex`.
- Link con **frammento di testo** (`#:~:text=`): tutto dopo `#` è ignorato dalla Ricerca → è un **link normale**, nessun effetto speciale su PageRank.
- **503** per 10–15 minuti 4 volte a settimana durante i rilasci: un 503 **prolungato** riduce la frequenza di scansione; brevi finestre occasionali **non sono un problema**.
- Cambio URL pagina Facebook: ideale un redirect; senza redirect i motori impiegano più tempo; altrimenti rimuovere la vecchia pagina.
- Sito sparito dopo migrazione da WordPress a soluzione self-hosted → probabile **blocco dei motori** nel nuovo sito; partire dai dati di Search Console.
- Cambio hosting: se fatto bene, risolvibile e con downtime minimo → **nessun effetto negativo** sul ranking.
- URL di ricerca in cinese creati da bot nell'indice → probabile compromissione ("Japanese Keyword Hack").
- Blocco IP (es. App Engine) e 403 sulle Sitemap → inserire in **allowlist gli intervalli IP dei crawler Google** pubblicati.
- **Link alla copia cache rimosso** dalla Ricerca (aprile 2024); snippet aggiornati nel tempo; urgenze → strumento Rimozioni.
- **Indexing API**: limitata a **offerte di lavoro e video in streaming (livestream)**; per altri verticali potrebbe smettere di funzionare.
- Titoli nelle immagini come testo HTML (H1): la maggior parte dei metodi funziona; **evitare il testo dentro il file immagine** (difficile da riconoscere per motori e alcuni utenti).
- Menu di navigazione nascosto con gli stessi link del menu desktop (link duplicati nel DOM) → **nessuna sanzione**.
- Più valori hreflang per la stessa pagina (es. tedesco per DE e AT) → ammesso.
- **HTTP → HTTPS**: serve una **nuova proprietà** Search Console, oppure verificare a livello di **Dominio** (copre entrambe).
- 404 "falsi" da fonti esterne → non possono essere ragionevolmente collegati a cali di ranking; normali; se molti utenti reali arrivano da quegli URL, mostrare contenuti pertinenti.
- Account che verifica Search Console: per Google irrilevante chi verifica; organizzativamente sconsigliato dipendere da account personali di dipendenti.
- **Sitemap non obbligatoria**; il nome del file è libero (es. `johnmu_loves_cheese.xml`).
- URL mobile separati → rende tutto più difficile (SEO, analytics, manutenzione, test) → passare al **responsive design** quando possibile.

## Office Hours — giugno 2024
Fonte: https://developers.google.com/search/help/office-hours/2024/june?hl=it

- **Traduzioni con AI**: nessun markup speciale per segnalarle; valutare se rispettano gli standard di qualità del sito; se no, `noindex`. Una buona localizzazione è più di una traduzione di parole.
- Search Console include i risultati delle ricerche `site:` → **sì**.
- **PageSpeed Insights** varia: usa **test di laboratorio** (simulazioni) con varianza; concentrarsi sui **dati reali (field)**. I Core Web Vitals sono usati ma "ci sono molti altri fattori"; non inseguire variazioni minime; usarli per validità approssimativa, obiettivi facili, monitoraggio di cambi imprevisti.
- Dominio appena acquistato non visibile → verificarlo in Search Console, esaminare i dati; un precedente proprietario in genere non è un problema; pubblicare contenuti utili e attendere.
- **Bozze generate con AI + revisione editoriale**: non è un problema usare strumenti; ciò che conta è la **qualità complessiva**; non è automaticamente "alta qualità". Consultare linee guida sui contenuti AI e domande sui contenuti utili; utile il parere di terzi indipendenti.
- **Traduzione automatica** per altre regioni: se di bassa qualità, forse influisce negativamente → revisione da **madrelingua**; nessun problema se se ne blocca la scansione.
- Molti link di affiliazione: non rendono la pagina automaticamente scadente né utile; la pagina deve essere utile di per sé.
- Correggere tutti i backlink rotti → correggere quelli **utili agli utenti**; impossibile correggerli tutti su siti enormi.
- **Next.js** (e framework JS in generale): la maggior parte delle piattaforme funziona bene per la SEO se configurata bene; con molto JavaScript consultare le **best practice JavaScript SEO**; **configurare la SEO prima del lancio** di un nuovo sito: ottimizzarla dopo è sempre molto più difficile.
- Canonical da pagine corsi part-time a tempo pieno (93% uguali) → per Google indifferente.
- Sottodominio dismesso che riceve molte richieste di scansione: se utenti reali vi accedono → redirect alle nuove pagine appropriate e aggiornare i link sorgente; se solo crawler → si può spegnere; rimuovendo il **record DNS** il server non vede più richieste.
- Sabotaggio con link dannosi (negative SEO) → **ignorarli**; facoltativo disavow o segnalazione spam.
- Migrazione a Shopify + core update con -60% traffico: concentrarsi sulla **migrazione** (sotto il proprio controllo): analizzare in Search Console URL e query principali prima del cambio, confrontare le vecchie pagine con **Internet Archive**; controllare Google Immagini e Merchant Center; non serve annullare la migrazione.
- Title e H1 devono corrispondere? → **No**, fare ciò che ha senso per l'utente.
- Contenuti localizzati → **non sono contenuti duplicati**, nessuna penalità.
- Tool di terze parti che interrogano Google per verificare l'indicizzazione (A/B test): le query `site:` sono **a bassa affidabilità** (dipendono dal data center) → usare **Search Console e la sua API**.
- Posizione 1 con CTR 0,8%: metriche non adatte a valutare l'utilità; guardare le SERP reali, il contesto della pagina dei risultati e chiedere pareri esterni.
- HTML non valido / errori in console: dipende; un paragrafo rotto è irrilevante, un **`<head>` non funzionante può essere un problema** (vedi documentazione metadati validi).
- Linkare tutte le varianti prodotto solo per Googlebot e non per gli utenti = **cloaking** (violazione); alternativa: inviare le varianti via **Merchant Center**.
- "Pagine che riguardano principalmente singoli video" = **una pagina dedicata per ogni video**, con il video come scopo principale (richiesto per Momenti chiave, badge Dal vivo, ecc.).
- Articoli ripubblicati su **LinkedIn Pulse** che superano l'originale: i risultati non indicano chi Google ritiene la fonte originale; **la syndication scambia visibilità sulla piattaforma con il rischio che la piattaforma si posizioni meglio del tuo sito** → decisione di business.

## Office Hours — luglio 2024
Fonte: https://developers.google.com/search/help/office-hours/2024/july?hl=it

- Migrazione incrementale di CMS con hreflang/dati strutturati mancanti su parte delle pagine: ciò che non è presente non viene considerato; hreflang richiede reciprocità; transizione non ideale ma **nessun problema a lungo termine**.
- **GoogleOther**: crawler generico per team di prodotto (es. ricerca e sviluppo interni); bloccarlo può avere effetti su vari prodotti Google **ma non sulla Ricerca** (che usa Googlebot).
- Prodotti spariti dai rich result dopo un problema di Sitemap → chiedere aiuto a esperti (hosting, consulente, forum).
- **.kr vs .com per utenti coreani**: i domini locali tendono ad avere un **piccolo vantaggio** (contenuti locali promossi); **la corrispondenza della lingua del sito con la query conta probabilmente di più** del dominio.
- Espansione da 10.000 a 100.000 prodotti → il sito è di fatto nuovo; è logico che i motori lo rivalutino.
- Vecchie pagine del sito precedente ancora visibili → normale; la Ricerca riflette le intenzioni degli utenti che usano ancora i vecchi nomi.
- Errori nel report Indicizzazione pagine: **non è necessario risolverli tutti**; molti sono previsti o normali (i motori non indicizzano tutto).
- Dashboard di stato: dati disponibili via **feed RSS** (`status.search.google.com/en/feed.atom`) e **JSON della cronologia** (`status.search.google.com/incidents.json`).
- Rich result prodotto: richiedono pagina indicizzata + dati strutturati validi + decisione dei sistemi che valga la pena mostrarli; non forzabili. Alternativa: feed Merchant Center.
- Richieste di indicizzazione illimitate in Search Console → **No**.
- Brand confuso con una parola comune → si risolve col tempo (anche **molti mesi**) man mano che i sistemi vedono che gli utenti cercano davvero il sito; **nessuna scorciatoia**.
- Tag HTML per far ignorare parti di testo a Google → **non esiste**; trucco: inserire il testo via JavaScript e bloccare quel JS in robots.txt.
- Recipe per ricette non commestibili (deodorante, detersivo) → **No**, uso improprio contrario alle linee guida sui dati strutturati.
- Google può trasferire il ranking al nuovo dominio? → No, lo fai **tu** seguendo le linee guida sulla migrazione.
- Verificare il lavoro di un'agenzia SEO: riunioni periodiche, report di avanzamento, capire a grandi linee il lavoro; componente di fiducia; vedi pagina "Avvalersi di un esperto SEO".
- `noindex`: si applica a singole pagine/risorse; per l'HTML meta robots `noindex` nell'`<head>`.
- Dati strutturati varianti prodotto senza campi obbligatori (es. senza prezzi) → probabilmente ignorati perché incompleti; per milioni di varianti usare il markup sulle varianti comunemente offerte.
- **Feed RSS** referenziati sul sito possono essere usati per **scoprire nuovi URL**, come le Sitemap.
- **Favicon/logo** aggiornato non visibile: le favicon vengono aggiornate raramente; aggiornare **tutti** i file pertinenti (a volte più favicon marcate) e attendere.
- **Ordine delle intestazioni**: la Guida introduttiva SEO (aggiornata nel 2024) dice che l'ordine semantico è ottimo per gli screen reader ma **per la Ricerca Google non importa** se non in ordine. Che un tool non Google lo segnali non lo rende rilevante per Google.
- Blocco di scansione/indicizzazione di una pagina e i suoi link: se una parte importante del sito è raggiungibile **solo** da una pagina bloccata, sarà molto più difficile da scoprire; linkare pagine indicizzabili e pertinenti.
- Organizzazione Sitemap: libera; limite **50.000 URL per file**; se generate automaticamente usare il massimo.

## Office Hours — agosto 2024
Fonte: https://developers.google.com/search/help/office-hours/2024/august?hl=it

- Pagine in swahili non indicizzate vs inglese: lingue trattate in modo simile; servono **link interni** alle pagine localizzate e **crosslinking tra versioni linguistiche**, oltre a hreflang.
- Molti `nofollow` interni o molte pagine `noindex` → **non sono un segnale di bassa qualità**. Per contenuti generati dagli utenti usare **`rel=ugc`** invece di `nofollow`.
- Molti 404 senza redirect: **i 404 non influiscono sul ranking del resto del sito**. Redirect solo verso un **sostituto equivalente** (es. nuova tazza al posto di quella fuori produzione); **non redirigere a pagine simili, categorie o home** ("in caso di dubbio, non reindirizzare"); creare una buona pagina 404.
- Velocità di risposta della CDN per le immagini non determina la presenza in Ricerca (contano molti motivi, es. immagine già indicizzata da altro dominio); immagini veloci giovano agli utenti.
- Dominio che scade senza accesso a Search Console: i dati SC **non sono legati all'utente** (chi verifica dopo li vede); meglio non far scadere il dominio; rimozione temporanea del sito via verifica Dominio; avvisare l'eventuale acquirente.
- Sottodomini per mercati con contenuti identici: **"se i contenuti sono uguali, sono uguali"**; hreflang per varianti (valuta/prezzi); sottodomini/sottocartelle regionali **non rendono i contenuti unici**.
- Valuta sbagliata nei rich result: spesso perché le pagine paese sono considerate **duplicate**; differenziarle o usare feed Merchant Center per i prezzi.
- Scraping aggressivo: contattare l'abuse dell'hoster (WHOIS); CDN con rilevamento bot (la maggior parte riconosce i bot dei motori legittimi).
- Scheda "Shopping" in Search Console su sito non e-commerce → nulla da fare, nessuno svantaggio.
- **Video YouTube + stesso testo sulla pagina** → **non è contenuto duplicato**; utile per chi preferisce il testo o ha limiti di banda/visivi.
- Prezzi corretti nei risultati organici → **feed Merchant Center**.
- **Recensioni aggregate da altri siti/servizi** nei dati strutturati → contro le linee guida ("Non aggregare recensioni o valutazioni provenienti da altri siti web") → **non idonei** ai rich result recensioni.
- Sottocartelle senza pagine: Google scopre URL **tramite link**, non prova varianti; anche se dessero 404 nessun problema.
- Pagine compromesse rimosse (404) ancora scansionate dopo un anno → normale, non danneggia; Googlebot desisterà.
- **Targeting geografico** non esiste più in Search Console; per il mercato USA da sede francese considerare un **gTLD (.com)** invece di .fr.
- **Audit SEO con elementi non documentati**: "rapporto testo/codice" **non conta** per Google; CSS/JS non minificati non hanno implicazioni SEO dirette (ma minificare è buona pratica per gli utenti).
- Problemi di indicizzazione dopo aggiornamento plugin WordPress: CMS, plugin e temi possono **bloccare la ricerca**; farsi aiutare da chi conosce quel sistema.
- **UTM** nei backlink: non tolgono valore, ma la pagina di destinazione deve **canonicalizzare all'URL senza UTM**.
- **Pagina di login** nei sitelink (SaaS): nessun controllo diretto sui sitelink; reindirizzare utenti non loggati alla pagina di login, renderla **indicizzabile** (niente `noindex`, non bloccata da robots.txt).
- Commenti senza risposta → nessun impatto; è solo testo.
- robots.txt mostrato come soft 404 in Search Console → **nessun problema** (non serve indicizzarlo).
- `X-Robots-Tag` "mancante" → **non è un problema**; header/meta robots servono solo per trattamenti diversi (es. escludere dall'indice). Senza, la pagina è indicizzabile normalmente.
- **Redirect basati su IP geografico** → problemi significativi: anche i crawler vengono reindirizzati e non vedono le altre versioni ("pagina con reindirizzamento"). Usare **banner** che propongono la versione locale.
- Traffico falso/spam inviato da malintenzionati → l'affidabilità non è binaria; **nessuno controlla la provenienza di traffico o link**, Google non lo considera per valutare l'affidabilità.
- Modificare title, intestazioni, meta description **può cambiare** ranking/snippet: comportamento previsto.
- Effetti dopo un anno di lavoro SEO: molte best practice hanno impatto minimo sul traffico quotidiano; la struttura chiara aiuta la comprensione ma non necessariamente cambia il traffico subito; serve esperienza per **prioritizzare pochi elementi critici** da una lunga checklist.
- Limite di proprietà in Search Console per account → **non aumentabile**.

---

# Implicazioni per la skill SEO

Sintesi operativa ricavata esclusivamente dalle pagine del gruppo F. Le date tra parentesi indicano la sessione Office Hours (OH) di riferimento; alcune affermazioni potrebbero essere superate da documentazione successiva (es. INP, cache, nomi sito).

## (a) Miti SEO da NON seguire secondo Google

1. **Meta keywords** — non usato da Google (OH gen 2023).
2. **Densità delle parole chiave** — non esiste una densità ottimale; non serve ripetere tutte le varianti. Serve invece essere **espliciti** su cosa si offre con la terminologia degli utenti (OH gen 2023).
3. **Title = H1 = URL** — non devono coincidere (OH dic 2022, giu 2024).
4. **Ordine gerarchico delle intestazioni come fattore di ranking** — per la Ricerca non importa l'ordine; conta per gli screen reader (OH lug 2024).
5. **Validazione W3C come fattore di ranking** — no, non direttamente (FAQ scansione). Solo `<head>` rotto può essere un problema (OH giu 2024).
6. **"Spam score", "rapporto testo/codice", CSS/JS non minificati** come fattori SEO — Google non usa punteggi di tool terzi; testo/codice irrilevante; minificazione = buona pratica UX, non SEO diretta (OH nov 2022, ago 2024).
7. **Sanzione per contenuti duplicati** — in genere i duplicati non violano le norme spam; contenuti localizzati non sono duplicati; video YouTube + trascrizione sulla pagina non è duplicato (FAQ, OH mar 2023, giu 2024, ago 2024).
8. **I 404 danneggiano il sito / vanno tutti rediretti** — i 404 sono normali e non influenzano il ranking del resto del sito; non redirigere a home/categorie/pagine simili; nessun limite al numero di 301 (OH nov 2022, dic 2022, lug 2023, dic 2023, ago 2024).
9. **Molti `noindex`/`nofollow` = segnale di bassa qualità** — no (OH nov 2022, ago 2024).
10. **"Index bloat" / rapporto indicizzate-non indicizzate** — concetto inesistente in Google; nessun rapporto magico; crawl budget irrilevante sotto ~1 milione di pagine (OH nov 2022, giu 2023).
11. **Lunghezza/numero di parole** — non incide su scansione né definisce "contenuti scarni" (OH nov 2022).
12. **Frequenza di pubblicazione ottimale** — non esiste (OH dic 2022).
13. **Directory, social bookmarking, schede locali per la SEO** — perdita di tempo per la SEO; usare le directory eventualmente per traffico non da Ricerca (OH nov 2022, mag 2023).
14. **Acquisto di backlink / guest post per link** — link spam; guest post per link = violazione se non qualificati `nofollow`/`sponsored` (FAQ posizione, OH nov 2022, set 2023, dic 2023).
15. **Disavow preventivo di link "strani"** — sconsigliato; disavow solo per link pagati/creati attivamente non rimovibili o azione manuale (OH nov 2022, gen 2023, mag 2023).
16. **Negative SEO via link o traffico falso** — Google ignora i link irrilevanti; nessuno controlla provenienza di link o traffico, non conta per l'affidabilità (FAQ posizione, OH giu 2024, ago 2024).
17. **Annunci Google Ads migliorano il ranking** — no (FAQ posizione).
18. **TLD (.com/.org/nuovi gTLD), trattini nel dominio, sottodomini vs sottocartelle** — nessun effetto/preferenza (FAQ); eccezione: ccTLD come segnale di localizzazione (.nl, .kr: piccolo vantaggio; la lingua conta di più) (OH mar 2023, lug 2024).
19. **Keyword negli URL importanti** — effetto minimo; non cambiare URL per "trucchi" (OH mag 2023, apr 2024).
20. **HTTP/3, HSTS, tag `<article>`, `<strong>`, ARIA, `prefetch`** come segnali di ranking — nessun effetto diretto; contano solo se migliorano metriche reali (CWV) o per accessibilità/semantica (OH nov 2022, giu 2023, ago 2023).
21. **EXIF delle immagini** — non usati; solo IPTC (OH gen 2023).
22. **Profondità URL immagini** — irrilevante (OH gen 2023, mag 2023).
23. **Verificare Search Console migliora il ranking** — no (OH gen 2023).
24. **Copia cache necessaria / indicatore di qualità** — no; il link cache è stato rimosso (OH nov 2022, ago 2023, apr 2024).
25. **Inviare la Sitemap garantisce l'indicizzazione** — no; serve solo alla scoperta (FAQ, OH giu 2023). Sitemap non obbligatoria, nome file libero (OH apr 2024).
26. **Più scansioni = ranking migliore** — no (OH mag 2023).
27. **Canonical autoreferenziale "magico"** — di per sé non fa nulla; utile contro varianti (UTM) (OH nov 2022).
28. **Eliminare pagine scarse rende il sito automaticamente migliore** — no (OH nov 2022, lug 2023).
29. **Certificazione SEO ufficiale Google / consulenze private / "trasferimento ranking" da parte di Google** — non esistono (OH giu 2023, lug 2023, dic 2023, lug 2024).
30. **SEO perfetta** — non esiste (OH dic 2023).
31. **Cambiamenti nei risultati `site:` = core update** — no; le query `site:` sono a bassa affidabilità (OH mar 2023, giu 2024).

## (b) Controlli verificabili in un audit

**Indicizzabilità e risposta HTTP**
- La home e le pagine chiave rispondono **200 anche a Googlebot smartphone** (testare con user agent Googlebot; casi reali di 404/403 solo a Googlebot) (OH gen 2023, lug 2023).
- Nessun `noindex` involontario: cercare nel sorgente "robots" e "googlebot", **anche meta robots duplicati** (es. plugin) e nel **DOM renderizzato**; controllare header `X-Robots-Tag` (OH mag 2023, set 2023).
- Assenza di `X-Robots-Tag`/meta robots **non è un errore** (OH ago 2024).
- URL da non indicizzare: **non** bloccati in robots.txt se si usa `noindex` (altrimenti il noindex non si vede); robots.txt da solo non impedisce la comparsa per nome (OH set 2023, dic 2023, apr 2024).
- robots.txt raggiungibile (firewall/CDN/hosting non bloccano gli IP Google) (OH apr 2023, mag 2023, apr 2024).
- Pagine inesistenti rispondono **404/410 reali**, non 200 (soft 404) (OH dic 2023).
- Nessun **cloaking dei codici di stato** (es. 410 a Googlebot e 200 agli utenti) né contenuti/link diversi per Googlebot (OH apr 2023, giu 2024).
- Nessun redirect basato su **IP geografico**; varianti per paese/valuta su **URL separati** (OH lug 2023, ago 2024).
- 503 solo per brevi finestre di manutenzione (OH apr 2024).
- Staging/preprod: protetto da password (401) o 404/410; non indicizzato (OH dic 2022, gen 2023, mar 2023).
- Dichiarazione `<meta charset>` presente (OH dic 2023).
- `<head>` HTML valido (OH giu 2024).

**Canonicalizzazione e redirect**
- Una sola versione host (www o non-www; http→https) con redirect 301/308 e canonical coerenti; tutti i segnali (canonical, redirect, Sitemap, link interni) puntano allo stesso URL (OH nov 2022, set 2023).
- Canonical che eliminano parametri UTM/tracking (OH nov 2022, ago 2024).
- Catene di redirect corte (pochi hop) (OH dic 2022).
- Redirect da vecchi URL al **nuovo URL equivalente**, non alla home; nessuna redirect massiva alla home (OH dic 2022, ago 2024).
- Vecchi domini/siti obsoleti reindirizzati o eliminati, non lasciati online in parallelo (OH dic 2022, apr 2023).
- Asset spostati (immagini, PDF, video): redirect anch'essi (OH lug 2023, dic 2023).
- Favicon: un solo set coerente, vecchi file rimossi/rediretti (OH mag 2023, set 2023, lug 2024).

**Link e scoperta**
- Navigazione con **`<a href>` reali**: niente link in `<select><option>`, niente link caricati da click su pulsanti, niente navigazione solo JS (OH dic 2022, mag 2023, set 2023).
- Paginazione con link reali oltre allo scroll infinito; ogni "pagina virtuale" con URL univoco (OH mar 2023, set 2023).
- Pagine importanti non raggiungibili **solo** da pagine `noindex`/bloccate (OH apr 2024, lug 2024).
- Versioni linguistiche: URL distinti, crosslink tra lingue, hreflang reciproci/coerenti (OH gen 2023, ago 2024).
- Anchor text descrittivi (no "qui"); anchor interni ripetuti sono normali (OH nov 2022, dic 2022).
- Link di affiliazione/sponsorizzati con `rel="sponsored"` (o `nofollow`); UGC con `rel="ugc"`; link footer "realizzato da" eventualmente `nofollow` senza keyword stuffing (OH gen 2023, lug 2023, ago 2024).
- Profili esterni (Business Profile, social) che **linkano al sito** (OH dic 2023).

**Contenuti e presentazione**
- Title e meta description unici, descrittivi; per attività locali includere città/località nei title (OH mar 2023). Meta description generate programmaticamente ammesse se uniche e specifiche (OH nov 2022).
- Testo importante come **testo HTML**, non dentro immagini; `alt` descrittivi; nomi file immagine descrittivi (OH dic 2022, mar 2023, apr 2024, mag 2023).
- Video: pagina dedicata per video, video in alto (above the fold) e contenuto principale (OH mar 2023, giu 2023, dic 2023, giu 2024).
- Contenuto mobile completo (mobile-first): stessi contenuti e link di desktop; preferire responsive (OH gen 2023, set 2023, apr 2024).
- Interstitial/overlay di form non intrusivi (OH lug 2023).
- Assenza di contenuti compromessi: `site:` + parole spam (farmaci, gioco), Google Alert; report Sicurezza in Search Console (OH ago 2023, set 2023, apr 2024).

**Dati strutturati**
- Validare con il **Test dei risultati avanzati** (solo tipi supportati da Google), non solo con il validator schema.org (OH dic 2022, giu 2023).
- Proprietà obbligatorie presenti; un solo valore per campo; un solo nodo WebSite in home; annidamento coerente; enum in inglese (`dayOfWeek`) (OH nov 2022, apr 2023, ago 2023).
- Nessun uso improprio (Product per servizi/immobili, Recipe per non commestibili, recensioni aggregate da altri siti) (OH gen 2023, ago 2023, lug 2024, ago 2024).
- Recensioni marcate solo se **visibili in pagina** e relative a un singolo elemento (OH apr 2023).
- Date coerenti in pagina e nei dati strutturati con **fuso orario** (OH gen 2023).

**Sitemap**
- ≤ 50.000 URL per file (anche indice); `lastmod` reale; Sitemap inviata in Search Console o via robots.txt; non serve includere pagine paginate (OH dic 2022, gen 2023, ago 2023, lug 2024).

**Search Console (da verificare con il proprietario)**
- Proprietà **Dominio** verificata (copre www/non-www, http/https, sottodomini) (FAQ, OH apr 2024).
- Report Azioni manuali, Sicurezza, Indicizzazione pagine, Statistiche di scansione (tipo Googlebot prevalente = smartphone), Rendimento (OH vari).
- Non serve azzerare errori 404 o errori "previsti" nel report di indicizzazione (OH lug 2023, lug 2024).

## (c) Note per SPA JavaScript / Angular

- **Googlebot non clicca sui pulsanti**: i link verso le rotte devono essere `<a href="/percorso">` reali nell'HTML renderizzato (in Angular: `routerLink` su elementi `<a>` produce `href`; evitare navigazione solo via `(click)` + `router.navigate`) (OH dic 2022, set 2023).
- **Frammenti `#` ignorati**: evitare il routing hash (`/#/pagina`); usare URL a percorso (in Angular `PathLocationStrategy`, default) (OH ago 2023, apr 2024).
- Ogni pagina che risponde correttamente viene **renderizzata**; i test live (Controllo URL, Rich Results Test) **non usano cache** → possibili timeout; verificare l'HTML renderizzato con Controllo URL (OH mag 2023).
- **SSR/prerendering** sono la strada consigliata per nuovi progetti; il **rendering dinamico** (SSR solo per bot) è ammesso ma **non consigliato** per nuovi progetti (OH mag 2023). Configurare la SEO **prima del lancio**: correggerla dopo è molto più difficile (OH giu 2024, Next.js — principio valido per qualsiasi framework).
- **Soft 404 nelle SPA**: `<meta name="prerender-status-code" content="404">` è **ignorato**. Soluzioni: stato 404 reale dal server (con SSR), redirect JS verso un URL che risponde 404, oppure inserire dinamicamente `<meta name="robots" content="noindex">` (OH dic 2023).
- Rotte "nessun risultato"/widget non caricato possono diventare soft 404 → verificare con Controllo URL che il contenuto venga renderizzato (OH mar 2023).
- Non bloccare in robots.txt le **API/JS da cui dipende il contenuto renderizzato** (CSR): Googlebot deve accedervi. API costose di terze parti: caricamento condizionale (OH mag 2023).
- 404 da URL di API trovati in JSON/bundle: innocui; eventualmente Disallow in robots.txt (OH set 2023, dic 2023).
- Contenuti visibili solo con eventi di scroll (scrolljacking, lazy-load legato allo scroll) rischiano di non essere visti: Google rende la pagina come un dispositivo mobile molto alto (OH mar 2023, set 2023).
- Nessuna differenza di canonicalizzazione tra CSR e non-CSR; servono comunque canonical coerenti (OH lug 2023).
- Title/meta/canonical/hreflang/dati strutturati devono essere presenti nell'HTML renderizzato per ogni rotta (inferenza dai principi "ciò che non è presente non viene considerato", OH lug 2024).
- Non adattare contenuti/prezzi per geolocalizzazione lato client: Googlebot scansiona soprattutto dagli USA (OH lug 2023).

## (d) Note per personal brand (portfolio sviluppatore) e professionista locale (orientatrice di carriera)

**Comuni**
- Sito nuovo: la causa più comune di mancata indicizzazione è che è **troppo recente**; azioni: Search Console + Sitemap + richiesta indicizzazione della home + far **menzionare** il sito altrove (FAQ, OH apr 2023).
- Velocità di indicizzazione dipende da **qualità** e **popolarità**: promuovere il sito (es. social) (OH dic 2022, mag 2023).
- **Nome/brand**: evitare nomi che somigliano a refusi di parole comuni o a entità famose; nomi comuni (es. "Whiteout") sono difficili da trovare; serve un **identificatore chiaro**; la correzione automatica della query si risolve solo in molti mesi (OH nov 2022, gen 2023, dic 2023, lug 2024).
- Nome del sito coerente in tutto il sito (non solo nel markup); favicon coerente (OH dic 2022, mag 2023).
- Essere **espliciti** su cosa si fa con le parole che usano gli utenti (es. "orientamento professionale", "sviluppatore Angular") (OH gen 2023).
- Ospitare sul **proprio dominio** (no frame/inoltro mascherato; Google Sites non ideale) (FAQ, OH set 2023).
- Più siti non sono penalizzati, ma meglio concentrarsi su uno ottimo (OH apr 2024).
- Contenuti AI o tradotti automaticamente: ammessi se revisionati e di qualità; altrimenti `noindex` (OH giu 2024, set 2023).

**Portfolio sviluppatore (target recruiter)**
- Articoli ripubblicati su **LinkedIn Pulse**/piattaforme: possono superare l'originale; è un compromesso visibilità/ranking; se si vuole che vinca il proprio sito, pubblicare prima sul sito e valutare la syndication (OH giu 2024); i partner possono usare `noindex` (OH giu 2023).
- Pagine progetto con screenshot: testo descrittivo come HTML, `alt` utili (OH dic 2022, mar 2023).
- Video demo: pagina dedicata con video in evidenza se si mira ai risultati video (OH giu 2024).
- Pubblicazioni/CV/PDF: indicizzabili; inserire **link al sito in cima al PDF** (OH dic 2023); pagine accessibili senza login (OH lug 2023).
- Un post in un'altra lingua non danneggia; per un sito bilingue: URL distinti per lingua + crosslink + hreflang (OH dic 2022, gen 2023).

**Professionista locale + online (orientatrice)**
- La presenza nella **mappa/risultati locali** passa dal **Profilo dell'attività su Google** (rivendicarlo, verificarlo, foto); "la ricerca locale è diversa" (FAQ aspetto, OH nov 2022, dic 2023).
- Collegare **tutti i profili** (Business Profile, social, directory) al sito web (OH dic 2023).
- Directory locali **non** migliorano la SEO; utili solo come traffico diretto (OH nov 2022).
- Dati strutturati per servizi con prezzo su preventivo: **LocalBusiness** con fascia di prezzo, non Product (OH gen 2023).
- Title con città/località (OH mar 2023); orari in dati strutturati con `dayOfWeek` in inglese (OH ago 2023).
- Nessun problema ad avere servizi diversi sullo stesso sito; due siti = decisione di business con costi di manutenzione (OH mar 2023).
- Attività chiusa/trasferita: segnare chiuso il profilo; rimuovere/redirigere il vecchio sito (OH dic 2023).
- Verificare il sito in Search Console per ricevere notifiche su azioni manuali, sicurezza, rimozioni legali (pagina notifiche piccole imprese).
- Recensioni: marcate solo se visibili in pagina; **non aggregare** recensioni di altri siti nei dati strutturati (OH apr 2023, ago 2024).

## (e) Cose che una skill NON può fare

- **Garantire o prevedere** scansione, indicizzazione, tempi o ranking (FAQ scansione; OH ripetutamente).
- Forzare l'aggiornamento dei risultati o una **reindicizzazione massiva** (non esiste un pulsante; richieste di indicizzazione limitate) (FAQ, OH mar 2023, lug 2024).
- Controllare **sitelink, snippet, meta description mostrata, immagine mostrata, gruppi host, funzionalità SERP** (OH dic 2022, gen 2023, mar 2023, giu 2023, ago 2024).
- Garantire rich result: dipendono da indicizzazione, validità e decisione dei sistemi (OH lug 2024).
- Vedere **azioni algoritmiche**: solo le azioni manuali sono comunicate in Search Console; recuperi algoritmici possono richiedere **mesi** (OH dic 2022, ago 2023).
- Accedere ai dati riservati di Search Console senza che il proprietario verifichi il sito/conceda accesso; Controllo URL e report sono riservati ai proprietari verificati (debug). Può però usare strumenti anonimi (Test risultati avanzati), eventualmente con tunnel tipo ngrok per pagine locali.
- Usare le query `site:` o tool terzi come misura affidabile di indicizzazione (OH giu 2024).
- Ottenere supporto diretto/personalizzato da Google, certificazioni, o far "trasferire" ranking (OH lug 2023, giu 2023, lug 2024).
- Rimuovere link esterni dal web (il disavow non li rimuove) (OH lug 2023).
- Influenzare Discover direttamente (OH nov 2022, lug 2023).
- Sostituire il giudizio sulla **qualità e unicità dei contenuti** e sull'intento degli utenti: la SEO tecnica è necessaria ma non sufficiente (OH ago 2023, dic 2023, ago 2024).
- Distinguere con certezza l'effetto di un core update da quello di una migrazione: la skill può solo indirizzare all'analisi prima/dopo (Search Console, Internet Archive) (OH giu 2024) e alla **dashboard dello stato** per incidenti noti.
