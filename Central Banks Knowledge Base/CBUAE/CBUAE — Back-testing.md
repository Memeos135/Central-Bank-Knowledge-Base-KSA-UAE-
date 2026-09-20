# Back-testing

This node governs a Bank's back-testing programme for internal market risk measurement models: formal quarterly evaluation of exceptions (trading outcomes not covered by the risk measures) using the most recent twelve months of modelled results and profit data, documentation and explanation of every exception, and capacity to back-test at both whole-portfolio and material sub-portfolio/book level. Back-tests must use both actual (cleaned of fees, commissions, brokerage and non-market-risk reserve movements) and hypothetical trading outcomes. It binds Banks using internal models and feeds into model validation and trading book capital charge provisions.

**Regimes:** governance/risk, banking prudential

## Sources

- `corpus/markdown/CBUAE_EN_1430_VER1.md`

## Connections

### [[CBUAE — Internal Validation|Internal Validation]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** Back-testing should be assessed as one input into the model validation framework, not as a standalone compliance item: the validation requirements place initial and ongoing model assessment under Board-approved policies with independent review, and back-testing results are among the evidence that ongoing validation relies on. Both provisions sit in the same market risk instrument, which makes the governance chain run from Board policy, through validation, to the testing programme. In practice, deficient or too-short back-testing exposes the firm on the validation obligation as well; the linkage is inferred, so check the primary text for how explicitly back-testing is tied to validation.
- **Grounding — this node** (CBUAE_EN_1430_VER1 · Page 12): "Testing carried out for longer than required for the regular back-testing program (for instance 3 years)."
- **Grounding — related node** (CBUAE_EN_1430_VER1 · Page 11): "Development, internal approval and ongoing use of models and other market risk management methodologies must be governed by Board-approved policies and procedures, which at a minimum must address initial and ongoing validation, valuation and independent review by the internal aud"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[CBUAE — Valuation|Valuation]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1430_VER1 · Page 12): "Testing carried out for longer than required for the regular back-testing program (for instance 3 years)."
- **Grounding — related node** (CBUAE_EN_1430_VER1 · Page 14): "Valuation adjustments must be made as appropriate (for example, to cover the uncertainty of the model valuation)."

## Lookup terms

`back-testing`, `exceptions`, `clean trading outcomes`, `hypothetical trading outcomes`, `internal model validation`, `market risk measurement model`, `capital charge trading book`

#graphify/enriched #source/cbuae #community/market-risk-controls
