# Exposure at Default (EAD)

Exposure at default is the exposure amount recognised for counterparty credit risk, computed per netting set as replacement cost plus potential future exposure multiplied by a fixed scaling factor, and then risk weighted. The concept also appears in the treatment of exposures to qualifying central counterparties, where the QCCP's aggregate exposure to clearing members feeds the default fund capital calculation subject to a floor, and in securitisation and fund look-through contexts. Applies to banks computing regulatory capital for derivatives and cleared transactions.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`
- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — CVA Capital Calculation|CVA Capital Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** Treat the exposure-at-default determination as an upstream input you must settle before any CVA capital number can be defended. The CVA capital component sits inside the same capital adequacy framework whose denominator is built from exposure measures, so the EAD definition and its measurement conventions feed directly into the CVA charge rather than standing as a separate calculation. Practically, a change or supervisory challenge to how EAD is derived for a counterparty propagates into the CVA capital result and the overall capital ratio; verify the primary text for the precise EAD basis applied to CVA, since the surrounding provisions also address leverage exposure and should not be conflated.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 12): "Capital component of Capital Adequacy Regulation If a bank has complied with the minimum CET1 and Tier 1 capital ratios, the excess AT1 capital can be counted to meet the total capital ratio, also referred to as Capital Adequacy Ratio (CAR)."

### [[CBUAE — Counterparty Credit Risk Standard|Counterparty Credit Risk Standard]] — `references` [EXTRACTED]
- **What this link tells you:** Exposure at default is the measurement input on which counterparty credit risk capital turns, so a decision about EAD methodology cannot be taken independently of the counterparty credit risk standard that governs it and of the supervisory review expectations for credit risk, residual risk and concentration risk. Because both sit within the same capital framework, an EAD figure that is technically compliant at Pillar 1 may still be challenged under supervisory review if it understates residual or concentration risk. Note that the linked passage concerns securitisation implicit support, so the reader should verify in the primary text which EAD provision is actually being cross-referenced before relying on this link.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 176): "Examples of implicit support include the purchase of deteriorating credit risk exposures from the underlying pool, the sale of discounted credit risk exposures into the pool of securitized credit risk exposures, the purchase of underlying exposures at above market price or an inc"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 153): "This Standard discusses the key principles of supervisory review, with respect to banking risks, including guidance relating to, among other things, the treatment of interest rate risk in the banking book, credit risk (stress testing, residual risk, and credit concentration risk)"

### [[CBUAE — Netting Set|Netting Set]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 56): "If multiple margin agreements apply to a single netting set, the bank must divide the netting set into sub-netting sets that align with each respective margin agreement, and calculate RC for each sub-netting set separately."

### [[CBUAE — Potential Future Exposure|Potential Future Exposure]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."

### [[CBUAE — Potential Future Exposure (PFE)|Potential Future Exposure (PFE)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 201): "When a bank acts as a principal, its SFT exposure is the sum of gross SFT assets (subject to adjustments) and a measure of counterparty credit risk calculated as the current exposure without an add-on for potential future exposure."

### [[CBUAE — Replacement Cost (RC)|Replacement Cost (RC)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"

## Lookup terms

`exposure at default`, `EAD`, `alpha factor 1.4`, `QCCP default fund exposure`, `clearing member exposure`, `credit equivalent amount`, `securitisation exposure amount`

#graphify/enriched #source/cbuae #community/counterparty-exposure-(sa-ccr)
