# Collateral Evolutive Fields (Table 3)

A data-field specification (Table 3, "Evolutive Field – Common Data") within SAMA's trade repository reporting and risk mitigation requirements for OTC derivative contracts, setting out the collateral-related attributes a reporting bank must populate. It covers the collateralisation status of the contract (uncollateralised, partially, one-way or fully collateralised), portfolio collateralisation and portfolio code, initial and variation margin posted/received, excess collateral, and the ISO currency codes and character/decimal formats for each. It binds banks subject to the OTC derivatives reporting obligation when submitting trade data to the SAMA-authorised trade repository operator.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[SAMA — Common Data Reporting (Appendix A Table 2)|Common Data Reporting (Appendix A Table 2)]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When determining what must be submitted for a given trade, the collateral fields and the common data table operate as one reporting record, not separable filings. The collateral evolutive fields (e.g. currency and value of excess collateral posted or received) sit alongside the common data elements that drive lifecycle handling, such as the action type used for modification reports on notional changes. Practically, a change reported through common data must be reflected consistently in the associated collateral values; inconsistency across the two tables is a reporting-quality failure under the same instrument, so confirm field-level linkage in the appendix itself.
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 43): "3 13 Parties to the | Currency of the | Specify the currency of the excess collateral | ISO 4217 Currency Code, 3 alphabetical characters contract - excess collateral | posted Collateral posted 3 14 Parties to the | Excess Value of collateral received in excess of the | Up to 20 "
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 55): "For reporting purposes, in the event of an increase or decrease in the notional amount of an existing contract (partial termination but not fully close-out), the reporting counterparty shall submit a modification report (table 2 item 53 “Action type” populated with the value “M’’"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`collateral evolutive fields`, `OTC derivatives trade repository reporting`, `initial margin posted`, `variation margin received`, `excess collateral`, `collateral portfolio code`, `fully collateralised / partially collateralised`, `ISO 4217 currency code field format`

#graphify/enriched #source/sama #community/otc-derivatives-reporting
