# Custody

This node addresses custodial arrangements in repo: participants must understand the terms, rights and obligations of any custody agreement before entering repos with custodial arrangements, and licensed banks must maintain custody arrangements and processes for held-in-custody eligible securities, including monitoring and segregation to prevent duplicative use of the same securities. Surrounding context covers collateral price sources and valuation (agreed sources, dirty prices, waterfall approach, dispute handling) and leads into reporting and settlement. Binds repo market participants, with the heavier obligation on SAMA-licensed banks acting as custodians.

**Regimes:** governance/risk, banking prudential

## Sources

- `corpus/markdown/SAMA_EN_6073_VER1.md`

## Connections

### [[SAMA — Eligible Securities|Eligible Securities]] — `shares_data_with` [INFERRED]
- **What this link tells you:** The scoping question comes first: the custody, segregation and monitoring duties placed on a licensed bank attach to securities that qualify as eligible securities held on behalf of repo participants, so eligibility determination drives whether the custody obligation is engaged at all. Both concepts are drawn from the same operative provision, which is why the defined term and the obligation share the same reference data about the held-in-custody positions. For a decision, confirm the instrument's eligibility status, then apply the full segregation and duplication-risk controls to those positions; instruments outside the definition are governed by the bank's general custody arrangements rather than this rule. Verify the definitional article directly, as the boundary of eligible securities is where most disputes arise.
- **Grounding — this node** (SAMA_EN_6073_VER1 · Page 9): "A licensed bank shall have in place custody arrangement and processes for eligible securities held-in-custody on behalf of the repo participants, including comprehensive systems and processes to monitor and segregate the held-in- custody securities to mitigate the risk of duplica"
- **Grounding — related node** (SAMA_EN_6073_VER1 · Page 9): "A licensed bank shall have in place custody arrangement and processes for eligible securities held-in-custody on behalf of the repo participants, including comprehensive systems and processes to monitor and segregate the held-in- custody securities to mitigate the risk of duplica"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[SAMA — SAMA Guidelines on Repurchase Agreements|SAMA Guidelines on Repurchase Agreements]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_6073_VER1 · Page 9): "A licensed bank shall have in place custody arrangement and processes for eligible securities held-in-custody on behalf of the repo participants, including comprehensive systems and processes to monitor and segregate the held-in- custody securities to mitigate the risk of duplica"
- **Grounding — related node** (SAMA_EN_6073_VER1 · Page 2): "Saudi Central Bank (SAMA) Guidelines on Repurchase Agreements"

## Lookup terms

`repo custody arrangement`, `held-in-custody segregation`, `custodian collateral management`, `duplicative use of securities`, `price sources valuation dirty price`, `margin call dispute waterfall`

#graphify/enriched #source/sama #community/repurchase-&-securities-agreements
