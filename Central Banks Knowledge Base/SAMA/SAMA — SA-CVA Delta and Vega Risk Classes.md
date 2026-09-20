# SA-CVA Delta and Vega Risk Classes

This node sets out how SA-CVA capital is built up as the sum of delta and vega risk charges across prescribed risk classes (six for delta, five for vega, with no vega charge for counterparty credit spread risk). It covers the CVA multiplier, the requirement to allocate an eligible credit spread hedge wholly to one risk class, and the calculation of CVA and hedge sensitivities including index hedges. It binds banks approved by SAMA to use the SA-CVA.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Standardized Approach for CVA (SA-CVA)|Standardized Approach for CVA (SA-CVA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 96): "The primary differences of the SA-CVA from the standardized approach for market risk are: (1) The SA-CVA features a reduced granularity of market risk factors; and (2) The SA-CVA does not include default risk and curvature risk."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

## Lookup terms

`SA-CVA delta risk`, `vega risk classes`, `mCVA multiplier`, `counterparty credit spread risk`, `reference credit spread risk`, `CVA sensitivities`, `eligible hedge allocation`

#graphify/enriched #source/sama #community/rwa-&-cva-disclosure-templates
