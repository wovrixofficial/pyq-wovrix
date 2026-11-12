import json
import re

print("Starting comprehensive repair of LaTeX syntax and links...")

# ---------------------------------------------------------
# 1. FIX cbse_physics.json
# ---------------------------------------------------------
phys_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_physics.json'
with open(phys_path, 'r', encoding='utf-8') as f:
    phys = json.load(f)

for q in phys:
    qid = q['id']
    t = q.get('text', '')
    if qid == 333:
        q['chapter_name'] = 'Semiconductor Electronics: Materials, Devices and Simple Circuits'
        q['chapter_number'] = 14
        q['subtopic'] = 'Semiconductors, Diodes & Logic Gates'
        q['subtopic_slug'] = 'semiconductors-diodes-gates'
        q['text'] = t.replace('$100 \\pi t$', '(100 \\pi t)').replace('$\\sin (100 \\pi t) \\text{ V}$', '\\sin(100 \\pi t) \\text{ V}')
        q['text'] = q['text'].replace('$V_i = 12 \\sin (100 \\pi t) \\text{ V}$', '$V_i = 12 \\sin(100 \\pi t) \\text{ V}$')
        if q['text'].count('$') % 2 != 0:
            q['text'] = q['text'].replace('12 \\sin (100 \\pi t) \\text{ V}$', '12 \\sin(100 \\pi t) \\text{ V}$')
    elif qid == 2078:
        # fix unclosed (D) $320\text{ cm}
        q['text'] = t.replace('(D) $320\\text{ cm}\n', '(D) $320\\text{ cm}$\n')
    elif qid == 5846:
        q['text'] = t.replace('$140 \\sin$100 \\pi t$ \\text{ V}$', '$140 \\sin(100 \\pi t) \\text{ V}$')
        q['text'] = q['text'].replace('$140 \\sin $100 \\pi t$ \\text{ V}$', '$140 \\sin(100 \\pi t) \\text{ V}$')
    elif qid == 7101:
        q['text'] = t.replace('$V = 0.5 \\sin $100 \\pi t$$', '$V = 0.5 \\sin(100 \\pi t)$')
    elif qid == 5513:
        q['text'] = t.replace('0.1% ', '0.1\\% ')

with open(phys_path, 'w', encoding='utf-8') as f:
    json.dump(phys, f, indent=2, ensure_ascii=False)
print("✔ Fixed cbse_physics.json")

# ---------------------------------------------------------
# 2. FIX cbse_chemistry.json
# ---------------------------------------------------------
chem_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_chemistry.json'
with open(chem_path, 'r', encoding='utf-8') as f:
    chem = json.load(f)

for q in chem:
    qid = q['id']
    t = q.get('text', '')
    if qid in (931, 969):
        q['text'] = t.replace('\\text{HCOOH}\n', '\\text{HCOOH}$\n')
    elif qid == 991:
        q['text'] = t.replace('\\xrightarrow[\\text{Heat}]{\\text{Ethanol}}\n', '\\xrightarrow[\\text{Heat}]{\\text{Ethanol}}$\n')
    elif qid == 1122:
        q['text'] = t.replace('(\\text{Given}', '($\\text{Given}')
    elif qid == 1152:
        q['text'] = t.replace('(I) $2 \\text{ Cl} \\xrightarrow{\\text{Na/dry Ether}}\n', '(I) $2 \\text{ Cl} \\xrightarrow{\\text{Na/dry Ether}}$\n')
    elif qid == 2831:
        q['text'] = t.replace('\\xrightarrow{\\hspace*{2cm}}\n', '\\xrightarrow{\\hspace*{2cm}}$\n')
    elif qid == 3059:
        q['text'] = t.replace('(C) $\\text{[Co(NH}_3)_4\\text{Cl}_2]^+\n', '(C) $\\text{[Co(NH}_3)_4\\text{Cl}_2]^+$\n')
    elif qid == 9945:
        q['text'] = t.replace('_{58}\\text{Ce} = [\\text{Xe}]^{54} 4f^1 5d^1 6s^2.', '$_{58}\\text{Ce} = [\\text{Xe}]^{54} 4f^1 5d^1 6s^2$.')
    elif qid in (8385, 8425):
        q['text'] = t.replace('40% ', '40\\% ')
    elif qid == 9827:
        q['text'] = t.replace('75% ', '75\\% ')

with open(chem_path, 'w', encoding='utf-8') as f:
    json.dump(chem, f, indent=2, ensure_ascii=False)
print("✔ Fixed cbse_chemistry.json")

# ---------------------------------------------------------
# 3. FIX cbse_mathematics.json
# ---------------------------------------------------------
math_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_mathematics.json'
with open(math_path, 'r', encoding='utf-8') as f:
    math = json.load(f)

for q in math:
    qid = q['id']
    t = q.get('text', '')
    if qid == 177:
        q['text'] = t.replace('\\end{cases}$ is continuous', '\\end{cases}$$ is continuous')
    elif qid == 1425:
        q['text'] = t.replace('(B) $[-3, 5]\n', '(B) $[-3, 5]$\n')
    elif qid == 1571:
        q['text'] = t.replace('(A) $-\\frac{\\pi}{2}\n', '(A) $-\\frac{\\pi}{2}$\n')
    elif qid == 4986:
        q['text'] = t.replace('\\cot^{-1}\\left$-\\frac{1}{\\sqrt{3}}\\right$$', '\\cot^{-1}\\left(-\\frac{1}{\\sqrt{3}}\\right)$')
        q['text'] = q['text'].replace('(A) $-\\frac{\\pi}{3}\n', '(A) $-\\frac{\\pi}{3}$\n')
        q['text'] = q['text'].replace('(B) $-\\frac{2\\pi}{3}\n', '(B) $-\\frac{2\\pi}{3}$\n')
    elif qid == 4987:
        q['text'] = t.replace('(B) $-10\n', '(B) $-10$\n')
    elif qid == 5003:
        q['text'] = t.replace("(D) $(2, 2)'", "(D) $(2, 2)$'")
    elif qid == 6690:
        q['text'] = t.replace('; y(0) = 5. OR', '; y(0) = 5.$ OR')
    elif qid == 7405:
        q['text'] = t.replace('b^2} = 1." (i)', 'b^2} = 1$." (i)')
    elif qid == 7383:
        q['text'] = t.replace('1.56%', '1.56\\%')

with open(math_path, 'w', encoding='utf-8') as f:
    json.dump(math, f, indent=2, ensure_ascii=False)
print("✔ Fixed cbse_mathematics.json")

# ---------------------------------------------------------
# 4. FIX HTML FILES: formula-sheets link in root pages
# ---------------------------------------------------------
for root_html in ['index.html', 'practice/index.html', 'syllabus/index.html']:
    p = f'E:/PYQ_Wovrix_Portal/pyq-wovrix/{root_html}'
    with open(p, 'r', encoding='utf-8') as f:
        h = f.read()
    h = h.replace('href="/formula-sheets/"', 'href="/syllabus/"')
    h = h.replace('href="/formula-sheets"', 'href="/syllabus/"')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(h)
    print(f"✔ Fixed formula-sheets link in {root_html}")

# ---------------------------------------------------------
# 5. FIX CHAPTER HTML FILES: broken formulas and unescaped %
# ---------------------------------------------------------
html_fixes = [
    ('cbse-12/physics/alternating-current/index.html', [
        ('$140 \\sin$100 \\pi t$ \\text{ V}$', '$140 \\sin(100 \\pi t) \\text{ V}$'),
        ('$140 \\sin $100 \\pi t$ \\text{ V}$', '$140 \\sin(100 \\pi t) \\text{ V}$')
    ]),
    ('cbse-12/physics/semiconductor-electronics-materials-devices-and-simple-circuits/index.html', [
        ('$0.5 \\sin $100 \\pi t$$ volt', '$0.5 \\sin(100 \\pi t)$ volt'),
        ('$12 \\sin $100 \\pi t$\\text{ V}$', '$12 \\sin(100 \\pi t)\\text{ V}$'),
        ('$12 \\sin $100 \\pi t$ \\text{ V}$', '$12 \\sin(100 \\pi t) \\text{ V}$'),
        ('$40%$', '$40\\%$'),
        ('$60%$', '$60\\%$')
    ]),
    ('cbse-12/chemistry/amines/index.html', [
        ('$51%$', '$51\\%$'),
        ('$47%$', '$47\\%$'),
        ('$2%$', '$2\\%$')
    ]),
    ('cbse-12/chemistry/chemical-kinetics/index.html', [
        ('$25%$', '$25\\%$'),
        ('$75%$', '$75\\%$'),
        ('$50%$', '$50\\%$'),
        ('$10%$', '$10\\%$')
    ]),
    ('cbse-12/chemistry/solutions/index.html', [
        ('$5%$', '$5\\%$'),
        ('$2%$', '$2\\%$'),
        ('$10%$', '$10\\%$'),
        ('$20%$', '$20\\%$')
    ]),
    ('cbse-12/mathematics/probability/index.html', [
        ('$2%$', '$2\\%$'),
        ('$5%$', '$5\\%$'),
        ('$10%$', '$10\\%$'),
        ('$20%$', '$20\\%$'),
        ('$25%$', '$25\\%$'),
        ('$30%$', '$30\\%$'),
        ('$35%$', '$35\\%$'),
        ('$40%$', '$40\\%$'),
        ('$45%$', '$45\\%$'),
        ('$50%$', '$50\\%$'),
        ('$55%$', '$55\\%$'),
        ('$60%$', '$60\\%$'),
        ('$70%$', '$70\\%$'),
        ('$80%$', '$80\\%$'),
        ('$90%$', '$90\\%$')
    ])
]

for rel_path, repls in html_fixes:
    p = f'E:/PYQ_Wovrix_Portal/pyq-wovrix/{rel_path}'
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    for target, rep in repls:
        content = content.replace(target, rep)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✔ Fixed LaTeX in {rel_path}")

print("[SUCCESS] Comprehensive repair completed successfully.")
