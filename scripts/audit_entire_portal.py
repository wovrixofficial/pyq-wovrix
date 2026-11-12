import urllib.request
import re
import os
import glob
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://learnosha.in"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) LearnoshaAuditor/1.0'}

print("==================================================")
print("STARTING FULL-SITE PRODUCTION AUDIT: learnosha.in")
print("==================================================")

# Step 1: Collect all pages from local directory structure
root_dir = "E:/PYQ_Wovrix_Portal/pyq-wovrix"
html_files = []
for p in glob.glob(f"{root_dir}/**/*.html", recursive=True):
    if ".git" in p or "node_modules" in p or "q\\" in p or "q/" in p:
        continue
    rel = os.path.relpath(p, root_dir).replace('\\', '/')
    if rel == 'index.html':
        url_path = '/'
    elif rel.endswith('/index.html'):
        url_path = '/' + rel[:-10]
    elif rel.endswith('.html'):
        url_path = '/' + rel[:-5]
    else:
        url_path = '/' + rel
    if not url_path.endswith('/'):
        url_path += '/'
    html_files.append((url_path, p))

# Deduplicate URLs
url_map = {}
for u, p in html_files:
    if u not in url_map:
        url_map[u] = p

print(f"Total core structural pages to audit: {len(url_map)}")

# Audit function for a single URL
def audit_url(url_path):
    url = f"{BASE_URL}{url_path}"
    errors = []
    warnings = []
    
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=12) as resp:
            status = resp.status
            content = resp.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return url_path, [f"HTTP Error {e.code}"], []
    except Exception as e:
        return url_path, [f"Fetch failed: {e}"], []

    # 1. Check title
    m_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if not m_title or not m_title.group(1).strip():
        errors.append("Missing <title>")
    elif len(m_title.group(1).strip()) > 75:
        warnings.append(f"Title long ({len(m_title.group(1).strip())} chars): {m_title.group(1)[:50]}...")

    # 2. Check meta description
    m_desc = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.IGNORECASE)
    if not m_desc or not m_desc.group(1).strip():
        errors.append("Missing meta description")

    # 3. Check canonical
    m_canon = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\'](.*?)["\']', content, re.IGNORECASE)
    if not m_canon:
        warnings.append("Missing canonical tag")
    elif not m_canon.group(1).startswith("https://learnosha.in"):
        errors.append(f"Invalid canonical domain: {m_canon.group(1)}")

    # 4. Check for old domain leak
    if "pyq.wovrix.in" in content:
        # Check if it's in a redirect rule or visible link
        matches = re.findall(r'https?://pyq\.wovrix\.in[^\s"\'<>]*', content)
        if matches:
            errors.append(f"Contains old domain links: {matches[:3]}")

    # 5. Check for formula-sheets link
    if "/formula-sheets/" in content or "/formula-sheets" in content:
        errors.append("Contains link to old /formula-sheets/")

    # 6. Check for stale "Class 10 (Soon)"
    if "Class 10 (Soon)" in content:
        errors.append("Contains stale 'Class 10 (Soon)' in footer pills")

    # 7. Check for old non-commercial restrictive disclaimer
    if "Official past examination papers reproduced under fair dealing for educational non-commercial study" in content:
        warnings.append("Contains old non-commercial disclaimer")

    # 8. Check for broken LaTeX in HTML
    if "$100 \\pi t$" in content:
        errors.append("Contains broken nested $100 \\pi t$")
    if re.search(r'\$\s*\d+%\s*\$', content):
        errors.append("Contains unescaped % inside math ($20%$)")

    return url_path, errors, warnings

# Execute audit in parallel
print("Auditing live production pages...")
results = []
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(audit_url, u) for u in sorted(url_map.keys())]
    for f in futures:
        results.append(f.result())

total_pages = len(results)
pages_with_errors = 0
pages_with_warnings = 0

print("\n--- AUDIT RESULTS ---")
for url_path, errs, warns in sorted(results):
    if errs:
        pages_with_errors += 1
        print(f"❌ [FAIL] {url_path}")
        for e in errs:
            print(f"     Error: {e}")
    elif warns:
        pages_with_warnings += 1
        print(f"⚠  [WARN] {url_path}")
        for w in warns:
            print(f"     Warning: {w}")
    else:
        print(f"✔  [OK]   {url_path}")

print("\n==================================================")
print(f"AUDIT SUMMARY: {total_pages} pages tested.")
print(f"Clean: {total_pages - pages_with_errors - pages_with_warnings} | Warnings: {pages_with_warnings} | Errors: {pages_with_errors}")
print("==================================================")
