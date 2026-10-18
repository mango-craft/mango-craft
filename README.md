# Mango Craft

Modpack personale per **Minecraft 1.21.1 · NeoForge**, da giocare in single player con **Prism Launcher**.
Cucina e agricoltura (Farmer's Delight e addon, Botany Pots, Let's Do, stagioni), tecnologia (Create, Mekanism), esplorazione (strutture, dimensioni, boss), magia (Ars Nouveau, Occultism…) e decorazione.

Il pack è gestito con [packwiz](https://packwiz.infra.link/): il repository contiene solo l'elenco delle mod (con versione esatta e hash), le configurazioni e il datapack. Prism scarica e aggiorna tutto da solo a ogni avvio.

| | |
|---|---|
| Versione attuale | **0.1.1** (tag `1.21.1-v0.1.1`) |
| Minecraft | 1.21.1 |
| NeoForge | **21.1.259**, da impostare a mano in Prism (non usare versioni più nuove, vedi `1.21.1/CHANGELOG.md`) |
| Memoria consigliata | 8 GB |

## Installazione in Prism (in breve)

1. Scarica `packwiz-installer-bootstrap.jar` dalle [release ufficiali](https://github.com/packwiz/packwiz-installer-bootstrap/releases).
2. In Prism crea un'istanza **Minecraft 1.21.1** con **NeoForge 21.1.259**, e nelle sue impostazioni (*Java*) dai 8 GB di memoria massima.
3. Metti il `.jar` nella cartella `minecraft` dell'istanza (tasto destro sull'istanza → *Cartella*).
4. Nelle impostazioni dell'istanza, *Comandi personalizzati* → *Comando prima dell'avvio* (Pre-launch command):
   ```
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/mango-craft/mango-craft/refs/tags/1.21.1-v0.1.1/1.21.1/pack/pack.toml
   ```
5. Avvia: la prima volta scarica circa 200 file.
6. Alcune mod di CurseForge (oggi Roaster's Delight) vanno scaricate a mano: nella finestra *Failed file downloads* clicca la mod per vedere dove salvarla, premi *Open missing mods*, scarica il file, mettilo in quel percorso senza rinominarlo e premi *Continue*. Passi dettagliati: [mod da scaricare a mano](docs/prism.md#mod-di-curseforge-da-scaricare-a-mano).

Guida completa, con le istanze di prova, del mondo vero e di archivio: [`docs/prism.md`](docs/prism.md).

## Struttura

```
AGENTS.md / CLAUDE.md     istruzioni per gli agenti AI che lavorano sul repository
docs/                     guide comuni: prism.md, sviluppo.md
scripts/                  script di supporto (indice, controlli, importazione)
.github/workflows/        controllo automatico, aggiunta mod CurseForge, release
1.21.1/
├── CHANGELOG.md          versioni del pack
├── docs/                 stato del progetto, decisioni, verifiche, ricerche, datapack
├── data/                 dati grezzi delle ricerche
└── pack/                 il pack vero e proprio (solo questo finisce nel gioco)
```

## Versioni

Il lavoro in corso sta sul ramo `dev`; `main` riceve solo versioni provate. Le **0.x** sono tappe di prova (*pre-release*), il mondo vero parte dalla **1.0.0**.

Ogni versione è un tag `1.21.1-vX.Y.Z` con la sua [release](https://github.com/mango-craft/mango-craft/releases), che contiene un `.mrpack` con le sole mod di Modrinth e lo zip della documentazione. Le mod solo CurseForge non sono incluse nei file pubblici: sono elencate nelle note di ogni release.

## Licenze

I contenuti originali di questo repository (documentazione, script, datapack `matteo_tweaks`, configurazioni) sono sotto licenza MIT, vedi [`LICENSE`](LICENSE). Le parti copiate da altri progetti lo indicano nel readme della cartella. **Le mod non sono incluse**: il pack contiene solo riferimenti ai file pubblicati dai rispettivi autori su Modrinth e CurseForge, ognuno con la propria licenza.
