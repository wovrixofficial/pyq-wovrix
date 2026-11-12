import re

ce_file = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/current-electricity/index.html'
with open(ce_file, 'r', encoding='utf-8') as f:
    ce_html = f.read()

parts = ce_html.split('<article class="card question-card">')
header = parts[0]
raw_cards = parts[1:]
print(f"Original cards in current-electricity: {len(raw_cards)}")

remove_qids = {"103", "205", "5649", "9721", "218", "3674", "4598", "4670", "4708", "1905", "1945", "2175"}
kept_cards = []

for raw in raw_cards:
    full_card = '<article class="card question-card">' + raw
    m_qid = re.search(r'href="/practice/\?q=(\d+)#card_\1"', full_card)
    qid = m_qid.group(1) if m_qid else None
    
    if qid in remove_qids:
        print(f"Dropping card {qid} from Current Electricity HTML")
        continue

    # Fix any internal LaTeX or text issues in kept cards
    # ID 565
    if qid == "565":
        full_card = full_card.replace('$20%$', '$20\\%$')
        print("Fixed card 565 percentage format")

    kept_cards.append(full_card)

print(f"Kept cards in current-electricity: {len(kept_cards)}")

# Extract trailing html after last card
last_raw = raw_cards[-1]
trailing_idx = last_raw.rfind('</article>')
trailing_html = last_raw[trailing_idx + len('</article>'):]

cleaned_joined = ""
for c in kept_cards:
    art_end = c.rfind('</article>')
    cleaned_joined += c[:art_end + len('</article>')] + "\n\n"

new_html = header + cleaned_joined + trailing_html

# Update counts in header and meta
new_html = re.sub(
    r'<meta name="description" content="[^"]*"',
    f'<meta name="description" content="All CBSE Class 12 Physics previous year questions for Current Electricity. {len(kept_cards)} distinct problems across 171 board paper sets. Free, no login.">',
    new_html
)
new_html = re.sub(
    r'<meta property="og:description" content="[^"]*"',
    f'<meta property="og:description" content="All CBSE Class 12 Physics previous year questions for Current Electricity. {len(kept_cards)} distinct problems across 171 board paper sets. Free, no login.">',
    new_html
)
new_html = re.sub(
    r'<meta name="twitter:description" content="[^"]*"',
    f'<meta name="twitter:description" content="All CBSE Class 12 Physics previous year questions for Current Electricity. {len(kept_cards)} distinct problems across 171 board paper sets. Free, no login.">',
    new_html
)
new_html = re.sub(
    r'<p class="chapter-desc">[\s\S]*?</p>',
    f'<p class="chapter-desc">\n        {len(kept_cards)} distinct questions across 171 board paper set appearances (2015–2026). Complete with solutions, marks breakdown, and repeated question trends.\n      </p>',
    new_html,
    count=1
)
new_html = re.sub(
    r'<h2>Board Questions \(\d+ Distinct Problems\)</h2>',
    f'<h2>Board Questions ({len(kept_cards)} Distinct Problems)</h2>',
    new_html
)
new_html = re.sub(
    r'<div class="hero-stats">[\s\S]*?</div>',
    f'''<div class="hero-stats">
        <span><strong>{len(kept_cards)}</strong> Distinct Problems</span>
        <span>•</span>
        <span><strong>171</strong> Board Paper Sets (2015–2026)</span>
        <span>•</span>
        <span><strong>100%</strong> NCERT Derivations & KaTeX</span>
      </div>''',
    new_html,
    count=1
)

# Update footer exam pills to add JEE Main and remove Class 10 (Soon)
new_html = new_html.replace(
    '<span class="f-pill">Class 10 (Soon)</span>',
    '<span class="f-pill active">JEE Main</span>'
)

# Replace any formula-sheets link
new_html = new_html.replace('/formula-sheets/', '/syllabus/')
new_html = new_html.replace('/formula-sheets', '/syllabus/')

with open(ce_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"[OK] Saved {ce_file} with {len(kept_cards)} clean cards.")
