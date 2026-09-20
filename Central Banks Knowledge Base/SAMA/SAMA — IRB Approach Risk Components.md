# IRB Approach: Risk Components

Concept node for the IRB risk components — the inputs (probability of default, loss given default, exposure at default and effective maturity) that feed the IRB risk weight functions, with the split between own estimates and supervisory values determining F-IRB versus A-IRB treatment. In SAMA's Pillar 3 instructions these components are the disclosed parameters in IRB templates, including EAD post-CRM, average PD and average maturity by PD band. Applies to banks with SAMA approval to use IRB approaches.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — Effective Maturity (M)|Effective Maturity (M)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 137): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."

### [[SAMA — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Loss Given Default (LGD)|Loss Given Default (LGD)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 364): "3.3 The risks subject to market risk capital requirements include but are not limited to: (1) Default risk, interest rate risk, credit spread risk, equity risk, foreign exchange (FX) risk and commodities risk for trading book instruments; and (2) FX risk and commodities risk for "
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"

### [[SAMA — Probability of Default (PD)|Probability of Default (PD)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 364): "3.3 The risks subject to market risk capital requirements include but are not limited to: (1) Default risk, interest rate risk, credit spread risk, equity risk, foreign exchange (FX) risk and commodities risk for trading book instruments; and (2) FX risk and commodities risk for "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 429): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"

### [[SAMA — Standardized Approach Credit Risk Mitigation|Standardized Approach: Credit Risk Mitigation]] — `references` [EXTRACTED]
- **What this link tells you:** This link tells you where mitigation is actually reflected in the calculation: under the standardized approach it adjusts the exposure amount or the applicable risk weight, whereas the general credit risk mitigation chapter routes IRB exposures to the risk-components rules, where protection is instead reflected in parameters such as loss given default and exposure at default. The two chapters therefore describe one obligation chain with two calculation routes, not two independent entitlements. The consequence is that a bank must recognise a given piece of collateral or protection once, through the route matching its approach, and should not combine a standardized-approach adjustment with a parameter-based benefit for the same exposure.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 564): "(2) The simple approach or comprehensive approach to the recognition of collateral, which are both set out in the credit risk mitigation chapter of the standardized approach to credit risk (see Chapter 9 on the mitigation techniques for exposures risk-weighted under the standardi"

## Lookup terms

`risk components`, `PD LGD EAD maturity`, `exposure at default`, `loss given default`, `EAD post-CRM`, `PD scale`, `IRB parameters`

#graphify/enriched #source/sama #community/irb-risk-components
