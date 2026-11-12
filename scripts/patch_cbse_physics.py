import json
import re

json_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_physics.json'
with open(json_path, 'r', encoding='utf-8') as f:
    phys = json.load(f)

print(f"Original question count in cbse_physics.json: {len(phys)}")

remove_ids = {1905, 1945, 4670, 4708, 2175}
new_phys = []

for q in phys:
    qid = q.get('id')
    if qid in remove_ids:
        print(f"Removing duplicate/fragment ID {qid}")
        continue

    # Fix 103
    if qid == 103:
        q['chapter_name'] = 'Semiconductor Electronics: Materials, Devices and Simple Circuits'
        q['chapter_number'] = 14
        q['subtopic'] = 'Semiconductors, Diodes & Logic Gates'
        q['subtopic_slug'] = 'semiconductors-diodes-gates'
        q['text'] = q['text'].replace('$100 \\pi t$', '(100 \\pi t)')
        q['text'] = q['text'].replace('$100 \\\\pi t$', '(100 \\pi t)')
        print(f"Updated ID 103: Ch={q['chapter_name']}")

    # Fix 205
    elif qid == 205:
        q['chapter_name'] = 'Alternating Current'
        q['chapter_number'] = 7
        q['subtopic'] = 'Alternating Currents, LCR Circuits & Transformers'
        q['subtopic_slug'] = 'alternating-currents-lcr'
        print(f"Updated ID 205: Ch={q['chapter_name']}")

    # Fix 5649
    elif qid == 5649:
        q['chapter_name'] = 'Alternating Current'
        q['chapter_number'] = 7
        q['subtopic'] = 'Alternating Currents, LCR Circuits & Transformers'
        q['subtopic_slug'] = 'alternating-currents-lcr'
        print(f"Updated ID 5649: Ch={q['chapter_name']}")

    # Fix 9721
    elif qid == 9721:
        q['chapter_name'] = 'Semiconductor Electronics: Materials, Devices and Simple Circuits'
        q['chapter_number'] = 14
        q['subtopic'] = 'Semiconductors, Diodes & Logic Gates'
        q['subtopic_slug'] = 'semiconductors-diodes-gates'
        print(f"Updated ID 9721: Ch={q['chapter_name']}")

    # Fix 218
    elif qid == 218:
        q['text'] = q['text'].replace('$100 \\pi t$', '(100 \\pi t)')
        q['text'] = q['text'].replace('$100 \\\\pi t$', '(100 \\pi t)')
        print(f"Updated ID 218 formula")

    # Fix 565
    elif qid == 565:
        q['text'] = re.sub(r'\$20%\$', r'$20\\%$', q['text'])
        print(f"Updated ID 565 percentage format")

    # Fix 1854
    elif qid == 1854:
        q['multi_year_count'] = 3
        q['cluster_size'] = 3
        q['is_parallel_clone'] = True
        print(f"Updated ID 1854 cluster metadata")

    # Fix 4598
    elif qid == 4598:
        q['multi_year_count'] = 3
        q['cluster_size'] = 3
        q['is_parallel_clone'] = True
        print(f"Updated ID 4598 cluster metadata")

    # Fix 2174
    elif qid == 2174:
        q['text'] = """(a) (i) Derive the condition for which a Wheatstone Bridge is balanced.
(ii) Determine the current in $3\\ \\Omega$ branch of a Wheatstone Bridge in the circuit shown in the figure."""
        print(f"Updated ID 2174 combined text")

    # Fix tab characters before 'ext{' in any text
    if 'text' in q and q['text']:
        # if text has TAB followed by ext{, fix to \text{
        q['text'] = q['text'].replace('\text{', '\\text{')
        q['text'] = q['text'].replace('\t', ' ')

    new_phys.append(q)

print(f"New question count in cbse_physics.json: {len(new_phys)}")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(new_phys, f, indent=2, ensure_ascii=False)

print("[SUCCESS] cbse_physics.json successfully updated and saved.")
