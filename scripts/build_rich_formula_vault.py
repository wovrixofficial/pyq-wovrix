import json
import re
import os

print("[1/4] Loading scraped formula dataset...")
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/syllab_scraped_formulas.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Common toppers' tips and traps dictionary for major topics
TOPPER_TIPS = {
    "coulomb's law": "⚠️ Common Trap: Always express distance 'r' in meters (not cm or mm), and ensure charges are in Coulombs (convert µC by 10⁻⁶). In a dielectric medium of constant K, F_med = F_air / K.",
    "electric field": "⭐ Pro Tip: Electric field due to a point charge follows the inverse-square law. Field lines never intersect because at the intersection point there would be two directions of field, which is impossible.",
    "electric potential": "⭐ Pro Tip: Electric potential is a scalar quantity! When finding net potential at a point, calculate algebraically with sign (positive for +q, negative for -q).",
    "capacitance": "⚠️ Watch out: When a dielectric slab (dielectric constant K) is inserted: if battery remains connected, V is constant and C increases by K; if battery is disconnected, Q is constant and V decreases by 1/K.",
    "ohm's law": "⚠️ Board Trap: Ohm's law is NOT a universal law! Non-ohmic devices like diodes, transistors, and electrolytes do not follow linear V-I graphs.",
    "resistivity": "⭐ Memory Trick: Resistivity (ρ) depends ONLY on material and temperature, NOT on length or area of cross-section! If a wire is stretched to double length, resistance becomes 4×, but resistivity stays constant.",
    "kirchhoff": "⭐ Rule of Thumb: In KVL loop rule, moving across a resistor in direction of current gives -IR drop; across battery from negative to positive terminal gives +E.",
    "biot savart": "⭐ Right Hand Palm Rule: Point thumb along current I, curl fingers towards point P — palm push gives direction of magnetic field B.",
    "lorentz force": "⚠️ Key Insight: Magnetic force does ZERO work on a charged particle because F is always perpendicular to velocity v. Kinetic energy and speed remain constant; only direction of motion changes!",
    "faraday's law of induction": "⚠️ Lenz's Law Sign: The negative sign in ε = -dΦ/dt represents Lenz's Law, which is a direct consequence of the Conservation of Energy.",
    "alternating current": "⭐ Peak vs RMS: Always remember AC ammeters and voltmeters measure RMS values (I_rms = I_0 / √2 ≈ 0.707 I_0), not peak values!",
    "resonance": "⭐ Pro Tip: At series resonance, impedance is minimum (Z = R), current is maximum, and power factor cos φ = 1 (purely resistive).",
    "photoelectric": "⭐ Threshold Condition: Photoelectric emission is instantaneous (< 10⁻⁹ s). Kinetic energy depends ONLY on frequency of light, while photocurrent depends ONLY on intensity.",
    "de broglie": "⭐ Formula Shortcut: For an electron accelerated through potential difference V, λ = 12.27 / √V Ångströms (0.1 nm).",
    "radioactive decay": "⭐ Half-life Trick: After 'n' half-lives, fraction remaining is (1/2)ⁿ. Number of half-lives n = t / T_half.",
    "snell's law": "⭐ Remember: Light bends TOWARDS normal when going from rarer to denser medium (μ₂ > μ₁). Speed and wavelength decrease, but frequency remains strictly constant!",
    "lens maker": "⚠️ Sign Convention Trap: For biconvex lens, R₁ is positive (+), R₂ is negative (-). For biconcave lens, R₁ is negative (-), R₂ is positive (+).",
    "interference": "⭐ Fringe Width: β = λD/d. To increase fringe width, increase distance between screen and slits (D) or decrease distance between slits (d).",
    "molarity": "⚠️ Board Alert: Molarity depends on temperature because volume of liquid expands with heat! Molality (m) and mole fraction (χ) are temperature independent.",
    "raoult's law": "⭐ Ideal Solution: Follows Raoult's Law over entire concentration range. ΔH_mix = 0, ΔV_mix = 0. E.g., Benzene + Toluene, n-hexane + n-heptane.",
    "osmotic pressure": "⭐ Medical Fact: 0.9% (m/V) NaCl solution is isotonic with human red blood cells. Hypotonic causes swelling/bursting (hemolysis); hypertonic causes shrinkage (crenation).",
    "nernst equation": "⭐ Nernst Shortcut: At 298 K (25°C), 2.303 RT/F = 0.0591. For Daniell cell: E_cell = 1.10 - (0.0591/2) log([Zn²⁺]/[Cu²⁺]).",
    "chemical kinetics": "⭐ Rate Law vs Order: Order is strictly an experimental quantity and can be zero, fractional, or integer. Molecularity is theoretical and must be a positive integer (1, 2, or 3).",
    "integration by parts": "⭐ ILATE Rule: Choose first function 'u' by priority: Inverse trig > Logarithmic > Algebraic > Trigonometric > Exponential.",
    "matrix multiplication": "⚠️ Watch Order: Matrix multiplication is NOT commutative! AB ≠ BA in general. Also, (AB)ᵀ = Bᵀ Aᵀ.",
    "quadratic formula": "⭐ Discriminant Check: D = b² - 4ac. If D > 0: two distinct real roots; D = 0: two equal real roots; D < 0: complex conjugate roots.",
    "distance formula": "⭐ 3D Coordinate Tip: In 3D space, distance between (x₁, y₁, z₁) and (x₂, y₂, z₂) is √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]."
}

def get_topper_tip(name, expr, chapter):
    search_str = f"{name} {expr} {chapter}".lower()
    for key, tip in TOPPER_TIPS.items():
        if key in search_str:
            return tip
    if "physics" in search_str:
        return "⭐ High-Yield Rule: Always verify dimensional consistency before finalizing your answer in numericals. Check that units on both sides of the '=' match!"
    elif "chemistry" in search_str:
        return "⭐ Topper Tip: Check state symbols (aq, s, l, g) and remember temperature must be converted to Kelvin (T = °C + 273.15) for all thermodynamic and kinetic formulas."
    elif "math" in search_str:
        return "⭐ Pro Shortcut: Look for symmetry or domain restrictions before expanding. Always add '+ C' in indefinite integrals to avoid losing 1 mark!"
    else:
        return "⭐ Quick Revision Note: Master this formula for 1-mark objective and 3-mark derivation questions in board and competitive exams."

def format_latex(name, expr):
    clean = expr.strip()
    note = ""
    if ';' in clean:
        parts = clean.split(';', 1)
        clean = parts[0].strip()
        note = parts[1].strip()
    elif ',' in clean and any(w in clean for w in ['where', 'unit', 'same', 'at ']):
        parts = clean.split(',', 1)
        clean = parts[0].strip()
        note = parts[1].strip()

    latex = clean
    replacements = [
        ('×', r' \times '),
        ('·', r' \cdot '),
        ('ε₀', r'\varepsilon_0'),
        ('ε', r'\varepsilon'),
        ('π', r'\pi'),
        ('λ', r'\lambda'),
        ('ν', r'\nu'),
        ('μ', r'\mu'),
        ('ρ', r'\rho'),
        ('σ', r'\sigma'),
        ('θ', r'\theta'),
        ('ω', r'\omega '),
        ('Δ', r'\Delta '),
        ('Φ', r'\Phi'),
        ('α', r'\alpha'),
        ('β', r'\beta'),
        ('γ', r'\gamma'),
        ('Σ', r'\sum '),
        ('½', r'\frac{1}{2}'),
        ('⅓', r'\frac{1}{3}'),
        ('¼', r'\frac{1}{4}'),
        ('√', r'\sqrt'),
        ('°', r'^\circ'),
        ('−', '-'),
        ('²', '^2'),
        ('³', '^3'),
        ('₁', '_1'),
        ('₂', '_2'),
        ('₃', '_3'),
        ('₄', '_4'),
        ('₀', '_0'),
        ('ₐ', '_a'),
        ('ᵇ', '^b'),
        ('ˣ', '^x'),
    ]
    for orig, rep in replacements:
        latex = latex.replace(orig, rep)

    nm = name.lower()
    if "ohm's law" in nm:
        latex = r"V = I \cdot R"
    elif "coulomb's law" in nm:
        latex = r"F = \frac{1}{4\pi\varepsilon_0} \frac{|q_1 q_2|}{r^2}"
    elif "electric current" in nm:
        latex = r"I = \frac{Q}{t}"
    elif "resistivity" in nm:
        latex = r"R = \rho \frac{L}{A}"
    elif "series resistance" in nm or "resistances in series" in nm:
        latex = r"R_{\text{eq}} = R_1 + R_2 + R_3 + \dots"
    elif "parallel resistance" in nm or "resistances in parallel" in nm:
        latex = r"\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots"
    elif "power of electric" in nm or "power dissipated" in nm or "electric power" in nm:
        latex = r"P = V I = I^2 R = \frac{V^2}{R}"
    elif "joule's heating" in nm:
        latex = r"H = I^2 R t = V I t"
    elif "nernst equation" in nm:
        latex = r"E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{0.0591}{n} \log_{10} Q"
    elif "faraday's first law" in nm:
        latex = r"m = Z \cdot I \cdot t = \frac{M \cdot I \cdot t}{n \cdot F}"
    elif "cell emf" in nm:
        latex = r"E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}"
    elif "gibbs free energy" in nm:
        latex = r"\Delta G^\circ = -n F E^\circ_{\text{cell}}"
    elif "photoelectric" in nm:
        latex = r"h\nu = \Phi_0 + K_{\max} = h\nu_0 + \frac{1}{2} m v_{\max}^2"
    elif "de broglie" in nm:
        latex = r"\lambda = \frac{h}{p} = \frac{h}{mv} = \frac{h}{\sqrt{2mE}}"
    elif "radioactive decay" in nm:
        latex = r"N(t) = N_0 e^{-\lambda t}, \quad T_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}"
    elif "molarity" in nm:
        latex = r"M = \frac{\text{moles of solute}}{\text{volume of solution (L)}}"
    elif "molality" in nm:
        latex = r"m = \frac{\text{moles of solute}}{\text{mass of solvent (kg)}}"
    elif "mole fraction" in nm:
        latex = r"\chi_A = \frac{n_A}{n_A + n_B}, \quad \chi_A + \chi_B = 1"
    elif "raoult's law" in nm:
        latex = r"P_A = \chi_A \cdot P^\circ_A, \quad P_{\text{total}} = P_A + P_B"
    elif "elevation of boiling" in nm:
        latex = r"\Delta T_b = i \cdot K_b \cdot m"
    elif "depression of freezing" in nm:
        latex = r"\Delta T_f = i \cdot K_f \cdot m"
    elif "osmotic pressure" in nm:
        latex = r"\pi = i C R T = i \left(\frac{n}{V}\right) R T"
    elif "arrhenius equation" in nm:
        latex = r"k = A e^{-\frac{E_a}{RT}}, \quad \ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)"
    elif "first order" in nm and "rate" in nm:
        latex = r"k = \frac{2.303}{t} \log_{10}\left(\frac{[A]_0}{[A]}\right), \quad t_{1/2} = \frac{0.693}{k}"
    elif "snell's law" in nm:
        latex = r"\frac{\sin i}{\sin r} = \frac{\mu_2}{\mu_1} = \frac{v_1}{v_2}"
    elif "lens formula" in nm:
        latex = r"\frac{1}{f} = \frac{1}{v} - \frac{1}{u}, \quad m = \frac{v}{u}"
    elif "mirror formula" in nm:
        latex = r"\frac{1}{f} = \frac{1}{v} + \frac{1}{u}, \quad m = -\frac{v}{u}"
    elif "lens maker" in nm:
        latex = r"\frac{1}{f} = (\mu - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)"
    elif "integration by parts" in nm:
        latex = r"\int u \cdot v \, dx = u \int v \, dx - \int \left( \frac{du}{dx} \int v \, dx \right) dx"
    elif "power rule integration" in nm:
        latex = r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)"
    elif "quadratic formula" in nm or "roots of quadratic" in nm:
        latex = r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
    elif "distance formula" in nm:
        latex = r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}"
    elif "section formula" in nm:
        latex = r"P(x,y) = \left( \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \right)"
    elif "biot savart" in nm:
        latex = r"d\vec{B} = \frac{\mu_0}{4\pi} \frac{I (d\vec{l} \times \hat{r})}{r^2}"
    elif "lorentz force" in nm:
        latex = r"\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})"
    elif "magnetic force on charge" in nm:
        latex = r"F = q v B \sin\theta = q(\vec{v} \times \vec{B})"
    elif "faraday's law of induction" in nm or "electromagnetic induction" in nm:
        latex = r"\varepsilon = -\frac{d\Phi_B}{dt} = -N \frac{\Delta \Phi_B}{\Delta t}"
    elif "gravitational force" in nm or "newton's law of gravitation" in nm:
        latex = r"F = G \frac{M_1 M_2}{r^2}"
    elif "acceleration due to gravity" in nm:
        latex = r"g = \frac{GM}{R^2}, \quad g_h = g \left(1 - \frac{2h}{R}\right)"
    elif "escape velocity" in nm:
        latex = r"v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR} \approx 11.2 \text{ km/s}"
    elif "orbital velocity" in nm:
        latex = r"v_o = \sqrt{\frac{GM}{R}} = \sqrt{gR} \approx 7.9 \text{ km/s}"
    elif "ac voltage" in nm:
        latex = r"V = V_0 \sin(\omega t + \phi)"
    elif "ac current" in nm:
        latex = r"I = I_0 \sin(\omega t + \phi)"
    elif "rms current" in nm:
        latex = r"I_{\text{rms}} = \frac{I_0}{\sqrt{2}} \approx 0.707 I_0"
    elif "rms voltage" in nm:
        latex = r"V_{\text{rms}} = \frac{V_0}{\sqrt{2}} \approx 0.707 V_0"

    latex = re.sub(r'(?<!\\)(sin|cos|tan|cot|sec|csc|ln|log)\(', r'\\\1(', latex)

    if '/' in latex and r'\frac' not in latex and len(latex) < 60:
        latex = re.sub(r'([A-Za-z0-9_]+)\s*/\s*([A-Za-z0-9_]+)', r'\\frac{\1}{\2}', latex)

    return latex, note

print("[2/4] Processing and enriching formula records...")
enriched_chapters = []
seen_slugs = set()

def get_practice_url(cls_num, subj, chap_slug):
    if cls_num == 12:
        return f"/practice/?exam=cbse&subject={subj}&chapter={chap_slug.replace('-', '+')}"
    elif cls_num in [10, 11]:
        return f"/practice/?exam=cbse&subject={subj}"
    else:
        return f"/practice/?exam=cbse"

for it in raw_items:
    slug = it['slug']
    parts = slug.split('-')
    if len(parts) >= 3 and parts[0] == 'class' and parts[1].isdigit():
        cls_num = int(parts[1])
        subj_raw = parts[2].lower()
        if subj_raw in ['maths', 'mathematics']:
            subj = 'Mathematics'
            icon = '📐'
        elif subj_raw == 'physics':
            subj = 'Physics'
            icon = '⚛️'
        elif subj_raw == 'chemistry':
            subj = 'Chemistry'
            icon = '🧪'
        elif subj_raw == 'biology':
            subj = 'Biology'
            icon = '🧬'
        elif subj_raw == 'science':
            subj = 'Science'
            icon = '🔬'
        else:
            subj = subj_raw.capitalize()
            icon = '📝'
            
        chap_slug = '-'.join(parts[3:]) if len(parts) > 3 else 'general'
        
        raw_t = it['title']
        clean_title = raw_t.split(' Formulas')[0].split(' — ')[0].replace(f"Class {cls_num} {subj}:", '').strip()
        clean_title = re.sub(r'\(PDF\)', '', clean_title, flags=re.IGNORECASE)
        clean_title = re.sub(r'Formula Sheet.*', '', clean_title, flags=re.IGNORECASE).strip()
        clean_title = re.sub(r'Formulas.*', '', clean_title, flags=re.IGNORECASE).strip()
        clean_title = clean_title.replace('Class ' + str(cls_num) + ' ' + subj, '').strip()
        clean_title = clean_title.replace('Class ' + str(cls_num) + ' Physics & Numerics', '').strip()
        clean_title = clean_title.strip(': -')
        
        if not clean_title or clean_title.lower() in ['general', '']:
            if subj == 'Physics':
                clean_title = 'Core Fundamentals & Constants' if cls_num == 12 else 'Dimensional Analysis & Units'
            elif subj == 'Science':
                clean_title = 'Key Science Laws & Numerics'
            elif subj == 'Mathematics':
                clean_title = 'Algebra & Geometry Foundations'
            else:
                clean_title = f"{subj} Core Master Sheet"

        norm_key = f"c{cls_num}_{subj.lower()}_{chap_slug.replace('-and-', '-').replace('-its-', '-').replace('-modern-physics', '').replace('-calculus', '')}"
        
        if norm_key in seen_slugs:
            continue
        seen_slugs.add(norm_key)
        
        chap_formulas = []
        for raw_f in it.get('formulas', []):
            f_name = raw_f.get('name', '').strip()
            f_expr = raw_f.get('expression', '').strip()
            if not f_name or not f_expr:
                continue
                
            latex_code, note = format_latex(f_name, f_expr)
            tip = get_topper_tip(f_name, f_expr, clean_title)
            
            chap_formulas.append({
                'name': f_name,
                'expression_raw': f_expr,
                'latex': latex_code,
                'note': note,
                'topper_tip': tip,
                'high_yield': any(k in f_name.lower() for k in ['law', 'equation', 'formula', 'theorem', 'decay', 'effect', 'rule', 'first', 'second', 'rms'])
            })
            
        if chap_formulas:
            enriched_chapters.append({
                'id': norm_key,
                'class': f"Class {cls_num}",
                'class_num': cls_num,
                'subject': subj,
                'icon': icon,
                'chapter_title': clean_title,
                'chapter_slug': chap_slug,
                'practice_url': get_practice_url(cls_num, subj, chap_slug),
                'formulas': chap_formulas,
                'formula_count': len(chap_formulas)
            })

subj_order = {'Physics': 1, 'Chemistry': 2, 'Mathematics': 3, 'Biology': 4, 'Science': 5}
enriched_chapters.sort(key=lambda c: (-c['class_num'], subj_order.get(c['subject'], 99), c['chapter_title']))

total_formulas_count = sum(c['formula_count'] for c in enriched_chapters)
print(f"[3/4] Successfully prepared {len(enriched_chapters)} chapters with {total_formulas_count} enriched formulas.")

master_data = {
    'portal': 'LearnOsha Handwritten Formula Vault & Revision Cheat Sheets',
    'academic_session': '2026-2027',
    'total_chapters': len(enriched_chapters),
    'total_formulas': total_formulas_count,
    'classes': ['Class 12', 'Class 11', 'Class 10', 'Class 9'],
    'subjects': ['Physics', 'Chemistry', 'Mathematics', 'Biology'],
    'chapters': enriched_chapters
}

os.makedirs('E:/PYQ_Wovrix_Portal/pyq-wovrix/data', exist_ok=True)
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/formulas_master.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=2, ensure_ascii=False)

print("Saved master formula database to E:/PYQ_Wovrix_Portal/pyq-wovrix/data/formulas_master.json")
