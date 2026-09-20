# Eligible Collateral for Margin

Concept node on collateral eligibility, substitution and treatment of provided initial margin under the SAMA margin framework for non-centrally cleared derivatives. It covers dispute resolution over collateral valuation, conditions for substituting alternative collateral (including sufficiency after haircuts), the requirement to exchange initial margin on a gross basis, and holding arrangements ensuring immediate availability on counterparty default and protection of the posting party in insolvency. Binds banks and covered entities collecting or posting margin.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_2757_VER1.md`

## Connections

### [[SAMA — Covered Bonds|Covered Bonds]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When deciding how a secured instrument or posted asset is treated for prudential purposes, check both rule sets rather than assuming one governs: covered bonds are defined by the protection afforded to bondholders through a supervised cover pool, while the margin rules define what may be accepted and re-used as collateral for non-centrally-cleared derivatives. The link is conceptual — both regimes turn on asset quality, segregation and creditor protection — rather than an express cross-reference, so covered bonds may appear as an eligible collateral category in the margin framework without either text governing the other. Practically, a bank should apply the covered bond rules for issuance/exposure treatment and the margin rules separately for eligibility, haircuts and re-hypothecation limits. Because this link is inferred, verify in the primary texts whether the margin framework in fact lists covered bonds as eligible before relying on the overlap.
- **Grounding — this node** (SAMA_EN_2757_VER1 · Page 14): " Where the initial margin collector re-hypothecates initial margin, the agreement with the recipient of the collateral (ie the third party) must prohibit the third party from further re-hypothecating the collateral."
- **Grounding — related node** (SAMA_EN_2340_VER1 · Page 33): "Covered bonds are bonds issued by a bank or mortgage institution and are subject by law to special public supervision designed to protect bond holders."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — Margin Requirements for Non-centrally Cleared Derivatives|Margin Requirements for Non-centrally Cleared Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_2757_VER1 · Page 3): "Margin requirements for non-centrally cleared derivatives have two main benefits:  Reduction of systemic risk: Margin requirements for non-centrally cleared derivatives would be expected to reduce contagion and spillover effects by ensuring that collateral is available to offset"
- **Grounding — related node** (SAMA_EN_2757_VER1 · Page 3): "Margin requirements for non-centrally cleared derivatives have two main benefits:  Reduction of systemic risk: Margin requirements for non-centrally cleared derivatives would be expected to reduce contagion and spillover effects by ensuring that collateral is available to offset"

## Lookup terms

`eligible collateral`, `haircuts`, `collateral substitution`, `collateral valuation dispute`, `gross exchange of initial margin`, `segregation of margin`, `bankruptcy remoteness`

#graphify/enriched #source/sama #community/large-exposures-framework
