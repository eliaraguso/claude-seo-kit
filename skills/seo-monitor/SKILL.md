---
name: seo-monitor
description: Misura i risultati SEO di un sito nel tempo e produce un report periodico in linguaggio semplice - analizza gli export di Google Search Console (clic, impressioni, query col proprio nome e non, pagine, query nuove e sparite), li confronta con la baseline e con il periodo precedente, collega le variazioni agli interventi fatti, controlla la visibilità negli assistenti AI con domande fisse e suggerisce le prossime azioni. Usa questa skill quando l'utente chiede come sta andando il sito, se le modifiche hanno funzionato, perché il traffico è calato, vuole un report mensile, ha scaricato dati da Search Console o vuole impostare un controllo ricorrente.
---

# Monitoraggio SEO

La SEO dà risultati in settimane o mesi e con molto rumore: senza un punto di partenza registrato e un registro degli interventi è impossibile capire cosa ha funzionato. Questa skill trasforma i dati di Search Console (e, se ci sono, di analytics e Bing) in poche risposte chiare: com'è andata, perché probabilmente, cosa fare dopo.

## Base di conoscenza
In `${CLAUDE_PLUGIN_ROOT}/knowledge/` (se la variabile non è espansa: la cartella `knowledge/` due livelli sopra questa skill):
- `measurement.md` — report di Search Console, filtro query col brand, report AI generativa, GA4, Bing, misurazione della visibilità AI, tempi attesi, **diagnosi dei cali** (checklist passo passo): leggilo sempre;
- `ai-search.md` — come leggere la presenza negli assistenti AI;
- `myths-deprecated.md` — note sui dati (es. bug delle impressioni di Search Console fino ad aprile 2026, che falsa i confronti con quel periodo).

Leggi `SEO.md`: baseline (sezione 7), intenti, entità, storico audit e registro degli interventi.

## Procedura

### 1. Procurati i dati
Claude non accede a Search Console da solo (a meno che l'utente non abbia configurato un connettore). Chiedi all'utente:
1. **Search Console → Rendimento → Risultati di ricerca**, periodo (es. ultimi 28 giorni o ultimi 3 mesi), poi **Esporta → Scarica CSV**: uno .zip con query, pagine, paesi, dispositivi, date.
2. Per il confronto, lo stesso export del periodo precedente di pari durata (o "Confronta" nell'interfaccia e poi esporta).
3. Facoltativo: report **Pagine** (indicizzazione), **AI generativa** (solo impressioni), Bing Webmaster Tools **AI Performance**, eventi di conversione da analytics.

### 2. Analizza
```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/seo-monitor/scripts/analyze_gsc.py" export-attuale.zip \
  --previous export-precedente.zip --brand "nome|cognome|marchio" --check-urls
```
Con `--check-urls` lo script verifica lo stato attuale delle pagine presenti nei dati: pagine che oggi danno 404 o un redirect vanno spiegate (URL rinominati, varianti www/http) prima di interpretare i numeri. Lo script avvisa anche se i periodi hanno lunghezza diversa o se i volumi sono troppo piccoli per conclusioni solide.
La regex `--brand` separa le ricerche col nome della persona/attività dalle altre: per un sito piccolo sono due storie diverse (chi ti conosce già contro chi ti scopre). Lo script dà totali, query e pagine principali, query con molte impressioni e pochi clic, query nuove e sparite, crescite e cali. Le query anonimizzate da Google non compaiono nel file delle query: il totale affidabile è quello per data.

### 3. Interpreta, con prudenza
- **Volumi piccoli = rumore grande.** Con poche decine di clic, variazioni del 50% possono essere casuali: dillo, e guarda le tendenze su più mesi.
- **Collega agli interventi** del registro in `SEO.md` (data di ogni modifica) e agli eventi esterni: aggiornamenti core/spam di Google, stagionalità, problemi tecnici. Le date degli aggiornamenti di Google presenti nella base di conoscenza si fermano al suo aggiornamento: per i periodi successivi indicale come da verificare sulla Search Status Dashboard di Google. Se un calo coincide con un intervento, verifica prima che non abbia rotto qualcosa (indicizzazione, redirect, title).
- **Calo di traffico:** segui la checklist di diagnosi in `measurement.md` (tracking, problemi tecnici, azioni manuali, aggiornamenti di Google, brand contro non brand, pagine e query coinvolte) prima di proporre rimedi.
- **Molte impressioni e pochi clic:** title e description da rivedere (skill `seo-content`) o intento diverso da quello della pagina.
- **Query nuove pertinenti senza una pagina dedicata:** candidati per nuovi contenuti.

### 4. Visibilità negli assistenti AI
Mantieni in `SEO.md` (sezione "Monitoraggio") un **set fisso di domande** (es. "Chi è Nome Cognome?", "Orientatrice di carriera a Verona", "Chi può aiutarmi a fare un bilancio di competenze a Verona?"). Ogni 3 mesi l'utente le pone a ChatGPT, Gemini, Perplexity, Copilot e alla Modalità AI di Google, in conversazioni nuove, e annota per ciascuna: sito citato sì/no, informazioni corrette/obsolete/false/riferite ad altri. Leggi i risultati come tendenza, non come misura precisa. Claude non può interrogare quegli assistenti per conto dell'utente.

### 5. Report e aggiornamento
Scrivi `seo-reports/AAAA-MM-GG-monitor.md`:
1. **In sintesi** (3-5 righe, linguaggio semplice): com'è andata rispetto al periodo precedente e alla baseline, cosa probabilmente l'ha causato;
2. **Numeri chiave**: clic, impressioni, CTR, posizione; ricerche col nome e altre; pagine principali;
3. **Cosa è cambiato**: query nuove/sparite, crescite e cali rilevanti, collegati agli interventi;
4. **Assistenti AI** (se ci sono nuove rilevazioni);
5. **Prossime azioni** (al massimo 3-5), ciascuna con la skill del plugin che serve;
6. **Limiti dei dati**.

Aggiorna `SEO.md`: nuova riga nella baseline/storico e, se l'utente conferma interventi fatti, nel registro degli interventi.

## Controllo ricorrente
Se l'utente vuole un promemoria mensile, proponi un'attività pianificata (skill `schedule` se disponibile) che ogni mese ricordi di scaricare l'export e lanci questa analisi. Ricorda che i dati di Search Console arrivano con circa 2-3 giorni di ritardo e che i confronti sensati sono tra periodi di pari durata.
