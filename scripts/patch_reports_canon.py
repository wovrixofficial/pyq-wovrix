p = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/reports/index.html'
with open(p, 'r', encoding='utf-8') as f:
    h = f.read()

if 'rel="canonical"' not in h:
    h = h.replace('</title>', '</title>\n  <link rel="canonical" href="https://learnosha.in/reports/">')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(h)
    print('[OK] Added canonical to reports/index.html')
