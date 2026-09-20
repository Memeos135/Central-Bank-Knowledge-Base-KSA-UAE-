# Qualifying Central Counterparty (QCCP)

Defines the preferential capital treatment for bank exposures to qualifying central counterparties, covering trade exposures as clearing member or client, posted collateral and default fund contributions, including the 2% risk weight and a 10-day minimum margin period of risk for OTC derivatives. It also permits a bank to fall back to non-qualifying CCP treatment where that produces lower combined RWA. Binds banks with cleared derivative exposures.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`
- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — Central Counterparty (CCP)|Central Counterparty (CCP)]] — `implements` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 67): "If a bank’s combined RWA for trade exposures to a QCCP and default fund contribution for that QCCP is higher than would apply for those same exposures if the QCCP were a non-qualifying CCP, the bank may treat the exposures as if the QCCP was non-qualifying."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 67): "If a bank’s combined RWA for trade exposures to a QCCP and default fund contribution for that QCCP is higher than would apply for those same exposures if the QCCP were a non-qualifying CCP, the bank may treat the exposures as if the QCCP was non-qualifying."

### [[CBUAE — Counterparty Credit Risk Standard|Counterparty Credit Risk Standard]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 88): "For banks in the UAE, the applicable standards for counterparty credit risk is the Central Bank’s Standards for Counterparty Credit Risk Capital, which reflects the Standardised Approach to Counterparty Credit Risk (SA-CCR)."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 29): "The credit equivalent amount of over-the-counter (OTC) derivatives that expose a bank to counterparty credit risk is calculated under the requirements set forth in the below Standard on Counterparty Credit Risk Capital."

### [[CBUAE — Default Fund Contributions|Default Fund Contributions]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 67): "If a bank’s combined RWA for trade exposures to a QCCP and default fund contribution for that QCCP is higher than would apply for those same exposures if the QCCP were a non-qualifying CCP, the bank may treat the exposures as if the QCCP was non-qualifying."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 68): "However, if the RWA from the calculation above is less than 2% of the amount of the bank’s pre-funded contributions to the default fund, then the bank must set RWA equal to 2% of its pre-funded contributions to the default fund, which is 2%×DFM."

### [[CBUAE — Look-Through Approach (LTA)|Look-Through Approach (LTA)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 67): "If a bank’s combined RWA for trade exposures to a QCCP and default fund contribution for that QCCP is higher than would apply for those same exposures if the QCCP were a non-qualifying CCP, the bank may treat the exposures as if the QCCP was non-qualifying."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 78): "Banks must treat in-scope equity positions in a manner consistent with one or more of the following three approaches: the “look-through approach”, the “mandate-based approach” and the “fall-back approach”."

### [[CBUAE — Replacement Cost (RC)|Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** Decide the counterparty's QCCP status first, then measure the exposure — the two instruments split those steps. Qualifying status under the capital adequacy provisions governs the preferential treatment of trade exposures and default fund contributions, while the replacement cost component in the counterparty credit risk standard supplies the measurement input for derivative exposures to that counterparty. The consequence is that a loss (or absence) of QCCP status does not change how replacement cost is computed, but it changes the weighting applied to that measured exposure, so both documents must be read together when sizing CCP-related capital.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 67): "If a bank’s combined RWA for trade exposures to a QCCP and default fund contribution for that QCCP is higher than would apply for those same exposures if the QCCP were a non-qualifying CCP, the bank may treat the exposures as if the QCCP was non-qualifying."
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"

## Lookup terms

`QCCP`, `qualifying central counterparty`, `trade exposure`, `default fund contribution`, `clearing member`, `2% risk weight`, `margin period of risk`, `posted collateral`

#graphify/enriched #source/cbuae #community/counterparty-credit-&-cva-risk
