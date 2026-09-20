# Maturity Mismatches

This node sets out when a maturity mismatch between credit protection and the underlying exposure may still be recognized (original maturity of at least one year, residual maturity of at least three months), the partial-recognition adjustment formula, and the conservative definitions of hedge and exposure maturity. It also covers how maturity mismatches are handled for securitization exposures and synthetic securitizations. It binds banks applying credit risk mitigation for regulatory capital purposes.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[SAMA — Collateralized Transactions|Collateralized Transactions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 62): "General treatment of maturity mismatches 9.10 For the purposes of calculating risk-weighted assets, a maturity mismatch occurs when the residual maturity of a credit protection arrangement (e.g."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 556): "Long settlement transactions Transactions such as repurchase agreements, reverse repurchase agreements, security lending and borrowing, and margin lending transactions, where the value of the transactions depends on market valuations and the transactions are often subject to marg"

### [[SAMA — Effective Maturity (M)|Effective Maturity (M)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** For an IRB credit risk calculation, the maturity input and the credit risk mitigation maturity-mismatch adjustment must be read as one chain: effective maturity (M) drives the risk weight, while a protection instrument maturing before the exposure triggers the mismatch haircut. The shared defined term 'effective maturity (M)' — including the foundation-approach defaults — is what ties the two provisions. Consequently, a decision on recognising a hedge or guarantee cannot be taken on the mitigation rules alone; the maturity assigned to the underlying exposure must be settled first. The link is inferred, so confirm the precise paragraph cross-references in the primary text.
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 130): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 137): "Effective maturity (M) 12.44 Effective maturity (M) will be 2.5 years for exposures to which the bank applies the foundation approach, except for repo-style transactions where the effective maturity is 6 months (i.e."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`maturity mismatch`, `residual maturity`, `credit protection adjustment`, `hedge maturity`, `effective maturity`, `simple approach collateral`, `synthetic securitization`

#graphify/enriched #source/sama #community/counterparty-credit-risk-mitigation
