# Hedging Set

Concept node for the hedging set, the grouping level within a netting set used to aggregate derivative trade-level inputs when computing the potential future exposure add-on under the standardised counterparty credit risk approach. It sets the allocation rules per asset class (e.g. one hedging set per currency for interest rate derivatives, with maturity-category subdivision and offset rules), and requires basis transactions and volatility transactions to sit in their own distinct hedging sets. It binds banks calculating counterparty credit risk exposure amounts under the CBUAE capital standards.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Add-on for Commodity Derivatives|Add-on for Commodity Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "Specifically, the bank must calculate the add-on for each of the four commodity derivative hedging sets by calculating: 2 + ∑((1 −𝜌2) × 𝐴𝑖 2) 𝑖 𝐻𝑒𝑑𝑔𝑖𝑛𝑔 𝑆𝑒𝑡 𝐴𝑑𝑑𝑂𝑛= √(∑𝜌× 𝐴𝑖 ) 𝑖 where ρ is the supervisory correlation factor for commodity derivatives, and Ai is the add-on for one co"

### [[CBUAE — Add-on for Credit Derivatives|Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."

### [[CBUAE — Add-on for Equity Derivatives|Add-on for Equity Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."

### [[CBUAE — Add-on for Foreign Exchange Derivatives|Add-on for Foreign Exchange Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 62): "The bank must multiply the absolute value of the resulting effective notional amount for each hedging set (each currency pair) by the supervisory factor for the foreign exchange asset class from Table 2, and sum across all foreign exchange hedging sets to calculate the aggregate "
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 62): "The bank must multiply the absolute value of the resulting effective notional amount for each hedging set (each currency pair) by the supervisory factor for the foreign exchange asset class from Table 2, and sum across all foreign exchange hedging sets to calculate the aggregate "

### [[CBUAE — Add-on for Interest Rate Derivatives|Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 60): "Banks must allocate every transaction within each netting set to a hedging set according to the following rules for each asset class: a) Interest Rate Derivatives: A hedging set must be created for each set of interest rate derivatives that reference interest rates of the same cu"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 60): "Banks must allocate every transaction within each netting set to a hedging set according to the following rules for each asset class: a) Interest Rate Derivatives: A hedging set must be created for each set of interest rate derivatives that reference interest rates of the same cu"

### [[CBUAE — Potential Future Exposure|Potential Future Exposure]] — `references` [EXTRACTED]
- **What this link tells you:** Hedging set classification is the decision that determines how much offsetting is recognised inside the PFE add-on, so it must be justified per netting set. The rules grouping transactions by asset class and common risk factors exist to drive the aggregation step of the add-on, not as a standalone taxonomy. Misallocating a trade to the wrong hedging set therefore distorts PFE and flows through to counterparty credit risk exposure and the derivative component of the leverage exposure measure.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 61): "CBUAE Classification: Public a) All basis transactions in a netting set that belong to the same asset class and reference the same pair of risk factors form a single hedging set, and follow the hedging set aggregation rules for the relevant asset class."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."

## Lookup terms

`hedging set`, `netting set`, `SA-CCR`, `potential future exposure add-on`, `basis transactions`, `volatility transactions`, `maturity category`, `asset class allocation`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
