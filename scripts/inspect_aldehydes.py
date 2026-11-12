import json
import re

with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/cbse_chemistry.json', 'r', encoding='utf-8') as f:
    chem = json.load(f)

aldehydes_qs = [q for q in chem if q.get('chapter_name') == 'Aldehydes, Ketones and Carboxylic Acids']
print(f"Total in Aldehydes: {len(aldehydes_qs)}")

# Check subtopics and keywords
halo_count = 0
alcohol_count = 0
amine_count = 0
biomol_count = 0
coord_count = 0
kinetics_count = 0
sol_count = 0

sample_misclassified = []

for q in aldehydes_qs:
    t = q.get('text', '').lower()
    # Check for strong markers of OTHER chapters
    # Amines: diazotization, aniline, carbylamine, gabriel phthalimide, benzenediazonium, primary amine, hinsberg
    if ('aniline' in t or 'diazonium' in t or 'carbylamine' in t or 'hinsberg' in t or 'gabriel phthalimide' in t) and not ('benzoic acid' in t or 'benzaldehyde' in t):
        amine_count += 1
        sample_misclassified.append(('Amines', q['id'], q['text'][:80]))
    # Alcohols/Phenols: kolbe reaction, reimer-tiemann, phenol, picric acid, lucas reagent
    elif ('phenol' in t or 'reimer-tiemann' in t or 'lucas test' in t or 'kolbe\'s reaction' in t) and not ('carboxylic' in t or 'aldehyde' in t or 'ketone' in t):
        alcohol_count += 1
        sample_misclassified.append(('Alcohols, Phenols and Ethers', q['id'], q['text'][:80]))
    # Haloalkanes: wurtz-fittig, sn1, sn2, swarts, finkelstein, haloalkane, haloarene, chlorobenzene
    elif ('sn1' in t or 'sn2' in t or 'swarts' in t or 'finkelstein' in t or 'chlorobenzene' in t) and not ('carboxylic' in t or 'aldehyde' in t or 'ketone' in t):
        halo_count += 1
        sample_misclassified.append(('Haloalkanes and Haloarenes', q['id'], q['text'][:80]))
    # Biomolecules: glucose, fructose, amino acid, peptide, denaturation, rna, dna
    elif ('glucose' in t or 'fructose' in t or 'peptide linkage' in t or 'denaturation of protein' in t or 'nucleic acid' in t):
        biomol_count += 1
        sample_misclassified.append(('Biomolecules', q['id'], q['text'][:80]))
    # Solutions / Kinetics / Electrochemistry
    elif ('first order reaction' in t or 'rate constant' in t or 'half-life' in t or 'activation energy' in t):
        kinetics_count += 1
        sample_misclassified.append(('Chemical Kinetics', q['id'], q['text'][:80]))
    elif ('molarity' in t or 'molality' in t or 'henry\'s law' in t or 'raoult\'s law' in t or 'osmotic pressure' in t):
        sol_count += 1
        sample_misclassified.append(('Solutions', q['id'], q['text'][:80]))

print(f"Misclassified suspects in Aldehydes:")
print(f"  Amines: {amine_count}")
print(f"  Alcohols/Phenols: {alcohol_count}")
print(f"  Haloalkanes: {halo_count}")
print(f"  Biomolecules: {biomol_count}")
print(f"  Chemical Kinetics: {kinetics_count}")
print(f"  Solutions: {sol_count}")
print(f"Sample misclassified (first 10):")
for ch, qid, txt in sample_misclassified[:10]:
    print(f"  -> {ch} [ID {qid}]: {txt.replace(chr(10), ' ')}")
