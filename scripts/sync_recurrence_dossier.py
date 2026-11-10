import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
REPEATED_JSON = os.path.join(DATA_DIR, "repeated_questions.json")
MD_PATH = os.path.join(os.path.dirname(ROOT), "neet-ug-portal", "NEET_Most_Repeated_Questions_10_Years.md")

def parse_recurrence_dossier():
    if not os.path.exists(MD_PATH):
        print(f"[ERROR] Markdown file not found at {MD_PATH}")
        return []

    with open(MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # 1. Parse leaderboard table
    # | Rank | High-Yield Concept | Subject | Total Qs | Exam Frequency | Exact Years Tested |
    leaderboard = {}
    table_pattern = re.compile(r'\|\s*(\d+)\s*\|\s*\*\*(.*?)\*\*\s*\|\s*(\w+)\s*\|\s*\*\*(\d+)\s*Qs\*\*\s*\|\s*(\d+/\d+\s*yrs\s*\(\d+%\))\s*\|\s*`(.*?)`\s*\|')
    for m in table_pattern.finditer(content):
        rank = int(m.group(1))
        concept = m.group(2).strip()
        subj = m.group(3).strip()
        total_qs = int(m.group(4))
        freq = m.group(5).strip()
        years = [y.strip() for y in m.group(6).split(',')]
        leaderboard[concept] = {
            "rank": rank,
            "concept": concept,
            "subject": subj,
            "total_qs": total_qs,
            "frequency_str": freq,
            "years": years
        }

    print(f"[DOSSIER] Parsed {len(leaderboard)} leaderboard concepts from markdown table.")

    # 2. Parse Section Deep-Dives
    # ### <rank>. <concept> • <subject>
    section_regex = re.compile(r'\n###\s+(\d+)\.\s+(.*?)\s*•\s*(\w+)\n(.*?)(?=\n###|\Z)', re.DOTALL)
    
    concepts_data = []
    for sec in section_regex.finditer(content):
        rank = int(sec.group(1))
        concept_name = sec.group(2).strip()
        subject = sec.group(3).strip()
        body = sec.group(4)

        # Extract volume, frequency, and twin IDs
        m_vol = re.search(r'\*\*10-Year Question Volume\*\*:\s*\*\*(\d+)\s+Questions?\*\*', body)
        total_qs = int(m_vol.group(1)) if m_vol else (leaderboard.get(concept_name, {}).get('total_qs', 1))

        m_freq = re.search(r'\*\*Exam Cycle Frequency\*\*:\s*Tested in\s*\*\*(.*?)\*\*\s*\((.*?)\)', body)
        freq_str = m_freq.group(1) if m_freq else ""
        years_str = m_freq.group(2) if m_freq else ""
        years_list = [y.strip(' `') for y in years_str.split(',') if y.strip(' `')]

        m_twins = re.search(r'\*\*All Historical Twin IDs\*\*:\s*`?(.*?)`?\n', body)
        twin_ids = []
        if m_twins:
            raw_twins = m_twins.group(1).replace('`', '')
            twin_ids = [t.strip() for t in raw_twins.split(',') if t.strip()]

        # Extract representative questions
        # ##### **[NEET_2026_Q052] NEET 2026 (Q52) • Chemistry • General Chemistry**
        q_regex = re.compile(r'#####\s+\*\*\[(.*?)\]\s+(.*?)\*\*\n(.*?)(?=#####|\Z)', re.DOTALL)
        rep_questions = []
        for q_m in q_regex.finditer(body):
            qid = q_m.group(1).strip()
            q_header = q_m.group(2).strip()
            q_content = q_m.group(3).strip()

            options = {}
            for opt_m in re.finditer(r'-\s+\*\*\(?([A-D])\)?\*\*\s*(.*)', q_content):
                options[opt_m.group(1)] = opt_m.group(2).replace('*(Official NTA Correct Key)*', '').replace('*(Correct Answer)*', '').strip()

            ans_m = re.search(r'\*\*Official Key\*\*:\s*Option\s*\*\*\(?([A-D])\)?\*\*', q_content)
            correct_key = ans_m.group(1) if ans_m else 'A'

            # Clean question text
            q_text = re.split(r'\n-\s+\*\*\(?[A-D]', q_content)[0].strip()
            q_text = re.split(r'\n\*\*Official Key\*\*:', q_text)[0].strip()

            rep_questions.append({
                "id": qid,
                "header": q_header,
                "text": q_text,
                "options": options,
                "correct_answer": correct_key
            })

        concepts_data.append({
            "rank": rank,
            "concept_name": concept_name,
            "subject": subject,
            "total_questions": total_qs,
            "frequency_label": freq_str,
            "years_tested": years_list if years_list else leaderboard.get(concept_name, {}).get('years', []),
            "years_count": len(years_list) if years_list else len(leaderboard.get(concept_name, {}).get('years', [])),
            "historical_twin_ids": twin_ids,
            "twin_count": len(twin_ids),
            "representative_questions": rep_questions
        })

    # Also add leaderboard entries 41-119 that don't have detailed ### sections
    covered_ranks = {c['rank'] for c in concepts_data}
    for concept_name, l_info in leaderboard.items():
        if l_info['rank'] not in covered_ranks:
            concepts_data.append({
                "rank": l_info['rank'],
                "concept_name": concept_name,
                "subject": l_info['subject'],
                "total_questions": l_info['total_qs'],
                "frequency_label": l_info['frequency_str'],
                "years_tested": l_info['years'],
                "years_count": len(l_info['years']),
                "historical_twin_ids": [],
                "twin_count": 0,
                "representative_questions": []
            })

    # Sort by rank
    concepts_data.sort(key=lambda x: x['rank'])
    print(f"[DOSSIER] Successfully synthesized {len(concepts_data)} total concept tiers (40 deep-dives + {len(concepts_data)-40} leaderboard tiers).")
    return concepts_data

def sync_all():
    neet_concepts = parse_recurrence_dossier()

    # Load existing CBSE repeats
    cbse_repeats = []
    if os.path.exists(REPEATED_JSON):
        with open(REPEATED_JSON, 'r', encoding='utf-8') as f:
            existing = json.load(f)
            cbse_repeats = existing.get('cbse_repeats', [])

    # Flatten NEET concepts into actionable question clusters for the radar
    flattened_neet_repeats = []
    for c in neet_concepts:
        # Use first representative question or create archetype
        rep = c['representative_questions'][0] if c['representative_questions'] else None
        flattened_neet_repeats.append({
            "id": rep['id'] if rep else f"NEET_CONCEPT_{c['rank']:03d}",
            "rank": c['rank'],
            "subject": c['subject'],
            "concept_name": c['concept_name'],
            "ncert_chapter": c['concept_name'].split(':')[0].strip(),
            "text": rep['text'] if rep else f"Concept Focus: {c['concept_name']}",
            "options": rep['options'] if rep else {},
            "correct_answer": rep['correct_answer'] if rep else 'A',
            "repeat_count": c['total_questions'],
            "unique_years_count": c['years_count'],
            "years": c['years_tested'],
            "historical_twin_ids": c['historical_twin_ids'],
            "representative_questions": c['representative_questions'],
            "is_multi_year": c['years_count'] > 1,
            "type": f"High-Yield Archetype ({c['total_questions']} Qs across {c['years_count']} Years)",
            "slug": f"neet-concept-{c['rank']}"
        })

    max_neet_repeats = max([c['total_questions'] for c in neet_concepts]) if neet_concepts else 0
    max_cbse_repeats = max([c.get('repeat_count', 0) for c in cbse_repeats]) if cbse_repeats else 0

    output_data = {
        "summary": {
            "cbse_total_questions": 8089,
            "cbse_verified_repeat_clusters": len(cbse_repeats),
            "cbse_max_repeats": max_cbse_repeats,
            "neet_total_questions": 2060,
            "neet_verified_repeat_clusters": len(flattened_neet_repeats),
            "neet_max_repeats": max_neet_repeats,
            "neet_leaderboard_concepts": len(neet_concepts)
        },
        "cbse_repeats": cbse_repeats,
        "neet_repeats": flattened_neet_repeats,
        "neet_concepts": neet_concepts
    }

    with open(REPEATED_JSON, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] Updated {REPEATED_JSON}")
    print(f"Summary: CBSE Clusters = {len(cbse_repeats)}, NEET Concepts = {len(flattened_neet_repeats)}, Max NEET Repeat = {max_neet_repeats}x")

if __name__ == "__main__":
    sync_all()
