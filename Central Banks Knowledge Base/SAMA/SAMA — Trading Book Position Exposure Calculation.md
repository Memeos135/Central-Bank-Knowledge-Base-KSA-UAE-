# Trading Book Position Exposure Calculation

This node governs how trading book positions are valued and aggregated for large exposure purposes, requiring trading book and banking book exposures to the same counterparty to be summed. It scopes the limit to single-counterparty default risk (so debt and equity positions are captured, but commodity and currency concentrations are not) and prescribes conversion of swaps, futures, forwards, credit derivatives and options into counterparty positions, with a default-based valuation rule for options. It binds SAMA-supervised banks maintaining trading book positions.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_2340_VER1.md`

## Connections

### [[SAMA — Large Exposure (LEX) Rules for Banks|Large Exposure (LEX) Rules for Banks]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_2340_VER1 · Page 32): "When the result of the offsetting is a net short position with a single counterparty, this net exposure need not be considered as an exposure for large exposure purposes (refer to “Scope of large exposure limits in the trading book” section in this Appendix)."
- **Grounding — related node** (SAMA_EN_2340_VER1 · Page 40): "In the case of non-QCCPs, banks must measure their exposure as a sum of both the clearing exposures described in sections titled “Calculation of exposures related to clearing activities” and “Other exposures” below, and must respect the general large exposure limit of 25% of the "

### [[SAMA — Standardised Approach for Counterparty Credit Risk (SA-CCR)|Standardised Approach for Counterparty Credit Risk (SA-CCR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_2340_VER1 · Page 29): "A bank must add any exposures to a single counterparty arising in the trading book to any other exposures to that counterparty that lie in the banking book to calculate its total exposure to that counterparty."
- **Grounding — related node** (SAMA_EN_2340_VER1 · Page 27): "The exposure value for instruments that give rise to counterparty credit risk and are not securities financing transactions must be the exposure at default according to the standardised approach for counterparty credit risk (SA-CCR — (See SAMA Circular No 351000095021, 21 May 201"

## Lookup terms

`trading book exposure value`, `offsetting long and short positions`, `concentration risk`, `single counterparty default`, `credit derivatives conversion`, `option exposure value`, `banking book aggregation`

#graphify/enriched #source/sama #community/large-exposures-framework
