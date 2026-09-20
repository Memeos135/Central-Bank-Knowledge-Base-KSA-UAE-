# Single-Name Exposure (SNE)

A cross-cutting concept node for single-name exposure as used in CBUAE capital standards — most directly in the CVA framework (single-name hedges and counterparty-specific exposure) and in exposure-level risk weighting under the securitisation standard. The supplied context is drawn from the securitisation chapter (SEC-SA risk weights, floors, look-through and capital caps) and securitisation definitions, so the node is a weak anchor for the term itself. Open the underlying standards rather than relying on this node for a definition; relevant to UAE banks calculating RWA on a consolidated basis.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`
- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — CVA Capital Calculation|CVA Capital Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** If you are sizing CVA risk capital, you cannot stop at the capital-adequacy component alone: the CVA charge is driven by counterparty-level exposure, and single-name exposure is the defined input that nets discounted counterparty exposure against eligible single-name CVA hedges. The reference runs one way — the CVA capital provisions depend on the SNE measurement rules — so the two instruments sit in the same Basel-aligned capital adequacy chain rather than being alternatives. Practically, any hedge-recognition or exposure-netting judgement must be settled under the SNE definition before the resulting number is carried into the CET1/Tier 1/total capital ratio test. Note the supplied excerpts are partly generic, so verify the primary text for the exact CVA-to-SNE cross-reference.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 74): "For each counterparty, the bank should calculate single-name exposure (SNE) as the discounted counterparty exposure minus the discounted value of eligible single-name CVA hedges."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 12): "Capital component of Capital Adequacy Regulation If a bank has complied with the minimum CET1 and Tier 1 capital ratios, the excess AT1 capital can be counted to meet the total capital ratio, also referred to as Capital Adequacy Ratio (CAR)."

### [[CBUAE — CVA Capital Formula|CVA Capital Formula]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 74): "For each counterparty, the bank should calculate single-name exposure (SNE) as the discounted counterparty exposure minus the discounted value of eligible single-name CVA hedges."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 72): "Figure 2 Accordingly, the general form of the CVA capital calculation depends on the standard deviation of CVA losses: CVA capital = 2.33 × 𝑠𝑡𝑎𝑛𝑑𝑎𝑟𝑑 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 𝑜𝑓 𝑐ℎ𝑎𝑛𝑔𝑒𝑠 𝑖𝑛 𝐶𝑉𝐴 = 2.33 × √𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒 𝑜𝑓 𝑐ℎ𝑎𝑛𝑔𝑒𝑠 𝑖𝑛 𝐶𝑉𝐴 The normality assumption, together with a desired 99% confidence l"

### [[CBUAE — Eligible CVA Hedges|Eligible CVA Hedges]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 74): "For each counterparty, the bank should calculate single-name exposure (SNE) as the discounted counterparty exposure minus the discounted value of eligible single-name CVA hedges."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 71): "This means, for example, that a bank might have a single-name CDS referencing an OTC counterparty in its portfolio, and yet that CDS would not be eligible to offset the single-name CVA exposure within the CVA calculation if that CDS was not originated or acquired as part of the b"

### [[CBUAE — Supervisory Discount Factor (DF)|Supervisory Discount Factor (DF)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 74): "For each counterparty, the bank should calculate single-name exposure (SNE) as the discounted counterparty exposure minus the discounted value of eligible single-name CVA hedges."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 73): "DF is a supervisory discount factor, described further below.) In effect, the discounted value of the individual counterparty exposure is offset by the discounted value of eligible single-name CVA hedges for that counterparty."

## Lookup terms

`single-name exposure`, `SNE`, `single-name hedge`, `SEC-SA`, `securitisation risk weight floor`, `look-through approach`, `resecuritisation exposure`, `originating bank`

#graphify/enriched #source/cbuae #community/cva-capital-calculation
