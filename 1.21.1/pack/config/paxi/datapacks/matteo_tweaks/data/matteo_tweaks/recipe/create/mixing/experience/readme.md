# Esperienza: scambio Create ↔ Cognition (0.6.3)

Due ricette del Mescolatore di Create che convertono i due liquidi dell'esperienza **senza perdite né guadagni**: 50 mB di `create_enchantment_industry:experience` (1 mB per punto) ↔ 1000 mB di `cognition:cognitium_source` (20 mB per punto). Sono 50 punti da entrambe le parti, e 1000 mB è la capienza di un serbatoio della bacinella (2 di ingresso e 2 di uscita da 1000 mB, `BasinBlockEntity` di Create): il lotto più grande possibile. Nessun calore richiesto.

- `create_in_cognitium.json`: esperienza di Create → cognitium (per portare l'esperienza prodotta da Create nell'Obelisco di Cognition).
- `cognitium_in_create.json`: cognitium → esperienza di Create (per alimentare incantatore e stampante di Create: accettano **solo** il loro liquido).

Condizioni: tutte e due le mod caricate. Gli altri liquidi dell'esperienza (quello degli zaini Sophisticated) passano prima dall'Obelisco, che li accetta e li restituisce come cognitium: le ricette usano solo i due liquidi esatti, mai l'etichetta `c:experience` (alcuni liquidi di quell'etichetta, come quello di CoFH, valgono 25 mB per punto).

**Mai** unire i liquidi per etichetta o per config: esperienza ×20 o −95%. Regola in `1.21.1/docs/0303-note-tecniche.md`; fatti e schema della base nel tema `1.21.1/theme-knowledge/esperienza.md`. Il terzo file della versione è `data/create_enchantment_industry/data_maps/fluid/unit/experience.json` (readme in `data/create_enchantment_industry/`).
