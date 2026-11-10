import os
import re

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

REPLACEMENTS = [
    # URLs and Domains
    ("https://pyq.wovrix.in", "https://learnosha.in"),
    ("https://wovrix.in", "https://learnosha.in"),
    ("http://pyq.wovrix.in", "https://learnosha.in"),
    ("http://wovrix.in", "https://learnosha.in"),
    ("pyq.wovrix.in", "learnosha.in"),
    
    # Emails
    ("academic@wovrix.in", "support@learnosha.in"),
    ("support@wovrix.in", "support@learnosha.in"),
    ("privacy@wovrix.in", "privacy@learnosha.in"),
    ("legal@wovrix.in", "legal@learnosha.in"),
    
    # Brand HTML spans
    ('<span class="brand-name">WOVRIX <span class="brand-slash">/</span> <span class="brand-sub">PYQ</span></span>', '<span class="brand-name">LEARNOSHA</span>'),
    ('WOVRIX <span class="brand-slash">/</span> <span class="brand-sub">PYQ</span>', 'LEARNOSHA'),
    ('<span class="brand-name">WOVRIX <span class="brand-slash">/</span> <span class="brand-sub">JEE MAIN</span></span>', '<span class="brand-name">LEARNOSHA <span class="brand-slash">/</span> <span class="brand-sub">JEE</span></span>'),
    ('WOVRIX <span class="brand-sub">PYQ</span>', 'LEARNOSHA'),
    ('<span class="footer-brand-text">WOVRIX PYQ</span>', '<span class="footer-brand-text">LEARNOSHA</span>'),
    ('<div class="footer-giant-wordmark">WOVRIX</div>', '<div class="footer-giant-wordmark">LEARNOSHA</div>'),
    ('footer-massive-wovrix', 'footer-massive-learnosha'),
    
    # Text Titles and Mentions
    ("PYQ Wovrix", "Learnosha"),
    ("Wovrix PYQ", "Learnosha"),
    ("About Wovrix", "About Learnosha"),
    ("Wovrix Main Portal", "Learnosha Home"),
    ("Wovrix (wovrix.in)", "Learnosha (learnosha.in)"),
    ("wovrix_study_backup_", "learnosha_study_backup_"),
]

EXTENSIONS = {".html", ".js", ".css", ".json"}
IGNORE_DIRS = {".git", "node_modules", ".gemini", "automation-suite", ".github"}
IGNORE_FILES = {"jee_main_all.json", "jee_main_all.js", "questions_all.json", "questions_all.js", "solutions_cache.json", "package-lock.json"}

total_files_updated = 0
total_replacements = 0

for root, dirs, files in os.walk(REPO_DIR):
    # filter directories
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
    for fname in files:
        if fname in IGNORE_FILES:
            continue
        ext = os.path.splitext(fname)[1].lower()
        if ext in EXTENSIONS:
            filepath = os.path.join(root, fname)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            orig_content = content
            rep_count = 0
            for old_s, new_s in REPLACEMENTS:
                if old_s in content:
                    c = content.count(old_s)
                    rep_count += c
                    content = content.replace(old_s, new_s)

            if content != orig_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                total_files_updated += 1
                total_replacements += rep_count

print(f"DONE: Updated {total_files_updated} files with {total_replacements} replacements.")
