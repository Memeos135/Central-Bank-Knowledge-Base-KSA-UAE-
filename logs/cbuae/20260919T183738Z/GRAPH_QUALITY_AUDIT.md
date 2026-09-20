# Graph Quality Audit

> Generated: 2026-09-19T18:37:41+00:00
> Graph: 1608 nodes, 2043 edges
> Method: deterministic structural audit + verbatim drift check (no LLM)

## Overall grade: **B**

| Dimension | Grade | Value | Note |
|---|---|---|---|
| Grounding | A | 100.0% | stored excerpts still present verbatim in their source |
| Broken Arabic Exposure | A | 0.0% | share of nodes resting on presentation-form Arabic (lower is better) |
| Structure | C | 57.2% | nodes with degree >= 2 |
| Dedup | A | 100.0% | nodes not in a duplicate-label cluster |
| Locator Coverage | A | 100.0% | edges carrying an exact page locator |
| Extraction Coverage | B | 89.1% | A-grade documents adequately covered |

## Integrity (graphify diagnose multigraph)
- CLEAN — no dangling/missing/collapsed/self-loop edges

## Broken-Arabic exposure (measured from the corpus)

- Corpus documents with presentation-form Arabic >= 2%: **0** of 174
- Nodes resting on those documents: **0 / 1608** (0.0%)

## Grounding drift

- Stored excerpts: **4085** (checkable: 4085)
- Still verbatim in source: **4085** → **100.0%**

_Excerpts are sliced directly from the corpus, so this should read 100%. Anything lower means a source file changed after grounding ran — re-run the ground stage._

## Locators

- Edges with an exact page locator: **2043 / 2043**
- Nodes carrying source_location from extraction: **23 / 1608**

## Enrichment coverage

- Node summaries: **1607 / 1608**
- Community blurbs: **228**
- Edge narratives: **403** (selective by design — grounding covers every edge)

## Structure

- Isolated: **64** · degree-1: **624** (39%)
- Top hubs: Central Bank of the UAE (32), Internal Shari'ah Supervision Committee (ISSC) (25), Customer Due Diligence (CDD) (25), Risk Governance Framework (20), Trade-Based Money Laundering (19), ICAAP Guidance (18)

## Edges

- Confidence: EXTRACTED=1927, INFERRED=116
- Relations: references=1574, cites=274, conceptually_related_to=154, semantically_similar_to=25, shares_data_with=13, implements=3
- Orphans: 0 · self-loops: 0

## Duplicate-label clusters

- none (dedup ran)

## Per-document coverage

| Stem | Nodes | Pages | Nodes/pg | Grade | Flags |
|---|---|---|---|---|---|
| CBUAE_EN_2464_VER2 | 98 | 204 | 0.48 | A | - |
| CBUAE_EN_1691_VER2 | 94 | 197 | 0.477 | A | - |
| CBUAE_EN_3524_VER1 | 59 | 163 | 0.362 | A | - |
| CBUAE_EN_4229_VER1 | 56 | 162 | 0.346 | A | - |
| CBUAE_EN_3945_VER2 | 53 | 114 | 0.465 | A | - |
| CBUAE_EN_6788_VER1 | 45 | 58 | 0.776 | A | - |
| CBUAE_EN_5731_VER1 | 39 | 101 | 0.386 | A | - |
| CBUAE_EN_996_VER1 | 34 | 23 | 1.478 | A | - |
| CBUAE_EN_6843_VER1 | 31 | 68 | 0.456 | A | - |
| CBUAE_EN_238_VER1 | 27 | 118 | 0.229 | A | - |
| CBUAE_EN_6092_VER1 | 27 | 53 | 0.509 | A | - |
| CBUAE_EN_2413_VER1 | 26 | 41 | 0.634 | A | - |
| CBUAE_EN_5808_VER1 | 26 | 55 | 0.473 | A | - |
| CBUAE_EN_4961_VER1 | 25 | 70 | 0.357 | A | - |
| CBUAE_EN_6725_VER1 | 25 | 59 | 0.424 | A | - |
| CBUAE_EN_6127_VER1 | 24 | 71 | 0.338 | A | - |
| CBUAE_EN_6587_VER1 | 24 | 49 | 0.49 | A | - |
| CBUAE_EN_1531_VER1 | 23 | 85 | 0.271 | A | - |
| CBUAE_EN_1580_VER1 | 23 | 91 | 0.253 | A | - |
| CBUAE_EN_6185_VER1 | 22 | 123 | 0.179 | A | under_extracted |
| CBUAE_EN_4669_VER1 | 20 | 32 | 0.625 | A | - |
| CBUAE_EN_5056_VER1 | 19 | 43 | 0.442 | A | - |
| CBUAE_EN_5072_VER1 | 19 | 77 | 0.247 | A | - |
| CBUAE_EN_498_VER1 | 19 | 34 | 0.559 | A | - |
| CBUAE_EN_6593_VER1 | 19 | 42 | 0.452 | A | - |
| CBUAE_EN_1087_VER1 | 18 | 114 | 0.158 | A | under_extracted |
| CBUAE_EN_1577_VER1 | 18 | 29 | 0.621 | A | - |
| CBUAE_EN_4368_VER1 | 18 | 27 | 0.667 | A | - |
| CBUAE_EN_4881_VER1 | 18 | 56 | 0.321 | A | - |
| CBUAE_EN_7267_VER1 | 18 | 44 | 0.409 | A | - |
| CBUAE_EN_2757_VER1 | 17 | 45 | 0.378 | A | - |
| CBUAE_EN_7031_VER1 | 17 | 50 | 0.34 | A | - |
| CBUAE_EN_5114_VER1 | 16 | 18 | 0.889 | A | - |
| CBUAE_EN_6531_VER1 | 16 | 56 | 0.286 | A | - |
| CBUAE_EN_4473_VER1 | 16 | 26 | 0.615 | A | - |
| CBUAE_EN_7178_VER1 | 15 | 27 | 0.556 | A | - |
| CBUAE_EN_4711_VER1_0 | 15 | 48 | 0.312 | A | - |
| CBUAE_EN_5027_VER1 | 15 | 32 | 0.469 | A | - |
| CBUAE_EN_418_VER2 | 15 | 46 | 0.326 | A | - |
| CBUAE_EN_4689_VER1 | 14 | 32 | 0.438 | A | - |
| CBUAE_EN_1627_VER1 | 14 | 34 | 0.412 | A | - |
| CBUAE_EN_5558_VER1 | 14 | 33 | 0.424 | A | - |
| CBUAE_EN_1250_VER1 | 13 | 13 | 1.0 | A | - |
| CBUAE_EN_4728_VER1 | 13 | 9 | 1.444 | A | - |
| CBUAE_EN_7233_VER1 | 13 | 22 | 0.591 | A | - |
| CBUAE_EN_6052_VER1 | 13 | 27 | 0.481 | A | - |
| CBUAE_EN_6471_VER1 | 13 | 35 | 0.371 | A | - |
| CBUAE_EN_699_VER1 | 13 | 35 | 0.371 | A | - |
| CBUAE_EN_6986_VER1 | 13 | 16 | 0.812 | A | - |
| CBUAE_EN_7246_VER1 | 13 | 32 | 0.406 | A | - |
| CBUAE_EN_1286_VER1 | 12 | 59 | 0.203 | A | under_extracted |
| CBUAE_EN_4654_VER1 | 12 | 24 | 0.5 | A | - |
| CBUAE_EN_5974_VER1 | 12 | 20 | 0.6 | A | - |
| CBUAE_EN_7293_VER1 | 12 | 29 | 0.414 | A | - |
| CBUAE_EN_4640_VER1 | 11 | 31 | 0.355 | A | - |
| CBUAE_EN_1287_VER1 | 11 | 24 | 0.458 | A | - |
| CBUAE_EN_4044_VER1 | 11 | 12 | 0.917 | A | - |
| CBUAE_EN_1269_VER1 | 11 | 16 | 0.688 | A | - |
| CBUAE_EN_6034_VER1 | 11 | 19 | 0.579 | A | - |
| CBUAE_EN_6678_VER1 | 11 | 17 | 0.647 | A | - |
| CBUAE_EN_4185_VER1 | 11 | 13 | 0.846 | A | - |
| CBUAE_EN_5622_VER1 | 11 | 23 | 0.478 | A | - |
| CBUAE_EN_4208_VER1 | 11 | 31 | 0.355 | A | - |
| CBUAE_EN_6431_VER1 | 11 | 20 | 0.55 | A | - |
| CBUAE_EN_6415_VER1 | 11 | 19 | 0.579 | A | - |
| CBUAE_EN_5609_VER1 | 10 | 29 | 0.345 | A | - |
| CBUAE_EN_202_VER1 | 10 | 26 | 0.385 | A | - |
| CBUAE_EN_915_VER1 | 10 | 22 | 0.455 | A | - |
| CBUAE_EN_949_VER1 | 10 | 24 | 0.417 | A | - |
| CBUAE_EN_6070_VER1 | 10 | 27 | 0.37 | A | - |
| CBUAE_EN_4091_VER1_0 | 10 | 40 | 0.25 | A | - |
| CBUAE_EN_2387_VER1 | 10 | 21 | 0.476 | A | - |
| CBUAE_EN_644_VER1 | 10 | 34 | 0.294 | A | - |
| CBUAE_EN_6530_VER1 | 10 | 21 | 0.476 | A | - |
| CBUAE_EN_4496_VER1 | 10 | 19 | 0.526 | A | - |
| CBUAE_EN_6663_VER1 | 10 | 8 | 1.25 | A | - |
| CBUAE_EN_1249_VER1 | 9 | 43 | 0.209 | A | - |
| CBUAE_EN_1430_VER1 | 9 | 18 | 0.5 | A | - |
| CBUAE_EN_2200_VER1 | 9 | 17 | 0.529 | A | - |
| CBUAE_EN_2825_VER1 | 9 | 38 | 0.237 | A | - |
| CBUAE_EN_1494_VER1 | 9 | 42 | 0.214 | A | - |
| CBUAE_EN_2267_VER1 | 9 | 15 | 0.6 | A | - |
| CBUAE_EN_5791_VER1 | 9 | 13 | 0.692 | A | - |
| CBUAE_EN_5996_VER1 | 9 | 44 | 0.205 | A | under_extracted |
| CBUAE_EN_2776_VER1 | 8 | 16 | 0.5 | A | - |
| CBUAE_EN_5692_VER1 | 8 | 8 | 1.0 | A | - |
| CBUAE_EN_1836_VER1 | 8 | 12 | 0.667 | A | - |
| CBUAE_EN_1714_VER1 | 8 | 14 | 0.571 | A | - |
| CBUAE_EN_3459_VER1 | 8 | 20 | 0.4 | A | - |
| CBUAE_EN_7332_VER1 | 8 | 23 | 0.348 | A | - |
| CBUAE_EN_7000_VER1 | 8 | 33 | 0.242 | A | - |
| CBUAE_EN_1002_VER1 | 7 | 24 | 0.292 | A | - |
| CBUAE_EN_156_VER1 | 7 | 12 | 0.583 | A | - |
| CBUAE_EN_2405_VER1 | 7 | 8 | 0.875 | A | - |
| CBUAE_EN_2620_VER1 | 7 | 11 | 0.636 | A | - |
| CBUAE_EN_4588_VER1 | 7 | 13 | 0.538 | A | - |
| CBUAE_EN_1702_VER1 | 7 | 21 | 0.333 | A | - |
| CBUAE_EN_3440_VER1 | 7 | 25 | 0.28 | A | - |
| CBUAE_EN_4407_VER1 | 7 | 22 | 0.318 | A | - |
| CBUAE_EN_4429_VER1 | 7 | 32 | 0.219 | A | - |
| CBUAE_EN_6446_VER1 | 7 | 24 | 0.292 | A | - |
| CBUAE_EN_6708_VER1 | 7 | 23 | 0.304 | A | - |
| CBUAE_EN_3042_VER1 | 6 | 12 | 0.5 | A | - |
| CBUAE_EN_176_VER1 | 6 | 16 | 0.375 | A | - |
| CBUAE_EN_2028_VER1 | 6 | 12 | 0.5 | A | - |
| CBUAE_EN_2179_VER1 | 6 | 23 | 0.261 | A | - |
| CBUAE_EN_3509_VER1 | 6 | 17 | 0.353 | A | - |
| CBUAE_EN_2377_VER1 | 6 | 12 | 0.5 | A | - |
| CBUAE_EN_6672_VER1 | 6 | 14 | 0.429 | A | - |
| CBUAE_EN_1884_VER1 | 5 | 13 | 0.385 | A | - |
| CBUAE_EN_2839_VER1 | 5 | 3 | 1.667 | A | - |
| CBUAE_EN_2896_VER1 | 5 | 12 | 0.417 | A | - |
| CBUAE_EN_4246_VER1 | 5 | 7 | 0.714 | A | - |
| CBUAE_EN_1082_VER1 | 5 | 14 | 0.357 | A | - |
| CBUAE_EN_2370_VER1_0 | 5 | 9 | 0.556 | A | - |
| CBUAE_EN_1941_VER1 | 5 | 10 | 0.5 | A | - |
| CBUAE_EN_5583_VER1 | 5 | 11 | 0.455 | A | - |
| CBUAE_EN_2792_VER1 | 5 | 11 | 0.455 | A | - |
| CBUAE_EN_4841_VER1_0 | 5 | 5 | 1.0 | A | - |
| CBUAE_EN_1853_VER1 | 5 | 5 | 1.0 | A | - |
| CBUAE_EN_1953_VER1 | 5 | 12 | 0.417 | A | - |
| CBUAE_EN_2343_VER1 | 5 | 12 | 0.417 | A | - |
| CBUAE_EN_2809_VER1 | 5 | 14 | 0.357 | A | - |
| CBUAE_EN_3394_VER1 | 5 | 39 | 0.128 | A | under_extracted |
| CBUAE_EN_6018_VER1 | 5 | 18 | 0.278 | A | - |
| CBUAE_EN_2978_VER1 | 4 | 5 | 0.8 | A | - |
| CBUAE_EN_1130_VER1 | 4 | 10 | 0.4 | A | - |
| CBUAE_EN_2079_VER1 | 4 | 11 | 0.364 | A | - |
| CBUAE_EN_3070_VER1 | 4 | 10 | 0.4 | A | - |
| CBUAE_EN_7041_VER1 | 4 | 50 | 0.08 | A | under_extracted |
| CBUAE_EN_2850_VER1 | 4 | 20 | 0.2 | A | under_extracted |
| CBUAE_EN_2850_VER2 | 4 | 15 | 0.267 | A | - |
| CBUAE_EN_3406_VER2 | 4 | 13 | 0.308 | A | - |
| CBUAE_EN_7154_VER1 | 4 | 9 | 0.444 | A | - |
| CBUAE_EN_5590_VER1 | 4 | 11 | 0.364 | A | - |
| CBUAE_EN_5705_VER1 | 4 | 16 | 0.25 | A | - |
| CBUAE_EN_1150_VER1 | 3 | 26 | 0.115 | A | under_extracted |
| CBUAE_EN_2027_VER1 | 3 | 9 | 0.333 | A | - |
| CBUAE_EN_4171_VER1 | 3 | 6 | 0.5 | A | - |
| CBUAE_EN_2103_VER1 | 3 | 7 | 0.429 | A | - |
| CBUAE_EN_2865_VER1 | 3 | 14 | 0.214 | A | - |
| CBUAE_EN_3013_VER2 | 3 | 12 | 0.25 | A | - |
| CBUAE_EN_3133_VER1 | 3 | 11 | 0.273 | A | - |
| CBUAE_EN_3285_VER1 | 3 | 29 | 0.103 | A | under_extracted |
| CBUAE_EN_3486_VER1 | 3 | 14 | 0.214 | A | - |
| CBUAE_EN_3934_VER1 | 3 | 9 | 0.333 | A | - |
| CBUAE_EN_1082_VER2 | 2 | 12 | 0.167 | A | under_extracted |
| CBUAE_EN_2327_VER1 | 2 | 6 | 0.333 | A | - |
| CBUAE_EN_156_VER2 | 2 | 9 | 0.222 | A | - |
| CBUAE_EN_2839_VER2 | 2 | 4 | 0.5 | A | - |
| CBUAE_EN_2888_VER1 | 2 | 3 | 0.667 | A | - |
| CBUAE_EN_2896_VER2 | 2 | 9 | 0.222 | A | - |
| CBUAE_EN_3013_VER1 | 2 | 16 | 0.125 | A | under_extracted |
| CBUAE_EN_3106_VER1 | 2 | 2 | 1.0 | A | - |
| CBUAE_EN_3109_VER1 | 2 | 4 | 0.5 | A | - |
| CBUAE_EN_3121_VER1 | 2 | 7 | 0.286 | A | - |
| CBUAE_EN_3435_VER1 | 2 | 2 | 1.0 | A | - |
| CBUAE_EN_1702_VER2 | 1 | 8 | 0.125 | A | under_extracted |
| CBUAE_EN_1884_VER2 | 1 | 11 | 0.091 | A | under_extracted |
| CBUAE_EN_3117_VER1 | 1 | 3 | 0.333 | A | - |
| CBUAE_EN_3394_VER2 | 1 | 5 | 0.2 | A | under_extracted |
| CBUAE_EN_3406_VER1 | 1 | 18 | 0.056 | A | under_extracted |
| CBUAE_EN_3459_VER2 | 1 | 15 | 0.067 | A | under_extracted |
| CBUAE_EN_3844_VER1 | 1 | 3 | 0.333 | A | - |
| CBUAE_EN_3844_VER2 | 1 | 3 | 0.333 | A | - |
| CBUAE_EN_3845_VER1 | 1 | 3 | 0.333 | A | - |
| CBUAE_EN_3853_VER1_0 | 1 | 2 | 0.5 | A | - |
| CBUAE_EN_3858_VER1 | 1 | 9 | 0.111 | A | under_extracted |
| CBUAE_EN_3884_VER1 | 1 | 2 | 0.5 | A | - |
| CBUAE_EN_3901_VER1 | 1 | 2 | 0.5 | A | - |
| CBUAE_EN_3912_VER1_0 | 1 | 2 | 0.5 | A | - |
| CBUAE_EN_3919_VER1 | 1 | 5 | 0.2 | A | under_extracted |
| CBUAE_EN_3920_VER1 | 1 | 6 | 0.167 | A | under_extracted |
| CBUAE_EN_4122_VER1_0 | 1 | 4 | 0.25 | A | - |

## Prioritized fixes

1. **624 degree-1 nodes** — consider a deeper extraction pass.
