import glob, os, re

chapter_files = glob.glob('E:/PYQ_Wovrix_Portal/pyq-wovrix/cbse-12/**/*.html', recursive=True)
print(f"Inspecting titles for {len(chapter_files)} files in cbse-12/")

updated = 0
for p in chapter_files:
    rel = os.path.relpath(p, 'E:/PYQ_Wovrix_Portal/pyq-wovrix').replace('\\', '/')
    parts = rel.split('/')
    if len(parts) != 4 or parts[-1] != 'index.html':
        continue
    
    subject = parts[1].capitalize()
    ch_slug = parts[2]
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract h1 chapter title
    m_h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html)
    if not m_h1:
        continue
    ch_title = m_h1.group(1).strip()

    # Build concise title
    short_ch = ch_title.replace(' and ', ' & ')
    candidate = f"{short_ch} PYQs – CBSE 12 {subject} | Learnosha"
    if len(candidate) > 65:
        candidate = f"{short_ch} PYQs – CBSE 12 | Learnosha"

    m_title = re.search(r'<title>(.*?)</title>', html)
    if m_title and len(m_title.group(1)) > 70:
        old_title = m_title.group(1)
        html = html.replace(f'<title>{old_title}</title>', f'<title>{candidate}</title>')
        # Also sync og:title and twitter:title if they were identical
        html = html.replace(f'content="{old_title}"', f'content="{candidate}"')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✔ [{len(candidate)} chars] {candidate}")
        updated += 1

print(f"[SUCCESS] Streamlined {updated} long chapter titles.")
