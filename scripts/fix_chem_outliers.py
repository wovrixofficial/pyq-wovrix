import json

json_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_chemistry.json'
with open(json_path, 'r', encoding='utf-8') as f:
    chem = json.load(f)

print(f"Total chemistry questions: {len(chem)}")

reclass_count = 0
for q in chem:
    if q.get('chapter_name') == 'Aldehydes, Ketones and Carboxylic Acids':
        t = q.get('text', '').lower()
        
        # 1. Glucose / Fructose / Amino acids -> Biomolecules (Chapter 10, NCERT)
        if ('glucose' in t or 'fructose' in t or 'denaturation of protein' in t or 'peptide linkage' in t) and not ('benzoic' in t or 'aldehyde' in t or 'ketone' in t or 'carboxylic' in t):
            q['chapter_name'] = 'Biomolecules'
            q['chapter_number'] = 10
            q['subtopic'] = 'Carbohydrates & Proteins'
            q['subtopic_slug'] = 'biomolecules-carbohydrates-proteins'
            reclass_count += 1
            print(f"Reclassified ID {q['id']} to Biomolecules: {q['text'][:60]}")

        # 2. Carbylamine / Hinsberg / Gabriel phthalimide / Diazonium -> Amines (Chapter 9, NCERT)
        elif ('carbylamine' in t or 'hinsberg' in t or 'gabriel phthalimide' in t or 'diazonium' in t or 'aniline' in t) and not ('benzoic' in t or 'aldehyde' in t or 'ketone' in t or 'carboxylic' in t):
            q['chapter_name'] = 'Amines'
            q['chapter_number'] = 9
            q['subtopic'] = 'Amines & Diazonium Salts'
            q['subtopic_slug'] = 'amines-diazonium-salts'
            reclass_count += 1
            print(f"Reclassified ID {q['id']} to Amines: {q['text'][:60]}")

        # 3. Lucas test / Phenol / Picric acid -> Alcohols, Phenols and Ethers (Chapter 7, NCERT)
        elif ('lucas test' in t or 'reimer-tiemann' in t or 'kolbe\'s reaction' in t or 'picric acid' in t) and not ('benzoic' in t or 'aldehyde' in t or 'ketone' in t or 'carboxylic' in t):
            q['chapter_name'] = 'Alcohols, Phenols and Ethers'
            q['chapter_number'] = 7
            q['subtopic'] = 'Alcohols, Phenols & Ethers'
            q['subtopic_slug'] = 'alcohols-phenols-ethers'
            reclass_count += 1
            print(f"Reclassified ID {q['id']} to Alcohols, Phenols and Ethers: {q['text'][:60]}")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(chem, f, indent=2, ensure_ascii=False)

print(f"[SUCCESS] Reclassified {reclass_count} misclassified questions from Aldehydes.")
