# Bug report — Mango Craft 1.21.1

Tutti i problemi trovati nelle versioni del pack, anche minori: dai log dell'istanza di prova, dal controllo dei nomi (`data/inventario/controllo.md`) e dalle prove in gioco.

**Regole**
- Ogni problema nuovo riceve un codice (`B01`, `B02`…) che non si riusa mai, anche quando il problema è risolto.
- "Visto in" è la prima versione in cui è comparso. La voce del `CHANGELOG.md` di ogni versione elenca i codici dei suoi problemi noti.
- Quando un problema si risolve, la riga passa in "Risolti" con la versione che lo chiude.

**Stato**: 🔧 da correggere da noi · 🔍 da verificare in gioco · 👁️ della mod, non correggibile da noi (si tiene d'occhio) · ✅ risolto o aggirato
**Effetto**: alto = blocca o fa crashare · medio = una funzione non va · basso = estetico o solo nel log

_Ultimo aggiornamento: 18/10/2026 (versioni fino alla 0.3.0)._

---

## 🔧 Da correggere da noi

| Codice | Visto in | Dove | Problema | Effetto | Piano |
|---|---|---|---|---|---|
| B01 | 0.1.1 | Datapack, artefatti | 15 nomi di casse di When Dungeons Arise e Dungeons and Taverns presi da versioni vecchie non esistono più: in quelle casse gli artefatti non compaiono mai | medio | 0.6.0, con i nomi veri dell'inventario |
| B02 | 0.1.0 | Cataclysm + YUNG's Better Nether Fortresses | I Berserker infuocati sono legati alla fortezza vanilla, che YUNG's sostituisce: non compaiono mai | medio | 0.6.0 (`berserker_spawn.json` nel datapack) |
| B03 | 0.1.0 | Datapack, artefatti | Le casse di Mowzie's Mobs e Born in Chaos non hanno gli artefatti (nomi delle tabelle mai verificati) | basso | 0.6.0, nomi presi dall'inventario |

## 🔍 Da verificare in gioco

| Codice | Visto in | Dove | Problema | Effetto | Come verificare |
|---|---|---|---|---|---|
| B04 | 0.1.0 | Apotheosis + Truly Modular | All'avvio Apotheosis non riesce a leggere il "livello" (tier) di 20 armi e attrezzi modulari di Miapi | medio | Le armi Miapi ricevono affissi, gemme e riforgiatura? I nomi generati sono giusti? |
| B05 | 0.1.0 | Truly Modular | 48 errori nella creazione delle ricette del tavolo da forgiatura, un materiale di prova (`tm_armory:test`) non trovato, due attributi di danno nulli | medio | In EMI: ci sono le ricette di potenziamento delle parti modulari? |
| B06 | 0.3.0 | Animal Pen + My Nether's Delight | Le due mod modificano lo stesso punto del codice (probabilità di drop dell'equipaggiamento dei mob) | basso | Un mob con armatura uccisa lascia cadere l'equipaggiamento come al solito? |
| B07 | 0.1.0 | Accessories (dentro l'Aether) + Miapi/Hexalia | Bug noto di Accessories quando un'entità subisce danno; Forgified Fabric API dovrebbe evitarlo | alto se si presenta | Prova 3.2 di `context.md`: subire e infliggere danno con armi Miapi e oggetti di Hexalia |

## 👁️ Delle mod (non correggibili da noi)

| Codice | Visto in | Dove | Problema | Effetto |
|---|---|---|---|---|
| B08 | 0.1.0 | Let's Do Compat (15), Unusual End (13), Brewin' And Chewin', Farmer's Delight, Ender's Delight, Undergarden Delight | Ricette che non si caricano (compatibilità con mod non presenti o cambiate: piatti di Farm & Charm, ricette "farmer delight" di Unusual End, pizza da impasto, succo di melone, fetta di torta al chorus, gloomgourd) | basso: quelle ricette mancano |
| B09 | 0.1.0 | Create: Connected (16), Unusual End (2), Hexerei (1) | Tabelle del bottino non valide (es. catalizzatori del Dye Depot) | basso: quei blocchi rotti non lasciano niente |
| B10 | 0.1.0 | Starcatcher, Starcatcher's Delight, Selling Bin (dentro Starcatcher) | Oggetti vuoti nelle schede creative: circa 180 righe di errore di JEI a ogni avvio | nessuno |
| B11 | 0.1.0 | Aspect Alchemy | Il plugin per Jade non si carica | basso: niente informazioni di Jade sui suoi blocchi |
| B12 | 0.1.0 | Varie | Grafica e suoni mancanti: zuppa di guardiano piazzata (Ocean's Delight, 0.3.0), una variante dell'altare del vuoto (Cognition, 0.3.0), modello `icysweetness` (Born in Chaos), animazioni GeckoLib (Ars Nouveau, Ars Elemental, Cataclysm…), suoni di Deep Aether, Cataclysm, Born in Chaos, Aether's Delight | basso, estetico |
| B13 | 0.1.0 | Da identificare | 9 pozioni con dati non validi in qualche ricetta o bottino ("Failed to apply component patch") | basso |
| B14 | 0.1.0 | Varie | Messaggi innocui all'avvio: conflitto Lithium/ModernFix (`getTemperature`), file di accesso mancanti in librerie incorporate (`wdutils` di Starcatcher, `pride` di LambDynamicLights), data map di esempio `modid:example`, tag `blueprint:generates_overrides`, file con nome non valido in Create: Integrated Farming, progressi con riferimenti mancanti, Paxi "repository source", avviso di Moonlight su Forgified Fabric API (0.2.3, atteso), errore di OpenAL alla chiusura | nessuno |
| B15 | 0.3.0 | Strutture sotterranee (mod non identificata) | 42 cornici o quadri generati in posizione non valida a quota −50 circa | basso: quelle decorazioni non vengono piazzate |
| B16 | 0.1.1 | Brewin' And Chewin' 4.5.0 + AlmostUnified | Il nostro tag del mais cita `brewinandchewin:corn`, che in questa versione non esiste: voce saltata | nessuno (si attiva da sola quando B&C aggiungerà il mais) |

## ✅ Risolti o aggirati

| Codice | Visto in | Problema | Soluzione | In |
|---|---|---|---|---|
| B17 | 0.1.0 | Con NeoForge 21.1.261 o successive: "Connection lost" entrando nel mondo (owo-lib 0.12.15.5 dentro l'Aether) | **Aggirato**: NeoForge fermo a 21.1.259. Si chiude davvero quando esce owo-lib 0.12.15.6 | 0.1.1 |
| B18 | 0.1.0 | `README.md` maiuscoli dentro `data/` del datapack: "Invalid path in pack" | Rinominati `readme.md` | 0.1.1 |
| B19 | 0.1.0 | Il file per i vasi di Ars Elemental è nel formato vecchio e con il nome sbagliato: non si carica | Coltura e terreni scritti nel nostro datapack | 0.1.0 |
| B20 | 0.1.0 | Il pesce cotto di Starcatcher non vale come "pesce cotto" nelle ricette | Etichette del pesce cotto nel datapack | 0.3.0 |
| B21 | 0.1.1 | Istanza nuova: il bootstrap riceve 403 da GitHub e non parte | Non è un bug del pack (limite di GitHub): copiare `packwiz-installer.jar` o creare l'istanza per copia. In `docs/prism.md` | — |
