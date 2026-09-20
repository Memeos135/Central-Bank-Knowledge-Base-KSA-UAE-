# PD Estimation

Sets out the minimum requirements for banks' own estimates of probability of default under the IRB approaches, including the requirement that PD be a long-run average of one-year default rates per borrower grade or retail pool, and the related expectations for LGD and EAD estimation, data sources and empirical grounding. It also covers where supervisory parameters must be used instead (F-IRB, specialised lending, HVCRE). Binds banks permitted by SAMA to use foundation or advanced IRB approaches for credit risk capital.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Data Maintenance Requirements|Data Maintenance Requirements]] — `shares_data_with` [INFERRED]
- **What this link tells you:** This link suggests that the data quality, retention and traceability conditions governing model inputs also constrain what data may be relied on for parameter estimation, so a weakness in the data set is a defect in the estimate itself rather than a separate operational issue. The connection is inferred rather than stated: the extracted text concerns adjustments to risk-theoretical P&L input data and its alignment with hypothetical P&L, which sits in the market risk model-approval provisions, not obviously in the IRB PD estimation requirements. Treat the shared-data reading as tentative and verify in the primary text which data-maintenance article actually feeds the PD estimation obligations before relying on it for a model validation or capital decision.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 471): "12.31 Adjustments to RTPL input data will be allowed when the input data for a given risk factor that is included in both the RTPL and the HPL differs due to different providers of market data sources or time fixing of market data sources, or transformations of market data into i"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 471): "12.31 Adjustments to RTPL input data will be allowed when the input data for a given risk factor that is included in both the RTPL and the HPL differs due to different providers of market data sources or time fixing of market data sources, or transformations of market data into i"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[SAMA — Definition of Default|Definition of Default]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."

### [[SAMA — Definition of Loss (Economic Loss)|Definition of Loss (Economic Loss)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 541): "Specific criteria on loss data identification, collection and treatment: 9.1 Building of the standardized approach loss data set: In order to build an acceptable loss data set from the available internal data, a bank must develop policies and procedures to address several feature"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 541): "Specific criteria on loss data identification, collection and treatment: 9.1 Building of the standardized approach loss data set: In order to build an acceptable loss data set from the available internal data, a bank must develop policies and procedures to address several feature"

### [[SAMA — Expected Loss (EL) Amount|Expected Loss (EL) Amount]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 857): "12 Loss event threshold: 44,600 SAR or 446,000 SAR for the operational risk capital calculation if applicable 13 Definitions Row 1: Based on a loss event threshold of 44,600 SAR, the total loss amount net of recoveries resulting from loss events above the loss event threshold for"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 140): "Expected loss for specialized lending (SL) exposures subject to the supervisory slotting criteria 13.8 For SL exposures subject to the supervisory slotting criteria, the expected loss (EL) amount is determined by multiplying 8% by the risk-weighted assets produced from the approp"

### [[SAMA — Guarantees and Credit Derivatives|Guarantees and Credit Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** If you are deciding whether recognised credit protection can change a capital number, you cannot treat the guarantee/credit-derivative provisions as a standalone concession: they operate through the risk-parameter estimation rules, in this case PD. The guarantees and credit derivatives provisions permit recognition of protection only where the stated minimum operational conditions are met, and the effect is then expressed as a substitution or adjustment within the estimation of the obligor's default probability. Practically, a recognition decision must be evidenced against both limbs — eligibility/operational conditions and conformity with the PD estimation rules — and failing either means the exposure stands unmitigated for capital purposes.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 72): "Guarantees and credit derivatives 9.22 Where guarantees or credit derivatives fulfil the minimum operational conditions set out in paragraphs 9.69 to 9.71, banks may take account of the credit protection offered by such credit risk mitigation techniques in calculating capital req"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 72): "Guarantees and credit derivatives 9.22 Where guarantees or credit derivatives fulfil the minimum operational conditions set out in paragraphs 9.69 to 9.71, banks may take account of the credit protection offered by such credit risk mitigation techniques in calculating capital req"

### [[SAMA — Qualifying Purchased Receivables|Qualifying Purchased Receivables]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 112): "In this context, the relevant assets classes are as follows: (1) Sovereigns (2) Banks (3) Corporates (excluding specialized lending and purchased receivables) (4) Specialized lending (5) Corporate purchased receivables (6) QRRE (7) Retail residential mortgages (8) Other retail (e"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 112): "In this context, the relevant assets classes are as follows: (1) Sovereigns (2) Banks (3) Corporates (excluding specialized lending and purchased receivables) (4) Specialized lending (5) Corporate purchased receivables (6) QRRE (7) Retail residential mortgages (8) Other retail (e"

### [[SAMA — Risk Quantification|Risk Quantification]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Use of Internal Ratings|Use of Internal Ratings]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 203): "Section 6: use of internal ratings 16.59 Internal ratings and default and loss estimates must play an essential role in the credit approval, risk management, internal capital allocations, and corporate governance functions of banks using the IRB approach."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 203): "Section 6: use of internal ratings 16.59 Internal ratings and default and loss estimates must play an essential role in the credit approval, risk management, internal capital allocations, and corporate governance functions of banks using the IRB approach."

### [[SAMA — Validation of Internal Estimates|Validation of Internal Estimates]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 226): "Section 8: validation of internal estimates 16.121 Banks must have a robust system in place to validate the accuracy and consistency of rating systems, processes, and the estimation of all relevant risk components."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 203): "Section 6: use of internal ratings 16.59 Internal ratings and default and loss estimates must play an essential role in the credit approval, risk management, internal capital allocations, and corporate governance functions of banks using the IRB approach."

## Lookup terms

`PD estimation`, `probability of default`, `long-run average one-year default rate`, `IRB approach`, `A-IRB F-IRB`, `borrower grade`, `retail pool`, `specialised lending HVCRE`, `risk quantification`, `own estimates`

#graphify/enriched #source/sama #community/irb-credit-risk-requirements
