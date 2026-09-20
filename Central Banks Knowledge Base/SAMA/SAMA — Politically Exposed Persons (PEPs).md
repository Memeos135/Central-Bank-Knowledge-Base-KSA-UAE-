# Politically Exposed Persons (PEPs)

This node addresses politically exposed persons within SAMA's AML/CTF guide, treating PEP determination as a customer due diligence measure supporting the risk-based approach. It requires financial institutions to use reasonable tools and credible databases to establish whether a customer or beneficial owner is a domestic or foreign PEP, and to apply enhanced due diligence to high-risk PEP relationships, extending to family members and close associates. It binds SAMA-supervised financial institutions and links to the AML Law's requirement for internal procedures and tools to identify PEPs.

**Regimes:** AML/CTF, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_1704_VER1.md`

## Connections

### [[SAMA — Beneficial Owner|Beneficial Owner]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** For onboarding and ongoing due diligence, these two are sequential steps in the same CDD chain rather than alternatives: you must first identify and verify the beneficial owner from authenticated, independent sources, and that outcome then feeds the PEP determination, which is itself described as a CDD measure applying the risk-based approach. The practical consequence is that a PEP screening performed only on the named account holder is incomplete — if a beneficial owner (or their close associate/family member, per the applicable definition) is a PEP, enhanced due diligence and senior management approval obligations are triggered at the relationship level. Treat a failure to resolve beneficial ownership as blocking a defensible PEP conclusion. The linkage is inferred from the structure of the CDD provisions, so verify the specific article wording before relying on it in a file decision.
- **Grounding — this node** (SAMA_EN_1704_VER1 · Page 39): "Politically Exposed Persons (PEPs) Identifying a PEP and the extent to which that person is considered politically exposed is one of the customer due diligence measures taken by the financial institution to implement the risk-based approach in conducting its business."
- **Grounding — related node** (SAMA_EN_1704_VER1 · Page 28): "c) The financial institution shall identify the beneficial owner and take adequate measures to verify the identity of the beneficial owner using documents, data or information from an authenticated and independent source as mentioned under the Beneficial Owner Section."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — Enhanced Due Diligence Measures|Enhanced Due Diligence Measures]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_1704_VER1 · Page 39): "Politically Exposed Persons (PEPs) Identifying a PEP and the extent to which that person is considered politically exposed is one of the customer due diligence measures taken by the financial institution to implement the risk-based approach in conducting its business."
- **Grounding — related node** (SAMA_EN_1704_VER1 · Page 38): "4.5 When discovering that another financial institution has refused to deal with a specific customer, the financial institution shall implement enhanced due diligence measures, know the reasons behind that refusal, and take additional due diligence measures if the reason for refu"

## Lookup terms

`politically exposed persons`, `PEP`, `foreign and domestic PEP`, `family members and close associates`, `enhanced due diligence (EDD)`, `PEP screening database`, `illicit enrichment`, `high-risk business relationship`

#graphify/enriched #source/sama #community/aml/ctf-due-diligence
