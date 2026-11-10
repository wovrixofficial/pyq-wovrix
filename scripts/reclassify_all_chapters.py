import os
import json
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

# ==============================================================================
# 1. CBSE MATHEMATICS RULES (Class 12 - 13 Chapters)
# ==============================================================================
MATH_CHAPTERS = {
    1: ("Relations and Functions", [
        r'\brelation\b', r'\bfunction\b', r'\bequivalence relation\b', r'\breflexive\b', r'\bsymmetric\b',
        r'\btransitive\b', r'\bbijective\b', r'\bone-one\b', r'\bonto\b', r'\binvertible function\b',
        r'\bcomposite function\b', r'\bfog\b', r'\bgof\b', r'\bcodomain\b', r'\bdomain of\b'
    ]),
    2: ("Inverse Trigonometric Functions", [
        r'\\sin\^\{-1\}', r'\\cos\^\{-1\}', r'\\tan\^\{-1\}', r'\\cot\^\{-1\}', r'\\sec\^\{-1\}', r'\\csc\^\{-1\}',
        r'\bsin\^\{-1\}', r'\bcos\^\{-1\}', r'\btan\^\{-1\}', r'\binverse trigonometric\b', r'\bprincipal value\b',
        r'\barcsin\b', r'\barccos\b', r'\barctan\b'
    ]),
    3: ("Matrices", [
        r'\bmatrix\b', r'\bmatrices\b', r'\border of matrix\b', r'\brow matrix\b', r'\bcolumn matrix\b',
        r'\bskew-symmetric\b', r'\bsymmetric matrix\b', r'\btranspose of\b', r'\belementary row\b',
        r'\bmatrix multiplication\b', r'\bidentity matrix\b', r'\bsquare matrix of order\b', r'\\begin\{pmatrix\}',
        r'\\begin\{bmatrix\}'
    ]),
    4: ("Determinants", [
        r'\bdeterminant\b', r'\|A\|', r'\|B\|', r'\bdet\(', r'\bcofactor\b', r'\bminor\b', r'\badjoint\b',
        r'\badj\(A\)', r'\bsingular matrix\b', r'\bnon-singular\b', r'\bcramer\b', r'\bsystem of linear equations\b',
        r'\|A\^\{-1\}\|', r'A\^\{-1\}\s*=', r'\|\s*adj', r'\\det\b'
    ]),
    5: ("Continuity and Differentiability", [
        r'\bcontinuous at\b', r'\bcontinuity\b', r'\bdifferentiable\b', r'\bdifferentiability\b',
        r'\bderivative of\b', r'\\frac\{dy\}\{dx\}', r'\\frac\{d\^2y\}\{dx\^2\}', r'\bdy/dx\b',
        r'\blogarithmic differentiation\b', r'\bparametric form\b', r'\bsecond order derivative\b',
        r'\brolle\'s\b', r'\bmean value theorem\b'
    ]),
    6: ("Applications of Derivatives", [
        r'\brate of change\b', r'\bincreasing function\b', r'\bdecreasing function\b', r'\bstrictly increasing\b',
        r'\bstrictly decreasing\b', r'\bmaxima\b', r'\bminima\b', r'\bmaximum value\b', r'\bminimum value\b',
        r'\blocal maxima\b', r'\blocal minima\b', r'\btangent\b', r'\bnormal to the curve\b', r'\bmarginal revenue\b',
        r'\bmarginal cost\b', r'\bturning point\b', r'\bpoint of inflection\b'
    ]),
    7: ("Integrals", [
        r'\\int\b', r'\\int_', r'\bevaluate the integral\b', r'\bindefinite integral\b', r'\bdefinite integral\b',
        r'\bintegration by parts\b', r'\bpartial fractions\b', r'\bsubstitution method\b', r'\bintegral\b',
        r'\\int\s*\\frac'
    ]),
    8: ("Applications of the Integrals", [
        r'\barea of the region\b', r'\barea bounded by\b', r'\barea enclosed by\b', r'\barea under the curve\b',
        r'\bsketch the region\b', r'\barea of the circle\b', r'\barea of the ellipse\b', r'\bparabola and the line\b'
    ]),
    9: ("Differential Equations", [
        r'\bdifferential equation\b', r'\border and degree\b', r'\bgeneral solution of\b', r'\bparticular solution of\b',
        r'\bintegrating factor\b', r'\\frac\{dy\}\{dx\}\s*\+', r'\bhomogeneous differential\b', r'\bvariable separable\b'
    ]),
    10: ("Vectors", [
        r'\\vec\{a\}', r'\\vec\{b\}', r'\\vec\{c\}', r'\\vec\{r\}', r'\\hat\{i\}', r'\\hat\{j\}', r'\\hat\{k\}',
        r'\bdot product\b', r'\bcross product\b', r'\bscalar product\b', r'\bvector product\b',
        r'\bunit vector\b', r'\bprojection of vector\b', r'\bcollinear vectors\b', r'\bcoplanar vectors\b',
        r'\bmagnitude of\s*\\vec'
    ]),
    11: ("Three-Dimensional Geometry", [
        r'\bdirection cosines\b', r'\bdirection ratios\b', r'\bequation of a line\b', r'\bskew lines\b',
        r'\bshortest distance between\b', r'\bcartesian equation of line\b', r'\bvector equation of line\b',
        r'\bfoot of the perpendicular\b', r'\bcoordinates of the point\b.*line', r'\\frac\{x\s*[-+]\s*\d+\}'
    ]),
    12: ("Linear Programming", [
        r'\blinear programming\b', r'\blpp\b', r'\bmaximize\b', r'\bminimize\b', r'\bobjective function\b',
        r'\bconstraints\b', r'\bfeasible region\b', r'\bcorner points\b', r'\bbounded region\b', r'\bunbounded region\b'
    ]),
    13: ("Probability", [
        r'\bprobability\b', r'P\([A-Z]\|[A-Z]\)', r'\bconditional probability\b', r'\bbayes\'\b',
        r'\btotal probability\b', r'\bindependent events\b', r'\brandom variable\b', r'\bprobability distribution\b',
        r'\bbernoulli\b', r'\bbinomial distribution\b', r'\bcoin is tossed\b', r'\bdice is thrown\b', r'\bcards are drawn\b'
    ])
}

# ==============================================================================
# 2. CBSE PHYSICS RULES (Class 12 - 14 Chapters)
# ==============================================================================
PHYSICS_CHAPTERS = {
    1: ("Electric Charges and Fields", [
        r'\bcoulomb\b', r'\belectric dipole\b', r'\bdipole moment\b', r'\belectric flux\b', r'\bgauss\'s\b',
        r'\belectric field\b', r'\bpoint charge\b', r'\blinear charge density\b', r'\bsurface charge density\b',
        r'\belectric lines of force\b', r'\btorque on dipole\b'
    ]),
    2: ("Electrostatic Potential and Capacitance", [
        r'\belectric potential\b', r'\bpotential difference\b', r'\bequipotential\b', r'\bcapacitance\b',
        r'\bcapacitor\b', r'\bcapacitors\b', r'\bparallel plate capacitor\b', r'\bdielectric constant\b',
        r'\bdielectric medium\b', r'\benergy stored in capacitor\b', r'\bpotential energy of system of charges\b'
    ]),
    3: ("Current Electricity", [
        r'\bohm\'s law\b', r'\bdrift velocity\b', r'\bmobility\b', r'\bresistivity\b', r'\bconductivity\b',
        r'\bkirchhoff\b', r'\bwheatstone\b', r'\bmeter bridge\b', r'\bpotentiometer\b', r'\binternal resistance\b',
        r'\bcells in series\b', r'\bcells in parallel\b', r'\belectric current\b', r'\bterminal voltage\b'
    ]),
    4: ("Moving Charges and Magnetism", [
        r'\bbiot-savart\b', r'\blorentz force\b', r'\bampere\'s circuital\b', r'\bsolenoid\b', r'\btoroid\b',
        r'\bcyclotron\b', r'\bgalvanometer\b', r'\bmagnetic dipole moment\b', r'\bforce between two parallel\b',
        r'\bcircular coil carrying current\b', r'\bhelical path\b'
    ]),
    5: ("Magnetism and Matter", [
        r'\bearth\'s magnetic\b', r'\bmagnetic declination\b', r'\bdip angle\b', r'\bangle of dip\b',
        r'\bsusceptibility\b', r'\bdiamagnetic\b', r'\bparamagnetic\b', r'\bferromagnetic\b',
        r'\bhysteresis\b', r'\bbar magnet\b', r'\bcurie temperature\b'
    ]),
    6: ("Electromagnetic Induction", [
        r'\bfaraday\'s law\b', r'\blenz\'s law\b', r'\bmotional emf\b', r'\binduced emf\b', r'\binduced current\b',
        r'\beddy currents\b', r'\bself-induction\b', r'\bself-inductance\b', r'\bmutual induction\b',
        r'\bmutual inductance\b', r'\bmagnetic flux linked\b'
    ]),
    7: ("Alternating Current", [
        r'\balternating current\b', r'\brms value\b', r'\bac voltage\b', r'\breactance\b', r'\bimpedance\b',
        r'\blcr circuit\b', r'\bresonance in lcr\b', r'\bquality factor\b', r'\bpower factor\b',
        r'\btransformer\b', r'\bwattless current\b', r'\bstep-up\b', r'\bstep-down\b'
    ]),
    8: ("Electromagnetic Waves", [
        r'\bdisplacement current\b', r'\belectromagnetic spectrum\b', r'\bem waves\b', r'\bmicrowaves\b',
        r'\bradio waves\b', r'\binfrared\b', r'\bultraviolet\b', r'\bx-rays\b', r'\bgamma rays\b',
        r'\bmaxwell\'s equations\b', r'\bpointing vector\b'
    ]),
    9: ("Ray Optics and Optical Instruments", [
        r'\brefraction\b', r'\breflection\b', r'\bsnell\'s law\b', r'\btotal internal reflection\b',
        r'\boptical fiber\b', r'\blens maker\b', r'\bprism\b', r'\bangle of deviation\b', r'\bmicroscope\b',
        r'\btelescope\b', r'\bmagnifying power\b', r'\bfocal length\b', r'\bconvex lens\b', r'\bconcave mirror\b'
    ]),
    10: ("Wave Optics", [
        r'\bhuygens\b', r'\bwavefront\b', r'\binterference\b', r'\byoung\'s double slit\b', r'\bfringe width\b',
        r'\bcoherent sources\b', r'\bdiffraction\b', r'\bsingle slit\b', r'\bpolarization\b',
        r'\bbrewster\'s\b', r'\bmalus\b', r'\bcentral maxima\b'
    ]),
    11: ("Dual Nature of Radiation and Matter", [
        r'\bphotoelectric effect\b', r'\bwork function\b', r'\bthreshold frequency\b', r'\bthreshold wavelength\b',
        r'\bstopping potential\b', r'\bde broglie\b', r'\bdavisson-germer\b', r'\bphoton\b', r'\beffort of radiation\b'
    ]),
    12: ("Atoms", [
        r'\brutherford\b', r'\balpha particle scattering\b', r'\bbohr\'s model\b', r'\bbohr radius\b',
        r'\bhydrogen spectrum\b', r'\blyman series\b', r'\bbalmer series\b', r'\bpaschen\b', r'\benergy levels of hydrogen\b',
        r'\bclosest approach\b', r'\bimpact parameter\b'
    ]),
    13: ("Nuclei", [
        r'\bmass defect\b', r'\bbinding energy\b', r'\bnuclear force\b', r'\bradioactivity\b', r'\bhalf-life\b',
        r'\bdecay constant\b', r'\balpha decay\b', r'\bbeta decay\b', r'\bgamma decay\b', r'\bnuclear fission\b',
        r'\bnuclear fusion\b', r'\batomic mass unit\b', r'\bisotopes\b', r'\bisobars\b'
    ]),
    14: ("Semiconductor Electronics: Materials, Devices and Simple Circuits", [
        r'\bsemiconductor\b', r'\bintrinsic\b', r'\bextrinsic\b', r'\bn-type\b', r'\bp-type\b', r'\bp-n junction\b',
        r'\bforward bias\b', r'\breverse bias\b', r'\bzener diode\b', r'\brectifier\b', r'\blogic gate\b',
        r'\band gate\b', r'\bor gate\b', r'\bnand gate\b', r'\bnor gate\b', r'\bphotodiode\b', r'\bled\b', r'\bsolar cell\b'
    ])
}

# ==============================================================================
# 3. CBSE CHEMISTRY RULES (Class 12 - 10 Chapters)
# ==============================================================================
CHEMISTRY_CHAPTERS = {
    1: ("Solutions", [
        r'\bmolarity\b', r'\bmolality\b', r'\bmole fraction\b', r'\bhenry\'s law\b', r'\braoult\'s law\b',
        r'\bideal solution\b', r'\bnon-ideal solution\b', r'\bazeotrope\b', r'\bcolligative\b',
        r'\belevation in boiling\b', r'\bdepression in freezing\b', r'\bosmotic pressure\b', r'\bvan\'t hoff\b'
    ]),
    2: ("Electrochemistry", [
        r'\bgalvanic cell\b', r'\bnernst equation\b', r'\belectrode potential\b', r'\bemf of the cell\b',
        r'\bkohlrausch\b', r'\bmolar conductivity\b', r'\bfaraday\'s law\b', r'\belectrolysis\b',
        r'\bfuel cell\b', r'\bcorrosion\b', r'\blead storage battery\b'
    ]),
    3: ("Chemical Kinetics", [
        r'\brate of reaction\b', r'\border of reaction\b', r'\bmolecularity\b', r'\brate constant\b',
        r'\bhalf-life\b', r'\bfirst order reaction\b', r'\bzero order reaction\b', r'\bactivation energy\b',
        r'\barrhenius\b', r'\brate law\b', r'\bpseudo first order\b', r'\bcollision theory\b'
    ]),
    4: ("The d- and f-Block Elements", [
        r'\btransition element\b', r'\bd-block\b', r'\bf-block\b', r'\blanthanoid\b', r'\bactinoid\b',
        r'\blanthanoid contraction\b', r'\binterstitial compounds\b', r'\bkmno4\b', r'\bk2cr2o7\b',
        r'\bpotassium permanganate\b', r'\bpotassium dichromate\b', r'\bmagnetic moment of transition\b'
    ]),
    5: ("Coordination Compounds", [
        r'\bcoordination compound\b', r'\bligand\b', r'\bcoordination number\b', r'\bwerner\'s theory\b',
        r'\biupac name of coordination\b', r'\bvalence bond theory\b', r'\bvbt\b', r'\bcrystal field\b',
        r'\bcft\b', r'\bisomerism in coordination\b', r'\bchelating\b', r'\[[A-Z][a-z]?\(.+\]'
    ]),
    6: ("Haloalkanes and Haloarenes", [
        r'\bhaloalkane\b', r'\bhaloarene\b', r'\balkyl halide\b', r'\baryl halide\b', r'\bsn1\b', r'\bsn2\b',
        r'\bnucleophilic substitution\b', r'\bsaytzeff\b', r'\bgrignard\b', r'\bwurtz\b', r'\bfittig\b',
        r'\bsandmeyer\b', r'\bchiral\b', r'\benantiomer\b', r'\bracemic\b'
    ]),
    7: ("Alcohols, Phenols and Ethers", [
        r'\balcohol\b', r'\bphenol\b', r'\bether\b', r'\blucas test\b', r'\bkolbe\'s reaction\b',
        r'\breimer-tiemann\b', r'\bwilliamson ether\b', r'\bpicric acid\b', r'\bhydroboration\b',
        r'\bdehydration of alcohol\b', r'\bacidity of phenol\b'
    ]),
    8: ("Aldehydes, Ketones and Carboxylic Acids", [
        r'\baldehyde\b', r'\bketone\b', r'\bcarboxylic acid\b', r'\bcarbonyl\b', r'\brosenmund\b',
        r'\bstephen\b', r'\betard\b', r'\bclemmensen\b', r'\bwolff-kishner\b', r'\btollens\b',
        r'\bfehling\b', r'\baldol\b', r'\bcannizzaro\b', r'\bhvz\b', r'\bhell-volhard\b'
    ]),
    9: ("Amines", [
        r'\bamine\b', r'\bdiazonium\b', r'\bgabriel phthalimide\b', r'\bhoffmann bromamide\b',
        r'\bcarbylamine\b', r'\bhinsberg\b', r'\bcoupling reaction\b', r'\bazo dye\b', r'\bbasic character of amine\b'
    ]),
    10: ("Biomolecules", [
        r'\bcarbohydrate\b', r'\bglucose\b', r'\bfructose\b', r'\bprotein\b', r'\bamino acid\b',
        r'\bpeptide linkage\b', r'\bdenaturation\b', r'\bnucleic acid\b', r'\bdna\b', r'\brna\b',
        r'\bvitamin\b', r'\benzyme\b', r'\breducing sugar\b', r'\bglycosidic linkage\b'
    ])
}

# ==============================================================================
# 4. NEET UG MAPPING RULES (Dispersing generic buckets)
# ==============================================================================
NEET_SPECIFIC_MAP = {
    # Physics Mechanics & Thermal
    "Kinematics & Motion": [r'\bmotion in a straight line\b', r'\bvelocity\b', r'\bacceleration\b', r'\bprojectile\b', r'\btrajectory\b'],
    "Laws of Motion": [r'\bnewton\'s laws\b', r'\bfriction\b', r'\btension in string\b', r'\bpulley\b', r'\bmomentum conservation\b'],
    "Work, Energy and Power": [r'\bwork done\b', r'\bkinetic energy\b', r'\bpotential energy\b', r'\bconservative force\b', r'\bpower\b', r'\bcollision\b'],
    "Rotational Dynamics": [r'\bmoment of inertia\b', r'\btorque\b', r'\bangular momentum\b', r'\bradius of gyration\b', r'\brolling\b'],
    "Gravitation": [r'\bgravitational\b', r'\bescape velocity\b', r'\borbital velocity\b', r'\bkepler\'s\b', r'\bacceleration due to gravity\b'],
    "Mechanical Properties of Fluids & Solids": [r'\bviscosity\b', r'\bsurface tension\b', r'\bbernoulli\b', r'\byoung\'s modulus\b', r'\bpascal\b', r'\bstress\b', r'\bstrain\b'],
    "Thermodynamics & Kinetic Theory": [r'\bcarnot engine\b', r'\bfirst law of thermodynamics\b', r'\badabatic\b', r'\bisothermal\b', r'\bkinetic theory\b', r'\bmolar heat capacity\b'],
    "Oscillations & Waves": [r'\bsimple harmonic motion\b', r'\bshm\b', r'\btime period of pendulum\b', r'\bdoppler effect\b', r'\bsound waves\b', r'\bresonance\b'],

    # Chemistry Physical & Inorganic
    "Atomic Structure & Periodic Trends": [r'\bbohr\b', r'\bquantum numbers\b', r'\belectron affinity\b', r'\bionization enthalpy\b', r'\bperiodic table\b', r'\bpauli\b', r'\bhund\b'],
    "Chemical Bonding & Molecular Structure": [r'\bhybridization\b', r'\bvsepr\b', r'\bmolecular orbital theory\b', r'\bmot\b', r'\bdipole moment\b', r'\bbond order\b'],
    "Thermodynamics (Chemical)": [r'\benthalpy\b', r'\bentropy\b', r'\bgibbs free energy\b', r'\bdelta g\b', r'\bspontaneous\b', r'\bhess\'s law\b'],
    "Equilibrium": [r'\ble chatelier\b', r'\bequilibrium constant\b', r'\bph of\b', r'\bbuffer solution\b', r'\bsolubility product\b', r'\bksp\b'],
    "Redox & Electrochemistry": [r'\boxidation number\b', r'\bredox reaction\b', r'\bnernst equation\b', r'\bfaraday\b', r'\bstandard reduction potential\b'],
    "Organic Chemistry Principles": [r'\biupac name\b', r'\binductive effect\b', r'\bmesomeric effect\b', r'\bhyperconjugation\b', r'\bcarbocation\b', r'\bisomerism\b'],

    # Biology - Botany & Plant Physiology
    "Photosynthesis in Higher Plants": [r'\bphotosynthesis\b', r'\bcalvin cycle\b', r'\bc3\b', r'\bc4\b', r'\brubisco\b', r'\bchlorophyll\b', r'\bz-scheme\b', r'\blight reaction\b'],
    "Respiration in Plants": [r'\bglycolysis\b', r'\bkrebs cycle\b', r'\belectron transport system\b', r'\bets\b', r'\batp synthesis\b', r'\bfermentation\b'],
    "Plant Growth Regulators": [r'\bauxin\b', r'\bgibberellin\b', r'\bcytokinin\b', r'\bethylene\b', r'\babscisic acid\b', r'\bphotoperiodism\b'],
    "Plant Reproduction & Anatomy": [r'\bpollen\b', r'\banther\b', r'\bovule\b', r'\bdouble fertilization\b', r'\bxylem\b', r'\bphloem\b', r'\bstomata\b'],

    # Biology - Zoology & Human Physiology
    "Human Digestion & Absorption": [r'\bstomach\b', r'\bpepsin\b', r'\btrypsin\b', r'\bbile\b', r'\bvilli\b', r'\bpancreas\b', r'\bsmall intestine\b'],
    "Breathing and Exchange of Gases": [r'\blungs\b', r'\balveoli\b', r'\btidal volume\b', r'\boxygen dissociation curve\b', r'\bhaemoglobin\b'],
    "Body Fluids and Circulation": [r'\bheart\b', r'\bblood group\b', r'\becg\b', r'\bcardiac cycle\b', r'\brbc\b', r'\bwbc\b', r'\bplatelets\b'],
    "Excretory Products and Elimination": [r'\bnephron\b', r'\bglomerulus\b', r'\bloop of henle\b', r'\bcounter-current\b', r'\burea\b', r'\bjuxtaglomerular\b'],
    "Locomotion and Movement": [r'\bmuscle\b', r'\bactin\b', r'\bmyosin\b', r'\bsarcomere\b', r'\bbones\b', r'\bjoint\b'],
    "Neural Control & Chemical Coordination": [r'\bneuron\b', r'\baction potential\b', r'\bsynapse\b', r'\breflex arc\b', r'\bpituitary\b', r'\bthyroid\b', r'\badrenal\b', r'\binsulin\b'],
    "Human Reproduction & Genetics": [r'\bmenstrual\b', r'\bovulation\b', r'\bspermatogenesis\b', r'\boogenesis\b', r'\blh\b', r'\bfsh\b', r'\bmendel\b', r'\blinkage\b', r'\bdna replication\b']
}

def classify_text(text, rule_dict):
    best_match = None
    max_score = 0
    t_lower = text.lower()

    for ch_num, (ch_name, patterns) in rule_dict.items():
        score = 0
        for pat in patterns:
            matches = len(re.findall(pat, t_lower, flags=re.IGNORECASE))
            score += matches
        if score > max_score:
            max_score = score
            best_match = (ch_num, ch_name)

    if max_score > 0:
        return best_match
    return None

def process_cbse_math():
    p = os.path.join(DATA_DIR, 'cbse_mathematics.json')
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)

    reclassified = 0
    for q in data:
        curr_ch = q.get('chapter_name', 'Unclassified')
        txt = q.get('text', '')

        # Specific rebalancing: Matrices vs Determinants
        if curr_ch == 'Matrices':
            # If question mentions determinant, |A|, cofactor, adjoint, singular -> move to Determinants
            if re.search(r'\bdeterminant\b|\|A\||\|B\||\bdet\(|\bcofactor\b|\badjoint\b|\badj\(A\)|\bsingular matrix\b', txt, re.I):
                q['chapter_number'] = 4
                q['chapter_name'] = 'Determinants'
                reclassified += 1
                continue

        # Specific rebalancing: Continuity vs Applications of Derivatives
        if curr_ch in ['Continuity and Differentiability', 'Integrals']:
            if re.search(r'\brate of change\b|\bincreasing function\b|\bdecreasing function\b|\bmaxima\b|\bminima\b|\bmaximum value\b|\bminimum value\b|\blocal maxima\b|\bmarginal cost\b', txt, re.I):
                q['chapter_number'] = 6
                q['chapter_name'] = 'Applications of Derivatives'
                reclassified += 1
                continue

        # If Unclassified, General, or None, match against all Math rules
        if curr_ch in ['Unclassified', 'General', None, 'None', '']:
            match = classify_text(txt, MATH_CHAPTERS)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                reclassified += 1

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[CBSE Math] Reclassified {reclassified} questions.")

def process_cbse_physics():
    p = os.path.join(DATA_DIR, 'cbse_physics.json')
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)

    reclassified = 0
    for q in data:
        curr_ch = q.get('chapter_name', 'Unclassified')
        txt = q.get('text', '')

        if curr_ch in ['Unclassified', 'General', None, 'None', '']:
            match = classify_text(txt, PHYSICS_CHAPTERS)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                reclassified += 1

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[CBSE Physics] Reclassified {reclassified} questions.")

def process_cbse_chemistry():
    p = os.path.join(DATA_DIR, 'cbse_chemistry.json')
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)

    reclassified = 0
    for q in data:
        curr_ch = q.get('chapter_name', 'Unclassified')
        txt = q.get('text', '')

        if curr_ch in ['Unclassified', 'General', None, 'None', '']:
            match = classify_text(txt, CHEMISTRY_CHAPTERS)
            if match:
                q['chapter_number'] = match[0]
                q['chapter_name'] = match[1]
                reclassified += 1

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[CBSE Chemistry] Reclassified {reclassified} questions.")

def process_neet():
    p = os.path.join(DATA_DIR, 'neet_all.json')
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)

    reclassified = 0
    generic_buckets = ['General Chemistry', 'General Physics Topics', 'General Physics & Mechanics',
                       'Animal Biology & Physiology', 'Plant Biology Principles']

    for q in data:
        curr_ch = q.get('ncert_chapter', 'General')
        txt = q.get('text', '')

        if curr_ch in generic_buckets:
            # First check NEET specific map
            best_neet = None
            max_s = 0
            for specific_ch, pats in NEET_SPECIFIC_MAP.items():
                s = sum(len(re.findall(pat, txt, re.I)) for pat in pats)
                if s > max_s:
                    max_s = s
                    best_neet = specific_ch
            if max_s > 0 and best_neet:
                q['ncert_chapter'] = best_neet
                reclassified += 1
                continue

            # Fallback to Subject rules
            subj = q.get('subject', '')
            if subj == 'Physics':
                match = classify_text(txt, PHYSICS_CHAPTERS)
                if match:
                    q['ncert_chapter'] = match[1]
                    reclassified += 1
            elif subj == 'Chemistry':
                match = classify_text(txt, CHEMISTRY_CHAPTERS)
                if match:
                    q['ncert_chapter'] = match[1]
                    reclassified += 1

    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[NEET UG] Reclassified {reclassified} generic questions into specific NCERT chapters.")

if __name__ == "__main__":
    process_cbse_math()
    process_cbse_physics()
    process_cbse_chemistry()
    process_neet()
