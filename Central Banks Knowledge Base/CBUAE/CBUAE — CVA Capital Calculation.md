# CVA Capital Calculation

The mechanics of computing CVA capital: discounting each counterparty's total EAD by a supervisory discount factor reflecting the notional weighted-average maturity of the netting set, summing across netting sets where multiple exist, and computing discounted values of eligible single-name hedges by hedge maturity. It sits within the wider capital adequacy framework (minimum total capital of 10.5% of RWA plus CCB, CCyB, D-SIB and any SREP-based supervisory capital guidance add-on). Binds UAE banks on a consolidated basis.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Credit Valuation Adjustment (CVA) Standard|Credit Valuation Adjustment (CVA) Standard]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 71): "The CVA capital calculation encompasses a bank's CVA portfolio, which includes the bank's entire portfolio of covered transactions as well as eligible CVA hedges."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 29): "Risk-weighted asset amounts for Credit Valuation Adjustment (CVA) risk are calculated based on the provisions set out below in the Standard, Credit Valuation Adjustment 4."

### [[CBUAE — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** Treat the exposure-at-default determination as an upstream input you must settle before any CVA capital number can be defended. The CVA capital component sits inside the same capital adequacy framework whose denominator is built from exposure measures, so the EAD definition and its measurement conventions feed directly into the CVA charge rather than standing as a separate calculation. Practically, a change or supervisory challenge to how EAD is derived for a counterparty propagates into the CVA capital result and the overall capital ratio; verify the primary text for the precise EAD basis applied to CVA, since the surrounding provisions also address leverage exposure and should not be conflated.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 12): "Capital component of Capital Adequacy Regulation If a bank has complied with the minimum CET1 and Tier 1 capital ratios, the excess AT1 capital can be counted to meet the total capital ratio, also referred to as Capital Adequacy Ratio (CAR)."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."

### [[CBUAE — Single-Name Exposure (SNE)|Single-Name Exposure (SNE)]] — `references` [EXTRACTED]
- **What this link tells you:** If you are sizing CVA risk capital, you cannot stop at the capital-adequacy component alone: the CVA charge is driven by counterparty-level exposure, and single-name exposure is the defined input that nets discounted counterparty exposure against eligible single-name CVA hedges. The reference runs one way — the CVA capital provisions depend on the SNE measurement rules — so the two instruments sit in the same Basel-aligned capital adequacy chain rather than being alternatives. Practically, any hedge-recognition or exposure-netting judgement must be settled under the SNE definition before the resulting number is carried into the CET1/Tier 1/total capital ratio test. Note the supplied excerpts are partly generic, so verify the primary text for the exact CVA-to-SNE cross-reference.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 12): "Capital component of Capital Adequacy Regulation If a bank has complied with the minimum CET1 and Tier 1 capital ratios, the excess AT1 capital can be counted to meet the total capital ratio, also referred to as Capital Adequacy Ratio (CAR)."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 74): "For each counterparty, the bank should calculate single-name exposure (SNE) as the discounted counterparty exposure minus the discounted value of eligible single-name CVA hedges."

## Lookup terms

`CVA capital calculation`, `supervisory discount factor`, `netting set`, `discounted counterparty exposure`, `weighted-average maturity`, `capital conservation buffer`, `countercyclical buffer`, `supervisory capital guidance`

#graphify/enriched #source/cbuae #community/counterparty-credit-&-cva-risk
