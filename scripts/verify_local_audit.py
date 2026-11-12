import re
import os
import glob

print("==================================================")
print("LOCAL VERIFICATION AUDIT: All Core Pages")
print("==================================================")

root_dir = "E:/PYQ_Wovrix_Portal/pyq-wovrix"
html_files = []
for p in glob.glob(f"{root_dir}/**/*.html", recursive=True):
    if ".git" in p or "node_modules" in p or "q\\" in p or "q/" in p or "scratch" in p or "scripts" in p:
        continue
    rel = os.path.relpath(p, root_dir).replace('\\', '/')
    html_files.append((rel, p))

print(f"Total production HTML pages to verify: {len(html_files)}")

errors = []
warnings = []

for rel, path in sorted(html_files):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check title
    m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if not m_title or not m_title.group(1).strip():
        errors.append((rel, "Missing <title>"))
    elif len(m_title.group(1).strip()) > 75 and 'google' not in rel:
        warnings.append((rel, f"Title long ({len(m_title.group(1).strip())} chars): {m_title.group(1)[:50]}..."))

    # 2. Check meta description
    if 'google' not in rel and '404' not in rel:
        m_desc = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.IGNORECASE)
        if not m_desc or not m_desc.group(1).strip():
            errors.append((rel, "Missing meta description"))

    # 3. Check canonical
    if 'google' not in rel and '404' not in rel:
        m_canon = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\'](.*?)["\']', content, re.IGNORECASE)
        if not m_canon:
            warnings.append((rel, "Missing canonical tag"))

    # 4. Check for old domain leak
    if "pyq.wovrix.in" in content and rel != 'vercel.json':
        matches = re.findall(r'https?://pyq\.wovrix\.in[^\s"\'<>]*', content)
        if matches:
            errors.append((rel, f"Contains old domain links: {matches[:3]}"))

    # 5. Check for formula-sheets link
    if "/formula-sheets/" in content or "/formula-sheets" in content:
        errors.append((rel, "Contains link to old /formula-sheets/"))

    # 6. Check for stale "Class 10 (Soon)"
    if "Class 10 (Soon)" in content:
        errors.append((rel, "Contains stale 'Class 10 (Soon)' in footer pills"))

    # 7. Check for broken LaTeX in HTML
    if "$100 \\pi t$" in content:
        errors.append((rel, "Contains broken nested $100 \\pi t$"))
    if re.search(r'\$[^\$]*?\d+%\$', content):
        errors.append((rel, "Contains unescaped % inside math ($20%$)"))

print(f"\nErrors found: {len(errors)}")
for rel, err in errors:
    print(f"  ❌ {rel}: {err}")

print(f"\nWarnings found: {len(warnings)}")
for rel, warn in warnings:
    print(f"  ⚠  {rel}: {warn}")

if len(errors) == 0:
    print("\n🎉 ALL LOCAL PRODUCTION PAGES ARE 100% CLEAN AND PASSING ALL AUDIT RULES!")
