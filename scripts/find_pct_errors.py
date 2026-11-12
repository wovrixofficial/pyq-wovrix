import json, re

for fname in ['cbse_chemistry.json', 'cbse_mathematics.json', 'cbse_physics.json', 'neet_all.json', 'jee_adv_all.json']:
    path = f'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {fname} ===")
    for q in data:
        t = q.get('text', '')
        m = re.findall(r'\$[^\$]*?\d+%\$|\$[^\$]*?\d+%\s', t)
        if m:
            print(f"ID {q.get('id')}: matches={m} | snippet={t[:80].replace(chr(10), ' ')}")
