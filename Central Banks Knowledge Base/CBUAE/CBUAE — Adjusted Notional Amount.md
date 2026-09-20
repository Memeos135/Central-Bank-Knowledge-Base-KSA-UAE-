# Adjusted Notional Amount

Concept node for the adjusted notional amount, the trade-level input used in the add-on calculation for counterparty credit risk. For interest rate and credit derivatives it is the trade notional scaled by a supervisory duration based on the start and end dates of the referenced period, and it includes specific rules for determining trade notionals for state-contingent payoffs, formula-based notionals, variable-notional and leveraged swaps, and multiple principal exchanges. It applies to banks computing exposure at default for derivative transactions.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Add-on for Credit Derivatives|Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 62): "That is, for each individual credit derivative referencing any single entity, the bank must calculate: Adjusted Notional Amount × Supervisory Delta Adjustment × MF for each transaction and then sum that product across all credit derivatives that reference that entity to get the e"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."

### [[CBUAE — Add-on for Interest Rate Derivatives|Add-on for Interest Rate Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 61): "The bank must then calculate the effective notional amount for each interest rate derivative hedging set (that is, for the set of interest rate derivatives in any single currency) by summing across transactions within a maturity category the product of the adjusted notional amoun"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 130): "Interest rate derivatives Interest rate risk calculations for market risk capital should include all interest rate derivatives and off-balance-sheet instruments held in the trading book that respond to changes in interest rates."

### [[CBUAE — Supervisory Delta Adjustment|Supervisory Delta Adjustment]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 62): "CBUAE Classification: Public Adjusted Notional Amount × Supervisory Delta Adjustment × MF and then sum that product across all foreign exchange derivatives in that hedging set to get the effective notional amount for the hedging set."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 62): "CBUAE Classification: Public Adjusted Notional Amount × Supervisory Delta Adjustment × MF and then sum that product across all foreign exchange derivatives in that hedging set to get the effective notional amount for the hedging set."

## Lookup terms

`adjusted notional amount`, `trade notional`, `supervisory duration`, `SD formula`, `amortising and accreting swaps`, `leveraged swaps`, `digital options`, `primary risk driver asset class`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
