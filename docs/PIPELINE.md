# Pipeline — data flow and artifacts

```
rulebook.sama.gov.sa
        │  crawl        (playwright, one pass: tree + status + PDF links)
        ▼
raw-pdfs/sama/*.pdf ─── reports/sama/crawl/{tree,manifest}.json, crawl_report.md
        │  convert      (text layer → OCR when thin / presentation-form / isolated-Arabic)
        ▼
corpus/sama/markdown/*.md ────── reports/sama/conversion/conversion_quality.json
        │                                        CONVERSION_QUALITY_REPORT.md
        │               grade F → quarantine/sama/  (never reaches the graph)
        │  build        (snapshot → extract → dedup → cluster → label → export)
        ▼
graph-build/sama/graph.json ─── reports/sama/graph/dedup.json
        │
        ▼
Central Banks Knowledge Base/*.md      (raw graphify export)
        │  enrich
        │    ├─ ground()        free    → graph-build/sama/grounding.json
        │    ├─ enrich()        paid    → graph-build/sama/enrichment.jsonl
        │    │                            graph-build/sama/usage.jsonl
        │    ├─ render()        free    → rewrites vault notes
        │    └─ routing_index() free    → vault/_INDEX_Routing.md
        ▼                                 reports/sama/graph/routing_index.json
        │  audit        (read-only)
        ▼
reports/sama/graph/GRAPH_QUALITY_AUDIT.md + graph_quality_audit.json
```

## Artifacts

| Path | Written by | Survives a re-run? |
|---|---|---|
| `raw-pdfs/sama/*.pdf` | crawl | yes — existing files are skipped |
| `corpus/sama/markdown/*.md` | convert | overwritten |
| `quarantine/sama/*.md` | convert | overwritten |
| `graph-build/sama/graph.json` | build | replaced only after a successful extract |
| `archive/sama/graphify-snapshots/` | build | one snapshot per build |
| `graph-build/sama/grounding.json` | enrich (free) | regenerated each run |
| `graph-build/sama/enrichment.jsonl` | enrich (paid) | **append-only resume log** — delete to re-pay |
| `graph-build/sama/usage.jsonl` | enrich (paid) | append-only cost ledger |
| `Central Banks Knowledge Base/*.md` | build + enrich | rewritten by render |
| `reports/sama/**` | every stage | overwritten |
| `logs/sama/<stamp>/` | run.py | one directory per run |

> This describes the SAMA pipeline; CBUAE mirrors it exactly with `graph-build/cbuae/`,
> `corpus/cbuae/`, etc. in place of the `sama/` paths above — run with `--source cbuae`.
> All source (this file's `run.py`) lives under `codebase/` — run from there, or use
> `python codebase/run.py ...` from the repo root.

## Cost control

Only two stages spend money.

**build** — graph extraction. The model is pinned because graphify 0.9.23 breaks
on models that emit thinking blocks.

**enrich** — split into a free tier and a paid tier:

- *free*: every excerpt, every page locator, every caveat, the routing index
- *paid*: one summary per node (context sent **once**, not once per edge),
  one blurb per community, and a narrative for ~22% of edges

To rehearse without spending anything:

```bash
python run.py --stage enrich --skip-model     # grounding + render only
python run.py --stage enrich --limit-nodes 12 # small paid smoke test
```

Every API call appends to `graph-build/sama/usage.jsonl`; `run.py` prints the
running total at the end of a run.

## Re-running a stage

Stages are independent and idempotent.

```bash
python run.py --stage convert --stems SAMA_EN_5565_VER1 SAMA_EN_10959_VER1
python run.py --stage build --skip-extract      # re-dedup/cluster/export only
python run.py --stage enrich --apply-only       # re-render from existing data
python run.py --stage audit
```

`enrich` never re-pays for work already in `enrichment.jsonl`. To force a fresh
paid pass, delete that file.
