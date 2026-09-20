# Regulatory CVA Calculation

This node defines regulatory CVA and the principles for calculating it at counterparty level for CVA capital purposes, notably excluding the bank's own default risk and imposing constraints on accounting-CVA practice. It also sets the minimum eligibility criteria a bank must meet for SAMA to permit use of SA-CVA, including monthly CVA and sensitivity computation and a dedicated CVA desk. It binds banks with covered derivative and SFT positions and requires demonstration of compliance to SAMA.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SAMA — Margin Period of Risk (MPOR)|Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **What this link tells you:** MPOR is a counterparty credit risk input that also conditions the regulatory CVA calculation, because exposure paths used for CVA must reflect the assumed close-out and re-margining horizon for margined netting sets. The link matters because regulatory CVA is not the accounting figure: it excludes the bank's own default and is subject to prescribed constraints, so MPOR assumptions must follow the regulatory specification rather than internal or accounting practice. In a review, check that the MPOR used for CVA is consistent with the CCR framework's prescribed floors and any extensions triggered by disputes or illiquid collateral, and confirm the point against the primary text.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 87): "(1) regulatory CVA excludes the effect of the bank’s own default; and (2) several constraints reflecting best practice in accounting CVA are imposed on calculations of regulatory CVA."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[SAMA — Standardized Approach for CVA (SA-CVA)|Standardized Approach for CVA (SA-CVA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 87): "(1) regulatory CVA excludes the effect of the bank’s own default; and (2) several constraints reflecting best practice in accounting CVA are imposed on calculations of regulatory CVA."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

## Lookup terms

`regulatory CVA`, `counterparty-level CVA`, `SA-CVA eligibility`, `CVA desk`, `market-implied PD`, `expected loss given default`, `CVA sensitivities`, `prudent valuation`

#graphify/enriched #source/sama #community/rwa-&-cva-disclosure-templates
