import glob, json

for p in glob.glob('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/*.json'):
    if 'syllabus' in p or 'topics' in p: continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list) and len(data) > 0 and 'id' in data[0]:
            ids = [q['id'] for q in data if isinstance(q.get('id'), int)]
            if ids:
                print(f"{p:55s} | Count: {len(data):5d} | Min ID: {min(ids):5d} | Max ID: {max(ids):5d}")
    except Exception as e:
        pass
