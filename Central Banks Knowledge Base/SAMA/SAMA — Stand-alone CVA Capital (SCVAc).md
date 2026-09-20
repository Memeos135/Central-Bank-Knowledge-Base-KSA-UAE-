# Stand-alone CVA Capital (SCVAc)

A concept node for the stand-alone CVA capital requirement (SCVAc) component within SAMA's Basel-aligned capital framework, sitting alongside Pillar 3 disclosure templates on regulatory capital composition and capital distribution constraints. It relates to how credit valuation adjustment risk is capitalised separately from counterparty credit risk and how the resulting figures feed disclosed capital ratios and buffer-trigger levels. It binds banks subject to SAMA's risk-based capital and disclosure requirements at the consolidated group level.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — Internal Models Method (IMM)|Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** If the bank uses IMM for counterparty exposures, it still has to answer separately how CVA risk capital is calculated, and the stand-alone CVA capital component is where that computation lands. The link reflects that IMM outputs feed the exposure measures used in the CVA charge, with SCVAc being the per-counterparty building block before eligible hedges and correlation effects are recognised. The consequence is that an IMM permission does not by itself dispose of the CVA capital question — the CVA calculation must be run and evidenced on its own terms.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 642): "The part of capital requirements that recognizes eligible hedges (𝐾ℎ𝑒𝑑𝑔𝑒𝑑) is calculated formulas follows (where the summations are taken over all counterparties c that are within scope of the CVA charge), where: (1) Both the stand-alone CVA capital (SCVAc) and the correlation pa"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 891): "* RWA and capital requirements under the Standardised Approach for credit risk weighting are to be subdivided in the standardised approach for counterparty credit risk (SA-CCR) and the internal models method (IMM), and the same for RWA and capital requirements under the internal "

### [[SAMA — Reduced Version of BA-CVA|Reduced Version of BA-CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

## Lookup terms

`stand-alone CVA capital`, `SCVAc`, `credit valuation adjustment capital requirement`, `BA-CVA`, `Pillar 3 capital disclosure`, `capital distribution constraints`, `CET1 buffer trigger`

#graphify/enriched #source/sama #community/rwa-&-cva-disclosure-templates
