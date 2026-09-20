# Maturity Factor

Concept node for the maturity factor used to scale adjusted notionals in the counterparty credit risk add-on calculation, with distinct treatments for margined and unmargined netting sets (and related maturity-bucket concepts appearing in market risk risk-factor modellability rules). It determines the time-horizon scaling of derivative exposure. Applies to banks computing regulatory capital under SAMA's adopted Basel minimum capital requirements.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[SAMA — Aggregate Add-On|Aggregate Add-On]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 573): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

### [[SAMA — Effective Notional|Effective Notional]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 688): "That is: Adjusted Effective notional, 𝐷𝑖 (USD, thousands) Base currency Notional notional, 𝑑𝑖 (USD, thousands) Maturity Factor, Delta, IR Trade Maturity (USD thousands) # (hedging bucket 𝑀𝐹𝑖 𝛿𝑖 set) 1 10,000 USD 3 78,694 1.5 ∗√14 250 ⁄ 1 27,934 2 10,000 USD 2 36,254 1.5 ∗√14 250 "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 688): "That is: Adjusted Effective notional, 𝐷𝑖 (USD, thousands) Base currency Notional notional, 𝑑𝑖 (USD, thousands) Maturity Factor, Delta, IR Trade Maturity (USD thousands) # (hedging bucket 𝑀𝐹𝑖 𝛿𝑖 set) 1 10,000 USD 3 78,694 1.5 ∗√14 250 ⁄ 1 27,934 2 10,000 USD 2 36,254 1.5 ∗√14 250 "

### [[SAMA — Margin Period of Risk (MPOR)|Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`maturity factor`, `margined netting set`, `unmargined trades`, `margin period of risk`, `maturity bucket`, `remaining maturity`, `SA-CCR`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
