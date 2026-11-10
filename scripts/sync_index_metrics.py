import json
import os
import re

INDEX_PATH = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\index.html"
DATA_DIR = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\data"

# 1. Compute exact ground-truth stats from data files
subject_files = [
    ('Physics', 'cbse_physics.json'),
    ('Chemistry', 'cbse_chemistry.json'),
    ('Mathematics', 'cbse_mathematics.json')
]

chapter_data = {}
subject_totals = {}

for sub, fn in subject_files:
    fpath = os.path.join(DATA_DIR, fn)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    ch_map = {}
    for d in data:
        ch = d.get('chapter_name', 'UNKNOWN').strip()
        if ch not in ch_map:
            ch_map[ch] = {'appearances': 0, 'distinct_sigs': set()}
        ch_map[ch]['appearances'] += 1
        sig = d.get('signature', d.get('text', '')).strip()
        ch_map[ch]['distinct_sigs'].add(sig)
    
    chapter_data[sub] = {
        ch: {
            'appearances': v['appearances'],
            'distinct': len(v['distinct_sigs'])
        }
        for ch, v in ch_map.items()
    }
    
    subject_totals[sub] = {
        'appearances': len(data),
        'distinct': sum(len(v['distinct_sigs']) for v in ch_map.values())
    }

total_cbse_appearances = sum(v['appearances'] for v in subject_totals.values())
total_cbse_distinct = sum(v['distinct'] for v in subject_totals.values())

print(f"CBSE Total Appearances: {total_cbse_appearances} (Expected 10279)")
print(f"CBSE Total Distinct: {total_cbse_distinct} (Expected 7761)")
for sub, t in subject_totals.items():
    print(f"  {sub}: {t['distinct']} distinct out of {t['appearances']} appearances")

# 2. Read index.html
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 3. Update Hero text and chips
old_hero_lead = re.search(r'<p class="hero-editorial-lead">[\s\S]*?</p>', html).group(0)
new_hero_lead = f'''<p class="hero-editorial-lead">
          <strong>10,279 official CBSE board question appearances</strong> (deduplicated into <strong>7,761 canonical PYQs</strong>) across 5 years (2022–2026) and <strong>2,060 verified NEET UG problems</strong> across 11 years (2016–2026). Pure NCERT alignment, multi-year frequency filters, and zero distractions.
        </p>'''
html = html.replace(old_hero_lead, new_hero_lead)

# Replace portal chips
html = re.sub(
    r'<span class="portal-chip">CBSE 12 PCM \(\d+[\d,]*\s*Qs\)</span>',
    f'<span class="portal-chip">CBSE 12 PCM (10,279 Qs • 7,761 Canonical)</span>',
    html
)

# 4. Update JSON-LD Schema
old_schema_ans = re.search(r'"acceptedAnswer":\s*\{\s*"@type":\s*"Answer",\s*"text":\s*"Learnosha includes 5 complete CBSE Class 12 board cycles[\s\S]*?"\s*\}', html)
if old_schema_ans:
    new_schema_ans = f'''"acceptedAnswer": {{
          "@type": "Answer",
          "text": "Learnosha includes 5 complete CBSE Class 12 board cycles (2022–2026) comprising 10,279 past question appearances deduplicated into 7,761 canonical NCERT-aligned questions, alongside 11 NEET UG national cycles (2016–2026) with 2,060 verified questions."
        }}'''
    html = html.replace(old_schema_ans.group(0), new_schema_ans)

# Update JSON-LD rubrics question & answer
old_schema_rubric = re.search(r'\{\s*"@type":\s*"Question",\s*"name":\s*"Are the step-marking rubrics official\?",[\s\S]*?\}', html)
if old_schema_rubric:
    new_schema_rubric = '''{
        "@type": "Question",
        "name": "How do the step-marking schemes work?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Our step-marking schemes follow CBSE's official marking pattern. Rather than offering bare final answers, solutions are broken down into discrete steps (formula statement, substitution, derivation/calculation, and final answer with proper units or concluding statement), showing exactly how evaluators allocate marks across 1M, 2M, 3M, 4M case-based, and 5M questions."
        }
      }'''
    html = html.replace(old_schema_rubric.group(0), new_schema_rubric)

# 5. Update Subject Header Badges
html = re.sub(
    r'<h2>Physics</h2>\s*<span class="subj-badge">[\s\S]*?</span>',
    f'<h2>Physics</h2>\n            <span class="subj-badge">{subject_totals["Physics"]["appearances"]:,} Questions ({subject_totals["Physics"]["distinct"]:,} Distinct)</span>',
    html
)
html = re.sub(
    r'<h2>Chemistry</h2>\s*<span class="subj-badge">[\s\S]*?</span>',
    f'<h2>Chemistry</h2>\n            <span class="subj-badge">{subject_totals["Chemistry"]["appearances"]:,} Questions ({subject_totals["Chemistry"]["distinct"]:,} Distinct)</span>',
    html
)
html = re.sub(
    r'<h2>Mathematics</h2>\s*<span class="subj-badge">[\s\S]*?</span>',
    f'<h2>Mathematics</h2>\n            <span class="subj-badge">{subject_totals["Mathematics"]["appearances"]:,} Questions ({subject_totals["Mathematics"]["distinct"]:,} Distinct)</span>',
    html
)

# 6. Update all 37 chapter cards
# Helper mapping to match chapter card titles with dataset names
name_aliases = {
    'Semiconductor Electronics': 'Semiconductor Electronics: Materials, Devices and Simple Circuits',
    'Semiconductor Electronics: Materials, Devices and Simple Circuits': 'Semiconductor Electronics: Materials, Devices and Simple Circuits',
    'The d- and f-Block Elements': 'The d- and f-Block Elements',
    'd- and f-Block Elements': 'The d- and f-Block Elements'
}

def replace_chapter_meta(match):
    full_card = match.group(0)
    h3_match = re.search(r'<h3>(.*?)</h3>', full_card)
    if not h3_match:
        return full_card
    title = h3_match.group(1).strip()
    lookup_title = name_aliases.get(title, title)
    
    # Find which subject this belongs to
    found_stats = None
    for sub in ['Physics', 'Chemistry', 'Mathematics']:
        if lookup_title in chapter_data[sub]:
            found_stats = chapter_data[sub][lookup_title]
            break
        # Case insensitive fallback
        for k, v in chapter_data[sub].items():
            if k.lower() == lookup_title.lower():
                found_stats = v
                break
        if found_stats:
            break
            
    if not found_stats:
        print(f"WARNING: Could not find stats for chapter '{title}'")
        return full_card
        
    distinct_cnt = found_stats['distinct']
    app_cnt = found_stats['appearances']
    
    new_meta = f'<span class="ch-meta">{distinct_cnt} distinct problems • {app_cnt} appearances</span>'
    updated_card = re.sub(r'<span class="ch-meta">[\s\S]*?</span>', new_meta, full_card)
    return updated_card

chapter_card_pattern = re.compile(r'<a href="/cbse-12/[^"]+/" class="chapter-card">[\s\S]*?</a>')
html = chapter_card_pattern.sub(replace_chapter_meta, html)

# 7. Update FAQ Accordion
# FAQ Question 1
html = re.sub(
    r'<div class="faq-item">\s*<button class="faq-question"[^>]*>\s*<span>How many years of CBSE Class 12 past papers are included\?</span>[\s\S]*?</div>\s*</div>',
    f'''<div class="faq-item">
          <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
            <span>How many years of CBSE Class 12 past papers are included?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer">
            Learnosha includes 5 complete CBSE Class 12 board cycles from 2022 through 2026. Across Physics, Chemistry, and Mathematics, this encompasses 10,279 total question appearances across all Delhi, All India, and Foreign regional parallel sets, deduplicated into 7,761 canonical NCERT-aligned questions. For medical entrance preparation, our separate NEET UG archive covers 11 complete national cycles (2016–2026) with 2,060 questions.
          </div>
        </div>''',
    html
)

# FAQ Question 2 (Repeat Radar)
html = re.sub(
    r'<div class="faq-item">\s*<button class="faq-question"[^>]*>\s*<span>How does the Repeat Radar identify recurring questions\?</span>[\s\S]*?</div>\s*</div>',
    '''<div class="faq-item">
          <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
            <span>How does the Repeat Radar identify recurring questions?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer">
            Our algorithmic repeat detection analyzes mathematical formula structures, question text signatures, and core concept keywords across board years. We isolate questions that have appeared across multiple board years or parallel sets (such as Wheatstone bridge derivations or ray optics proofs) to help students prioritize high-frequency topics.
          </div>
        </div>''',
    html
)

# FAQ Question 3 (Rubrics)
html = re.sub(
    r'<div class="faq-item">\s*<button class="faq-question"[^>]*>\s*<span>Are the step-marking rubrics official\?</span>[\s\S]*?</div>\s*</div>',
    '''<div class="faq-item">
          <button class="faq-question" onclick="this.parentElement.classList.toggle('open')">
            <span>How do the step-marking schemes work?</span>
            <span class="faq-icon">▼</span>
          </button>
          <div class="faq-answer">
            Our step-marking schemes follow CBSE's official marking pattern. Rather than offering bare final answers, solutions are broken into discrete evaluative steps (given data, formula/theorem statement, substitution, derivation/calculation, and final answer with correct units or concluding statement), reflecting how marks are awarded across 1M, 2M, 3M, 4M case studies, and 5M long-answer questions in Physics, Chemistry, and Mathematics.
          </div>
        </div>''',
    html
)

# 8. Update Footer Links
# Replace Medical Entrance identical links
old_neet_footer = re.search(r'<div class="footer-col">\s*<span class="footer-col-heading">Medical Entrance</span>[\s\S]*?</ul>\s*</div>', html)
if old_neet_footer:
    new_neet_footer = '''<div class="footer-col">
        <span class="footer-col-heading">Medical Entrance</span>
        <ul class="footer-links-list">
          <li><a href="/practice/?exam=neet">NEET UG 11-Year Archive (2016–2026)</a></li>
          <li><a href="/practice/?exam=neet&subject=Physics">NEET Physics (2016–2026)</a></li>
          <li><a href="/practice/?exam=neet&subject=Chemistry">NEET Chemistry (2016–2026)</a></li>
          <li><a href="/practice/?exam=neet&subject=Botany">NEET Botany (2016–2026)</a></li>
          <li><a href="/practice/?exam=neet&subject=Zoology">NEET Zoology (2016–2026)</a></li>
        </ul>
      </div>'''
    html = html.replace(old_neet_footer.group(0), new_neet_footer)

# Replace Parallel Set Comparison link in Study Tools
html = html.replace(
    '<li><a href="/practice/">Parallel Set Comparison</a></li>',
    '<li><a href="/repeated/">Parallel Set & Repeat Radar</a></li>'
)

# 9. Save updated index.html
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html fully updated and synchronized!")
