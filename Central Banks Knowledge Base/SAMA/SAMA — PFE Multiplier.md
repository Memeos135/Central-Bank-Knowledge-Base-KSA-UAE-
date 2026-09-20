# PFE Multiplier

This node explains the PFE multiplier in SA-CCR — a function of net market value (V), collateral (C) and the aggregate add-on — which reduces the PFE component to recognise over-collateralisation or a negative mark-to-market position in a netting set. It sits within the EAD formula (alpha of 1.4 times replacement cost plus PFE) and the distinction between margined and unmargined netting sets, including the cap of margined EAD at the unmargined amount. It applies to banks computing counterparty credit risk exposure under SA-CCR.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — PFE Add-on|PFE Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "Banks should apply a multiplier to the PFE component that decreases as excess collateral increases, without reaching zero (the multiplier is floored at 5% of the PFE add-on)."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

## Lookup terms

`PFE multiplier`, `excess collateral recognition`, `negative mark-to-market`, `alpha 1.4`, `EAD formula SA-CCR`, `margined netting set`, `unmargined netting set`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
