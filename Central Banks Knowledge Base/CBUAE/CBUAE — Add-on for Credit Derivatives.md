# Add-on for Credit Derivatives

Concept node for the credit derivative add-on in the counterparty credit risk calculation: effective notional amounts are computed per reference entity or index from adjusted notional, maturity factor and supervisory delta, then scaled by the rating-dependent supervisory factor, with unrated single names treated at the BBB factor. Related context addresses the treatment of written credit derivatives and offsetting purchased protection for leverage ratio exposure purposes, including when pool-level protection may offset single-name protection sold. It binds banks measuring derivative exposures and leverage ratio exposure.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Adjusted Notional Amount|Adjusted Notional Amount]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 62): "That is, for each individual credit derivative referencing any single entity, the bank must calculate: Adjusted Notional Amount × Supervisory Delta Adjustment × MF for each transaction and then sum that product across all credit derivatives that reference that entity to get the e"

### [[CBUAE — Hedging Set|Hedging Set]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."

### [[CBUAE — Maturity Factor (MF)|Maturity Factor (MF)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 91): "Tranche maturity (MT) Tranche maturity is a tranche’s remaining effective maturity in years, calculated in one of the following two ways, subject to a floor of one year and a cap of five years: (a) Weighted-average maturity, calculated as the weighted-average maturity of the cont"

### [[CBUAE — Supervisory Delta Adjustment|Supervisory Delta Adjustment]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 50): "Supervisory Delta Adjustment Question D1: What is the Supervisory Delta for FX Swaps and FX Forwards?"

### [[CBUAE — Supervisory Factors and Correlations (Table 2)|Supervisory Factors and Correlations (Table 2)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "Table 2 provides the values of Supervisory Factors, correlations, and supervisory option volatilities for use with each asset class and subclass."

## Lookup terms

`credit derivative add-on`, `written credit derivative`, `effective notional amount`, `single name and index credit derivatives`, `unrated entity BBB factor`, `leverage ratio exposure measure`, `credit protection offset`, `reference entity`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
