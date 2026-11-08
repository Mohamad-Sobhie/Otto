# In-chat visual cards (Discuss)

Discuss output is shown **inside the chat** as coloured cards, using the Claude app's built-in visual tool (`show_widget`, from the `visualize` tools). The student never has to open a browser.

## Rules

- **Once per session, before the first card,** call the visual tool's `read_me` (modules `mockup` and `interactive`) silently. Never mention it.
- One `show_widget` call per stage. Give it a specific `title` (e.g. `discuss_nbfi_lenses`, `discuss_nbfi_argument_map`).
- The tool's own rules apply: no emoji inside the widget, sentence case, font weights 400/500 only, colours only through CSS variables (they adapt to dark mode), no big headings inside the widget (use the small `.pl` / `.lb` labels).
- Keep the fixed colour per lens (the chat emoji in the text match):

| Lens | Accent `--a` | Tint `--t` | Icon | Chat emoji |
|---|---|---|---|---|
| practitioner | `var(--text-tint-blue)` | `var(--bg-tint-blue)` | `ti-tool` | 🟦 |
| skeptic | `var(--text-tint-red)` | `var(--bg-tint-red)` | `ti-help` | 🟥 |
| economist | `var(--text-tint-green)` | `var(--bg-tint-green)` | `ti-coin-pound` (`ti-coin` outside the UK) | 🟩 |
| historian | `var(--text-tint-yellow)` | `var(--bg-tint-yellow)` | `ti-hourglass` | 🟨 |
| academic | `var(--text-tint-violet)` | `var(--bg-tint-violet)` | `ti-books` | 🟪 |
| legal (the Lawyer) | `var(--text-tint-aqua)` | `var(--bg-tint-aqua)` | `ti-scale` | 🔷 |
| justice (Social justice) | `var(--text-tint-magenta)` | `var(--bg-tint-magenta)` | `ti-heart-handshake` | 🩷 |
| global_south (the Global South) | `var(--text-tint-orange)` | `var(--bg-tint-orange)` | `ti-world` | 🟧 |
| schools of thought | the same eight hues in order (they replace the lenses) | | `ti-building-bank`, `ti-flag`, `ti-scale`, ... | ◻️ |

- Source tags: library-backed → class `ok` (`var(--bg-success)` / `var(--text-success)`), text `source-id, pinpoint`. Gap → class `nd` (`var(--bg-warning)` / `var(--text-warning)`), text `needs: kind of source` or `not in your library yet`. Only sources that are in INDEX.md may get an `ok` tag.
- **No `sendPrompt` buttons.** Buttons that send a message to the chat don't work in the Claude Code app, so never add any. Show/hide toggles and filter chips that only change the page (the script in the stage 1 template) are fine. Next steps go in the widget's next-step box and the reply's *Next:* line.
- **Write the full content as plain HTML, then let the script fold it.** Everything is visible while the widget streams (and if the script fails); the script at the end builds the filter chips and folds the full reasoning. Copy the script exactly.
- **Everything goes in the cards; nothing is repeated in text.** The reply around a widget is exactly:
  1. one short intro line before it (e.g. "Here's your question through the eight lenses. Tap a lens to hide it, or open its full reasoning:"), and
  2. one *Next:* line after it, recommended step first.
  Never restate, summarise or list the cards' content in text - the student sees it once, in the cards.
- **If the visual tool isn't available** (e.g. the terminal version of Claude Code), give the same content as markdown with the chat emoji per lens (layout in SKILL.md) - never paste raw HTML into the reply.

## Shared style block (start every widget with this)

```html
<h2 class="sr-only">ONE-SENTENCE SUMMARY OF THE WIDGET</h2>
<style>
.pc{background:var(--surface-2);border:0.5px solid var(--border);border-radius:12px;padding:14px 18px 14px 20px;margin:0 0 10px;position:relative;overflow:hidden}
.pc::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--a)}
.ph{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.pi{width:28px;height:28px;border-radius:8px;background:var(--t);color:var(--a);display:flex;align-items:center;justify-content:center;font-size:16px;flex:none}
.pn{font-weight:500;font-size:15px}
.pt{margin-left:auto;font-size:13px;font-style:italic;color:var(--text-secondary)}
.pl,.lb{font-size:11px;letter-spacing:.04em;color:var(--a,var(--text-secondary));font-weight:500;margin:10px 0 2px}
.lb{color:var(--text-secondary);margin:0 0 6px}
.pc p,.bx p{margin:0;font-size:14px;line-height:1.6}
.pc ul,.pc ol,.bx ul,.bx ol{margin:2px 0 0;padding-left:18px;font-size:14px;line-height:1.6}
.tg{display:inline-block;font-size:12px;padding:0 8px;border-radius:6px;margin-left:4px}
.ok{background:var(--bg-success);color:var(--text-success)}
.nd{background:var(--bg-warning);color:var(--text-warning)}
.bx{background:var(--surface-2);border:0.5px solid var(--border);border-radius:12px;padding:12px 16px;margin:0 0 10px}
.ch{display:inline-block;font-size:12px;padding:1px 9px;border-radius:999px;background:var(--t);color:var(--a);font-weight:500}
.dt{display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--a);margin-right:3px}
.row{display:flex;gap:12px;padding:8px 0;border-bottom:0.5px solid var(--border);align-items:flex-start}
.row:last-child{border-bottom:none}
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}
.f{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px}
.f button{font-size:12px;padding:3px 10px;border-radius:999px;border:0.5px solid var(--border-strong);background:transparent;color:var(--text-secondary);cursor:pointer}
.f button.on{background:var(--t);color:var(--a);border-color:transparent}
.mr{font-size:12px;color:var(--a);background:none;border:none;padding:0;margin-top:8px;cursor:pointer}
.fr{margin-top:8px}
.ag{border-top:0.5px solid var(--border);padding:8px 0 4px}
.an{font-size:14px;font-weight:500;line-height:1.5;margin-bottom:4px}
.r{display:grid;grid-template-columns:110px minmax(0,1fr);gap:8px;font-size:13px;line-height:1.55;padding:2px 0}
.r b{font-weight:500;color:var(--a)}
.nx{border:0.5px solid var(--border);border-radius:12px;padding:12px 16px;margin-top:10px;background:var(--surface-1)}
</style>
<div style="padding:.5rem 0">
  ... stage content ...
</div>
```

## Stage 1 · the eight lenses

Order: step label, filter bar, the eight lens cards inside `#cards`, then clashes, thesis, examiner questions, the next-step box, and the script last.

```html
<div class="lb">Step 1 of 4 · eight lenses · tap a lens to hide it</div>
<div class="f" id="f"></div>
<div id="cards">
<div class="pc" style="--a:var(--text-tint-aqua);--t:var(--bg-tint-aqua)">
  <div class="ph"><div class="pi"><i class="ti ti-scale" aria-hidden="true"></i></div>
    <div class="pn">The lawyer</div><div class="pt">reads the rulebook</div></div>
  <p>Position: one sentence that answers the question.</p>
  <ol class="cl"><li>Claim 1, one line</li><li>Claim 2</li><li>Claim 3</li></ol>
  <button class="mr">Show full reasoning</button>
  <div class="fr">
    <div class="ag"><div class="an">1. Claim 1</div>
      <div class="r"><b>Because</b><span>grounds <span class="tg nd">needs: FPC powers provisions</span></span></div>
      <div class="r"><b>Only holds if</b><span>hidden assumption</span></div>
      <div class="r"><b>Type</b><span>rule and authority</span></div>
      <div class="r"><b>Weak point</b><span>the critical question, made specific</span></div>
      <div class="r"><b>Objection</b><span><span class="ch" style="--a:var(--text-tint-green);--t:var(--bg-tint-green)">Economist</span> the objection</span></div>
      <div class="r"><b>Reply</b><span>the reply (or "no good reply yet")</span></div>
    </div>
    ... one .ag per argument (3-4) ...
  </div>
</div>
... the other seven lens cards, in order ...
</div>
<div class="bx"><div class="pl">Where they clash</div>
  <div class="row"><div style="white-space:nowrap;padding-top:4px"><span class="dt" style="--a:var(--text-tint-blue)"></span><span class="dt" style="--a:var(--text-tint-yellow)"></span></div>
    <p><span style="font-weight:500">Practitioner vs historian:</span> the disagreement · who wins, on what condition</p></div>
</div>
<div class="bx"><div class="pl">What this means for your thesis</div><p>...</p></div>
<div class="bx"><div class="pl">Likely examiner questions</div><ol><li>...</li></ol></div>
<div class="nx"><div class="lb">Recommended next step</div><p style="margin:0;font-size:14px;line-height:1.6">The step, and why these results point to it. Or: alternative · alternative.</p></div>
<script>
(()=>{const f=document.getElementById('f'),cs=[...document.querySelectorAll('#cards .pc')];
const set=(c,o)=>{c.querySelector('.fr').style.display=o?'':'none';const l=c.querySelector('.cl');if(l)l.style.display=o?'none':'';c.querySelector('.mr').textContent=o?'Hide full reasoning':'Show full reasoning'};
cs.forEach(c=>{const b=document.createElement('button');b.className='on';b.style.cssText=c.style.cssText;b.textContent=c.querySelector('.pn').textContent.replace(/^the /i,'');
b.onclick=()=>{b.classList.toggle('on');c.style.display=b.classList.contains('on')?'':'none'};f.appendChild(b);
set(c,false);c.querySelector('.mr').onclick=()=>set(c,c.querySelector('.fr').style.display=='none')});
const a=document.createElement('button');a.textContent='Expand all';let all=false;
a.onclick=()=>{all=!all;cs.forEach(c=>set(c,all));a.textContent=all?'Collapse all':'Expand all'};f.appendChild(a)})();
</script>
```
Next line: *Next: [recommended step] · map the arguments · play the examiner*.

## Stage 2 · argument map and fight map

Argument map first (one node per lens, in order, built from the stage 1 arguments; reasons green, objections red with the attacking lens and the reply), then the fight map below it, in the same widget. Label: `Step 2 of 4 · argument map`.

```html
<style>
.mq{border:0.5px solid var(--border-strong);border-radius:12px;padding:10px 14px;text-align:center;font-size:15px;font-weight:500;margin:0 0 10px}
.mg{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:10px;margin-bottom:12px}
.mn{border:0.5px solid var(--border);border-top:3px solid var(--a);border-radius:0;padding:10px 12px;background:var(--surface-2)}
.mh{font-size:13px;font-weight:500;color:var(--a);margin-bottom:4px}
.mp,.mo{font-size:13px;line-height:1.5;padding:4px 0 4px 10px;margin-top:6px;border-left:3px solid var(--text-success)}
.mo{border-left-color:var(--text-danger);margin-left:12px;color:var(--text-secondary)}
</style>
<div class="mq">The question</div>
<div class="mg">
  <div class="mn" style="--a:var(--text-tint-blue)"><div class="mh">Practitioner</div>
    <p style="margin:0;font-size:13px;font-weight:500">Position</p>
    <div class="mp">Claim 1</div><div class="mo">Lawyer: objection → reply</div>
    <div class="mp">Claim 2</div><div class="mo">Economist: objection → reply</div>
  </div>
  ... one node per lens ...
</div>
<p style="font-size:12px;color:var(--text-secondary);margin:0 0 12px">Green: reasons · red: objections, named by the lens that raises them</p>
```

Then the fight map:

```html
<div class="bx"><div class="pl">Direct contradictions</div>
  <div class="row"><div style="white-space:nowrap;padding-top:4px"><span class="dt" style="--a:var(--text-tint-red)"></span><span class="dt" style="--a:var(--text-tint-blue)"></span></div>
    <p><span style="font-weight:500">Skeptic vs practitioner:</span> ...</p></div>
</div>
<div class="g2">
  <div class="bx" style="border-top:3px solid var(--text-success);border-radius:0 0 12px 12px"><div class="pl">Strongest evidence</div>
    <span class="ch" style="--a:var(--text-tint-green);--t:var(--bg-tint-green)">Economist</span><p style="margin-top:6px">why ...</p></div>
  <div class="bx" style="border-top:3px solid var(--text-danger);border-radius:0 0 12px 12px"><div class="pl">Weakest evidence</div>
    <span class="ch" style="--a:var(--text-tint-yellow);--t:var(--bg-tint-yellow)">Historian</span><p style="margin-top:6px">why ...</p></div>
  <div class="bx"><div class="pl">What they all agree on</div><ul><li>...</li></ul></div>
  <div class="bx"><div class="pl">What nobody addressed</div><ul><li>To check: ...</li></ul></div>
</div>
```
Next line: *Next: write the briefing · debate the two strongest*. Use step labels `Step 3 of 4 · briefing` and `Step 4 of 4 · peer review` on the later stages.

## Stage 3 · briefing

```html
<div class="bx"><div class="pl">Supervisor summary</div><p>one paragraph</p></div>
<div class="bx"><div class="pl">Key findings · ranked by reliability</div>
  <div class="row">
    <div style="width:22px;height:22px;border-radius:50%;background:var(--text-primary);color:var(--surface-2);font-size:12px;display:flex;align-items:center;justify-content:center;flex:none">1</div>
    <div style="flex:1"><p>finding</p><span class="ch" style="--a:var(--text-tint-green);--t:var(--bg-tint-green)">Economist</span></div>
    <div style="font-size:12px;font-weight:500;color:var(--text-success)">High</div>
  </div>
  ... (Medium → var(--text-warning), Low → var(--text-danger))
</div>
<div class="bx" style="border-left:3px solid var(--text-tint-violet);border-radius:0"><div class="pl">Hidden connection</div><p>...</p></div>
<div class="bx" style="border-left:3px solid var(--text-success);border-radius:0;background:var(--bg-success)"><div class="pl">One thing to change in your thesis</div><p>...</p></div>
```
"High" only when a library source backs the finding; otherwise Medium at most. Next line: *Next: grade your work · draft the section*.

## Stage 4 · peer review

```html
<div class="bx"><div class="pl">Confidence per finding</div>
  <div class="row"><div style="flex:1"><p>1. finding (short)</p><p style="font-size:12px;color:var(--text-secondary)">why</p></div>
    <div style="display:flex;align-items:center;gap:8px"><div style="width:100px;height:6px;border-radius:3px;background:var(--border)"><div style="width:90%;height:6px;border-radius:3px;background:var(--text-primary)"></div></div><span style="font-size:12px;font-weight:500">9/10</span></div></div>
</div>
<div class="bx" style="border-left:3px solid var(--text-danger);border-radius:0"><div class="pl">Weakest claim</div><p style="font-weight:500">...</p><p style="color:var(--text-secondary)">Why: ... · Fix: ...</p></div>
<div class="bx"><div class="pl">Bias check · whose voice shaped the findings</div>
  <div style="display:flex;height:10px;border-radius:5px;overflow:hidden;gap:2px;margin:8px 0">
    <div style="flex:2;background:var(--text-tint-green)"></div><div style="flex:1;background:var(--text-tint-red)"></div> ...
  </div>
  <p>Economist drives 2 of 5 findings ... Not represented: Academic.</p>
</div>
```
Count the bar segments from the briefing's findings (one per finding, by perspective); flag any perspective behind 40%+ and name any that's missing. Scores: no library source → 6 at most; pure pattern or opinion → 4 at most.

## Outline (table of contents)

One card per chapter; sections as rows inside it. Use a neutral accent (`--a:var(--text-secondary)`) for chapters - the perspective colours are reserved for Discuss. When showing two alternative structures, put a small label above each set ("Structure A · thematic", "Structure B · comparative") using `.pl`, and one line on what each is good for inside a `.bx` above its chapters.

```html
<div class="pc" style="--a:var(--text-secondary);--t:var(--surface-1)">
  <div class="ph"><div class="pi" style="font-size:13px;font-weight:500">3</div>
    <div class="pn">Regulating through banks</div><div class="pt">4,500 words · RQ1</div></div>
  <p style="color:var(--text-secondary)">one-line purpose of the chapter</p>
  <div class="row"><div style="width:34px;font-size:13px;color:var(--text-secondary)">3.1</div>
    <div style="flex:1"><p>Entity-based tools</p><p style="font-size:12px;color:var(--text-secondary)">bank exposure limits and reporting</p></div>
    <div style="text-align:right;white-space:nowrap"><div style="font-size:12px">2,500 w</div><span class="tg ok">2 sources</span></div></div>
  <div class="row"><div style="width:34px;font-size:13px;color:var(--text-secondary)">3.2</div>
    <div style="flex:1"><p>Limits of the approach</p></div>
    <div style="text-align:right;white-space:nowrap"><div style="font-size:12px">2,000 w</div><span class="tg nd">needs: 2022 LDI analysis</span></div></div>
</div>
```

Budget bar (once, under the chapters) - one segment per chapter, proportional to its budget, with the total vs the limit:

```html
<div class="bx"><div class="pl">Word budget · 15,000 of 15,000</div>
  <div style="display:flex;height:10px;border-radius:5px;overflow:hidden;gap:2px;margin:8px 0">
    <div style="flex:1500;background:var(--border-strong)"></div><div style="flex:3000;background:var(--text-secondary)"></div> ...
  </div>
  <p style="font-size:13px;color:var(--text-secondary)">1 Intro 1,500 · 2 Risk 3,000 · 3 Banks 4,500 · 4 Backstops 4,000 · 5 Conclusion 2,000</p>
</div>
```

Checks card (only if there's something to flag), with `.nd` tags: "RQ3 has no section", "Chapter 2's sections add up to 3,500 of 3,000 words", "No comparison chapter for a comparative question".

When editing, mark changed rows with a small tag before the title: `<span class="tg nd">changed</span>`, `<span class="tg ok">new</span>`, `<span class="tg" style="background:var(--bg-danger);color:var(--text-danger)">removed</span>` (keep removed rows, struck through: `style="text-decoration:line-through;color:var(--text-secondary)"`), and show renumbering as "2.2 → 3.1" in the number column.

*Next:* line: creating → *Next: "use A" / "use B" · or tell me what to change*; editing → *Next: "go" to save · or tell me what else to change*.
