# Action Type / Life Cycle Events

Explains the action-type codes and life-cycle reporting scenarios for OTC derivative transactions reported to the SAMA-authorised trade repository: new trades (N), modifications (M) including late population of a UTI and notional increases/decreases, terminations/early terminations (C), and error reports (E) to eliminate erroneous submissions, each keyed to a previously reported internal unique trade ID. It also frames the scope of reportable transactions, including novations for central clearing and booking transfers into a KSA branch, while excluding spot FX, interbranch and intrabranch transactions. Binds SAMA-licensed reporting banks.

**Regimes:** banking prudential, governance/risk, other

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[SAMA — Common Data Reporting (Appendix A Table 2)|Common Data Reporting (Appendix A Table 2)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 55): "If the reporting counterparty (or the other counterparty upon communication to the reporting counterparty) detects that a report (no matter its nature or “Action type”) was submitted by error, the reporting counterparty is required to submit an error report (table 2 item 53 “Acti"

### [[SAMA — Unique Trade Identifier|Unique Trade Identifier]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 25): "Until a global Unique transaction identifier (UTI) is available, an internal unique trade identifier code shall be generated."

## Lookup terms

`action type N M C E`, `life cycle events reporting`, `novation reporting`, `early termination report`, `error report / correction`, `notional increase or decrease`, `reportable transactions scope`, `interbranch and intrabranch exclusion`, `spot FX exclusion`

#graphify/enriched #source/sama #community/otc-derivatives-reporting
