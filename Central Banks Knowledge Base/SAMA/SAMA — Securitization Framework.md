# Securitization Framework

This node sets out the securitisation capital framework: definitions of securitisation and resecuritisation exposures, when a bank is an originator, the range of exposures captured (ABS, MBS, credit enhancements, liquidity facilities, swaps, reserve accounts), and the hierarchy of capital approaches including SEC-SA, SEC-ERBA, SEC-IAA and SEC-IRBA with the 15% risk-weight floor and resecuritisation adjustments. It binds banks holding, originating or sponsoring securitisation positions when calculating risk-weighted assets.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — ABCP ProgrammeConduit|ABCP Programme/Conduit]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 304): "19.17 If the underlying portfolio of a resecuritization consists in a pool of exposures to securitization tranches and to other assets, one should separate the exposures to securitization tranches from exposures to assets that are not securitizations."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 260): "18.67 For regulatory capital purposes, the following will be considered STC- compliant: (1) Exposures to non-ABCP, traditional securitizations that meet the criteria in 18.72 to 18.95; and (2) Exposures to ABCP conduits and/or transactions financed by ABCP conduits, where the con"

### [[SAMA — Guidance Note on Scope of Application of Basel Framework  Min Capital Requirements Credit Risk|Guidance Note on Scope of Application of Basel Framework / Min Capital Requirements Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** Before applying any securitisation capital treatment, you must first settle the scope-of-application question — which entities and which consolidation perimeter the framework binds — because the guidance note on scope and minimum credit risk capital requirements sets that perimeter and defines the CET1/Tier 1 ratios, buffers and Pillar 2 add-ons that securitisation RWA ultimately feed. The securitisation chapter (including SEC-SA, resecuritisation treatment and the STC-based alternative treatment) is therefore a downstream computation within that same minimum capital obligation, not a separate regime. In practice, resolve the consolidation and approach-eligibility questions first; the securitisation hierarchy you may use follows from them, and an error there flows straight through to the reported capital ratios.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 12): "Securitization: standardized approach 294 Standardized approach (SEC-SA) 294 Resecuritisation exposures 297 Alternative capital treatment for term STC securitizations and short- term STC securitizations meeting the STC criteria for capital purposes 298 Version Issuance Date Page "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "capital conservation buffer, G-SIB surcharge and countercyclical capital buffer) and Pillar 2 capital requirements (if CET1 capital is required); (ii) CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capi"

### [[SAMA — IRB Approach RWA for Purchased Receivables|IRB Approach: RWA for Purchased Receivables]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank applies the IRB treatment for purchased receivables, it needs to test whether the receivables pool is in substance a securitisation, because the two chapters lead to different RWA outcomes. The purchased receivables rules use the IRB asset-class list (including corporate purchased receivables), while the securitisation chapter supplies its own IRB route with KIRB, attachment/detachment points and the supervisory parameter — and KIRB itself is derived from the underlying IRB capital on the pool, creating a direct obligation chain between the two. Consequence for the reader: decide the characterisation before choosing the approach, and where a pool is tranched, expect the securitisation chapter to govern and to require the underlying IRB inputs as a precondition.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 13): "Securitization: Internal- ratings-based approach 311 Internal ratings-based approach (SEC-IRBA) 311 Definition of KIRB 311 Definition of attachment point (A), detachment point (D) and supervisory parameter (p) 315 Calculation of risk weight 319 Alternative capital treatment for t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 112): "In this context, the relevant assets classes are as follows: (1) Sovereigns (2) Banks (3) Corporates (excluding specialized lending and purchased receivables) (4) Specialized lending (5) Corporate purchased receivables (6) QRRE (7) Retail residential mortgages (8) Other retail (e"

### [[SAMA — Minimum Capital Requirements for Credit Risk|Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** If you are computing minimum credit risk capital on an exposure that is a securitisation position, you cannot stop at the general credit risk chapter — you must route the exposure into the securitisation chapter's hierarchy of approaches. Both sit inside the same SAMA capital adequacy instrument and share defined terms (notably the risk-class taxonomy distinguishing non-securitisation from securitisation credit spread exposures), so the securitisation chapter operates as the specific regime carving out of the general one. Practical consequence: classify the exposure first; a mis-classified securitisation position produces the wrong risk weight and an understated capital requirement, so confirm the treatment in the securitisation chapter's primary text before finalising the calculation.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Resecuritization Exposure|Resecuritization Exposure]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 238): "An exposure resulting from retranching of a securitization exposure is not a resecuritization exposure if the bank is able to demonstrate that the cash flows to and from the bank could be replicated in all circumstances and conditions by an exposure to the securitization of a poo"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 238): "An exposure resulting from retranching of a securitization exposure is not a resecuritization exposure if the bank is able to demonstrate that the cash flows to and from the bank could be replicated in all circumstances and conditions by an exposure to the securitization of a poo"

### [[SAMA — Special Purpose Entity (SPE)|Special Purpose Entity (SPE)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Supervisory slotting approach for specialized lending 138 Risk weights for specialized lending (PF, OF, CF and IPRE) 138 Risk weights for specialized lending (HVCRE) 139 Expected loss for specialized lending (SL) exposures subject to the supervisory slotting criteri"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Supervisory slotting approach for specialized lending 138 Risk weights for specialized lending (PF, OF, CF and IPRE) 138 Risk weights for specialized lending (HVCRE) 139 Expected loss for specialized lending (SL) exposures subject to the supervisory slotting criteri"

### [[SAMA — Synthetic Securitization|Synthetic Securitization]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 237): "Securitization: general provisions Scope and definitions of transactions covered under the securitization framework 18.1 Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizatio"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 237): "Securitization: general provisions Scope and definitions of transactions covered under the securitization framework 18.1 Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizatio"

### [[SAMA — Template SEC1 Securitisation Exposures Banking Book|Template SEC1: Securitisation Exposures Banking Book]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** Before populating the banking-book securitisation disclosure template, you must first settle classification under the securitisation framework, since the template reports positions whose scope and labels (securitisation versus resecuritisation, tranche versus non-securitisation asset) are defined there. This is an inferred rather than stated link: the disclosure serves the prudential framework, so a reclassification of an exposure upstream changes what is disclosed downstream. Treat the framework's classification rules as the determinant of the template's contents, and verify the primary text of both instruments before relying on this alignment.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 304): "19.17 If the underlying portfolio of a resecuritization consists in a pool of exposures to securitization tranches and to other assets, one should separate the exposures to securitization tranches from exposures to assets that are not securitizations."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 832): "Template SEC1: Securitisation exposures in the banking book Purpose: Present a bank's securitisation exposures in its banking book."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — Traditional Securitization|Traditional Securitization]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 237): "Securitization: general provisions Scope and definitions of transactions covered under the securitization framework 18.1 Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizatio"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 237): "Securitization: general provisions Scope and definitions of transactions covered under the securitization framework 18.1 Banks must apply the securitization framework for determining regulatory capital requirements on exposures arising from traditional and synthetic securitizatio"

## Lookup terms

`securitisation framework`, `securitization exposure`, `resecuritisation`, `SEC-SA`, `SEC-ERBA`, `SEC-IRBA`, `STC criteria`, `originator and sponsor`, `risk weight floor 15%`

#graphify/enriched #source/sama #community/securitization-framework
