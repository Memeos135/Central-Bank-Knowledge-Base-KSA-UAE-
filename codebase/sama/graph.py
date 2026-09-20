"""Stage 3 - build the knowledge graph, deduplicate it, export the vault.

The live graph is snapshotted before anything runs and replaced only once a new
extraction has succeeded, so a failed build cannot leave it half-updated.

Order matters: dedup runs between extract and cluster, so the community pass and
the Obsidian export both see one node per entity rather than one per
(entity, source document).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import config
from .common import read_json, write_json


def _run(args: List[str], step: str) -> None:
    """Run one graphify subprocess with cwd fixed at the repo root.

    Every path graphify needs is therefore passed explicitly, relative to
    ROOT (see cluster_and_label()/export_vault() below) rather than relying
    on cwd-relative defaults or graphify's own marker-file lookup.
    """
    print(f"\n=== {step} ===\n$ {' '.join(args)}", flush=True)
    proc = subprocess.run(args, cwd=str(config.ROOT))
    if proc.returncode != 0:
        raise RuntimeError(f"{step} failed (exit {proc.returncode})")


def check_prereqs() -> None:
    if shutil.which(config.GRAPHIFY_BIN) is None:
        raise SystemExit(
            f"'{config.GRAPHIFY_BIN}' is not on PATH.\n"
            "  Install it, or point SAMA config at it:  export GRAPHIFY_BIN=/path/to/graphify"
        )
    if not os.environ.get(config.GRAPHIFY_API_KEY_ENV, "").strip():
        raise SystemExit(
            f"{config.GRAPHIFY_API_KEY_ENV} is not set (graphify needs it for extraction).\n"
            f'  export {config.GRAPHIFY_API_KEY_ENV}="sk-ant-..."'
        )


def snapshot() -> Optional[Path]:
    """Copy the live graph aside before touching it."""
    if not config.GRAPH_JSON.exists():
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = config.SNAPSHOTS / f"graphify-out_{stamp}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(config.GRAPH_DIR, dest)
    print(f"Snapshot: {dest}")
    return dest


def extract(force: bool = True) -> None:
    """Extract into <corpus>/graphify-out, then promote only on success.

    graphify creates its own `graphify-out` subfolder inside whatever
    directory it is told to extract — that target is passed as a path
    relative to cwd (ROOT, per _run), not a bare directory name, so this
    works whether CORPUS_DIR is one level under ROOT or several (it is now
    `corpus/<source>/`, two levels deep, after the 2026-09 path reorg).
    """
    staged = config.CORPUS_DIR / "graphify-out"
    if staged.exists():
        shutil.rmtree(staged)

    corpus_arg = config.CORPUS_DIR.relative_to(config.ROOT).as_posix()

    # Converted .md is gitignored (re-derivable). Graphify honors .gitignore,
    # so without this flag extract sees an empty corpus.
    args = [config.GRAPHIFY_BIN, "extract", corpus_arg,
            "--no-gitignore",
            "--mode", config.GRAPHIFY_MODE, "--backend", "claude",
            "--model", config.GRAPHIFY_MODEL]
    if force:
        args.insert(3, "--force")
    _run(args, "graphify extract")

    if not (staged / "graph.json").exists():
        raise RuntimeError(f"extract produced no graph at {staged} — live graph left untouched")

    # Promote: the previous graph is only replaced once a good one exists.
    if config.GRAPH_DIR.exists():
        shutil.rmtree(config.GRAPH_DIR)
    shutil.move(str(staged), str(config.GRAPH_DIR))
    print(f"Promoted new graph -> {config.GRAPH_DIR}")


# --------------------------------------------------------------------------- #
# Node dedup
# --------------------------------------------------------------------------- #

def _norm_key(node: dict) -> str:
    raw = (node.get("norm_label") or node.get("label") or node["id"])
    return " ".join(str(raw).lower().split())


def dedup(graph_path: Optional[Path] = None) -> dict:
    """Merge nodes that denote the same entity extracted from different PDFs.

    Extraction emits one node per (entity, source document), so a law cited by
    ten circulars becomes ten near-identical notes and a reader cannot tell which
    is authoritative.  Merging on normalised label keeps a single canonical node
    carrying every source.
    """
    is_live = graph_path is None or graph_path == config.GRAPH_JSON
    graph_path = graph_path or config.GRAPH_JSON
    g = read_json(graph_path)
    if not g:
        raise SystemExit(f"Missing {graph_path}")
    nodes: List[dict] = g["nodes"]
    links: List[dict] = g.get("links") or g.get("edges") or []

    groups: Dict[str, List[dict]] = defaultdict(list)
    for n in nodes:
        groups[_norm_key(n)].append(n)

    degree: Dict[str, int] = defaultdict(int)
    for l in links:
        degree[l["source"]] += 1
        degree[l["target"]] += 1

    remap: Dict[str, str] = {}
    merged: List[dict] = []
    clusters_merged = 0
    for key, members in groups.items():
        if len(members) == 1:
            merged.append(members[0])
            remap[members[0]["id"]] = members[0]["id"]
            continue
        clusters_merged += 1
        # Canonical = best connected, tie-broken by the label without a _N suffix.
        canon = sorted(
            members,
            key=lambda n: (-degree[n["id"]], len(str(n.get("label") or "")), str(n["id"])),
        )[0]
        sources, urls, locations = [], [], []
        for m in members:
            remap[m["id"]] = canon["id"]
            for field, bucket in (("source_file", sources), ("source_url", urls),
                                  ("source_location", locations)):
                v = m.get(field)
                if v and v not in bucket:
                    bucket.append(v)
        node = dict(canon)
        node["source_files"] = sources
        node["source_urls"] = urls
        node["source_locations"] = [x for x in locations if x]
        node["merged_from"] = [m["id"] for m in members if m["id"] != canon["id"]]
        merged.append(node)

    # Rewrite edges onto canonical ids, dropping self-loops and parallel edges.
    seen: Dict[Tuple[str, str, str], dict] = {}
    conf_rank = {"EXTRACTED": 3, "INFERRED": 2, "AMBIGUOUS": 1}
    dropped_self = 0
    for l in links:
        s, t = remap.get(l["source"], l["source"]), remap.get(l["target"], l["target"])
        if s == t:
            dropped_self += 1
            continue
        a, b = sorted([s, t])
        key = (a, b, l.get("relation", ""))
        new = dict(l, source=s, target=t)
        cur = seen.get(key)
        if cur is None or conf_rank.get(new.get("confidence"), 0) > conf_rank.get(cur.get("confidence"), 0):
            seen[key] = new
    new_links = list(seen.values())

    g["nodes"] = merged
    if "links" in g:
        g["links"] = new_links
    else:
        g["edges"] = new_links

    stats = {
        "nodes_before": len(nodes), "nodes_after": len(merged),
        "edges_before": len(links), "edges_after": len(new_links),
        "clusters_merged": clusters_merged,
        "self_loops_dropped": dropped_self,
        "parallel_edges_dropped": len(links) - dropped_self - len(new_links),
    }
    write_json(graph_path, g)
    if is_live:   # only report on the project's own graph, never a caller's copy
        write_json(config.GRAPH_REPORTS / "dedup.json",
                   {"generated": datetime.now(timezone.utc).isoformat(), **stats})
    print(f"Dedup: {stats['nodes_before']} -> {stats['nodes_after']} nodes "
          f"({clusters_merged} clusters merged), "
          f"{stats['edges_before']} -> {stats['edges_after']} edges")
    return stats


# --------------------------------------------------------------------------- #
# Cluster / label / export
# --------------------------------------------------------------------------- #

def cluster_and_label() -> None:
    """Rerun clustering + community labeling on the promoted graph.

    Confirmed empirically 2026-09-19 (installed graphify 0.9.23), because the
    real CLI's behaviour here doesn't match what the pre-reorg code assumed:
    `cluster-only <path>` and `label <path>` take a positional <path> whose
    `<path>/graphify-out/graph.json` is where they *write* their result -
    always, regardless of `--graph`. `--graph <file>` only selects which
    graph.json to *read* as input; it does not redirect the output. Passing
    GRAPH_DIR as <path> and GRAPH_JSON as --graph (the natural-looking call,
    since graph.py's own extract() already promoted GRAPH_JSON out of any
    graphify-out/ folder) therefore left GRAPH_JSON untouched and wrote a
    *new* nested GRAPH_DIR/graphify-out/graph.json instead - one level
    deeper than every other stage (dedup, enrich, audit) expects to find it.

    So: chain both calls through that nested working copy (label reads the
    graph cluster-only just wrote, via --graph, so it sees real communities
    rather than re-reading the stale top-level file), then copy the result
    back up to GRAPH_JSON/GRAPH_REPORT.md/graph.html and discard the nested
    folder - keeping GRAPH_JSON the one canonical path everything else reads.
    """
    common = ["--backend", "claude", "--model", config.GRAPHIFY_MODEL]
    staged = config.GRAPH_DIR / "graphify-out"
    if staged.exists():
        shutil.rmtree(staged)

    graph_dir_arg = config.GRAPH_DIR.relative_to(config.ROOT).as_posix()
    graph_json_arg = config.GRAPH_JSON.relative_to(config.ROOT).as_posix()
    _run([config.GRAPHIFY_BIN, "cluster-only", graph_dir_arg, "--graph", graph_json_arg] + common,
         "graphify cluster-only")

    staged_graph = staged / "graph.json"
    if not staged_graph.exists():
        raise RuntimeError(f"graphify cluster-only produced no graph at {staged_graph}")
    staged_graph_arg = staged_graph.relative_to(config.ROOT).as_posix()
    _run([config.GRAPHIFY_BIN, "label", graph_dir_arg, "--graph", staged_graph_arg] + common,
         "graphify label")

    shutil.copy2(staged_graph, config.GRAPH_JSON)
    for extra in ("GRAPH_REPORT.md", "graph.html", ".graphify_analysis.json"):
        src = staged / extra
        if src.exists():
            shutil.copy2(src, config.GRAPH_DIR / extra)
    shutil.rmtree(staged)


def export_vault() -> None:
    """Export the Obsidian vault from GRAPH_JSON.

    `export obsidian` does honour `--graph` for its *input* (unlike
    cluster-only/label above, confirmed empirically the same day) - it has
    no working-folder output of its own to redirect, so there's no
    equivalent mismatch to work around here.
    """
    config.VAULT_DIR.mkdir(parents=True, exist_ok=True)
    graph_json_arg = config.GRAPH_JSON.relative_to(config.ROOT).as_posix()
    _run([config.GRAPHIFY_BIN, "export", "obsidian", "--graph", graph_json_arg,
          "--dir", str(config.VAULT_DIR)],
         "graphify export obsidian")


def namespace_vault() -> int:
    """Prefix every exported note's filename and rewrite links to match.

    graphify's own `export obsidian` has no subfolder/prefix option (confirmed
    against its actual invocations in this repo — the only flag it takes is
    `--dir`) and writes flat, unprefixed filenames keyed by label. Obsidian
    resolves [[wikilinks]] by note name across the *entire* vault regardless of
    folder, so once CBUAE's export lands in a folder next to SAMA's, an
    unprefixed generic note ("Board of Directors.md" exists in both regulators'
    real vocabulary) could silently cross-link between the two graphs. This is
    the one place graphify's own output has to be touched after the fact: it
    renames every note graphify just wrote to carry config.NOTE_PREFIX, and
    rewrites every [[Target]]/[[Target|Alias]] reference so the link target
    matches the new filename while the *display* text stays the original,
    readable label.

    A no-op (returns 0 immediately) when config.NOTE_PREFIX is empty. Both
    sources currently set a prefix, so this always runs in practice; the
    early-out just keeps the function safe if a future source opts out.
    """
    import re

    from .common import strip_forbidden

    prefix = config.NOTE_PREFIX
    if not prefix:
        return 0

    files = [p for p in config.VAULT_DIR.glob("*.md") if not p.stem.startswith(prefix)]
    if not files:
        return 0

    old_stems = {p.stem for p in files}
    renamed = 0
    for p in files:
        p.rename(p.with_name(f"{prefix}{p.name}"))
        renamed += 1

    link_re = re.compile(r"\[\[([^\]\|]+)(\|[^\]]+)?\]\]")

    def repl(m: "re.Match") -> str:
        target, alias_group = m.group(1).strip(), m.group(2)
        stripped = strip_forbidden(target)
        if stripped not in old_stems:
            return m.group(0)   # not a link into this vault (or already handled)
        display = alias_group[1:] if alias_group else target
        return f"[[{prefix}{stripped}|{display}]]"

    rewritten_files = rewritten_links = 0
    for md in config.VAULT_DIR.glob(f"{prefix}*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        new_text, n = link_re.subn(repl, text)
        if n:
            md.write_text(new_text, encoding="utf-8")
            rewritten_files += 1
            rewritten_links += n

    print(f"Namespaced vault: renamed {renamed} note(s) with prefix {prefix!r}, "
          f"rewrote {rewritten_links} link(s) across {rewritten_files} file(s)")
    return renamed


def fix_wikilinks(dry_run: bool = False) -> int:
    """Repair links written with characters the exported filenames strip.

    An export drops filesystem-forbidden characters from note filenames, but the
    links inside notes keep the original label, so `[[AML/CTF Guide]]` fails to
    resolve and - for '/' - renders as a phantom node.  Rewriting to the alias
    form fixes the target while keeping the readable display text.
    """
    from .common import strip_forbidden

    import re
    link_re = re.compile(r"\[\[([^\]\|]+)(\|[^\]]+)?\]\]")
    existing = {p.stem for p in config.VAULT_DIR.glob("*.md")}
    total = files = 0

    for md in config.VAULT_DIR.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        changed = 0

        def repl(m):
            nonlocal changed
            target, alias = m.group(1).strip(), m.group(2)
            if target in existing:
                return m.group(0)
            stripped = strip_forbidden(target)
            if stripped != target and stripped in existing:
                changed += 1
                return f"[[{stripped}{alias}]]" if alias else f"[[{stripped}|{target}]]"
            return m.group(0)

        new = link_re.sub(repl, text)
        if changed:
            total += changed
            files += 1
            if not dry_run:
                md.write_text(new, encoding="utf-8")

    print(f"{'Would rewrite' if dry_run else 'Rewrote'} {total} wikilink(s) across {files} file(s)")
    return total


def run(skip_extract: bool = False, no_dedup: bool = False, force: bool = True) -> int:
    config.ensure_dirs()
    if not list(config.CORPUS_MD.glob("*.md")):
        print(f"{config.CORPUS_MD} is empty — run the convert stage first.")
        return 1

    check_prereqs()
    snapshot()
    if not skip_extract:
        extract(force=force)
    if config.DEDUP_NODES and not no_dedup:
        dedup()
    cluster_and_label()
    export_vault()
    namespace_vault()     # prefixes + relinks this source's notes (both sources)
    fix_wikilinks()

    g = read_json(config.GRAPH_JSON, {})
    print(f"\nGraph: {len(g.get('nodes', []))} nodes, "
          f"{len(g.get('links') or g.get('edges') or [])} edges")
    print(f"Vault: {len(list(config.VAULT_DIR.glob('*.md')))} notes -> {config.VAULT_DIR}")
    return 0
