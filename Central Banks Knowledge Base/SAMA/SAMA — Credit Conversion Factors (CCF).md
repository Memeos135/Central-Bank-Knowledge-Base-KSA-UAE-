# Credit Conversion Factors (CCF)

Concept node on credit conversion factors used to convert off-balance sheet items into credit exposure equivalents under SAMA's credit risk standard, including the 10% CCF for unconditionally cancellable commitments, SAMA's discretion to impose higher CCFs, and the rule to apply the lower of two CCFs where a commitment to provide a commitment exists. Also touches adjacent treatments for exposures giving rise to counterparty credit risk and for written/purchased credit derivatives (first-, second- and nth-to-default). Binds banks computing RWA under SAMA's Basel III frameworks.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`
- `corpus/markdown/SAMA_EN_4303_VER1.md`

## Connections

### [[SAMA — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** The linkage matters when quantifying exposure on off-balance-sheet and undrawn items: the credit conversion factor is the mechanism that converts a committed or contingent amount into the exposure at default used for RWA and for defaulted-exposure reporting. EAD is therefore not a freestanding input but the output of applying the prescribed or estimated CCF to the relevant facility amount. In practice, any challenge to the CCF applied (supervisory versus own estimates, and the facility classification behind it) flows directly through to reported EAD, capital requirements and the stock-of-defaulted-exposures disclosures. Note the excerpts here are imperfectly aligned, so the reader should verify the specific CCF and EAD paragraphs in the primary text before relying on them.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 661): "The counterparty credit spread delta risk factors for a given bucket: (1) The counterparty credit spread delta risk factors are absolute shifts of credit spreads of individual entities (counterparties and reference names for counterparty credit spread hedges) and qualified indice"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[SAMA — Leverage Ratio Framework|Leverage Ratio Framework]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 723): "(iii) OBS items are converted under the standardized approach for credit risk into credit exposure equivalents through the use of credit conversion factors (CCFs) as mentioned in the latest risk-based capital framework adopted by SAMA."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "2 3 Leverage ratio: Leverage ratio which would trigger capital distribution constraints, should the bank’s leverage ratio fall below this level."

### [[SAMA — Off-Balance Sheet Items|Off-Balance Sheet Items]] — `references` [EXTRACTED]
- **What this link tells you:** If you are sizing exposure on commitments, guarantees or other off-balance-sheet positions, the credit conversion factor provision is the operative step that turns those positions into on-balance-sheet-equivalent credit exposure for RWA purposes. Both instruments carry the same provision and numbering, so they are two expressions of one rule within the credit risk framework rather than two independent obligations. The decision point is therefore which instrument and version is currently in force for your reporting date, since applying superseded conversion factors would misstate credit RWA.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 53): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 46): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."

### [[SAMA — Off-Balance Sheet Items Treatment|Off-Balance Sheet Items Treatment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 53): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[SAMA — SCRE - Minimum Capital Requirements for Credit Risk|SCRE - Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When converting off-balance-sheet commitments into exposure amounts, the credit conversion factor provisions cannot be applied standalone — they operate as a component of the standardised credit risk capital requirements. Both sit within the same SAMA capital instrument and share its defined terms (including the risk class taxonomy), so the CCF outcome feeds directly into the exposure base to which SCRE risk weights are applied. In practice, any classification or CCF judgement should be validated against the SCRE definitions and asset class rules rather than resolved in isolation.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`credit conversion factor`, `CCF off-balance sheet`, `unconditionally cancellable commitment`, `written credit derivative`, `first-to-default credit derivative`, `effective notional amount`, `counterparty credit risk exposure`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
