import json

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_physics.json', 'r', encoding='utf-8') as f:
    phys = json.load(f)

print(f"Total questions: {len(phys)}")
check_ids = [103, 205, 218, 565, 1854, 1905, 1945, 2174, 2175, 4598, 4670, 4708, 5649, 9721]
for cid in check_ids:
    matches = [q for q in phys if q['id'] == cid]
    if matches:
        q = matches[0]
        print(f"ID {cid:4d}: Ch='{q.get('chapter_name')[:25]}' | Text={repr(q.get('text'))[:50]}")
    else:
        print(f"ID {cid:4d}: REMOVED")
