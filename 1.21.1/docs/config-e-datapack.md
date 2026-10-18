# File di configurazione del modpack

_Versione del 16/10/2026 · MC 1.21.1 · NeoForge · Prism Launcher_

Questi file vanno copiati nella cartella dell'istanza. In Prism: tasto destro sull'istanza → **Cartella** → entrare in `minecraft` (o `.minecraft`) e copiare la cartella `config` di questo pacchetto sopra quella esistente.

| File | Cosa fa | Quando ha effetto |
|---|---|---|
| `config/almostunified/tags.json` | Rende intercambiabili gli ingredienti doppi tra le mod di cucina e magia | Al riavvio del gioco, in tutti i mondi |
| `config/sparsestructures.json5` | Distanze tra le strutture (generale 1.4; villaggi normali) | Al riavvio, solo nei chunk nuovi → mondo nuovo |
| `config/paxi/datapacks/matteo_tweaks/` | Datapack caricato da Paxi in tutti i mondi: lune di sangue più rare e meno affollate; artefatti nelle casse delle strutture modded; colture e frutti di Ars Nouveau nei vasi di Botany Pots | Al riavvio / alla creazione del mondo (il bottino vale per le casse non ancora aperte) |

Il datapack `matteo_tweaks` ha un file di spiegazione in ogni cartella (i `.json` non accettano commenti): si parte da `config/paxi/datapacks/matteo_tweaks/README.md`, dentro `data/` si chiamano `readme.md` (minuscolo, altrimenti il gioco segnala un errore di percorso).

AlmostUnified e Sparse Structures generano un file di default al primo avvio: questi lo **sostituiscono**. Se il gioco li ha già creati, sovrascriverli.

---

## 1. Ingredienti intercambiabili (AlmostUnified, `tags.json`)

AlmostUnified lavora sui tag già risolti: un oggetto aggiunto a un tag "figlio" non arriva al tag "padre". Per questo ogni oggetto è aggiunto a **tutti** i tag che le ricette usano davvero (ricavati dai sorgenti delle mod).

| Ingrediente | Prima | Dopo |
|---|---|---|
| **Farina** | Create (`c:flours/wheat`), Farm & Charm e Bountiful Fares (`c:flour`) non si scambiavano | Tutte e tre valgono ovunque |
| **Impasto** | FD e Create (`c:foods/dough`), Farm & Charm (`c:dough`) separati | Impasto di grano intercambiabile tra le tre. Gli impasti speciali (mais, patata dolce) restano separati |
| **Sale** | Expanded e Cultural Delights (`c:dusts/salt`), Meadow (`c:salts`), Hexalia (`c:salt`) | Ogni sale vale nelle ricette di tutte (Hexalia li accettava già) |
| **Mais** | Cultural Delights e Farm & Charm (`c:crops/corn`), Bountiful Fares (`c:foods/corn`), Brewin' And Chewin' (solo `c:crops`) | Intercambiabile. ⚠️ Le 5 ricette di Brewin' che chiedono proprio il **suo** mais restano così (non si sistemano con i tag) |
| **Limone** | Cultural Delights (`c:fruits/lemon`), Bountiful Fares (`c:foods/lemons`) | Intercambiabile |
| **Formaggio (porzioni)** | Meadow (fetta), Expanded Delight (fetta), Brewin' (spicchi), Cultural Delights (spicchio): quattro tag diversi | Le porzioni base valgono ovunque; le fette speciali di Meadow (ametista, distorta…) restano solo di Meadow. Formaggio di capra di Meadow valido per Expanded Delight |

Burro: già condiviso (`c:butter`). Latte: lasciato com'è (secchi, bottiglie e cocco sono forme diverse).

**Come verificare**: nel log di avvio, le righe `[CustomTags]` segnalano eventuali oggetti inesistenti (vengono saltati, il gioco non si rompe). In EMI, cercando `#c:dusts/salt` (il `#` cerca per tag) devono comparire tutti e quattro i sali.

## 2. Strutture (Sparse Structures, `sparsestructures.json5`)

- **Generale 1.4**: tutte le strutture un po' più rade (decisione del pack)
- **Villaggi a 1**: frequenza originale
- **Magione 2**: default della mod
- **Da completare** (istruzioni dentro il file): Witch Villa e Swamp Village di Dungeons and Taverns con fattore **3** (molto più rare, scelta dell'utente) e When Dungeons Arise a 2. I nomi esatti si leggono in gioco con `/dumpstructuresets` (crea un file con tutti i gruppi) oppure `/locate structure nova_structures:` + Tab

## 3. Lune (datapack `matteo_tweaks`, via Paxi)

| Evento | Prima | Dopo |
|---|---|---|
| Luna di sangue | 10% delle notti, mostri ×2,25 | **5%** delle notti, mostri **×2** |
| Super luna di sangue | 5% delle lune piene, almeno 20 notti di distanza, mostri ×4,5 | stessa frequenza (era già rarissima), mostri **×4** |

I due file sono le copie complete degli originali di Enhanced Celestials 6.x con solo questi valori cambiati. Per ritoccare: `dimension_chances → minecraft:overworld → chance` e `mob_settings → spawn_category_multiplier → monster`.

## 4. Artefatti nelle strutture modded (datapack `matteo_tweaks`)

Artifacts aggiunge i suoi oggetti solo alle casse **vanilla** (miniere, templi, fortezze, roccaforti…), e NeoForge non applica i modificatori alle tabelle "annidate": una cassa modded che richiama una tabella vanilla non dà artefatti. Per questo il datapack aggiunge 15 modificatori, uno per livello di bottino: ogni gruppo di casse modded usa la tabella di Artifacts della struttura vanilla equivalente, con la stessa probabilità e le stesse regole di config (`artifactRarity`, oggetti disattivati). Nelle strutture grandi è collegata solo la cassa del tesoro finale, non tutte le stanze.

| Livello Artifacts (probabilità di base) | Casse modded collegate |
|---|---|
| Bastione, tesoro (65%) | Aether: ricompensa del dungeon d'oro · Twilight Forest: caveau dei troll |
| Grande rovina sottomarina (45%) | Cataclysm: tesoro dell'Acropoli · DnT: rovina del condotto, monumento del tridente |
| Magione (40%) | Twilight: caveau del labirinto (anche jackpot), stanza dell'aurora · Aether: ricompensa del dungeon di bronzo · Illager Invasion: labirinto · Cataclysm: tesori abbandonato e della prigione ghiacciata · Friends & Foes: barili della cittadella · WDA: tesori di Foundry, Heavenly Conqueror, Plague Asylum, Shiraz Palace, Keep Kayra, Illager Fort, Aviary · DnT: caveau del boss della Lone Citadel, laboratorio della Witch Villa |
| Tempio della giungla (35%) | YUNG's Jungle Temples: tesoro · Twilight: labirinto di siepi · WDA: casa sull'albero · DnT: tempio delle rovine nella giungla |
| Roccaforte, corridoio (30%) | YUNG's Strongholds: tesoro, armeria, cripta, trappola, prigione, stanza segreta · Twilight: stanze della roccaforte dei cavalieri, torre del Lich, colline cave grandi, torre oscura · Aether: dungeon d'argento · WDA: tesori di Bandit Towers, Heavenly Challenger, Heavenly Rider, Infested Temple, Thornborn Towers, Ceryneian Hind, Typhon, Abandoned Temple, biblioteca e giardino di Keep Kayra, élite di Shiraz Palace · DnT: caveau della Lone Citadel · Unusual End: altare di Gloopy |
| Miniera (30%) | Twilight: colline cave medie · Undergarden: miniera esaurita · Cataclysm: nido d'ametista · WDA: Mining System, Mushroom Mines, Scorched Mines, tesori di miniera grandi e medi · DnT: avamposto dei minatori |
| Città dell'End, tesoro (30%) | Aether: ricompensa del dungeon d'argento · Deep Aether: ricompensa del dungeon d'ottone · Moog's End Structures: navi giganti · DnT: caveau del castello e del faro dell'End · Unusual End: antiche torri dell'End, nave volante, nave distorta |
| Igloo (30%) | Friends & Foes: capanna dell'Iceologer · Twilight: deposito dell'aurora · DnT: forte degli Stray |
| Avamposto dei predoni (25%) | Illager Invasion: torre del forte, scale della torre dell'Illusioner, capanna dello stregone · WDA: Illager Corsair, Illager Galley, Illager Windmill · DnT: nascondiglio degli illager · Supplementaries: cassaforte del Galeone |
| Piramide del deserto (20%) | YUNG's Desert Temples: tomba del faraone, nascondiglio, tombe · Cataclysm: tesoro del deserto · DnT: tempio delle rovine del deserto |
| Dungeon (15%) | YUNG's Dungeons: scheletri, zombie, ragni · Twilight: colline cave piccole, stanza del labirinto, deposito della roccaforte · Aether: dungeon di bronzo · Deep Aether: dungeon d'ottone · Undergarden: catacombe · Cataclysm: rovine abbandonate · WDA: casa e villaggio dei funghi, funghi giganti, piccolo dirigibile, faro · DnT: bunker e case sotterranee, cripte, santuari di combattimento, città in rovina · Unusual End: biblioteche delle case dell'End, casa del viandante |
| Relitto, tesoro (15%: amo d'oro, boccaglio, pinne…) | WDA: nave pirata dei non morti |
| Fortezza del Nether (15%) | YUNG's Fortresses: mastio, culto, enigma, ossidiana, alloggi, magazzino · YUNG's Dungeons: piccolo dungeon del Nether · DnT: avamposto dei piglin, torre degli scheletri, porto del Nether |
| Città antica (15%) | Deeper and Darker: tempio antico (vertice, stanza segreta, seminterrato) |
| Portale in rovina (15%) | Aether: portali in rovina |

Esclusi di proposito: casse di cibo e scorte (mensa, depositi, accampamenti, barili), casse "decorative" (Witch Huts, Ocean Monuments, Extras, Towns and Towers, capanne di Hexerei e Hexalia, capanna nella palude di DnT), tabelle dei pacchetti "overhaul" di DnT (non installati).

**Da dove vengono i nomi**
- YUNG's, Twilight, Aether, Deep Aether, Deeper and Darker, Undergarden, Cataclysm, Illager Invasion, Friends & Foes, Moog's End Structures, **Unusual End**, Supplementaries: sorgenti delle versioni 1.21.1, verificati
- **When Dungeons Arise** e **Dungeons and Taverns**: il sorgente 1.21.1 non è pubblico, i nomi vengono da versioni precedenti pubblicate su GitHub (WDA: repository dell'autore, versione 1.18.2, più una copia del 2025 con le strutture nuove; DnT: copia del datapack di marzo 2024), controllati sui file delle strutture. Le strutture aggiunte dopo potrebbero mancare. Un nome che non esiste non dà errori: semplicemente non scatta

**Da completare**: Mowzie's Mobs e Born in Chaos (nessun sorgente trovato), più eventuali strutture nuove di WDA e DnT. I nomi si trovano così:
- aprendo il `.jar` della mod come zip, cartella `data/<mod>/loot_table/chests/`
- in gioco, guardando una cassa non aperta: `/data get block <x> <y> <z> LootTable`
- nelle pagine delle casse di EMI Loot

Poi si aggiungono, nella lista `terms`, al file del livello giusto in `data/matteo_tweaks/loot_modifiers/artifacts/`.

**Come provare**: `/loot spawn ~ ~ ~ loot <id tabella>` applica i modificatori; mettendo per prova `artifactRarity = 0` nella config di Artifacts l'artefatto esce ogni volta.

## 5. Colture e alberi di Ars Nouveau in Botany Pots

| Cosa | Come | Da dove |
|---|---|---|
| **Magebloom**, **Sourceberry** | Seme nel vaso, terra normale | Datapack del pack |
| **Alberi di archwood** (blu, rosso, viola, verde; giallo di Ars Elemental) | Alberello nel vaso: tronchi, foglie (con le cesoie), alberello al 5% | Già in **Botany Trees** |
| **Frutti** (Frostaya, Bombegranate, Bastion, Mendosteen, Flashpine) | Tronco di archwood come terreno + frutto come coltura, come il cacao sul tronco della giungla; 3 frutti a raccolto | Datapack del pack |

In Ars gli alberi cresciuti da alberello non fanno frutti (li hanno solo quelli generati nel mondo): i frutti si piantano sui tronchi del colore giusto. Nei vasi vale la stessa regola: blu → Frostaya, rosso → Bombegranate, viola → Bastion, verde → Mendosteen, giallo → Flashpine.

## 6. Config da impostare a mano (non incluse nel pacchetto)

- `config/artifacts/general.toml`, sezione `[slots]`: `enableAccessoriesCompat = false` (lasciare `enableCuriosCompat = true`), prima di creare il mondo
