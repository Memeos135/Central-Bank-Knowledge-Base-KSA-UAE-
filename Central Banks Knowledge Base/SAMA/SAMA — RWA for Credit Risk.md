# RWA for Credit Risk

This node concerns the credit risk component of risk-weighted assets for output floor and Pillar 3 reporting purposes, distinguishing exposures measured under the standardised approach from those measured under foundation/advanced IRB and supervisory slotting approaches. It specifies scope boundaries, excluding counterparty credit risk, credit valuation adjustment, equity positions, settlement risk, securitisation exposures and amounts below deduction thresholds, each reported elsewhere, and addresses the phase-out of the IRB approach for equity exposures. It is relevant to banks calculating and disclosing credit risk RWA, including those with SAMA approval to use modelled approaches.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4376_VER1.md`

## Connections

### [[SAMA — CCP Hypothetical Capital (KCCP)|CCP Hypothetical Capital (KCCP)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 77): "𝐾𝐶𝐶𝑃 is a hypothetical capital requirement for a CCP, calculated on a consistent basis for the sole purpose of determining the capitalization of clearing member default fund contributions; it does not represent the actual capital requirements for a CCP which may be determined by "

### [[SAMA — Output Floor Requirements|Output Floor Requirements]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 728): "Minimum risk-based capital requirements 3 Risk-weighted assets and Output Floor requirements 4 RWA for credit risk 5 RWA for market risk 6 RWA for operational risk 6 Calculation of the output floor 7 Version Issuance Date Page Number Output Floor Requirements 1.1 December 2022 2 "

### [[SAMA — SCCR - Minimum Capital Requirements for CCR and CVA|SCCR - Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "capital conservation buffer, G-SIB surcharge and countercyclical capital buffer) and Pillar 2 capital requirements (if CET1 capital is required); (ii) CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capi"

### [[SAMA — SCRE - Minimum Capital Requirements for Credit Risk|SCRE - Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Standardized Approach for CCR (SA-CCR)|Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** A credit RWA calculation cannot be completed for derivative and other counterparty exposures without first determining exposure at default under the standardised approach for counterparty credit risk, which the credit risk rules cross-refer to directly. The reference also imports a floor that operates consistently across SA-CCR, the comprehensive approach to collateral within standardised credit risk, and the internal models method. For a compliance decision this means the two instruments form a single obligation chain: approach selection and any model permission on the counterparty credit side feed the credit risk capital number, and both sets of provisions must be evidenced together.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

## Lookup terms

`credit risk RWA`, `standardised approach credit risk`, `F-IRB A-IRB`, `supervisory slotting`, `credit risk mitigation haircuts`, `equity exposures phase-in`, `failed trades non-DvP`, `SCRE`

#graphify/enriched #source/sama #community/rwa-&-cva-disclosure-templates
