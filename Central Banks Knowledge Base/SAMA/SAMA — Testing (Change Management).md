# Testing (Change Management)

Testing controls within the system change management section of the SAMA IT Governance Framework. It requires documented test cases with defined attributes, minimum testing types (unit, system integration, stress where applicable, security and user acceptance testing), testing in a separate test environment, formal business-user acceptance, positive and negative scenarios, retention of UAT results, and use of sanitised rather than production data. It also flags third-party testing certification where applicable. Binds Member Organizations.

**Regimes:** governance/risk, data/credit info

## Sources

- `corpus/markdown/SAMA_EN_4066_VER1.md`

## Connections

### [[SAMA — Change Security Requirements|Change Security Requirements]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When deciding whether a system change can be promoted to production, the security requirements applied to the change and the testing expectations operate as sequential gates within the same change management policy. Security criteria define what the change must satisfy; testing is the control that evidences satisfaction before deployment, including after periodic policy reviews or changes in laws and regulatory requirements. For a compliance decision, absence of documented testing evidence generally means the security requirement cannot be treated as met, regardless of design intent. The linkage is inferred from the shared change management provisions, so confirm the sequencing and approval steps in the primary text.
- **Grounding — this node** (SAMA_EN_4066_VER1 · Page 27): "System change management process should be governed by the change management policy and procedure that should be approved, monitored, reviewed and updated on periodic basis and/or whenever significant changes occurs in the IT environment or changes in laws and regulatory requirem"
- **Grounding — related node** (SAMA_EN_4066_VER1 · Page 27): "System change management process should be governed by the change management policy and procedure that should be approved, monitored, reviewed and updated on periodic basis and/or whenever significant changes occurs in the IT environment or changes in laws and regulatory requirem"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — Quality Assurance|Quality Assurance]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When assessing whether a change can be promoted to production, treat quality assurance and change-management testing as two controls in the same gate rather than alternatives. Both sit within the same IT governance framework: the testing requirement is governed by an approved, periodically reviewed change management policy, while quality assurance requires an independently defined, approved and communicated process confirming that developments or changes meet business and user requirements before go-live. Practically, evidencing testing alone will not satisfy the independent assurance expectation, and a gap in either will be read as a deficiency in controlled change. This linkage is inferred from thematic proximity, so the reader should confirm the exact wording and scope in the primary framework text.
- **Grounding — this node** (SAMA_EN_4066_VER1 · Page 27): "System change management process should be governed by the change management policy and procedure that should be approved, monitored, reviewed and updated on periodic basis and/or whenever significant changes occurs in the IT environment or changes in laws and regulatory requirem"
- **Grounding — related node** (SAMA_EN_4066_VER1 · Page 33): "The quality assurance process should be defined, approved, communicated and implemented to independently ascertain quality of the changes or development in the information assets in line with the business/user requirements prior moving them to the production environment."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`user acceptance testing (UAT)`, `system integration testing (SIT)`, `test cases`, `separate test environment`, `sanitized data`, `production data in testing`, `third party testing certification`, `mada certification`

#graphify/enriched #source/sama #community/cyber-security-framework
