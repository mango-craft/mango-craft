# Enhanced Celestials 2 al posto di Enhanced Celestials (18/10/2026)

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Richiesta dell'utente: sostituire Enhanced Celestials (EC1, nel pack dalla 0.1.1) con le tre mod di **Enhanced Celestials 2** (EC2): Core, Default Lunar Events, Shader Support. Il sorgente di EC2 **non è pubblico** (il repository dell'autore contiene solo l'editor sperimentale): i dati vengono dai .jar letti con il workflow **Esamina mod** (`../data/esami/`), dal sorgente pubblico di EC1 (ramo `1.21.X`) e dal testo dell'editor di EC2.

## In breve

- EC2 è il **seguito ufficiale** di EC1. L'ultima versione di EC1 (6.0.2.6, 7/8/2026) esiste quasi solo per aggiungere una **schermata che annuncia EC2**, mostrata **a ogni ingresso in un mondo** e senza opzione per spegnerla (verificato nel sorgente: `EC2AnnouncementTrigger`, chiamato a ogni login). Dopo il 6/8/2026 su EC1 non c'è più nessun commit.
- Le **lune sono le stesse** (sangue, raccolto, blu, super) con **gli stessi valori** di base. EC2 aggiunge qualche effetto alla luna di sangue (vedi sotto).
- Il **formato dei dati cambia** completamente: il nostro datapack delle lune va riscritto, ma con file più piccoli.
- **Shader Support** richiede Iris (shader), che il pack non ha per scelta: non serve.

## Le mod

| | EC1 (nel pack) | EC2 Core | EC2 Default Lunar Events | EC2 Shader Support |
|---|---|---|---|---|
| Versione per NeoForge 1.21.1 | 6.0.2.6 (7/8/2026) | 2.0.3.3 (7/9/2026) | 2.0.1.3 (3/9/2026) | 2.0.0.3 (3/9/2026) |
| Licenza | LGPL-3.0 | ARR | ARR | ARR |
| Download (Modrinth) | ~2,5 milioni | ~66 mila | ~63 mila | ~50 mila |
| Cosa fa | Tutto in una mod | Solo il motore: calendario delle lune, formato dei dati, comandi. Nessuna luna | Le 7 lune "classiche" | Colori della luna con gli shader (Iris) |
| Dipendenze obbligatorie | CorgiLib ≥ 5.0.0.9, Data Anchor ≥ 2.0.0.3 | CorgiLib ≥ 5.0.0.9, **Data Anchor ≥ 2.0.0.16** | Core, CorgiLib | Core, CorgiLib, **Sodium e Iris** |
| Incompatibile con | — | EC1 | EC1 | EC1 |

Nel pack: CorgiLib 5.0.0.9 (va bene), **Data Anchor 2.0.0.14** (troppo vecchia per EC2: andrebbe aggiornata alla 2.0.0.17, release del 19/9/2026). Data Anchor serve solo a Enhanced Celestials, nessun'altra mod la usa. Nessun'altra mod del pack dipende da Enhanced Celestials o ne usa i dati (verificato sull'inventario).

## Le lune: cosa cambia

| Luna | EC1 | EC2 |
|---|---|---|
| **Sangue** | Mostri ×2,25, comparsa forzata in superficie, niente letto | Uguale, **più**: mostri che compaiono entro 64 blocchi dal giocatore (più concentrati, dalla descrizione del campo) e **assedio di zombi ai villaggi** con probabilità 50% |
| **Super luna di sangue** (solo luna piena) | Mostri ×4,5 | Uguale, più: comparsa entro 32 blocchi, assedio ai villaggi 100% |
| **Raccolto** / super | Colture (`#c:crop`) ×2 / ×4 | Uguale (stessa etichetta), più il grano esplicito |
| **Blu** / super | Fortuna, esperienza ×2 / ×4, incantamenti e incudine meno cari, beacon più ampio | Uguale |
| **Super luna** | Slime ovunque | Uguale |
| Bottino in più nelle casse (con la Fortuna della luna blu) | 16 tabelle vanilla | Le stesse 16 |

Regole comuni del calendario (anno di 100 giorni, almeno 2 giorni tra due lune in EC1 e **3** in EC2, al massimo 98 giorni senza lune, niente lune con la pioggia).

## Il calendario: probabilità contro pesi

- **EC1** (codice pubblico): ogni notte le lune vengono provate in ordine casuale, ognuna con la sua **probabilità** (`chance`: 10% le normali, 5% le super) e le sue distanze minime. Una simulazione dello stesso algoritmo (rifatto in Python sul codice di `EnhancedCelestialsLunarForecastWorldData`, 2000 anni simulati) dà, ogni 100 giorni:
  - con i valori della mod: circa **5 lune di sangue**, 5 del raccolto, 5 blu, 0,3 di ogni super luna;
  - **con il nostro datapack** (luna di sangue al 5%): circa **3 lune di sangue**, cioè una ogni 30–35 notti.
- **EC2**: niente probabilità, ma un **peso** per luna e dimensione (10 le normali, 5 le super) più regole (notti minime, fasi lunari). Come i pesi diventano frequenza non si può leggere nel codice (chiuso). Si verifica in gioco con il comando delle previsioni lunari, che mostra le lune in arrivo (in EC1 è `/ec lunarForecast`; EC2 ha lo stesso comando, il nome esatto è da confermare in gioco).

## Il nostro datapack

Oggi (EC1) il datapack contiene **copie complete** di `blood_moon.json` e `super_blood_moon.json` (consentito dalla licenza LGPL), con due numeri cambiati.

Con EC2 ogni luna è divisa in file piccoli: l'evento, la sua **probabilità** (`event_probability`) e i suoi **effetti** (`event_modifier`, uno per effetto). Per ottenere lo stesso risultato bastano tre file scritti da noi, senza copiare quelli della mod (che è ARR):

| File (in `data/enhancedcelestials2defaultlunarevents/enhancedcelestials2core/lunar/`) | Cosa |
|---|---|
| `event_probability/blood_moon.json` | Peso più basso (da tarare con le previsioni in gioco, obiettivo circa 3 lune ogni 100 giorni) |
| `event_modifier/blood_moon_spawn_category_multiplier.json` | Mostri ×2 (invece di ×2,25) |
| `event_modifier/super_blood_moon_spawn_category_multiplier.json` | Mostri ×4 (invece di ×4,5) |

Da decidere: se tenere i due effetti nuovi della luna di sangue (mostri più vicini, assedio ai villaggi; con Guard Villagers i villaggi hanno le guardie). La cartella `enhancedcelestials/` di oggi andrebbe tolta. Come in EC1, i file li legge solo la mod: senza EC2 restano inerti. Le lune si ricaricano riaprendo il mondo (sono registri del datapack).

## Shader Support

Fa solo una cosa: con un **pacchetto di shader** attivo (Iris), mostra i colori della luna e del cielo. Richiede **Iris** e Sodium come dipendenze obbligatorie. Il pack non usa shader (scelta dell'utente, `docs/0001-progetto.md`) e non ha Iris: aggiungerla porterebbe una mod di rendering in più senza effetti visibili. Ha senso solo se un giorno si decide di usare gli shader.

## Rischi

- EC2 è giovane (prima versione il 4/8/2026, 2.0.x da agosto) e poco diffusa; il codice è chiuso, quindi i problemi si possono verificare solo in gioco.
- Formato nuovo: i datapack di EC1 non funzionano (l'editor dell'autore ha una funzione apposta per convertirli).
- L'editor sperimentale dell'autore (`/ec config`) **non** è per i modpack: non va nel pack.
- Cambiare mod azzera il calendario delle lune: nessun problema finché non c'è il mondo vero (1.0.0).

## Come provarla

1. Togliere EC1, aggiungere EC2 Core e Default Lunar Events, aggiornare Data Anchor (il controllo dei nomi verifica le versioni richieste).
2. Mondo di prova: il comando delle previsioni lunari (in EC1 `/ec lunarForecast`) per contare le lune di sangue in arrivo e tarare il peso.
3. Il comando che avvia una luna (in EC1 `/ec setLunarEvent`) e quello che elenca gli effetti attivi (EC2 ha un comando "dumpmodifiers"): devono comparire i nostri ×2 e ×4. I nomi esatti dei comandi di EC2 sono da confermare in gioco.
