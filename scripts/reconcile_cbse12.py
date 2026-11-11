import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

curr_elec_file = os.path.join(ROOT, "cbse-12", "physics", "current-electricity", "index.html")
semi_file = os.path.join(ROOT, "cbse-12", "physics", "semiconductor-electronics-materials-devices-and-simple-circuits", "index.html")
ac_file = os.path.join(ROOT, "cbse-12", "physics", "alternating-current", "index.html")
index_file = os.path.join(ROOT, "index.html")

with open(curr_elec_file, "r", encoding="utf-8") as f:
    ce_html = f.read()

# Split strictly by <article class="card question-card">
parts = ce_html.split('<article class="card question-card">')
header = parts[0]
raw_cards = parts[1:]
print(f"Initial cards count in current-electricity: {len(raw_cards)}")

new_cards = []
semi_cards = []
ac_cards = []

# IDs to remove from Current Electricity
diodes_to_remove = {"218", "4598", "4670", "4708"}
ac_to_remove = {"3674"}
duplicates_to_remove = {"1905", "1945", "457", "2073", "5531", "2175", "2216", "2217"}

for raw in raw_cards:
    full_card = '<article class="card question-card">' + raw
    # Extract question ID from practice link: href="/practice/?q=1854#card_1854"
    m_qid = re.search(r'href="/practice/\?q=(\d+)#card_\1"', full_card)
    if not m_qid:
        new_cards.append(full_card)
        continue

    qid = m_qid.group(1)

    # Diodes
    if qid in diodes_to_remove:
        if qid in ("218", "4598"):
            # Prepare card for semiconductor page
            clean_card = re.sub(r'<span class="tag tag-chapter"[\s\S]*?</span>', '', full_card)
            if qid == "4598":
                clean_card = re.sub(
                    r'<span class="repeat-pill\s*">[\s\S]*?</span>',
                    '<span class="repeat-pill" style="background:#fee2e2; color:#ef4444; border:1px solid #fca5a5; font-weight:700;">🔥 Appeared in 3 Board Sets (2025)</span>',
                    clean_card
                )
            semi_cards.append(clean_card)
        continue

    # AC
    if qid in ac_to_remove:
        clean_card = re.sub(r'<span class="tag tag-chapter"[\s\S]*?</span>', '', full_card)
        ac_cards.append(clean_card)
        continue

    # Duplicate cards to drop
    if qid in duplicates_to_remove:
        continue

    # Cards to modify
    if qid == "1854":
        full_card = re.sub(
            r'<span class="repeat-pill\s*">[\s\S]*?</span>',
            '<span class="repeat-pill" style="background:#fee2e2; color:#ef4444; border:1px solid #fca5a5; font-weight:700;">🔥 Appeared in 3 Board Sets (2025 Series 55-2)</span>',
            full_card
        )
    elif qid == "575":
        full_card = re.sub(
            r'<span class="repeat-pill\s*">[\s\S]*?</span>',
            '<span class="repeat-pill" style="background:#fee2e2; color:#ef4444; border:1px solid #fca5a5; font-weight:700;">🔥 Appeared in 3 Board Sets (2024, 2025 Series 55)</span>',
            full_card
        )
    elif qid == "4303":
        full_card = re.sub(
            r'<span class="repeat-pill\s*">[\s\S]*?</span>',
            '<span class="repeat-pill" style="background:#fee2e2; color:#ef4444; border:1px solid #fca5a5; font-weight:700;">🔥 Appeared in Multiple Board Sets</span>',
            full_card
        )
    elif qid == "2174":
        combined_text = """(a) (i) Derive the condition for which a Wheatstone Bridge is balanced.
(ii) Determine the current in $3\\ \\Omega$ branch of a Wheatstone Bridge in the circuit shown in the figure."""
        repl_str = f'<div class="question-text math-content">\n                    {combined_text}\n                  </div>'
        full_card = re.sub(
            r'<div class="question-text math-content">[\s\S]*?</div>',
            lambda _: repl_str,
            full_card
        )

    new_cards.append(full_card)

print(f"Final deduplicated cards count in current-electricity: {len(new_cards)}")

# Reconstruct current-electricity HTML
# The last card in raw_cards ends with closing tags of the container: </main> etc.
# But since we kept the last card's tail, we can join:
# Actually: `header + "".join(new_cards)` works if the last card contains its original trailing container markup!
# Let's inspect what follows the last card:
last_raw = raw_cards[-1]
# Everything after the last </article> is trailing markup
trailing_idx = last_raw.rfind('</article>')
trailing_html = last_raw[trailing_idx + len('</article>'):]

# Let's clean the cards so each ends with </article>\n\n
cleaned_joined_cards = ""
for c in new_cards:
    art_end = c.rfind('</article>')
    cleaned_joined_cards += c[:art_end + len('</article>')] + "\n\n"

ce_html_new = header + cleaned_joined_cards + trailing_html

# Update chapter hero numbers in current-electricity/index.html
ce_html_new = re.sub(
    r'<div class="hero-stats">[\s\S]*?</div>',
    f'''<div class="hero-stats">
        <span><strong>{len(new_cards)}</strong> Distinct Problems</span>
        <span>•</span>
        <span><strong>171</strong> Board Paper Sets (2026-2015)</span>
        <span>•</span>
        <span><strong>100%</strong> NCERT Derivations & KaTeX</span>
      </div>''',
    ce_html_new,
    count=1
)
ce_html_new = re.sub(
    r'<h2>Board Questions \(\d+ Distinct Problems\)</h2>',
    f'<h2>Board Questions ({len(new_cards)} Distinct Problems)</h2>',
    ce_html_new
)

# Footer legal disclaimer
new_disclaimer = 'Disclaimer: Independent study resource providing NCERT-aligned past paper revision, repeat pattern analytics, and step-by-step solutions for CBSE and competitive exams.'
old_disclaimer_pattern = r'Official past examination papers reproduced under fair dealing for educational non-commercial study[^\.]*\.'
ce_html_new = re.sub(old_disclaimer_pattern, new_disclaimer, ce_html_new)
ce_html_new = re.sub(r'Free, No-Login Educational Past Paper Archive\.', new_disclaimer, ce_html_new)

with open(curr_elec_file, "w", encoding="utf-8") as f:
    f.write(ce_html_new)
print(f"[OK] Saved updated {curr_elec_file}")

# RELOCATE TO SEMICONDUCTOR
if os.path.exists(semi_file) and semi_cards:
    with open(semi_file, "r", encoding="utf-8") as f:
        semi_html = f.read()
    to_add = [c for c in semi_cards if 'href="/practice/?q=4598#card_4598"' not in semi_html or 'href="/practice/?q=218#card_218"' not in semi_html]
    if to_add:
        semi_html = semi_html.replace('</main>', "\n".join(to_add) + '\n</main>')
        with open(semi_file, "w", encoding="utf-8") as f:
            f.write(semi_html)
        print(f"[OK] Added {len(to_add)} relocated cards to semiconductor-electronics")

# RELOCATE TO ALTERNATING CURRENT
if os.path.exists(ac_file) and ac_cards:
    with open(ac_file, "r", encoding="utf-8") as f:
        ac_html = f.read()
    if 'href="/practice/?q=3674#card_3674"' not in ac_html:
        ac_html = ac_html.replace('</main>', "\n".join(ac_cards) + '\n</main>')
        with open(ac_file, "w", encoding="utf-8") as f:
            f.write(ac_html)
        print(f"[OK] Added relocated card 3674 to alternating-current")

# UPDATE HOMEPAGE (index.html)
if os.path.exists(index_file):
    with open(index_file, "r", encoding="utf-8") as f:
        idx_html = f.read()

    # Reconcile count: 24,994 -> 25,006 Questions
    idx_html = idx_html.replace("24,994 Questions", "25,006 Questions")
    idx_html = idx_html.replace("24,994 questions", "25,006 questions")
    idx_html = idx_html.replace("24,994", "25,006")

    # Update Current Electricity line on homepage table
    idx_html = re.sub(
        r'Current Electricity</a>[\s\S]*?</td>\s*<td>\s*<span[^>]*>[^<]*</span>\s*</td>',
        f'Current Electricity</a>\n                <span class="ch-meta-sub">{len(new_cards)} distinct problems • 171 appearances</span>\n              </td>\n              <td>\n                <span class="weight-badge tag-high">7 Theory Marks</span>\n              </td>',
        idx_html
    )

    # Future-proof legal disclaimer in footer
    idx_html = re.sub(old_disclaimer_pattern, new_disclaimer, idx_html)
    idx_html = re.sub(r'Free, No-Login Educational Past Paper Archive\.', new_disclaimer, idx_html)

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(idx_html)
    print(f"[OK] Updated {index_file} with 25,006 questions and reconciled stats")

print("=== True Reconciliation Complete ===")
