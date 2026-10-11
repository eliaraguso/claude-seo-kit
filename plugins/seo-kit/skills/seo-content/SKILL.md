---
name: seo-content
description: Scrive e migliora i testi di un sito perché siano trovati su Google e citati dagli assistenti AI senza diventare generici - pagine servizio, home, pagina "chi sono", articoli del blog, case study, title, meta description e H1, piano editoriale. Parte da come le persone cercano davvero e dall'esperienza diretta dell'autore, rispetta le regole Google sui contenuti utili e sui contenuti generati con AI. Usa questa skill quando l'utente vuole scrivere o riscrivere una pagina o un articolo, migliorare i testi esistenti, decidere di cosa scrivere, preparare un piano di contenuti, o quando un audit ha trovato testi da sistemare.
---

# Contenuti per la ricerca

Google premia i contenuti scritti per le persone, che mostrano esperienza diretta e rispondono bene a una domanda precisa. I contenuti generici, riscritti da altre fonti o prodotti in serie (anche con l'AI) non aiutano e, in quantità, sono trattati come spam. Questa skill aiuta a scrivere testi che una persona del settore riconoscerebbe come utili, con le parole che il pubblico usa davvero.

## Base di conoscenza
In `${CLAUDE_PLUGIN_ROOT}/knowledge/` (se la variabile non è espansa: la cartella `knowledge/` due livelli sopra questa skill):
- `content-quality-spam.md` — contenuti utili, chi/come/perché, contenuti AI, norme antispam (doorway, abuso di contenuti su larga scala): leggilo sempre;
- `on-page-appearance.md` — title, snippet, heading, immagini, date;
- `ai-search.md` — cosa rende un contenuto citabile (e cosa è mito);
- `entity-personal-brand.md` — autore, credenziali, pagina chi sono;
- `local-seo.md` — pagine servizio e località senza doorway;
- `structured-data.md` — `Article`/`BlogPosting` con `author`.

Leggi anche `SEO.md` del progetto: intenti, pubblico, entità, ricerche da non inseguire.

## Procedura

### 1. Scegli l'intento e controlla cosa esiste
- Ogni testo risponde a **un intento** della tabella di `SEO.md` (o a uno nuovo che aggiungi lì). Se due pagine rispondono alla stessa domanda, meglio unirle che farle competere.
- Leggi la pagina attuale (se esiste) e le pagine collegate: non ripetere ciò che sta già altrove, collegalo.
- Nessuna pagina "servizio + città" clonata: una pagina località ha senso solo se c'è una presenza reale e contenuto diverso.

### 2. Raccogli il materiale che solo l'autore ha
È la parte che distingue un testo utile da uno generico, e non si inventa. Chiedi all'utente (raggruppando le domande) o ricava dai suoi materiali:
- esempi e casi reali (anonimi se serve), numeri propri, errori comuni dei clienti, cosa succede davvero in un incontro o in un progetto;
- opinioni motivate, cosa sconsiglia e perché, per chi il servizio **non** è adatto;
- credenziali vere e verificabili, metodo, prezzi o come si formano.
Se l'utente non ha tempo, scrivi una bozza segnando con `[DA COMPLETARE: ...]` i punti dove serve la sua esperienza invece di riempirli con frasi generiche.

### 3. Usa le parole del pubblico
```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/seo-discovery/scripts/suggest.py" "servizio città" "domanda tipica" --expand
```
I suggerimenti di ricerca mostrano come le persone formulano le domande (non quante sono). Usa le formulazioni pertinenti in title, H1, sottotitoli e testo, in modo naturale: niente elenchi di parole chiave, niente ripetizioni forzate. La densità delle parole chiave non è un fattore.

### 4. Scrivi
- **Apertura:** la risposta o la promessa principale nelle prime righe; chi legge deve capire subito se è nel posto giusto.
- **Struttura:** sottotitoli che dicono cosa contiene la sezione; paragrafi brevi; elenchi dove aiutano. Non esiste una lunghezza ideale: tanto quanto serve all'intento.
- **Chi/come/perché:** chi scrive è chiaro (autore con pagina profilo), come è stato prodotto il contenuto quando è rilevante, e lo scopo è aiutare chi legge.
- **Temi delicati** (salute, soldi, lavoro, scelte di vita): niente promesse di risultato, fonti per i dati, distinzione tra esperienza personale e regole generali.
- **Invito all'azione** coerente con la conversione di `SEO.md` (contatto, prenotazione, download), senza interstitial invasivi.
- **Link interni** verso le pagine collegate con anchor descrittivi, compresi gli articoli del blog pertinenti; indica anche quali pagine esistenti dovrebbero linkare la nuova.
- Scrivi nella lingua del sito, con ortografia e accenti corretti (in italiano: "è", "perché", "cos'è").

### 5. Prepara gli elementi per Google
- **Title**, **meta description** (una frase che invoglia, specifica per la pagina), **H1**. Google non fissa limiti, ma per evitare troncamenti punta a circa 50-60 caratteri per il title (compreso l'eventuale suffisso col nome del sito) e 120-160 per la description; se il progetto ha un suo controllo di lunghezza, rispetta quello. Conta i caratteri con uno strumento (es. `python -c "print(len('...'))"`), non a occhio.
- **Data** visibile ("Pubblicato il… · aggiornato il…") per articoli e case study; aggiorna la data solo per modifiche sostanziali.
- **Dati strutturati** `Article`/`BlogPosting` con `author` collegato alla pagina profilo (vedi `structured-data.md`); niente FAQ o HowTo per ottenere risultati avanzati (ritirati).
- **Immagini** reali e pertinenti, con `alt` descrittivo.

### 6. Controllo finale
Rileggi il testo con le domande di autovalutazione di `content-quality-spam.md`. In breve:
- contiene informazioni originali o un'esperienza che altrove non c'è?
- chi lo legge esce soddisfatto o deve cercare ancora?
- un esperto del settore lo considererebbe corretto?
- ci sono affermazioni non verificabili, credenziali vaghe, promesse?
- è stato scritto per le persone o per "piacere a Google"?

Se il testo è stato prodotto con l'AI, è l'autore a doverlo verificare e approvare: segnala all'utente i fatti da controllare.

### 7. Consegna
Consegna nel formato del progetto (file Markdown dei contenuti, componenti, CMS): individua dove stanno i testi nel repository e proponi la modifica lì. Per un piano editoriale usa `assets/brief-template.md` per ogni contenuto. Aggiorna la tabella degli intenti in `SEO.md` (pagina che risponde, stato).

## Piano editoriale
Se l'utente chiede "di cosa scrivere": parti dagli intenti senza pagina in `SEO.md`, dalle domande che i clienti fanno davvero, dai suggerimenti di ricerca e, se disponibili, dalle query di Search Console con molte impressioni e pochi clic. Proponi pochi contenuti solidi (es. 1-2 al mese) piuttosto che molti deboli: i contenuti in serie poco utili sono un rischio, la costanza conta solo se la qualità resta alta.
