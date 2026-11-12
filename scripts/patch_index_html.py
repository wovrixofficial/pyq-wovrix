import re

index_file = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    h = f.read()

# 1. Update Title and Social Meta Titles to under 60 chars
old_title = 'Learnosha | CBSE Class 12, NEET UG & JEE Main Master Past Paper Archive (25,006 Qs)'
new_title = 'Learnosha – CBSE 12, NEET & JEE Main Previous Year Questions'

h = h.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>')
h = h.replace(f'<meta property="og:title" content="{old_title}">', f'<meta property="og:title" content="{new_title}">')
h = h.replace(f'<meta name="twitter:title" content="{old_title}">', f'<meta name="twitter:title" content="{new_title}">')

# 2. Update Current Electricity count on Homepage line 926
old_ce_meta = '<span class="ch-meta">324 distinct problems • 437 appearances</span>'
new_ce_meta = '<span class="ch-meta">116 distinct problems • 171 appearances</span>'

h = h.replace(old_ce_meta, new_ce_meta)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(h)

print("[SUCCESS] Patched index.html title and Current Electricity counts.")
