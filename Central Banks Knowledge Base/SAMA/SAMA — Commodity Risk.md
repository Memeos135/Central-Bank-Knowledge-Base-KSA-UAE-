# Commodity Risk

Concept node for commodity risk, one of the defined market risk classes used to calculate market risk capital requirements and expressly included, together with FX risk, within the market risk capital scope even when arising in the banking book for internal risk transfer purposes. It governs identification of commodity risk positions and their capital treatment under the sensitivities-based and simplified standardised approaches. Binds banks holding commodity exposures subject to SAMA minimum capital requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Maturity Ladder Approach|Maturity Ladder Approach]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 515): "Maturity ladder approach 14.68 In calculating the capital requirements under the maturity ladder approach, banks will first have to express each commodity position (spot plus forward) in terms of the standard unit of measurement (barrels, kilos, grams etc)."

### [[SAMA — Sensitivities-Based Method|Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank decides how to capitalise commodity exposures in the trading book, the sensitivities-based method is the calculation engine and commodity risk is one of the prescribed risk classes fed into it. The link is definitional and hierarchical: the market risk framework fixes a closed list of risk classes, and the sensitivities-based method applies delta, vega and curvature charges to instruments within each class. Practically, commodity positions cannot be capitalised under a bespoke bucket — they must be mapped to the commodity risk class and run through the sensitivities-based method's prescribed risk weights and correlations.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

### [[SAMA — Simplified Standardised Approach|Simplified Standardised Approach]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 846): "22.2.3 Market risk under the simplified standardised approach (SSA) Table MR3: Market risk under the simplified standardised approach Purpose: Provide the components of the capital requirement under the simplified standardised approach for market risk."

## Lookup terms

`commodity risk`, `commodities risk in the banking book`, `risk class`, `CR_COMM`, `sensitivities-based method`, `internal risk transfer`, `delta and vega commodity risk`

#graphify/enriched #source/sama #community/options-&-simplified-market-risk
