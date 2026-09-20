# Liquidity Horizon

Concept node for the liquidity horizon — the supervisory-set holding period assigned to each risk factor category (10 to 120 days) used to scale expected shortfall from a 10-day base horizon when computing market risk capital under the internal models approach. The source sets out the scaling formula, the nested risk factor subsets and the full table of horizons by risk factor class (interest rate, credit spread, equity, FX, commodity and their volatilities), with specific rules for repo, dividend, basis and inflation risk factors. Binds banks calculating market risk capital under the IMA.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Default Risk Capital (DRC) Requirement|Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When computing the standardised default risk capital charge, you cannot treat it as a free-standing calculation: the framework's liquidity horizon concept governs the holding-period assumption applied to positions, so the same defined term drives both the sensitivities-based and default risk components. The reference means the DRC provisions must be read together with the liquidity horizon definition rather than against a bank's own internal holding-period view. Practically, a capital submission that uses a bespoke horizon for jump-to-default exposures is not compliant unless it matches the horizon specified in the market risk text, which should be verified in the primary articles.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 429): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 429): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"

### [[SAMA — Expected Shortfall (ES)|Expected Shortfall (ES)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 480): "The liquidity horizon of the index is the shortest liquidity horizon (out of 10, 20, 40, 60 and 120 days) that is equal to or longer than the weighted average liquidity horizon."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "Calculation of expected shortfall 13.1 Banks will have flexibility in devising the precise nature of their expected shortfall (ES) models, but the following minimum standards will apply for the purpose of calculating market risk capital requirements."

### [[SAMA — Expected Shortfall (ES) Model|Expected Shortfall (ES) Model]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 480): "The liquidity horizon of the index is the shortest liquidity horizon (out of 10, 20, 40, 60 and 120 days) that is equal to or longer than the weighted average liquidity horizon."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"

## Lookup terms

`liquidity horizon`, `LH`, `base liquidity horizon 10 days`, `liquidity-adjusted ES`, `risk factor category horizons`, `scaling expected shortfall`, `Table 2 liquidity horizons`

#graphify/enriched #source/sama #community/internal-models-approach
