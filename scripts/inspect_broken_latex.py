import re

files = [
    'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/alternating-current/index.html',
    'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/semiconductor-electronics-materials-devices-and-simple-circuits/index.html',
    'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/chemistry/amines/index.html',
    'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/chemistry/chemical-kinetics/index.html',
    'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/chemistry/solutions/index.html',
    'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/mathematics/probability/index.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    print("="*60)
    print(f"File: {p.split('/')[-2]}")
    
    # Check 100 \pi t
    if '$100 \\pi t$' in content:
        for m in re.finditer(r'.{0,40}\$100 \\pi t\$.{0,40}', content):
            print("  Broken $100 \\pi t$:", m.group(0).replace('\n', ' '))

    # Check % inside math
    for m in re.finditer(r'\$[^\$]*?\d+%\$|\$[^\$]*?\d+%\s', content):
        print("  Unescaped % in math:", m.group(0).replace('\n', ' '))
