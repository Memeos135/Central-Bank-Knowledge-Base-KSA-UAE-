# Virtual Asset Service Provider

Defines and addresses the Virtual Asset Service Provider as the primary obligated entity under the UAE Travel Rule, acting either for the Originator (executing a transfer) or for the Beneficiary (receiving one). Obligations include collecting, verifying and transmitting prescribed transfer data, verifying beneficiary identity above the daily aggregated AED 3,500 threshold, applying enhanced due diligence in unhosted wallet scenarios, maintaining risk-based policies for incomplete transfers, and reporting systemic counterparty failures to the Supervisory Authority. Applies to VASPs in the UAE, including Free Zones and Financial Free Zones, and contemplates dealings with counterparty VASPs that may be unregulated in the UAE.

**Regimes:** AML/CTF, payments, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_6663_VER1.md`

## Connections

### [[CBUAE — Intermediary Provider|Intermediary Provider]] — `implements` [INFERRED]
- **Grounding — this node** (CBUAE_EN_6663_VER1 · Page 4): "An Intermediary Provider must transfer all Originator and Beneficiary information received by it from the Originator’s Virtual Asset Service Provider (whether or not regulated as a Virtual Asset Service Provider in the UAE) to the Beneficiary’s Virtual Asset Service Provider (whe"
- **Grounding — related node** (CBUAE_EN_6663_VER1 · Page 4): "An Intermediary Provider must transfer all Originator and Beneficiary information received by it from the Originator’s Virtual Asset Service Provider (whether or not regulated as a Virtual Asset Service Provider in the UAE) to the Beneficiary’s Virtual Asset Service Provider (whe"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[CBUAE — Privacy Token|Privacy Token]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_6663_VER1 · Page 4): "An Intermediary Provider must transfer all Originator and Beneficiary information received by it from the Originator’s Virtual Asset Service Provider (whether or not regulated as a Virtual Asset Service Provider in the UAE) to the Beneficiary’s Virtual Asset Service Provider (whe"
- **Grounding — related node** (CBUAE_EN_6663_VER1 · Page 4): "An Intermediary Provider must transfer all Originator and Beneficiary information received by it from the Originator’s Virtual Asset Service Provider (whether or not regulated as a Virtual Asset Service Provider in the UAE) to the Beneficiary’s Virtual Asset Service Provider (whe"

### [[CBUAE — Virtual Asset Transfer|Virtual Asset Transfer]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_6663_VER1 · Page 4): "An Intermediary Provider must transfer all Originator and Beneficiary information received by it from the Originator’s Virtual Asset Service Provider (whether or not regulated as a Virtual Asset Service Provider in the UAE) to the Beneficiary’s Virtual Asset Service Provider (whe"
- **Grounding — related node** (CBUAE_EN_6663_VER1 · Page 2): "A Virtual Asset Service Provider which Executes a Virtual Asset Transfer to another Virtual Asset Service Provider must ensure that the information referred to in paragraph 2 of this Article which accompanies the Virtual Asset Transfer has been verified by the Originator’s Virtua"

## Lookup terms

`Virtual Asset Service Provider`, `VASP`, `counterparty VASP due diligence`, `beneficiary identity verification`, `enhanced due diligence virtual assets`, `Supervisory Authority reporting`

#graphify/enriched #source/cbuae #community/virtual-asset-travel-rule
