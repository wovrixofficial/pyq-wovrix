import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def task1_sitemaps():
    print("--- Task 1: Sitemaps Domain Clean-up ---")
    files_to_fix = [
        os.path.join(ROOT, "sitemap-chapters.xml"),
        os.path.join(ROOT, "sitemap-clusters.xml"),
        os.path.join(ROOT, "sitemap-index.xml"),
        os.path.join(ROOT, "robots.txt")
    ]
    total_replaced = 0
    for path in files_to_fix:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        cnt = content.count("https://pyq.wovrix.in/")
        if cnt > 0:
            new_content = content.replace("https://pyq.wovrix.in/", "https://learnosha.in/")
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Replaced {cnt} occurrences in {os.path.basename(path)}")
            total_replaced += cnt
        else:
            print(f"No occurrences in {os.path.basename(path)}")
    print(f"Task 1 Complete: {total_replaced} total URLs migrated to learnosha.in\n")

def task2_formula_redirect():
    print("--- Task 2: /formula-sheets/ 404 Redirect ---")
    # Update vercel.json
    vercel_path = os.path.join(ROOT, "vercel.json")
    with open(vercel_path, "r", encoding="utf-8") as f:
        v_data = json.load(f)

    redirects = v_data.setdefault("redirects", [])
    has_redirect = any(r.get("source") == "/formula-sheets/" for r in redirects)
    if not has_redirect:
        redirects.extend([
            {
                "source": "/formula-sheets",
                "destination": "/syllabus/",
                "permanent": True
            },
            {
                "source": "/formula-sheets/",
                "destination": "/syllabus/",
                "permanent": True
            }
        ])
        with open(vercel_path, "w", encoding="utf-8") as f:
            json.dump(v_data, f, indent=2)
        print("Added 301 redirects for /formula-sheets in vercel.json")
    else:
        print("Redirect already present in vercel.json")

    # Also update chapter HTML footers
    updated_html = 0
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.vercel', 'q', 'scratch']]
        for file in files:
            if file.endswith('.html'):
                fpath = os.path.join(root, file)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    c = f.read()
                if 'href="/formula-sheets/"' in c:
                    new_c = c.replace('href="/formula-sheets/"', 'href="/syllabus/"')
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_c)
                    updated_html += 1
    print(f"Updated footer links in {updated_html} HTML files to point to /syllabus/ directly.\n")

def task3_current_electricity():
    print("--- Task 3: Current Electricity LaTeX & Tagging Fixes ---")
    html_path = os.path.join(ROOT, "cbse-12", "physics", "current-electricity", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix \t (Tab character) corruption
    # Literal tab followed by ext -> \text
    tab_ext_cnt = len(re.findall(r'\text', content))
    tab_imes_cnt = len(re.findall(r'\times', content))
    content = content.replace('\text', r'\text')
    content = content.replace('\times', r'\times')
    print(f"Fixed {tab_ext_cnt} tab-corrupted \\text and {tab_imes_cnt} tab-corrupted \\times")

    # 2. Fix nested math on line 544
    nested_math_old = r'$V_i = 12 \sin $100 \pi t$ \text{ V}$'
    nested_math_new = r'$V_i = 12 \sin(100 \pi t)\text{ V}$'
    if nested_math_old in content:
        content = content.replace(nested_math_old, nested_math_new)
        print("Fixed nested math in Line 544")
    else:
        # Try regex if slight whitespace variations
        content = re.sub(
            r'\$V_i\s*=\s*12\s*\\sin\s*\$100\s*\\pi\s*t\$\s*\\text\{\s*V\}\$',
            nested_math_new,
            content
        )
        print("Applied regex fix for nested math in Line 544")

    # 3. Fix unescaped %
    if '$20%$' in content:
        content = content.replace('$20%$', r'$20\%$')
        print("Fixed unescaped $20%$ to $20\\%$")
    # General regex for any $num%$ -> $num\%$
    content = re.sub(r'(\$\d+(?:\.\d+)?)(%)\$', r'\1\\%$', content)

    # 4. Re-tag misclassified questions in HTML
    # QID 3674 (Line 326: AC series circuit) -> Tag as Ch 7 Alternating Current
    q3674_needle = '<a href="/practice/?q=3674#card_3674"'
    pos3674 = content.find(q3674_needle)
    if pos3674 != -1:
        # Find card-meta before this
        meta_pos = content.rfind('<div class="card-meta">', 0, pos3674)
        if meta_pos != -1:
            insertion = '<div class="card-meta">\n                    <span class="tag tag-chapter" style="background:rgba(234,88,12,0.12); color:#ea580c; border:1px solid rgba(234,88,12,0.25); font-weight:700;">Ch 7: Alternating Current</span>'
            content = content[:meta_pos] + insertion + content[meta_pos + len('<div class="card-meta">'):]
            print("Added Ch 7 Alternating Current tag to Question 3674")

    # QID 218 (Line 544: diode network) -> Tag as Ch 14 Semiconductor Electronics
    q218_needle = '<a href="/practice/?q=218#card_218"'
    pos218 = content.find(q218_needle)
    if pos218 != -1:
        meta_pos = content.rfind('<div class="card-meta">', 0, pos218)
        if meta_pos != -1:
            insertion = '<div class="card-meta">\n                    <span class="tag tag-chapter" style="background:rgba(16,185,129,0.12); color:#059669; border:1px solid rgba(16,185,129,0.25); font-weight:700;">Ch 14: Semiconductor Electronics</span>'
            content = content[:meta_pos] + insertion + content[meta_pos + len('<div class="card-meta">'):]
            print("Added Ch 14 Semiconductor tag to Question 218")

    # QIDs 4598, 4670, 4708 (Diode threshold questions) -> Tag as Ch 14 Semiconductor Electronics
    for qid in ['4598', '4670', '4708']:
        needle = f'<a href="/practice/?q={qid}#card_{qid}"'
        pos = content.find(needle)
        if pos != -1:
            meta_pos = content.rfind('<div class="card-meta">', 0, pos)
            if meta_pos != -1:
                insertion = '<div class="card-meta">\n                    <span class="tag tag-chapter" style="background:rgba(16,185,129,0.12); color:#059669; border:1px solid rgba(16,185,129,0.25); font-weight:700;">Ch 14: Semiconductor Electronics</span>'
                content = content[:meta_pos] + insertion + content[meta_pos + len('<div class="card-meta">'):]
                print(f"Added Ch 14 Semiconductor tag to Question {qid}")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Saved cbse-12/physics/current-electricity/index.html")

    # 5. Update data source: data/cbse_physics.json
    json_path = os.path.join(ROOT, "data", "cbse_physics.json")
    with open(json_path, "r", encoding="utf-8") as f:
        cbse_data = json.load(f)

    json_modified = 0
    for q in cbse_data:
        qid = q.get("id")
        if qid in [4598, 4670, 4708, 218]:
            q["chapter_number"] = 14
            q["chapter_name"] = "Semiconductor Electronics: Materials, Devices and Simple Circuits"
            if qid == 218:
                q["text"] = q["text"].replace(r"$V_i = 12 \sin $100 \pi t$ \text{ V}$", r"$V_i = 12 \sin(100 \pi t)\text{ V}$")
            json_modified += 1
        elif qid == 3674:
            q["chapter_number"] = 7
            q["chapter_name"] = "Alternating Current"
            json_modified += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cbse_data, f, indent=2, ensure_ascii=False)
    print(f"Updated {json_modified} question records in data/cbse_physics.json\n")

if __name__ == '__main__':
    task1_sitemaps()
    task2_formula_redirect()
    task3_current_electricity()
    print("ALL REMEDIATION TASKS APPLIED SUCCESSFULLY.")
