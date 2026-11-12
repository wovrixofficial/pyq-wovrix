import json

targets = [
    ('cbse_chemistry.json', [931, 969, 991, 1122, 1152, 2831, 3059, 9945]),
    ('cbse_mathematics.json', [177, 1425, 1571, 4986, 4987, 5003, 6690, 7405]),
    ('cbse_physics.json', [2078, 333, 5846, 7101])
]

for fname, qids in targets:
    with open(f'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/{fname}', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"================ {fname} ================")
    for q in data:
        if q['id'] in qids:
            print(f"ID {q['id']}: count($) = {q.get('text', '').count('$')}")
            print(repr(q.get('text', '')))
