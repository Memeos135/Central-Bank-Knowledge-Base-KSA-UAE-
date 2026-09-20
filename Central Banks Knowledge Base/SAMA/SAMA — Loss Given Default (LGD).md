# Loss Given Default (LGD)

Concept node for Loss Given Default (LGD) as used in SAMA's credit risk capital framework, covering the requirements for banks permitted to use own LGD estimates under the advanced IRB approach. It sets the substantive standards: LGD must reflect economic downturn conditions, cannot fall below the long-run default-weighted average loss rate for the facility type, and must conservatively address dependence between borrower and collateral/collateral provider as well as currency mismatches. It binds banks approved by SAMA to use internal ratings-based approaches; related material also appears in Pillar 3 disclosure templates.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Advanced IRB (A-IRB) Approach|Advanced IRB (A-IRB) Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether a bank may use its own risk parameters for a given exposure, the A-IRB designation is what unlocks internal LGD estimation, so the two provisions must be read together rather than separately. The advanced IRB provisions expressly rely on the LGD definition and on the bank's ability to estimate default-weighted average loss rates given default reliably, meaning LGD is a dependent parameter whose permissible source is fixed by the approach the bank is approved to use. Practically, a reviewer confirming A-IRB status must also confirm that the LGD estimation and reliability conditions are satisfied; failure on the LGD side undermines the A-IRB treatment and the resulting RWA and disclosure template population.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "Advanced IRB treatment 14.6 Under the advanced IRB approach, if the purchasing bank can estimate either the pool’s default-weighted average loss rates given default (as defined in paragraph 16.82) or average PD in a reliable manner, the bank may estimate the other parameter based"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 823): "Scope of application: The template is mandatory for banks using an advanced IRB (A-IRB) or foundation IRB (F-IRB) approach to compute RWA for counterparty credit risk exposures, whatever CCR approach is used to determine exposure at default."

### [[SAMA — Advanced IRB Approach (A-IRB)|Advanced IRB Approach (A-IRB)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "Advanced IRB treatment 14.6 Under the advanced IRB approach, if the purchasing bank can estimate either the pool’s default-weighted average loss rates given default (as defined in paragraph 16.82) or average PD in a reliable manner, the bank may estimate the other parameter based"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 116): "LGD under the F-IRB approach: collateral recognition 12.8 In addition to the eligible financial collateral recognized in the standardized approach, under the F-IRB approach some other forms of collateral, known as eligible IRB collateral, are also recognized."

### [[SAMA — Comprehensive Approach to Collateral|Comprehensive Approach to Collateral]] — `references` [EXTRACTED]
- **What this link tells you:** The decision here is how collateral flows into the loss estimate: under the foundation IRB approach, recognised collateral (eligible financial collateral plus the wider set of eligible IRB collateral) adjusts the supervisory LGD rather than being applied as a standalone exposure reduction. The comprehensive approach supplies the haircut mechanics and eligibility gate, while the LGD chapter governs how the resulting loss rate is derived and, for advanced IRB, how own estimates must reflect long-run default-weighted averages. Consequence: collateral relief is only as good as its LGD recognition — check both chapters together, since collateral that is ineligible or unsupported by loss data will not reduce the capital requirement.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 123): "LGD under the F-IRB approach: collateral recognition 12.8 In addition to the eligible financial collateral recognized in the standardized approach, under the F-IRB approach some other forms of collateral, known as eligible IRB collateral, are also recognized."

### [[SAMA — Eligible Financial Collateral|Eligible Financial Collateral]] — `references` [EXTRACTED]
- **What this link tells you:** Where a bank is on the foundation IRB approach it does not set LGD itself, so the operative question becomes which collateral is recognized and how it adjusts supervisory LGD — a determination made by the eligible collateral rules in the other instrument. The LGD provisions point to the collateral recognition framework, which extends the standardized approach list of eligible financial collateral with additional eligible IRB collateral. The consequence is that an F-IRB credit risk mitigation decision must be tested against the eligibility and operational conditions in the collateral instrument before any LGD reduction is claimed; collateral that fails those conditions yields no LGD benefit.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 116): "LGD under the F-IRB approach: collateral recognition 12.8 In addition to the eligible financial collateral recognized in the standardized approach, under the F-IRB approach some other forms of collateral, known as eligible IRB collateral, are also recognized."

### [[SAMA — Foundation IRB (F-IRB) Approach|Foundation IRB (F-IRB) Approach]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 823): "Scope of application: The template is mandatory for banks using an advanced IRB (A-IRB) or foundation IRB (F-IRB) approach to compute RWA for counterparty credit risk exposures, whatever CCR approach is used to determine exposure at default."

### [[SAMA — IRB Approach Risk Components|IRB Approach: Risk Components]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 364): "3.3 The risks subject to market risk capital requirements include but are not limited to: (1) Default risk, interest rate risk, credit spread risk, equity risk, foreign exchange (FX) risk and commodities risk for trading book instruments; and (2) FX risk and commodities risk for "

### [[SAMA — IRB Approach Risk Weight Functions|IRB Approach: Risk Weight Functions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 115): "Explanation of the risk-weight functions 11.2 Regarding the risk-weight functions for deriving risk weighted assets set out in this chapter: (1) Probability of default (PD) and loss-given-default (LGD) are measured as decimals (2) Exposure at default (EAD) is measured as currency"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."

### [[SAMA — IRB Approach Treatment of Expected Losses and Provisions|IRB Approach: Treatment of Expected Losses and Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 181): "IRB Approach: Treatment of expected losses and provisions 15.1 This chapter discusses the calculation of expected losses (EL) under the internal ratings-based (IRB) approach, and the method by which the difference between provisions (e.g."

### [[SAMA — IRB Risk Components (PD, LGD, EAD, M)|IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"

## Lookup terms

`Loss Given Default`, `LGD`, `own-LGD estimates`, `downturn LGD`, `A-IRB`, `default-weighted average loss rate`, `collateral dependence`, `risk components`

#graphify/enriched #source/sama #community/irb-risk-components
