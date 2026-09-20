# Retail Deposit Run-off

Guidance node within SAMA's amended Liquidity Coverage Ratio package setting how banks classify natural-person deposits as stable or less stable and the outflow assumptions applied over the 30-day stress horizon. It records KSA-specific positions, notably that there is no effective deposit insurance scheme in the Kingdom (so insurance-linked lower run-off treatment is unavailable) and that foreign-currency deposits are not treated as less stable, with run-off rates following the Basel Committee's January 2013 standard. It binds banks licensed in Saudi Arabia when completing the LCR prudential return.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_2788_VER1.md`

## Connections

### [[SAMA — Total Net Cash Outflows|Total Net Cash Outflows]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_2788_VER1 · Page 27): "Buckets of less stable deposits could include deposits that are not fully covered by an effective deposit insurance scheme or sovereign deposit guarantee, high-value deposits, deposits from sophisticated or high net worth individuals, deposits that can be withdrawn quickly (e.g."
- **Grounding — related node** (SAMA_EN_2788_VER1 · Page 24): "Total net cash outflows over the next 30 calendar days = Total expected cash outflows — Min {total expected cash inflows; 75% of total expected cash outflows}"

## Lookup terms

`retail deposit run-off`, `stable vs less stable deposits`, `LCR cash outflows`, `deposit insurance KSA`, `foreign currency deposits run-off rate`, `retail term deposits 30 days`, `Basel III LCR paragraph 73-84`

#graphify/enriched #source/sama #community/liquidity-coverage-ratio
