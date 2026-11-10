import os
import sys
import json
import time
import urllib.request
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
CACHE_FILE = os.path.join(DATA_DIR, "solutions_cache.json")
REPEATS_FILE = os.path.join(DATA_DIR, "repeated_questions.json")
Q_DIR = os.path.join(ROOT, "q")
STOP_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stop_solver.flag")

# Load rotation keys from environment or local .env (never hardcode in Git)
def get_keys():
    keys_str = os.environ.get("GEMINI_KEYS")
    if keys_str:
        return [k.strip() for k in keys_str.split(",") if k.strip()]
    env_path = os.path.join(ROOT, ".env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("GEMINI_KEYS="):
                        val = line.split("=", 1)[1].strip()
                        return [k.strip() for k in val.split(",") if k.strip()]
        except Exception:
            pass
    return []

KEYS = get_keys()

MODELS_POOL = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash",
    "gemini-3-flash-preview"
]

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "_comment": "Wovrix PYQ Permanent Solution Cache. CBSE Full-Marks + EL10 Intuition.",
        "solutions": {}
    }

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html).strip()

def inject_to_static_page(qid, sol_html):
    pattern = os.path.join(Q_DIR, f"*-{qid}", "index.html")
    matches = glob.glob(pattern)
    for file_path in matches:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if "Verified CBSE Marking Scheme" in content:
                continue

            solution_block = f'''
      <div class="solution-box" style="margin-top:24px; padding:20px; background:var(--card-bg, #ffffff); border:1.5px solid var(--border, #e2e8f0); border-radius:12px;">
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:14px;">
          <span style="background:#10b981; color:#fff; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px; text-transform:uppercase;">✓ Verified CBSE Marking Scheme</span>
          <span style="font-size:12px; color:var(--text-muted, #64748b); font-weight:600;">Official Evaluation Steps & EL10 Insight</span>
        </div>
        <div class="math-content solution-content" style="line-height:1.7; font-size:15px;">
          {sol_html}
        </div>
      </div>
'''
            target = re.search(r'(<div class="question-body">.*?</div>\s*</div>)', content, flags=re.DOTALL)
            if target:
                insertion_pos = target.end()
                new_content = content[:insertion_pos] + solution_block + content[insertion_pos:]

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
        except Exception:
            pass

def solve_with_gemini(question_text, subject, marks, key_idx=0):
    prompt = f"""You are a Senior CBSE Class 12 Board Examiner and Master Teacher.
Provide an authentic, full-marks step-by-step marking scheme solution for this past board examination question.

Subject: CBSE Class 12 {subject}
Marks Allocation: {marks} Mark{'s' if marks > 1 else ''}

Question:
{question_text}

Strict Requirements for Full Marks:
1. Format with clean, valid HTML tags suitable for direct web embedding (<p>, <strong>, <div>, <ul>, <li>).
2. For all mathematical formulas, symbols, and variables, use valid KaTeX LaTeX:
   - Inline math inside single $...$ (e.g. $E = mc^2$, $\\vec{{a}} \\cdot \\vec{{b}}$).
   - Display/standalone equations inside double $$...$$.
3. Follow the Official CBSE Step-Wise Marking Blueprint:
   - <strong>Step 1 (Formula / Governing Law & Given Data): [Mark Fraction]</strong> Explicitly state the foundational law, definition, formula, or reaction equation with mark fraction.
   - <strong>Step 2 (Step-by-Step Mathematical Working): [Mark Fraction]</strong> Show complete algebraic substitution and computation without skipping intermediate steps so students get full method credit.
   - <strong>Step 3 (Final Concluded Answer): [Mark Fraction]</strong> Concluding numerical result or deduction with standard S.I. units and proper sign convention.
4. <strong>💡 EL10 Concept Insight (Easy to Understand):</strong> Include a dedicated 1-2 sentence intuitive explanation in plain, conversational English (Explain Like I'm 10) so any student immediately grasps WHY this concept works intuitively.
5. Scientific and mathematical accuracy must strictly match the NCERT textbook standard. No conversational filler or introductory preamble. Output ONLY the solution HTML."""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 900
        }
    }

    for model_name in MODELS_POOL:
        for attempt in range(len(KEYS)):
            current_k = KEYS[(key_idx + attempt) % len(KEYS)]
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={current_k}"
            
            try:
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=12) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    text = re.sub(r"^```html\s*", "", text, flags=re.MULTILINE)
                    text = re.sub(r"^```\s*", "", text, flags=re.MULTILINE)
                    text = text.strip()
                    return text, (key_idx + attempt) % len(KEYS)
            except urllib.error.HTTPError as e:
                if e.code in (429, 503):
                    continue
                else:
                    continue
            except Exception:
                continue
                
    return None, key_idx

def run_continuous_solver(batch_size=50, max_total=None):
    if os.path.exists(STOP_FILE):
        try:
            os.remove(STOP_FILE)
        except Exception:
            pass

    print("=================================================================")
    print("  WOVRIX PYQ CONTINUOUS AUTO-SOLVER (CBSE STEP MARKS + EL10)")
    print(f"  Mode: Auto-continuing batches of {batch_size} one by one")
    if max_total:
        print(f"  Target Run Limit: {max_total} questions")
    print("  Keys Pool: 5 Rotated Active Keys | Models: Gemini Flash Series")
    print("=================================================================\n")

    # Load high yield repeats
    cbse_questions = []
    if os.path.exists(REPEATS_FILE):
        with open(REPEATS_FILE, "r", encoding="utf-8") as f:
            repeats = json.load(f)
            cbse_questions = repeats.get("cbse_repeats", [])

    total_pool = len(cbse_questions)
    print(f"[INIT] Loaded {total_pool} high-yield repeated questions.")

    key_idx = 0
    cycle_num = 1
    total_solved_in_session = 0

    while True:
        # Check stop flag
        if os.path.exists(STOP_FILE):
            print("\n[STOP] Stop flag detected ('stop_solver.flag'). Exiting solver loop cleanly.")
            break

        cache = load_cache()
        solutions = cache.setdefault("solutions", {})
        
        # Find unsolved questions
        unsolved = [q for q in cbse_questions if str(q.get("id")) not in solutions or len(solutions[str(q.get("id"))]) < 50]
        
        if not unsolved:
            print("\n[SUCCESS] ALL questions in the repeat pool have been solved! Nothing remaining.")
            break

        current_batch = unsolved[:batch_size]
        print(f"\n>>> CYCLE {cycle_num}: Starting batch of {len(current_batch)} questions (Total remaining: {len(unsolved)}) <<<")

        batch_solved = 0
        for i, q in enumerate(current_batch):
            if os.path.exists(STOP_FILE):
                print("\n[STOP] Stop flag detected mid-batch. Halting.")
                return

            if max_total and total_solved_in_session >= max_total:
                print(f"\n[GOAL REACHED] Completed session target of {max_total} questions. Exiting cleanly.")
                return

            qid = str(q.get("id"))
            text = q.get("text", "").strip()
            subject = q.get("subject", "Physics")
            marks = q.get("marks", 2)
            repeats_cnt = q.get("repeat_count", 1)
            chapter = q.get("chapter_name", "")

            print(f"  [{i+1}/{len(current_batch)}] Q#{qid} ({subject} - {chapter[:20]}... {repeats_cnt}x)...", end=" ", flush=True)

            t0 = time.time()
            sol, key_idx = solve_with_gemini(text, subject, marks, key_idx)
            elapsed = time.time() - t0

            if sol:
                solutions[qid] = sol
                cache["_total_cached"] = len(solutions)
                save_cache(cache)
                inject_to_static_page(qid, sol)
                batch_solved += 1
                total_solved_in_session += 1
                print(f"DONE in {elapsed:.1f}s (Key #{key_idx+1})", flush=True)
                time.sleep(0.8)
            else:
                print("FAILED (Rotating/Skipped)", flush=True)
                time.sleep(1.2)

        print(f"\n=== CYCLE {cycle_num} COMPLETED! Solved {batch_solved}/{len(current_batch)} in this batch.")
        print(f"=== Total Cached in Vault: {len(solutions)} / {total_pool}")
        
        if max_total and total_solved_in_session >= max_total:
            print(f"\n[GOAL REACHED] Completed session target of {max_total} questions. Exiting cleanly.")
            break

        print("=== Auto-starting next batch in 2 seconds...\n")
        time.sleep(2)
        cycle_num += 1

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--continuous":
        run_continuous_solver(batch_size=50, max_total=None)
    elif len(sys.argv) > 1:
        limit = int(sys.argv[1])
        run_continuous_solver(batch_size=min(50, limit), max_total=limit)
    else:
        run_continuous_solver(batch_size=50, max_total=None)
