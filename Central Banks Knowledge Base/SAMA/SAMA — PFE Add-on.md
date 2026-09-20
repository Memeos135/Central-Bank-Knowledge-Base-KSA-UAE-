# PFE Add-on

This node defines the potential future exposure (PFE) add-on used in SA-CCR, comprising an aggregate add-on component and a multiplier recognising excess collateral or negative mark-to-market within a netting set. It sits alongside the replacement cost formula (including threshold, minimum transfer amount and net independent collateral amount, floored at zero) and is illustrated by worked hedging-set aggregation examples such as the commodity asset class. It applies to banks calculating counterparty credit risk exposure under SA-CCR.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Derivative Exposures Treatment|Derivative Exposures Treatment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[SAMA — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** If you are validating a bank's counterparty credit risk capital numbers, you cannot assess the exposure-at-default figure in isolation: for derivative and long-settlement transactions the EAD is built from a replacement cost element plus a potential future exposure component, and the PFE add-on rules supply the aggregate add-on and multiplier that drive that second element. The two instruments therefore sit in one obligation chain — the EAD definition sets what must be measured, the PFE add-on provisions set how part of it is calculated. Practically, an error or unapproved simplification in the add-on aggregation or multiplier treatment flows straight through to reported EAD and risk-weighted assets, so both texts must be checked together.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[SAMA — Hedging Set|Hedging Set]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 38): "(7) Step 7: Calculate the asset class level add-on (𝐴𝑑𝑑𝑂𝑛𝐼𝑅) by adding together all of the hedging set level add-ons calculated in step 6: 𝐴𝑑𝑑𝑂𝑛𝐼𝑅= ∑𝐴𝑑𝑑𝑂𝑛𝐻𝑆 𝐻𝑆 Add-on for foreign exchange derivatives 6.61."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 139): "Next, the hedging set level add-ons (𝐴𝑑𝑑𝑂𝑛ℎ𝑠) must be recalculated by multiplying the recalculated effective notionals of each hedging set (𝐸𝑁ℎ𝑠) by the prescribed supervisory factor of the hedging set (𝑆𝐹𝑈𝑆𝐷)."

### [[SAMA — Maturity Factor (MF)|Maturity Factor (MF)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 35): "transactions, the supervisory factor applicable to a given asset class must be multiplied by a factor of five.21 Maturity factors 6.51."

### [[SAMA — PFE Multiplier|PFE Multiplier]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "Banks should apply a multiplier to the PFE component that decreases as excess collateral increases, without reaching zero (the multiplier is floored at 5% of the PFE add-on)."

### [[SAMA — Supervisory Delta Adjustment|Supervisory Delta Adjustment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 575): "In this case, for each asset class to which the position is allocated, banks must determine appropriately the sign and delta adjustment of the relevant risk driver (the role of delta adjustments in SA-CCR is outlined further in 6.32 below)."

### [[SAMA — Supervisory Factors|Supervisory Factors]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 34): "Supervisory factors (𝑆𝐹𝑖) are used, together with aggregation formulas, to convert effective notional amounts into the add-on for each hedging set.18 The way in which supervisory factors are used within the aggregation formulas varies between asset classes."

## Lookup terms

`PFE add-on`, `potential future exposure`, `aggregate add-on`, `replacement cost`, `NICA`, `threshold plus MTA`, `AddOn hedging set`, `over-collateralisation`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
