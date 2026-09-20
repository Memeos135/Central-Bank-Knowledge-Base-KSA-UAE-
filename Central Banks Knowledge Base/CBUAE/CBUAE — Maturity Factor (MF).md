# Maturity Factor (MF)

Concept node for the maturity factor, the time-scaling input in the counterparty credit risk add-on formulas. For margined transactions it is derived from the margin period of risk, with prescribed minimum MPOR floors (including for non-centrally cleared and centrally cleared daily-margined trades and large netting sets) and a doubling requirement where repeated unresolved margin call disputes have occurred. It binds banks computing derivative exposure at default, and interacts with maturity-category and maturity-mismatch concepts elsewhere in the capital standards.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Add-on for Credit Derivatives|Add-on for Credit Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 91): "Tranche maturity (MT) Tranche maturity is a tranche’s remaining effective maturity in years, calculated in one of the following two ways, subject to a floor of one year and a cap of five years: (a) Weighted-average maturity, calculated as the weighted-average maturity of the cont"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."

## Lookup terms

`maturity factor`, `MF`, `margin period of risk`, `MPOR`, `margin call disputes`, `margined transactions`, `maturity mismatch`, `remaining maturity`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
