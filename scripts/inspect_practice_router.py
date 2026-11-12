with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/practice/index.html', 'r', encoding='utf-8') as f:
    h = f.read()

pos1 = h.find('let currentTopic')
print('Globals:\n', h[pos1:pos1+500])

pos2 = h.find('const urlQ = p.get(\'q\');')
print('\nRouter:\n', h[pos2-50:pos2+300])
