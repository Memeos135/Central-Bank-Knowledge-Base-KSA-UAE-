# Netting Set

Defines the netting set as the unit of account for counterparty credit risk exposure measurement: exposure at default is computed separately for each netting set as replacement cost plus potential future exposure, scaled by a fixed alpha factor. It distinguishes margined from un-margined netting sets (with the margined result capped at the un-margined result), sets minimum margin periods of risk including a doubling where repeated unresolved margin disputes occurred, and requires each transaction to be allocated to a hedging set by asset class. Relevant to banks calculating regulatory capital for derivatives portfolios.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 56): "If multiple margin agreements apply to a single netting set, the bank must divide the netting set into sub-netting sets that align with each respective margin agreement, and calculate RC for each sub-netting set separately."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."

### [[CBUAE — PFE Multiplier|PFE Multiplier]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 57): "As is the case with Replacement Cost, if multiple margin agreements apply to a single netting set, the bank must divide the netting set into sub-netting sets that align with each respective margin agreement, and calculate the PFE for each sub-netting set separately."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 65): "If the PFE multiplier for a netting set is greater than 1.0 when calculated according to the formula above (which generally occurs when NCV>0), the bank should set the PFE multiplier equal to 1.0 when calculating PFE."

## Lookup terms

`netting set`, `hedging set`, `margin period of risk`, `MPOR`, `margined vs un-margined`, `bilateral netting`, `netting by novation`, `maturity factor`

#graphify/enriched #source/cbuae #community/counterparty-exposure-(sa-ccr)
