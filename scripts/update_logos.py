import os
import re

OLD_PATTERN = re.compile(r'<svg class="brand-logo-icon"[^>]*>.*?</svg>', re.DOTALL)
NEW_SVG = '''<svg class="brand-logo-icon" width="22" height="23" viewBox="8 6 48 51" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 17V46H45" fill="none" stroke="currentColor" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M29 26.5A10 10 0 0 1 39 36.5" fill="none" stroke="#D97706" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M29 18.5A18 18 0 0 1 47 36.5" fill="none" stroke="#D97706" stroke-opacity=".6" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="29" cy="36.5" r="3" fill="#D97706"/>
        </svg>'''

count = 0
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'assets' in root or 'temp_' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                content = fp.read()
            if 'brand-logo-icon' in content:
                new_content, n = OLD_PATTERN.subn(NEW_SVG, content)
                if n > 0:
                    with open(p, 'w', encoding='utf-8') as fp:
                        fp.write(new_content)
                    print(f"Updated {n} logos in {p}")
                    count += n

print(f"Total logos updated: {count}")
