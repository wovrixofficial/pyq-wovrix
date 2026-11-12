p = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/jee/index.html'
with open(p, 'r', encoding='utf-8') as f:
    h = f.read()

if 'rel="canonical"' not in h:
    target = '</title>'
    replacement = '</title>\n  <link rel="canonical" href="https://learnosha.in/jee/">'
    h = h.replace(target, replacement, 1)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(h)
    print('[OK] Added canonical tag to jee/index.html')
