# Tema: achievement e progressione

Aggiornata il 19/10/2026 · nessuna mod nel pack per questo tema; candidate: Reliable Advancements, Lucid Advancements, Questlog, Achievements Optimizer (`../lavoro/0601-mod-candidate.md`) · fonti: API di Modrinth, sorgenti su GitHub delle mod, inventario del pack. Ricerca: `../lavoro/versioni/v0.6.0.md`, sezione 2; grezzo `../../ai-agents/stage/2026-10-19_1.21.1-v0.6.0_achievement/`. Decisioni aperte: `../lavoro/0503-temi-aperti.md`.

## Quanti progressi ha già il pack

L'inventario conta i file `advancement` di ogni mod: **10.769 file in 98 mod**, più 1.400 di Minecraft. Quasi tutti sono "sblocchi di ricette" (file nascosti che servono al libro delle ricette): i progressi veri sono molti meno. Minecraft: 122 veri in 5 schede. Contati dai sorgenti, togliendo gli sblocchi: circa **780 veri in 18 mod**; stima per tutto il pack, non verificata, 1.000–1.500.

| Mod | File | Veri |
|---|---:|---:|
| Create | 1.150 | 102 (85 visibili) |
| Occultism | 1.131 | 221 (45 visibili) |
| Regions Unexplored | 638 | non contati (622 sono sblocchi di ricette) |
| Twilight Forest | 545 | 45 |
| Bountiful Fares | 408 | circa 19 |
| Undergarden | 377 | 37 |
| Deep Aether | 377 | circa 6 |
| Ars Nouveau | 344 | circa 39 |
| Aether | 343 | 31 |
| Supplementaries | 330 | 9 (2 visibili) |
| Handcrafted | 317 | 0 |
| Deeper and Darker | 264 | 11 |
| Farmer's Delight | 218 | 21 |
| Mekanism (+ Generators) | 97 + 4 | tutti veri |

Alberi che fanno già da guida: Create, Mekanism, Farmer's Delight, Aether, Ars Nouveau, Undergarden. **Twilight Forest usa i progressi dei boss come lucchetto**: non vanno mai tolti (`../mod-knowledge/twilight-forest.md`). Animal Pens e Nether Depths Upgrade usano ancora la cartella `advancements/` della 1.20, ignorata: innocuo.

## Mod per la schermata (NeoForge 1.21.1)

| Mod | Versione | Licenza | Cosa fa |
|---|---|---|---|
| **Reliable Advancements** | 6.3.1 (15/10/2026, release) | MIT | Erede di Better Advancements: schermata a tutta finestra, zoom, elenco dei requisiti, schede ordinate; **editor in gioco** (con i trucchi) che salva i progressi in JSON in `config/reliable_advancements_edits/`; opzione `requireRewardClaiming`. Aggiornata spesso. Incompatibile con Better Advancements, Clickable Advancements, Advancements Arranged |
| **Lucid Advancements** | 1.2.21 (11/10/2026) | GPL-3.0 | Elenco al posto dell'albero, ricerca (anche `@modid`), filtri, barre di completamento, progressi da fissare a schermo; testi dei requisiti in italiano. Recente (giugno 2026), pochi download |
| Better Advancements | 0.4.3.21 (2024, beta) | non commerciale | La più diffusa, ma ferma da due anni sulla 1.21.1 |
| Advancements Reloaded | 0.6.1 (2024, beta) | MIT | Senza ricerca nella 1.21.1; ferma |
| Advancement Plaques | 1.6.8 (2024) | CC-BY-NC-ND | Notifiche a targa; richiede Iceberg |
| Fancy Toasts | 1.5.0 (2026) | MIT | Notifiche con stili e suoni |
| Achievements Optimizer | 2.1.0 (2025) | MIT | Alleggerisce i controlli degli sblocchi di ricette alla raccolta: utile solo se si nota lag |
| Just Enough Advancements | 21.1.1 (beta) | Apache | Progressi cercabili in JEI; richiede LibX; non verificato con EMI |

Advancements Debug esiste solo per Fabric fino alla 1.19.3. Mod che danno bonus permanenti per ogni progresso: sconsigliate, con circa 10.000 sblocchi di ricette sbilanciano il gioco.

## Una progressione del pack

| Strada | Pro | Contro |
|---|---|---|
| **Progressi nostri nel datapack** | Nessuna mod nuova; JSON controllati dal controllo dei nomi; condizioni di caricamento; agganciabili ai progressi delle mod; ricompense esperienza, bottino, ricette, funzioni | Niente editor in gioco (salvo quello di Reliable Advancements, da cui copiare i file); schermata vanilla piccola; "fai N cose" richiede funzioni |
| Questlog 3.3.2 | Apache-2.0, Cloth Config già nel pack; libro di missioni con pagine di testo, circa 30 obiettivi, editor in gioco; missioni in JSON | Una mod in più; su GitHub c'è già la 3.4.1 non su Modrinth |
| Odyssey Quests (ex Heracles) 2.0.3 | MIT, editor | Beta di due settimane, riscritta da zero |
| FTB Quests | L'editor migliore | Solo CurseForge, licenza chiusa, due librerie nuove; scartata (`../lavoro/0602-mod-scartate.md`) |

Proposta del 19/10: provare una mod per la schermata (una sola alla volta), poi una scheda "Mango Craft" nel datapack con 20–40 traguardi; Questlog solo se serve una guida con pagine di testo.

## Non verificato

- Per Ars Nouveau, Bountiful Fares e Deep Aether i rami dei sorgenti letti potrebbero non corrispondere alla versione del pack: numeri approssimati.
- Problemi noti delle mod per la schermata con alberi molto grandi (la pagina delle segnalazioni di Better Advancements non era raggiungibile).
- Numero esatto dei progressi veri del pack: l'inventario conta i file senza distinguere gli sblocchi di ricette; si potrebbe estendere `scripts/inventory.py` per separarli.
