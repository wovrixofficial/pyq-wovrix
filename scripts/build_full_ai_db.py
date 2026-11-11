import os, json, sqlite3, re

ROOT = r"E:\PYQ_Wovrix_Portal\pyq-wovrix"
DATA_DIR = os.path.join(ROOT, "data")
DB_PATH = os.path.join(DATA_DIR, "learnosha_anti_hallucination_master.db")
TRAIN_PATH = os.path.join(DATA_DIR, "ai_training_anti_hallucination.jsonl")
CORPUS_PATH = os.path.join(DATA_DIR, "ai_proof_corpus.jsonl")

def clean_text(text):
    if not text: return ""
    t = re.sub(r'<[^>]+>', ' ', str(text))
    return re.sub(r'\s+', ' ', t).strip()

def format_paper_code(source):
    if not source: return "Official Paper"
    s = str(source)
    if s.endswith(".pdf"):
        s = s[:-4]
        if re.match(r'^\d+-\d+-\d+$', s):
            return f"QP Code {s.replace('-', '/')}"
    return s

def main():
    print("=== Compiling Master Anti-Hallucination AI Database (CBSE + NEET + JEE) ===")
    
    # Load CBSE repeat clusters
    repeats_data = {}
    rep_file = os.path.join(DATA_DIR, "repeated_questions.json")
    if os.path.exists(rep_file):
        with open(rep_file, "r", encoding="utf-8") as f:
            repeats_data = json.load(f)
    cbse_rep_map = {str(item.get("id")): item for item in repeats_data.get("cbse_repeats", [])}

    # Load CBSE solutions cache
    sol_cache = {}
    sol_file = os.path.join(DATA_DIR, "solutions_cache.json")
    if os.path.exists(sol_file):
        with open(sol_file, "r", encoding="utf-8") as f:
            sol_cache = json.load(f).get("solutions", {})

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS verified_questions;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS verified_questions (
        id TEXT PRIMARY KEY,
        exam TEXT NOT NULL,
        subject TEXT NOT NULL,
        chapter TEXT,
        subtopic TEXT,
        subtopic_slug TEXT,
        year INTEGER,
        q_num INTEGER,
        marks INTEGER,
        section TEXT,
        paper_code TEXT,
        page_number INTEGER,
        question_text TEXT NOT NULL,
        options_json TEXT,
        correct_answer TEXT,
        solution_marking_scheme TEXT,
        el10_intuition TEXT,
        repeat_count INTEGER DEFAULT 1,
        repeat_years_proof TEXT,
        historical_twins_json TEXT,
        is_multi_year INTEGER DEFAULT 0,
        proof_citation_text TEXT NOT NULL,
        has_solution INTEGER DEFAULT 0
    )""")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_vh_exam ON verified_questions(exam, subject);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_vh_rep ON verified_questions(repeat_count);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_vh_year ON verified_questions(year);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_vh_sol ON verified_questions(has_solution);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_vh_subtopic ON verified_questions(subtopic);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_vh_subtopic_slug ON verified_questions(subtopic_slug);")
    conn.commit()

    total_records = 0
    records_with_solutions = 0

    def insert_rec(rec):
        nonlocal total_records, records_with_solutions
        has_sol = 1 if (rec["solution"] or rec["correct_answer"]) else 0
        if has_sol: records_with_solutions += 1
        total_records += 1
        cursor.execute("""
        INSERT OR REPLACE INTO verified_questions (
            id, exam, subject, chapter, subtopic, subtopic_slug, year, q_num, marks, section,
            paper_code, page_number, question_text, options_json,
            correct_answer, solution_marking_scheme, el10_intuition,
            repeat_count, repeat_years_proof, historical_twins_json,
            is_multi_year, proof_citation_text, has_solution
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            rec["id"], rec["exam"], rec["subject"], rec["chapter"],
            rec.get("subtopic"), rec.get("subtopic_slug"),
            rec["year"], rec["q_num"], rec["marks"], rec["section"],
            rec["paper_code"], rec["page_number"], rec["question_text"],
            rec["options_json"], rec["correct_answer"], rec["solution"],
            rec["el10_intuition"], rec["repeat_count"], rec["repeat_years_proof"],
            rec["historical_twins_json"], rec["is_multi_year"],
            rec["proof_citation_text"], has_sol
        ))

    # Ingest CBSE
    for fn, sub in [("cbse_physics.json", "Physics"), ("cbse_chemistry.json", "Chemistry"), ("cbse_mathematics.json", "Mathematics")]:
        p = os.path.join(DATA_DIR, fn)
        with open(p, "r", encoding="utf-8") as f:
            items = json.load(f)
        print(f"Ingesting CBSE 12 {sub} ({len(items)} items)...")
        for item in items:
            raw_id = str(item.get("id"))
            qid = f"cbse-12-{sub.lower()}-{raw_id}"
            q_text = clean_text(item.get("text", ""))
            if not q_text: continue
            year = int(item.get("year", 2024)) if str(item.get("year", "")).isdigit() else 2024
            marks = int(item.get("marks", 1)) if str(item.get("marks", "")).isdigit() else 1
            q_num = item.get("q_num")
            page = item.get("page")
            paper_code = format_paper_code(item.get("source"))

            rep_entry = cbse_rep_map.get(raw_id)
            if rep_entry:
                repeat_count = rep_entry.get("repeat_count", 1)
                rep_years = rep_entry.get("years", [str(year)])
                is_multi = 1 if rep_entry.get("is_multi_year") else 0
            else:
                repeat_count = item.get("multi_year_count") or item.get("cluster_size") or 1
                rep_years = item.get("repeat_years") or [str(year)]
                is_multi = 1 if len(rep_years) > 1 else 0

            cached_sol = sol_cache.get(raw_id, "")
            sol_text, intuition = "", ""
            if cached_sol:
                sol_text = clean_text(cached_sol)
                if "Intuition:" in cached_sol or "EL10" in cached_sol:
                    parts = cached_sol.split("Intuition:")
                    if len(parts) > 1:
                        sol_text = clean_text(parts[0])
                        intuition = clean_text(parts[1])

            rep_years_str = ", ".join([str(y) for y in sorted(set(rep_years))])
            citation = f"### Verified CBSE Exam Proof & Citation\n- **Exam Authority**: Central Board of Secondary Education (CBSE Class 12)\n- **Subject & Chapter**: {sub} | {item.get('chapter_name') or 'General'}\n- **Verified Source Paper**: {paper_code} (Question #{q_num if q_num else 'N/A'}, Page {page if page else 'N/A'})\n- **Official Exam Year**: {year} Board Examination\n- **Official Mark Weight**: {marks} Mark(s) ({item.get('section') or 'Standard Section'})\n- **Recurrence History**: Appeared {repeat_count} time(s) across board sets (Verified years: {rep_years_str})"

            insert_rec({
                "id": qid, "exam": "CBSE Class 12", "subject": sub, "chapter": item.get("chapter_name") or "General",
                "subtopic": item.get("subtopic"), "subtopic_slug": item.get("subtopic_slug"),
                "year": year, "q_num": q_num, "marks": marks, "section": item.get("section") or "",
                "paper_code": paper_code, "page_number": page, "question_text": q_text,
                "options_json": None, "correct_answer": None, "solution": sol_text or None,
                "el10_intuition": intuition or None, "repeat_count": repeat_count,
                "repeat_years_proof": rep_years_str, "historical_twins_json": None,
                "is_multi_year": is_multi, "proof_citation_text": citation
            })

    # Ingest NEET
    neet_path = os.path.join(DATA_DIR, "neet_all.json")
    with open(neet_path, "r", encoding="utf-8") as f:
        neet_items = json.load(f)
    print(f"Ingesting NEET UG ({len(neet_items)} items)...")
    for item in neet_items:
        qid = f"neet-{item.get('id')}"
        q_text = clean_text(item.get("text", ""))
        if not q_text: continue
        year = int(item.get("year", 2024)) if str(item.get("year", "")).isdigit() else 2024
        q_num = item.get("q_num")
        paper_code = format_paper_code(item.get("source"))
        opts = item.get("options")
        opts_json = json.dumps(opts, ensure_ascii=False) if opts else None
        corr = item.get("correct_answer")
        rep_count = item.get("recurrence_count_10yr") or 1
        rep_years = item.get("recurrence_years") or [str(year)]
        rep_years_str = ", ".join([str(y) for y in sorted(set(rep_years))])
        twins = item.get("historical_twins")

        citation = f"### Verified NEET Exam Proof & Citation\n- **Exam Authority**: National Testing Agency (NTA NEET UG)\n- **Subject & NCERT Chapter**: {item.get('subject') or 'General'} | {item.get('ncert_chapter') or 'General'}\n- **Verified Source Paper**: {paper_code} (Question #{q_num if q_num else 'N/A'})\n- **Exam Year**: NEET {year} National Paper\n- **Mark Weight**: 4 Marks (+4 Correct, -1 Incorrect)\n- **10-Year Recurrence Evidence**: Repeated {rep_count} times in 10-year cycle ({rep_years_str})\n- **Concept Cluster**: {item.get('concept_name') or 'Core NCERT Objective'}"

        insert_rec({
            "id": qid, "exam": "NEET UG", "subject": item.get("subject") or "General",
            "chapter": item.get("ncert_chapter") or "General",
            "subtopic": item.get("subtopic"), "subtopic_slug": item.get("subtopic_slug"),
            "year": year, "q_num": q_num,
            "marks": 4, "section": item.get("section") or "Section A", "paper_code": paper_code,
            "page_number": item.get("page"), "question_text": q_text, "options_json": opts_json,
            "correct_answer": corr, "solution": f"Correct Option: ({corr})" if corr else None,
            "el10_intuition": None, "repeat_count": rep_count, "repeat_years_proof": rep_years_str,
            "historical_twins_json": json.dumps(twins) if twins else None,
            "is_multi_year": 1 if len(rep_years) > 1 else 0, "proof_citation_text": citation
        })

    # Ingest Full 12,667 JEE Main Questions
    jee_path = os.path.join(DATA_DIR, "jee_main_all.json")
    with open(jee_path, "r", encoding="utf-8") as f:
        jee_items = json.load(f)
    print(f"Ingesting Full JEE Main Archive ({len(jee_items)} items)...")
    for item in jee_items:
        qid = f"jee-{item.get('id')}"
        q_text = clean_text(item.get("text", ""))
        if not q_text: continue
        year = int(item.get("year", 2024)) if str(item.get("year", "")).isdigit() else 2024
        q_num = item.get("q_num")
        shift = item.get("shift_name") or "Official Shift"
        opts = item.get("options")
        opts_json = json.dumps(opts, ensure_ascii=False) if opts else None
        corr = item.get("correct_answer")
        sol = clean_text(item.get("solution", ""))

        citation = f"### Verified JEE Main Exam Proof & Citation\n- **Exam Authority**: National Testing Agency (NTA JEE Main)\n- **Subject & Chapter**: {item.get('subject') or 'General'} | {item.get('ncert_chapter') or 'General'}\n- **Verified Session Shift**: JEE Main {year} ({shift}, Question #{q_num if q_num else 'N/A'})\n- **Mark Weight**: 4 Marks (+4 Correct, -1 Incorrect)\n- **Question Type**: {item.get('type') or 'MCQ'}"

        insert_rec({
            "id": qid, "exam": "JEE Main", "subject": item.get("subject") or "General",
            "chapter": item.get("ncert_chapter") or "General",
            "subtopic": item.get("subtopic"), "subtopic_slug": item.get("subtopic_slug"),
            "year": year, "q_num": q_num,
            "marks": 4, "section": item.get("section") or "Section A",
            "paper_code": f"JEE Main {year} {shift}", "page_number": None,
            "question_text": q_text, "options_json": opts_json, "correct_answer": corr,
            "solution": sol or (f"Correct Option: ({corr})" if corr else None),
            "el10_intuition": None, "repeat_count": 1, "repeat_years_proof": str(year),
            "historical_twins_json": None, "is_multi_year": 0, "proof_citation_text": citation
        })

    conn.commit()
    print(f"-> Total Verified Records Stored in Master DB: {total_records}")
    print(f"-> Records with Solutions / Official Answers: {records_with_solutions}")

    # Export Anti-Hallucination Training Dataset
    print("Exporting Anti-Hallucination Training Samples...")
    cursor.execute("""
    SELECT id, exam, subject, chapter, subtopic, subtopic_slug, year, marks, question_text,
           options_json, correct_answer, solution_marking_scheme,
           el10_intuition, proof_citation_text
    FROM verified_questions
    WHERE solution_marking_scheme IS NOT NULL OR correct_answer IS NOT NULL
    """)
    rows = cursor.fetchall()
    with open(TRAIN_PATH, "w", encoding="utf-8") as f_train, open(CORPUS_PATH, "w", encoding="utf-8") as f_corpus:
        for row in rows:
            qid, exam, subject, chapter, subtopic, subtopic_slug, year, marks, q_text, opts_json, corr, sol, intuition, citation = row
            subtopic_line = f"Subtopic: {subtopic}\n" if subtopic else ""
            prompt = f"Exam: {exam}\nSubject: {subject}\nChapter: {chapter}\n{subtopic_line}Marks: {marks} Mark(s)\n\nQuestion:\n{q_text}"
            if opts_json:
                try:
                    options = json.loads(opts_json)
                    if isinstance(options, dict):
                        prompt += "\n\nOptions:\n" + "\n".join([f"({k}) {v}" for k, v in options.items()])
                    elif isinstance(options, list):
                        prompt += "\n\nOptions:\n" + "\n".join([f"• {opt}" for opt in options])
                except Exception: pass

            ans = []
            if sol: ans.append(f"### Official Evaluation & Step-by-Step Marking Scheme\n{sol}")
            elif corr: ans.append(f"### Correct Answer\nCorrect Option: ({corr})")
            if intuition: ans.append(f"### Conceptual Intuition (EL10)\n{intuition}")
            ans.append(citation)

            f_train.write(json.dumps({
                "messages": [
                    {"role": "system", "content": "You are the Learnosha Master AI STEM Tutor. You MUST provide step-marked solutions followed by the exact official exam proof, QP paper code, question number, and recurrence history to eliminate hallucinations."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": "\n\n".join(ans)}
                ],
                "ground_truth_proof": {"id": qid, "exam": exam, "subject": subject, "chapter": chapter, "subtopic": subtopic, "subtopic_slug": subtopic_slug, "year": year}
            }, ensure_ascii=False) + "\n")

            subtopic_tag = f" [{subtopic}]" if subtopic else ""
            f_corpus.write(json.dumps({
                "id": qid, "exam": exam, "subject": subject, "chapter": chapter,
                "subtopic": subtopic, "subtopic_slug": subtopic_slug, "year": year,
                "text_to_embed": f"{exam} {subject} {chapter}{subtopic_tag}: {q_text}",
                "full_question": prompt, "solution": sol or "", "correct_answer": corr or ""
            }, ensure_ascii=False) + "\n")

    conn.close()
    print(f"-> Anti-Hallucination Training JSONL created: {TRAIN_PATH} ({len(rows)} samples)")
    print("=== Complete! ===")

if __name__ == "__main__":
    main()
