import re

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/current-electricity/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

links = re.findall(r'href="/practice/[^"]*"', h)
print('Sample practice links in current-electricity HTML:')
for l in links[:10]:
    print(' ', l)
