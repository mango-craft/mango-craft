# Esperienza: scambio Create ↔ Cognition (0.6.3)

Due ricette del Mescolatore di Create che convertono i due liquidi dell'esperienza **senza perdite né guadagni**: 50 mB di `create_enchantment_industry:experience` (1 mB per punto) ↔ 1000 mB di `cognition:cognitium_source` (20 mB per punto). Sono 50 punti da entrambe le parti, e 1000 mB è la capienza di un serbatoio della bacinella (2 di ingresso e 2 di uscita da 1000 mB, `BasinBlockEntity` di Create): il lotto più grande possibile. Nessun calore richiesto.

- `create_in_cognitium.json`: esperienza di Create → cognitium (per portare l'esperienza prodotta da Create nell'Obelisco di Cognition).
- `cognitium_in_create.json`: cognitium → esperienza di Create (per alimentare incantatore e stampante di Create: accettano **solo** il loro liquido).

Condizioni: tutte e due le mod caricate. Gli altri liquidi dell'esperienza (quello degli zaini Sophisticated) passano prima dall'Obelisco, che li accetta e li restituisce come cognitium: le ricette usano solo i due liquidi esatti, mai l'etichetta `c:experience` (alcuni liquidi di quell'etichetta, come quello di CoFH, valgono 25 mB per punto).

**Nella stessa bacinella le due ricette fanno avanti e indietro**: le ricette della bacinella leggono anche i serbatoi di uscita, quindi il risultato di una viene ripreso dall'altra. Non si crea né si perde esperienza, ma l'uscita cambia liquido a ogni ciclo e un tubo può prendere quello sbagliato. Per convertire in un verso solo, mettere nel **filtro della bacinella** il secchio del liquido da ottenere (`cognition:cognitium_bucket` oppure `create_enchantment_industry:experience_bucket`): la ricetta parte solo se il suo risultato passa il filtro. Scelta del 24/10/2026 (`1.21.1/lavoro/versioni/v0.6.3.md`).

**Mai** unire i liquidi per etichetta o per config: esperienza ×20 o −95%. Regola in `1.21.1/docs/0303-note-tecniche.md`; fatti e schema della base nel tema `1.21.1/theme-knowledge/esperienza.md`. Il terzo file della versione è `data/create_enchantment_industry/data_maps/fluid/unit/experience.json` (readme in `data/create_enchantment_industry/`).
