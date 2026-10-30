# Artefatti nelle casse che Relics non vede (dalla 0.7.0)

## Il problema

Dalla 0.7.0 gli artefatti sono **reliquie** (Relics + Reliquified Artifacts). Le reliquie nelle casse le mette **Relics**: in una cassa su dieci (il 10%, regolato in [`../../../relics/readme.md`](../../../relics/readme.md)), scegliendo la reliquia per nome della cassa, bioma e dimensione. Relics però guarda solo le tabelle il cui nome è `<mod>:chests/…`.

Restano fuori 25 casse che prima avevano gli artefatti: quasi tutte quelle di **Twilight Forest** (che non usa `chests/` nei nomi), quelle di **YUNG's Better Dungeons** (`betterdungeons:<dungeon>/chests/…`), le navi giganti di **Moog's End Structures**, la cassaforte del **Galeone** di Supplementaries e i barili della cittadella di **Friends & Foes**. Questi file danno a quelle casse un artefatto con le probabilità di Artifacts.

Dalla 0.7.5 anche i **tesori di Better Archeology**: le sue casse (`betterarcheology:archeology/chest_…`) non avevano mai avuto artefatti, perché Artifacts non le conosceva e Relics non le vede. Una cassa per struttura, quella del tesoro (la regola della 0.6.0 per Twilight Forest), con il livello di una cassa vanilla simile: 9 casse. Le altre casse di Better Archeology restano senza. Se Better Archeology venisse tolta, quelle righe non trovano niente e non danno errori.

Fino alla 0.6.3 qui c'erano 15 file per 152 casse, con il tipo `artifacts:roll_loot_table`. Con Reliquified Artifacts quel tipo non dà più reliquie (le scarta), e 127 di quelle casse le copre già Relics: i file e le casse in più sono stati tolti (elenco completo di prima nella storia del repository e nella scheda `artifacts`).

## Com'è fatto un file

Questo è `stronghold_corridor.json`. I commenti `//` servono solo a spiegare: nel file vero non ci sono, e non si possono mettere.

```jsonc
{
  // 1. SE CARICARE IL FILE: solo se Artifacts è installata (la tabella tirata è sua).
  "neoforge:conditions": [
    { "type": "neoforge:mod_loaded", "modid": "artifacts" }
  ],

  // 2. COSA FARE: tira una tabella e AGGIUNGI il risultato alla cassa (non toglie niente).
  //    È un tipo di NeoForge: Reliquified Artifacts non lo tocca.
  "type": "neoforge:add_table",

  // 3. QUANDO FARLO: se la cassa che si sta riempiendo è una di queste.
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        { "condition": "neoforge:loot_table_id", "loot_table_id": "twilightforest:stronghold_room" },
        { "condition": "neoforge:loot_table_id", "loot_table_id": "twilightforest:hill_3" },
        { "condition": "neoforge:loot_table_id", "loot_table_id": "twilightforest:darktower_key" }
      ]
    }
  ],

  // 4. QUALE TABELLA TIRARE: quella che Artifacts usa per la roccaforte vanilla (30%).
  "table": "artifacts:inject/chests/stronghold_corridor"
}
```

I file con una cassa sola non hanno `any_of`. Ogni file deve comparire nell'elenco [`data/neoforge/loot_modifiers/global_loot_modifiers.json`](../../../neoforge/loot_modifiers/readme.md), altrimenti resta spento.

## I 10 file

34 casse in tutto: le 25 fino alla 0.7.4 e le 9 di Better Archeology. Probabilità di base delle tabelle di Artifacts (la config di Artifacts non vale più: Reliquified Artifacts la ignora).

| File | Probabilità | Casse |
|---|---|---|
| `bastion_treasure.json` | 65% | Twilight Forest: caveau dei troll (con e senza lampada) |
| `woodland_mansion.json` | 40% | Twilight Forest: caveau del labirinto (anche jackpot), stanza dell'aurora · Friends & Foes: barili della cittadella · Better Archeology: tesoro del tempio della luce |
| `jungle_temple.json` | 35% | Twilight Forest: labirinto di siepi · Better Archeology: tesoro del tempio della giungla |
| `stronghold_corridor.json` | 30% | Twilight Forest: stanza della roccaforte dei cavalieri, colline cave grandi, stanza della chiave della torre oscura · Better Archeology: cassa d'oro delle catacombe, cassa della spada dello sculk che consuma |
| `abandoned_mineshaft.json` | 30% | Twilight Forest: colline cave medie |
| `end_city_treasure.json` | 30% | Moog's End Structures: tesoro e cassa della nave gigante |
| `igloo_chest.json` | 30% | Twilight Forest: deposito dell'aurora |
| `pillager_outpost.json` | 25% | Supplementaries: cassaforte del Galeone · Better Archeology: motta |
| `simple_dungeon.json` | 15% | YUNG's Better Dungeons: dungeon degli scheletri, degli zombie (anche lapide e stanza speciale), dei ragni · Twilight Forest: colline cave piccole, stanza del labirinto, deposito della roccaforte · Better Archeology: rovine sepolte nella sabbia, rovine della mesa, tumulo, rovine sottomarine |
| `nether_bridge.json` | 15% | YUNG's Better Dungeons: piccolo dungeon del Nether |

In queste casse non c'è anche la reliquia di Relics: Relics non le vede. Le reliquie proprie di Relics (le sue 20) qui non escono.
