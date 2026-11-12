import glob, os, re

chapter_files = glob.glob('E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/**/*.html', recursive=True)
print(f"Found {len(chapter_files)} HTML files in cbse-12/")

updated_count = 0
for p in chapter_files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Update Class 10 (Soon) to JEE Main
    if 'Class 10 (Soon)' in content:
        content = content.replace(
            '<span class="f-pill">Class 10 (Soon)</span>',
            '<span class="f-pill active">JEE Main</span>'
        )
        content = content.replace(
            '<span>Class 10 (Soon)</span>',
            '<span class="f-pill active">JEE Main</span>'
        )
        changed = True

    # 2. Update formula-sheets link
    if '/formula-sheets/' in content or '/formula-sheets' in content:
        content = content.replace('/formula-sheets/', '/syllabus/')
        content = content.replace('/formula-sheets', '/syllabus/')
        changed = True

    # 3. Ensure "non-commercial" assertion is replaced with standard disclaimer
    old_disc = 'Official past examination papers reproduced under fair dealing for educational non-commercial study'
    if old_disc in content:
        content = re.sub(
            r'Official past examination papers reproduced under fair dealing for educational non-commercial study[^\.]*\.',
            'Disclaimer: Independent study resource providing NCERT-aligned past paper revision, repeat pattern analytics, and step-by-step solutions for CBSE and competitive exams.',
            content
        )
        changed = True

    if changed:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

print(f"[SUCCESS] Updated footers across {updated_count} files in cbse-12/")
