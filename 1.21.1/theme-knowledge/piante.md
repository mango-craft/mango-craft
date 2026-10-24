# Tema: le piante del pack (vasi e mercato)

Aggiornata il 24/10/2026 · mod coinvolte: Botany Pots (+ Tiers, Additions), Farming for Blockheads, e tutte le mod che portano piante · fonti: inventario dei 255 jar, sorgenti di Botany Pots 21.1.44 e Farming for Blockheads 21.1.14, base dati `scripts/botanypots_db.py` · schede: `../mod-knowledge/botany-pots/` (vasi, con il modello in `analisi.md`), `../mod-knowledge/farming-for-blockheads.md` (mercato) · versioni: `../lavoro/versioni/v0.6.1.md` (vasi), `v0.6.2.md` (mercato).

Documento vivo: la vista d'insieme su come il pack tratta le piante delle mod, due mod alla volta. I fatti di una sola mod stanno nella sua scheda.

## Cose da non rompere

- **Una base dati sola** per vasi e mercato (`1.21.1/data/vasi/vasi.sqlite`, generata): le piante sono le stesse, i nomi anche. Tutto ciò che si pianta sta in `PIANTABILE`, costruita dai semi dei vasi e dai tag di alberelli e fiori; il mercato vende da lì. Un nome che cambia con un aggiornamento salta in un posto solo.
- **Le regole stanno nei CSV**, i file del datapack si generano: `data/vasi/*.csv` → `scripts/botanypots_genera.py`; `data/mercato/*.csv` → `scripts/mercato_genera.py`. Non si modificano i file generati a mano; la CI verifica che corrispondano alle regole.
- **La rarità ha un'anagrafica sola** (`data/rarita.csv`: 10 classi «natura» e 10 «craft-diff») e due specializzazioni: i bonus dei vasi (`vasi/rarita_pots_settings.csv`) e i moltiplicatori del mercato (`mercato/rarita_mercato_settings.csv`). Sono due scale per due cose diverse: un bonus continuo contro un biglietto d'ingresso pagato una volta sola (un seme comprato è infinito).
- **Nomi di mod e dimensioni in inglese** anche nei dati: le origini del mercato sono `overworld`, `nether`, `end`, `aether`, `undergarden`, `twilight`.

## Come si incastrano

| | Vasi (Botany Pots) | Mercato (Farming for Blockheads) |
|---|---|---|
| Cosa descrive un file | una coltura (seme → raccolto) o un terreno (bonus) | una voce (oggetto in vendita, categoria, listino) o un listino (moneta, quantità, acceso) |
| Il gioco sceglie per | l'oggetto nello slot del seme e del terreno | il listino della voce: deve esistere ed essere acceso |
| Il nostro datapack vince | sì, stesso percorso (Paxi in cima) | sì, anche per i listini delle mod |
| Progressione | bonus del terreno sommato a quello del vaso (`analisi.md`, sezione 1) | prezzo = base per origine e rarità × moltiplicatore; moneta della dimensione (`v0.6.2.md`) |
| Regole nostre | `coltura_*`, `terreno_*` | `mercato_*`, per mod, per tipo e per oggetto |

Il legame: `PIANTABILE.oggetto_id` = `POTS_COLTURA_SEME.seme` (entrambi → `OGGETTO`), quindi da una voce del mercato si arriva alla coltura, ai suoi terreni (`POTS_COMPATIBILITA`) e a quello che rende. I numeri di oggi: 652 piantabili (95 alberelli, 139 fiori, 62 selvatiche, 59 semi, 94 colture piantate con il prodotto, 26 funghi, 10 colonie, 167 piante decorative), 31 voci attive nel mercato delle mod.

## Da provare

Le prove dei vasi stanno in `v0.6.1.md` e in `../lavoro/0502-prove-in-gioco.md`; quelle del mercato in `v0.6.2.md`.
