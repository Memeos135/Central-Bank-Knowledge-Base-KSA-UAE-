# Counterparty Credit Risk (CCR) Framework

A concept node covering SAMA's minimum capital requirements framework for counterparty credit risk (CCR) and credit valuation adjustment (CVA), including the definition of CCR as bilateral risk of loss before final settlement and related risks such as rollover risk and general/specific wrong-way risk. It also fixes the effective date (1 January 2023) and the quarterly Q17 reporting obligation to SAMA within 30 days of quarter-end. It binds banks with derivative, SFT and long-settlement exposures.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Collateralized Transactions|Collateralized Transactions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 71): "Overview of credit risk mitigation techniques Collateralized transactions 9.16 A collateralized transaction is one in which: (1) banks have a credit exposure or a potential credit exposure; and (2) that credit exposure or potential credit exposure is hedged in whole or in part by"

### [[SAMA — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing counterparty credit risk capital, the CCR framework does not itself produce the number; it directs you to the exposure at default measure, which is the quantum the risk weight is applied to. The reference is an obligation chain within the same SAMA capital instrument: the CCR framework sets scope and approach eligibility, and EAD supplies the measurement input. For a decision, any CCR-related conclusion (netting recognition, collateral effect, approach choice) must be traced through to how it alters EAD, because that is where the capital consequence crystallises.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Master Netting Agreements for SFTs|Master Netting Agreements for SFTs]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Off-Balance Sheet Items|Off-Balance Sheet Items]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 46): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."

### [[SAMA — SA-CCR Standardized Approach|SA-CCR Standardized Approach]] — `references` [EXTRACTED]
- **What this link tells you:** Where a bank is not using an internal models method for counterparty exposures, the CCR framework routes it to SA-CCR as the standardised measurement method, so the framework's requirements are only operable once SA-CCR is applied. The cross-reference also carries a floor that is expressed consistently across SA-CCR, the comprehensive approach within standardised credit risk, and the internal models method, indicating the framework intends a common minimum regardless of route. The practical consequence is that approach selection does not escape the floor, and a compliance review should confirm the floor has been applied under whichever method the bank has adopted.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 620): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

## Lookup terms

`counterparty credit risk`, `CCR`, `credit valuation adjustment`, `CVA`, `wrong-way risk`, `rollover risk`, `Q17 reporting template`, `bilateral risk of loss`

#graphify/enriched #source/sama #community/counterparty-credit-risk-mitigation
