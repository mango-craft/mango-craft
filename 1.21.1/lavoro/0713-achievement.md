# Achievement e progressione (19/10/2026)

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Richiesta dell'utente: aprire il tema degli achievement (i "progressi" di Minecraft). Due strade: migliorare la schermata dei progressi e/o dare al pack una progressione propria. Fonti: API di Modrinth (versioni per NeoForge 1.21.1), sorgenti su GitHub delle mod, inventario del pack (`../data/inventario/`). Prospetto riassuntivo e decisioni: `0503-temi-aperti.md`.

## 1. Quanti progressi ha già il pack

L'inventario conta i file `advancement` di ogni mod: **10.769 file in 98 mod**, più quelli di Minecraft. Ma quasi tutti sono "sblocchi di ricette" (file nascosti che servono solo a sbloccare le ricette nel libro): i progressi veri sono molti meno.

- Minecraft 1.21.1: 1.400 file, di cui **122 progressi veri** in 5 schede.
- Contati dai sorgenti delle mod, togliendo gli sblocchi di ricette: circa **780 progressi veri in 18 mod**. Stima per tutto il pack (non verificata): **1.000–1.500**.

| Mod | File nell'inventario | Progressi veri (dai sorgenti) |
|---|---:|---:|
| Create | 1.150 | 102 (85 visibili) |
| Occultism | 1.131 | 221 (45 visibili, 158 nascosti finché non si ottengono) |
| Regions Unexplored | 638 | non contati (622 file sono sblocchi di ricette) |
| Twilight Forest | 545 | 45 |
| Bountiful Fares | 408 | circa 19 |
| Undergarden | 377 | 37 |
| Deep Aether | 377 | circa 6 |
| Ars Nouveau | 344 | circa 39 |
| Aether | 343 | 31 |
| Supplementaries | 330 | 9 (2 visibili) |
| Handcrafted | 317 | 0 (solo sblocchi di ricette) |
| Deeper and Darker | 264 | 11 |
| Farmer's Delight | 218 | 21 |
| Mekanism (+ Generators) | 97 + 4 | 97 + 4 (nessuno sblocco di ricette) |

Per Ars Nouveau, Bountiful Fares e Deep Aether i rami dei sorgenti letti potrebbero non corrispondere alla versione del pack: numeri approssimati.

**Alberi che fanno già da guida**: Create (dall'andesite all'ottone, ai treni), Mekanism, Farmer's Delight (compreso "pianta tutte le colture"), Aether, Ars Nouveau, Undergarden.

**Twilight Forest usa i progressi come lucchetto**: le zone del bosco si aprono solo con i progressi dei boss (`progress_lich`, `progress_knights`, `progress_yeti`, `progress_labyrinth`, `progress_troll`, `progress_merge`; verificato nel sorgente, `twilight/restrictions`). Questi progressi **non vanno mai cancellati né nascosti**.

Due mod usano ancora la cartella della 1.20 (`advancements/`), che la 1.21.1 ignora: Animal Pens (2 file) e Nether Depths Upgrade (4). Innocuo.

## 2. Mod per la schermata dei progressi

Versioni per NeoForge 1.21.1 lette dall'API di Modrinth.

| Mod | Versione | Licenza | Dipendenze | Cosa fa |
|---|---|---|---|---|
| **Reliable Advancements** | 6.3.1 (15/10/2026, release) | MIT | nessuna obbligatoria | Erede di Better Advancements: schermata a tutta finestra, spostamento e zoom, elenco dei requisiti, schede ordinate; **editor in gioco** (con i trucchi attivi) che salva i progressi in JSON. Aggiornata spesso (dalla 6.0 alla 6.3.1 in due mesi). Incompatibile con Better Advancements |
| **Lucid Advancements** | 1.2.21 (11/10/2026, release) | GPL-3.0 | nessuna | Un **elenco** al posto dell'albero, con ricerca (anche per mod), filtri, **barre di completamento** per scheda e totale, progressi da fissare a schermo. Testi dei requisiti tradotti in italiano. Pensata per i modpack grandi; recente (giugno 2026), pochi download |
| Better Advancements | 0.4.3.21 (2024, beta) | non commerciale | nessuna | La più diffusa, ma la build per la 1.21.1 è ferma da due anni |
| Advancements Reloaded | 0.6.1 (2024, beta) | MIT | Cloth Config | Nella 1.21.1 senza ricerca; ferma |
| Advancement Plaques | 1.6.8 (2024) | CC-BY-NC-ND | Iceberg (nuova) | Notifiche a "targa" al posto dei popup |
| Fancy Toasts | 1.5.0 (2026) | MIT | nessuna | Notifiche con 8 stili e suoni per tipo |
| Achievements Optimizer | 2.1.0 (2025) | MIT | nessuna | Alleggerisce i controlli degli sblocchi di ricette quando si raccolgono oggetti: utile solo se si nota lag |
| Just Enough Advancements | 21.1.1 (beta) | Apache | LibX (nuova) | Progressi cercabili in JEI; non verificato con EMI |

Advancements Debug esiste solo per Fabric fino alla 1.19.3.

## 3. Una progressione del pack

| Strada | Pro | Contro |
|---|---|---|
| **Progressi nostri nel datapack** `matteo_tweaks` | Nessuna mod nuova; JSON nel repository, controllati dal controllo dei nomi; condizioni di caricamento (`mod_loaded`) come gli altri file; si possono agganciare ai progressi delle mod; ricompense: esperienza, bottino, ricette, comandi (tramite funzioni) | Niente editor in gioco (salvo l'editor di Reliable Advancements, da cui copiare i file); la schermata vanilla è piccola; "fai N di queste cose" richiede funzioni |
| **Questlog** 3.3.2 | Apache-2.0, richiede Cloth Config (già nel pack); libro di missioni con pagine di testo, circa 30 tipi di obiettivo e ricompense; editor in gioco; missioni in JSON nella config | Una mod in più da mantenere; su GitHub c'è già la 3.4.1, non su Modrinth per NeoForge 1.21.1 |
| Odyssey Quests (ex Heracles) 2.0.3 | MIT, editor in gioco | Beta di due settimane, riscritta da zero |
| FTB Quests | L'editor migliore | Solo CurseForge, licenza chiusa, due librerie nuove; già scartata (`0602-mod-scartate.md`) |

Mod che danno bonus permanenti per ogni progresso (Advancements&Rewards, Achievement attribute rewards): sconsigliate, con circa 10.000 file di sblocchi di ricette rischiano di dare bonus enormi o di sbilanciare il gioco.

## 4. Proposta

1. 🟢 Provare **una** mod per la schermata nell'istanza di prova: **Reliable Advancements** (albero, editor per i nostri progressi, MIT) oppure **Lucid Advancements** (ricerca, percentuali, italiano). Una alla volta: insieme non sono state verificate.
2. 🟢 Poi, se piace, una scheda "Mango Craft" nel nostro datapack: 20–40 traguardi che collegano le mod (cucina, vasi, Create, magia, dimensioni), con ricompense in esperienza o bottino.
3. 🟡 Questlog solo se serve anche una guida del pack con pagine di testo.
4. 🟡 Achievements Optimizer solo se si nota lag raccogliendo oggetti.

## Non verificato

- Problemi noti delle mod per la schermata con alberi molto grandi (la pagina delle segnalazioni di Better Advancements non era raggiungibile).
- Numero esatto dei progressi veri del pack: l'inventario conta i file senza distinguere gli sblocchi di ricette. Si potrebbe estendere `scripts/inventory.py` per separarli.
