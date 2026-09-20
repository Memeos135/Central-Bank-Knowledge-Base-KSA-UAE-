# Replacement Cost (RC)

Concept node on replacement cost, a core component of exposure at default under SA-CCR, including the formula for margined netting sets based on trade value less collateral, threshold, minimum transfer amount and net independent collateral amount, floored at zero. The framework illustrates its operation through worked examples covering standard margin agreements, variation margin and independent amounts. It applies to banks computing counterparty credit risk exposures under SA-CCR.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Derivative Exposures (Leverage Ratio)|Derivative Exposures (Leverage Ratio)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 786): "10 Future administrative costs: PVAs to take into account the administrative costs and future hedging costs over the expected life of the exposures for which a direct exit price is not applied for the closeout costs."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 699): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[SAMA — EAD Calculation under SA-CCR|EAD Calculation under SA-CCR]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 334): "Whenever the replacement cost is unknown, the exposure measure for CCR will be calculated in a conservative manner by using the sum of the notional amounts of the derivatives in the netting set as a proxy for the replacement cost, and the multiplier used in the calculation of the"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 333): "This includes, for example, any underlying exposure arising from the fund’s derivatives activities for situations in which the underlying receives a risk weighting treatment under the calculation of minimum risk based capital requirements and the associated counterparty credit ri"

### [[SAMA — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** Treat replacement cost as an input to, not an alternative to, the exposure at default figure: for counterparty credit risk the exposure measure is built from RC, and where RC cannot be determined the rules impose a conservative substitute based on notional amounts of the netting set. For a compliance decision this means an EAD number cannot be signed off without confirming how RC was established, since an unknown RC forces the conservative treatment rather than an estimate. Note that the excerpt captured for the EAD node points to defaulted-exposure flow reporting, so verify the primary text to confirm exactly which EAD provision is cross-referenced.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 334): "Whenever the replacement cost is unknown, the exposure measure for CCR will be calculated in a conservative manner by using the sum of the notional amounts of the derivatives in the netting set as a proxy for the replacement cost, and the multiplier used in the calculation of the"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[SAMA — Margin Period of Risk (MPOR)|Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Net Independent Collateral Amount (NICA)|Net Independent Collateral Amount (NICA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"

### [[SAMA — SA-CCR Standardized Approach|SA-CCR Standardized Approach]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 334): "Whenever the replacement cost is unknown, the exposure measure for CCR will be calculated in a conservative manner by using the sum of the notional amounts of the derivatives in the netting set as a proxy for the replacement cost, and the multiplier used in the calculation of the"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 564): "(2) The simple approach or comprehensive approach to the recognition of collateral, which are both set out in the credit risk mitigation chapter of the standardized approach to credit risk (see Chapter 9 on the mitigation techniques for exposures risk-weighted under the standardi"

## Lookup terms

`replacement cost (RC)`, `SA-CCR`, `margined netting set`, `minimum transfer amount (MTA)`, `threshold (TH)`, `net independent collateral amount (NICA)`, `variation margin`, `exposure at default`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
