"""Stage 1 (CBUAE) - crawl rulebook.centralbank.ae and download in-force PDFs.

Mirrors sama/crawl.py's shape (crawl -> plan -> fetch -> write_report -> run) so
run.py can dispatch to either module identically, and reuses plan()/fetch()/
write_report() from sama.crawl unchanged - those are already source-agnostic
(everything they touch is config.PDF_DIR, config.FETCH_*, config.CRAWL_REPORTS,
...). Only the site walk itself is CBUAE-specific.

Live-verified against rulebook.centralbank.ae on 2026-09-19 (see the inline
notes below for what was actually confirmed versus inferred).

Run end-to-end on 2026-09-19: the first real `--manifest-only` pass returned 0
PDFs across only the 4 seed pages, with no exceptions and no failed_pages
entries - i.e. every `page.goto` "succeeded". Root cause: this site's WAF
403s any request whose User-Agent contains `HeadlessChrome` (Playwright's
default headless UA), while the identical URL returns 200 to a plain HTTP
client with an ordinary Chrome UA. `page.goto` doesn't raise on a 403, so the
crawler silently walked 4 near-empty error pages and returned successfully.
Fixed by `crawl.new_page()`, which opens every page (both sources) through a
browser context whose User-Agent has "Headless" stripped - see that
function's docstring. After the fix this crawler found the real sidebar tree
and PDF links.

Site structure (confirmed live):
  - Built on Drupal's Book module. Each top-level "book" (All Licensed
    Financial Institutions, Banking, Insurance, Other Regulated Entities) has
    its own <nav class="book-block-menu"> in the left sidebar
    (#block-rulebook-booknavigation), each wrapping one <ul class="menu">.
    This is real nested <ul>/<li> markup, not the pixel-geometry layout SAMA's
    site requires - so children are read directly from the DOM tree instead of
    bounding-rect math.
  - A book's OWN root page does not list itself as an <li> inside its own
    block (confirmed: on /en/rulebook/all-licensed-financial-institutions,
    that book's nav block's top-level <li>s are already its depth-1 children -
    "Laws", "AML/CFT", ... - not a self-referencing entry). Whichever block
    currently has the most total <li> nodes is the one Drupal has expanded for
    the active trail; when the current path isn't found as an <li> inside it,
    we are on that book's own unlisted root, and its top-level <li>s are the
    children.
  - The PDF "Download" link is per REGULATION, not per article: confirmed live
    that a law's own page and every one of its Article sub-pages link to the
    exact same PDF (CBUAE_EN_4588_VER1.pdf, for both the "Registered Hawala
    Providers Regulation" page and its "Article 1: Definitions" child). So
    dedup-by-URL (already how sama.crawl._merge works) is sufficient; there is
    no need for special-case logic to stop descending at the regulation level.
  - Filenames follow the same convention as SAMA: CBUAE_EN_<id>_VER<n>.pdf
    under a path containing "file_store" (.../en_net_file_store/...).
  - "Status: In-Force" uses the identical wording SAMA's site uses. The
    document-number line does not say "No:" the way SAMA's does; instead it's
    a short code right under the H1, e.g. "DFL 6/2025 Effective from
    16/9/2025" or "C 24/2019 Effective from 14/6/2019".
  - Arabic mirror pages exist (/ar/rulebook/<arabic-slug>) but the slug is not
    a simple /en/->/ar/ substitution, so the Arabic root for each book is
    discovered by following that book's own "عربي" toggle link rather than
    guessed.
"""

from __future__ import annotations

import re
import time
import urllib.parse
from collections import deque
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

from . import config
from .common import abs_url, is_in_force, norm_slug, stem_for, write_json
from .crawl import PdfRecord, _file_id, _merge, fetch, new_page, plan, write_report

# Extracts page text, PDF download link(s) and the sidebar tree context in one
# evaluation. currentPath is passed in (location.pathname alone, since a query
# string would break the href comparison against link hrefs that never carry
# one).
_TREE_JS = """(currentPath) => {
    const contentRoot = document.querySelector('main, article, #block-rulebook-content, .region-content') || document.body;
    const text = (contentRoot.innerText || '').slice(0, 12000);

    const pdfs = [];
    document.querySelectorAll('a[href]').forEach(el => {
        const h = el.getAttribute('href') || '';
        if (h.includes('file_store') && h.includes('.pdf')) {
            pdfs.push({ href: h, text: (el.innerText || '').trim().slice(0, 120) });
        }
    });

    const sidebar = document.getElementById('block-rulebook-booknavigation')
                  || document.getElementById('sidebar_first') || document.body;
    const navBlocks = Array.from(sidebar.querySelectorAll('nav.book-block-menu, .book-navigation'));

    function topLis(nb) {
        const ul = nb.querySelector(':scope > ul.menu') || nb.querySelector('ul.menu');
        return ul ? Array.from(ul.querySelectorAll(':scope > li')) : [];
    }
    function linkOf(li) {
        const a = li.querySelector(':scope > a');
        if (!a) return null;
        return { href: (a.getAttribute('href') || '').split('?')[0], title: (a.innerText || '').trim().replace(/\\s+/g, ' ') };
    }
    function findLiForPath(lis, path) {
        for (const li of lis) {
            const a = li.querySelector(':scope > a');
            if (a && (a.getAttribute('href') || '').split('?')[0] === path) return li;
            const nestedUl = li.querySelector(':scope > ul');
            if (nestedUl) {
                const hit = findLiForPath(Array.from(nestedUl.querySelectorAll(':scope > li')), path);
                if (hit) return hit;
            }
        }
        return null;
    }

    // The block with the most <li> nodes is the one Drupal has expanded for
    // the current page's active trail (a collapsed sibling book has exactly
    // one <li> - its own root link - and nothing nested under it).
    let bestBlock = null, bestCount = -1;
    for (const nb of navBlocks) {
        const ul = nb.querySelector('ul.menu');
        const count = ul ? ul.querySelectorAll('li').length : 0;
        if (count > bestCount) { bestCount = count; bestBlock = nb; }
    }

    const extraRoots = [];
    navBlocks.forEach(nb => topLis(nb).forEach(li => { const lk = linkOf(li); if (lk) extraRoots.push(lk); }));

    let children = [];
    if (bestBlock) {
        const lis = topLis(bestBlock);
        const hit = findLiForPath(lis, currentPath);
        if (hit) {
            const nestedUl = hit.querySelector(':scope > ul');
            children = nestedUl ? Array.from(nestedUl.querySelectorAll(':scope > li')).map(linkOf).filter(Boolean) : [];
        } else {
            // Current page is this book's own (unlisted) root.
            children = lis.map(linkOf).filter(Boolean);
        }
    }

    const arA = document.querySelector('a[href^="/ar/"]');
    return { text, pdfs, children, extraRoots, arHref: arA ? arA.getAttribute('href') : null };
}"""

# CBUAE's document-number line has no "No:" label the way SAMA's does; it's a
# short code immediately followed by "Effective from", e.g.
# "DFL 6/2025 Effective from 16/9/2025" or "C 24/2019 Effective from 14/6/2019".
DOC_NO_RE = re.compile(r"^\s*([A-Za-z]{1,6}\s*\d+[/-]\d{2,4})\s+Effective from", re.M)
STATUS_RE = re.compile(r"Status:\s*([^\n|]+)", re.I)


def _should_skip(href: str, lang: str) -> bool:
    slug = norm_slug(href)
    prefix = f"/{lang}/"
    if not slug.startswith(prefix):
        return True
    if slug in config.SKIP_HREFS:
        return True
    return "/entiresection/" in slug or "/node/" in slug  # cross-reference popups, not tree nodes


def _records_from_page(data: dict, slug: str, title: str) -> List[PdfRecord]:
    text = data.get("text", "")
    m = STATUS_RE.search(text)
    status = m.group(1).strip()[:80] if m else None
    m2 = DOC_NO_RE.search(text)
    doc_no = m2.group(1).strip()[:40] if m2 else None
    in_force = is_in_force(status)

    out: List[PdfRecord] = []
    seen: Set[str] = set()
    for item in data.get("pdfs", []):
        url = abs_url(item.get("href", ""))
        if "file_store" not in url and config.BASE_URL not in url:
            continue
        if url in seen:
            continue
        seen.add(url)
        stem = stem_for(url) if "CBUAE_" in url.upper() else None
        if stem and not stem.startswith("CBUAE_"):
            stem = None
        basename = urllib.parse.unquote(url.split("/")[-1].split("?")[0])
        out.append(PdfRecord(
            file_id=_file_id(url, stem), stem=stem, pdf_url=url, filename=basename,
            link_label=item.get("text", ""), source_slug=slug, source_title=title,
            tree_path=title, source_kind="tree", document_no=doc_no,
            status=status, in_force=in_force,
        ))
    return out


def _walk_book_tree(page, seeds: Dict[str, str], lang: str,
                     tree: Dict[str, dict], by_id: Dict[str, PdfRecord],
                     stats: dict, failed_pages: List[dict], max_pages: int,
                     expanded: Set[str]) -> List[Tuple[str, str]]:
    """BFS one language's set of root books. Returns [(href, title)] for any
    root book discovered along the way that wasn't in `seeds` (defensive - a
    book added to the site later needs no code change to be picked up).

    `expanded` is owned by the caller and shared across every call for this
    language, not created fresh here. Confirmed empirically 2026-09-19 on a
    live CBUAE crawl: whenever a page found a new `extraRoots` entry late in
    a ~3000-page walk, `crawl()`'s outer `while pending_en/ar:` loop made one
    more `_walk_book_tree` call for just that new root - but a local
    `expanded = set()` on that call meant every child already sitting in the
    shared `tree` dict from the *first* call looked "not yet expanded *this
    call*" and got requeued, so the walk re-visited the entire already-known
    tree via `page.goto` a second time (dedup by `file_id` in `by_id` kept the
    PDF set correct, so this was silent - the symptom was only a full replay
    of the visited/queued counters with the pdf count flat throughout, easy
    to mistake for a hung crawl). One redundant late root can cost an entire
    extra pass; several can compound. Threading one `Set` through every call
    for a language makes "already expanded" mean what its name says: expanded
    at any point in this run, not just in this call.
    """
    discovered_roots: List[Tuple[str, str]] = []
    known_roots = set(seeds.keys())

    for slug, title in seeds.items():
        tree.setdefault(slug, {"slug": slug, "title": title, "depth": 0,
                               "parent": None, "children": [], "lang": lang})
    queue: deque = deque(seeds.keys())

    while queue:
        slug = queue.popleft()
        if slug in expanded:
            continue
        if max_pages and len(expanded) >= max_pages:
            print(f"  [{lang}] [cap] stopping at --max-pages {max_pages}", flush=True)
            break
        expanded.add(slug)
        node = tree[slug]

        try:
            page.goto(abs_url(slug), wait_until="domcontentloaded")
            page.wait_for_timeout(600)
            path_only = urllib.parse.urlsplit(page.url).path
            data = page.evaluate(_TREE_JS, path_only)
        except Exception as exc:
            print(f"  [{lang}] ERR {slug}: {exc}", flush=True)
            failed_pages.append({"slug": slug, "kind": "tree", "lang": lang,
                                 "title": node["title"], "error": str(exc)[:200]})
            continue

        stats["pages_visited"] += 1
        found = _records_from_page(data, slug, node["title"])
        if found:
            stats["pages_with_pdf"] += 1
            _merge(by_id, found)

        for lk in data.get("extraRoots", []):
            rs = norm_slug(lk["href"])
            if rs not in known_roots and rs not in tree and not _should_skip(rs, lang):
                known_roots.add(rs)
                discovered_roots.append((rs, lk["title"]))

        for lk in data.get("children", []):
            ch = norm_slug(lk["href"])
            if _should_skip(ch, lang):
                continue
            if ch not in tree:
                tree[ch] = {"slug": ch, "title": lk["title"], "depth": node["depth"] + 1,
                           "parent": slug, "children": [], "lang": lang}
                node["children"].append(ch)
                queue.append(ch)
            elif ch not in expanded:
                queue.append(ch)

        if len(expanded) % 25 == 0:
            print(f"  [{lang}] visited {len(expanded)} | queued {len(queue)} | pdfs {len(by_id)}", flush=True)

    return discovered_roots


def crawl(max_pages: int = 0, headless: bool = True) -> Tuple[List[PdfRecord], dict]:
    from playwright.sync_api import sync_playwright

    tree: Dict[str, dict] = {}
    by_id: Dict[str, PdfRecord] = {}
    failed_pages: List[dict] = []
    stats: dict = {"pages_visited": 0, "pages_with_pdf": 0, "circular_indexes": 0,
                   "circular_pages": 0, "skipped_not_in_force": 0,
                   "failed_pages": failed_pages}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = new_page(browser, viewport={"width": 1600, "height": 1000})
        page.set_default_timeout(30000)

        # English pass. Seeded from the live-confirmed root list; any sibling
        # book not in that seed (site added a new one) is picked up via
        # extraRoots and queued the same way.
        en_seeds = dict(config.CBUAE_ROOT_BOOKS)
        pending_en = list(en_seeds.items())
        ar_seed_hrefs: Dict[str, str] = {}   # english root slug -> arHref, for seeding the Arabic pass
        en_expanded: Set[str] = set()
        while pending_en:
            batch = dict(pending_en)
            pending_en = []
            more = _walk_book_tree(page, batch, "en", tree, by_id, stats, failed_pages,
                                   max_pages, en_expanded)
            pending_en.extend(more)

        if "ar" in config.CRAWL_LANGS:
            # Arabic roots aren't guessable from the English slug, so visit
            # each known English root once more and follow its "عربي" toggle.
            ar_seeds: Dict[str, str] = {}
            for en_slug in config.CBUAE_ROOT_BOOKS:
                try:
                    page.goto(abs_url(en_slug), wait_until="domcontentloaded")
                    page.wait_for_timeout(600)
                    ar_href = page.evaluate("() => { const a = document.querySelector('a[href^=\"/ar/\"]'); return a ? a.getAttribute('href') : null; }")
                except Exception as exc:
                    print(f"  ERR finding Arabic root for {en_slug}: {exc}", flush=True)
                    failed_pages.append({"slug": en_slug, "kind": "ar-root-lookup",
                                         "title": "", "error": str(exc)[:200]})
                    continue
                if ar_href:
                    ar_slug = norm_slug(ar_href)
                    ar_seeds[ar_slug] = config.CBUAE_ROOT_BOOKS[en_slug] + " (AR)"

            pending_ar = list(ar_seeds.items())
            ar_expanded: Set[str] = set()
            while pending_ar:
                batch = dict(pending_ar)
                pending_ar = []
                more = _walk_book_tree(page, batch, "ar", tree, by_id, stats, failed_pages,
                                       max_pages, ar_expanded)
                pending_ar.extend(more)

        browser.close()

    records = list(by_id.values())
    if config.REQUIRE_IN_FORCE:
        keep = [r for r in records if r.in_force]
        stats["skipped_not_in_force"] = len(records) - len(keep)
        records = keep

    write_json(config.CRAWL_REPORTS / "tree.json", {
        "generated": datetime.now(timezone.utc).isoformat(),
        "entry": config.ENTRY_PAGE, "nodes": len(tree), "tree": tree,
    })
    return records, stats


def run(max_pages: int = 0, headless: bool = True, manifest_only: bool = False) -> int:
    config.ensure_dirs()
    t0 = time.time()
    records, stats = crawl(max_pages=max_pages, headless=headless)
    records = plan(records)
    if not manifest_only:
        records = fetch(records)
    write_report(records, stats, time.time() - t0)
    n_fail = sum(1 for r in records if r.action == "failed")
    n_pages = len(stats.get("failed_pages", []))
    print(f"\nCBUAE crawl done: {len(records)} PDFs | failed={n_fail} | "
          f"pages unreachable={n_pages} | {time.time() - t0:.1f}s")
    print(f"Report: {config.CRAWL_REPORTS / 'crawl_report.md'}")
    return 1 if (n_fail or n_pages) else 0
