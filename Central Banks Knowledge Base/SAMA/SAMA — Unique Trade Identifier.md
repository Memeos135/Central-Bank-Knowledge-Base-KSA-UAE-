# Unique Trade Identifier

Sets out the trade identifier convention for SAMA trade repository reporting: pending a global UTI, an internal unique trade identifier must be generated (prefix plus the generating entity's LEI plus a unique code), unique to each OTC derivative contract and unchangeable once reported. Where the other counterparty is international, or where a CCP, clearing member or electronic confirmation platform is agreed as generating entity, that entity generates the UTI and must communicate it in time for the reporting counterparty to meet its deadline. Binds reporting banks and shapes their arrangements with foreign counterparties and clearing infrastructure.

**Regimes:** banking prudential, governance/risk, data/credit info

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[SAMA — Action Type  Life Cycle Events|Action Type / Life Cycle Events]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 25): "Until a global Unique transaction identifier (UTI) is available, an internal unique trade identifier code shall be generated."
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"

### [[SAMA — Common Data Reporting (Appendix A Table 2)|Common Data Reporting (Appendix A Table 2)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 8): "After an original trade is novated for central clearing, the reporting bank should report the open trade as an early termination business events and open a new one with the reference to the old trade identifier in the field “Linked UTI” (table 3 item 47) as specified in the Appen"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 8): "After an original trade is novated for central clearing, the reporting bank should report the open trade as an early termination business events and open a new one with the reference to the old trade identifier in the field “Linked UTI” (table 3 item 47) as specified in the Appen"

## Lookup terms

`Unique Trade Identifier UTI`, `internal unique trade ID`, `generating entity`, `UTI generation rules`, `CCP / clearing member UTI`, `electronic confirmation platform`, `52 character alphanumeric code`

#graphify/enriched #source/sama #community/otc-derivatives-reporting
