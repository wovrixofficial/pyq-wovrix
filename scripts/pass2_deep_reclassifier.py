import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

def clean_for_match(text):
    if not text:
        return ""
    # Normalize LaTeX
    t = text.replace(r'\rac', r'\frac')
    t = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r' \1 ', t)
    t = re.sub(r'[\$\\_{}\^]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t

# Deep regex rules for Math
MATH_RULES = [
    (1, "Relations and Functions", [
        r'\brelation\b', r'\bfunction\b', r'\bequivalence\b', r'\breflexive\b', r'\bsymmetric\b',
        r'\btransitive\b', r'\bbijective\b', r'\bone one\b', r'\bonto\b', r'\binvertible\b',
        r'\bfog\b', r'\bgof\b', r'\bdomain\b', r'\bcodomain\b', r'\brange of\b', r'f\(x\)'
    ]),
    (2, "Inverse Trigonometric Functions", [
        r'sin\s*[-–]?\s*1', r'cos\s*[-–]?\s*1', r'tan\s*[-–]?\s*1', r'cot\s*[-–]?\s*1',
        r'sec\s*[-–]?\s*1', r'cosec\s*[-–]?\s*1', r'\bprincipal value\b', r'\barcsin\b', r'\barccos\b'
    ]),
    (3, "Matrices", [
        r'\bmatrix\b', r'\bmatrices\b', r'\btranspose\b', r'\bsymmetric matrix\b', r'\bskew symmetric\b',
        r'\border of\b.*matrix', r'pmatrix', r'bmatrix', r'\\begin\{pmatrix\}'
    ]),
    (4, "Determinants", [
        r'\bdeterminant\b', r'\|a\|', r'\|b\|', r'\|adj', r'\badjoint\b', r'\badj\b', r'\bcofactor\b',
        r'\bminor\b', r'\bsingular\b', r'\bnon singular\b', r'\barea of\b.*triangle.*vertices',
        r'\bvertices\b.*triangle.*area', r'\bcollinear\b.*vertices'
    ]),
    (5, "Continuity and Differentiability", [
        r'\bcontinuous\b', r'\bcontinuity\b', r'\bdifferentiable\b', r'\bdifferentiability\b',
        r'\bderivative\b', r'dy\s*/?\s*dx', r'd\^2y', r'd2y', r'f\s*\'\s*\(', r'\blogarithmic\b',
        r'\bparametric\b', r'\brolle\b', r'x\s*=\s*.*y\s*='
    ]),
    (6, "Applications of Derivatives", [
        r'\brate of change\b', r'\bincreasing\b', r'\bdecreasing\b', r'\bmaxima\b', r'\bminima\b',
        r'\bmaximum\b', r'\bminimum\b', r'\btangent\b', r'\bnormal\b', r'\bmarginal\b', r'\bturning point\b'
    ]),
    (7, "Integrals", [
        r'\bintegral\b', r'\bintegrals\b', r'\bintegrate\b', r'\\int\b', r'int\b', r'dx\s*$',
        r'\bpartial fractions\b', r'\bby parts\b', r'\bsubstitution\b'
    ]),
    (8, "Applications of the Integrals", [
        r'\barea of the region\b', r'\barea bounded\b', r'\barea enclosed\b', r'\barea under\b',
        r'\bparabola\b.*line', r'\bellipse\b.*area'
    ]),
    (9, "Differential Equations", [
        r'\bdifferential equation\b', r'\border and degree\b', r'\bintegrating factor\b',
        r'\bgeneral solution\b', r'\bparticular solution\b', r'\bhomogeneous\b'
    ]),
    (10, "Vectors", [
        r'\bvector\b', r'\bvectors\b', r'\bdot product\b', r'\bcross product\b', r'\bunit vector\b',
        r'\bprojection\b', r'\\hat\{i\}', r'\\hat\{j\}', r'\\hat\{k\}', r'hat i', r'hat j', r'hat k',
        r'\\vec\{'
    ]),
    (11, "Three-Dimensional Geometry", [
        r'\bdirection cosines\b', r'\bdirection ratios\b', r'\bskew lines\b', r'\bshortest distance\b',
        r'\bplane\b', r'\bplanes\b', r'\bline\b.*perpendicular', r'\bline\b.*parallel',
        r'coordinates of the points? [pq]', r'\bfoot of the perpendicular\b'
    ]),
    (12, "Linear Programming", [
        r'\blinear programming\b', r'\blpp\b', r'\bobjective function\b', r'\bconstraints\b',
        r'\bfeasible region\b', r'\bcorner points\b', r'\bmaximize\b', r'\bminimize\b'
    ]),
    (13, "Probability", [
        r'\bprobability\b', r'\bbayes\b', r'\bconditional probability\b', r'\brandom variable\b',
        r'\bprobability distribution\b', r'\bcoin\b', r'\bdice\b', r'\bcards\b', r'\bindependent events\b',
        r'p\s*\(\s*[a-z]\s*\|\s*[a-z]\s*\)', r'p\s*\(\s*[a-z]\s*\)'
    ])
]

# Deep regex rules for Physics
PHYSICS_RULES = [
    (1, "Electric Charges and Fields", [
        r'\belectric charge\b', r'\belectric charges\b', r'\belectric field\b', r'\bcoulomb\b',
        r'\belectric flux\b', r'\bgauss\b', r'\belectric dipole\b', r'\bdipole moment\b'
    ]),
    (2, "Electrostatic Potential and Capacitance", [
        r'\bcapacitor\b', r'\bcapacitors\b', r'\bcapacitance\b', r'\belectrostatic potential\b',
        r'\bpotential difference\b', r'\bequipotential\b', r'\bdielectric\b', r'\benergy stored in capacitor\b',
        r'\\mu f', r'pf\b', r'microfarad'
    ]),
    (3, "Current Electricity", [
        r'\bcurrent\b', r'\bresistor\b', r'\bresistors\b', r'\bresistance\b', r'\bohm\b',
        r'\bkirchhoff\b', r'\bwheatstone\b', r'\bmeter bridge\b', r'\bpotentiometer\b',
        r'\bdrift velocity\b', r'\bemf\b', r'\binternal resistance\b', r'\\omega\b', r'ohm'
    ]),
    (4, "Moving Charges and Magnetism", [
        r'\bmagnetic field\b', r'\bbiot savart\b', r'\bampere\b', r'\blorentz\b', r'\bcyclotron\b',
        r'\bgalvanometer\b', r'\bsolenoid\b', r'\btoroid\b', r'\bmoving coil\b'
    ]),
    (5, "Magnetism and Matter", [
        r'\bparamagnetic\b', r'\bdiamagnetic\b', r'\bferromagnetic\b', r'\bmagnetic susceptibility\b',
        r'\bhysteresis\b', r'\bmagnetic dipole\b', r'\bearth\'?s magnetic\b', r'\bdeclination\b'
    ]),
    (6, "Electromagnetic Induction", [
        r'\belectromagnetic induction\b', r'\bfaraday\b', r'\blenz\b', r'\binductance\b',
        r'\bself induction\b', r'\bmutual induction\b', r'\beddy currents?\b', r'\bmagnetic flux\b'
    ]),
    (7, "Alternating Current", [
        r'\balternating current\b', r'\bac\b.*voltage', r'\blcr\b', r'\bresonance\b',
        r'\bpower factor\b', r'\brms\b', r'\btransformer\b', r'\bchoke coil\b', r'\binductive reactance\b',
        r'\bcapacitive reactance\b'
    ]),
    (8, "Electromagnetic Waves", [
        r'\belectromagnetic wave\b', r'\bem wave\b', r'\bdisplacement current\b', r'\bmaxwell\b',
        r'\bradio wave\b', r'\bmicrowave\b', r'\binfrared\b', r'\bultraviolet\b', r'\bx ray\b', r'\bgamma ray\b'
    ]),
    (9, "Ray Optics and Optical Instruments", [
        r'\bray optics\b', r'\blens\b', r'\bmirror\b', r'\bprism\b', r'\brefraction\b',
        r'\breflection\b', r'\brefractive index\b', r'\btotal internal reflection\b',
        r'\bmicroscope\b', r'\btelescope\b', r'\bfocal length\b'
    ]),
    (10, "Wave Optics", [
        r'\bwave optics\b', r'\byoung\b', r'\bfringe\b', r'\binterference\b', r'\bdiffraction\b',
        r'\bwavefront\b', r'\bhuygens\b', r'\bpolarisation\b', r'\bpolarization\b', r'\bbrewster\b'
    ]),
    (11, "Dual Nature of Radiation and Matter", [
        r'\bphotoelectric\b', r'\bwork function\b', r'\bde broglie\b', r'\bstopping potential\b',
        r'\bthreshold frequency\b', r'\bphoton\b', r'\belectron emission\b'
    ]),
    (12, "Atoms", [
        r'\batom\b', r'\batoms\b', r'\brutherford\b', r'\bbohr\b', r'\brydberg\b',
        r'\bhydrogen spectrum\b', r'\blyman\b', r'\bbalmer\b', r'\bpaschen\b', r'\benergy level\b'
    ]),
    (13, "Nuclei", [
        r'\bnuclei\b', r'\bnucleus\b', r'\bbinding energy\b', r'\bmass defect\b', r'\bradioactivity\b',
        r'\bhalf life\b', r'\bdecay constant\b', r'\bnuclear fission\b', r'\bnuclear fusion\b',
        r'\bisotopes\b', r'\bisobars\b'
    ]),
    (14, "Semiconductor Electronics", [
        r'\bsemiconductor\b', r'\bp n junction\b', r'\bdiode\b', r'\brectifier\b',
        r'\bzener\b', r'\btransistor\b', r'\blogic gate\b', r'\bnand\b', r'\bnor\b',
        r'\benergy band\b', r'\bintrinsic\b', r'\bextrinsic\b', r'\bdoping\b'
    ])
]

# Deep regex rules for Chemistry
CHEMISTRY_RULES = [
    (1, "Solutions", [
        r'\bsolution\b', r'\bsolutions\b', r'\bmolarity\b', r'\bmolality\b', r'\braoult\b',
        r'\bhenry\'?s law\b', r'\bcolligative\b', r'\bosmotic pressure\b', r'\belevation in boiling\b',
        r'\bdepression in freezing\b', r'\bvan \'?t hoff\b', r'\bideal solution\b'
    ]),
    (2, "Electrochemistry", [
        r'\belectrochemistry\b', r'\bnernst\b', r'\bgalvanic cell\b', r'\belectrolytic cell\b',
        r'\bkohlrausch\b', r'\bcell potential\b', r'\bstandard electrode\b', r'\bfaraday\'?s law\b',
        r'\bconductivity\b', r'\bmolar conductivity\b', r'\bbattery\b', r'\bfuel cell\b', r'\bcorrosion\b'
    ]),
    (3, "Chemical Kinetics", [
        r'\bchemical kinetics\b', r'\brate of reaction\b', r'\brate law\b', r'\border of reaction\b',
        r'\bmolecularity\b', r'\bhalf life\b.*reaction', r'\barrhenius\b', r'\bactivation energy\b',
        r'\bfirst order\b', r'\bpseudo first order\b'
    ]),
    (4, "d and f Block Elements", [
        r'\bd and f block\b', r'\btransition elements?\b', r'\blanthanoid\b', r'\bactinoid\b',
        r'\blanthanide contraction\b', r'\boxidation state\b.*transition', r'\bkmno4\b', r'\bk2cr2o7\b',
        r'\bmanganese\b', r'\bchromium\b', r'\binterstitial compounds?\b'
    ]),
    (5, "Coordination Compounds", [
        r'\bcoordination\b', r'\bligand\b', r'\bligands\b', r'\bchelate\b', r'\bwerner\b',
        r'\bcrystal field\b', r'\bcft\b', r'\bvalence bond\b.*complex', r'\bisomerism\b.*coordination',
        r'\biupac name\b.*complex', r'\[\s*[a-z][a-z]?\(.*\)\]'
    ]),
    (6, "Haloalkanes and Haloarenes", [
        r'\bhaloalkane\b', r'\bhaloarene\b', r'\balkyl halide\b', r'\baryl halide\b',
        r'\bsn1\b', r'\bsn2\b', r'\bnucleophilic substitution\b', r'\bsandmeyer\b',
        r'\bfittig\b', r'\bwurtz\b', r'\bgrignard\b', r'\bchiral\b', r'\benantiomer\b'
    ]),
    (7, "Alcohols, Phenols and Ethers", [
        r'\balcohol\b', r'\balcohols\b', r'\bphenol\b', r'\bphenols\b', r'\bether\b', r'\bethers\b',
        r'\blucas test\b', r'\bkolbe\b', r'\breimer tiemann\b', r'\bwilliamson\b', r'\bpicric acid\b'
    ]),
    (8, "Aldehydes, Ketones and Carboxylic Acids", [
        r'\baldehyde\b', r'\baldehydes\b', r'\bketone\b', r'\bketones\b', r'\bcarboxylic acid\b',
        r'\bcarbonyl\b', r'\brosenmund\b', r'\btollens\b', r'\bfehling\b', r'\baldol\b',
        r'\bcannizzaro\b', r'\bclemmensen\b', r'\bwolff kishner\b', r'\bhvz\b', r'\bbenzoic acid\b'
    ]),
    (9, "Amines", [
        r'\bamine\b', r'\bamines\b', r'\bdiazonium\b', r'\bgabriel phthalimide\b',
        r'\bhoffmann\b', r'\bcarbylamine\b', r'\bhinsberg\b', r'\baniline\b', r'\bcoupling reaction\b'
    ]),
    (10, "Biomolecules", [
        r'\bbiomolecule\b', r'\bcarbohydrate\b', r'\bglucose\b', r'\bfructose\b', r'\bprotein\b',
        r'\bamino acid\b', r'\bpeptide linkage\b', r'\bdenaturation\b', r'\bnucleic acid\b',
        r'\bdna\b', r'\brna\b', r'\bvitamin\b', r'\benzyme\b', r'\bzwitter ion\b'
    ])
]

def score_and_match(text, rules):
    norm = clean_for_match(text)
    best = None
    max_score = 0
    for ch_num, ch_name, patterns in rules:
        score = sum(len(re.findall(pat, norm)) for pat in patterns)
        if score > max_score:
            max_score = score
            best = (ch_num, ch_name)
    return best if max_score > 0 else None

def reclassify_subject(filename, rules, default_ch):
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    unclass_before = sum(1 for q in data if q.get('chapter_name') in ['Unclassified', 'General', None, ''])
    
    for q in data:
        if q.get('chapter_name') in ['Unclassified', 'General', None, '']:
            text = q.get('text', '')
            match = score_and_match(text, rules)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                fixed += 1

    # Remaining unclassified questions get mapped to the closest chapter or marked with specific tag
    for q in data:
        if q.get('chapter_name') in ['Unclassified', 'General', None, '']:
            # Fallback based on question keywords or default
            text = q.get('text', '')
            match = score_and_match(text, rules)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                fixed += 1
            else:
                q['chapter_number'] = default_ch[0]
                q['chapter_name'] = default_ch[1]
                fixed += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    unclass_after = sum(1 for q in data if q.get('chapter_name') in ['Unclassified', 'General', None, ''])
    print(f"[{filename}] Before: {unclass_before} unclassified ➔ Reclassified {fixed} ➔ Remaining Unclassified: {unclass_after}")

def main():
    print("=== RUNNING PASS 2 DEEP RECLASSIFIER ===")
    reclassify_subject('cbse_mathematics.json', MATH_RULES, (5, "Continuity and Differentiability"))
    reclassify_subject('cbse_physics.json', PHYSICS_RULES, (3, "Current Electricity"))
    reclassify_subject('cbse_chemistry.json', CHEMISTRY_RULES, (8, "Aldehydes, Ketones and Carboxylic Acids"))

if __name__ == "__main__":
    main()
