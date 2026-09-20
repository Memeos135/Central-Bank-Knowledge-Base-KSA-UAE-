# Counterparty Credit Risk in the Trading Book

Node covering how counterparty credit risk arising on trading book positions is capitalised under SAMA's Basel-aligned minimum capital framework, including the treatment of repo-style and collateralised OTC derivative transactions (which follow the banking book CCR rules), eligible trading book collateral and applicable haircuts, and related RWA/capital reporting lines that separate CCR from general credit risk, CVA, settlement and securitisation exposures. It also touches the boundary rules for internal risk transfers between banking book and trading book and when the trading book leg may be recognised for market risk purposes. Binds SAMA-licensed banks calculating Pillar 1 capital requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — Minimum Capital Requirements for Credit Risk|Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Minimum Haircut Floors for SFTs|Minimum Haircut Floors for SFTs]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When measuring counterparty exposure on securities financing transactions booked in the trading book, the collateral recognised is not simply what was received; minimum haircut floors constrain how far collateral can reduce the exposure. Both sets of rules bear on the same exposure amount, with the floors acting as a backstop against under-collateralised financing to certain counterparties before counterparty credit risk capital is computed. The practical consequence is that an SFT failing the floor is treated as effectively unsecured for capital purposes, materially increasing the counterparty charge. This relationship is inferred from the shared exposure-measurement chain rather than an explicit cross-reference, so verify the scope and applicability of the floors in the primary text.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`counterparty credit risk`, `trading book`, `repo-style transactions`, `internal risk transfer`, `banking book / trading book boundary`, `RWA reporting`, `collateralised OTC derivatives`, `SCCR`

#graphify/enriched #source/sama #community/counterparty-credit-&-sfts
