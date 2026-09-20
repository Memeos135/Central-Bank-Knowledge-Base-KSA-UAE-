# Expected Shortfall (ES) Model

This node addresses the expected shortfall (ES) internal model under SAMA's market risk standard, focusing on risk factor modellability: the risk factor eligibility test (RFET), the principles for data quality and real price observations, and the consequence that risk factors failing these standards are excluded from the ES model and capitalised as non-modellable risk factors (NMRF). It also records SAMA's narrow discretion to treat a failing risk factor as modellable only in extraordinary systemic stress, without reducing capital, and includes the statistical backtesting error-probability material underpinning exception thresholds. It binds SAMA-licensed banks with internal model permission for market risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Aggregate Capital Requirement for Modellable Risk Factors (IMCC)|Aggregate Capital Requirement for Modellable Risk Factors (IMCC)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"

### [[SAMA — Internal Models Approach (IMA)|Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 118): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 843): "22.2.2 Market risk under the internal models approach (IMA): Table MRB: Qualitative disclosures for banks using the IMA Purpose: Provide the scope, main characteristics and key modelling choices of the different models used for the capital requirement computation of market risks "

### [[SAMA — Liquidity Horizon|Liquidity Horizon]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 480): "The liquidity horizon of the index is the shortest liquidity horizon (out of 10, 20, 40, 60 and 120 days) that is equal to or longer than the weighted average liquidity horizon."

### [[SAMA — Non-Modellable Risk Factor (NMRF)|Non-Modellable Risk Factor (NMRF)]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — Risk Factor Eligibility Test (RFET)|Risk Factor Eligibility Test (RFET)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 447): "(e) The market risk capital requirements for risk factors that do not satisfy the risk factor eligibility test must be determined using stressed expected shortfall (SES) models as specified in [13.16] to [13.17] The model approval process requires an overall assessment of a bank’"

### [[SAMA — Risk-Theoretical P&L (RTPL)|Risk-Theoretical P&L (RTPL)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Stressed Expected Shortfall (ESR,S)|Stressed Expected Shortfall (ESR,S)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 118): "Calculation of expected shortfall 13.1 Banks will have flexibility in devising the precise nature of their expected shortfall (ES) models, but the following minimum standards will apply for the purpose of calculating market risk capital requirements."

## Lookup terms

`expected shortfall (ES) model`, `risk factor eligibility test (RFET)`, `non-modellable risk factor (NMRF)`, `modellability principles`, `real price observations`, `backtesting type 1 and type 2 error`, `model approval SAMA`

#graphify/enriched #source/sama #community/internal-models-approach
