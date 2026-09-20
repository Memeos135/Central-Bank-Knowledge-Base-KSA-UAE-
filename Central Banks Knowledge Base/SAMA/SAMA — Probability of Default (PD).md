# Probability of Default (PD)

Concept node for Probability of Default (PD), the estimated likelihood that an obligor defaults over a one-year horizon and a core IRB risk component, as used in SAMA's Pillar 3 disclosure templates. It governs the PD-band breakdowns in IRB templates and the annual backtesting disclosure comparing modelled PD against realised default rates, using at least a five-year average annual default rate; it also links to the defaulted-exposure definitions (e.g. past due more than 90 days under the standardised approach). Binds banks using A-IRB or F-IRB, with PD models requiring SAMA approval.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Foundation IRB Approach (F-IRB)|Foundation IRB Approach (F-IRB)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 823): "Scope of application: The template is mandatory for banks using an advanced IRB (A-IRB) or foundation IRB (F-IRB) approach to compute RWA for counterparty credit risk exposures, whatever CCR approach is used to determine exposure at default."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 116): "LGD under the F-IRB approach: collateral recognition 12.8 In addition to the eligible financial collateral recognized in the standardized approach, under the F-IRB approach some other forms of collateral, known as eligible IRB collateral, are also recognized."

### [[SAMA — IRB Approach Risk Components|IRB Approach: Risk Components]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 429): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 364): "3.3 The risks subject to market risk capital requirements include but are not limited to: (1) Default risk, interest rate risk, credit spread risk, equity risk, foreign exchange (FX) risk and commodities risk for trading book instruments; and (2) FX risk and commodities risk for "

### [[SAMA — IRB Approach Risk Weight Functions|IRB Approach: Risk Weight Functions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."

### [[SAMA — IRB Approach Treatment of Expected Losses and Provisions|IRB Approach: Treatment of Expected Losses and Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 181): "IRB Approach: Treatment of expected losses and provisions 15.1 This chapter discusses the calculation of expected losses (EL) under the internal ratings-based (IRB) approach, and the method by which the difference between provisions (e.g."

### [[SAMA — IRB Risk Components (PD, LGD, EAD, M)|IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 115): "Explanation of the risk-weight functions 11.2 Regarding the risk-weight functions for deriving risk weighted assets set out in this chapter: (1) Probability of default (PD) and loss-given-default (LGD) are measured as decimals (2) Exposure at default (EAD) is measured as currency"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"

## Lookup terms

`probability of default`, `PD`, `PD backtesting`, `CR9`, `default rate`, `defaulted exposures`, `past due 90 days`, `obligor rating`, `PD scale`

#graphify/enriched #source/sama #community/irb-risk-components
