# Supervisory Discount Factor (DF)

Worked-example material from CBUAE guidance showing how derivative exposure add-ons are built: supervisory duration and adjusted notional, supervisory delta (+1 long / -1 short for linear trades), maturity factor scaling for sub-one-year un-margined trades, effective notional aggregation, and supervisory factors by asset class (e.g. rating-based factors for single-name credit, investment-grade treatment for CDS indices) with hedging sets and offsetting rules for commodities. Binds banks calculating counterparty credit risk exposure on derivatives. Open it for numerical illustration of the parameters rather than for the underlying rule text.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — Single-Name Exposure (SNE)|Single-Name Exposure (SNE)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 73): "DF is a supervisory discount factor, described further below.) In effect, the discounted value of the individual counterparty exposure is offset by the discounted value of eligible single-name CVA hedges for that counterparty."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 74): "For each counterparty, the bank should calculate single-name exposure (SNE) as the discounted counterparty exposure minus the discounted value of eligible single-name CVA hedges."

## Lookup terms

`supervisory factor`, `supervisory duration`, `supervisory delta`, `adjusted notional`, `maturity factor`, `effective notional`, `hedging set`, `add-on`, `SA-CCR worked example`

#graphify/enriched #source/cbuae #community/cva-capital-calculation
