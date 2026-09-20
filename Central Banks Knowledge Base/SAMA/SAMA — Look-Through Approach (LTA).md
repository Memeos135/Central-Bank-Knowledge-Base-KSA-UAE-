# Look-Through Approach (LTA)

This node explains the look-through approach (LTA) for exposures held indirectly through structures: when a bank must identify and assign exposures to underlying counterparties, when it may instead assign the amount to the structure, and when unidentified underlyings must be assigned to the "unknown client" and aggregated as a single counterparty subject to the large exposure limit. It also prescribes pro rata attribution for pari passu structures, a tranche-based method where investors rank differently, and an anti-arbitrage expectation where LTA is not applied. It binds SAMA-supervised banks with fund, securitisation or similar structured investments.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_2340_VER1.md`
- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Collective Investment Undertakings and Securitization Vehicles|Collective Investment Undertakings and Securitization Vehicles]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 13): "Equity investments in funds 325 The look-through approach 325 The mandate-based approach 326 The fall-back approach 328 Treatment of funds that invest in other funds 328 Partial use of an approach 328 Leverage adjustment 329 Application of the LTA and MBA to banks using the IRB a"
- **Grounding — related node** (SAMA_EN_2340_VER1 · Page 16): "Collective investment undertakings, securitizations vehicles and other structures;"

### [[SAMA — Credit Valuation Adjustment (CVA)|Credit Valuation Adjustment (CVA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 13): "Equity investments in funds 325 The look-through approach 325 The mandate-based approach 326 The fall-back approach 328 Treatment of funds that invest in other funds 328 Partial use of an approach 328 Leverage adjustment 329 Application of the LTA and MBA to banks using the IRB a"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 755): "Credit valuation adjustment (row 3): Definition of standardised approach: The standardised approach for CVA (SA-CVA), the basic approach (BA-CVA) or 100% of a bank’s counterparty credit risk capital requirements (depending on which approach the bank uses for CVA risk)."

### [[SAMA — Equity Investments in Funds|Equity Investments in Funds]] — `shares_data_with` [INFERRED]
- **What this link tells you:** If a bank holds equity investments in funds in the banking book, the choice of capital treatment is made within a single hierarchy, and the look-through approach is the first and most risk-sensitive option in that hierarchy. The two provisions sit in the same instrument: the equity-investments-in-funds rules set the scope and the conditions for selecting among the look-through, mandate-based and fall-back approaches, and the LTA provisions supply the mechanics, including leverage adjustment and interaction with IRB. The practical consequence is that eligibility for LTA depends on sufficient and verifiable information about the fund's underlying exposures; where that is unavailable, the bank falls down the hierarchy to a more conservative approach. Read the two sections together rather than as independent rules.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 13): "Equity investments in funds 325 The look-through approach 325 The mandate-based approach 326 The fall-back approach 328 Treatment of funds that invest in other funds 328 Partial use of an approach 328 Leverage adjustment 329 Application of the LTA and MBA to banks using the IRB a"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 332): "Equity investments in funds Introduction 24.1 Equity investments in funds that are held in the banking book must be treated in a manner consistent with one or more of the following three approaches, which vary in their risk sensitivity and conservatism: the “look-through approach"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`look-through approach`, `LTA`, `unknown client`, `pari passu structure`, `pro rata share underlying asset`, `seniority tranche exposure`, `regulatory arbitrage`, `nominal amount invested`

#graphify/enriched #source/sama #community/trading-book-boundary
