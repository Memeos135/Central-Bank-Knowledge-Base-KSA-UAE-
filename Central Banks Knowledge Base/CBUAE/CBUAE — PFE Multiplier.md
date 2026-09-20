# PFE Multiplier

The PFE multiplier is the netting-set-level scaling factor applied to the aggregate asset-class add-on to recognise the risk-reducing effect of over-collateralisation and negative mark-to-market, computed from net current value and the aggregate add-on subject to a prescribed floor. Where the formula yields a value above one, the multiplier is set to one. It sits within the supervisory factor, correlation and volatility parameter table used by banks in the standardised CCR calculation.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Netting Set|Netting Set]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 65): "If the PFE multiplier for a netting set is greater than 1.0 when calculated according to the formula above (which generally occurs when NCV>0), the bank should set the PFE multiplier equal to 1.0 when calculating PFE."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 57): "As is the case with Replacement Cost, if multiple margin agreements apply to a single netting set, the bank must divide the netting set into sub-netting sets that align with each respective margin agreement, and calculate the PFE for each sub-netting set separately."

### [[CBUAE — Potential Future Exposure|Potential Future Exposure]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"

## Lookup terms

`PFE multiplier`, `aggregate add-on`, `AddOn agg`, `supervisory factors table`, `correlation and volatility parameters`, `over-collateralisation`, `floor 0.05`

#graphify/enriched #source/cbuae #community/counterparty-exposure-(sa-ccr)
