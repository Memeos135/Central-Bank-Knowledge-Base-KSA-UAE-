# Counterparty Credit Risk (CCR)

Concept node for the counterparty credit risk regime: the risk that a counterparty defaults before final settlement where there is bilateral risk of loss, together with related risks (rollover risk, general and specific wrong-way risk) and the linkage to CVA capital. It sets the framework's effective date and requires quarterly reporting of CCR and CVA risk-weighted assets and capital charges on SAMA's designated template within 30 days of quarter end, with corresponding Pillar 3 template disclosure. It binds banks subject to SAMA's minimum capital requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Internal Models Method (IMM)|Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** Where a bank calculates counterparty credit risk exposure using the Internal Models Method, the CCR requirements are not self-contained: they reference the IMM provisions, which govern how EAD is modelled and how the resulting RWA are reported and explained. This is an obligation chain within one capital framework, where the general CCR rules set the requirement and the IMM chapter sets the conditions and disclosure expectations for that particular measurement approach. For a decision on derivatives or SFT exposures, confirm whether IMM is being used and, if so, apply the IMM conditions and reporting requirements in addition to the general CCR rules.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 826): "Template CCR7: RWA flow statements of CCR exposures under Internal Model Method (IMM) Purpose: Present a flow statement explaining changes in counterparty credit risk RWA determined under the Internal Model Method for counterparty credit risk (derivatives and SFTs)."

### [[SAMA — Minimum Capital Requirements for CCR and CVA|Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 89): "However, all banks using the BA-CVA must calculate the reduced version of BA-CVA capital Version Minimum Capital Requirements for Counterparty Credit Risk (CCR) and 89 of 145 Issue Date December 2022 Page Number Credit Valuation Adjustment (CVA) 1.1"

### [[SAMA — Minimum Capital Requirements for Credit Risk|Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — SA-CCR Standardized Approach|SA-CCR Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** A question about counterparty credit risk treatment resolves, in the standardised case, into the SA-CCR calculation rules, so the general CCR provisions should be read as scope and definition rather than as a self-contained method. The link is an internal cross-reference within the same SAMA capital instrument, and it carries the same minimum floor that applies across the standardised comprehensive approach and the internal models method. For the reader, this means a CCR determination is incomplete until SA-CCR application and the applicable floor have been checked.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 620): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

### [[SAMA — Securities Financing Transactions (SFTs)|Securities Financing Transactions (SFTs)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 3): "Introduction The Basel III framework on Counterparty Credit Risk includes a comprehensive, non-modelled approach for measuring counterparty credit risk arising from derivative contracts, Securities Financing transaction (SFT) and cash transactions in securities, foreign exchange "

## Lookup terms

`counterparty credit risk (CCR)`, `wrong-way risk`, `rollover risk`, `bilateral risk of loss`, `CCR RWA reporting`, `Q17 template`, `SA-CCR`, `exposure at default`

#graphify/enriched #source/sama #community/counterparty-credit-&-sfts
