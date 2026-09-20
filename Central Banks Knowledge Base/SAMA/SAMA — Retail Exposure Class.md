# Retail Exposure Class

This node defines the retail exposure class under SAMA's credit risk standardized approach, comprising exposures to individuals and to MSMEs meeting the "regulatory retail" criteria (product type, an aggregate exposure cap of SAR 4.46 million per counterparty, and a 0.2% granularity limit), while excluding real estate exposures. It distinguishes regulatory retail exposures to "transactors" (45% risk weight) from other regulatory retail (75%) and "other retail" (100%). It binds SAMA-licensed banks in classifying and risk-weighting retail credit.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Currency Mismatch Risk Weight Multiplier|Currency Mismatch Risk Weight Multiplier]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 32): "Retail exposure class 7.55 The retail exposure class excludes exposures within the real estate exposure class."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 168): "Risk-weighted assets for default risk 14.2 For receivables belonging unambiguously to one asset class, the IRB risk weight for default risk is based on the risk-weight function applicable to that particular exposure type, as long as the bank can meet the qualification standards f"

### [[SAMA — Regulatory Retail Exposures|Regulatory Retail Exposures]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 98): "10.21 Within the retail asset class category, banks are required to identify separately three sub-classes of exposures: (1) Residential mortgage loans, as defined above; (2) Qualifying revolving retail exposures, as defined in the following paragraph; and (3) All other retail exp"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 98): "10.21 Within the retail asset class category, banks are required to identify separately three sub-classes of exposures: (1) Residential mortgage loans, as defined above; (2) Qualifying revolving retail exposures, as defined in the following paragraph; and (3) All other retail exp"

## Lookup terms

`retail exposure class`, `regulatory retail criteria`, `transactors definition`, `granularity criterion 0.2%`, `SAR 4.46 million threshold`, `other retail exposures`, `75% retail risk weight`, `credit cards and overdrafts risk weight`

#graphify/enriched #source/sama #community/irb-retail-exposures
