import re

ce_file = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/current-electricity/index.html'
with open(ce_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace href="/practice/?q=1841#card_1841" with href="/practice/?exam=cbse&subject=Physics&chapter=Current+Electricity&q=1841#1841"
pattern = r'href="/practice/\?q=(\d+)#card_\1"'
replacement = r'href="/practice/?exam=cbse&subject=Physics&chapter=Current+Electricity&q=\1#\1"'

new_html = re.sub(pattern, replacement, html)

with open(ce_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("[SUCCESS] Updated practice links in current-electricity to pass exam, subject, chapter, and q.")
