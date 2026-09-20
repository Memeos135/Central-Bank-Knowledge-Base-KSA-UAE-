# Credit Spread Risk (CSR)

Concept node for Credit Spread Risk (CSR), a defined market risk class (split into non-securitisation, securitisation non-correlation trading portfolio and correlation trading portfolio) and also a delta/vega risk class within the standardised CVA (SA-CVA) capital calculation, where it separates counterparty credit spread from reference credit spread. It governs classification of spread-sensitive positions and eligible hedges for capital purposes, including the rule that a hedge must sit wholly in one spread risk class. Binds banks computing market risk and CVA capital requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Correlation Trading Portfolio (CTP)|Correlation Trading Portfolio (CTP)]] — `references` [EXTRACTED]
- **What this link tells you:** When classifying a trading-book position for market risk capital, the credit spread risk class is not a single bucket: the framework splits it by whether the exposure is non-securitisation, securitisation outside the correlation trading portfolio, or securitisation within the CTP. The link reflects that the CTP is a defined term used to partition CSR, so the CTP definition determines which CSR treatment and risk weights apply. For a decision, confirm the CTP scope test first, because misclassifying a securitisation position as inside or outside the CTP changes the capital outcome, not just the label.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Sensitivities-Based Method|Sensitivities-Based Method]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

## Lookup terms

`Credit Spread Risk`, `CSR non-securitisation`, `correlation trading portfolio`, `counterparty credit spread`, `reference credit spread`, `SA-CVA delta risk`, `eligible CVA hedge`, `CVA multiplier`

#graphify/enriched #source/sama #community/sensitivities-based-market-risk
