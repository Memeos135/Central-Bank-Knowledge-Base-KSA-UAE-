# ISO 17442 Legal Entity Identifier

Defines the identification standard used across the SAMA OTC derivatives reporting templates: parties, brokers and clearing members are identified by a 20-character ISO 17442 Legal Entity Identifier, with prescribed client-code fallbacks for natural persons (national ID or country code plus national ID) and for KSA corporates without an LEI (country code plus commercial registration number). Country of the other counterparty is reported using ISO 3166 two-character codes. Binds reporting banks completing trade repository submissions.

**Regimes:** data/credit info, banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[SAMA — Counterparty Data Reporting (Appendix A Table 1)|Counterparty Data Reporting (Appendix A Table 1)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 49): "Section 2;— | Reference entity | Identification of the underlying reference | ISO 3166 - 2 character country code Credit entity (issuer of the debt that uderlines a credit | or derivatives derivative) ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code or For"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 55): "If the reporting counterparty (or the other counterparty upon communication to the reporting counterparty) detects that a report (no matter its nature or “Action type”) was submitted by error, the reporting counterparty is required to submit an error report (table 2 item 53 “Acti"

## Lookup terms

`ISO 17442 Legal Entity Identifier`, `LEI 20 alphanumeric`, `client code CLC`, `National Identification Number NIN`, `commercial registration number CR`, `ISO 3166 country code`, `counterparty identification format`

#graphify/enriched #source/sama #community/counterparty-data-reporting
