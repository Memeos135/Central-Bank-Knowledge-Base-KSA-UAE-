# Margin Period of Risk (MPOR)

Sets the supervisory floors on the margin period of risk used when measuring exposure on margined netting sets, and the exceptions that lengthen them — large netting sets not facing a central counterparty, illiquid collateral or OTC derivatives that cannot be easily replaced, and a doubling of the floor following repeated prolonged margin call disputes. Binds banks calculating counterparty credit risk exposure for margined transactions.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Internal Models Method (IMM)|Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 597): "Internal models method for counterparty credit risk Approval to adopt an internal models method to estimate EAD 7.1."

### [[SAMA — Maturity Factor|Maturity Factor]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

### [[SAMA — Maturity Factor (MF)|Maturity Factor (MF)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 35): "For margined transactions, the maturity factor is calculated using the margin period of risk (MPOR), subject to specified floors."

### [[SAMA — Regulatory CVA Calculation|Regulatory CVA Calculation]] — `references` [EXTRACTED]
- **What this link tells you:** MPOR is a counterparty credit risk input that also conditions the regulatory CVA calculation, because exposure paths used for CVA must reflect the assumed close-out and re-margining horizon for margined netting sets. The link matters because regulatory CVA is not the accounting figure: it excludes the bank's own default and is subject to prescribed constraints, so MPOR assumptions must follow the regulatory specification rather than internal or accounting practice. In a review, check that the MPOR used for CVA is consistent with the CCR framework's prescribed floors and any extensions triggered by disputes or illiquid collateral, and confirm the point against the primary text.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 87): "(1) regulatory CVA excludes the effect of the bank’s own default; and (2) several constraints reflecting best practice in accounting CVA are imposed on calculations of regulatory CVA."

### [[SAMA — Replacement Cost (RC)|Replacement Cost (RC)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Trade Exposures to CCPs|Trade Exposures to CCPs]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 352): "The RWA for counterparty credit risk (RWACCR) are determined by multiplying the exposure amount by the relevant risk weight for trade exposures to CCPs, which 2% in this case (see chapter 8 of Minimum Capital Requirements for Credit Risk for the capital requirements for bank expo"

## Lookup terms

`margin period of risk`, `MPOR floor`, `margined netting set`, `illiquid collateral`, `margin call dispute`, `non-centrally cleared derivatives`, `20 business days`

#graphify/enriched #source/sama #community/basel-iii-counterparty-exposure
