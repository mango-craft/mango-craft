# Bug report — Mango Craft 1.21.1

Tutti i problemi trovati nelle versioni del pack, anche minori: dai log dell'istanza di prova, dal controllo dei nomi (`../data/inventario/controllo.md`) e dalle prove in gioco. Documento vivo. Le prove ancora da fare stanno in `../lavoro/0502-prove-in-gioco.md`.

**Regole**
- Ogni problema nuovo riceve un codice (`B01`, `B02`…) che non si riusa mai, anche quando il problema è risolto.
- "Visto in" è la prima versione in cui è comparso. La voce del changelog (`0401-changelog.md`) di ogni versione elenca i codici dei suoi problemi noti.
- Quando un problema si risolve, la riga passa in "Risolti" con la versione che lo chiude.

**Stato**: 🔧 da correggere da noi · 🔍 da verificare in gioco · 👁️ della mod, non correggibile da noi (si tiene d'occhio) · ✅ risolto o aggirato
**Effetto**: alto = blocca o fa crashare · medio = una funzione non va · basso = estetico o solo nel log

_Ultimo aggiornamento: 18/10/2026 (versioni fino alla 0.5.0, prima prova)._

---

## 🔧 Da correggere da noi

| Codice | Visto in | Dove | Problema | Effetto | Piano |
|---|---|---|---|---|---|
| B01 | 0.1.1 | Datapack, artefatti | 15 nomi di casse di When Dungeons Arise e Dungeons and Taverns presi da versioni vecchie non esistono più: in quelle casse gli artefatti non compaiono mai | medio | 0.6.0, con i nomi veri dell'inventario |
| B02 | 0.1.0 | Cataclysm + YUNG's Better Nether Fortresses | I Berserker infuocati sono legati alla fortezza vanilla, che YUNG's sostituisce: non compaiono mai | medio | 0.6.0 (`berserker_spawn.json` nel datapack) |
| B03 | 0.1.0 | Datapack, artefatti | Le casse di Mowzie's Mobs e Born in Chaos non hanno gli artefatti (nomi delle tabelle mai verificati) | basso | 0.6.0, nomi presi dall'inventario |
| B22 | 0.4.0 | Every Compat (config di serie) | Crea 10.733 blocchi, il 40,7% di tutti i blocchi del pack (il più pesante è il modulo di Rechiseled, 2.183 blocchi). L'avvio passa da 51 a 78 secondi, le ricette da 22.123 a 28.026, JEI impiega di più a registrare gli oggetti | medio: tempo di avvio e memoria | 0.6.0, config ridotta di Every Compat: rivedere anche il modulo di Rechiseled, che il piano voleva tenere |

## 🔍 Da verificare in gioco

| Codice | Visto in | Dove | Problema | Effetto | Come verificare |
|---|---|---|---|---|---|
| B04 | 0.1.0 | Apotheosis + Truly Modular | All'avvio Apotheosis non riesce a leggere il "livello" (tier) di 20 armi e attrezzi modulari di Miapi | medio | Prova "Apotheosis + Truly Modular" in `0502` |
| B05 | 0.1.0 | Truly Modular | 48 errori nella creazione delle ricette del tavolo da forgiatura, un materiale di prova (`tm_armory:test`) non trovato, due attributi di danno nulli | medio | In EMI: ci sono le ricette di potenziamento delle parti modulari? |
| B06 | 0.3.0 | Animal Pen + My Nether's Delight | Le due mod modificano lo stesso punto del codice (probabilità di drop dell'equipaggiamento dei mob) | basso | Un mob con armatura uccisa lascia cadere l'equipaggiamento come al solito? |
| B07 | 0.1.0 | Accessories (dentro l'Aether) + Miapi/Hexalia | Bug noto di Accessories quando un'entità subisce danno; Forgified Fabric API dovrebbe evitarlo | alto se si presenta | Prova "Miapi + Accessories" in `0502`: subire e infliggere danno con armi Miapi e oggetti di Hexalia |
| B23 | 0.4.0 | Diagonal Walls + Aether, Deep Aether | Il modello diagonale di 11 muri non si costruisce (muro di aerogel dell'Aether, muri di tronco di Deep Aether: proprietà diverse da quelle dei muri normali). Stesso avviso per muro e recinto "wrapped copycat" di Create: Connected | basso | Piazzare in diagonale un muro di tronco di Deep Aether: si vede bene o senza texture? |
| B24 | 0.4.0 | Every Compat (Moonlight) + Twilight Forest | 48 traduzioni mancanti per i tronchi cavi (`item_type.twilightforest.hollow_log`) | basso | In EMI, i tronchi cavi creati da Every Compat hanno un nome leggibile? |

## 👁️ Delle mod (non correggibili da noi)

| Codice | Visto in | Dove | Problema | Effetto |
|---|---|---|---|---|
| B08 | 0.1.0 | Let's Do Compat (15), Unusual End (13), Brewin' And Chewin', Farmer's Delight, Ender's Delight, Undergarden Delight | Ricette che non si caricano (compatibilità con mod non presenti o cambiate: piatti di Farm & Charm, ricette "farmer delight" di Unusual End, pizza da impasto, succo di melone, fetta di torta al chorus, gloomgourd) | basso: quelle ricette mancano |
| B09 | 0.1.0 | Create: Connected (16), Unusual End (2), Hexerei (1) | Tabelle del bottino non valide (es. catalizzatori del Dye Depot) | basso: quei blocchi rotti non lasciano niente |
| B10 | 0.1.0 | Starcatcher, Starcatcher's Delight, Selling Bin (dentro Starcatcher) | Oggetti vuoti nelle schede creative: circa 180 righe di errore di JEI a ogni avvio | nessuno |
| B11 | 0.1.0 | Aspect Alchemy | Il plugin per Jade non si carica | basso: niente informazioni di Jade sui suoi blocchi |
| B12 | 0.1.0 | Varie | Grafica e suoni mancanti: zuppa di guardiano piazzata (Ocean's Delight, 0.3.0), una variante dell'altare del vuoto (Cognition, 0.3.0), modello `icysweetness` (Born in Chaos), animazioni GeckoLib (Ars Nouveau, Ars Elemental, Cataclysm…), suoni di Deep Aether, Cataclysm, Born in Chaos, Aether's Delight | basso, estetico |
| B13 | 0.1.0 | Da identificare | 9 pozioni con dati non validi in qualche ricetta o bottino ("Failed to apply component patch") | basso |
| B14 | 0.1.0 | Varie | Messaggi innocui all'avvio: conflitto Lithium/ModernFix (`getTemperature`), file di accesso mancanti in librerie incorporate (`wdutils` di Starcatcher, `pride` di LambDynamicLights), data map di esempio `modid:example`, tag `blueprint:generates_overrides`, file con nome non valido in Create: Integrated Farming, progressi con riferimenti mancanti, Paxi "repository source", avviso di Moonlight su Forgified Fabric API (0.2.3, atteso), errore di OpenAL alla chiusura. Dalla 0.5.0: Aquamirae registra lo Scuttler in una categoria di mob diversa da quella in cui lo fa comparire, file di config corretti al primo avvio (Every Compat, Jaden's), Biolith (dentro Jaden's) ignora i mondi di prova di un'altra mod, 3 file con spazi nel nome in Starcatcher's Delight | nessuno |
| B15 | 0.3.0 | Strutture sotterranee (mod non identificata) | 42 cornici o quadri generati in posizione non valida a quota −50 circa | basso: quelle decorazioni non vengono piazzate |
| B16 | 0.1.1 | Brewin' And Chewin' 4.5.0 + AlmostUnified | Il nostro tag del mais cita `brewinandchewin:corn`, che in questa versione non esiste: voce saltata | nessuno (si attiva da sola quando B&C aggiungerà il mais) |
| B29 | 0.5.0 | Jaden's Nether Expansion 2.4.1 | 5 ricette della mod citano oggetti che nella versione riscritta non esistono più (`iron_scrap`, `warphopper_fur`, `igneous_reeds`, `indented_soul_slate_tiles`) e vengono saltate; lo stesso per una ricetta di Just Enough Breeding (uovo del False Carcass). Mancano anche 2 suoni, 2 etichette e alcuni parametri di shader (Lodestone) | basso: ricette di oggetti inesistenti, al massimo qualche suono o effetto grafico in meno |
| B25 | 0.4.0 | Unusual End + Every Compat | La ricetta `unusualend:chorus_cane_cabinet_fix` cita una credenza di Every Compat (`everycomp:fd/unusualend/chorus_cane_cabinet`) che non viene creata: ricetta saltata | nessuno |
| B26 | 0.4.0 | Chimes | Due suoni della campana d'ametista hanno lettere maiuscole nel nome (`shimmering1A.ogg`, `shimmering2A.ogg`): il gioco li scarta | basso: due varianti di suono in meno |
| B27 | 0.4.0 | Generazione del mondo (mod non identificata) | 123 avvisi "Ignoring unknown attribute 'forge:entity_gravity'" mentre si genera il mondo: qualche mob delle strutture ha un attributo col nome vecchio di Forge, che viene ignorato | nessuno: il mob usa la gravità normale |

## ✅ Risolti o aggirati

| Codice | Visto in | Problema | Soluzione | In |
|---|---|---|---|---|
| B17 | 0.1.0 | Con NeoForge 21.1.261 o successive: "Connection lost" entrando nel mondo (owo-lib 0.12.15.5 dentro l'Aether) | **Aggirato**: NeoForge fermo a 21.1.259. Si chiude davvero quando esce owo-lib 0.12.15.6 | 0.1.1 |
| B18 | 0.1.0 | `README.md` maiuscoli dentro `data/` del datapack: "Invalid path in pack" | Rinominati `readme.md` | 0.1.1 |
| B19 | 0.1.0 | Il file per i vasi di Ars Elemental è nel formato vecchio e con il nome sbagliato: non si carica | Coltura e terreni scritti nel nostro datapack | 0.1.0 |
| B20 | 0.1.0 | Il pesce cotto di Starcatcher non vale come "pesce cotto" nelle ricette | Etichette del pesce cotto nel datapack | 0.3.0 |
| B28 | 0.5.0 | Il gioco non parte: Moog's Nether Structures richiede Moog's Structure Lib 3.3.0 o più recente, nel pack c'era la 3.0.3. packwiz non aggiorna una libreria già presente quando una mod nuova ne chiede una versione più recente, e il controllo dei nomi verificava solo la versione di NeoForge | Libreria aggiornata alla 3.4.2; il controllo dei nomi ora verifica le versioni richieste di tutte le dipendenze | 0.5.0 |
| B21 | 0.1.1 | Istanza nuova: il bootstrap riceve 403 da GitHub e non parte | Non è un bug del pack (limite di GitHub): copiare `packwiz-installer.jar` o creare l'istanza per copia. In `../../docs/0101-installazione.md` | — |
