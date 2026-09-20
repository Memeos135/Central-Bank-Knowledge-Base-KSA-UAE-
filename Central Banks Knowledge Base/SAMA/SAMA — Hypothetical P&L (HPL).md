# Hypothetical P&L (HPL)

Defines hypothetical P&L (HPL), the revaluation of a desk's unchanged end-of-day positions using the same market data as the front-office P&L, excluding intraday trading, new or modified deals, fees and commissions, and certain valuation adjustments already capitalised or deducted from CET1. HPL serves as the benchmark series for both backtesting and the PLA test, with specific rules on which valuation adjustments must be included at desk versus bank-wide level. Binds banks applying the internal models approach to market risk under SAMA rules.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Backtesting|Backtesting]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 465): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 109): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."

### [[SAMA — Backtesting Requirements|Backtesting Requirements]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 465): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 465): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."

### [[SAMA — P&L Attribution (PLA) Test|P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 118): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."

### [[SAMA — Profit and Loss Attribution (PLA) Test|Profit and Loss Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 523): "15- Transitional arrangements for Profit and loss (P&L) attribution (PLA) 15.1 Banks are required to conduct the profit and loss (P&L) attribution (PLA) test beginning 1 January 2023 as set out in [12.3]."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 523): "15- Transitional arrangements for Profit and loss (P&L) attribution (PLA) 15.1 Banks are required to conduct the profit and loss (P&L) attribution (PLA) test beginning 1 January 2023 as set out in [12.3]."

### [[SAMA — Spearman Correlation Metric|Spearman Correlation Metric]] — `shares_data_with` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

## Lookup terms

`hypothetical P&L`, `HPL`, `backtesting`, `valuation adjustments`, `desk-level P&L`, `credit valuation adjustment exclusion`, `PLA test`

#graphify/enriched #source/sama #community/internal-models-approach
