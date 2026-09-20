# Beneficial Owner

This node covers the beneficial owner identification and verification obligations within SAMA's AML/CTF guide for financial institutions, anchored in the AML Law Implementing Regulations and the counter-terrorism financing regulations. It sets out that the beneficial owner must be a natural person who directly or indirectly owns or controls a legal person, applies a 25% ownership/control threshold as a starting point, and prescribes cascading fallback measures (senior management, sub-25% controllers, EDD, record keeping) where no such person is identified or where suspicion arises. It binds financial institutions supervised by SAMA and requires that CDD intensity be calibrated to assessed risk, with reliance on the customer's own written statement expressly insufficient.

**Regimes:** AML/CTF, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_1704_VER1.md`

## Connections

### [[SAMA — Due Diligence Measures|Due Diligence Measures]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_1704_VER1 · Page 28): "c) The financial institution shall identify the beneficial owner and take adequate measures to verify the identity of the beneficial owner using documents, data or information from an authenticated and independent source as mentioned under the Beneficial Owner Section."
- **Grounding — related node** (SAMA_EN_1704_VER1 · Page 43): "5.3 Application of the simplified measures does not mean exemption from the requirements of customer due diligence, but rather the application of due diligence measures in a streamlined and simplified manner consistent with the ML/TF risks posed by the customer or beneficial owne"

### [[SAMA — Politically Exposed Persons (PEPs)|Politically Exposed Persons (PEPs)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** For onboarding and ongoing due diligence, these two are sequential steps in the same CDD chain rather than alternatives: you must first identify and verify the beneficial owner from authenticated, independent sources, and that outcome then feeds the PEP determination, which is itself described as a CDD measure applying the risk-based approach. The practical consequence is that a PEP screening performed only on the named account holder is incomplete — if a beneficial owner (or their close associate/family member, per the applicable definition) is a PEP, enhanced due diligence and senior management approval obligations are triggered at the relationship level. Treat a failure to resolve beneficial ownership as blocking a defensible PEP conclusion. The linkage is inferred from the structure of the CDD provisions, so verify the specific article wording before relying on it in a file decision.
- **Grounding — this node** (SAMA_EN_1704_VER1 · Page 28): "c) The financial institution shall identify the beneficial owner and take adequate measures to verify the identity of the beneficial owner using documents, data or information from an authenticated and independent source as mentioned under the Beneficial Owner Section."
- **Grounding — related node** (SAMA_EN_1704_VER1 · Page 39): "Politically Exposed Persons (PEPs) Identifying a PEP and the extent to which that person is considered politically exposed is one of the customer due diligence measures taken by the financial institution to implement the risk-based approach in conducting its business."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`beneficial owner`, `BO identification`, `25% ownership threshold`, `controlling interest`, `legal person ownership structure`, `customer due diligence (CDD)`, `risk-based approach`, `verification from independent source`

#graphify/enriched #source/sama #community/aml/ctf-due-diligence
