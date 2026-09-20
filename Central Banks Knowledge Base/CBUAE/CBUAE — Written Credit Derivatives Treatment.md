# Written Credit Derivatives Treatment

Defines and sets the leverage ratio treatment of written credit derivatives, i.e. contracts through which a bank effectively sells credit protection, which generate notional credit exposure in addition to counterparty credit risk on fair value. It specifies the conditions for offsetting with purchased protection (symmetrical fair-value adjustments to effective notional, exclusion where the offsetting protection relates to client-cleared trades), states that reference names match only if the same legal entity, and permits pool protection to offset single-name protection where economically equivalent. Binds banks computing the leverage ratio exposure measure.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Leverage Ratio Standard (CBUAE 1691)|Leverage Ratio Standard (CBUAE 1691)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 153): "This Standard discusses the key principles of supervisory review, with respect to banking risks, including guidance relating to, among other things, the treatment of interest rate risk in the banking book, credit risk (stress testing, residual risk, and credit concentration risk)"

### [[CBUAE — QCCP Clearing Member Treatment|QCCP Clearing Member Treatment]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** Both provisions bear on how a bank may recognise offsetting when calculating capital for derivative exposures, so they should be read together before concluding a given exposure is reduced. The clearing member provision governs when a client bank's exposure may receive favourable counterparty treatment where a clearing member faces a qualifying central counterparty, while the written credit derivatives provision limits when purchased protection may be offset against protection sold on a pool. The practical consequence is that recognition of offsets is conditional in each case and the conditions are not interchangeable; the relationship is inferred from their shared capital-treatment context, so verify the specific paragraphs.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 191): "However, such purchased credit protection may offset written credit derivatives on a pool provided that the credit protection purchased through credit derivatives covers the entirety of the subset of the pool on which the credit protection has been sold."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 69): "Where a bank is a client of a clearing member, and enters into a transaction with a clearing member who completes an offsetting transaction with the QCCP, of if a clearing member guarantees QCCP performance to the bank as a client, the bank’s exposures to the clearing member may "
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`written credit derivative`, `effective notional amount`, `credit protection sold`, `credit default swap`, `total return swap`, `reference name`, `leverage ratio offsetting`

#graphify/enriched #source/cbuae #community/bank-capital-adequacy-(basel-iii)
