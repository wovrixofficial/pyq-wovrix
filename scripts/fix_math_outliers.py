import json

json_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_mathematics.json'
with open(json_path, 'r', encoding='utf-8') as f:
    math = json.load(f)

print(f"Total math questions: {len(math)}")

cont_diff_eq = []
for q in math:
    if q.get('chapter_name') == 'Continuity and Differentiability':
        t = q.get('text', '').lower()
        # Differential equations
        if ('differential equation' in t or 'integrating factor' in t or 'general solution' in t or 'order and degree' in t or 'order and the degree' in t):
            cont_diff_eq.append(q)

print(f"Found {len(cont_diff_eq)} Differential Equations questions in Continuity and Differentiability")
for q in cont_diff_eq[:5]:
    print(f"  ID {q['id']}: {q['text'][:80].replace(chr(10), ' ')}")

# Perform reclassification
for q in cont_diff_eq:
    q['chapter_name'] = 'Differential Equations'
    q['chapter_number'] = 9
    q['subtopic'] = 'Differential Equations & Degree'
    q['subtopic_slug'] = 'diff-equations-order-degree'

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(math, f, indent=2, ensure_ascii=False)

print(f"[SUCCESS] Reclassified {len(cont_diff_eq)} questions to Differential Equations.")
