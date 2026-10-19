# Artefatti nelle casse delle strutture modded

## Il problema

Artifacts mette i suoi oggetti solo nelle casse **vanilla**: si aggancia ai nomi delle tabelle di bottino come `minecraft:chests/abandoned_mineshaft`. Le casse delle mod di strutture hanno nomi propri (`dungeons_arise:chests/...`, `twilightforest:...`) e quindi restano fuori.

Anche quando una cassa modded richiama al suo interno una tabella vanilla, NeoForge applica i modificatori solo alla tabella **"radice"**, cioè quella scritta nella cassa. Senza questi file, nelle strutture modded gli artefatti non uscirebbero mai.

## La soluzione: un file per livello di rarità

Il **nome del file non dice dove va l'artefatto, ma quanto è probabile trovarlo**. Artifacts ha già una tabella di bottino per ogni struttura vanilla, con la sua probabilità e il suo elenco di oggetti (per esempio la miniera: 30%, con occhiali per la visione notturna, artigli da scavo…). Ogni file prende una di queste tabelle e la applica a un elenco di casse modded, anche di mod diverse. Per questo dentro lo stesso file le mod sembrano mescolate a caso: i file sono ordinati per valore del bottino, non per mod.

Usare le tabelle di Artifacts ha tre vantaggi:
- sono già bilanciate dall'autore, quindi non abbiamo inventato nessuna probabilità;
- rispettano la config di Artifacts: se cambi `artifactRarity` o disattivi un oggetto, vale anche qui;
- bastano 15 file invece di uno per ognuna delle 148 casse collegate.

## Com'è fatto un file

Questo è `abandoned_mineshaft.json`, accorciato. I commenti `//` servono solo a spiegare: nel file vero non ci sono, e non si possono mettere.

```jsonc
{
  // 1. SE CARICARE IL FILE: solo se Artifacts è installata.
  //    Senza Artifacts il tipo "artifacts:roll_loot_table" non esisterebbe e il file darebbe errore;
  //    con questa condizione viene saltato in silenzio.
  "neoforge:conditions": [
    { "type": "neoforge:mod_loaded", "modid": "artifacts" }
  ],

  // 2. COSA FARE: tira una tabella di bottino e aggiungi il risultato alla cassa.
  //    Il bottino originale della cassa resta tutto: l'artefatto si aggiunge, non sostituisce.
  "type": "artifacts:roll_loot_table",

  // 3. QUANDO FARLO: se la cassa che si sta riempiendo è una di queste.
  //    Non sono condizioni sulle mod ma NOMI DI CASSE; il prefisso dice solo di che mod è la cassa.
  //    Se quella mod non c'è, il nome non compare mai: nessun effetto, nessun errore.
  "conditions": [
    {
      "condition": "minecraft:any_of",            // basta che UNO dei termini sia vero
      "terms": [
        { "condition": "neoforge:loot_table_id", "loot_table_id": "undergarden:chests/depleted_mine/normal" },
        { "condition": "neoforge:loot_table_id", "loot_table_id": "dungeons_arise:chests/mining_system/mining_system_treasure" }
      ]
    }
  ],

  // 4. QUALE TABELLA TIRARE: quella che Artifacts usa per le miniere vanilla (30%).
  //    Attenzione: qui "lootTable" si scrive con la T maiuscola.
  "lootTable": "artifacts:inject/chests/abandoned_mineshaft"
}
```

I file con una sola cassa (`shipwreck_treasure.json`, `ruined_portal.json`) non hanno `any_of`: hanno direttamente la condizione `neoforge:loot_table_id`.

Ogni file deve comparire anche nell'elenco [`data/neoforge/loot_modifiers/global_loot_modifiers.json`](../../../neoforge/loot_modifiers/readme.md), altrimenti resta spento.

## I 15 livelli

Probabilità di base, con `artifactRarity = 1` (il default). La colonna "Casse" conta i nomi di tabella collegati.

| File | Struttura vanilla di riferimento | Probabilità | Casse | Mod collegate |
|---|---|---|---|---|
| `bastion_treasure.json` | Tesoro del bastione | 65% | 3 | Aether, Twilight Forest |
| `underwater_ruin_big.json` | Grande rovina sottomarina | 45% | 2 | Cataclysm, Dungeons and Taverns |
| `woodland_mansion.json` | Magione | 40% | 17 | Twilight Forest, Aether, Illager Invasion, Cataclysm, Friends & Foes, When Dungeons Arise, Dungeons and Taverns |
| `jungle_temple.json` | Tempio della giungla | 35% | 4 | YUNG's Jungle Temples, Twilight Forest, When Dungeons Arise, Dungeons and Taverns |
| `stronghold_corridor.json` | Corridoio della roccaforte | 30% | 26 | YUNG's Strongholds, Twilight Forest, Aether, When Dungeons Arise, Dungeons and Taverns, Unusual End |
| `abandoned_mineshaft.json` | Miniera abbandonata | 30% | 10 | Twilight Forest, Undergarden, Cataclysm, When Dungeons Arise, Dungeons and Taverns |
| `end_city_treasure.json` | Tesoro della città dell'End | 30% | 13 | Aether, Deep Aether, Moog's End Structures, Dungeons and Taverns, Unusual End |
| `igloo_chest.json` | Igloo | 30% | 3 | Friends & Foes, Twilight Forest, Dungeons and Taverns |
| `pillager_outpost.json` | Avamposto dei predoni | 25% | 10 | Illager Invasion, When Dungeons Arise, Dungeons and Taverns, Supplementaries (cassaforte del Galeone) |
| `desert_pyramid.json` | Piramide del deserto | 20% | 6 | YUNG's Desert Temples, Cataclysm, When Dungeons Arise, Dungeons and Taverns |
| `simple_dungeon.json` | Dungeon | 15% | 39 | YUNG's Dungeons, Twilight Forest, Aether, Deep Aether, Undergarden, Cataclysm, When Dungeons Arise, Dungeons and Taverns, Unusual End, Mowzie's Mobs |
| `shipwreck_treasure.json` | Tesoro del relitto | 15% | 1 | When Dungeons Arise |
| `nether_bridge.json` | Fortezza del Nether | 15% | 10 | YUNG's Fortresses, YUNG's Dungeons, Dungeons and Taverns |
| `ancient_city.json` | Città antica | 15% | 3 | Deeper and Darker |
| `ruined_portal.json` | Portale in rovina | 15% | 1 | Aether |

Le casse sono state assegnate alla struttura vanilla più simile:
- **a volte conta il tema**: nel file della miniera ci sono solo miniere e grotte;
- **a volte conta solo il valore**: la ricompensa del dungeon d'oro dell'Aether e il caveau dei troll di Twilight stanno nel tesoro del bastione perché sono bottini di fine percorso, non perché abbiano a che fare con il Nether.

Nelle strutture grandi (When Dungeons Arise, Dungeons and Taverns, Mowzie's Mobs) è collegata una sola cassa per struttura, quella del **tesoro finale**, non tutte le stanze. Sono escluse di proposito i barili, le casse di cibo e scorte, le stanze comuni, i campi e i villaggi senza un tesoro, le tabelle generiche di Born in Chaos e le tabelle degli overhaul di Dungeons and Taverns, che non sono installati. **L'elenco completo, struttura per struttura, è nella scheda `artifacts`** (`1.21.1/mod-knowledge/artifacts.md`), insieme alle strutture ancora da decidere.

## Le casse livello per livello

Quali strutture finiscono in ogni livello (i nomi esatti delle tabelle sono nei file `.json`).

| Livello Artifacts (probabilità di base) | Casse modded collegate |
|---|---|
| Bastione, tesoro (65%) | Aether: ricompensa del dungeon d'oro · Twilight Forest: caveau dei troll |
| Grande rovina sottomarina (45%) | Cataclysm: tesoro dell'Acropoli · DnT: rovina del condotto |
| Magione (40%) | Twilight: caveau del labirinto (anche jackpot), stanza dell'aurora · Aether: ricompensa del dungeon di bronzo · Illager Invasion: labirinto · Cataclysm: tesori abbandonato e della prigione ghiacciata · Friends & Foes: barili della cittadella · WDA: tesori di Foundry, Heavenly Conqueror, Plague Asylum, Shiraz Palace, Keep Kayra, Illager Fort, Aviary · DnT: caveau del boss della Lone Citadel, laboratorio della Witch Villa |
| Tempio della giungla (35%) | YUNG's Jungle Temples: tesoro · Twilight: labirinto di siepi · WDA: casa sull'albero · DnT: tempio delle rovine nella giungla |
| Roccaforte, corridoio (30%) | YUNG's Strongholds: tesoro, armeria, cripta, trappola, prigione, stanza segreta · Twilight: stanze della roccaforte dei cavalieri, torre del Lich, colline cave grandi, torre oscura · Aether: dungeon d'argento · WDA: tesori di Bandit Towers, Heavenly Challenger, Heavenly Rider, Infested Temple, Thornborn Towers, Ceryneian Hind, Typhon, Abandoned Temple, Kisegi Sanctuary, Mechanical Nest, biblioteca e giardino di Keep Kayra, élite di Shiraz Palace · DnT: caveau della Lone Citadel · Unusual End: altare di Gloopy |
| Miniera (30%) | Twilight: colline cave medie · Undergarden: miniera esaurita · Cataclysm: nido d'ametista · WDA: Mining System, Mining Complex, Mushroom Mines, Scorched Mines, tesori di miniera grandi e medi · DnT: avamposto dei minatori |
| Città dell'End, tesoro (30%) | Aether: ricompensa del dungeon d'argento · Deep Aether: ricompensa del dungeon d'ottone · Moog's End Structures: navi giganti · DnT: caveau del castello e del faro dell'End · Unusual End: antiche torri dell'End, nave volante, nave distorta |
| Igloo (30%) | Friends & Foes: capanna dell'Iceologer · Twilight: deposito dell'aurora · DnT: forte degli Stray |
| Avamposto dei predoni (25%) | Illager Invasion: torre del forte, scale della torre dell'Illusioner, capanna dello stregone · WDA: Illager Corsair, Illager Galley, Illager Windmill · DnT: nascondiglio degli illager e suo tesoro minore · Supplementaries: cassaforte del Galeone |
| Piramide del deserto (20%) | YUNG's Desert Temples: tomba del faraone, nascondiglio, tombe · Cataclysm: tesoro del deserto · DnT: tempio delle rovine del deserto e suo tesoro minore |
| Dungeon (15%) | YUNG's Dungeons: scheletri, zombie, ragni · Twilight: colline cave piccole, stanza del labirinto, deposito della roccaforte · Aether: dungeon di bronzo · Deep Aether: dungeon d'ottone · Undergarden: catacombe · Cataclysm: rovine abbandonate · WDA: casa e villaggio dei funghi, piccolo dirigibile, faro · DnT: bunker e case sotterranee, cripte, santuari di combattimento e tesoro minore del santuario, rovine (tabella `ruin_loot_master`), borgo (hamlet) · Mowzie's Mobs: monastero e boschetto degli Umvuthana · Unusual End: biblioteche delle case dell'End, casa del viandante |
| Relitto, tesoro (15%: amo d'oro, boccaglio, pinne…) | WDA: nave pirata dei non morti |
| Fortezza del Nether (15%) | YUNG's Fortresses: mastio, culto, enigma, ossidiana, alloggi, magazzino · YUNG's Dungeons: piccolo dungeon del Nether · DnT: avamposto dei piglin, torre degli scheletri, porto del Nether |
| Città antica (15%) | Deeper and Darker: tempio antico (vertice, stanza segreta, seminterrato) |
| Portale in rovina (15%) | Aether: portali in rovina |

## La manopola `artifactRarity`

Si regola in `config/artifacts/general.toml` e vale per tutte le casse, vanilla e modded. La probabilità vera è `p / (p + r − r·p)`, dove `p` è quella della tabella e `r` è `artifactRarity`:

| `artifactRarity` | Miniera (30%) | Dungeon (15%) |
|---|---|---|
| 0 | 100% (utile solo per le prove) | 100% |
| 0,5 | 46% | 26% |
| 1 (default) | 30% | 15% |
| 2 | 18% | 8% |
| oltre 9999 | artefatti spenti | spenti |

## Aggiungere una cassa

1. **Trova il nome della sua tabella** in uno di questi modi:
   - apri il `.jar` della mod come zip e guarda in `data/<mod>/loot_table/chests/` (il nome è il percorso senza `.json`, per esempio `mowziesmobs:chests/...`);
   - in gioco, guarda una cassa **ancora chiusa** e lancia `/data get block <x> <y> <z> LootTable`;
   - sfoglia le pagine delle casse in EMI Loot.
2. **Scegli il livello** guardando la tabella sopra: a che struttura vanilla somiglia per valore?
3. **Aggiungi una riga** in `terms` nel file di quel livello, con la virgola dopo la riga precedente:
   ```json
   { "condition": "neoforge:loot_table_id", "loot_table_id": "mowziesmobs:chests/NOME" }
   ```
4. `/reload` in gioco.

Ogni cassa deve stare in **un solo** livello, altrimenti tirerebbe gli artefatti due volte.

**Nuovo livello**: Artifacts ha tabelle anche per `buried_treasure`, `spawn_bonus_chest`, `bastion_hoglin_stable`, `ancient_city_ice_box` e per le case dei villaggi (`village_armorer`, `village_temple`…). Copia un file esistente, rinominalo, cambia `lootTable` e le casse, poi aggiungilo a `global_loot_modifiers.json`.

## Provare

1. Metti per prova `artifactRarity = 0` in `config/artifacts/general.toml`: l'artefatto esce ogni volta.
2. Lancia `/loot spawn ~ ~ ~ loot <nome tabella>`, per esempio `/loot spawn ~ ~ ~ loot dungeons_arise:chests/foundry/foundry_treasure`. Il comando applica anche i modificatori, quindi a terra deve comparire un artefatto insieme al bottino normale.
3. Rimetti `artifactRarity = 1`.

## Da dove vengono i nomi

- **Verificati nei sorgenti delle versioni 1.21.1**: mod YUNG's, Twilight Forest, Aether, Deep Aether, Deeper and Darker, Undergarden, Cataclysm, Illager Invasion, Friends & Foes, Moog's End Structures, Unusual End.
- **When Dungeons Arise e Dungeons and Taverns**: i primi nomi erano presi da versioni precedenti pubblicate su GitHub (When Dungeons Arise 1.18.2 dell'autore più una copia del 2025; copia del datapack di Dungeons and Taverns di marzo 2024), perché il sorgente 1.21.1 non è pubblico. Il controllo dei nomi sull'inventario dei .jar ha mostrato che **15 nomi non esistevano** (bug B01): nella 0.6.0 sono stati tolti e, per ogni struttura rimasta senza cassa, è stato aggiunto il tesoro con il nome vero. Un nome che non esiste più non dà errori: semplicemente non scatta mai.
- **Il tipo di ogni tabella** (cassa o altro) è stato letto nei file della mod (workflow Esamina mod, 19/10/2026, `ai-agents/stage/2026-10-19_1.21.1-v0.5.3_esame-mod/`): tutte le tabelle con "vault" nel nome di Dungeons and Taverns e di When Dungeons Arise sono di tipo cassa (`minecraft:chest`), non ricompense dei blocchi caveau.
- **Supplementaries**: cassaforte del Galeone (`supplementaries:loot/galleon/safe`), verificata nei file della struttura e nell'inventario (dalla 0.2.3).
- **Mowzie's Mobs** (dalla 0.6.0, bug B03): le sue due casse, `monastery_chest` e `umvuthana_grove_chest`, sono nel livello Dungeon (15%, scelta prudente: si alza dopo la prova se le strutture si rivelano rare). **Born in Chaos** non è collegata: le sue 7 tabelle (`minecraft:chests/basic_chest`, `chest_level_1…3`, `farm_drop`, `firewell_d`, `shater`) sono generiche, a livelli, e usano il prefisso `minecraft`; collegarle metterebbe gli artefatti in ogni cassa delle sue strutture, contro la regola di una cassa per struttura.

**Due nomi che ingannano**: `minecraft:chests/ancient_end_city` e `minecraft:chests/end_house_library` sembrano vanilla, ma nel gioco base non esistono. Li aggiunge Unusual End usando il prefisso `minecraft`.
