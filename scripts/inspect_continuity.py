import json
import re

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_mathematics.json', 'r', encoding='utf-8') as f:
    math = json.load(f)

cont_qs = [q for q in math if q.get('chapter_name') == 'Continuity and Differentiability']
print(f"Total in Continuity and Differentiability: {len(cont_qs)}")

# Check for keywords of other chapters
# Applications of Derivatives: increasing, decreasing, tangent, normal, maxima, minima, rate of change
aod_count = 0
integrals_count = 0
diff_eq_count = 0
matrix_count = 0

sample_mis = []
for q in cont_qs:
    t = q.get('text', '').lower()
    if ('strictly increasing' in t or 'strictly decreasing' in t or 'local maxima' in t or 'local minima' in t or 'rate of change of' in t):
        aod_count += 1
        sample_mis.append(('Applications of Derivatives', q['id'], q['text'][:80]))
    elif ('differential equation' in t or 'integrating factor' in t or 'general solution' in t):
        diff_eq_count += 1
        sample_mis.append(('Differential Equations', q['id'], q['text'][:80]))
    elif ('evaluate:' in t or 'integrate' in t or '\\int' in t) and not ('derivative' in t or 'differentiate' in t):
        integrals_count += 1
        sample_mis.append(('Integrals', q['id'], q['text'][:80]))

print(f"Misclassified in Continuity:")
print(f"  Applications of Derivatives: {aod_count}")
print(f"  Differential Equations: {diff_eq_count}")
print(f"  Integrals: {integrals_count}")
print(f"Sample misclassified (first 10):")
for ch, qid, txt in sample_mis[:10]:
    print(f"  -> {ch} [ID {qid}]: {txt.replace(chr(10), ' ')}")
