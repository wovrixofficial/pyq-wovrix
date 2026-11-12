import os

root_dir = 'E:/PYQ_Wovrix_Portal/pyq-wovrix'
count = 0

for root, dirs, files in os.walk(root_dir):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                
                if '/formula-sheets/' in content or '/formula-sheets' in content:
                    new_content = content.replace('href="/formula-sheets/"', 'href="/syllabus/"')
                    new_content = new_content.replace('href="/formula-sheets"', 'href="/syllabus/"')
                    new_content = new_content.replace("href='/formula-sheets/'", "href='/syllabus/'")
                    new_content = new_content.replace("href='/formula-sheets'", "href='/syllabus/'")
                    if new_content != content:
                        with open(p, 'w', encoding='utf-8') as fp:
                            fp.write(new_content)
                        count += 1
            except Exception as e:
                print(f"Error reading {p}: {e}")

print(f"[SUCCESS] Replaced formula-sheets link in {count} HTML files.")
