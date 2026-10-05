# seo-kit

Plugin per Claude Code che porta la SEO dentro il lavoro su un sito: dalla prima riga di codice al monitoraggio dopo il lancio. È agnostico rispetto al tipo di sito (personal brand, professionista, attività locale, blog, e-commerce, SaaS) e al framework (Angular, React/Next, Vue/Nuxt, Astro, WordPress, HTML statico).

Le regole vengono dalla documentazione ufficiale **Google Search Central** (letta integralmente a ottobre 2026) e, come fonte secondaria, da un anno di articoli di **Search Engine Journal**. Ciò che è superato o solo "hype" (es. `llms.txt` come leva per Google, schema FAQ per i risultati avanzati) è marcato e non viene consigliato.

## Skill

| Skill | Quando usarla | Produce |
|---|---|---|
| `seo-discovery` | prima di tutto, su un sito nuovo o esistente | `SEO.md`: tipo di sito, obiettivo, ricerche da presidiare e pagina che risponde, identità, accessi, baseline |
| `seo-build` | mentre si costruisce: basi del progetto, nuove pagine, deploy, migrazioni | controlli e codice; `check_build.py` verifica l'output della build |
| `seo-audit` | per sapere cosa sistemare e in che ordine | `seo-reports/AAAA-MM-GG-audit.md` con piano d'azione, testi pronti e appendice tecnica |
| `seo-content` | per scrivere o riscrivere pagine, servizi, articoli, title e description | testi pronti e brief |
| `seo-entity-local` | identità coerente (personal brand) e presenza locale (Business Profile, recensioni) | `seo-reports/AAAA-MM-GG-identita.md` con testi per ogni piattaforma e JSON-LD |
| `seo-monitor` | per capire com'è andata (export di Search Console) | `seo-reports/AAAA-MM-GG-monitor.md` |

Le skill condividono `SEO.md` nella radice del progetto del sito: è la memoria SEO del progetto (profilo, ricerche, decisioni, baseline, registro interventi).

## Installazione

Requisiti: [Claude Code](https://docs.claude.com/en/docs/claude-code) e Python 3 (gli script usano solo la libreria standard).

Dal terminale:

```
claude plugin marketplace add eliaraguso/claude-seo-kit
claude plugin install seo-kit@seo-kit-marketplace
```

Oppure da dentro una sessione di Claude Code:

```
/plugin marketplace add eliaraguso/claude-seo-kit
/plugin install seo-kit@seo-kit-marketplace
```

Per aggiornare alla versione più recente:

```
claude plugin marketplace update seo-kit-marketplace
```

## Uso

Apri Claude Code nella cartella del tuo sito e parti da `/seo-kit:seo-discovery`, poi usa le altre skill (`/seo-kit:seo-audit`, `/seo-kit:seo-build`, ecc.). Le skill si attivano anche da sole quando la richiesta è pertinente.

## Sviluppo

Per lavorare sul plugin, clona la repository e avvia Claude Code puntando alla cartella, così legge sempre i file aggiornati:

```
git clone https://github.com/eliaraguso/claude-seo-kit.git
claude --plugin-dir ./claude-seo-kit
```

Per pubblicare una nuova versione, alza `version` in `.claude-plugin/plugin.json` prima del commit.

## Struttura

```
.claude-plugin/        plugin.json e marketplace.json
skills/<skill>/        SKILL.md, script e modelli di ciascuna skill
knowledge/             base di conoscenza condivisa (un file per argomento, con tabelle di controlli a ID stabili)
sources/               appunti di ricerca (Google Search Central, Search Engine Journal); i testi integrali restano solo in locale
evals/                 casi di prova delle skill
```

Gli script usano solo la libreria standard di Python 3.

## Limiti

- Nessuna skill garantisce posizioni o tempi: rimuovono ostacoli e aumentano le probabilità.
- Search Console, Business Profile e analytics richiedono accessi che Claude non ha: le skill guidano l'utente a usarli o a esportarne i dati.
- La base di conoscenza è aggiornata al 2026-10-03: va rinfrescata periodicamente (le date sono in testa a ogni file).
