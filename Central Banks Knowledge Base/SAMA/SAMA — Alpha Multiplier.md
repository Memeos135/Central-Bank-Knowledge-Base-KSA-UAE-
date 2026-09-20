# Alpha Multiplier

Concept node for the alpha multiplier used in the internal models method (IMM) for counterparty credit risk, where exposure at default equals alpha times Effective EPE. It fixes alpha at 1.4, permits SAMA to impose a higher value based on a bank's CCR exposure profile (e.g. low counterparty granularity, general wrong-way risk, high correlation of market values), and allows bank-specific internal estimates subject to prior SAMA approval and a 1.2 floor. Binds SAMA-supervised banks calculating regulatory capital for counterparty credit risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — Effective Expected Positive Exposure (EPE)|Effective Expected Positive Exposure (EPE)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 560): "Expected positive exposure (EPE) The weighted average over time of effective expected exposure over the first year, or, if all the contracts in the netting set mature before one year, over the time period of the longest maturity contract in the netting set where the weights are t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 560): "Expected positive exposure (EPE) The weighted average over time of effective expected exposure over the first year, or, if all the contracts in the netting set mature before one year, over the time period of the longest maturity contract in the netting set where the weights are t"

### [[SAMA — Internal Models Method (IMM)|Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 538): "7.3 The Internal Loss Multiplier: 7.3.1 A bank’s internal operational risk loss experience affects the calculation of operational risk capital through the Internal Loss Multiplier (ILM)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 597): "Internal models method for counterparty credit risk Approval to adopt an internal models method to estimate EAD 7.1."

## Lookup terms

`alpha multiplier`, `alpha 1.4`, `Effective EPE`, `internal models method`, `IMM EAD`, `own estimates of alpha`, `alpha floor 1.2`, `counterparty credit risk capital`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
