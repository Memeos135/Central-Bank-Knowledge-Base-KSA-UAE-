# Standardized Approach for CCR (SA-CCR)

This node sets the scope and positioning of the Standardized Approach for Counterparty Credit Risk (SA-CCR) — applying to OTC derivatives, exchange-traded derivatives and long settlement transactions — and the routing of calculated CCR exposures (EAD) into the standardized or IRB credit risk approaches, or the CCP exposure rules. It also carries the IRB maturity adjustment cap, the IMM current-versus-stressed RWA floor, exemptions where no CCR charge applies (certain purchased credit protection and banking book sold CDS), and the cross-reference to minimum haircut floors for non-centrally cleared SFTs. It binds banks that lack SAMA approval for the Internal Model Method, which must use SA-CCR.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Derivative Exposures Treatment|Derivative Exposures Treatment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 18): "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions.5 Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions mus"
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[SAMA — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** For a decision on how a bank must compute derivative EAD absent internal model approval, SA-CCR is the standardised default and is cross-referenced from the EAD provisions, including the shared floor that is mirrored across SA-CCR, the comprehensive approach under the standardised credit risk rules, and IMM. The relationship is a defined-term and cross-reference one: EAD is the quantity to be reported, SA-CCR prescribes one prescribed method for arriving at it. Consequence: confirm which method the exposure falls under before testing the calculation, and check that the common floor has been applied consistently whichever route is used.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[SAMA — Minimum Capital Requirements for Credit Risk|Minimum Capital Requirements for Credit Risk]] — `cites` [EXTRACTED]
- **What this link tells you:** For derivative and margined counterparty exposures, the exposure amount feeding the credit risk capital calculation is determined under SA-CCR (or the internal models method), and the credit risk text is expressly cross-referenced in setting the applicable floor alongside the comprehensive approach to collateral. The link is an explicit provision-level cross-reference within the same Basel-derived capital regime, so the two must be read as one continuous measurement chain. In practice, a counterparty credit risk capital number is only defensible if the SA-CCR exposure calculation and the credit risk floor provisions have both been applied consistently.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Netting Set|Netting Set]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"

### [[SAMA — RWA for Credit Risk|RWA for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** A credit RWA calculation cannot be completed for derivative and other counterparty exposures without first determining exposure at default under the standardised approach for counterparty credit risk, which the credit risk rules cross-refer to directly. The reference also imports a floor that operates consistently across SA-CCR, the comprehensive approach to collateral within standardised credit risk, and the internal models method. For a compliance decision this means the two instruments form a single obligation chain: approach selection and any model permission on the counterparty credit side feed the credit risk capital number, and both sets of provisions must be evidenced together.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`SA-CCR`, `standardized approach counterparty credit risk`, `exposure at default EAD`, `internal model method IMM`, `netting set`, `CCR exemptions`, `sold credit default swap banking book`, `minimum haircut floors SFT`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
