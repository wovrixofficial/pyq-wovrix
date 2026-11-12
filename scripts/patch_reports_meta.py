p = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/reports/index.html'
with open(p, 'r', encoding='utf-8') as f:
    h = f.read()

if 'name="description"' not in h:
    target = '<title>Learnosha | Student Reports & Error Resolution Console</title>'
    replacement = target + '\n  <meta name="description" content="Learnosha question error reporting, solution corrections, and moderation dashboard.">'
    h = h.replace(target, replacement)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(h)
    print('[OK] Added meta description to reports/index.html')
