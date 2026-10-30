# Piano — Minecraft 1.21.1

Le tappe del pack verso il mondo vero e lo stato di avanzamento. Documento vivo: si aggiorna a ogni tappa. Regole (rami, tag, prove, mondo vero): `AGENTS.md`, sezione 5. Cosa è uscito: `../docs/0401-changelog.md`; il perché di ogni versione: `versioni/` (indice in [`README.md`](README.md)); cosa c'è nel pack: `../docs/0301-mod.md`.

## Tappe

**Fatte**: le tappe 0–6.4, dalla 0.2.3 alla 0.7.4 (18–30/10/2026), tutte provate e rilasciate come pre-release; la 0.7.1 è uscita dentro la 0.7.2, senza un tag suo.

| Tappa | Versione | Contenuto | Stato |
|---|---|---|---|
| 6.5 | [0.7.5](versioni/v0.7.5.md) | **Archeologia e reperti**: tabelle del bottino nella base dati (inventario esteso, ramo «bottino»), analisi delle tabelle di scavo di tutte le mod, poi i tesori delle casse di Better Archeology nella toppa delle reliquie e i miglioramenti decisi, con file generati (tema `../theme-knowledge/archeologia.md`). Contenuto e approccio decisi da Matteo il 24/10 | 🔧 aperta il 30/10 |
| 7 e oltre | — | Il resto, nella proposta qui sotto: eventuali 0.7.x (strumenti a tappe, terreno), progressione (0.8); poi le **fasi senza numero**: aggiornamenti e licenze, **mondo di prova**, correzioni, mondo vero | da fare |

NeoForge è a 21.1.265 dalla 0.7.4 (`../docs/0303-note-tecniche.md`). Se una mod nuova ne chiede uno più recente, il controllo dei nomi lo segnala.

## Proposta per dopo la 0.7.3 (25/10/2026, in sospeso)

Matteo approva una versione alla volta: quando ne approva una, la sua riga passa nella tabella qui sopra. Il 25/10 ha deciso: gli **strumenti a tappe** sono da esplorare (una 0.7.x senza numero fisso), la **progressione** è il tema della **0.8**, le fasi dopo **non hanno un numero**. Negli altri documenti il mondo di prova si chiama per nome.

**Ordine**: prima il contenuto (0.7.x), poi la progressione (0.8), poi gli aggiornamenti, poi il mondo di prova, che deve girare con il pack **finale** (`0503`, sezione 4, n. 5). La progressione viene dopo i contenuti perché la scheda «Mango Craft» descrive le tappe fatte prima.

### Versioni proposte

| Versione | Contenuto | Cosa decide Matteo | Prove di uscita |
|---|---|---|---|
| **0.7.x** | 🟡 **Strumenti a tappe**, da esplorare (Matteo, 25/10): tabella dei materiali di Truly Modular e materiali scritti a mano per i gradini (`0503`, sezione 5); la stessa scala può servire alle ricette di fornaci e computer | se farla, e i gradini | i materiali nostri compaiono in Truly Modular |
| **0.7.x** | 🟡 Solo se Matteo lo decide: mod che cambiano il terreno (Tectonic, con StructBlend) o Malum se esce la 1.9 (`0601`) | sì o no, **prima** del mondo di prova | mondo nuovo: biomi e strutture sensati, nessun errore |
| **0.8** | **Progressione** (anche in più versioni 0.8.x): una mod per la schermata dei progressi (🟢 Reliable Advancements o Lucid Advancements, provate una alla volta), gli effetti nuovi della luna di sangue, 🟡 scheda «Mango Craft» (20–40 traguardi nel datapack) e guida del pack (`0503`, sezione 3) | quale mod; gli effetti della luna; se fare la scheda e quanti traguardi | la schermata mostra i progressi; i traguardi si sbloccano; luna di sangue come deciso |

### Fasi senza numero (in quest'ordine)

| Fase | Contenuto | Cosa decide Matteo |
|---|---|---|
| **Aggiornamenti e licenze** | Workflow che elenca le versioni nuove senza installarle, giro di aggiornamenti, controllo delle licenze; dopo, si rifanno inventario, dump del gioco e base dati | quali mod aggiornare |
| **Mondo di prova** | Le prove della sezione «Mondo di prova» di `0502`, difficoltà, slot degli accessori se stretti, B33 con 12 GB | le decisioni aperte di `0503`, sezione 4 (tasti, lingua…), prima |
| **Correzioni** | Quello che il mondo di prova trova, una versione per volta | cosa correggere subito e cosa dopo |
| **Mondo vero** | Con la versione 0.x che supera la soglia (`0503`, sezione 4, n. 5) | l'OK finale |
| **1.0.0** | Quando il pack è stato giocato a lungo nel mondo vero ed è stabile | quando |
