# Credit Conversion Factors (CCF)

Concept node for credit conversion factors, the mechanism converting off-balance sheet items into on-balance sheet credit exposure equivalents for risk weighting. Identifies the categories attracting a 100% CCF (direct credit substitutes, sale and repurchase agreements and asset sales with recourse, forward asset purchases and certain commitments, securities lending or posting of securities as collateral, and other unclassified credit substitutes) alongside lower CCF bands, and interacts with CRM rules where the converted exposure is collateralised. Binds banks computing credit risk-weighted assets and, separately, exposure measures for leverage purposes.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`
- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — Counterparty Credit Risk (SA-CCR)|Counterparty Credit Risk (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** For off-balance-sheet exposures, the decision point is which measurement route applies: credit conversion factors convert commitments and similar items into credit exposure equivalents under the standardised credit risk approach, whereas derivative and securities-financing exposures are measured as counterparty credit risk exposure (SA-CCR) rather than by CCF. The cross-reference matters because counterparty risk is also a risk type that must be captured in the institution's internal capital adequacy assessment, so the same exposures feed both Pillar 1 measurement and Pillar 2 risk scoping. Reviewers should confirm, for each off-balance-sheet item, that it is not double-counted or omitted between the CCF and counterparty-risk treatments, and verify the specific provision in the primary text since the linked passage addresses risk scope generally.
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 32): "Off-Balance Sheet Items: Credit Conversion Factors Under the standardised approach, off-balance sheet items are converted into credit exposure equivalents with Credit Conversion Factors (CCFs)."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 169): "At a minimum, the scope of risks should cover strategic risk, credit risk, market risk, counterparty risk, operational risk, liquidity risk, IRRBB, credit concentration risk, funding risk, reputational risk, and climate risk."

### [[CBUAE — Credit Risk|Credit Risk]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 32): "Off-Balance Sheet Items: Credit Conversion Factors Under the standardised approach, off-balance sheet items are converted into credit exposure equivalents with Credit Conversion Factors (CCFs)."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 169): "At a minimum, the scope of risks should cover strategic risk, credit risk, market risk, counterparty risk, operational risk, liquidity risk, IRRBB, credit concentration risk, funding risk, reputational risk, and climate risk."

### [[CBUAE — Credit Risk Standardised Approach|Credit Risk Standardised Approach]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 32): "Off-Balance Sheet Items: Credit Conversion Factors Under the standardised approach, off-balance sheet items are converted into credit exposure equivalents with Credit Conversion Factors (CCFs)."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 35): "Section IV on credit risk mitigation sets out the requirements for the calculation of risk-weighted assets where the credit converted exposure is secured by eligible collateral; (v) Off-balance sheet items that are credit substitutes not explicitly included in any other category "

### [[CBUAE — Leverage Ratio Standard (CBUAE 1691)|Leverage Ratio Standard (CBUAE 1691)]] — `references` [EXTRACTED]
- **What this link tells you:** A leverage exposure calculation cannot be completed without applying the credit conversion factors used to bring off-balance-sheet items into exposure measures, so the two instruments must be read together when sizing the denominator. The Leverage Ratio Standard relies on the CCF treatment defined in the standardised credit risk material rather than restating it. The consequence is that any change in CCF classification or the standardised approach flows directly into the reported leverage ratio and must be reflected in both credit risk and leverage reporting.
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 32): "Off-Balance Sheet Items: Credit Conversion Factors Under the standardised approach, off-balance sheet items are converted into credit exposure equivalents with Credit Conversion Factors (CCFs)."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 4): "Application The following Standards are already in effect as follows:  The Tier Capital Supply Standard  Tier Capital Instruments Standard  Pillar 2 Standard The remaining Standards are effective from Q2 2021 onwards."

## Lookup terms

`credit conversion factor`, `CCF`, `off-balance sheet items`, `direct credit substitutes`, `100% CCF 50% CCF`, `undrawn commitments`, `written credit derivative`, `leverage ratio exposure measure`

#graphify/enriched #source/cbuae #community/credit-risk-standardised-approach
