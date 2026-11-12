with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/practice/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

pos = h.find('function renderStreamQuestionsFeed()')
print(h[pos+5000:pos+7000])
