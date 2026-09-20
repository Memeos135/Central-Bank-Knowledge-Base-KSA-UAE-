# Supervisory Delta Adjustment

Concept node for the supervisory delta adjustment, the prescribed directional/optionality multiplier applied to each derivative's adjusted notional and maturity factor to produce the effective notional amount for a hedging set or reference entity. It is used consistently across interest rate, foreign exchange, credit, equity and commodity asset classes in the counterparty credit risk add-on formulas. It binds banks calculating derivative exposure amounts under the CBUAE capital framework.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`
- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — Add-on for Credit Derivatives|Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 50): "Supervisory Delta Adjustment Question D1: What is the Supervisory Delta for FX Swaps and FX Forwards?"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."

### [[CBUAE — Adjusted Notional Amount|Adjusted Notional Amount]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 62): "CBUAE Classification: Public Adjusted Notional Amount × Supervisory Delta Adjustment × MF and then sum that product across all foreign exchange derivatives in that hedging set to get the effective notional amount for the hedging set."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 62): "CBUAE Classification: Public Adjusted Notional Amount × Supervisory Delta Adjustment × MF and then sum that product across all foreign exchange derivatives in that hedging set to get the effective notional amount for the hedging set."

### [[CBUAE — Potential Future Exposure (PFE)|Potential Future Exposure (PFE)]] — `references` [EXTRACTED]
- **What this link tells you:** Use the supervisory delta guidance as the parameter source whenever you calculate a PFE add-on, particularly for FX swaps and forwards where direction and sign are contested. The delta adjustment scales each trade's adjusted notional before aggregation, so it is an embedded input to the add-on rather than a separate step, and the clarification instrument governs how the capital standard is applied. The consequence is that adopting a different delta convention changes PFE, EAD and downstream capital outcomes; confirm against the primary text which product types the clarification covers, as the linked provision also addresses securities financing exposures measured without a PFE add-on.
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 50): "Supervisory Delta Adjustment Question D1: What is the Supervisory Delta for FX Swaps and FX Forwards?"
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 201): "When a bank acts as a principal, its SFT exposure is the sum of gross SFT assets (subject to adjustments) and a measure of counterparty credit risk calculated as the current exposure without an add-on for potential future exposure."

### [[CBUAE — Supervisory Factors and Correlations (Table 2)|Supervisory Factors and Correlations (Table 2)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 50): "Supervisory Delta Adjustment Question D1: What is the Supervisory Delta for FX Swaps and FX Forwards?"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "Table 2 provides the values of Supervisory Factors, correlations, and supervisory option volatilities for use with each asset class and subclass."

## Lookup terms

`supervisory delta adjustment`, `effective notional amount`, `delta`, `add-on calculation`, `entity-level add-on`, `supervisory correlation`, `credit derivative add-on`, `equity derivative add-on`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
