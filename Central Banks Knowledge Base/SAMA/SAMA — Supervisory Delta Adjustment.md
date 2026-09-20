# Supervisory Delta Adjustment

Concept node for the supervisory delta adjustment applied at trade level to adjusted notional amounts to reflect direction (long/short in the primary risk factor) and non-linearity of options and CDO tranches. It is a prescribed parameter set (including option formulas using supervisory volatility) within the standardised counterparty credit risk calculation. Binds banks determining derivative exposure amounts for capital and leverage ratio purposes under SAMA rules.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Aggregate Add-On|Aggregate Add-On]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 575): "In this case, for each asset class to which the position is allocated, banks must determine appropriately the sign and delta adjustment of the relevant risk driver (the role of delta adjustments in SA-CCR is outlined further in 6.32 below)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 573): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

### [[SAMA — Effective Notional|Effective Notional]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 575): "In this case, for each asset class to which the position is allocated, banks must determine appropriately the sign and delta adjustment of the relevant risk driver (the role of delta adjustments in SA-CCR is outlined further in 6.32 below)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 683): "Effective notional, 𝐷𝑖(USD, thousands) Maturity Factor, Trade # Notional (USD Adjusted notional, 𝑑𝑖 𝑀𝐹𝑖 Delta, 𝛿𝑖 thousands) (USD, thousands) 1 10,000 10,000 (9/12)0.5 1 8,660 2 20,000 20,000 1 -1 -20,000 3 10,000 10,000 1 1 10,000 12.48."

### [[SAMA — PFE Add-on|PFE Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 575): "In this case, for each asset class to which the position is allocated, banks must determine appropriately the sign and delta adjustment of the relevant risk driver (the role of delta adjustments in SA-CCR is outlined further in 6.32 below)."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

## Lookup terms

`supervisory delta`, `delta adjustment`, `long/short primary risk factor`, `option delta`, `CDO tranche delta`, `supervisory volatility`, `SA-CCR parameters`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
