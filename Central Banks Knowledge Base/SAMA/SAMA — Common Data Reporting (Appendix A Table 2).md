# Common Data Reporting (Appendix A Table 2)

Appendix A Table 2 of the SAMA OTC derivatives reporting requirements, covering the common/transaction-level data fields (e.g. internal unique trade ID, notional, early termination date, action type) used for reporting reportable transactions and their subsequent business events to the SAMA-authorised trade repository. It is applied through a life-cycle approach with a T+1 reporting deadline (Fridays, Saturdays and KSA holidays excluded) and record-keeping sufficient to demonstrate compliance. Binds SAMA-licensed reporting banks.

**Regimes:** banking prudential, governance/risk, data/credit info

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[SAMA — Action Type  Life Cycle Events|Action Type / Life Cycle Events]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 55): "If the reporting counterparty (or the other counterparty upon communication to the reporting counterparty) detects that a report (no matter its nature or “Action type”) was submitted by error, the reporting counterparty is required to submit an error report (table 2 item 53 “Acti"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"

### [[SAMA — Collateral Evolutive Fields (Table 3)|Collateral Evolutive Fields (Table 3)]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When determining what must be submitted for a given trade, the collateral fields and the common data table operate as one reporting record, not separable filings. The collateral evolutive fields (e.g. currency and value of excess collateral posted or received) sit alongside the common data elements that drive lifecycle handling, such as the action type used for modification reports on notional changes. Practically, a change reported through common data must be reflected consistently in the associated collateral values; inconsistency across the two tables is a reporting-quality failure under the same instrument, so confirm field-level linkage in the appendix itself.
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 55): "For reporting purposes, in the event of an increase or decrease in the notional amount of an existing contract (partial termination but not fully close-out), the reporting counterparty shall submit a modification report (table 2 item 53 “Action type” populated with the value “M’’"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 43): "3 13 Parties to the | Currency of the | Specify the currency of the excess collateral | ISO 4217 Currency Code, 3 alphabetical characters contract - excess collateral | posted Collateral posted 3 14 Parties to the | Excess Value of collateral received in excess of the | Up to 20 "
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[SAMA — Unique Product Identifier (UPI)|Unique Product Identifier (UPI)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 5): "If, however, the transaction is booked in KSA branch of Bank Y, reporting obligation rules must be applied to determine the reporting counterparty as per the single sided reporting obligation approach as mentioned in Appendix C."
- **Grounding — related node** (SAMA_EN_10592_VER1 · Page 22): "2 6 Section 2b-— | Product The product shall be identified through ISIN or | For product identifier type I: ISO 6166 ISIN 12- Contract identification | UPI depending on the identifier availability."

### [[SAMA — Unique Trade Identifier|Unique Trade Identifier]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 8): "After an original trade is novated for central clearing, the reporting bank should report the open trade as an early termination business events and open a new one with the reference to the old trade identifier in the field “Linked UTI” (table 3 item 47) as specified in the Appen"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 8): "After an original trade is novated for central clearing, the reporting bank should report the open trade as an early termination business events and open a new one with the reference to the old trade identifier in the field “Linked UTI” (table 3 item 47) as specified in the Appen"

## Lookup terms

`common data Table 2`, `internal unique trade ID`, `notional`, `T+1 reporting timeline`, `life cycle approach`, `business events reporting`, `Linked UTI`, `record keeping reporting bank`

#graphify/enriched #source/sama #community/otc-derivatives-reporting
