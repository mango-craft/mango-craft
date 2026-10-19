# Temi aperti — Minecraft 1.21.1

Gli argomenti del modpack non ancora affrontati, o rimasti a metà, e dove si trovano le mod in valutazione. Documento vivo: quando un tema entra in una tappa, il lavoro passa nel piano (`0501-piano.md`) e qui resta un rimando; quando è chiuso si toglie, con una riga nel log (`0610-log-decisioni.md`).

Ultimo aggiornamento: 19/10/2026.

## 1. Mod in valutazione

Non si ripetono qui, per non avere due elenchi da tenere allineati:
- **candidate**, ognuna con il momento in cui rivalutarla: `0601-mod-candidate.md`;
- **scartate**, con il motivo: `0602-mod-scartate.md`.

## 2. Argomenti non ancora trattati

| Tema | Cosa manca | Dove se ne parla già | Quando (proposta) |
|---|---|---|---|
| **Achievement e progressione** (nuovo, 19/10) | Tutto: schermata dei progressi, eventuali obiettivi del pack | sezione 3 | Da decidere |
| **Difficoltà** | Le fonti di difficoltà non sono mai state bilanciate insieme: World Tier ed Elites di Apotheosis, config di Cataclysm, buff permanenti di Cataclysm Delight, Born in Chaos (Krampus), lune di sangue. In più va deciso se tenere i due effetti nuovi della luna di sangue di Enhanced Celestials 2 (mostri più vicini, assedio di zombi ai villaggi) | `../docs/0302-config.md`, Impostazioni decise; readme delle lune nel datapack | Mondo di prova (tappa 6); la decisione sulle lune anche prima |
| **Tasti in conflitto** | Sophisticated e Traveler's aprono entrambi con B, Psi e Ars Nouveau usano entrambi C. I tasti stanno in `options.txt`, che il pack non porta (decisione del 19/10): vanno cambiati a mano, serve solo un elenco dei tasti consigliati | `0302`, Impostazioni decise | Prima del mondo vero |
| **Memoria e prestazioni** | Crash per memoria finita con 8 GB (B33); Every Compat pesa il 40% dei blocchi (B22). Dopo la config ridotta di Every Compat va rimisurato tutto (avvio, memoria) e, se serve, valutate altre ottimizzazioni | `../docs/0402-bug-report.md`, B22 e B33 | 0.6.0, poi mondo di prova |
| **Aggiornamento delle mod prima della 1.0.0** | Le versioni sono quelle verificate tra il 16 e il 19/10. Non c'è un controllo automatico degli aggiornamenti: servirebbe un workflow che elenca le versioni nuove (senza installarle) e un giro di aggiornamenti prima del mondo vero. Ci rientra il ritorno all'ultimo NeoForge quando esce owo-lib 0.12.15.6 (B17) | `../docs/0303-note-tecniche.md`; `0502` (owo-lib) | Prima della 1.0.0 |
| **Licenze da verificare** | La licenza di diverse mod (addon di Farmer's Delight, Let's Do, Botany Pots e altre) non è ancora stata controllata | Legenda di `../docs/0301-mod.md` | Prima della 1.0.0 |
| **Slot degli accessori** | Ars Nouveau e Artifacts si contendono testa, collana e cintura (Curios); se gli slot diventano stretti si aumentano con un file nel datapack, formato da verificare | `0302`, Impostazioni decise | Mondo di prova |
| **Lingua del gioco** | Non è stato deciso se giocare in italiano né cosa fare con le mod senza traduzione italiana (quante siano non è stato contato). Enhanced Celestials 2 le traduzioni le scaricherebbe da internet: spente nella 0.5.2 | `0302` (traduzioni di EC2) | Da chiarire |
| **Guida del pack** | Ogni mod ha il suo manuale, ma il pack non ha una guida sua (come iniziare, cosa si collega a cosa). Si lega agli achievement | sezione 3 | Insieme agli achievement |

Restano nei loro documenti, perché sono già pianificati: densità delle strutture e Chunky (tappa 6, `0501`), controlli durante la creazione del mondo e prove di compatibilità (`0502-prove-in-gioco.md`), parti del datapack (`0630-pre-progettazione-0.6.md`).

## 3. Achievement e progressione

*(in preparazione: ricerca sulle mod disponibili per NeoForge 1.21.1 e sugli achievement che le mod del pack aggiungono già)*
