import os
import glob
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
CACHE_FILE = os.path.join(DATA_DIR, "solutions_cache.json")
Q_DIR = os.path.join(ROOT, "q")

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html).strip()

def inject_solutions():
    if not os.path.exists(CACHE_FILE):
        print("[ERROR] solutions_cache.json not found.")
        return

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        solutions = data.get("solutions", {})

    print(f"[INFO] Total solutions in cache: {len(solutions)}")
    updated = 0

    for qid, sol_html in solutions.items():
        if len(sol_html) < 40:
            continue

        # Look for matching directory in q/
        pattern = os.path.join(Q_DIR, f"*-{qid}", "index.html")
        matches = glob.glob(pattern)
        if not matches:
            continue

        for file_path in matches:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Skip if already injected
            if "Verified CBSE Marking Scheme" in content:
                continue

            solution_block = f'''
      <div class="solution-box" style="margin-top:24px; padding:20px; background:var(--card-bg, #ffffff); border:1.5px solid var(--border, #e2e8f0); border-radius:12px;">
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:14px;">
          <span style="background:#10b981; color:#fff; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px; text-transform:uppercase;">✓ Verified CBSE Marking Scheme</span>
          <span style="font-size:12px; color:var(--text-muted, #64748b); font-weight:600;">Official Evaluation Steps</span>
        </div>
        <div class="math-content solution-content" style="line-height:1.7; font-size:15px;">
          {sol_html}
        </div>
      </div>
'''

            # Inject right after <div class="question-body">...</div>
            target = re.search(r'(<div class="question-body">.*?</div>\s*</div>)', content, flags=re.DOTALL)
            if target:
                insertion_pos = target.end()
                new_content = content[:insertion_pos] + solution_block + content[insertion_pos:]

                # Update Schema JSON-LD if present
                plain_answer = strip_tags(sol_html)[:300].replace('"', '\\"').replace('\n', ' ')
                schema_target = '"answerCount": 1'
                if schema_target in new_content and '"acceptedAnswer"' not in new_content:
                    replacement = f'''"answerCount": 1,
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{plain_answer}...",
        "upvoteCount": 1
      }}'''
                    new_content = new_content.replace(schema_target, replacement, 1)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated += 1
                print(f"[UPDATED] Injected solution into: {os.path.basename(os.path.dirname(file_path))}")

    print(f"[SUMMARY] Successfully injected solutions into {updated} static question pages.")

if __name__ == "__main__":
    inject_solutions()
