import json
import glob

for p in glob.glob('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/*.json'):
    if 'syllabus' in p or 'topics' in p:
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            continue
        odd_dollar = []
        for q in data:
            t = q.get('text', '')
            if t and t.count('$') % 2 != 0:
                odd_dollar.append(q['id'])
        if odd_dollar:
            print(f"{p.split('/')[-1]}: {len(odd_dollar)} questions with unclosed $ -> {odd_dollar[:10]}")
    except Exception as e:
        pass
