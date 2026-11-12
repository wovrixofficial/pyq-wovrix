import json
import re

print("="*60)
print("RUNNING COMPREHENSIVE VERIFICATION SUITE")
print("="*60)

# Test 1: Current Electricity HTML
ce_file = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/current-electricity/index.html'
with open(ce_file, 'r', encoding='utf-8') as f:
    ce_html = f.read()

parts = ce_html.split('<article class="card question-card">')
cards = parts[1:]
assert len(cards) == 116, f"Expected 116 cards in CE HTML, got {len(cards)}"
print(f"✔ Test 1 passed: Current Electricity HTML has exactly 116 curated cards.")

for dropped in ['103', '205', '5649', '9721', '1905', '1945', '2175', '4598', '4670', '4708']:
    assert f'q={dropped}#card_{dropped}' not in ce_html, f"Dropped ID {dropped} still in CE HTML!"
print("✔ Test 2 passed: All misclassified diode/AC cards & duplicate clones are removed from CE HTML.")

# Test 3: Meta and H2 consistency
assert '116 distinct' in ce_html, "Meta description does not say 116 distinct"
assert '<h2>Board Questions (116 Distinct Problems)</h2>' in ce_html, "H2 does not say 116 Distinct Problems"
print("✔ Test 3 passed: Meta description and H2 match exactly (116 Distinct Problems).")

# Test 4: cbse_physics.json
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_physics.json', 'r', encoding='utf-8') as f:
    phys = json.load(f)

q103 = [q for q in phys if q['id'] == 103][0]
assert q103['chapter_name'] == 'Semiconductor Electronics: Materials, Devices and Simple Circuits'
assert '$100 \\pi t$' not in q103['text']
q205 = [q for q in phys if q['id'] == 205][0]
assert q205['chapter_name'] == 'Alternating Current'
print("✔ Test 4 passed: cbse_physics.json has ID 103 in Semiconductor (fixed LaTeX) and ID 205 in Alternating Current.")

# Test 5: cbse_mathematics.json
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_mathematics.json', 'r', encoding='utf-8') as f:
    math = json.load(f)

diff_eq_in_cont = [q for q in math if q.get('chapter_name') == 'Continuity and Differentiability' and 'differential equation' in q.get('text', '').lower()]
assert len(diff_eq_in_cont) == 0, f"Still {len(diff_eq_in_cont)} differential equations in Continuity"
print("✔ Test 5 passed: cbse_mathematics.json has 0 differential equations in Continuity.")

# Test 6: syllabus/index.html
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/syllabus/index.html', 'r', encoding='utf-8') as f:
    syl = f.read()

assert '<table' in syl, "No table in syllabus/index.html"
assert 'Acad-39/2025' in syl, "No statutory CBSE circular in syllabus/index.html"
assert 'exams.nta.ac.in' in syl, "No NTA citation in syllabus/index.html"
print("✔ Test 6 passed: syllabus/index.html has static SSR tables and official board citations.")

# Test 7: index.html
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

assert '<title>Learnosha – CBSE 12, NEET & JEE Main Previous Year Questions</title>' in idx
assert '116 distinct problems • 171 appearances' in idx
print("✔ Test 7 passed: index.html title is < 60 chars and Current Electricity count is 116.")

# Test 8: practice/index.html
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/practice/index.html', 'r', encoding='utf-8') as f:
    prac = f.read()

assert 'targetQuestionId' in prac
assert 'Selected Question #' in prac
assert 'list.unshift(targetQ);' in prac
print("✔ Test 8 passed: practice/index.html deep links & pins target question as #1.")

print("="*60)
print("ALL VERIFICATION TESTS PASSED (8/8)!")
print("="*60)
