"""Generate Obsidian Graph View color groups for both sources' communities.

Not a `run.py` pipeline stage: the stage model in run.py is per-source
(`--source sama|cbuae`), but this reads *both* sources' `graph.json` at once
and writes into the one shared vault-level `.obsidian/graph.json`, so it is
invoked directly:

    cd codebase && python -m sama.colorize

Safe to re-run any time either source's communities are relabeled (a
`cluster-only`/`label` rerun) — it always rebuilds the full colorGroups list
from the current graph.json files rather than editing the previous one.

Obsidian's `.obsidian/graph.json` `colorGroups` is a flat, ordered list of
`{"query": ..., "color": {"a": 1, "rgb": <packed int>}}` entries, and a node
that matches more than one query gets the color of the *first* match in the
list (confirmed against Obsidian's own graph-view behaviour and community
documentation, 2026-09-19 — not just inferred from this repo's old, single-
source v1 vault, which never exercised the overlap case). So:

    [ all per-community groups ]  (mutually exclusive - order among these
                                    does not matter, every node has exactly
                                    one #community/<slug> tag)
    [ SAMA fallback, CBUAE fallback ]   (broad path: queries, last, so they
                                          only ever catch a note with no
                                          community tag at all - each
                                          source's own routing-index note)

Each source gets its own hue family (green for SAMA/KSA, blue for CBUAE/UAE)
so the graph reads as "source" at the hue level and "sub-cluster" at the
shade level within it, cycling shades by golden-angle hue/lightness offsets
within the family's band so adjacent communities in the (arbitrary, ID-order)
list don't land on near-identical shades.
"""

from __future__ import annotations

import colorsys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

from . import config
from .common import read_json

# (hue_start, hue_end) in degrees, and a base (lightness, saturation) for the
# two source-wide fallback groups (path:SAMA / path:CBUAE), which use the
# midpoint of the family so they read as "the plain version of this family's
# color" next to their own community shades.
_FAMILIES: Dict[str, Tuple[float, float]] = {
    "sama": (95.0, 165.0),     # yellow-green -> teal-green (KSA)
    "cbuae": (195.0, 265.0),   # cyan-blue -> indigo-blue (UAE)
}
_GOLDEN = 0.6180339887498949


def _pack_rgb(r: int, g: int, b: int) -> int:
    return (r << 16) | (g << 8) | b


def _shade(hue_deg: float, lightness: float, saturation: float) -> int:
    r, g, b = colorsys.hls_to_rgb((hue_deg % 360) / 360.0, lightness, saturation)
    return _pack_rgb(round(r * 255), round(g * 255), round(b * 255))


def _community_names(source: str) -> List[str]:
    graph_json = config.ROOT / "graph-build" / source / "graph.json"
    graph = read_json(graph_json)
    names = {n["community_name"] for n in graph.get("nodes", []) if n.get("community_name")}
    return sorted(names)


def _slug(name: str) -> str:
    # Must match enrich.py's render() exactly (both the per-node tag and the
    # community stub note's own tag) or the query below won't hit anything.
    return re.sub(r"\s+", "-", str(name).lower())


def _community_groups(source: str, vault_subfolder: str) -> List[dict]:
    hue_start, hue_end = _FAMILIES[source]
    hue_span = hue_end - hue_start
    names = _community_names(source)
    groups = []
    for i, name in enumerate(names):
        hue = hue_start + (i * _GOLDEN * hue_span) % hue_span
        lightness = 0.38 + 0.22 * ((i * _GOLDEN) % 1.0)
        color = _shade(hue, lightness, 0.55)
        groups.append({
            "query": f"tag:#community/{_slug(name)}",
            "color": {"a": 1, "rgb": color},
        })
    return groups


def _fallback_group(source: str, vault_subfolder: str) -> dict:
    hue_start, hue_end = _FAMILIES[source]
    color = _shade((hue_start + hue_end) / 2, 0.45, 0.55)
    return {
        "query": f'path:"{vault_subfolder}"',
        "color": {"a": 1, "rgb": color},
    }


def build_color_groups() -> List[dict]:
    groups: List[dict] = []
    groups += _community_groups("sama", "SAMA")
    groups += _community_groups("cbuae", "CBUAE")
    groups.append(_fallback_group("sama", "SAMA"))
    groups.append(_fallback_group("cbuae", "CBUAE"))
    return groups


def write_graph_json() -> Path:
    config.VAULT_ROOT.mkdir(parents=True, exist_ok=True)
    path = config.VAULT_ROOT / ".obsidian" / "graph.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        current = json.loads(path.read_text(encoding="utf-8"))
    else:
        # Obsidian's own defaults for the keys it would otherwise seed itself.
        current = {
            "collapse-filter": True, "search": "", "showTags": False,
            "showAttachments": False, "hideUnresolved": False, "showOrphans": True,
            "collapse-display": True, "showArrow": False, "textFadeMultiplier": 0,
            "nodeSizeMultiplier": 1, "lineSizeMultiplier": 1, "collapse-forces": True,
            "centerStrength": 0.5, "repelStrength": 10, "linkStrength": 1,
            "linkDistance": 250, "scale": 1, "close": False,
        }
    current["colorGroups"] = build_color_groups()
    current["collapse-color-groups"] = True
    path.write_text(json.dumps(current, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def main() -> int:
    path = write_graph_json()
    groups = json.loads(path.read_text(encoding="utf-8"))["colorGroups"]
    print(f"Wrote {len(groups)} color group(s) -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
