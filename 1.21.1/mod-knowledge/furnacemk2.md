# FurnaceMk2

Aggiornata il 24/10/2026 · **nel pack dalla 0.7.1** (approvata da Matteo il 24/10, insieme a Iron Furnaces; valori di serie, esperienza compresa: `../lavoro/versioni/v0.7.1.md`) (`../lavoro/0601-mod-candidate.md`), tema `../theme-knowledge/fornaci.md` · fonti: API di Modrinth (24/10); jar 0.1.11 letto dal workflow Esamina mod (`../../ai-agents/archivio/2026-10-24_1.21.1-v0.6.3_esame-mod/furnacemk2.md`); sorgente su GitHub (`ColinGBos/FurnaceMk2`, ramo `1.21.1-neoforge`, commit `bacfaa0` del 15/09/2026; `ColinGBos/VapourWare`, stesso ramo, commit `cb73d84`).

## La mod

- Di VapourDrive, **MIT**, sorgente pubblico. Per la 1.21.1 NeoForge: **0.1.11**, release del 29/07/2025 (circa 1.000 download di quel file; 10.000 in tutto, quasi tutti delle versioni vecchie). La pagina la descrive ancora come beta. Nel sorgente c'è già una 0.1.12 non pubblicata.
- Richiede **VapourWare** ≥ 0.2.36 (stesso autore, MIT, sorgente pubblico; 0.2.37 release del 29/07/2025): codice comune delle sue macchine a combustibile, più una chiave inglese (Handyman's Wrench) che gira i blocchi e smonta le macchine. Nessun'altra dipendenza.
- Integrazione con JEI e, tramite VapourWare, con Jade (entrambe nel pack).

## Come funziona (sorgente)

- **Un solo blocco**, la FurnaceMk2: non è una scala di livelli. Ha 3 slot per i **nuclei** (uno per tipo, non si impilano), 1 per il combustibile, 1 per l'ingrediente, **4 di uscita** e 1 per il cristallo dell'esperienza.
- Usa **solo le ricette di fusione** (`minecraft:smelting`), con il loro tempo di cottura: niente ricette dell'altoforno o dell'affumicatoio.
- **Velocità**: ×2 rispetto alla fornace normale (5 secondi invece di 10); con il **nucleo termico** ×4 (2,5 secondi).
- **Combustibile**: si accumula in una riserva interna (fino a 750 cotture) e si consuma solo cuocendo, quindi non si spreca. Rende ×1,25 (il carbone cuoce 10 oggetti invece di 8); con il **nucleo isolante** ×1,875 (15 oggetti). Il consumo per oggetto non cambia con la velocità.
- **Esperienza**: quella delle ricette di fusione ×1,25; con il **nucleo d'esperienza** ×2,5. Resta nella fornace fino a 500 punti. Il **cristallo sintonizzato** messo nel suo slot la assorbe da solo (fino a 10.000 punti, poi esce nello slot di uscita). Col cristallo in mano: clic destro dà esperienza fino al livello successivo; con Maiusc ci si mette dentro la propria, un livello alla volta. La chiave di VapourWare, con Maiusc sulla fornace, dà al giocatore l'esperienza accumulata. Non è un liquido: non tocca le regole dell'esperienza liquida (tema `esperienza`).
- **Tramogge e tubi**: dal basso escono solo i prodotti; dagli altri lati si accede a tutti gli slot insieme (non c'è un lato riservato al combustibile): se la si automatizza, da provare in gioco.

## Ricette (5 file nel jar, riscrivibili nel datapack)

| Oggetto | Ricetta | Note |
|---|---|---|
| FurnaceMk2 | fornace, altoforno, bottiglia di vetro, 2 pietra liscia, 4 pietra da attrezzi (`minecraft:stone_tool_materials`) | inizio partita |
| Nucleo termico (velocità) | secchio di lava, blocco di magma, 4 mattoni del Nether, 3 blackstone | serve il Nether |
| Nucleo isolante (combustibile) | 4 sabbia, 2 argilla, 3 cemento bianco | facile |
| Nucleo d'esperienza | 2 smeraldi, 2 diamanti, blocco di lapislazzuli | |
| Cristallo sintonizzato | 4 lapislazzuli, 2 smeraldi, 1 diamante | |

## Config

Config di tipo **server**: nel pack sarebbe `config/furnacemk2-server.toml`, valida per tutti i mondi (tema `neoforge`). Chiavi, sezione `furnacemk2.furnace`: `furnaceBaseSpeed` (2,0; da 0 a 10), `furnaceUpgradedSpeed` (2,0; moltiplica la base), `furnaceBaseEfficiency` (1,25), `furnaceUpgradedEfficiency` (1,5), `furnaceBaseExperience` (1,25), `furnaceUpgradedExperience` (2,0); sezione `furnacemk2.crystal`: `crystalXPStorage` (10.000; da 100 a 1.000.000).

## Da tenere presente

- L'esperienza moltiplicata rende più facile farne con la fusione: per esempio il cactus (1 punto nel gioco base) ne darebbe 2,5 con il nucleo. Si regola con `furnaceUpgradedExperience`.
- Da sola dà due gradini (fornace → FurnaceMk2 → nuclei), non una progressione lunga: quella la fa Iron Furnaces, che entra con lei (tema `fornaci`).
