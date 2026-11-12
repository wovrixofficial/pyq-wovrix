import json
import re

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/syllabus_cbse_12.json', 'r', encoding='utf-8') as f:
    cbse12 = json.load(f)

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/syllabus/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Generate Static SSR Table for Chemistry, Physics, and Mathematics
ssr_html = """
      <!-- Static SSR Content for Search Engines & Fast First Paint -->
      <div class="official-citation-box" style="background:var(--surface); border:1px solid var(--border); border-left:4px solid var(--accent); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:24px;">
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
          <span style="font-size:16px;">📜</span>
          <strong style="font-size:14px; color:var(--text);">Official Statutory Curriculum Citation</strong>
          <span style="font-size:11px; font-weight:700; color:#16a34a; background:#dcfce7; padding:2px 8px; border-radius:4px;">Verified 2025–2026</span>
        </div>
        <p style="font-size:13px; color:var(--text-muted); line-height:1.6; margin:0;">
          All syllabus allocations, prescribed topics, and mark distributions are sourced directly from official statutory board releases:
          <br>• <strong>CBSE Class 12:</strong> Central Board of Secondary Education Delhi Circular No. <strong>Acad-39/2025</strong> (<a href="https://cbseacademic.nic.in/curriculum_2026.html" target="_blank" rel="noopener" style="color:var(--accent);">cbseacademic.nic.in</a> Senior School Curriculum).
          <br>• <strong>NEET UG (Medical):</strong> National Testing Agency (NTA) official Information Bulletin 2025–2026 (<a href="https://exams.nta.ac.in/NEET/" target="_blank" rel="noopener" style="color:var(--accent);">exams.nta.ac.in/NEET</a>) aligning with NMC guidelines.
          <br>• <strong>JEE Main:</strong> NTA JEE (Main) official Information Bulletin 2025–2026 (<a href="https://jeemain.nta.nic.in/" target="_blank" rel="noopener" style="color:var(--accent);">jeemain.nta.nic.in</a>).
        </p>
      </div>
"""

for subj in ["Chemistry", "Physics", "Mathematics"]:
    if subj not in cbse12:
        continue
    data = cbse12[subj]
    code = data.get('code', '')
    theory = data.get('theory_marks', 70)
    internal = data.get('internal_marks', 30)
    total = data.get('total_marks', 100)
    chapters = data.get('chapters', [])

    ssr_html += f"""
      <div class="subject-blueprint-section" style="margin-bottom:32px;">
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <div>
            <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">CBSE Class 12 {subj} (Subject Code {code})</h2>
            <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">Official Examination Blueprint: {theory} Marks Theory + {internal} Marks Practical/Internal = {total} Marks.</p>
          </div>
          <div style="display:flex; gap:8px;">
            <a href="/practice/?exam=cbse&subject={subj}" class="btn-action-pyq" style="background:var(--accent); color:#ffffff; padding:8px 14px; border-radius:6px; font-size:12px; font-weight:700; text-decoration:none;">⚡ Practice All {subj} PYQs ➔</a>
          </div>
        </div>

        <!-- Semantic Accessible Marks Weightage Table for Google Indexing -->
        <div style="overflow-x:auto; margin-bottom:16px;">
          <table style="width:100%; border-collapse:collapse; background:var(--surface); border:1px solid var(--border); border-radius:8px; font-size:13px;">
            <thead>
              <tr style="background:var(--surface-hover); border-bottom:1px solid var(--border); text-align:left;">
                <th style="padding:10px 14px; color:var(--text); font-weight:700;">Unit</th>
                <th style="padding:10px 14px; color:var(--text); font-weight:700;">Chapter</th>
                <th style="padding:10px 14px; color:var(--text); font-weight:700; text-align:center;">Theory Marks</th>
                <th style="padding:10px 14px; color:var(--text); font-weight:700;">Expected Typology</th>
                <th style="padding:10px 14px; color:var(--text); font-weight:700;">Entrance Overlap</th>
              </tr>
            </thead>
            <tbody>
    """
    for ch in chapters:
        u_no = ch.get('unit_no', '—')
        ch_name = ch.get('chapter', '')
        marks = ch.get('theory_marks', '—')
        typology = ch.get('typology', 'Numerical / Concept / Derivation')
        jee = ch.get('jee_overlap', '')
        neet = ch.get('neet_overlap', '')
        overlap_str = f"JEE: {jee}" if jee else ""
        if neet:
            overlap_str += f" | NEET: {neet}" if overlap_str else f"NEET: {neet}"
        if not overlap_str:
            overlap_str = "Core NCERT"

        ssr_html += f"""
              <tr style="border-bottom:1px solid var(--border);">
                <td style="padding:10px 14px; color:var(--text-muted); font-weight:600;">{u_no}</td>
                <td style="padding:10px 14px; color:var(--text); font-weight:700;">{ch_name}</td>
                <td style="padding:10px 14px; color:var(--accent); font-weight:800; text-align:center;">{marks}</td>
                <td style="padding:10px 14px; color:var(--text-muted);">{typology}</td>
                <td style="padding:10px 14px; color:var(--text-muted);"><span style="background:var(--surface-hover); padding:2px 6px; border-radius:4px; font-size:11px; font-weight:600;">{overlap_str}</span></td>
              </tr>
        """

    ssr_html += """
            </tbody>
          </table>
        </div>
      </div>
    """

# Replace content inside blueprintContainer in syllabus/index.html
# Find <div id="blueprintContainer">...</div>
pattern = r'(<div id="blueprintContainer">)([\s\S]*?)(</div>\s*</main>)'
new_html = re.sub(pattern, rf'\1\n{ssr_html}\n    \3', html)

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/syllabus/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("[SUCCESS] Injected comprehensive static SSR tables and citations into syllabus/index.html")
