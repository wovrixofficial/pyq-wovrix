import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -----------------------------------------------------------------------------
# 1. FIX cbse-12/physics/current-electricity/index.html
# -----------------------------------------------------------------------------
curr_elec_path = os.path.join(ROOT, "cbse-12", "physics", "current-electricity", "index.html")
with open(curr_elec_path, "r", encoding="utf-8") as f:
    ce_content = f.read()

# Fix 1: KaTeX parse error on line 789 (unclosed \left$)
old_katex_1 = r"where $\alpha = \left$ \frac{ne^2}{m} \right$ \tau$"
new_katex_1 = r"where $\alpha = \left(\frac{ne^2}{m}\right)\tau$"
assert old_katex_1 in ce_content, "Target KaTeX string 1 not found"
ce_content = ce_content.replace(old_katex_1, new_katex_1)

# Fix 2: KaTeX double superscript on line 2576
old_katex_2 = r"$2.0 \times 10^{-4} ^{\circ}\text{C}^{-1}$"
new_katex_2 = r"$2.0 \times 10^{-4}\text{ }^\circ\text{C}^{-1}$"
assert old_katex_2 in ce_content, "Target KaTeX string 2 not found"
ce_content = ce_content.replace(old_katex_2, new_katex_2)

# Fix 3: KaTeX double superscript on line 2666
old_katex_3 = r"$1.70 \times 10^{-4} \ ^{\circ}\text{C}^{-1}$"
new_katex_3 = r"$1.70 \times 10^{-4}\text{ }^\circ\text{C}^{-1}$"
assert old_katex_3 in ce_content, "Target KaTeX string 3 not found"
ce_content = ce_content.replace(old_katex_3, new_katex_3)

# Fix 4: Orphan prefixes on lines 1353, 1372, 1412, 1431
old_prefix_1 = "33. (a) (i) Derive the condition for which a Wheatstone Bridge is balanced."
new_prefix_1 = "Derive the condition for which a Wheatstone Bridge is balanced."
assert old_prefix_1 in ce_content, "Target prefix string 1 not found"
ce_content = ce_content.replace(old_prefix_1, new_prefix_1)

old_prefix_2 = "(ii) Determine the current in $3\\ \\Omega$ branch of a Wheatstone Bridge in the circuit shown in the figure."
new_prefix_2 = "Determine the current in $3\\ \\Omega$ branch of a Wheatstone Bridge in the circuit shown in the figure."
assert old_prefix_2 in ce_content, "Target prefix string 2 not found"
ce_content = ce_content.replace(old_prefix_2, new_prefix_2)

old_prefix_3 = "(a) (i) Derive the condition for which a Wheatstone Bridge is balanced."
new_prefix_3 = "Derive the condition for which a Wheatstone Bridge is balanced."
assert old_prefix_3 in ce_content, "Target prefix string 3 not found"
ce_content = ce_content.replace(old_prefix_3, new_prefix_3)

old_prefix_4 = "(ii) Determine the current in $3\\;\\Omega$ branch of a Wheatstone Bridge in the circuit shown in the figure."
new_prefix_4 = "Determine the current in $3\\;\\Omega$ branch of a Wheatstone Bridge in the circuit shown in the figure."
assert old_prefix_4 in ce_content, "Target prefix string 4 not found"
ce_content = ce_content.replace(old_prefix_4, new_prefix_4)

# Fix 5: Cloned URLs in current-electricity links
ce_content = re.sub(r'/q/the-current-the-resistor-(1854|1905|1945)/', '/q/the-current-the-resistor-99a924/', ce_content)
ce_content = re.sub(r'/q/the-threshold-voltage-silicon-diode-operated-(4598|4670|4708)/', '/q/the-threshold-voltage-silicon-diode-operated-this-a605c8/', ce_content)

with open(curr_elec_path, "w", encoding="utf-8") as f:
    f.write(ce_content)
print("[OK] Updated cbse-12/physics/current-electricity/index.html")

# -----------------------------------------------------------------------------
# 2. UPDATE vercel.json WITH 301 REDIRECTS FOR CLONED QUESTION URLS
# -----------------------------------------------------------------------------
vercel_path = os.path.join(ROOT, "vercel.json")
with open(vercel_path, "r", encoding="utf-8") as f:
    vercel_data = json.load(f)

# Ensure redirects exist
new_redirects = [
    {
        "source": "/q/the-threshold-voltage-silicon-diode-operated-:id/",
        "destination": "/q/the-threshold-voltage-silicon-diode-operated-this-a605c8/",
        "permanent": True
    },
    {
        "source": "/q/the-threshold-voltage-silicon-diode-operated-:id",
        "destination": "/q/the-threshold-voltage-silicon-diode-operated-this-a605c8/",
        "permanent": True
    },
    {
        "source": "/q/the-current-the-resistor-:id/",
        "destination": "/q/the-current-the-resistor-99a924/",
        "permanent": True
    },
    {
        "source": "/q/the-current-the-resistor-:id",
        "destination": "/q/the-current-the-resistor-99a924/",
        "permanent": True
    }
]

existing_sources = {r.get("source") for r in vercel_data.get("redirects", [])}
for r in new_redirects:
    if r["source"] not in existing_sources:
        vercel_data["redirects"].append(r)

with open(vercel_path, "w", encoding="utf-8") as f:
    json.dump(vercel_data, f, indent=2)
print("[OK] Updated vercel.json with canonical redirects")

# -----------------------------------------------------------------------------
# 3. PRE-RENDER SYLLABUS BLUEPRINT IN syllabus/index.html
# -----------------------------------------------------------------------------
syllabus_html_path = os.path.join(ROOT, "syllabus", "index.html")
syllabus_json_path = os.path.join(ROOT, "data", "syllabus_cbse_12.json")

with open(syllabus_json_path, "r", encoding="utf-8") as f:
    syllabus_data = json.load(f)

with open(syllabus_html_path, "r", encoding="utf-8") as f:
    syl_content = f.read()

# Render CBSE 12 Chemistry default view
chem_data = syllabus_data.get("Chemistry", {})
code = chem_data.get("code", "043")
theory_marks = chem_data.get("theory_marks", 70)
internal_marks = chem_data.get("internal_marks", 30)
chapters = chem_data.get("chapters", [])

# Group by Unit
units_map = {}
for ch in chapters:
    u_no = ch.get("unit_no", "I")
    u_name = ch.get("unit_name", ch.get("chapter", ""))
    u_key = f"{u_no}: {u_name}"
    if u_key not in units_map:
        units_map[u_key] = {"unit": u_no, "name": u_name, "chapters": []}
    units_map[u_key]["chapters"].append(ch)

rendered_ssr = f'''
      <!-- Pre-rendered Static SSR Content for Fast First Paint & Search Engines -->
      <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:20px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">CBSE Class 12 Chemistry (Code {code})</h2>
          <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">Official Examination Blueprint: {theory_marks} Marks Theory + {internal_marks} Marks Practical/Internal.</p>
        </div>
        <div style="display:flex; gap:8px;">
          <a href="/practice/?exam=cbse&subject=Chemistry" class="btn-action-pyq">⚡ Practice All Chemistry PYQs ➔</a>
        </div>
      </div>
'''

for u_key, u in units_map.items():
    unit_total = sum(c.get("theory_marks", 0) for c in u["chapters"])
    unit_badge = f"{unit_total} Marks" if unit_total > 0 else "Official Unit"
    rendered_ssr += f'''
      <div class="unit-section">
        <div class="unit-header">
          <span class="unit-title">📖 Unit {u_key}</span>
          <span class="unit-marks-badge">{unit_badge}</span>
        </div>
        <div>
'''
    for ch in u["chapters"]:
        ch_name = ch.get("chapter", "")
        typology = ch.get("typology", "Derivations, Numerical Problems, Conceptual Reasoning")
        ch_marks = ch.get("theory_marks", 0)
        jee_o = ch.get("jee_overlap", "")
        neet_o = ch.get("neet_overlap", "")
        bitsat_o = ch.get("bitsat_overlap", "")
        topics = ch.get("official_topics", "")
        
        overlap_chips = ""
        if jee_o: overlap_chips += f'<span class="overlap-chip">JEE Main: <strong>{jee_o}</strong></span>'
        if neet_o: overlap_chips += f'<span class="overlap-chip">NEET UG: <strong>{neet_o}</strong></span>'
        if bitsat_o: overlap_chips += f'<span class="overlap-chip">BITSAT: <strong>{bitsat_o}</strong></span>'

        topics_markup = ""
        if topics:
            topics_markup = f'''
                <details class="topics-collapse">
                  <summary>▶ Prescribed Official Syllabus Topics (cbseacademic.nic.in)</summary>
                  <div class="topics-body">
                    {topics}
                  </div>
                </details>'''

        rendered_ssr += f'''
          <div class="chapter-row">
            <div class="chapter-meta-bar">
              <div class="chapter-title-group">
                <h3>{ch_name}</h3>
                <div class="chapter-typology-tag"><strong>High-Probability Typology:</strong> {typology}</div>
              </div>
              <span class="chapter-marks-pill">{ch_marks} Theory Marks</span>
            </div>

            <div class="cross-exam-box">
              <span class="cross-exam-title">🎯 Entrance Overlap:</span>
              {overlap_chips}
            </div>
            {topics_markup}
          </div>
'''
    rendered_ssr += '''
        </div>
      </div>
'''

# Official CBSE Academic Citation Footer
citation_footer = '''
      <div class="official-citation-footer" style="margin-top:28px; padding:18px 22px; background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); font-size:13px; color:var(--text-muted); line-height:1.6;">
        <div style="font-weight:700; color:var(--text); margin-bottom:6px;">🏛️ Official CBSE Academic Reference & Curriculum Attribution:</div>
        <div>All chapter unit boundaries, theory mark allocations, and question typologies are directly aligned with the official CBSE Senior Secondary Curriculum Notification (Circular No. Acad-39/2025) published by the Central Board of Secondary Education. For official source curriculum syllabi and sample question papers, visit the official portal at <a href="https://cbseacademic.nic.in/curriculum_2026.html" target="_blank" rel="noopener" style="color:var(--accent); text-decoration:underline; font-weight:600;">cbseacademic.nic.in</a>.</div>
      </div>
'''
rendered_ssr += citation_footer

container_regex = r'<div id="blueprintContainer">\s*<!-- Dynamically populated -->\s*</div>'
if re.search(container_regex, syl_content):
    syl_content = re.sub(container_regex, f'<div id="blueprintContainer">{rendered_ssr}</div>', syl_content)
else:
    # If already modified or different placeholder
    syl_content = re.sub(r'<div id="blueprintContainer">[\s\S]*?</div>', f'<div id="blueprintContainer">{rendered_ssr}</div>', syl_content, count=1)

with open(syllabus_html_path, "w", encoding="utf-8") as f:
    f.write(syl_content)
print("[OK] Pre-rendered default blueprint and official citation in syllabus/index.html")
