# Index CDS Hedge

Worked-example node showing how an eligible index CDS is recognised as a hedge of systematic CVA risk in the CVA capital formula. It illustrates derivation of the supervisory discount factor from the index maturity, the weighted-average risk weight across the index constituents' ratings, and the resulting reduction in CVA capital and RWA. Relevant to CBUAE-licensed banks applying the standardised CVA capital calculation.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/CBUAE_EN_2464_VER2.md`

## Connections

### [[CBUAE — CVA Capital Formula|CVA Capital Formula]] — `references` [EXTRACTED]
- **Grounding — this node** (CBUAE_EN_2464_VER2 · Page 76): "The calculation including index hedges is: 2 𝐾= 2.33√(∑0.5 𝑊𝑖 𝑆𝑁𝐸𝑖 + ∑0.75 (𝑊𝑖 𝑆𝑁𝐸𝑖)2 −∑𝑊𝑖𝑛𝑑 𝐻𝑖𝑛𝑑 𝐷𝐹𝑖𝑛𝑑) 𝑖 𝑖𝑛𝑑 𝑖 where Hind is the notional of an eligible purchased index hedge instrument that is used to hedge CVA risk, (1−𝑒−0.05𝑀𝑖𝑛𝑑) 0.05 is the applicable supervisory discount f"
- **Grounding — related node** (CBUAE_EN_2464_VER2 · Page 72): "Figure 2 Accordingly, the general form of the CVA capital calculation depends on the standard deviation of CVA losses: CVA capital = 2.33 × 𝑠𝑡𝑎𝑛𝑑𝑎𝑟𝑑 𝑑𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛 𝑜𝑓 𝑐ℎ𝑎𝑛𝑔𝑒𝑠 𝑖𝑛 𝐶𝑉𝐴 = 2.33 × √𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒 𝑜𝑓 𝑐ℎ𝑎𝑛𝑔𝑒𝑠 𝑖𝑛 𝐶𝑉𝐴 The normality assumption, together with a desired 99% confidence l"

## Lookup terms

`index CDS hedge`, `systematic CVA risk`, `supervisory discount factor`, `weighted average risk weight index`, `CVA capital calculation example`, `notional of index hedge`

#graphify/enriched #source/cbuae #community/cva-capital-calculation
