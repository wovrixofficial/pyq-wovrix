import re

with open('practice/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

subjs = ['Physics', 'Chemistry', 'Botany', 'Zoology']
for s in subjs:
    m = re.search(r'\b' + s + r':\s*\[([\s\S]*?)\]\s*(?:,|\})', text)
    if m:
        names = re.findall(r'name:\s*["\']([^"\']+)["\']', m.group(1))
        print(f'{s} ({len(names)}):', names[:4])
