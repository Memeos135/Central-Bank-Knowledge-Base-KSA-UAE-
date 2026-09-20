# Risk-Theoretical P&L (RTPL)

Defines risk-theoretical P&L (RTPL), the daily P&L predicted by a trading desk's risk management model using only the risk factors contained in that model, and used as one of the two inputs to the PLA test. The node also addresses the limited circumstances in which RTPL input data may be aligned with hypothetical P&L data (differing market data providers, snapshot times or data transformations), with documentation, validation, notification and impact-assessment duties owed to SAMA. Applies to banks using or seeking IMA approval for market risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Expected Shortfall (ES) Model|Expected Shortfall (ES) Model]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"

### [[SAMA — IMA Model Requirements|IMA Model Requirements]] — `references` [INFERRED]
- **What this link tells you:** Deciding whether a trading desk keeps internal models approval turns on how the desk's risk management model is specified, because that model produces the risk-theoretical P&L used in the attribution test. The model requirements oblige the desk to capture the risk factors in the expected shortfall model plus those SAMA deems non-modellable, and any omissions or simplifications feed directly into divergence between RTPL and hypothetical P&L. The consequence is that a model-specification shortcut is not a documentation issue but can cause desk-level test failure and a move to the standardised approach. The dependency is inferred from the framework's design, so check the IMA and P&L attribution provisions directly.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 469): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[SAMA — P&L Attribution (PLA) Test|P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 118): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."

### [[SAMA — Profit and Loss Attribution (PLA) Test|Profit and Loss Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 523): "15- Transitional arrangements for Profit and loss (P&L) attribution (PLA) 15.1 Banks are required to conduct the profit and loss (P&L) attribution (PLA) test beginning 1 January 2023 as set out in [12.3]."

### [[SAMA — Spearman Correlation Metric|Spearman Correlation Metric]] — `shares_data_with` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

## Lookup terms

`risk-theoretical P&L`, `RTPL`, `trading desk risk management model`, `input data alignment`, `PLA test inputs`, `non-modellable risk factor`, `market data snapshot`

#graphify/enriched #source/sama #community/internal-models-approach
