#!/usr/bin/env python3
"""
Build FLASH_Wiki.html — a single self-contained, zero-setup interactive Wiki.
Double-click to open in any browser. All data embedded; no server needed.
Usage: python3 pipeline/build_wiki_html.py   (run from the folder root)
"""
import os, json, re, html
from collections import Counter

# This script lives in <root>/pipeline/; it reads the corpus from
# <root>/library/ and writes FLASH_Wiki.html to <root>/ so the WG can
# double-click it straight from the top of the folder.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LIB = os.path.join(ROOT, "library")
DATA = json.load(open(os.path.join(LIB, "flash_library.json"), encoding="utf-8"))
RECS = DATA["records"]
GEN = DATA["generated"]

CAT_ORDER = ["Radiobiology","Physics & Dosimetry","Modeling & Mechanisms",
    "Beam Delivery & Technology","Treatment Planning & Optimization",
    "Clinical & Translational","Reviews & Consensus",
    "Opinions & Debate","Point-Counterpoint","Perspectives & Commentary",
    "Uncategorized"]

def tldr(a):
    if not a: return ""
    a = re.sub(r"^[A-Z][A-Za-z /]+:\s*", "", a.strip())
    s = re.split(r"(?<=[.!?])\s+", a)
    o = " ".join(s[:2])
    return o[:360] + ("…" if len(o) > 360 else "")

# slim records for embedding
slim = []
for r in RECS:
    slim.append({
        "p": r["pmid"], "y": r["year"], "t": r["title"],
        "a": "; ".join(r["authors"]), "j": r["journal"],
        "c": r["category"], "g": r["tags"], "d": r["doi"],
        "m": r["pmc"], "u": r["url"], "s": tldr(r["abstract"]),
        # "ai" = agent summary, present only for triaged records. Kept as a
        # separate key from "s" so the UI can label it; it must never silently
        # replace the authors' own words.
        "ai": r.get("summary", ""),
        "b": r["abstract"],
    })
cc = Counter(r["category"] for r in RECS)
years = sorted(set(int(r["year"]) for r in RECS if r["year"].isdigit()))
oa = sum(1 for r in RECS if r["pmc"])
payload = json.dumps(slim, ensure_ascii=False, separators=(",", ":"))

# year histogram for the mini chart (last 20y)
yc = Counter(int(r["year"]) for r in RECS if r["year"].isdigit())
ymin = max(min(years), 2005)
yhist = [(y, yc.get(y, 0)) for y in range(ymin, max(years) + 1)]
ymax = max(n for _, n in yhist) or 1
bars = "".join(
    f'<div class="yb" title="{y}: {n}"><span style="height:{max(2,int(100*n/ymax))}%"></span>'
    f'<label>{"’"+str(y)[2:] if y%5==0 else ""}</label></div>' for y, n in yhist)

CATJSON = json.dumps({c: cc.get(c, 0) for c in CAT_ORDER})

HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FLASH Radiotherapy Living Wiki — AAPM BESC FLASH WG</title>
<style>
:root{{--navy:#1F4E79;--accent:#2E74B5;--light:#EAF1F8;--ink:#1a2b3c;--muted:#5b6b7b;
--line:#d8e2ee;--oa:#2e7d32;--bg:#f4f7fb;}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
color:var(--ink);background:var(--bg);line-height:1.5}}
header{{background:linear-gradient(135deg,#183a5c,#2E74B5);color:#fff;padding:22px 26px 18px}}
header h1{{margin:0;font-size:1.5rem;letter-spacing:.2px}}
header .sub{{opacity:.9;font-size:.9rem;margin-top:3px}}
.stats{{display:flex;gap:26px;margin-top:14px;flex-wrap:wrap}}
.stat{{background:rgba(255,255,255,.12);padding:8px 14px;border-radius:9px}}
.stat b{{font-size:1.25rem;display:block;line-height:1.1}}
.stat span{{font-size:.72rem;opacity:.9;text-transform:uppercase;letter-spacing:.5px}}
.chart{{margin-top:14px}}
.chart .yb{{display:inline-flex;flex-direction:column;justify-content:flex-end;align-items:center;
width:calc((100% - 0px)/{len(yhist)});height:54px;vertical-align:bottom}}
.chart .yb span{{width:62%;background:rgba(255,255,255,.55);border-radius:2px 2px 0 0;min-height:2px}}
.chart .yb:hover span{{background:#fff}}
.chart .yb label{{font-size:.55rem;opacity:.8;margin-top:2px;height:10px}}
.chartwrap{{display:flex;align-items:flex-end;width:100%;max-width:640px}}
.wrap{{display:flex;gap:0;align-items:flex-start}}
aside{{width:250px;flex:0 0 250px;padding:18px 16px;position:sticky;top:0;height:100vh;
overflow:auto;border-right:1px solid var(--line);background:#fff}}
main{{flex:1;padding:18px 26px;min-width:0}}
.search{{width:100%;padding:11px 13px;font-size:.95rem;border:1px solid var(--line);
border-radius:9px;margin-bottom:6px}}
.controls{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0 14px;
font-size:.85rem;color:var(--muted)}}
select{{padding:6px 8px;border:1px solid var(--line);border-radius:7px;font-size:.85rem}}
.toggle{{display:flex;align-items:center;gap:6px;cursor:pointer}}
h3.side{{font-size:.72rem;text-transform:uppercase;letter-spacing:.7px;color:var(--muted);
margin:6px 0 8px}}
.chip{{display:block;width:100%;text-align:left;border:none;background:none;padding:7px 10px;
border-radius:8px;cursor:pointer;font-size:.86rem;color:var(--ink);margin-bottom:2px}}
.chip:hover{{background:var(--light)}}
.chip.on{{background:var(--navy);color:#fff;font-weight:600}}
.chip .n{{float:right;opacity:.7;font-variant-numeric:tabular-nums}}
.chip.on .n{{opacity:.95}}
.count{{font-size:.85rem;color:var(--muted);margin-bottom:12px}}
.card{{background:#fff;border:1px solid var(--line);border-radius:11px;padding:15px 17px;
margin-bottom:12px}}
.card h2{{font-size:1.02rem;margin:0 0 5px;line-height:1.35}}
.card h2 a{{color:var(--navy);text-decoration:none}}
.card h2 a:hover{{text-decoration:underline}}
.meta{{font-size:.82rem;color:var(--muted);margin-bottom:8px}}
.badges{{margin:6px 0}}
.badge{{display:inline-block;padding:2px 9px;margin:2px 4px 2px 0;border-radius:11px;
font-size:.7rem;font-weight:600}}
.badge.oa{{background:var(--oa);color:#fff}}
.badge.tag{{background:var(--light);color:var(--navy)}}
.tldr{{font-size:.9rem;margin:8px 0}}
details{{margin-top:6px}}
details summary{{cursor:pointer;color:var(--accent);font-size:.83rem;font-weight:600}}
.aisum{{margin:.5rem 0;padding:.55rem .7rem;border-left:3px solid var(--accent);background:rgba(127,127,127,.07);font-size:.88rem;line-height:1.45}}
.aitag{{font-size:.68rem;letter-spacing:.03em;text-transform:uppercase;opacity:.7;font-weight:600}}
details p{{font-size:.86rem;color:#33475b;margin:8px 0 2px}}
.links{{margin-top:10px;font-size:.83rem}}
.links a{{color:var(--accent);text-decoration:none;margin-right:14px;font-weight:600}}
.links a:hover{{text-decoration:underline}}
footer{{padding:22px 26px;color:var(--muted);font-size:.78rem;border-top:1px solid var(--line);
background:#fff}}
mark{{background:#fff3b0;padding:0 1px}}
@media(max-width:760px){{.wrap{{flex-direction:column}}aside{{width:100%;flex:none;height:auto;
position:static;border-right:none;border-bottom:1px solid var(--line)}}}}
</style></head><body>
<header>
  <h1>FLASH Radiotherapy — Living Literature Wiki</h1>
  <div class="sub">AAPM · BESC · FLASH Working Group &nbsp;|&nbsp; corpus generated {GEN}</div>
  <div class="stats">
    <div class="stat"><b>{len(RECS):,}</b><span>curated papers</span></div>
    <div class="stat"><b>{len(CAT_ORDER)}</b><span>categories</span></div>
    <div class="stat"><b>{oa:,}</b><span>open access</span></div>
    <div class="stat"><b>{min(years)}–{max(years)}</b><span>span</span></div>
  </div>
  <div class="chart"><div class="chartwrap">{bars}</div></div>
</header>
<div class="wrap">
  <aside>
    <h3 class="side">Categories</h3>
    <div id="cats"></div>
  </aside>
  <main>
    <input id="q" class="search" placeholder="Search titles, abstracts, authors, journals…" autofocus>
    <div class="controls">
      <label class="toggle"><input type="checkbox" id="oa"> Open access only</label>
      <span>Sort
        <select id="sort">
          <option value="year">Newest first</option>
          <option value="old">Oldest first</option>
          <option value="title">Title A–Z</option>
        </select>
      </span>
      <span>Year ≥ <select id="yr"></select></span>
    </div>
    <div class="count" id="count"></div>
    <div id="results"></div>
  </main>
</div>
<footer>
  Generated by the FLASH WG literature-automation pipeline. Each entry links to PubMed and,
  where available, DOI and open-access full text (PMC). Abstracts are the authors’ own.
  Re-run <code>flash_harvest.py</code> to refresh. &nbsp;|&nbsp; v1.0
</footer>
<script id="data" type="application/json">{payload}</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const CATS = {CATJSON};
const catOrder = {json.dumps(CAT_ORDER)};
let state = {{q:'', cat:null, oa:false, sort:'year', yr:0}};

const el = id => document.getElementById(id);
function esc(s){{return (s||'').replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c]));}}
function hl(s, q){{ if(!q) return esc(s); const t=esc(s);
  try{{return t.replace(new RegExp('('+q.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&')+')','ig'),'<mark>$1</mark>');}}catch(e){{return t;}} }}

// build category chips
function buildCats(){{
  let h = `<button class="chip ${{state.cat===null?'on':''}}" data-c="">All categories <span class="n">${{DATA.length}}</span></button>`;
  for(const c of catOrder){{ if(!CATS[c]) continue;
    h += `<button class="chip ${{state.cat===c?'on':''}}" data-c="${{esc(c)}}">${{esc(c)}} <span class="n">${{CATS[c]}}</span></button>`; }}
  el('cats').innerHTML = h;
  el('cats').querySelectorAll('.chip').forEach(b=>b.onclick=()=>{{
    state.cat = b.dataset.c || null; render(); buildCats();
  }});
}}
// year dropdown
(function(){{ const ys=[...new Set(DATA.map(d=>+d.y).filter(Boolean))].sort((a,b)=>a-b);
  let h='<option value="0">any</option>';
  for(let y=2005;y<=Math.max(...ys);y+=5) h+=`<option value="${{y}}">${{y}}</option>`;
  el('yr').innerHTML=h; }})();

function match(d){{
  if(state.cat && d.c!==state.cat) return false;
  if(state.oa && !d.m) return false;
  if(state.yr && (+d.y||0) < state.yr) return false;
  if(state.q){{ const q=state.q.toLowerCase();
    return (d.t+' '+d.a+' '+d.j+' '+d.b).toLowerCase().includes(q); }}
  return true;
}}
function card(d){{
  const q=state.q;
  const badges = (d.m?`<span class="badge oa">Open access</span>`:'')+
    d.g.slice(0,4).map(t=>`<span class="badge tag">${{esc(t)}}</span>`).join('');
  const links = [`<a href="${{d.u}}" target="_blank">PubMed</a>`]
    .concat(d.d?[`<a href="https://doi.org/${{d.d}}" target="_blank">DOI</a>`]:[])
    .concat(d.m?[`<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/${{d.m}}/" target="_blank">Full text</a>`]:[]).join('');
  return `<div class="card">
    <h2><a href="${{d.u}}" target="_blank">${{hl(d.t,q)}}</a></h2>
    <div class="meta">${{hl(d.a,q)}} — ${{esc(d.j)}} (${{d.y||'n.d.'}})</div>
    <div class="badges">${{badges}}</div>
    ${{d.s?`<div class="tldr"><b>TL;DR.</b> ${{hl(d.s,q)}}</div>`:''}}
    ${{d.ai?`<div class="aisum"><b>Summary</b> <span class="aitag">AI-generated, curator-reviewed</span><br>${{hl(d.ai,q)}}</div>`:''}}
    ${{d.b?`<details><summary>Abstract</summary><p>${{hl(d.b,q)}}</p></details>`:''}}
    <div class="links">${{links}}</div></div>`;
}}
function render(){{
  let r = DATA.filter(match);
  if(state.sort==='year') r.sort((a,b)=>(+b.y||0)-(+a.y||0));
  else if(state.sort==='old') r.sort((a,b)=>(+a.y||0)-(+b.y||0));
  else r.sort((a,b)=>a.t.localeCompare(b.t));
  el('count').textContent = `${{r.length.toLocaleString()}} paper${{r.length!==1?'s':''}}`+
    (state.cat?` in ${{state.cat}}`:'')+(state.q?` matching “${{state.q}}”`:'');
  const LIMIT=300;
  el('results').innerHTML = r.slice(0,LIMIT).map(card).join('') +
    (r.length>LIMIT?`<div class="count">Showing first ${{LIMIT}}. Refine your search to see more.</div>`:'');
  window.scrollTo({{top:0,behavior:'instant'}});
}}
let deb; el('q').oninput=e=>{{clearTimeout(deb);deb=setTimeout(()=>{{state.q=e.target.value.trim();render();}},160);}};
el('oa').onchange=e=>{{state.oa=e.target.checked;render();}};
el('sort').onchange=e=>{{state.sort=e.target.value;render();}};
el('yr').onchange=e=>{{state.yr=+e.target.value;render();}};
buildCats(); render();
</script>
</body></html>"""

out = os.path.join(ROOT, "FLASH_Wiki.html")
open(out, "w", encoding="utf-8").write(HTML)
print(f"wrote FLASH_Wiki.html  ({len(HTML)/1e6:.2f} MB, {len(RECS)} records embedded)")
