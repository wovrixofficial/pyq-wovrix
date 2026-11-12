import json
import glob
import re

for p in glob.glob('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/*.json'):
    if 'syllabus' in p or 'topics' in p:
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            continue
        
        pi_count = 0
        pct_count = 0
        tab_count = 0
        for q in data:
            t = q.get('text', '')
            if not t:
                continue
            if '$100 \\pi t$' in t:
                pi_count += 1
            if re.search(r'\$[^\$]*?\d+%\$', t) or re.search(r'\$[^\$]*?\d+%\s', t):
                pct_count += 1
            if '\text{' in t or '\t' in t:
                tab_count += 1

        print(f"{p.split('/')[-1]}: pi_errors={pi_count}, pct_errors={pct_count}, tab_errors={tab_count}")
    except Exception as e:
        print(f"Error reading {p}: {e}")
