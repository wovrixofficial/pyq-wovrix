import os
import json
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

def normalize_text(t):
    if not t:
        return ""
    t = re.sub(r'^(Question\s*(number)?\s*\d+(\s*(to|and)\s*\d+)?[\.:\s]*)', '', t, flags=re.I)
    t = re.sub(r'[^a-zA-Z0-9\s]', ' ', t).lower()
    return re.sub(r'\s+', ' ', t).strip()

def build_cbse_repeats():
    datasets = {
        'Physics': os.path.join(DATA_DIR, 'cbse_physics.json'),
        'Chemistry': os.path.join(DATA_DIR, 'cbse_chemistry.json'),
        'Mathematics': os.path.join(DATA_DIR, 'cbse_mathematics.json')
    }

    clusters = defaultdict(list)
    total_qs = 0

    for subj, path in datasets.items():
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            qs = json.load(f)
        total_qs += len(qs)

        for q in qs:
            t = normalize_text(q.get('text', ''))
            if len(t) < 20:
                continue
            words = t.split()
            # Fingerprint on first 8 significant words
            fp = ' '.join(words[:8])
            clusters[(subj, fp)].append(q)

    cbse_items = []
    seen_texts = set()

    for (subj, fp), q_list in clusters.items():
        if len(q_list) > 1:
            years = sorted(list(set(str(q.get('year', '2026')) for q in q_list if q.get('year'))))
            rep_count = len(q_list)
            # Pick the best representative question (longest text / clean formatting)
            best_q = max(q_list, key=lambda x: len(x.get('text', '')))
            norm = normalize_text(best_q.get('text', ''))[:100]
            if norm in seen_texts:
                continue
            seen_texts.add(norm)

            cbse_items.append({
                "id": best_q.get('id'),
                "subject": subj,
                "chapter_number": best_q.get('chapter_number'),
                "chapter_name": best_q.get('chapter_name', 'General'),
                "marks": best_q.get('marks', 1),
                "text": best_q.get('text', ''),
                "repeat_count": rep_count,
                "unique_years_count": len(years),
                "years": years,
                "is_multi_year": len(years) > 1,
                "type": "Multi-Year Repeat" if len(years) > 1 else "Parallel Set Clone",
                "slug": f"cbse-{best_q.get('id')}"
            })

    # Sort descending by repeat_count then unique_years_count
    cbse_items.sort(key=lambda x: (x['repeat_count'], x['unique_years_count']), reverse=True)
    return total_qs, cbse_items

def build_neet_repeats():
    path = os.path.join(DATA_DIR, 'neet_all.json')
    if not os.path.exists(path):
        return 0, []

    with open(path, 'r', encoding='utf-8') as f:
        qs = json.load(f)

    clusters = defaultdict(list)
    for q in qs:
        t = normalize_text(q.get('text', ''))
        if len(t) < 20:
            continue
        words = t.split()
        fp = ' '.join(words[:7])
        clusters[(q.get('subject', 'Physics'), fp)].append(q)

    neet_items = []
    seen = set()

    for (subj, fp), q_list in clusters.items():
        if len(q_list) > 1:
            years = sorted(list(set(str(q.get('year', '2026')) for q in q_list if q.get('year'))))
            rep_count = len(q_list)
            best_q = max(q_list, key=lambda x: len(x.get('text', '')))
            norm = normalize_text(best_q.get('text', ''))[:100]
            if norm in seen:
                continue
            seen.add(norm)

            neet_items.append({
                "id": best_q.get('id'),
                "subject": subj,
                "ncert_chapter": best_q.get('ncert_chapter', 'General'),
                "text": best_q.get('text', ''),
                "options": best_q.get('options', {}),
                "correct_answer": best_q.get('correct_answer', 'A'),
                "repeat_count": rep_count,
                "unique_years_count": len(years),
                "years": years,
                "is_multi_year": len(years) > 1,
                "type": "Multi-Year Repeat" if len(years) > 1 else "Parallel Paper Variant",
                "slug": f"neet-{best_q.get('id')}"
            })

    neet_items.sort(key=lambda x: (x['repeat_count'], x['unique_years_count']), reverse=True)
    return len(qs), neet_items

def main():
    print("Scanning CBSE datasets for repeated questions and parallel clones...")
    cbse_total, cbse_repeats = build_cbse_repeats()
    print(f"  Found {len(cbse_repeats)} unique repeat patterns in CBSE.")

    print("Scanning NEET dataset for recurring questions...")
    neet_total, neet_repeats = build_neet_repeats()
    print(f"  Found {len(neet_repeats)} unique repeat patterns in NEET.")

    output = {
        "summary": {
            "cbse_total_questions": cbse_total,
            "cbse_repeat_patterns": len(cbse_repeats),
            "cbse_max_repeats": cbse_repeats[0]['repeat_count'] if cbse_repeats else 0,
            "neet_total_questions": neet_total,
            "neet_repeat_patterns": len(neet_repeats),
            "neet_max_repeats": neet_repeats[0]['repeat_count'] if neet_repeats else 0
        },
        "cbse_repeats": cbse_repeats,
        "neet_repeats": neet_repeats
    }

    out_file = os.path.join(DATA_DIR, "repeated_questions.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"[OK] Generated comprehensive repeated_questions.json ({len(cbse_repeats)} CBSE, {len(neet_repeats)} NEET patterns)!")

if __name__ == "__main__":
    main()
