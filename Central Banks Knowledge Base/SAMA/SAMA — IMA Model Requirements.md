# IMA Model Requirements

Node on the specific model requirements for banks using the internal models approach to market risk, including the trading desk structure, expected shortfall models, default risk capital, stressed expected shortfall for non-modellable risk factors, and the mandatory MRB qualitative disclosure table. It binds banks permitted by SAMA to use the IMA for market risk capital, at group-wide regulatory consolidation level, with annual flexible-format disclosure. Consult for what must be described about model scope, coverage percentages and soundness criteria.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — Internal Models Approach (IMA)|Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 843): "22.2.2 Market risk under the internal models approach (IMA): Table MRB: Qualitative disclosures for banks using the IMA Purpose: Provide the scope, main characteristics and key modelling choices of the different models used for the capital requirement computation of market risks "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 843): "22.2.2 Market risk under the internal models approach (IMA): Table MRB: Qualitative disclosures for banks using the IMA Purpose: Provide the scope, main characteristics and key modelling choices of the different models used for the capital requirement computation of market risks "

### [[SAMA — Risk Factor Eligibility Test (RFET)|Risk Factor Eligibility Test (RFET)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 469): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

### [[SAMA — Risk-Theoretical P&L (RTPL)|Risk-Theoretical P&L (RTPL)]] — `references` [INFERRED]
- **What this link tells you:** Deciding whether a trading desk keeps internal models approval turns on how the desk's risk management model is specified, because that model produces the risk-theoretical P&L used in the attribution test. The model requirements oblige the desk to capture the risk factors in the expected shortfall model plus those SAMA deems non-modellable, and any omissions or simplifications feed directly into divergence between RTPL and hypothetical P&L. The consequence is that a model-specification shortcut is not a documentation issue but can cause desk-level test failure and a move to the standardised approach. The dependency is inferred from the framework's design, so check the IMA and P&L attribution provisions directly.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 469): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`Table MRB qualitative disclosures`, `internal models approach market risk`, `expected shortfall model`, `default risk capital DRC`, `SES non-modellable`, `trading desk structure`, `IMA model approval`

#graphify/enriched #source/sama #community/internal-models-approach
