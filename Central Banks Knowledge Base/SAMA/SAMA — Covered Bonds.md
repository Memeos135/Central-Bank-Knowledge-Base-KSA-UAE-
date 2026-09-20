# Covered Bonds

This node defines covered bonds for SAMA large exposure purposes and sets the conditions under which a bank's holding may be assigned a reduced exposure value (not less than 20% of nominal) rather than the default 100%, with the issuing bank treated as the counterparty. Eligibility depends on cover pool composition, loan-to-value ceilings for residential and commercial real estate, and a minimum 10% over-collateralisation, tested at inception and throughout the bond's life, plus operational requirements for eligible CRE/RRE collateral. It binds banks holding covered bonds under the LEX Rules.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_2340_VER1.md`

## Connections

### [[SAMA — Eligible Collateral for Margin|Eligible Collateral for Margin]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When deciding how a secured instrument or posted asset is treated for prudential purposes, check both rule sets rather than assuming one governs: covered bonds are defined by the protection afforded to bondholders through a supervised cover pool, while the margin rules define what may be accepted and re-used as collateral for non-centrally-cleared derivatives. The link is conceptual — both regimes turn on asset quality, segregation and creditor protection — rather than an express cross-reference, so covered bonds may appear as an eligible collateral category in the margin framework without either text governing the other. Practically, a bank should apply the covered bond rules for issuance/exposure treatment and the margin rules separately for eligibility, haircuts and re-hypothecation limits. Because this link is inferred, verify in the primary texts whether the margin framework in fact lists covered bonds as eligible before relying on the overlap.
- **Grounding — this node** (SAMA_EN_2340_VER1 · Page 33): "Covered bonds are bonds issued by a bank or mortgage institution and are subject by law to special public supervision designed to protect bond holders."
- **Grounding — related node** (SAMA_EN_2757_VER1 · Page 14): " Where the initial margin collector re-hypothecates initial margin, the agreement with the recipient of the collateral (ie the third party) must prohibit the third party from further re-hypothecating the collateral."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — High Quality Liquid Assets (HQLA)|High Quality Liquid Assets (HQLA)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When deciding whether a covered bond holding can be counted in the liquidity buffer, the definitional instrument and the HQLA classification rules must be read together: the former sets the structural characteristics of a covered bond (segregated cover pool serving bondholders on issuer failure), the latter determines whether such an instrument qualifies as Level 2A subject to rating and the aggregate Level 2 cap. The relationship is inferred from the shared defined term rather than an express cross-citation. Consequence: structural conformity alone does not confer HQLA status, and HQLA treatment cannot be claimed for an instrument that does not meet the covered bond definition plus the rating and cap conditions. Verify the eligibility criteria in the primary liquidity text before recognising the asset.
- **Grounding — this node** (SAMA_EN_2340_VER1 · Page 33): "Proceeds deriving from the issue of these bonds must be invested in conformity with the law in assets which, during the whole period of the validity of the bonds, are capable of covering claims attached to the bonds and which, in the event of the failure of the issuer, would be u"
- **Grounding — related node** (SAMA_EN_2788_VER1 · Page 37): "Level 2 assets (maximum of 40% of HQLA): Level 2A assets e Sovereign, central bank, multilateral development banks, and assets qualifying for 20% risk weighting ¢ Qualifying corporate debt securities rated AA- or higher e Qualifying covered bonds rated AA- or higher Level 2B asse"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SAMA — Large Exposure (LEX) Rules for Banks|Large Exposure (LEX) Rules for Banks]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_2340_VER1 · Page 33): "Other covered bonds must be assigned an exposure value equal to 100% of the nominal value of the bank’s covered bond holding."
- **Grounding — related node** (SAMA_EN_2340_VER1 · Page 40): "In the case of non-QCCPs, banks must measure their exposure as a sum of both the clearing exposures described in sections titled “Calculation of exposures related to clearing activities” and “Other exposures” below, and must respect the general large exposure limit of 25% of the "

## Lookup terms

`covered bonds`, `cover pool`, `over-collateralisation 10%`, `loan-to-value ratio`, `residential real estate collateral`, `commercial real estate collateral`, `exposure value 20%`, `issuing bank counterparty`

#graphify/enriched #source/sama #community/large-exposures-framework
