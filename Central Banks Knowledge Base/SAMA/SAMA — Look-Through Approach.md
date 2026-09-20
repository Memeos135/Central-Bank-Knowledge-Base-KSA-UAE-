# Look-Through Approach

This node governs when banks must look through index instruments, multi-underlying options and equity investments in funds to their constituent risk factors for delta and curvature risk, and when a single index-level sensitivity may instead be used. It lists the eligibility criteria for opting out (known constituents, at least 20 constituents, concentration limits, and a minimum aggregate market capitalisation), requires consistent application over time, and excludes index CTP instruments from decomposition. It binds SAMA-licensed banks applying the sensitivities-based standardised approach to market risk.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Default Risk Capital (DRC) Requirement|Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** For exposures held through funds, indices or other pooled vehicles, the decision on how to measure jump-to-default risk is determined by the look-through approach, which the DRC provisions invoke. The link signals an obligation chain: the DRC charge is calculated on the underlying constituent obligors where look-through is required and available, not on the vehicle as a single name. The consequence is that failure to look through can understate the default risk capital requirement and would be treated as a misapplication of the standardised approach.
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 73): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 429): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"

### [[SAMA — Equity Investments in Funds|Equity Investments in Funds]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 12): "3.11 All banks must calculate the market risk capital requirement using the standardised approach for the following: (1) Securitisation exposures; and (2) Equity investments in funds that cannot be looked through but are assigned to the trading book in accordance to the condition"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 332): "Equity investments in funds Introduction 24.1 Equity investments in funds that are held in the banking book must be treated in a manner consistent with one or more of the following three approaches, which vary in their risk sensitivity and conservatism: the “look-through approach"

## Lookup terms

`look-through approach`, `index instruments`, `multi-underlying options`, `equity investments in funds`, `delta and curvature risk`, `index bucket`, `correlation trading portfolio (CTP)`, `sensitivities-based method`

#graphify/enriched #source/sama #community/trading-book-boundary
