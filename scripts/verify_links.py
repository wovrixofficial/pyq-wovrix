import os
import glob
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

broken_patterns = [
    r'•subject=',
    r'\ufffdsubject=',
    r'href=["\']/neetug/["\']',
]

total_issues = 0

for root_dir, dirs, files in os.walk(ROOT):
    if any(ignore in root_dir for ignore in ['.git', 'node_modules', '.vercel']):
        continue
    for fname in files:
        if fname.endswith('.html'):
            fpath = os.path.join(root_dir, fname)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            for pat in broken_patterns:
                matches = re.findall(pat, content)
                if matches:
                    rel = os.path.relpath(fpath, ROOT)
                    print(f"Broken link pattern '{pat}' found in {rel}: {len(matches)} times")
                    total_issues += len(matches)

if total_issues == 0:
    print("Link Integrity Audit: PASSED (0 broken NEET or dead /neetug/ links across all files!)")
else:
    print(f"Link Integrity Audit: FAILED ({total_issues} issues found)")
