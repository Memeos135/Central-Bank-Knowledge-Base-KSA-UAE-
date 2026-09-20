# Maturity Factor (MF)

Defines the maturity factor (MF) used in SA-CCR to scale the effective notional of a derivative trade for the time horizon over which potential future exposure is measured. It sets a separate calculation for unmargined netting sets (based on remaining maturity capped at one year and floored at ten business days) and for margined netting sets (based on the margin period of risk subject to prescribed floors, including for centrally cleared trades). It binds SAMA-supervised banks computing counterparty credit risk capital.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Margin Period of Risk (MPOR)|Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 35): "For margined transactions, the maturity factor is calculated using the margin period of risk (MPOR), subject to specified floors."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — PFE Add-on|PFE Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 35): "transactions, the supervisory factor applicable to a given asset class must be multiplied by a factor of five.21 Maturity factors 6.51."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

## Lookup terms

`maturity factor`, `MF`, `SA-CCR`, `effective notional`, `margin period of risk`, `MPOR floor`, `unmargined netting set`, `potential future exposure`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
