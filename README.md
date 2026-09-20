# Regulatory Knowledge Base (SAMA / CBUAE)

Turns a central bank's rulebook — currently the Saudi Central Bank (SAMA) and the
Central Bank of the UAE (CBUAE) — into a knowledge graph and a searchable Obsidian
vault, where every regulatory concept is a node, every cross-reference is a traceable
link, and **every link carries a verbatim quotation with an exact page citation** back
to the source instrument.

Five stages, one command.

```
crawl → convert → build → enrich → audit
```

The rule that governs everything here: **the corpus is the authority, the graph is
navigation.** The vault tells you where to look. `corpus/<source>/markdown/` tells you
what the rule says.

All source lives under `codebase/` — everything else at the repo root is pipeline
output, organised by purpose (`corpus/`, `raw-pdfs/`, `reports/`, etc.), each with a
`sama/` and `cbuae/` subfolder. See [Layout](#layout) for the full tree.

---

## Quick start

```bash
cd codebase
python -m pip install -r requirements.txt
```

```bash
python -m playwright install chromium
```

Copy `.env.example` to `.env` in the **repo root** (next to this README, one level up
from `codebase/`) and fill in your keys. Then check everything is wired up before
spending anything:

```bash
python run.py --all --dry-run
```

Then run it:

```bash
python run.py --all
```

`run.py` resolves every path from its own location, so `python codebase/run.py ...`
from the repo root works exactly the same as `cd codebase && python run.py ...` — pick
whichever you prefer.

Open `Central Banks Knowledge Base/` (in the repo root) in Obsidian. Start at
`_INDEX_Routing.md`.

---

## Two regulators, one vault, never one graph

Everything above runs SAMA (the default). Point the whole pipeline at CBUAE instead
with `--source`:

```bash
python run.py --source cbuae --stage crawl --manifest-only   # see what it would fetch, fetch nothing
python run.py --source cbuae --all
```

`--source` (or `KB_SOURCE=cbuae` in the environment) switches every path the pipeline
touches — `raw-pdfs/cbuae/`, `corpus/cbuae/`, `graph-build/cbuae/`, `reports/cbuae/`,
`logs/cbuae/`, `archive/cbuae/`, `quarantine/cbuae/` — so `graphify` is always invoked
against exactly one regulator's corpus and never sees the other's documents. That's
what actually keeps the two graphs from intertwining: it isn't a filter applied
afterwards, the two builds simply never share a working directory.

The one thing the two sources share on purpose is the Obsidian vault: each source
exports into its own subfolder of one shared vault (`Central Banks Knowledge Base/SAMA/`,
`.../CBUAE/`, or wherever `GRAPHIFY_VAULT_DIR` points), so you get one place to browse
both. Because Obsidian resolves `[[wikilinks]]` by note name across the *entire* vault
regardless of folder, every note's filename and every wikilink pointing at it carries
that source's `SAMA — ` / `CBUAE — ` prefix (see `sama/graph.py:namespace_vault`) — a
generic label such as "Board of Directors" exists in both rulebooks' own vocabulary, and
without the prefix Obsidian could silently resolve a link into the wrong regulator's
note.

Color-code the graph view by source and by community with `python -m sama.colorize`
(run from `codebase/`, after both sources have an `enrich` pass so `community_name` is
populated) — it writes `.obsidian/graph.json`'s `colorGroups`: one shade per community,
green-family for SAMA and blue-family for CBUAE, so the graph reads as "regulator" at
the hue level and "sub-cluster" at the shade level. It's a personal Obsidian display
setting, not a pipeline artifact, so it's not wired into `run.py`; re-run it any time
either source's communities are relabeled. Close and reopen the graph view (or Obsidian
itself) afterwards — Obsidian only reloads `graph.json` when the view is (re)opened, and
will otherwise overwrite the file with its own in-memory state on the next graph
interaction.

Enrichment for the two sources uses separate env-var families (`SAMA_ENRICH_*` /
`CBUAE_ENRICH_*` — see `.env.example`) so they can bill to different keys/workspaces,
and each source's `graph-build/<source>/usage.jsonl` is already a separate cost ledger
by virtue of living in a separate directory.

CBUAE's crawl stage (`sama/crawl_cbuae.py`) walks a genuinely different site (also
Drupal, but real nested `<ul>/<li>` sidebar markup rather than SAMA's pixel-geometry
tree, and both English and Arabic trees). It has been checked against the live site's
DOM structure but not yet run end-to-end — **run `--source cbuae --stage crawl
--manifest-only` first** and read `reports/cbuae/crawl/crawl_report.md` before trusting
anything downstream of it.

> **About this reorg.** The paths above reflect a September 2026 cleanup: source moved
> into `codebase/`, and every output category (`corpus/`, `raw-pdfs/`, `graph-build/`,
> `reports/`, `logs/`, `archive/`, `quarantine/`, `tmp/`) now sits at the repo root with
> a `sama/`/`cbuae/` subfolder, instead of the old flat `corpus_cbuae/`,
> `graphify-out-cbuae/`, `scanner-sama-docs/` naming. `graphify`'s own `extract` call was
> updated to pass its corpus target as a full relative path rather than a bare directory
> name, so the extra nesting under `corpus/<source>/` is handled explicitly. Its
> `cluster-only`/`label`/`export obsidian` calls take no directory argument for the graph
> they act on — graphify appears to locate the promoted graph itself via its own marker
> files — and that lookup was not otherwise touched by this reorg. That one mechanism
> could not be exercised while making this change (no sandbox available here has
> `graphify` installed), so **run a small `--stage build` before trusting a full
> re-run** — a few converted documents is enough to see whether `build` still finds and
> promotes the graph correctly end to end.

---

## Requirements

| | | |
|---|---|---|
| Python | ≥ 3.9 | |
| PyMuPDF, Pillow, pytesseract | `pip install -r requirements.txt` | PDF and OCR |
| Playwright + Chromium | `python -m playwright install chromium` | acquisition |
| Tesseract | `brew install tesseract` / apt / installer | OCR engine — language data ships in `tools/tessdata/` |
| `graphify` | on `PATH`, or set `GRAPHIFY_BIN` | graph extraction |
| API key | `.env` | extraction and enrichment |

`--dry-run` reports exactly which of these are missing, scoped to the stages you
asked for, and refuses to start rather than failing halfway through.

---

## Stages

| Stage | Does | Tokens |
|---|---|---|
| `crawl` | One browser pass over the Rulebook: tree, publication status, PDF links. Downloads in-force instruments only. | no |
| `convert` | PDF → markdown with OCR fallback, graded in the same pass. Grade F is quarantined. | no |
| `build` | Snapshot → extract → dedup → cluster → label → export vault → repair wikilinks. | yes |
| `enrich` | Deterministic grounding (free), model summaries (paid), note rendering, routing index. | partly |
| `audit` | Read-only quality report. Modifies nothing. | no |

Run them individually, or resume from one:

```bash
python run.py --stage convert
```

```bash
python run.py --from-stage build
```

---

## How it works

### Acquisition filters at the source

Only instruments the Rulebook presents as **In-Force** are downloaded. Superseded
material never enters the corpus, so there is no retirement problem to solve
downstream. Override with `SAMA_REQUIRE_IN_FORCE=0` if you need the full set.

### Conversion routes to OCR on three signals

A document goes to 200 DPI OCR when its text layer is too thin, when it shows
isolated Arabic fragments, **or when it contains Arabic presentation-form glyphs**.

That third signal is the one that matters. A PDF can store Arabic as rendered glyph
shapes in visual order (`U+FB50–FDFF`, `U+FE70–FEFF`) rather than as readable
characters. Such a file looks healthy on every conventional metric — normal page
count, high character density, no replacement characters — and is completely
unsearchable:

```
stored:  ﺔﻳﻮﻀﻌﻟﺍ ﺢﺘﻓ ﻁﻭﺮﺷ   ﺕﺎﻧﺎﻴﺒﻟﺍ ﺚﻳﺪﺤﺗ
means:   شروط فتح العضوية    تحديث البيانات
```

Detection covers the standard Arabic block *and* both presentation-form blocks, in
one shared implementation (`sama/common.py`). Anything that survives is normalised
back to base letters and reversed to reading order.

Text is stored in **logical order**, never display order. `arabic-reshaper` and
`python-bidi` are deliberately not dependencies: they produce display forms, and
writing those to disk is what makes a corpus unsearchable.

### Grounding is deterministic, not generated

For each relationship, the supporting sentence is chosen by keyword scoring and
**sliced directly out of the source file**. It is therefore verbatim by
construction, and because the slice's byte offset is known, its page number is
exact rather than estimated.

Caveats are derived, not asked for — from relationship confidence, weak relation
types, and the measured Arabic quality of the cited source.

This costs nothing and cannot drift.

### The model does only synthesis

| Tier | Produces | Cost |
|---|---|---|
| Free | excerpts, page locators, caveats, dedup, all vault notes, routing index | **$0** |
| Paid | concept summaries + lookup terms, community themes, selected relationship narratives | metered |

Relationship narratives are earned, not universal: links that cross regimes, links
whose confidence is `INFERRED`/`AMBIGUOUS`, and links on high-traffic hubs.

Concept context is sent once per concept rather than once per relationship, the
system prompt is cacheable, calls run concurrently with backoff, and every call is
logged to `graph-build/<source>/usage.jsonl` with token counts and estimated cost.

You can run the free tier alone and get a complete, fully cited vault:

```bash
python run.py --stage enrich --skip-model
```

Then add the paid tier whenever you like. Nothing is recomputed and nothing is paid
for twice — `enrichment.jsonl` is an append-only resume log, which also means an
interrupted run continues rather than restarting.

### Concepts are deduplicated

Graph extraction emits one node per (concept, source document), so a law cited by
ten circulars becomes ten near-identical notes and a reader cannot tell which is
authoritative. `build` merges on normalised label between extraction and
clustering — unioning edges, keeping every source, dropping the self-loops and
parallel edges that merging creates.

### The audit reports what it cannot measure

A dimension that cannot be computed grades **N/A**, is excluded from the average,
and is flagged at the top of the report. It never grades as a pass. Broken-Arabic
exposure is measured straight from the corpus, so it is reported even before
anything has been graded.

---

## What a note looks like

```markdown
# Customer Due Diligence (CDD)

Defines the identification and verification measures a financial institution must
apply before establishing a business relationship. Binds banks, finance companies
and payment service providers.

**Regimes:** AML/CTF, payments

## Sources
- `corpus/sama/markdown/SAMA_EN_1704_VER1.md`

## Connections

### [[Beneficial Owner Verification]] — `imposes_obligation_on` [EXTRACTED]
- **What this link tells you:** When scoping onboarding obligations for a finance
  company, CDD and beneficial-owner identification cannot be treated as separate
  workstreams, because …
- **Grounding — this node** (SAMA_EN_1704_VER1 · Page 12): "…"
- **Grounding — related node** (SAMA_EN_10959_VER1 · Page 3): "…"

## Lookup terms
`cdd`, `due diligence`, `onboarding`, `identification`, `verification`
```

Every quotation is a literal slice of the cited file at the cited page.

---

## Layout

```
.
├── .env                                 secrets (gitignored) — one level above codebase/
├── .env.example                         tracked template
├── docs/
│   ├── PROPOSAL.md                      scope, design principles, risks, delivery plan
│   ├── PIPELINE.md                      data flow and artifacts
│   ├── SESSION.md                       runbook and open items
│   └── agents/                          reference copies of the live *-counsel / *-digger / *-auditor / gcc-counsel Claude Skills
│
├── codebase/                            all source — the only durable, tracked code
│   ├── run.py                           entry point
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── sama/
│   │   ├── config.py                    every path, threshold, model and key
│   │   ├── common.py                    Arabic, stems, page maps, wikilinks, tables
│   │   ├── crawl.py                     stage 1 (SAMA)
│   │   ├── crawl_cbuae.py               stage 1 (CBUAE)
│   │   ├── convert.py                   stage 2
│   │   ├── graph.py                     stage 3
│   │   ├── enrich.py                    stage 4
│   │   └── audit.py                     stage 5
│   └── tests/                           no network or API key required
│
│   # everything below is pipeline output — re-derivable, gitignored, one
│   # sama/ + cbuae/ (or CBUAE/) subfolder per category:
│
├── raw-pdfs/{sama,cbuae}/               downloaded PDFs (was scanner-<source>-docs/)
├── corpus/{sama,cbuae}/markdown/        converted text — the authority
├── quarantine/{sama,cbuae}/             failed conversions, held out of the graph
├── graph-build/{sama,cbuae}/            graph.json, grounding.json, enrichment.jsonl, usage.jsonl (was graphify-out*/)
├── archive/{sama,cbuae}/graphify-snapshots/   pre-build snapshots
├── reports/{sama,cbuae}/{crawl,conversion,graph}/
├── logs/{sama,cbuae}/<run-timestamp>/   one folder per pipeline run (was reports/runs/)
├── tmp/{sama,cbuae}/                    OCR scratch space, safe to wipe anytime
├── tools/tessdata/                      eng + ara OCR language data (shared, not per-source)
└── Central Banks Knowledge Base/        the vault — open THIS in Obsidian (CBUAE writes into its own CBUAE/ subfolder inside it)
```

Only `codebase/`, `docs/`, `tools/tessdata/` and `.env*` are durable. Everything else
is output — see `codebase/sama/config.py`'s module docstring for the authoritative,
always-current version of this tree.

Querying the corpus (turning a compliance question into a cited answer) is not done
with any code in this repo. It runs as Claude Skills — `sama-counsel` / `sama-digger`
/ `sama-auditor` for SAMA, `cbuae-counsel` / `cbuae-digger` / `cbuae-auditor` for
CBUAE, and `gcc-counsel` for questions spanning both — that Grep/Read
`corpus/<source>/markdown/` and the three `graph-build/<source>/` files above directly;
no script, shell command or Python runs in that path. Read `docs/agents/` for what each
one does — those files are a point-in-time copy for humans, not the live source; the
skills themselves live in Claude's own skills system, outside this repo. The old
`.opencode/` agent definitions and `sama/retrieve.py` / `sama/cite.py` (the CLI scripts
those agents shelled out to) have been removed — this pipeline now only builds and
refreshes the knowledge base; it no longer answers questions itself.

---

## Configuration

All defaults live in `sama/config.py`. Nothing else hardcodes a path, threshold or
model name. Environment variables override; `run.py` loads `.env` automatically,
and an explicit `export` always wins.

| Variable | Default | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | graph extraction |
| `GRAPHIFY_MODEL` | `claude-opus-4-8` | extraction model |
| `GRAPHIFY_BIN` | `graphify` | if not on `PATH` |
| `SAMA_ENRICH_API_KEY` | falls back to `ANTHROPIC_API_KEY` | enrichment — may bill separately |
| `SAMA_ENRICH_MODEL` | `claude-opus-5` | enrichment model |
| `SAMA_ENRICH_WORKSPACE_ID` | — | required for identity-linked API keys |
| `SAMA_ENRICH_WORKERS` | `6` | concurrent enrichment calls |
| `SAMA_EDGE_NARRATIVE_MAX` | `400` | cap on paid relationship narratives |
| `SAMA_REQUIRE_IN_FORCE` | `1` | `0` also ingests superseded instruments |
| `SAMA_DEDUP_NODES` | `1` | `0` keeps duplicate-label concepts |
| `GRAPHIFY_VAULT_DIR` | `Central Banks Knowledge Base` | vault location |
| `TESSERACT_CMD` | auto-detected | if not on `PATH` |

Secrets belong in `.env` (gitignored) or the environment — never in tracked source.
No code path prints a key value.

---

## Common tasks

Rehearse a single document before committing to the whole corpus:

```bash
python run.py --stage convert --stems SAMA_EN_5565_VER1
```

Rebuild the graph without re-extracting:

```bash
python run.py --stage build --skip-extract
```

Re-render notes from existing grounding and enrichment, with no API calls:

```bash
python run.py --stage enrich --apply-only
```

Small paid smoke test before a full enrichment pass:

```bash
python run.py --stage enrich --limit-nodes 12
```

Check quality at any time:

```bash
python run.py --stage audit
```

---

## Tests

```bash
cd codebase && python -m pytest
```

(or `python -m pytest codebase` from the repo root — both pick up `codebase/pytest.ini`,
which sets `pythonpath = .` so `sama` imports correctly either way.)

No network, no API key, no PDFs required. The suite pins Arabic presentation-form
detection and repair, the OCR routing decisions (including the dense-but-garbled
case that conventional metrics miss), page-offset locators, wikilink aliasing,
concept dedup, and the audit's N/A-not-pass behaviour.

---

## Known limits

- Grounding finds a supporting sentence on both sides of roughly 85% of
  relationships. The remainder carry a one-sided excerpt and an automatic caveat
  saying so.
- Concept extraction quality depends on the graph toolchain; sparsely-connected
  concepts reflect extraction depth, not a defect in this pipeline.
- PDF→markdown coverage can only be measured once PDFs are on disk. A fresh
  checkout has none, and the audit correctly reports `N/A` rather than a pass.
- This is a **build-once** pipeline. Refreshing is a full re-run, not an
  incremental sync. Because acquisition filters to in-force instruments, a re-run
  also retires superseded material automatically.

---

## Scope

This knowledge base routes to primary regulatory text and cites it. It is not a
source of legal advice, and it is not a substitute for reading the instrument.
Unresolved gaps are surfaced rather than hidden — see `docs/PROPOSAL.md` §8 for the
quality model and §14 for what the project holds itself to.
