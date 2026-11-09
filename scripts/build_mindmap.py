#!/usr/bin/env python3
"""Draw the student's thoughts mind map (sessions/mindmap.json) for the chat and as a page.

Usage: build_mindmap.py sessions/mindmap.json [--root DIR] [--chat]
Writes <name>.html next to the .json (a printable page) and, with --chat, <name>.chat.html:
an SVG for the visual tool's show_widget - pass its content unchanged. Prints one line of JSON.

Input format:
{
  "centre": "NBFI risk: banks or directly?",        the thesis question or topic (2 lines max)
  "updated": "2026-11-09",                          (optional, default today)
  "branches": [                                     2-6 branches, in display order
    {"title": "Angles",                             short: 18 characters at most
     "ideas": [                                     1-6 per branch
       {"id": "a1",                                 unique, stable (used for "discuss a1", "move a1")
        "text": "Regulate activity, not entities",  58 characters at most (two lines in the map)
        "by": "student",                            student | otto
        "wild": false,                              (optional) unusual idea
        "sources": ["fsb-2023-nbfi"],               (optional) library ids that support it
        "needed": "FSB report on NBFI leverage",    (optional) the kind of source still needed
        "status": "open",                           open | discussed | outlined | dropped
        "where": "3.2",                             (optional) outline section, when outlined
        "note": "why the student likes it"}         (optional, page only)
     ]}
  ]
}

Library tags: an idea with at least one source in references/INDEX.md gets a green dot; an idea
with "needed" (or a source that isn't in the library) gets an amber dot. Sources not in the
library are never shown as backed and are reported in "unknown_sources".
Dropped ideas are left out of the chat map and listed separately on the page.
Problems are reported in "checks" - prompts for Otto to fix the record and re-run.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_discussion import library_ids  # noqa: E402  (same INDEX.md reading as Discuss)

MAX_BRANCHES, MAX_IDEAS = 6, 6
MAX_TITLE, LINE, MAX_TEXT = 18, 29, 58
STATUSES = {"open", "discussed", "outlined", "dropped"}


def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def wrap(text: str, width: int = LINE) -> list[str]:
    """Split into at most two lines of ~width characters, on word boundaries."""
    words, lines, cur = (text or "").split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    if len(lines) > 2:
        lines = [lines[0], " ".join(lines[1:])]
        if len(lines[1]) > width:
            lines[1] = lines[1][: width - 1].rstrip() + "…"
    return lines or [""]


def check(data: dict, ids: set[str]) -> tuple[list[str], list[str]]:
    checks, unknown, seen = [], [], set()
    branches = data.get("branches") or []
    if not (data.get("centre") or "").strip():
        checks.append("no centre (the thesis question or topic)")
    if not 2 <= len(branches) <= MAX_BRANCHES:
        checks.append(f"{len(branches)} branches - use 2-{MAX_BRANCHES}")
    for b in branches:
        t = b.get("title") or "?"
        if len(t) > MAX_TITLE:
            checks.append(f"branch '{t}': title longer than {MAX_TITLE} characters")
        live = [i for i in b.get("ideas") or [] if i.get("status") != "dropped"]
        if not live:
            checks.append(f"branch '{t}': no ideas")
        if len(live) > MAX_IDEAS:
            checks.append(f"branch '{t}': {len(live)} ideas - {MAX_IDEAS} at most; split the branch or drop some")
        for i in b.get("ideas") or []:
            iid = i.get("id") or "?"
            if iid in seen:
                checks.append(f"idea id '{iid}' is used twice")
            seen.add(iid)
            if len(i.get("text") or "") > MAX_TEXT:
                checks.append(f"idea {iid}: longer than {MAX_TEXT} characters - shorten it (details go in 'note')")
            if not (i.get("text") or "").strip():
                checks.append(f"idea {iid}: no text")
            if i.get("by") not in ("student", "otto"):
                checks.append(f"idea {iid}: 'by' must be student or otto")
            if i.get("status", "open") not in STATUSES:
                checks.append(f"idea {iid}: unknown status '{i.get('status')}'")
            unknown += [s for s in i.get("sources") or [] if s not in ids]
    return checks, sorted(set(unknown))


def tag(i: dict, ids: set[str]) -> str:
    if any(s in ids for s in i.get("sources") or []):
        return "ok"
    if i.get("needed") or i.get("sources"):
        return "nd"
    return ""


# ------------------------------------------------------------------ chat SVG
def chat_svg(data: dict, ids: set[str]) -> str:
    branches = [dict(b, ideas=[i for i in b.get("ideas") or [] if i.get("status") != "dropped"])
                for b in data.get("branches") or []]
    branches = [b for b in branches if b["ideas"]]
    y, rows = 30, []          # rows: (branch, [(idea, top, height, lines)])
    for b in branches:
        items = []
        for i in b["ideas"]:
            lines = wrap(("* " if i.get("wild") else "") + i.get("text", ""))
            h = 26 if len(lines) == 1 else 40
            items.append((i, y, h, lines))
            y += h + 8
        rows.append((b, items))
        y += 14
    bottom = y - 22
    mid = (30 + bottom) / 2
    centre = wrap(data.get("centre") or "", 18)
    out = []
    lines_svg, nodes = [], []
    branch_c = []
    for b, items in rows:
        c = (items[0][1] + items[-1][1] + items[-1][2]) / 2
        branch_c.append(c)
        for i, top, h, _ in items:
            lc = top + h / 2
            lines_svg.append(f'<path d="M365 {c:.0f} C383 {c:.0f} 382 {lc:.0f} 400 {lc:.0f}"/>')
    for c in branch_c:
        lines_svg.append(f'<path d="M180 {mid:.0f} C198 {mid:.0f} 197 {c:.0f} 215 {c:.0f}"/>')
    out.append('<g fill="none" stroke="#888780" stroke-width="1" opacity="0.6">' + "".join(lines_svg) + "</g>")
    ch = 56 if len(centre) > 1 else 40
    out.append(f'<g class="c-purple"><rect x="30" y="{mid - ch / 2:.0f}" width="150" height="{ch}" rx="8" stroke-width="0.5"/>')
    if len(centre) > 1:
        out.append(f'<text class="th" x="105" y="{mid - 10:.0f}" text-anchor="middle" dominant-baseline="central">{esc(centre[0])}</text>'
                   f'<text class="th" x="105" y="{mid + 10:.0f}" text-anchor="middle" dominant-baseline="central">{esc(centre[1])}</text></g>')
    else:
        out.append(f'<text class="th" x="105" y="{mid:.0f}" text-anchor="middle" dominant-baseline="central">{esc(centre[0])}</text></g>')
    for (b, items), c in zip(rows, branch_c):
        nodes.append(f'<g class="c-purple"><rect x="215" y="{c - 18:.0f}" width="150" height="36" rx="8" stroke-width="0.5"/>'
                     f'<text class="th" x="290" y="{c:.0f}" text-anchor="middle" dominant-baseline="central">{esc(b.get("title"))}</text></g>')
        for i, top, h, lines in items:
            colour = "c-teal" if i.get("by") == "student" else "c-gray"
            txt = "".join(
                f'<text class="ts" x="436" y="{top + (13 if len(lines) == 1 else 13 + 14 * n):.0f}" dominant-baseline="central">{esc(ln)}</text>'
                for n, ln in enumerate(lines))
            txt = (f'<text class="ts" x="410" y="{top + 13:.0f}" dominant-baseline="central" opacity="0.7">{esc(i.get("id"))}</text>' + txt)
            nodes.append(f'<g class="{colour}"><rect x="400" y="{top}" width="250" height="{h}" rx="6" stroke-width="0.5"/>{txt}</g>')
            t = tag(i, ids)
            if t:
                nodes.append(f'<circle class="{"c-green" if t == "ok" else "c-amber"}" cx="640" cy="{top + h / 2:.0f}" r="4" stroke-width="0.5"/>')
    out += nodes
    ly = bottom + 30
    legend = [("rect", "c-teal", "Your thought"), ("rect", "c-gray", "Otto's suggestion"),
              ("circle", "c-green", "In your library"), ("circle", "c-amber", "Needs a source")]
    x = 40
    for shape, cls, label in legend:
        if shape == "rect":
            out.append(f'<rect class="{cls}" x="{x}" y="{ly - 7}" width="14" height="14" rx="3" stroke-width="0.5"/>')
        else:
            out.append(f'<circle class="{cls}" cx="{x + 7}" cy="{ly}" r="4" stroke-width="0.5"/>')
        out.append(f'<text class="ts" x="{x + 22}" y="{ly}" dominant-baseline="central">{label}</text>')
        x += 32 + int(len(label) * 6.5)
    if any(i.get("wild") for b in branches for i in b["ideas"]):
        out.append(f'<text class="ts" x="{x}" y="{ly}" dominant-baseline="central">* wild card</text>')
    height = ly + 30
    n = sum(len(b["ideas"]) for b in branches)
    return (f'<svg width="100%" viewBox="0 0 680 {height:.0f}" role="img"><title>Your thoughts mind map</title>'
            f'<desc>Mind map of {n} ideas in {len(branches)} branches around: {esc(data.get("centre"))}</desc>'
            + "".join(out) + "</svg>")


# ------------------------------------------------------------------ page
def page_html(data: dict, ids: set[str]) -> str:
    def idea_row(i: dict) -> str:
        t = tag(i, ids)
        src = ", ".join(esc(s) for s in i.get("sources") or [] if s in ids)
        badge = (f'<span class="src ok">{src}</span>' if t == "ok"
                 else f'<span class="src need">needs: {esc(i.get("needed") or "a source")}</span>' if t == "nd" else "")
        status = i.get("status", "open")
        st = {"discussed": "discussed", "outlined": f"in outline {esc(i.get('where', ''))}".strip()}.get(status, "")
        return (f'<li class="{"me" if i.get("by") == "student" else "otto"}"><span class="id">{esc(i.get("id"))}</span> '
                f'{esc(i.get("text"))}{" <em>wild card</em>" if i.get("wild") else ""} {badge}'
                + (f' <span class="st">{st}</span>' if st else "")
                + (f'<div class="note">{esc(i["note"])}</div>' if i.get("note") else "") + "</li>")
    secs, dropped = [], []
    for b in data.get("branches") or []:
        live = [i for i in b.get("ideas") or [] if i.get("status") != "dropped"]
        dropped += [i for i in b.get("ideas") or [] if i.get("status") == "dropped"]
        secs.append(f'<section><h2>{esc(b.get("title"))}</h2><ul>{"".join(idea_row(i) for i in live)}</ul></section>')
    drop = (f'<section class="dropped"><h2>Set aside</h2><ul>{"".join(idea_row(i) for i in dropped)}</ul></section>'
            if dropped else "")
    svg = chat_svg(data, ids)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Mind map - {esc(data.get("centre"))}</title>
<style>
:root{{--bg:#f6f5f2;--card:#fff;--text:#1f2328;--muted:#6b7079;--line:#e6e3dc;--ok:#2e7d4f;--okt:#e8f5ee;--need:#a86a12;--needt:#fbf2e2;--me:#0f6e56;--otto:#5f5e5a;
--p:#2c2c2a;--s:#5f5e5a;--b:#d3d1c7}}
@media (prefers-color-scheme: dark){{:root{{--bg:#141619;--card:#1c1f23;--text:#e6e7e9;--muted:#9aa1ab;--line:#2d3137;--ok:#5cc08a;--okt:#17301f;--need:#e2a94f;--needt:#35281a;--me:#5dcaa5;--otto:#b4b2a9}}}}
body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:820px;margin:0 auto;padding:32px 16px 64px}}
.kicker{{font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
h1{{font:600 1.6rem/1.25 Georgia,serif;margin:6px 0 18px}} h2{{font:600 1.1rem/1.3 Georgia,serif;margin:22px 0 6px}}
.map{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px}}
.map text{{font:12px sans-serif;fill:var(--text)}} .map .th{{font-weight:600;font-size:13px}}
.map .c-purple rect{{fill:#eeedfe;stroke:#534ab7}} .map .c-purple text{{fill:#3c3489}}
.map .c-teal rect,.map rect.c-teal{{fill:#e1f5ee;stroke:#0f6e56}} .map .c-teal text{{fill:#085041}}
.map .c-gray rect,.map rect.c-gray{{fill:#f1efe8;stroke:#5f5e5a}} .map .c-gray text{{fill:#444441}}
.map circle.c-green{{fill:#639922}} .map circle.c-amber{{fill:#ef9f27}}
ul{{margin:0;padding-left:0;list-style:none}} li{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--otto);padding:8px 12px;margin:6px 0}}
li.me{{border-left-color:var(--me)}} .id{{color:var(--muted);font-size:.8rem;margin-right:4px}}
.src{{font-size:.75rem;padding:0 7px;border-radius:6px;margin-left:4px}} .src.ok{{background:var(--okt);color:var(--ok)}} .src.need{{background:var(--needt);color:var(--need)}}
.st{{font-size:.75rem;color:var(--muted);margin-left:4px}} .note{{color:var(--muted);font-size:.9rem;margin-top:2px}}
.dropped li{{opacity:.7}} .foot{{color:var(--muted);font-size:.8rem;margin-top:24px}}
@media print{{body{{background:#fff}}li{{break-inside:avoid}}}}
</style></head><body><div class="wrap">
<div class="kicker">Mind map · updated {esc(data.get("updated") or dt.date.today().isoformat())}</div>
<h1>{esc(data.get("centre"))}</h1><div class="map">{svg}</div>{"".join(secs)}{drop}
<p class="foot">Teal: your own thoughts · grey: Otto's suggestions · green tags are sources in your library · amber tags still need a source.</p>
</div></body></html>"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="mind map JSON file")
    ap.add_argument("--root", help="project root (default: folder above scripts/)")
    ap.add_argument("--chat", action="store_true", help="also write the in-chat SVG")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    src = Path(args.input)
    if not src.is_absolute():
        src = (Path.cwd() / src).resolve()

    def shown(p: Path) -> str:
        try:
            return p.relative_to(root).as_posix()
        except ValueError:
            return str(p)
    try:
        data = json.loads(src.read_text(encoding="utf-8"))
        ids = library_ids(root)
        checks, unknown = check(data, ids)
        out = src.with_suffix(".html")
        out.write_text(page_html(data, ids), encoding="utf-8")
        ideas = [i for b in data.get("branches") or [] for i in b.get("ideas") or []]
        result = {"ok": True, "output": shown(out), "branches": len(data.get("branches") or []),
                  "ideas": sum(1 for i in ideas if i.get("status") != "dropped"),
                  "dropped": sum(1 for i in ideas if i.get("status") == "dropped")}
        if args.chat:
            chat = src.with_name(src.stem + ".chat.html")
            chat.write_text(chat_svg(data, ids), encoding="utf-8")
            result["chat"] = shown(chat)
        if checks:
            result["checks"] = checks
        if unknown:
            result["unknown_sources"] = unknown
            result["warning"] = "these sources are not in INDEX.md and were shown as needing a source"
    except FileNotFoundError:
        result = {"ok": False, "error": "not_found", "message": f"File not found: {src}"}
    except json.JSONDecodeError as e:
        result = {"ok": False, "error": "bad_json", "message": f"The mind map file isn't valid JSON: {e}"}
    except Exception as e:  # noqa: BLE001 - always answer in one JSON line
        result = {"ok": False, "error": "unexpected", "message": f"{type(e).__name__}: {e}"}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
