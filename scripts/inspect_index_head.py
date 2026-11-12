with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(min(120, len(lines))):
    l = lines[i]
    if 'title' in l.lower() or 'description' in l.lower():
        print(f"{i+1}: {l.strip()}")
