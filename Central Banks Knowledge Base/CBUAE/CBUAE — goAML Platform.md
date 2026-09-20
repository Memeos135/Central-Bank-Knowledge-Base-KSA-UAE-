# goAML Platform

Describes use of the goAML portal as the single reporting channel for both suspicious activity and targeted financial sanctions matters. Confirmed sanctions matches must be reported as a Fund Freeze Report within two business days and potential matches as a Partial Name Match Report, with suspension maintained until goAML instructions are received; these reports reach the Central Bank and Executive Office simultaneously. Separately, STRs/SARs and other report types must be filed without delay regardless of amount, using information from both ordering and beneficiary sides, with terrorism-financing suspicions reported within 24 hours; binds Licensed Persons and their Compliance Officers.

**Regimes:** AML/CTF, sanctions/TFS

## Sources

- `corpus/markdown/CBUAE_EN_3524_VER1.md`
- `corpus/markdown/CBUAE_EN_6788_VER1.md`

## Connections

### [[CBUAE — Sanctions Screening|Sanctions Screening]] — `references` [EXTRACTED]
- **What this link tells you:** A screening alert is not the end of the obligation — the screening control and the reporting channel are a single chain, so a potential or partial match against applicable sanctions lists must be escalated through the FIU reporting platform using the designated partial-match report type. The basis is that real-time screening is embedded in the KYC process for all parties to a transaction, and the outcome of that screening feeds a prescribed regulatory report. Practically, a compliance decision to clear a name internally does not discharge the reporting duty; confirm which report type and timing applies before closing the alert.
- **Grounding — this node** (CBUAE_EN_3524_VER1 · Page 111): "any match between data in the sanctions lists with any information in the Licensed Person’s databases), the Licensed Person is required to report the potential match via the goAML platform by selecting the Partial Name Match Report (PMNR)."
- **Grounding — related node** (CBUAE_EN_3524_VER1 · Page 109): "16.25 Sanctions Screening 16.25.1 Appropriate systems must be introduced for real time screening, as part of the KYC process, on all parties involved in a transaction against all applicable sanction lists (i.e."

### [[CBUAE — Suspicious Transaction Report (STR)|Suspicious Transaction Report (STR)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_6788_VER1 · Page 44): "(74) of 2020, LFIs are expected to report any freezing measures, prohibition to provide funds or services, and any attempted transactions immediately via the goAML platform by selecting the Funds Freeze Report (“FFR”) option."
- **Grounding — related node** (CBUAE_EN_418_VER2 · Page 15): "The STR and SAR are the primary (or first instance) reports which must be used to report a new suspicion, whereas Additional Information File without Transactions (“AIF”) and Additional Information File with Transactions (“AIFT”) report types are supplementary reports which can b"

### [[CBUAE — Suspicious TransactionActivity Reporting|Suspicious Transaction/Activity Reporting]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_6788_VER1 · Page 45): "Alternatively, transactions may be suspicious because, together with other transactions, they form a pattern that diverges from expected or historical transactional activity and may otherwise be indicative of illicit activity."
- **Grounding — related node** (CBUAE_EN_6587_VER1 · Page 30): "As part of this account activity review, the LFI should review the respondent’s transactional activity, paying close attention to whether transactional activity is inconsistent with due diligence information or expected activity and whether there are any material changes in the v"

## Lookup terms

`goAML`, `Fund Freeze Report`, `FFR`, `Partial Name Match Report`, `PNMR`, `STR`, `SAR`, `FIU reporting deadlines`

#graphify/enriched #source/cbuae #community/suspicious-transaction-reporting
