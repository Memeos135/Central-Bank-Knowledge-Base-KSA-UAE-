# Effective Maturity (M)

Concept node for Effective Maturity (M), the IRB risk component measuring the maturity of a facility for credit risk capital purposes. It fixes 2.5 years under the foundation approach (6 months for repo-style transactions), requires banks using advanced approaches to calculate M per facility subject to a one-year floor and five-year cap, and specifies treatment for cash-flow-scheduled instruments, netted derivatives and revolving exposures. It binds banks applying IRB approaches; related maturity-scaling concepts also arise in the market risk default risk charge.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — IRB Approach Risk Components|IRB Approach: Risk Components]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 137): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — IRB Approach Risk Weight Functions|IRB Approach: Risk Weight Functions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 137): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."

### [[SAMA — IRB Risk Components (PD, LGD, EAD, M)|IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 173): "the risk weights of the uncovered risk components will be added to the risk weights of the covered risk components) 62 At SAMA’s discretion, banks may recognize guarantors that are internally rated and associated with a PD equivalent to less than A- under the foundation IRB appro"

### [[SAMA — Maturity Mismatches|Maturity Mismatches]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** For an IRB credit risk calculation, the maturity input and the credit risk mitigation maturity-mismatch adjustment must be read as one chain: effective maturity (M) drives the risk weight, while a protection instrument maturing before the exposure triggers the mismatch haircut. The shared defined term 'effective maturity (M)' — including the foundation-approach defaults — is what ties the two provisions. Consequently, a decision on recognising a hedge or guarantee cannot be taken on the mitigation rules alone; the maturity assigned to the underlying exposure must be settled first. The link is inferred, so confirm the precise paragraph cross-references in the primary text.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 137): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 130): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`Effective Maturity`, `maturity adjustment M`, `F-IRB maturity 2.5 years`, `maturity floor and cap`, `repo-style transactions maturity`, `revolving exposures maturity`, `master netting agreement maturity`

#graphify/enriched #source/sama #community/irb-risk-components
