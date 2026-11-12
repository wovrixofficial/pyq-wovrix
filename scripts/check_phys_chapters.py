import re

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

cards = re.findall(r'<a href="/cbse-12/physics/([^/]+)/"[^>]*>[\s\S]*?<h3>([^<]+)</h3>[\s\S]*?<span class="ch-meta">([^<]+)</span>', h)
for slug, title, meta in cards:
    print(f"{slug:45s} | Meta on homepage: {meta}")
