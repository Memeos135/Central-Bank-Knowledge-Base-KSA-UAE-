# Aggregate Add-On

Defines the aggregate add-on component of the potential future exposure (PFE) calculation under SA-CCR, combined with a multiplier that recognises excess collateral or negative mark-to-market within a netting set, alongside the replacement cost formula using threshold, minimum transfer amount and net independent collateral amount. It explains why the calculation is floored at zero and how over-collateralisation reduces counterparty credit risk capital. It binds banks computing counterparty credit risk exposures under SAMA's SA-CCR rules.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — EAD Calculation under SA-CCR|EAD Calculation under SA-CCR]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 573): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 333): "This includes, for example, any underlying exposure arising from the fund’s derivatives activities for situations in which the underlying receives a risk weighting treatment under the calculation of minimum risk based capital requirements and the associated counterparty credit ri"

### [[SAMA — Maturity Factor|Maturity Factor]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 573): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

### [[SAMA — Supervisory Delta Adjustment|Supervisory Delta Adjustment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 573): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 575): "In this case, for each asset class to which the position is allocated, banks must determine appropriately the sign and delta adjustment of the relevant risk driver (the role of delta adjustments in SA-CCR is outlined further in 6.32 below)."

## Lookup terms

`aggregate add-on`, `AddOn aggregate`, `potential future exposure`, `PFE multiplier`, `SA-CCR replacement cost`, `NICA`, `minimum transfer amount`, `netting set`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
