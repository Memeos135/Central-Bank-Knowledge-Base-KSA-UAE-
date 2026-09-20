# Replacement Cost (RC)

Defines replacement cost as the netting-set-level component of counterparty credit risk exposure, derived from the current market value of in-scope derivative contracts net of eligible collateral after haircuts, producing the net current value. Different calculation methods apply to margined and un-margined transactions, and RC is floored at zero for un-margined netting sets. A related fallback applies when valuing fund derivative exposures: where replacement cost cannot be determined, the derivative's notional amount is used instead.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`
- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — Counterparty Credit Risk (SA-CCR)|Counterparty Credit Risk (SA-CCR)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 169): "At a minimum, the scope of risks should cover strategic risk, credit risk, market risk, counterparty risk, operational risk, liquidity risk, IRRBB, credit concentration risk, funding risk, reputational risk, and climate risk."
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 169): "At a minimum, the scope of risks should cover strategic risk, credit risk, market risk, counterparty risk, operational risk, liquidity risk, IRRBB, credit concentration risk, funding risk, reputational risk, and climate risk."

### [[CBUAE — Exposure at Default (EAD)|Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 186): "A bank’s total leverage ratio exposure measure is the sum of the following exposures:  On balance sheet exposures (excluding on-balance-sheet derivative and SFT exposures);  derivative exposures;  SFT exposures; and  Off-balance sheet items."

### [[CBUAE — Exposure at Default (EAD) Calculation|Exposure at Default (EAD) Calculation]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 47): "Summary of the EAD Calculation Process The following diagram provides a visual summary of the CCR calculation of EAD for derivatives, based on replacement cost and potential future exposure."

### [[CBUAE — Qualifying Central Counterparty (QCCP)|Qualifying Central Counterparty (QCCP)]] — `references` [EXTRACTED]
- **What this link tells you:** Decide the counterparty's QCCP status first, then measure the exposure — the two instruments split those steps. Qualifying status under the capital adequacy provisions governs the preferential treatment of trade exposures and default fund contributions, while the replacement cost component in the counterparty credit risk standard supplies the measurement input for derivative exposures to that counterparty. The consequence is that a loss (or absence) of QCCP status does not change how replacement cost is computed, but it changes the weighting applied to that measured exposure, so both documents must be read together when sizing CCP-related capital.
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 187): "In general, for the purpose of the leverage ratio exposure measure, exposures for derivatives are calculated in accordance with the Central Bank’s Standard for Counterparty Credit Risk Capital through the two components of replacement cost (RC) and PFE, as follows: Exposure measu"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 67): "If a bank’s combined RWA for trade exposures to a QCCP and default fund contribution for that QCCP is higher than would apply for those same exposures if the QCCP were a non-qualifying CCP, the bank may treat the exposures as if the QCCP was non-qualifying."

## Lookup terms

`replacement cost`, `RC`, `net current value`, `NCV`, `collateral haircuts`, `current market value of derivatives`, `equity investments in funds`, `mandate-based approach`

#graphify/enriched #source/cbuae #community/counterparty-exposure-(sa-ccr)
