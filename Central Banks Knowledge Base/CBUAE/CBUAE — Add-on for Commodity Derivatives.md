# Add-on for Commodity Derivatives

Describes the commodity derivatives add-on: effective notionals are computed per commodity type, scaled by supervisory factors, then aggregated into four hedging sets (energy, metals, agriculture, other) using a supervisory correlation, with basis and volatility trades in separate hedging sets. It notes the hedging sets ignore location and quality differences, so basis risk within a set is not captured. Applies to banks computing derivative exposure for capital purposes.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/CBUAE_EN_1691_VER2.md`

## Connections

### [[CBUAE — Hedging Set|Hedging Set]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_1691_VER2 · Page 64): "Specifically, the bank must calculate the add-on for each of the four commodity derivative hedging sets by calculating: 2 + ∑((1 −𝜌2) × 𝐴𝑖 2) 𝑖 𝐻𝑒𝑑𝑔𝑖𝑛𝑔 𝑆𝑒𝑡 𝐴𝑑𝑑𝑂𝑛= √(∑𝜌× 𝐴𝑖 ) 𝑖 where ρ is the supervisory correlation factor for commodity derivatives, and Ai is the add-on for one co"
- **Grounding — related node** (CBUAE_EN_1691_VER2 · Page 64): "The add-on for the commodity derivatives asset class is the sum of the four hedging set add-ons as calculated above (some of which may be zero if the bank has no derivatives within one of the four hedging sets), plus corresponding add-ons for any basis or volatility hedging sets."

## Lookup terms

`commodity derivatives add-on`, `commodity type`, `energy metals agriculture hedging sets`, `supervisory correlation factor`, `basis transactions`, `volatility transactions`, `effective notional amount`

#graphify/enriched #source/cbuae #community/derivative-add-on-calculations
