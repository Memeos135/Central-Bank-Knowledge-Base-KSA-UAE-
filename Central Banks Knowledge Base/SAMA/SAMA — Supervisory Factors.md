# Supervisory Factors

This node describes the supervisory factor (SF) in SA-CCR — the supervisory-specified change in the underlying risk factor, calibrated to its volatility — used with aggregation formulas to convert effective notionals into hedging-set add-ons, with the values tabulated in the framework. It is presented together with the other effective notional inputs (adjusted notional, maturity factor, supervisory delta) and the rule halving the supervisory factor for basis-transaction hedging sets. It binds banks applying SA-CCR.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — PFE Add-on|PFE Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 34): "Supervisory factors (𝑆𝐹𝑖) are used, together with aggregation formulas, to convert effective notional amounts into the add-on for each hedging set.18 The way in which supervisory factors are used within the aggregation formulas varies between asset classes."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

## Lookup terms

`supervisory factor`, `supervisory delta`, `maturity factor`, `adjusted notional`, `effective notional`, `Table 2 supervisory factors`, `basis transaction half factor`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
