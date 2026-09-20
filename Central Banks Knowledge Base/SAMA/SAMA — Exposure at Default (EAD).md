# Exposure at Default (EAD)

Concept node for Exposure at Default (EAD), the exposure amount risk component used in credit risk capital calculation and in related Pillar 3 disclosure templates (including credit risk mitigation and problem-asset disclosures). It anchors how carrying amounts, secured and unsecured exposures, and non-performing/forborne classifications feed the exposure measure. It binds banks subject to SAMA's minimum capital requirements for credit risk and disclosure requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Advanced IRB Approach (A-IRB)|Advanced IRB Approach (A-IRB)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 823): "Scope of application: The template is mandatory for banks using an advanced IRB (A-IRB) or foundation IRB (F-IRB) approach to compute RWA for counterparty credit risk exposures, whatever CCR approach is used to determine exposure at default."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 233): "18.15 For risk-based capital purposes, an internal ratings-based (IRB) pool means a securitization pool for which a bank is able to use an IRB approach to calculate capital requirements for all underlying exposures given that it has approval to apply IRB for the type of underlyin"

### [[SAMA — Counterparty Credit Risk (CCR) Framework|Counterparty Credit Risk (CCR) Framework]] — `references` [EXTRACTED]
- **What this link tells you:** When assessing counterparty credit risk capital, the CCR framework does not itself produce the number; it directs you to the exposure at default measure, which is the quantum the risk weight is applied to. The reference is an obligation chain within the same SAMA capital instrument: the CCR framework sets scope and approach eligibility, and EAD supplies the measurement input. For a decision, any CCR-related conclusion (netting recognition, collateral effect, approach choice) must be traced through to how it alters EAD, because that is where the capital consequence crystallises.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Credit Conversion Factors (CCF)|Credit Conversion Factors (CCF)]] — `references` [EXTRACTED]
- **What this link tells you:** The linkage matters when quantifying exposure on off-balance-sheet and undrawn items: the credit conversion factor is the mechanism that converts a committed or contingent amount into the exposure at default used for RWA and for defaulted-exposure reporting. EAD is therefore not a freestanding input but the output of applying the prescribed or estimated CCF to the relevant facility amount. In practice, any challenge to the CCF applied (supervisory versus own estimates, and the facility classification behind it) flows directly through to reported EAD, capital requirements and the stock-of-defaulted-exposures disclosures. Note the excerpts here are imperfectly aligned, so the reader should verify the specific CCF and EAD paragraphs in the primary text before relying on them.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 661): "The counterparty credit spread delta risk factors for a given bucket: (1) The counterparty credit spread delta risk factors are absolute shifts of credit spreads of individual entities (counterparties and reference names for counterparty credit spread hedges) and qualified indice"

### [[SAMA — IRB Approach Risk Components|IRB Approach: Risk Components]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — IRB Approach Risk Weight Functions|IRB Approach: Risk Weight Functions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."

### [[SAMA — IRB Risk Components (PD, LGD, EAD, M)|IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"

### [[SAMA — Internal Models Method (IMM)|Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding which EAD measurement basis a bank may lawfully use for counterparty credit risk, the internal models method is the conditional alternative: it is expressly a method for estimating EAD and is available only where SAMA approval has been obtained. The link is a hierarchy and permission point within the same framework — the EAD requirement is the obligation, IMM is a permitted route to satisfy it subject to supervisory authorisation and the associated model conditions and floors. If approval is absent, lapsed, or limited to certain portfolios, the bank must fall back to the non-model approach for the affected exposures.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 597): "Internal models method for counterparty credit risk Approval to adopt an internal models method to estimate EAD 7.1."

### [[SAMA — PFE Add-on|PFE Add-on]] — `references` [EXTRACTED]
- **What this link tells you:** If you are validating a bank's counterparty credit risk capital numbers, you cannot assess the exposure-at-default figure in isolation: for derivative and long-settlement transactions the EAD is built from a replacement cost element plus a potential future exposure component, and the PFE add-on rules supply the aggregate add-on and multiplier that drive that second element. The two instruments therefore sit in one obligation chain — the EAD definition sets what must be measured, the PFE add-on provisions set how part of it is calculated. Practically, an error or unapproved simplification in the add-on aggregation or multiplier treatment flows straight through to reported EAD and risk-weighted assets, so both texts must be checked together.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

### [[SAMA — Replacement Cost (RC)|Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** Treat replacement cost as an input to, not an alternative to, the exposure at default figure: for counterparty credit risk the exposure measure is built from RC, and where RC cannot be determined the rules impose a conservative substitute based on notional amounts of the netting set. For a compliance decision this means an EAD number cannot be signed off without confirming how RC was established, since an unknown RC forces the conservative treatment rather than an estimate. Note that the excerpt captured for the EAD node points to defaulted-exposure flow reporting, so verify the primary text to confirm exactly which EAD provision is cross-referenced.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 334): "Whenever the replacement cost is unknown, the exposure measure for CCR will be calculated in a conservative manner by using the sum of the notional amounts of the derivatives in the netting set as a proxy for the replacement cost, and the multiplier used in the calculation of the"

### [[SAMA — Standardized Approach for CCR (SA-CCR)|Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** For a decision on how a bank must compute derivative EAD absent internal model approval, SA-CCR is the standardised default and is cross-referenced from the EAD provisions, including the shared floor that is mirrored across SA-CCR, the comprehensive approach under the standardised credit risk rules, and IMM. The relationship is a defined-term and cross-reference one: EAD is the quantity to be reported, SA-CCR prescribes one prescribed method for arriving at it. Consequence: confirm which method the exposure falls under before testing the calculation, and check that the common floor has been applied consistently whichever route is used.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

### [[SAMA — The Market Risk Framework|The Market Risk Framework]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`Exposure at Default`, `EAD`, `exposure amount`, `credit risk mitigation`, `carrying amount`, `non-performing exposures`, `forborne exposure`, `Template CR3`

#graphify/enriched #source/sama #community/irb-risk-components
