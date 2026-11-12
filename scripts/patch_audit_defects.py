import re

print("Applying targeted fixes for 100% clean audit...")

# 1. Alternating Current HTML
ac_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/alternating-current/index.html'
with open(ac_path, 'r', encoding='utf-8') as f:
    ac = f.read()
ac = ac.replace('$v_i = 140 \\sin$100 \\pi t$ \\text{ V}$', '$v_i = 140 \\sin(100 \\pi t) \\text{ V}$')
ac = ac.replace('140 \\sin$100 \\pi t$', '140 \\sin(100 \\pi t)')
with open(ac_path, 'w', encoding='utf-8') as f:
    f.write(ac)
print("✔ Fixed alternating-current HTML")

# 2. Semiconductor Electronics HTML
semi_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/physics/semiconductor-electronics-materials-devices-and-simple-circuits/index.html'
with open(semi_path, 'r', encoding='utf-8') as f:
    semi = f.read()
semi = semi.replace('$V = 0.5 \\sin $100 \\pi t$$', '$V = 0.5 \\sin(100 \\pi t)$')
semi = semi.replace('$V_i = 12 \\sin $100 \\pi t$\\text{ V}$', '$V_i = 12 \\sin(100 \\pi t)\\text{ V}$')
semi = semi.replace('$V_i = 12 \\sin $100 \\pi t$ \\text{ V}$', '$V_i = 12 \\sin(100 \\pi t) \\text{ V}$')
with open(semi_path, 'w', encoding='utf-8') as f:
    f.write(semi)
print("✔ Fixed semiconductor-electronics HTML")

# 3. Chemical Kinetics HTML
ck_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/chemistry/chemical-kinetics/index.html'
with open(ck_path, 'r', encoding='utf-8') as f:
    ck = f.read()
ck = ck.replace('$99%$', '$99\\%$')
ck = ck.replace('$90%$', '$90\\%$')
ck = ck.replace('$30%$', '$30\\%$')
with open(ck_path, 'w', encoding='utf-8') as f:
    f.write(ck)
print("✔ Fixed chemical-kinetics HTML")

# 4. Probability HTML
prob_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/mathematics/probability/index.html'
with open(prob_path, 'r', encoding='utf-8') as f:
    prob = f.read()
prob = prob.replace('$60%, 70%$', '$60\\%, 70\\%$')
prob = prob.replace('$30%, 60%$', '$30\\%, 60\\%$')
with open(prob_path, 'w', encoding='utf-8') as f:
    f.write(prob)
print("✔ Fixed probability HTML")

# 5. Formula sheets redirect page
fs_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/formula-sheets/index.html'
fs_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Official Syllabus & Formulas Blueprint | Learnosha</title>
  <meta name="description" content="Redirecting to official CBSE Class 12, NEET UG, and JEE Main syllabus and formulas vault.">
  <meta http-equiv="refresh" content="0; url=/syllabus/">
  <link rel="canonical" href="https://learnosha.in/syllabus/">
  <script>window.location.replace('/syllabus/');</script>
</head>
<body style="font-family: sans-serif; text-align: center; padding: 40px;">
  <p>Redirecting to <a href="/syllabus/">Official Syllabus & Formulas Blueprint</a>...</p>
</body>
</html>
"""
with open(fs_path, 'w', encoding='utf-8') as f:
    f.write(fs_content)
print("✔ Converted formula-sheets/index.html to instant redirect")

# 6. Titles for paper-maker and syllabus
pm_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/paper-maker/index.html'
with open(pm_path, 'r', encoding='utf-8') as f:
    pm = f.read()
pm = re.sub(r'<title>.*?</title>', '<title>Custom Question Paper & CBT Mock Exam Maker | Learnosha</title>', pm)
with open(pm_path, 'w', encoding='utf-8') as f:
    f.write(pm)
print("✔ Streamlined paper-maker title")

syl_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/syllabus/index.html'
with open(syl_path, 'r', encoding='utf-8') as f:
    syl = f.read()
syl = re.sub(r'<title>.*?</title>', '<title>Official Syllabus & Marks Weightage Blueprints | Learnosha</title>', syl)
with open(syl_path, 'w', encoding='utf-8') as f:
    f.write(syl)
print("✔ Streamlined syllabus title")

# 7. NEET UG Progress monitor
prog_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/neetug/progress.html'
with open(prog_path, 'r', encoding='utf-8') as f:
    prog = f.read()
if 'robots' not in prog:
    prog = prog.replace('<title>', '<meta name="robots" content="noindex, nofollow">\n  <meta name="description" content="Internal NEET extraction monitor.">\n  <link rel="canonical" href="https://learnosha.in/neetug/progress.html">\n  <title>')
    with open(prog_path, 'w', encoding='utf-8') as f:
        f.write(prog)
print("✔ Added noindex and metadata to neetug/progress.html")

print("[SUCCESS] All targeted fixes successfully applied.")
