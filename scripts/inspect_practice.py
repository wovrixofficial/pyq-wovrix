with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/practice/index.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

pos = p_html.find('if (showRepeatsOnly)')
print(p_html[pos:pos+2000])
