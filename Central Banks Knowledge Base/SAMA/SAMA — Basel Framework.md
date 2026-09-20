# Basel Framework

This node reflects the Basel-derived calibration embedded in SAMA's market risk standard, including the simplified standardised approach for foreign exchange and commodities risk (8% of the overall net open position, gold treated as FX) and the sensitivities-based delta GIRR bucket structure, tenor risk weights and correlation parameters. It also records the de minimis FX exemption available at SAMA's discretion, referenced to eligible capital as defined in SAMA's Basel III regulatory capital guidance. It binds SAMA-licensed banks calculating market risk capital.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Sensitivities-Based Method|Sensitivities-Based Method]] — `cites` [EXTRACTED]
- **What this link tells you:** The sensitivities-based method as issued by SAMA is a domestic implementation of the Basel market risk standards, so interpretive questions about scope, risk classes and trading desk allocation should be read against the Basel Framework text that SAMA has adopted. The citation establishes the source hierarchy: Basel supplies the methodology, but SAMA's issuance is the enforceable requirement in the Kingdom, including any national discretions or calibrations. The reader should apply the SAMA text as binding and use Basel only as interpretive support, verifying the SAMA primary text where the two appear to diverge.
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 29): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

### [[SAMA — Stress Testing Programme|Stress Testing Programme]] — `cites` [INFERRED]
- **What this link tells you:** If a bank uses the internal models approach for market risk capital, the stress testing programme is not a discretionary risk-management practice but a condition embedded in the Basel-derived framework as adopted by SAMA. The framework text itself imposes the requirement at both trading desk and bank-wide level, so the stress testing node is a sub-obligation of the parent capital rules rather than a standalone standard. Consequently, a deficiency in the stress testing programme is capable of calling into question IMA eligibility itself, not merely triggering a risk-management finding.
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 96): "Stress testing 10.19 Banks that use the IMA for determining market risk capital requirements must have in place a rigorous and comprehensive stress testing programme both at the trading desk level and at the bank-wide level."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 96): "Stress testing 10.19 Banks that use the IMA for determining market risk capital requirements must have in place a rigorous and comprehensive stress testing programme both at the trading desk level and at the bank-wide level."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`Basel III implementation KSA`, `overall net open position`, `foreign exchange risk capital charge`, `commodities risk`, `delta GIRR buckets`, `risk weights and correlations`, `eligible capital`, `simplified standardised approach`

#graphify/enriched #source/sama #community/internal-models-approach
