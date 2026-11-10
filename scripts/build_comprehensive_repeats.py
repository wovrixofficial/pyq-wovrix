import os
import json
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
REPEATED_JSON = os.path.join(DATA_DIR, "repeated_questions.json")
MD_PATH = os.path.join(os.path.dirname(ROOT), "neet-ug-portal", "NEET_Most_Repeated_Questions_10_Years.md")

def clean_for_repeat(text):
    if not text:
        return ""
    # Strip question number e.g. "Q. 12", "14.", "Question 19:"
    t = re.sub(r'^(?:Question|Q\.?)\s*(?:number)?\s*\d+(?:\s*(?:to|and)\s*\d+)?[\.:\s]*', '', text, flags=re.I)
    # Strip marks indicators e.g. "(1 mark)", "[2 marks]", "[Marks : 3]"
    t = re.sub(r'\[\s*(?:Marks?\s*[:=]?\s*)?\d+\s*(?:Marks?)?\s*\]', '', t, flags=re.I)
    t = re.sub(r'\(\s*(?:Marks?\s*[:=]?\s*)?\d+\s*(?:Marks?)?\s*\)', '', t, flags=re.I)
    # Normalize LaTeX formulas
    t = re.sub(r'\\text\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\mathrm\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\mathbf\{([^}]*)\}', r'\1', t)
    t = re.sub(r'[\$\{\}]', '', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    t = re.sub(r'\b(\d+)\.0\b', r'\1', t)
    t = re.sub(r'[^a-z0-9\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def extract_numbers(text):
    return set(re.findall(r'\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b', text))

def scan_cbse_comprehensive():
    datasets = {
        'Physics': os.path.join(DATA_DIR, 'cbse_physics.json'),
        'Chemistry': os.path.join(DATA_DIR, 'cbse_chemistry.json'),
        'Mathematics': os.path.join(DATA_DIR, 'cbse_mathematics.json')
    }

    all_questions = []
    for subj, path in datasets.items():
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            qs = json.load(f)
        for q in qs:
            q['subject'] = subj
            all_questions.append(q)

    print(f"[CBSE] Total questions scanned across all sets: {len(all_questions)}")

    # Index by cleaned prefix (12 words) to avoid restriction by chapter or marks
    groups = defaultdict(list)
    for q in all_questions:
        raw_txt = q.get('text', '')
        if len(raw_txt.strip()) < 15:
            continue
        norm = clean_for_repeat(raw_txt)
        if len(norm) < 15:
            continue
        words = norm.split()
        prefix = " ".join(words[:12])
        nums = tuple(sorted(list(extract_numbers(raw_txt))))
        groups[(q['subject'], prefix, nums)].append(q)

    cbse_repeats = []
    for (subj, prefix, nums), cluster in groups.items():
        if len(cluster) < 2:
            continue
        
        # Sort cluster by year
        cluster.sort(key=lambda x: str(x.get('year', '')), reverse=True)
        primary = cluster[0]
        
        years = sorted(list({str(q.get('year', '')) for q in cluster if q.get('year')}), reverse=True)
        rep_count = len(cluster)
        
        cbse_repeats.append({
            "id": primary.get('id', f"cbse_rep_{len(cbse_repeats)+1}"),
            "subject": subj,
            "chapter_number": primary.get('chapter_number', 1),
            "chapter_name": primary.get('chapter_name', 'General'),
            "marks": primary.get('marks', 1),
            "text": primary.get('text', ''),
            "repeat_count": rep_count,
            "unique_years_count": len(years),
            "years": years,
            "is_multi_year": len(years) > 1,
            "type": f"Core Clone ({rep_count}x Frequency across sets)",
            "slug": f"cbse-rep-{primary.get('id', '')}"
        })

    # Sort descending by repeat count
    cbse_repeats.sort(key=lambda x: (x['repeat_count'], x['unique_years_count']), reverse=True)
    print(f"[CBSE] Verified repeat clusters found: {len(cbse_repeats)}. Max repeats: {cbse_repeats[0]['repeat_count'] if cbse_repeats else 0}x")
    return cbse_repeats, len(all_questions)

def scan_neet_comprehensive():
    neet_path = os.path.join(DATA_DIR, 'neet_all.json')
    if not os.path.exists(neet_path):
        return [], 0

    with open(neet_path, 'r', encoding='utf-8') as f:
        neet_qs = json.load(f)

    print(f"[NEET] Total questions scanned across all years: {len(neet_qs)}")

    groups = defaultdict(list)
    for q in neet_qs:
        raw_txt = q.get('text', '')
        if len(raw_txt.strip()) < 15:
            continue
        norm = clean_for_repeat(raw_txt)
        if len(norm) < 15:
            continue
        words = norm.split()
        prefix = " ".join(words[:10])
        nums = tuple(sorted(list(extract_numbers(raw_txt))))
        groups[(q.get('subject', 'General'), prefix, nums)].append(q)

    neet_repeats = []
    for (subj, prefix, nums), cluster in groups.items():
        if len(cluster) < 2:
            continue
        cluster.sort(key=lambda x: str(x.get('year', '')), reverse=True)
        primary = cluster[0]
        years = sorted(list({str(q.get('year', '')) for q in cluster if q.get('year')}), reverse=True)
        rep_count = len(cluster)

        neet_repeats.append({
            "id": primary.get('id', f"neet_rep_{len(neet_repeats)+1}"),
            "subject": subj,
            "ncert_chapter": primary.get('ncert_chapter', 'General'),
            "text": primary.get('text', ''),
            "options": primary.get('options', {}),
            "correct_answer": primary.get('correct_answer', 'A'),
            "repeat_count": rep_count,
            "unique_years_count": len(years),
            "years": years,
            "is_multi_year": len(years) > 1,
            "type": f"Core Clone ({rep_count}x Frequency)",
            "slug": f"neet-rep-{primary.get('id', '')}"
        })

    # Also parse curated markdown if exists
    curated_repeats = []
    if os.path.exists(MD_PATH):
        with open(MD_PATH, 'r', encoding='utf-8') as f:
            text = f.read().replace('\r\n', '\n')
        sections = re.split(r'\n###\s+(\d+\..*?)\n', text)
        for i in range(1, len(sections), 2):
            header = sections[i].strip()
            body = sections[i+1] if i+1 < len(sections) else ""
            m_head = re.match(r'\d+\.\s*(.*?)\s*•\s*(Physics|Chemistry|Botany|Zoology)\s*\((.*?)\)', header)
            if not m_head: continue
            concept_name, subj, meta = m_head.groups()
            m_count = re.search(r'(\d+)\s+Questions', meta)
            rep_count = int(m_count.group(1)) if m_count else 2
            m_years = re.search(r'Appeared in:\s*(.*)', meta)
            years_list = [y.strip() for y in m_years.group(1).split(',')] if m_years else []

            q_blocks = re.split(r'\n####\s+\*\*\[(.*?)\]\s+(.*?)\*\*\n', body)
            for j in range(1, len(q_blocks), 3):
                qid = q_blocks[j].strip()
                q_body = q_blocks[j+2].strip() if j+2 < len(q_blocks) else ""
                options = {}
                for opt_m in re.finditer(r'-\s+\*\*\(?([A-D])\)?\*\*\s*(.*)', q_body):
                    options[opt_m.group(1)] = opt_m.group(2).replace('*(Correct Answer)*', '').strip()
                m_ans = re.search(r'\*\*Official Key\*\*:\s*Option\s*\*\*\(?([A-D])\)?\*\*', q_body)
                correct_ans = m_ans.group(1) if m_ans else 'A'
                clean_q = re.split(r'\n-\s+\*\*\(?[A-D]', q_body)[0].strip()
                clean_q = re.split(r'\n\*\*Official Key\*\*:', clean_q)[0].strip()

                curated_repeats.append({
                    "id": qid,
                    "subject": subj,
                    "ncert_chapter": concept_name,
                    "text": clean_q,
                    "options": options,
                    "correct_answer": correct_ans,
                    "repeat_count": rep_count,
                    "unique_years_count": len(years_list),
                    "years": years_list,
                    "is_multi_year": len(years_list) > 1,
                    "type": f"High-Yield Archetype ({rep_count}x Frequency)",
                    "concept_name": concept_name,
                    "slug": f"neet-{qid.lower()}"
                })

    # Merge curated with exact-text clones
    curated_ids = {q['id'] for q in curated_repeats}
    filtered_clones = [q for q in neet_repeats if q['id'] not in curated_ids]
    all_neet = curated_repeats + filtered_clones
    all_neet.sort(key=lambda x: (x['repeat_count'], x['unique_years_count']), reverse=True)

    print(f"[NEET] Combined repeat intelligence: {len(all_neet)} patterns. Max repeats: {all_neet[0]['repeat_count'] if all_neet else 0}x")
    return all_neet, len(neet_qs)

def main():
    cbse_repeats, cbse_total = scan_cbse_comprehensive()
    neet_repeats, neet_total = scan_neet_comprehensive()

    # Count high-repeat items (> 5 times)
    cbse_high = [q for q in cbse_repeats if q['repeat_count'] >= 5]
    neet_high = [q for q in neet_repeats if q['repeat_count'] >= 5]
    print(f"\n[SUMMARY] CBSE questions appearing >= 5 times: {len(cbse_high)}")
    print(f"[SUMMARY] NEET questions appearing >= 5 times: {len(neet_high)}")

    data = {
        "summary": {
            "cbse_total_questions": cbse_total,
            "cbse_verified_repeat_clusters": len(cbse_repeats),
            "cbse_repeats_gte_5x": len(cbse_high),
            "cbse_max_repeats": cbse_repeats[0]['repeat_count'] if cbse_repeats else 0,
            "neet_total_questions": neet_total,
            "neet_verified_repeat_clusters": len(neet_repeats),
            "neet_repeats_gte_5x": len(neet_high),
            "neet_max_repeats": neet_repeats[0]['repeat_count'] if neet_repeats else 0
        },
        "cbse_repeats": cbse_repeats,
        "neet_repeats": neet_repeats
    }

    with open(REPEATED_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] Saved {len(cbse_repeats)} CBSE repeats & {len(neet_repeats)} NEET repeats to {REPEATED_JSON}")

if __name__ == "__main__":
    main()
