# SAMA Minimum Capital Requirements for Credit Risk

This node gathers the credit-related elements within SAMA's market risk capital framework: specific risk capital treatment for first-to-default and nth-to-default credit derivatives (including hedging offsets), internal CVA risk transfers between the CVA portfolio and the trading book, and the general provisions of the standardised approach. Notably, it records that all banks (D-SIB and non-D-SIB) must compute the market risk capital charge using the standardised approach, with RWA derived by a 12.5 multiplier. It binds SAMA-licensed banks with trading book and derivative exposures.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[SAMA — Credit Valuation Adjustment (CVA)|Credit Valuation Adjustment (CVA)]] — `cites` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 652): "(1) interest rate risk; (IR); (2) FX risk; (3) reference credit spread risk; (4) equity risk; and (5) commodity risk Version Minimum Capital Requirements for Counterparty Credit Risk (CCR) and 103 of 145 Issue Date December 2022 Page Number Credit Valuation Adjustment (CVA) 1.1"

### [[SAMA — Default Risk Capital (DRC) Requirement|Default Risk Capital (DRC) Requirement]] — `cites` [EXTRACTED]
- **What this link tells you:** The default risk capital requirement sits inside the market risk standardised approach but reaches across to the credit risk framework, so the two regimes must be read together when capitalising jump-to-default exposure on trading book instruments. The citation matters because it drives consistency of inputs and treatment between the credit risk rules and the DRC component rather than allowing a standalone market risk methodology. For a compliance decision, check that trading book default exposures are neither omitted nor double-counted against banking book credit risk charges, and confirm the exact cross-referenced provisions in the primary text before relying on a specific alignment.
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`specific risk capital requirement`, `first-to-default credit derivative`, `nth-to-default`, `credit valuation adjustment (CVA)`, `internal risk transfer`, `standardised approach market risk`, `D-SIB`, `risk-weighted assets 12.5`

#graphify/enriched #source/sama #community/trading-book-boundary
