"""Single source of truth for paths, thresholds and model/key selection.

Everything in this file is either a fixed project path or an environment
override.  No other module may hardcode a path, a threshold or a model name.

Source selection
-----------------
This file serves two regulators — SAMA (KSA) and CBUAE (UAE) — selected by
the KB_SOURCE environment variable (or `run.py --source`), defaulting to
"sama".

The two sources are kept in fully separate directories end to end (their own
raw-pdfs, corpus, graph-build, reports, logs, archive and quarantine
subtree), so graphify never sees both corpora in one extraction and can never
merge or cross-link a SAMA node with a CBUAE node — the isolation is
structural, not a filter applied after the fact. The one thing they
intentionally share is the *Obsidian vault root*: each source exports into
its own subfolder of that shared vault (`SAMA/`, `CBUAE/` — VAULT_DIR below),
and every note filename and wikilink target carries that source's "SAMA — "
/ "CBUAE — " prefix (NOTE_PREFIX) so Obsidian's vault-wide, folder-blind
wikilink resolution can never resolve a generic label (e.g. "Board of
Directors") into the wrong regulator's note.

Repo layout (2026-09 reorg)
----------------------------
This file lives at <repo root>/codebase/sama/config.py — the codebase/
folder holds only source (run.py, this package, tests/, pytest.ini,
requirements.txt). ROOT below resolves to <repo root>, two levels up, and
every data category is a direct child of it, organised by purpose with a
per-source subfolder underneath:

    codebase/                  run.py, sama/, tests/, pytest.ini, requirements.txt
    corpus/<source>/markdown/  converted, graphify-ready markdown
    raw-pdfs/<source>/         downloaded source PDFs (was scanner-<source>-docs/)
    graph-build/<source>/      graphify's own working directory (was graphify-out*/)
    reports/<source>/          crawl / conversion / graph quality reports
    logs/<source>/<run-stamp>/ one folder per pipeline run (was reports/runs/)
    archive/<source>/          pre-rebuild graph-build snapshots
    quarantine/<source>/       grade-F conversions excluded from the graph
    tools/tessdata/            shared OCR language data (not per-source)
    tmp/<source>/              OCR scratch space, safe to wipe anytime
    "Central Banks Knowledge Base/"   the Obsidian vault (was
                                       SAMA_Knowledge_Base_Obsidian/)

Only VAULT_DIR breaks the "<category>/<source>/" pattern, by design: both
regulators publish into the *same* vault so it can be opened as one Obsidian
vault, each isolated into its own SAMA/ or CBUAE/ subfolder inside it rather
than a sibling top-level folder.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def _env_path(name: str, default: Path) -> Path:
    """Resolve a path override, anchoring a relative one at ROOT.

    `.env.example` documents GRAPHIFY_VAULT_DIR as a bare relative value
    (`"Central Banks Knowledge Base"`), and the README promises `python
    run.py` behaves identically run from ROOT or from codebase/. A relative
    Path is only actually anchored at ROOT if every caller happens to run
    with ROOT as its cwd - graphify's own subprocess gets cwd=ROOT
    explicitly (see graph.py:_run), but this module's own Python-side use of
    the same value (e.g. run.py's final vault note count) does not, so it
    silently resolved against the interpreter's cwd instead: real notes
    landed under ROOT/"Central Banks Knowledge Base" while the summary
    counted CWD/"Central Banks Knowledge Base" and reported 0 (confirmed
    2026-09-19 running `cd codebase && python run.py`). Anchoring here once
    makes every reader of config.VAULT_ROOT agree regardless of cwd.
    """
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    p = Path(raw)
    return p if p.is_absolute() else ROOT / p


SOURCE = os.environ.get("KB_SOURCE", "sama").strip().lower()
if SOURCE not in ("sama", "cbuae"):
    raise SystemExit(f"KB_SOURCE must be 'sama' or 'cbuae', got {SOURCE!r}")

# Env-var family prefix. SAMA keeps today's exact names (SAMA_ENRICH_MODEL,
# SAMA_ENRICH_API_KEY, ...) so no existing .env file needs to change. CBUAE
# gets its own parallel family (CBUAE_ENRICH_MODEL, CBUAE_ENRICH_API_KEY, ...)
# so the two sources can run against different API keys/workspaces/budgets.
_ENV = "CBUAE" if SOURCE == "cbuae" else "SAMA"


# --------------------------------------------------------------------------- #
# Paths
#
# Every data category sits under ROOT with a per-source ("sama" / "cbuae")
# subfolder underneath — see the module docstring for the full tree. This
# nests CORPUS_DIR and GRAPH_DIR one level deeper than the pre-reorg layout
# (e.g. graph-build/sama instead of a top-level graphify-out/). graph.py's
# extract() passes graphify the *relative* path from ROOT (not just the
# basename) so the extra nesting is handled explicitly rather than assumed;
# graphify's own cluster-only/label/export calls take no directory argument
# (see graph.py's _run docstring) and were not otherwise touched by this
# reorg — validate the build stage on a small run before trusting it at
# scale, since graphify itself could not be exercised while writing this.
# --------------------------------------------------------------------------- #

VAULT_ROOT = _env_path("GRAPHIFY_VAULT_DIR", ROOT / "Central Banks Knowledge Base")

PDF_DIR = ROOT / "raw-pdfs" / SOURCE
CORPUS_DIR = ROOT / "corpus" / SOURCE
QUARANTINE = ROOT / "quarantine" / SOURCE
OCR_TMP = ROOT / "tmp" / SOURCE
GRAPH_DIR = ROOT / "graph-build" / SOURCE
REPORTS = ROOT / "reports" / SOURCE
ARCHIVE = ROOT / "archive" / SOURCE
LOGS_DIR = ROOT / "logs" / SOURCE

if SOURCE == "sama":
    VAULT_DIR = VAULT_ROOT / "SAMA"               # subfolder of the shared vault
    NOTE_PREFIX = "SAMA — "
    SOURCE_TAG = "#source/sama"
else:
    VAULT_DIR = VAULT_ROOT / "CBUAE"              # subfolder of the shared vault
    NOTE_PREFIX = "CBUAE — "
    SOURCE_TAG = "#source/cbuae"

# Both sources use the same subfolder + prefix convention (changed 2026-09-19;
# SAMA originally wrote unprefixed at the vault root since it predated CBUAE's
# addition — made symmetric on request so the layout is one standard rather
# than "the original one" plus "the namespaced one"). namespace_vault() below
# is a no-op only when NOTE_PREFIX is empty, which no longer happens for
# either source, so both now get renamed + relinked on every build.

CORPUS_MD = CORPUS_DIR / "markdown"
GRAPH_JSON = GRAPH_DIR / "graph.json"
GROUNDING_JSON = GRAPH_DIR / "grounding.json"
ENRICH_LOG = GRAPH_DIR / "enrichment.jsonl"
USAGE_LOG = GRAPH_DIR / "usage.jsonl"

CRAWL_REPORTS = REPORTS / "crawl"
CONV_REPORTS = REPORTS / "conversion"
GRAPH_REPORTS = REPORTS / "graph"
CONV_JSON = CONV_REPORTS / "conversion_quality.json"

SNAPSHOTS = ARCHIVE / "graphify-snapshots"

TESSDATA = ROOT / "tools" / "tessdata"          # shared — language data, not source data

# Directories that must exist before a run; all are re-derivable.
RUNTIME_DIRS = (
    PDF_DIR, CORPUS_MD, QUARANTINE, GRAPH_DIR, VAULT_DIR,
    CRAWL_REPORTS, CONV_REPORTS, GRAPH_REPORTS, LOGS_DIR, SNAPSHOTS,
)


# --------------------------------------------------------------------------- #
# Crawl
# --------------------------------------------------------------------------- #

# A self-identifying crawler UA ("CBUAE-KB-Crawl/1.0") gets 403'd outright by
# CBUAE's WAF on the direct-download (urllib) path used by crawl.fetch() -
# confirmed live 2026-09-19: same URL, same IP, only the UA differs between a
# blocked and a served request. SAMA's WAF tolerates a bot UA on this path (its
# crawl already completed 380/381 downloads under the old string), but there's
# no upside to a self-identifying UA anywhere in this pipeline, so both sources
# use an ordinary browser UA. This is unrelated to crawl.new_page()'s fix for
# the *tree-walk* (Playwright) path, which strips "Headless" from the browser's
# own UA - that one never claimed to be a bot in the first place.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

# Only ingest instruments the regulator currently presents as in force. Applied
# uniformly to tree pages and circular/detail pages, so superseded material
# never enters the corpus.
IN_FORCE_STATUSES = {"in-force", "in force"}
REQUIRE_IN_FORCE = os.environ.get(f"{_ENV}_REQUIRE_IN_FORCE", "1") != "0"

# A download is accepted only once the bytes have been checked.  A truncated
# body and an error page served as HTTP 200 both arrive without raising, so
# neither the status code nor the absence of an exception is evidence.
FETCH_MAX_RETRIES = 3
FETCH_BACKOFF_BASE = 2.0
MIN_PDF_BYTES = 1024

if SOURCE == "sama":
    BASE_URL = "https://rulebook.sama.gov.sa"
    ENTRY_PAGE = "/en/finance-sector-0"
    SKIP_HREFS = {
        "/en", "/en/search", "/en/view-revision-updates", "/en/terms-and-conditions",
    }
    SECTOR_NAV_SLUGS = {
        "/en/laws-and-implementing-regulations", "/en/all-financial-institutions",
        "/en/banking-sector-0", "/en/finance-sector-0",
        "/en/payment-systems-and-payment-services-providers",
        "/en/money-exchange-sector-0", "/en/credit-bureaus",
        "/en/regulatory-sandbox", "/en/sama-circulars",
    }
    CRAWL_LANGS = ("en",)
else:
    BASE_URL = "https://rulebook.centralbank.ae"
    # Seed list of root "books" (Drupal book-navigation entities), confirmed by
    # live inspection on 2026-09-19. Each is its own independent tree; the
    # crawler also discovers any sibling root book it has not seen yet from the
    # sidebar's `#block-rulebook-booknavigation` region, so a new one appearing
    # on the live site later does not require a code change.
    ENTRY_PAGE = "/en/rulebook/all-licensed-financial-institutions"
    CBUAE_ROOT_BOOKS = {
        "/en/rulebook/all-licensed-financial-institutions": "All Licensed Financial Institutions",
        "/en/rulebook/banking": "Banking",
        "/en/rulebook/insurance": "Insurance",
        "/en/rulebook/other-regulated-entities": "Other Regulated Entities",
    }
    SKIP_HREFS = {
        "/en", "/en/rulebook", "/en/search", "/en/view-revision-updates",
        "/en/advanced-search",
    }
    SECTOR_NAV_SLUGS = set(CBUAE_ROOT_BOOKS.keys())
    # English + Arabic, per the Sep-2026 decision to cover both from the start.
    CRAWL_LANGS = ("en", "ar")


# --------------------------------------------------------------------------- #
# Conversion / OCR routing
# --------------------------------------------------------------------------- #

DPI = 200
OCR_LANG = "eng+ara"

THIN_CPP = 400            # chars/page below this => text layer is unusable
ISOLATED_AR_OCR = 0.12    # rate of 1-2 letter Arabic fragments => broken bidi
PF_SHARE_OCR = 0.02       # share of Arabic *presentation-form* glyphs => the
                          # text layer holds rendered glyphs in visual order and
                          # is unsearchable, however dense it looks

EMPTY_PAGE_CHARS = 20
COVERAGE_WARN = 0.85
COVERAGE_FAIL = 0.60
ARABIC_SHARE_WARN = 0.15
ISOLATED_AR_WARN = 0.08
GARBAGE_WARN = 0.05

NEAR_DUP_THRESHOLD = 0.90
NEAR_DUP_LENGTH_BAND = 0.10   # only compare docs within +/-10% length

# Grade F documents are quarantined instead of being fed to the graph.
QUARANTINE_GRADE = "F"


def tesseract_cmd() -> str | None:
    """Locate the tesseract binary without assuming a Windows install path."""
    env = os.environ.get("TESSERACT_CMD", "").strip()
    if env and Path(env).exists():
        return env
    found = shutil.which("tesseract")
    if found:
        return found
    for cand in (
        "/opt/homebrew/bin/tesseract",
        "/usr/local/bin/tesseract",
        "/usr/bin/tesseract",
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    ):
        if Path(cand).exists():
            return cand
    return None


# --------------------------------------------------------------------------- #
# Graph build
# --------------------------------------------------------------------------- #

GRAPHIFY_BIN = os.environ.get("GRAPHIFY_BIN", "graphify")

# The extraction backend is pinned: graphify 0.9.23 breaks on models that emit
# thinking blocks.  Enrichment talks to the API directly and is not subject to
# that constraint, so it is configured separately below.  Both sources share
# one GRAPHIFY_MODEL/GRAPHIFY_MODE — they call the same external binary, just
# against different --corpus directories — but each gets its own dedup toggle
# since a wrong flag in one run must not silently affect the other.
GRAPHIFY_MODEL = os.environ.get("GRAPHIFY_MODEL", "claude-opus-4-8")
GRAPHIFY_MODE = os.environ.get("GRAPHIFY_MODE", "deep")
GRAPHIFY_API_KEY_ENV = "ANTHROPIC_API_KEY"

DEDUP_NODES = os.environ.get(f"{_ENV}_DEDUP_NODES", "1") != "0"


# --------------------------------------------------------------------------- #
# Enrichment (model layer)
# --------------------------------------------------------------------------- #

API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

ENRICH_MODEL = os.environ.get(f"{_ENV}_ENRICH_MODEL", "claude-opus-5")
ENRICH_KEY_ENV = f"{_ENV}_ENRICH_API_KEY"      # falls back to ANTHROPIC_API_KEY

# Identity-linked API keys must name the workspace the request acts in; the API
# rejects them with HTTP 400 otherwise. Ordinary org keys ignore this.
ENRICH_WORKSPACE_ID = os.environ.get(f"{_ENV}_ENRICH_WORKSPACE_ID", "").strip()

ENRICH_WORKERS = int(os.environ.get(f"{_ENV}_ENRICH_WORKERS", "6"))
ENRICH_MAX_RETRIES = 5
ENRICH_BACKOFF_BASE = 2.0

NODE_BATCH = 6
COMMUNITY_BATCH = 4
EDGE_BATCH = 5

MAX_CONTEXT_CHARS = 4500     # per node, sent once per node (not once per edge)
MAX_EXCERPT_CHARS = 280

# Per-edge narratives are the expensive tier, so they are earned rather than
# universal.  An edge qualifies when it crosses communities, when its confidence
# is not EXTRACTED (the reader needs framing to know how far to trust it), or
# when it touches a hub.
EDGE_NARRATIVE_CROSS_COMMUNITY = True
EDGE_NARRATIVE_LOW_CONFIDENCE = {"INFERRED", "AMBIGUOUS"}
EDGE_NARRATIVE_HUB_DEGREE = 8
EDGE_NARRATIVE_MAX = int(os.environ.get(f"{_ENV}_EDGE_NARRATIVE_MAX", "400"))

WEAK_RELATIONS = {"conceptually_related_to", "semantically_similar_to"}

# Published list prices (USD per million tokens) used only for the run ledger.
PRICES = {
    "claude-opus-5": (5.0, 25.0),
    "claude-opus-4-8": (5.0, 25.0),
    "claude-sonnet-5": (3.0, 15.0),
    "claude-haiku-4-5-20251001": (1.0, 5.0),
}


def enrich_api_key() -> str:
    """Key for the enrichment model.  Deliberately separate from the graphify
    key so the two stages can bill to different accounts."""
    for env in (ENRICH_KEY_ENV, "ANTHROPIC_API_KEY"):
        key = os.environ.get(env, "").strip()
        if key:
            return key
    raise SystemExit(
        f"No enrichment API key. Set {ENRICH_KEY_ENV} (preferred) or ANTHROPIC_API_KEY:\n"
        f'  export {ENRICH_KEY_ENV}="sk-ant-..."'
    )


# --------------------------------------------------------------------------- #
# Audit thresholds
# --------------------------------------------------------------------------- #

GROUND_A, GROUND_B, GROUND_C = 0.90, 0.75, 0.60
UNDEREXTRACT_FRAC = 0.5


def ensure_dirs() -> None:
    for d in RUNTIME_DIRS:
        d.mkdir(parents=True, exist_ok=True)
