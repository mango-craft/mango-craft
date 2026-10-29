# Sparse Structures

Aggiornata il 29/10/2026 · nel pack dalla 0.1.1 con il file `config/sparsestructures.json5` (cosa contiene: `../docs/0302-config.md`) · fonti: sorgente della 3.0 per la 1.21.5 (tag v3.0 @6cc5bf6; quello della versione per la 1.21.1 non è pubblico), file del pack.

## Cose da non rompere

- Il file va sempre portato **completo** (`spreadFactor`, `idBasedSalt`, `customSpreadFactors`): è letto con Gson in una classe senza valori di serie, quindi se manca `spreadFactor` vale 0 e **spariscono tutte le strutture**, se manca l'elenco il gioco va in errore.

## Fatti verificati

- `customSpreadFactors` accetta `{"structure": "<gruppo o struttura>", "factor": n}` (la descrizione su Modrinth dice `name`: è sbagliata); con il nome di una struttura cambia tutto il suo gruppo. I fattori sono rispetto ai valori originali, **non** si moltiplicano con quello generale; vince la prima voce che corrisponde; fattore 0 = frequenza 0; i gruppi ad anelli concentrici (fortezze dell'End) sono saltati; una virgola finale nell'elenco diventa una voce nulla, ignorata.
- Serve un riavvio; le distanze cambiano solo nei chunk nuovi.
- **Verificato nel gioco** (dump del 29/10/2026, `strutture.json` → tabella `GIOCO_STRUTTURA_SET`): i valori modificati si leggono dagli insiemi di strutture stessi, quindi il dump mostra le distanze finali. Con `spreadFactor` 1,4: città antiche 24/8 → 33/11, avamposti 32/8 → 44/11; ville 34/8 invariate (fattore 1); dimore 80/20 → 160/40 (fattore 2). 288 insiemi, 19 senza spaziatura (anelli concentrici e piazzamenti propri delle mod: Twilight Forest, Aquamirae, YUNG's).
- Comandi utili: `/dumpstructuresets` (scrive un file con tutti i gruppi), `/locate structure nova_structures:` + Tab.
- Regolazione struttura per struttura (Witch Villa e Swamp Village di Dungeons and Taverns a 3, When Dungeons Arise a 2) rimandata al mondo di prova (`../lavoro/0501-piano.md`).
