import os
import json
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

def normalize_text_for_classification(text):
    if not text:
        return ""
    t = text
    t = re.sub(r'\\?\s*rac\b', 'frac', t)
    t = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r' \1 ', t)
    t = re.sub(r'[\$\\_{}\^]', ' ', t)
    t = re.sub(r'[^a-zA-Z0-9\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t

# -----------------------------------------------------------------------------
# MATH NCERT CHAPTER ROOTS (Class 12)
# -----------------------------------------------------------------------------
MATH_CHAPTER_RULES = [
    (1, "Relations and Functions", [
        r'\brelation\b', r'\bfunction\b', r'\bfunctions\b', r'\bequivalence\b', r'\breflexive\b',
        r'\bsymmetric\b', r'\btransitive\b', r'\bbijective\b', r'\bone one\b', r'\bonto\b',
        r'\binvertible\b', r'\bcomposite\b', r'\bfog\b', r'\bgof\b', r'\bcodomain\b', r'\bdomain\b'
    ]),
    (2, "Inverse Trigonometric Functions", [
        r'\bsin\s*1\b', r'\bcos\s*1\b', r'\btan\s*1\b', r'\bcot\s*1\b', r'\bsec\s*1\b', r'\bcsc\s*1\b',
        r'\binverse trig\b', r'\bprincipal value\b', r'\barcsin\b', r'\barccos\b', r'\barctan\b',
        r'\bsin 1\b', r'\bcos 1\b', r'\btan 1\b'
    ]),
    (3, "Matrices", [
        r'\bmatrix\b', r'\bmatrices\b', r'\border of matrix\b', r'\brow matrix\b', r'\bcolumn matrix\b',
        r'\bskew symmetric\b', r'\bsymmetric matrix\b', r'\btranspose\b', r'\belementary row\b',
        r'\bmatrix multiplication\b', r'\bidentity matrix\b', r'\bsquare matrix\b', r'\bpmatrix\b', r'\bbmatrix\b'
    ]),
    (4, "Determinants", [
        r'\bdeterminant\b', r'\bdeterminants\b', r'\bdet\b', r'\bcofactor\b', r'\bcofactors\b',
        r'\bminor\b', r'\bminors\b', r'\badjoint\b', r'\badj\b', r'\bsingular matrix\b',
        r'\bnon singular\b', r'\bcramer\b', r'\bsystem of linear equations\b', r'\bconsistent\b', r'\binconsistent\b'
    ]),
    (5, "Continuity and Differentiability", [
        r'\bcontinuous\b', r'\bcontinuity\b', r'\bdifferentiable\b', r'\bdifferentiability\b',
        r'\bderivative\b', r'\bderivatives\b', r'\bdy dx\b', r'\blogarithmic\b', r'\bparametric\b',
        r'\bsecond order derivative\b', r'\brolle\b', r'\bmean value theorem\b'
    ]),
    (6, "Applications of Derivatives", [
        r'\brate of change\b', r'\bincreasing\b', r'\bdecreasing\b', r'\bstrictly increasing\b',
        r'\bstrictly decreasing\b', r'\bmaxima\b', r'\bminima\b', r'\bmaximum\b', r'\bminimum\b',
        r'\blocal maximum\b', r'\blocal minimum\b', r'\btangent\b', r'\bnormal\b', r'\bmarginal\b',
        r'\bturning point\b', r'\binflection\b'
    ]),
    (7, "Integrals", [
        r'\bintegral\b', r'\bintegrals\b', r'\bintegrate\b', r'\bevaluate the integral\b',
        r'\bindefinite integral\b', r'\bdefinite integral\b', r'\bby parts\b', r'\bpartial fraction\b',
        r'\bpartial fractions\b', r'\bsubstitution\b', r'\bint\b'
    ]),
    (8, "Applications of the Integrals", [
        r'\barea of the region\b', r'\barea bounded\b', r'\barea enclosed\b', r'\barea under\b',
        r'\bsketch the region\b', r'\barea\b.*curve', r'\bparabola and\b', r'\bellipse and\b'
    ]),
    (9, "Differential Equations", [
        r'\bdifferential equation\b', r'\bdifferential equations\b', r'\border and degree\b',
        r'\bgeneral solution\b', r'\bparticular solution\b', r'\bintegrating factor\b',
        r'\bhomogeneous\b', r'\bseparable\b'
    ]),
    (10, "Vectors", [
        r'\bvector\b', r'\bvectors\b', r'\bdot product\b', r'\bcross product\b', r'\bscalar product\b',
        r'\bvector product\b', r'\bunit vector\b', r'\bprojection\b', r'\bcollinear\b', r'\bcoplanar\b',
        r'\bmagnitude\b.*vector', r'\bhat i\b', r'\bhat j\b', r'\bhat k\b'
    ]),
    (11, "Three-Dimensional Geometry", [
        r'\bdirection cosines\b', r'\bdirection ratios\b', r'\bskew lines\b', r'\bshortest distance\b',
        r'\bfoot of the perpendicular\b', r'\bline\b.*perpendicular', r'\bline\b.*parallel',
        r'\bcartesian equation\b', r'\bvector equation of\b', r'\bintersecting lines\b', r'\blines\b'
    ]),
    (12, "Linear Programming", [
        r'\blinear programming\b', r'\blpp\b', r'\bmaximize\b', r'\bminimize\b', r'\bobjective function\b',
        r'\bconstraints\b', r'\bfeasible region\b', r'\bcorner points\b', r'\bbounded\b', r'\bunbounded\b'
    ]),
    (13, "Probability", [
        r'\bprobability\b', r'\bconditional probability\b', r'\bbayes\b', r'\bindependent events\b',
        r'\brandom variable\b', r'\bprobability distribution\b', r'\bbernoulli\b', r'\bbinomial\b',
        r'\bcoin\b', r'\bdice\b', r'\bcards\b', r'\bdeck of cards\b', r'\bvariance\b'
    ])
]

# -----------------------------------------------------------------------------
# PHYSICS NCERT CHAPTER ROOTS (Class 12)
# -----------------------------------------------------------------------------
PHYSICS_CHAPTER_RULES = [
    (1, "Electric Charges and Fields", [
        r'\bcoulomb\b', r'\belectric dipole\b', r'\bdipole moment\b', r'\belectric flux\b', r'\bgauss\b',
        r'\belectric field\b', r'\bpoint charge\b', r'\blinear charge\b', r'\bsurface charge\b',
        r'\blines of force\b', r'\btorque on dipole\b', r'\bcharged sphere\b', r'\belectrostatic force\b'
    ]),
    (2, "Electrostatic Potential and Capacitance", [
        r'\belectric potential\b', r'\bpotential difference\b', r'\bequipotential\b', r'\bcapacitance\b',
        r'\bcapacitor\b', r'\bcapacitors\b', r'\bparallel plate\b', r'\bdielectric\b', r'\bdielectrics\b',
        r'\benergy stored in capacitor\b', r'\bvan de graaff\b', r'\bpotential energy\b.*charges'
    ]),
    (3, "Current Electricity", [
        r'\bohm\b', r'\bdrift velocity\b', r'\bmobility\b', r'\bresistivity\b', r'\bconductivity\b',
        r'\bkirchhoff\b', r'\bwheatstone\b', r'\bmeter bridge\b', r'\bpotentiometer\b', r'\binternal resistance\b',
        r'\bcells\b', r'\bresistance\b', r'\bresistor\b', r'\bresistors\b', r'\bheater\b', r'\bcurrent\b',
        r'\bwire is stretched\b', r'\belectric power\b'
    ]),
    (4, "Moving Charges and Magnetism", [
        r'\bbiot savart\b', r'\blorentz\b', r'\bampere\b', r'\bsolenoid\b', r'\btoroid\b', r'\bcyclotron\b',
        r'\bgalvanometer\b', r'\bmagnetic dipole\b', r'\bforce between two parallel\b', r'\bcircular loop\b',
        r'\bhelical\b', r'\bmagnetic field\b'
    ]),
    (5, "Magnetism and Matter", [
        r'\bearth\b.*magnetic', r'\bmagnetic declination\b', r'\bdip\b', r'\bangle of dip\b', r'\bsusceptibility\b',
        r'\bdiamagnetic\b', r'\bparamagnetic\b', r'\bferromagnetic\b', r'\bhysteresis\b', r'\bbar magnet\b',
        r'\bcurie\b', r'\bpermeability\b'
    ]),
    (6, "Electromagnetic Induction", [
        r'\bfaraday\b', r'\blenz\b', r'\bmotional emf\b', r'\binduced emf\b', r'\binduced current\b',
        r'\beddy\b', r'\bself induction\b', r'\bself inductance\b', r'\bmutual induction\b',
        r'\bmutual inductance\b', r'\bmagnetic flux\b'
    ]),
    (7, "Alternating Current", [
        r'\balternating current\b', r'\brms\b', r'\bac\b.*voltage', r'\breactance\b', r'\bimpedance\b',
        r'\blcr\b', r'\bresonance\b', r'\bquality factor\b', r'\bpower factor\b', r'\btransformer\b',
        r'\bwattless\b', r'\binductor\b', r'\binductance\b'
    ]),
    (8, "Electromagnetic Waves", [
        r'\bdisplacement current\b', r'\belectromagnetic spectrum\b', r'\bem wave\b', r'\bem waves\b',
        r'\bmicrowaves\b', r'\bradio waves\b', r'\binfrared\b', r'\bultraviolet\b', r'\bx rays\b',
        r'\bgamma rays\b', r'\bmaxwell\b'
    ]),
    (9, "Ray Optics and Optical Instruments", [
        r'\brefraction\b', r'\breflection\b', r'\bsnell\b', r'\btotal internal reflection\b',
        r'\boptical fiber\b', r'\blens maker\b', r'\bprism\b', r'\bdeviation\b', r'\bmicroscope\b',
        r'\btelescope\b', r'\bmagnification\b', r'\bfocal length\b', r'\bconvex lens\b', r'\bconcave\b',
        r'\bpower of lens\b', r'\bray\b'
    ]),
    (10, "Wave Optics", [
        r'\bhuygens\b', r'\bwavefront\b', r'\binterference\b', r'\byoung\b', r'\bdouble slit\b',
        r'\bfringe width\b', r'\bcoherent\b', r'\bdiffraction\b', r'\bsingle slit\b', r'\bpolarization\b',
        r'\bbrewster\b', r'\bmalus\b', r'\bcentral maximum\b', r'\bwaves expressed as\b'
    ]),
    (11, "Dual Nature of Radiation and Matter", [
        r'\bphotoelectric\b', r'\bwork function\b', r'\bthreshold frequency\b', r'\bthreshold wavelength\b',
        r'\bstopping potential\b', r'\bde broglie\b', r'\bdavisson\b', r'\bphoton\b', r'\bphotons\b',
        r'\bradiation\b'
    ]),
    (12, "Atoms", [
        r'\brutherford\b', r'\balpha particle\b', r'\bbohr\b', r'\bbohr radius\b', r'\bhydrogen spectrum\b',
        r'\blyman\b', r'\bbalmer\b', r'\bpaschen\b', r'\bclosest approach\b', r'\bimpact parameter\b',
        r'\borbit of hydrogen\b'
    ]),
    (13, "Nuclei", [
        r'\bnucleus\b', r'\bnuclei\b', r'\bnucleon\b', r'\bnucleons\b', r'\bmass defect\b', r'\bbinding energy\b',
        r'\bnuclear\b', r'\bradioactivity\b', r'\bhalf life\b', r'\bdecay\b', r'\bfission\b', r'\bfusion\b',
        r'\batomic mass unit\b', r'\bisotopes\b'
    ]),
    (14, "Semiconductor Electronics: Materials, Devices and Simple Circuits", [
        r'\bsemiconductor\b', r'\bsemiconductors\b', r'\bintrinsic\b', r'\bextrinsic\b', r'\bn type\b',
        r'\bp type\b', r'\bp n junction\b', r'\bforward bias\b', r'\breverse bias\b', r'\bzener\b',
        r'\brectifier\b', r'\blogic gate\b', r'\band gate\b', r'\bor gate\b', r'\bnand\b', r'\bnor gate\b',
        r'\bphotodiode\b', r'\bled\b', r'\bsolar cell\b', r'\benergy band\b', r'\bforbidden gap\b'
    ])
]

# -----------------------------------------------------------------------------
# CHEMISTRY NCERT CHAPTER ROOTS (Class 12)
# -----------------------------------------------------------------------------
CHEMISTRY_CHAPTER_RULES = [
    (1, "Solutions", [
        r'\bmolarity\b', r'\bmolality\b', r'\bmole fraction\b', r'\bhenry\b', r'\braoult\b',
        r'\bideal solution\b', r'\bnon ideal\b', r'\bazeotrope\b', r'\bcolligative\b',
        r'\bboiling point\b', r'\bfreezing point\b', r'\bosmotic pressure\b', r'\bvan t hoff\b',
        r'\bsolute\b', r'\bsolvent\b', r'\bsolution\b'
    ]),
    (2, "Electrochemistry", [
        r'\bgalvanic\b', r'\bnernst\b', r'\belectrode potential\b', r'\bemf\b', r'\bkohlrausch\b',
        r'\bmolar conductivity\b', r'\bfaraday\b', r'\bfaradays\b', r'\belectrolysis\b',
        r'\bfuel cell\b', r'\bcorrosion\b', r'\bbattery\b', r'\breduce\b.*mol', r'\bcell potential\b'
    ]),
    (3, "Chemical Kinetics", [
        r'\brate of reaction\b', r'\border of reaction\b', r'\bmolecularity\b', r'\brate constant\b',
        r'\bhalf life\b', r'\bfirst order\b', r'\bzero order\b', r'\bactivation energy\b',
        r'\barrhenius\b', r'\brate law\b', r'\bpseudo first order\b', r'\bcollision\b',
        r'\bfraction of molecules\b', r'\benergies equal to\b', r'\binitial rate\b'
    ]),
    (4, "The d- and f-Block Elements", [
        r'\btransition\b', r'\bd block\b', r'\bf block\b', r'\blanthanoid\b', r'\blanthanoids\b',
        r'\bactinoid\b', r'\blanthanoid contraction\b', r'\binterstitial\b', r'\bkmno4\b', r'\bk2cr2o7\b',
        r'\bpermanganate\b', r'\bdichromate\b', r'\bmanganese\b', r'\bchromium\b', r'\bfe2\b', r'\bfe3\b',
        r'\bcr2o7\b', r'\bmno4\b', r'\bmagnetic moment\b'
    ]),
    (5, "Coordination Compounds", [
        r'\bcoordination\b', r'\bligand\b', r'\bligands\b', r'\bcoordination number\b', r'\bwerner\b',
        r'\bchelate\b', r'\bchelating\b', r'\bvalence bond\b', r'\bvbt\b', r'\bcrystal field\b',
        r'\bcft\b', r'\bisomerism in coordination\b', r'\bhomoleptic\b', r'\bheteroleptic\b'
    ]),
    (6, "Haloalkanes and Haloarenes", [
        r'\bhaloalkane\b', r'\bhaloarene\b', r'\balkyl halide\b', r'\baryl halide\b', r'\bsn1\b', r'\bsn2\b',
        r'\bnucleophilic substitution\b', r'\bsaytzeff\b', r'\bgrignard\b', r'\bwurtz\b', r'\bfittig\b',
        r'\bsandmeyer\b', r'\bchiral\b', r'\benantiomer\b', r'\bracemic\b', r'\bchlorobenzene\b'
    ]),
    (7, "Alcohols, Phenols and Ethers", [
        r'\balcohol\b', r'\balcohols\b', r'\bphenol\b', r'\bphenols\b', r'\bether\b', r'\bethers\b',
        r'\blucas\b', r'\bkolbe\b', r'\breimer tiemann\b', r'\bwilliamson\b', r'\bpicric\b',
        r'\bhydroboration\b', r'\boh group in phenol\b', r'\bdehydration of alcohol\b'
    ]),
    (8, "Aldehydes, Ketones and Carboxylic Acids", [
        r'\baldehyde\b', r'\baldehydes\b', r'\bketone\b', r'\bketones\b', r'\bcarboxylic acid\b',
        r'\bcarbonyl\b', r'\brosenmund\b', r'\bstephen\b', r'\betard\b', r'\bclemmensen\b',
        r'\bwolff kishner\b', r'\btollens\b', r'\bfehling\b', r'\baldol\b', r'\bcannizzaro\b',
        r'\bhvz\b', r'\bformic acid\b', r'\bacetic acid\b', r'\bbenzoic acid\b'
    ]),
    (9, "Amines", [
        r'\bamine\b', r'\bamines\b', r'\bdiazonium\b', r'\bgabriel\b', r'\bhoffmann\b',
        r'\bcarbylamine\b', r'\bhinsberg\b', r'\bcoupling\b', r'\bazo dye\b', r'\baniline\b',
        r'\bpkb\b', r'\bprimary amine\b', r'\bsecondary amine\b'
    ]),
    (10, "Biomolecules", [
        r'\bcarbohydrate\b', r'\bcarbohydrates\b', r'\bglucose\b', r'\bfructose\b', r'\bprotein\b',
        r'\bproteins\b', r'\bamino acid\b', r'\bamino acids\b', r'\bpeptide\b', r'\bdenaturation\b',
        r'\bnucleic acid\b', r'\bdna\b', r'\brna\b', r'\bvitamin\b', r'\bvitamins\b', r'\benzyme\b',
        r'\bglycosidic\b', r'\bzwitter\b'
    ])
]

def score_text_against_rules(norm_text, rule_list):
    best_match = None
    max_score = 0
    for ch_num, ch_name, patterns in rule_list:
        score = sum(len(re.findall(pat, norm_text)) for pat in patterns)
        if score > max_score:
            max_score = score
            best_match = (ch_num, ch_name)
    if max_score > 0:
        return best_match
    return None

def run_precision_reclassifier():
    print("=== STARTING FULL PRECISION RECLASSIFIER ===")
    
    # 1. CBSE Mathematics
    math_path = os.path.join(DATA_DIR, 'cbse_mathematics.json')
    with open(math_path, 'r', encoding='utf-8') as f:
        math_data = json.load(f)

    math_fixed = 0
    for q in math_data:
        raw_txt = q.get('text', '')
        norm = normalize_text_for_classification(raw_txt)
        curr_ch = q.get('chapter_name', 'Unclassified')

        # Prioritize Determinants vs Matrices separation
        if curr_ch in ['Matrices', 'Unclassified', 'General', None]:
            if re.search(r'\bdeterminant\b|\bdet\b|\bcofactor\b|\bcofactors\b|\bminor\b|\bminors\b|\badjoint\b|\badj\b|\bsingular\b', norm):
                q['chapter_number'] = 4
                q['chapter_name'] = 'Determinants'
                math_fixed += 1
                continue

        # Prioritize Applications of Derivatives
        if curr_ch in ['Continuity and Differentiability', 'Integrals', 'Unclassified', 'General', None]:
            if re.search(r'\brate of change\b|\bincreasing\b|\bdecreasing\b|\bmaxima\b|\bminima\b|\bmaximum\b|\bminimum\b|\bmarginal\b', norm):
                q['chapter_number'] = 6
                q['chapter_name'] = 'Applications of Derivatives'
                math_fixed += 1
                continue

        # If Unclassified or General, run full math scoring
        if curr_ch in ['Unclassified', 'General', None, '']:
            match = score_text_against_rules(norm, MATH_CHAPTER_RULES)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                math_fixed += 1

    with open(math_path, 'w', encoding='utf-8') as f:
        json.dump(math_data, f, ensure_ascii=False, indent=2)
    print(f"[CBSE Math] Successfully classified/rebalanced: {math_fixed} questions.")

    # 2. CBSE Physics
    phys_path = os.path.join(DATA_DIR, 'cbse_physics.json')
    with open(phys_path, 'r', encoding='utf-8') as f:
        phys_data = json.load(f)

    phys_fixed = 0
    for q in phys_data:
        curr_ch = q.get('chapter_name', 'Unclassified')
        if curr_ch in ['Unclassified', 'General', None, '']:
            raw_txt = q.get('text', '')
            norm = normalize_text_for_classification(raw_txt)
            match = score_text_against_rules(norm, PHYSICS_CHAPTER_RULES)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                phys_fixed += 1

    with open(phys_path, 'w', encoding='utf-8') as f:
        json.dump(phys_data, f, ensure_ascii=False, indent=2)
    print(f"[CBSE Physics] Successfully classified: {phys_fixed} questions.")

    # 3. CBSE Chemistry
    chem_path = os.path.join(DATA_DIR, 'cbse_chemistry.json')
    with open(chem_path, 'r', encoding='utf-8') as f:
        chem_data = json.load(f)

    chem_fixed = 0
    for q in chem_data:
        curr_ch = q.get('chapter_name', 'Unclassified')
        if curr_ch in ['Unclassified', 'General', None, '']:
            raw_txt = q.get('text', '')
            norm = normalize_text_for_classification(raw_txt)
            match = score_text_against_rules(norm, CHEMISTRY_CHAPTER_RULES)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                chem_fixed += 1

    with open(chem_path, 'w', encoding='utf-8') as f:
        json.dump(chem_data, f, ensure_ascii=False, indent=2)
    print(f"[CBSE Chemistry] Successfully classified: {chem_fixed} questions.")

if __name__ == "__main__":
    run_precision_reclassifier()
