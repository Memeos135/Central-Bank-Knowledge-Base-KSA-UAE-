# Kolmogorov-Smirnov Test Metric

Defines the Kolmogorov-Smirnov distributional metric used in the profit and loss attribution (PLA) test: the largest absolute gap between the empirical cumulative distributions of hypothetical P&L and risk-theoretical P&L. Together with the correlation metric it allocates each trading desk to a PLA green, amber or red zone, with red-zone desks barred from the internal models approach and pushed to the standardised approach until they return to green and clear backtesting requirements. Binds banks seeking IMA permission at trading desk level.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — P&L Attribution (PLA) Test|P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

## Lookup terms

`Kolmogorov-Smirnov test`, `KS metric`, `PLA test`, `profit and loss attribution`, `green amber red zone`, `hypothetical P&L`, `HPL`, `trading desk IMA eligibility`

#graphify/enriched #source/sama #community/internal-models-approach
