# Hedging Set

This node defines hedging sets for SA-CCR add-on aggregation: one per currency for interest rate derivatives, one per currency pair for FX, single sets for credit and for equity, and four broad commodity sets (energy, metals, agricultural, other). It also carves out basis transactions and volatility transactions into separate hedging sets, with the supervisory factor halved for basis hedging sets, and shows the step-by-step effective notional and add-on calculation. It binds banks applying SA-CCR to derivative exposures.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Netting Set|Netting Set]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 47): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"

### [[SAMA — PFE Add-on|PFE Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 139): "Next, the hedging set level add-ons (𝐴𝑑𝑑𝑂𝑛ℎ𝑠) must be recalculated by multiplying the recalculated effective notionals of each hedging set (𝐸𝑁ℎ𝑠) by the prescribed supervisory factor of the hedging set (𝑆𝐹𝑈𝑆𝐷)."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 38): "(7) Step 7: Calculate the asset class level add-on (𝐴𝑑𝑑𝑂𝑛𝐼𝑅) by adding together all of the hedging set level add-ons calculated in step 6: 𝐴𝑑𝑑𝑂𝑛𝐼𝑅= ∑𝐴𝑑𝑑𝑂𝑛𝐻𝑆 𝐻𝑆 Add-on for foreign exchange derivatives 6.61."

## Lookup terms

`hedging set`, `basis transactions`, `volatility transactions`, `effective notional`, `asset class add-on`, `currency pair hedging set`, `commodity hedging sets`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
