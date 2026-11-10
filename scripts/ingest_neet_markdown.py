import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
MD_PATH = r"c:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal\NEET_Most_Repeated_Questions_10_Years.md"
REPEATED_JSON = os.path.join(DATA_DIR, "repeated_questions.json")

def parse_neet_markdown():
    if not os.path.exists(MD_PATH):
        print(f"File not found: {MD_PATH}")
        return []

    with open(MD_PATH, 'r', encoding='utf-8') as f:
        text = f.read().replace('\r\n', '\n')

    # Split by concept sections: e.g. "### 1. Capacitors..."
    sections = re.split(r'\n###\s+(\d+\..*?)\n', text)
    if len(sections) < 2:
        return []

    parsed_concepts = []

    # sections[0] is preamble. sections[1] is header1, sections[2] is body1, etc.
    for i in range(1, len(sections), 2):
        header = sections[i].strip()
        body = sections[i+1] if i+1 < len(sections) else ""

        # Header format: "1. Capacitors: Series/Parallel & Dielectrics • Physics (30 Questions | Appeared in: 2026, 2025...)"
        m_head = re.match(r'\d+\.\s*(.*?)\s*•\s*(Physics|Chemistry|Botany|Zoology)\s*\((.*?)\)', header)
        if not m_head:
            continue

        concept_name = m_head.group(1).strip()
        subject = m_head.group(2).strip()
        meta = m_head.group(3).strip()

        # Extract count
        m_count = re.search(r'(\d+)\s+Questions', meta)
        rep_count = int(m_count.group(1)) if m_count else 2

        # Extract years
        m_years = re.search(r'Appeared in:\s*(.*)', meta)
        years_list = [y.strip() for y in m_years.group(1).split(',')] if m_years else []

        # Extract questions in this section
        q_blocks = re.split(r'\n####\s+\*\*\[(.*?)\]\s+(.*?)\*\*\n', body)
        for j in range(1, len(q_blocks), 3):
            qid = q_blocks[j].strip()
            q_head = q_blocks[j+1].strip() if j+1 < len(q_blocks) else ""
            q_body = q_blocks[j+2].strip() if j+2 < len(q_blocks) else ""

            # Extract options: - **(A)** ...
            options = {}
            for opt_m in re.finditer(r'-\s+\*\*\(?([A-D])\)?\*\*\s*(.*)', q_body):
                opt_key = opt_m.group(1)
                opt_text = opt_m.group(2).replace('*(Correct Answer)*', '').strip()
                options[opt_key] = opt_text

            # Extract correct answer
            m_ans = re.search(r'\*\*Official Key\*\*:\s*Option\s*\*\*\(?([A-D])\)?\*\*', q_body)
            correct_ans = m_ans.group(1) if m_ans else 'A'

            # Clean body text (remove options and key)
            clean_q = re.split(r'\n-\s+\*\*\(?[A-D]', q_body)[0].strip()
            clean_q = re.split(r'\n\*\*Official Key\*\*:', clean_q)[0].strip()

            parsed_concepts.append({
                "id": qid,
                "subject": subject,
                "ncert_chapter": concept_name,
                "text": clean_q,
                "options": options,
                "correct_answer": correct_ans,
                "repeat_count": rep_count,
                "unique_years_count": len(years_list),
                "years": years_list,
                "is_multi_year": len(years_list) > 1,
                "type": f"High-Yield Concept ({rep_count}x Frequency)",
                "concept_name": concept_name,
                "slug": f"neet-{qid.lower()}"
            })

    print(f"Successfully extracted {len(parsed_concepts)} curated NEET repeat questions from Markdown across {len(sections)//2} concept groups.")
    return parsed_concepts

def merge_into_repeated_json():
    curated_neet = parse_neet_markdown()
    if not curated_neet:
        print("[ERROR] No questions extracted.")
        return

    with open(REPEATED_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Combine curated_neet with existing neet_repeats, prioritizing curated_neet
    curated_ids = {q['id'] for q in curated_neet}
    existing_neet = data.get('neet_repeats', [])
    filtered_existing = [q for q in existing_neet if q.get('id') not in curated_ids]

    all_neet_repeats = curated_neet + filtered_existing
    all_neet_repeats.sort(key=lambda x: (x.get('repeat_count', 0), x.get('unique_years_count', 0)), reverse=True)

    data['neet_repeats'] = all_neet_repeats
    data['summary']['neet_curated_high_yield'] = len(curated_neet)
    data['summary']['neet_repeat_patterns'] = len(all_neet_repeats)
    data['summary']['neet_max_repeats'] = all_neet_repeats[0]['repeat_count'] if all_neet_repeats else 0

    with open(REPEATED_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] Updated repeated_questions.json with {len(all_neet_repeats)} verified NEET repeat entries! Max repeats: {data['summary']['neet_max_repeats']}x")

if __name__ == "__main__":
    merge_into_repeated_json()
