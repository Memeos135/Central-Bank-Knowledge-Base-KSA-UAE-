# Add-on for Interest Rate Derivatives

A component of the CBUAE counterparty credit risk standard setting out how the potential future exposure add-on is built for interest rate derivatives: contracts are sorted into three remaining-maturity buckets, and effective notional amounts are derived per currency hedging set from adjusted notional, supervisory delta and maturity factor. It also frames the general rule that basis and volatility transactions sit in their own hedging sets within each asset class. It binds banks calculating regulatory capital for derivative exposures.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Adjusted Notional Amount|Adjusted Notional Amount]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 130): "Interest rate derivatives Interest rate risk calculations for market risk capital should include all interest rate derivatives and off-balance-sheet instruments held in the trading book that respond to changes in interest rates."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 61): "The bank must then calculate the effective notional amount for each interest rate derivative hedging set (that is, for the set of interest rate derivatives in any single currency) by summing across transactions within a maturity category the product of the adjusted notional amoun"

### [[CBUAE — Hedging Set|Hedging Set]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 60): "Banks must allocate every transaction within each netting set to a hedging set according to the following rules for each asset class: a) Interest Rate Derivatives: A hedging set must be created for each set of interest rate derivatives that reference interest rates of the same cu"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 60): "Banks must allocate every transaction within each netting set to a hedging set according to the following rules for each asset class: a) Interest Rate Derivatives: A hedging set must be created for each set of interest rate derivatives that reference interest rates of the same cu"

## Lookup terms

`interest rate derivatives add-on`, `SA-CCR`, `hedging set`, `maturity category`, `effective notional amount`, `supervisory delta adjustment`, `maturity factor`, `potential future exposure`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
