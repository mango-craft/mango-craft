# Pacchetti di shader per il pack (19/10/2026)

> **Documento storico**: fotografia del momento in cui è stato scritto, non si aggiorna. Lo stato attuale è nei documenti vivi (vedi il README della cartella).

Richiesta dell'utente: includere nel pack un paio di pacchetti di shader **facoltativi** (spenti di serie) che funzionino con le mod del pack. Base: Iris 1.8.14-beta.1 con Sodium 0.8.13 (`0709-shader.md`). PC dell'utente letto dal log di Iris: NVIDIA GeForce RTX 5060 Ti, Ryzen 7 9700X.

Fonti: API di Modrinth (versioni, licenze, download), sorgenti su GitHub di Complementary Reimagined (r5.9.2) e MakeUp - Ultra Fast (commit del 16/10/2026), descrizione di Colorwheel, testi del codice di Enhanced Celestials 2: Shader Support (workflow Esamina mod, `../data/esami/`), inventario del pack.

## Candidati (versioni per Iris e Minecraft 1.21.1)

| Pacchetto | Download | Licenza | Nei modpack | Note |
|---|---:|---|---|---|
| **Complementary Reimagined** | 60 M | Complementary License 1.7 | ✅ se aggiunto tramite Modrinth (come fa packwiz), **senza modifiche** (nemmeno blocchi aggiunti), con credito se acceso di serie | r5.9.3, 15/9/2026. Profili da Potato a Ultra. Supporto ufficiale a Colorwheel |
| Complementary Unbound | 39 M | come sopra | ✅ come sopra | Stesso codice di Reimagined, stile più marcato: doppione |
| BSL | 27 M | ARR | da chiedere | Scartato per la licenza |
| Photon | 24 M | propria | non dichiarato | Bello ma pesante; niente sulle mod |
| Solas, Bliss | 15 M, 13 M | ARR | da chiedere | Scartati per la licenza |
| **MakeUp - Ultra Fast** | 11 M | LGPL-3.0 | ✅ | 9.5g, 4/10/2026. Il più leggero tra i diffusi, molto configurabile. Elenco esplicito di blocchi delle mod |
| Mellow, Miniature | 5 M, 4 M | MIT | ✅ | Stile semplice, nessun supporto alle mod |

## Compatibilità con le mod del pack

- **Blocchi delle mod**: gli shader riconoscono i blocchi (foglie che si muovono, luci, minerali) da un elenco nel file `block.properties`.
  - Complementary elenca **solo blocchi vanilla**: i blocchi delle mod hanno l'aspetto generico. La licenza vieta di aggiungerne (anche solo righe dell'elenco).
  - MakeUp elenca anche blocchi delle mod. Confrontato con l'inventario del pack, ne riconosce **circa 200 che esistono davvero nel pack**: Create 104, Handcrafted 22, Farmer's Delight 17, Twilight Forest 13, Ars Nouveau 13, Cataclysm 9, Create: Connected 7, Deeper and Darker 4, Occultism 4, Undergarden 2, Create: Enchantment Industry 1.
- **Create (Flywheel)**: con uno shader attivo Flywheel spegne la sua accelerazione e Create disegna i macchinari in modo normale (corretto, più lento con molte macchine). Colorwheel (candidata, `0601`) recupera l'accelerazione solo con i pacchetti che la supportano: **Complementary sì** (ufficiale dalla r5.7, file `colorwheel.properties` e programmi `clrwl_*` nel sorgente), MakeUp no.
- **Enhanced Celestials 2: Shader Support**: dai testi del codice, controlla con l'API di Iris se c'è un pacchetto attivo (`isShaderPackInUse`) e colora lo schermo sopra la scena (cielo, luna, bagliore). Non dipende dal pacchetto: funziona con entrambi.
- **Versione di Iris**: Complementary adatta il codice alla versione di Iris (controlli `IRIS_VERSION`, funzioni avanzate solo facoltative); MakeUp non chiede funzioni particolari. Nessun problema noto con la 1.8.14.
- Gli altri punti delicati (effetti di Lodestone, Twilight Forest, Ars Nouveau con i blocchi Skyweave neri) valgono per qualsiasi pacchetto: `0709-shader.md`.

## Scelta

- **Complementary Reimagined** 🟢: il più diffuso, profili per ogni PC, supporta Colorwheel se un giorno si usano gli shader con molti macchinari di Create.
- **MakeUp - Ultra Fast** 🟢: leggero, licenza libera, riconosce i blocchi di Create, Farmer's Delight, Twilight Forest, Ars Nouveau e altre mod del pack.
- Entrambi **spenti di serie**: packwiz li mette nella cartella `shaderpacks`, si scelgono in gioco. Nessun file di impostazioni di Iris nel pack (le impostazioni video restano a chi gioca, decisione del 19/10).

## Non verificato

- L'aspetto in gioco con le mod del pack (va provato: `0502`).
- Che gli id dei blocchi elencati da MakeUp abbiano ancora gli stessi stati e proprietà nelle versioni delle mod del pack: si è controllato solo che i nomi esistano.
