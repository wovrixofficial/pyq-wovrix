import json, os

def build_data():
    derivations = [
        # ==========================================
        # PHYSICS CLASS 12 (CODE 042)
        # ==========================================
        {
            "id": "phys_gauss_wire",
            "subject": "Physics",
            "chapter_num": 1,
            "chapter_name": "Electric Charges and Fields",
            "title": "Electric Field of an Infinitely Long Uniformly Charged Wire",
            "subtopic": "Applications of Gauss's Law",
            "standard_marks": 3,
            "statement": "Using Gauss's law, deduce an expression for the electric field at a distance r from an infinitely long straight wire with uniform linear charge density $\\lambda$.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><line x1='150' y1='10' x2='150' y2='150' stroke='#38bdf8' stroke-width='3'/><text x='160' y='25' fill='#38bdf8' font-size='12'>+ \\lambda</text><ellipse cx='150' cy='40' rx='60' ry='15' fill='none' stroke='#f59e0b' stroke-dasharray='4'/><ellipse cx='150' cy='120' rx='60' ry='15' fill='none' stroke='#f59e0b'/><line x1='90' y1='40' x2='90' y2='120' stroke='#f59e0b'/><line x1='210' y1='40' x2='210' y2='120' stroke='#f59e0b'/><line x1='150' y1='80' x2='210' y2='80' stroke='#ef4444' stroke-width='1.5' marker-end='url(#arrow)'/><text x='175' y='75' fill='#ef4444' font-size='11'>r</text><line x1='210' y1='80' x2='250' y2='80' stroke='#10b981' stroke-width='2'/><text x='255' y='84' fill='#10b981' font-size='12'>\\vec{E}</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Gauss's Law Statement & Gaussian Surface Definition",
                    "marks": "1.0 Mark",
                    "math": "\\oint \\vec{E} \\cdot d\\vec{A} = \\frac{q_{\\text{enc}}}{\\varepsilon_0}",
                    "explanation": "State Gauss's Law correctly. Construct an imaginary cylindrical Gaussian surface of radius $r$ and length $l$ coaxial with the charged line conductor."
                },
                {
                    "step_num": 2,
                    "label": "Flux Integration across Circular Caps & Curved Surface",
                    "marks": "1.0 Mark",
                    "math": "\\Phi = \\int_{\\text{top}} \\vec{E} \\cdot d\\vec{A} + \\int_{\\text{bottom}} \\vec{E} \\cdot d\\vec{A} + \\int_{\\text{curved}} E \\cdot dA = 0 + 0 + E(2\\pi r l)",
                    "explanation": "At flat circular end-faces, $\\vec{E} \\perp d\\vec{A} \\implies \\vec{E} \\cdot d\\vec{A} = 0$. On the curved mantle, $\\vec{E} \\parallel d\\vec{A}$ everywhere and $|\vec{E}|$ is constant by cylindrical symmetry."
                },
                {
                    "step_num": 3,
                    "label": "Charge Enclosure & Final Vector Form",
                    "marks": "1.0 Mark",
                    "math": "q_{\\text{enc}} = \\lambda l \\implies E(2\\pi r l) = \\frac{\\lambda l}{\\varepsilon_0} \\implies E = \\frac{\\lambda}{2\\pi \\varepsilon_0 r} = \\frac{2k\\lambda}{r}",
                    "explanation": "In vector notation, $\\vec{E} = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}\\hat{n}$, directed radially outward if $\\lambda > 0$ and radially inward if $\\lambda < 0$."
                }
            ],
            "invariance_and_limiting_cases": "$E \\propto \\frac{1}{r}$ (inverse first-power distance dependence). Independent of cylinder length $l$.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/1/1", "marks": 3 },
                { "year": 2024, "code": "Set 55/2/1", "marks": 3 },
                { "year": 2023, "code": "Set 55/4/1", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=1"
        },
        {
            "id": "phys_gauss_sheet",
            "subject": "Physics",
            "chapter_num": 1,
            "chapter_name": "Electric Charges and Fields",
            "title": "Electric Field due to an Infinite Uniformly Charged Plane Sheet",
            "subtopic": "Applications of Gauss's Law",
            "standard_marks": 3,
            "statement": "State Gauss's theorem. Deduce an expression for the electric field at a point near a uniformly charged infinite plane thin sheet of surface charge density $\\sigma$.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><rect x='135' y='15' width='30' height='130' fill='rgba(56,189,248,0.15)' stroke='#38bdf8' stroke-width='2'/><text x='142' y='85' fill='#38bdf8' font-size='14'>+\\sigma</text><line x1='50' y1='80' x2='250' y2='80' stroke='#f59e0b' stroke-dasharray='4'/><rect x='60' y='60' width='180' height='40' rx='10' fill='none' stroke='#f59e0b' stroke-width='1.5'/><line x1='240' y1='80' x2='280' y2='80' stroke='#10b981' stroke-width='2'/><text x='285' y='84' fill='#10b981' font-size='12'>\\vec{E}</text><line x1='60' y1='80' x2='20' y2='80' stroke='#10b981' stroke-width='2'/><text x='5' y='84' fill='#10b981' font-size='12'>\\vec{E}</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Pillbox Gaussian Surface Specification",
                    "marks": "1.0 Mark",
                    "math": "\\oint \\vec{E} \\cdot d\\vec{A} = \\frac{q_{\\text{enc}}}{\\varepsilon_0}",
                    "explanation": "Construct a cylindrical pillbox of cross-sectional area $A$ piercing perpendicular to the charged sheet with end-caps equidistant from sheet."
                },
                {
                    "step_num": 2,
                    "label": "Evaluation of Surface Integrals",
                    "marks": "1.0 Mark",
                    "math": "\\Phi = \\int_{\\text{left cap}} E dA + \\int_{\\text{right cap}} E dA + \\int_{\\text{curved}} \\vec{E} \\cdot d\\vec{A} = EA + EA + 0 = 2EA",
                    "explanation": "Curved surface is parallel to $\\vec{E}$, so flux through curved side is zero. Both circular caps contribute $EA$ in the outward normal direction."
                },
                {
                    "step_num": 3,
                    "label": "Charge Enclosure & Resultant Formula",
                    "marks": "1.0 Mark",
                    "math": "q_{\\text{enc}} = \\sigma A \\implies 2EA = \\frac{\\sigma A}{\\varepsilon_0} \\implies E = \\frac{\\sigma}{2\\varepsilon_0}",
                    "explanation": "Vector form: $\\vec{E} = \\frac{\\sigma}{2\\varepsilon_0}\\hat{n}$. Field is completely uniform and independent of distance $r$ from sheet."
                }
            ],
            "invariance_and_limiting_cases": "$E$ does not depend on distance $r$. For two oppositely charged sheets: $E = \\sigma/\\varepsilon_0$ in between and $E = 0$ outside.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/2/1", "marks": 3 },
                { "year": 2025, "code": "Set 55/1/2", "marks": 3 },
                { "year": 2023, "code": "Set 55/3/1", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=1"
        },
        {
            "id": "phys_parallel_plate_dielectric",
            "subject": "Physics",
            "chapter_num": 2,
            "chapter_name": "Electrostatic Potential and Capacitance",
            "title": "Capacitance of a Parallel Plate Capacitor with Dielectric Slab",
            "subtopic": "Dielectrics and Capacitance",
            "standard_marks": 5,
            "statement": "Derive an expression for the capacitance of a parallel plate capacitor having plate area A and plate separation d when a dielectric slab of thickness t (t < d) and dielectric constant K is introduced between the plates.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><rect x='40' y='20' width='10' height='120' fill='#38bdf8'/><text x='35' y='15' fill='#38bdf8' font-size='12'>+Q</text><rect x='250' y='20' width='10' height='120' fill='#ef4444'/><text x='250' y='15' fill='#ef4444' font-size='12'>-Q</text><rect x='100' y='20' width='80' height='120' fill='rgba(245,158,11,0.2)' stroke='#f59e0b' stroke-dasharray='4'/><text x='130' y='85' fill='#f59e0b' font-size='13'>K (t)</text><line x1='50' y1='150' x2='250' y2='150' stroke='#a1a1aa' stroke-width='1'/><text x='145' y='158' fill='#a1a1aa' font-size='11'>d</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Original Vacuum Electric Field & Potential",
                    "marks": "1.0 Mark",
                    "math": "E_0 = \\frac{\\sigma}{\\varepsilon_0} = \\frac{Q}{A\\varepsilon_0}, \\quad C_0 = \\frac{\\varepsilon_0 A}{d}",
                    "explanation": "State electric field in vacuum between plates without dielectric."
                },
                {
                    "step_num": 2,
                    "label": "Modified Field Inside Dielectric Slab",
                    "marks": "1.5 Marks",
                    "math": "E_{\\text{slab}} = \\frac{E_0}{K} = \\frac{Q}{KA\\varepsilon_0}",
                    "explanation": "Due to dielectric polarization, induced charges reduce the effective internal electric field by factor $K$ over thickness $t$."
                },
                {
                    "step_num": 3,
                    "label": "Total Potential Difference Calculation",
                    "marks": "1.5 Marks",
                    "math": "V = E_0(d - t) + E_{\\text{slab}}(t) = E_0(d - t) + \\frac{E_0}{K}t = E_0\\left[(d - t) + \\frac{t}{K}\\right]",
                    "explanation": "Electric potential difference equals work done across vacuum region $(d-t)$ and slab region $t$."
                },
                {
                    "step_num": 4,
                    "label": "Final Capacitance Equation",
                    "marks": "1.0 Mark",
                    "math": "C = \\frac{Q}{V} = \\frac{Q}{\\frac{Q}{A\\varepsilon_0}\\left[(d - t) + \\frac{t}{K}\\right]} = \\frac{\\varepsilon_0 A}{d - t\\left(1 - \\frac{1}{K}\\right)}",
                    "explanation": "If slab completely fills gap ($t = d$), $C = K C_0$. If conducting slab ($K = \\infty$), $C = \\frac{\\varepsilon_0 A}{d - t}$."
                }
            ],
            "invariance_and_limiting_cases": "$C > C_0$ always. For conducting slab ($K \\to \\infty$), $C = \\frac{\\varepsilon_0 A}{d - t}$.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/1/2", "marks": 5 },
                { "year": 2024, "code": "Set 55/3/1", "marks": 5 },
                { "year": 2022, "code": "Set 55/1/1", "marks": 3 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=2"
        },
        {
            "id": "phys_drift_velocity_ohm",
            "subject": "Physics",
            "chapter_num": 3,
            "chapter_name": "Current Electricity",
            "title": "Drift Velocity & Microscopic Deduction of Ohm's Law",
            "subtopic": "Conduction of Electric Current",
            "standard_marks": 5,
            "statement": "Define drift velocity. Derive the relation between electric current and drift velocity of electrons. Hence deduce Ohm's law and obtain the expression for electrical resistivity in terms of relaxation time.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><rect x='50' y='40' width='200' height='80' rx='40' fill='rgba(56,189,248,0.1)' stroke='#38bdf8' stroke-width='2'/><circle cx='100' cy='60' r='5' fill='#ef4444'/><line x1='100' y1='60' x2='70' y2='60' stroke='#ef4444' stroke-width='1.5' marker-end='url(#arrow)'/><text x='70' y='52' fill='#ef4444' font-size='10'>v_d</text><line x1='60' y1='25' x2='240' y2='25' stroke='#10b981' stroke-width='2'/><text x='140' y='20' fill='#10b981' font-size='12'>\\vec{E}</text><text x='140' y='95' fill='#38bdf8' font-size='13'>n, A, L</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Definition & Acceleration Expression",
                    "marks": "1.0 Mark",
                    "math": "\\vec{a} = -\\frac{e\\vec{E}}{m}, \\quad \\vec{v}_d = -\\frac{e\\vec{E}\\tau}{m}",
                    "explanation": "Drift velocity is average velocity acquired by free electrons in direction opposite to external electric field. Relaxation time $\\tau$ is mean time between successive collisions."
                },
                {
                    "step_num": 2,
                    "label": "Current vs Drift Velocity Relation",
                    "marks": "1.5 Marks",
                    "math": "dq = n e (A v_d dt) \\implies I = \\frac{dq}{dt} = n e A v_d",
                    "explanation": "Total number of electrons in length $v_d dt$ is $n A v_d dt$. Total charge flowing per unit time gives $I = n e A v_d$."
                },
                {
                    "step_num": 3,
                    "label": "Substitution of Electric Field & Potential",
                    "marks": "1.5 Marks",
                    "math": "I = n e A \\left(\\frac{e V}{m L}\\tau\\right) = \\left(\\frac{n e^2 A \\tau}{m L}\\right) V",
                    "explanation": "Since uniform electric field $E = V/L$, substitute into $v_d$ equation."
                },
                {
                    "step_num": 4,
                    "label": "Deduction of Ohm's Law & Resistivity Formula",
                    "marks": "1.0 Mark",
                    "math": "\\frac{V}{I} = \\left(\\frac{m}{n e^2 \\tau}\\right) \\frac{L}{A} = R \\implies \\rho = \\frac{m}{n e^2 \\tau}",
                    "explanation": "At constant temperature, $m, n, e, \\tau$ are constant, verifying $V/I = \\text{constant} = R$ (Ohm's Law)."
                }
            ],
            "invariance_and_limiting_cases": "Current density $J = \sigma E$ where conductivity $\sigma = \frac{n e^2 \tau}{m}$. For metals, as $T \\uparrow$, $\\tau \\downarrow \\implies \\rho \\uparrow$.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/1/1", "marks": 5 },
                { "year": 2024, "code": "Set 55/2/2", "marks": 5 },
                { "year": 2023, "code": "Set 55/5/1", "marks": 3 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=3"
        },
        {
            "id": "phys_lens_maker",
            "subject": "Physics",
            "chapter_num": 9,
            "chapter_name": "Ray Optics and Optical Instruments",
            "title": "Lens Maker's Formula for a Thin Double Convex Lens",
            "subtopic": "Refraction at Spherical Surfaces",
            "standard_marks": 5,
            "statement": "Using the relation for refraction at a curved spherical surface, derive the expression for lens maker's formula for a thin double convex lens.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><ellipse cx='150' cy='80' rx='25' ry='60' fill='rgba(56,189,248,0.2)' stroke='#38bdf8' stroke-width='2'/><line x1='20' y1='80' x2='280' y2='80' stroke='#a1a1aa' stroke-dasharray='4'/><circle cx='50' cy='80' r='3' fill='#f59e0b'/><text x='45' y='95' fill='#f59e0b' font-size='11'>O</text><circle cx='230' cy='80' r='3' fill='#10b981'/><text x='230' y='95' fill='#10b981' font-size='11'>I</text><circle cx='270' cy='80' r='3' fill='#ef4444'/><text x='270' y='95' fill='#ef4444' font-size='11'>I_1</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Refraction at First Spherical Surface (Radius R1)",
                    "marks": "1.5 Marks",
                    "math": "\\frac{\\mu_2}{v_1} - \\frac{\\mu_1}{u} = \\frac{\\mu_2 - \\mu_1}{R_1} \\quad \\text{--- (Equation 1)}",
                    "explanation": "Ray starts from object $O$ in rarer medium $\\mu_1$ and refracts into denser medium $\\mu_2$ at first surface, forming virtual image at $I_1$."
                },
                {
                    "step_num": 2,
                    "label": "Refraction at Second Spherical Surface (Radius R2)",
                    "marks": "1.5 Marks",
                    "math": "\\frac{\\mu_1}{v} - \\frac{\\mu_2}{v_1} = \\frac{\\mu_1 - \\mu_2}{R_2} = -\\frac{\\mu_2 - \\mu_1}{R_2} \\quad \\text{--- (Equation 2)}",
                    "explanation": "Virtual image $I_1$ acts as virtual object for second surface separating $\\mu_2$ into rarer medium $\\mu_1$, forming final image $I$ at distance $v$."
                },
                {
                    "step_num": 3,
                    "label": "Adding Both Refraction Equations",
                    "marks": "1.0 Mark",
                    "math": "\\mu_1\\left(\\frac{1}{v} - \\frac{1}{u}\\right) = (\\mu_2 - \\mu_1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)",
                    "explanation": "Add (1) and (2); intermediate term $\\frac{\\mu_2}{v_1}$ cancels out algebraically."
                },
                {
                    "step_num": 4,
                    "label": "Lens Maker's Master Formula",
                    "marks": "1.0 Mark",
                    "math": "\\frac{1}{f} = \\left(\\frac{\\mu_2}{\\mu_1} - 1\\right)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = (\\mu - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)",
                    "explanation": "By definition of focus: when $u = \\infty$, $v = f \\implies \\frac{1}{v} - \\frac{1}{u} = \\frac{1}{f}$."
                }
            ],
            "invariance_and_limiting_cases": "For equiconvex lens ($R_1 = R, R_2 = -R$): $1/f = 2(\\mu - 1)/R$. If placed in water ($\mu_{\\text{med}} > 1$), focal length increases ($f_{\\text{water}} \\approx 4 f_{\\text{air}}$).",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/1/1", "marks": 5 },
                { "year": 2025, "code": "Set 55/2/3", "marks": 5 },
                { "year": 2024, "code": "Set 55/4/1", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=9"
        },
        {
            "id": "phys_ydse_fringe",
            "subject": "Physics",
            "chapter_num": 10,
            "chapter_name": "Wave Optics",
            "title": "Fringe Width Expression in Young's Double Slit Experiment (YDSE)",
            "subtopic": "Wave Interference & Coherent Sources",
            "standard_marks": 5,
            "statement": "Describe Young's double slit experiment. Derive the conditions for constructive and destructive interference, and obtain the expression for the fringe width of bright and dark fringes.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><line x1='50' y1='40' x2='50' y2='120' stroke='#38bdf8' stroke-width='3'/><circle cx='50' cy='55' r='3' fill='#f59e0b'/><text x='30' y='58' fill='#f59e0b' font-size='10'>S1</text><circle cx='50' cy='105' r='3' fill='#f59e0b'/><text x='30' y='108' fill='#f59e0b' font-size='10'>S2</text><line x1='240' y1='20' x2='240' y2='140' stroke='#a1a1aa' stroke-width='2'/><line x1='50' y1='55' x2='240' y2='60' stroke='#10b981'/><line x1='50' y1='105' x2='240' y2='60' stroke='#10b981'/><text x='250' y='65' fill='#10b981' font-size='11'>P(y)</text><text x='140' y='145' fill='#a1a1aa' font-size='12'>D</text><text x='58' y='85' fill='#f59e0b' font-size='11'>d</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Geometric Path Difference Setup",
                    "marks": "1.5 Marks",
                    "math": "\\Delta x = S_2 P - S_1 P = \\frac{2yd}{S_2 P + S_1 P} \\approx \\frac{yd}{D}",
                    "explanation": "Since $d \\ll D$, $(S_2 P)^2 - (S_1 P)^2 = [D^2 + (y + d/2)^2] - [D^2 + (y - d/2)^2] = 2yd$. Approximating $S_2P + S_1P \\approx 2D$."
                },
                {
                    "step_num": 2,
                    "label": "Constructive & Destructive Position Conditions",
                    "marks": "1.5 Marks",
                    "math": "y_n^{\\text{bright}} = n\\frac{\\lambda D}{d}, \\quad y_n^{\\text{dark}} = \\left(n - \\frac{1}{2}\\right)\\frac{\\lambda D}{d}",
                    "explanation": "Bright fringes require path difference $\\Delta x = n\\lambda$. Dark fringes require $\\Delta x = (2n-1)\\frac{\\lambda}{2}$."
                },
                {
                    "step_num": 3,
                    "label": "Fringe Width Derivation",
                    "marks": "2.0 Marks",
                    "math": "\\beta = y_{n} - y_{n-1} = n\\frac{\\lambda D}{d} - (n-1)\\frac{\\lambda D}{d} = \\frac{\\lambda D}{d}",
                    "explanation": "Distance between any two consecutive bright or dark fringes is identical: $\\beta_{\\text{bright}} = \\beta_{\\text{dark}} = \\frac{\\lambda D}{d}$. Proves all fringes have equal width."
                }
            ],
            "invariance_and_limiting_cases": "If apparatus immersed in liquid with index $\\mu$, fringe width decreases to $\\beta' = \\beta/\\mu$.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/3/1", "marks": 5 },
                { "year": 2024, "code": "Set 55/1/1", "marks": 5 },
                { "year": 2023, "code": "Set 55/2/1", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=10"
        },
        {
            "id": "phys_lcr_series",
            "subject": "Physics",
            "chapter_num": 7,
            "chapter_name": "Alternating Current",
            "title": "Impedance and Resonance in a Series LCR Circuit",
            "subtopic": "AC Circuits & Phasors",
            "standard_marks": 5,
            "statement": "An AC voltage $V = V_0 \\sin(\\omega t)$ is applied across a series combination of an inductor L, capacitor C, and resistor R. Using a phasor diagram, deduce expressions for the impedance of the circuit and the phase difference between voltage and current. Hence obtain the condition for electrical resonance.",
            "diagram_svg": "<svg viewBox='0 0 300 160' class='deriv-diagram-svg'><line x1='150' y1='80' x2='260' y2='80' stroke='#38bdf8' stroke-width='2'/><text x='245' y='95' fill='#38bdf8' font-size='11'>V_R = I R</text><line x1='150' y1='80' x2='150' y2='20' stroke='#f59e0b' stroke-width='2'/><text x='155' y='30' fill='#f59e0b' font-size='11'>V_L</text><line x1='150' y1='80' x2='150' y2='140' stroke='#ef4444' stroke-width='2'/><text x='155' y='135' fill='#ef4444' font-size='11'>V_C</text><line x1='150' y1='80' x2='240' y2='35' stroke='#10b981' stroke-width='2'/><text x='245' y='40' fill='#10b981' font-size='12'>V_0</text><path d='M180,80 A30,30 0 0,0 174,67' fill='none' stroke='#a1a1aa'/><text x='182' y='72' fill='#a1a1aa' font-size='10'>\\phi</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Phasor Diagram Construction & Voltage Components",
                    "marks": "1.5 Marks",
                    "math": "V_R = I_0 R, \\quad V_L = I_0 X_L = I_0 (\\omega L), \\quad V_C = I_0 X_C = \\frac{I_0}{\\omega C}",
                    "explanation": "$V_R$ is in phase with current $I_0$; $V_L$ leads by $\\pi/2$; $V_C$ lags by $\\pi/2$."
                },
                {
                    "step_num": 2,
                    "label": "Impedance Triangle & Master Impedance Formula",
                    "marks": "2.0 Marks",
                    "math": "V_0^2 = V_R^2 + (V_L - V_C)^2 = I_0^2 [R^2 + (X_L - X_C)^2] \\implies Z = \\sqrt{R^2 + \\left(\\omega L - \\frac{1}{\\omega C}\\right)^2}",
                    "explanation": "Net reactive voltage is $(V_L - V_C)$. Resultant applied voltage phasor magnitude gives impedance $Z = V_0 / I_0$."
                },
                {
                    "step_num": 3,
                    "label": "Phase Angle & Electrical Resonance Condition",
                    "marks": "1.5 Marks",
                    "math": "\\tan\\phi = \\frac{X_L - X_C}{R}. \\quad \\text{At resonance: } X_L = X_C \\implies \\omega_0 L = \\frac{1}{\\omega_0 C} \\implies \\omega_0 = \\frac{1}{\\sqrt{LC}}",
                    "explanation": "At resonance, impedance is purely resistive ($Z = R$), current is maximum ($I_0 = V_0/R$), and power factor $\\cos\\phi = 1$."
                }
            ],
            "invariance_and_limiting_cases": "Quality factor $Q = \\frac{\\omega_0 L}{R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}$. At resonance, circuit is purely resistive and current leads by $0$ rad.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 55/1/3", "marks": 5 },
                { "year": 2024, "code": "Set 55/2/1", "marks": 5 },
                { "year": 2023, "code": "Set 55/1/2", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Physics&chapter=7"
        },

        # ==========================================
        # CHEMISTRY CLASS 12 (CODE 043)
        # ==========================================
        {
            "id": "chem_first_order_kinetics",
            "subject": "Chemistry",
            "chapter_num": 3,
            "chapter_name": "Chemical Kinetics",
            "title": "Integrated Rate Equation and Half-Life of a First-Order Reaction",
            "subtopic": "Rate Equations & Half-Life",
            "standard_marks": 5,
            "statement": "Derive the integrated rate equation for a first-order reaction $R \\to P$. Hence prove that the half-life period of a first-order reaction is independent of the initial concentration of the reactant.",
            "diagram_svg": "<svg viewBox='0 0 300 140' class='deriv-diagram-svg'><line x1='40' y1='110' x2='260' y2='110' stroke='#a1a1aa' stroke-width='2'/><line x1='40' y1='110' x2='40' y2='20' stroke='#a1a1aa' stroke-width='2'/><text x='250' y='125' fill='#a1a1aa' font-size='11'>t</text><text x='15' y='25' fill='#a1a1aa' font-size='11'>\\ln[R]</text><line x1='40' y1='30' x2='240' y2='100' stroke='#38bdf8' stroke-width='2'/><text x='160' y='55' fill='#38bdf8' font-size='12'>\\text{Slope} = -k</text><text x='50' y='35' fill='#f59e0b' font-size='11'>\\ln[R]_0</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Differential Rate Law Expression",
                    "marks": "1.0 Mark",
                    "math": "-\\frac{d[R]}{dt} = k[R]^1 \\implies \\frac{d[R]}{[R]} = -k dt",
                    "explanation": "Set up differential rate law for first-order reaction where rate is directly proportional to reactant concentration."
                },
                {
                    "step_num": 2,
                    "label": "Definite Integration with Boundary Conditions",
                    "marks": "1.5 Marks",
                    "math": "\\int_{[R]_0}^{[R]} \\frac{d[R]}{[R]} = -k \\int_0^t dt \\implies \\ln\\frac{[R]}{[R]_0} = -k t \\implies [R] = [R]_0 e^{-kt}",
                    "explanation": "Integrate between limits: at $t = 0$, concentration is $[R]_0$; at time $t$, concentration is $[R]$."
                },
                {
                    "step_num": 3,
                    "label": "Logarithm Base-10 Standard Form",
                    "marks": "1.0 Mark",
                    "math": "k = \\frac{2.303}{t}\\log_{10}\\left(\\frac{[R]_0}{[R]}\\right)",
                    "explanation": "Convert natural logarithm to common base-10 logarithm: $\\ln x = 2.303 \\log_{10} x$."
                },
                {
                    "step_num": 4,
                    "label": "Half-Life Period Proof",
                    "marks": "1.5 Marks",
                    "math": "t = t_{1/2} \\implies [R] = \\frac{[R]_0}{2} \\implies k = \\frac{2.303}{t_{1/2}}\\log_{10}(2) = \\frac{2.303 \\times 0.3010}{t_{1/2}} \\implies t_{1/2} = \\frac{0.693}{k}",
                    "explanation": "Since $[R]_0$ cancels out completely, $t_{1/2}$ is proven to be strictly independent of initial concentration."
                }
            ],
            "invariance_and_limiting_cases": "$t_{1/2} = 0.693/k$. For zero-order reaction, $t_{1/2} = [R]_0 / 2k$ (dependent on initial concentration).",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 56/1/1", "marks": 5 },
                { "year": 2025, "code": "Set 56/2/1", "marks": 3 },
                { "year": 2024, "code": "Set 56/3/1", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Chemistry&chapter=3"
        },
        {
            "id": "chem_nernst_equation",
            "subject": "Chemistry",
            "chapter_num": 2,
            "chapter_name": "Electrochemistry",
            "title": "Nernst Equation for Electrochemical Cell EMF & Equilibrium Constant",
            "subtopic": "Electrochemical Cells & Free Energy",
            "standard_marks": 5,
            "statement": "State the relationship between standard Gibbs energy and cell potential. Deduce the Nernst equation for a general cell reaction $aA + bB \\to cC + dD$ at 298 K, and derive its relationship with the equilibrium constant $K_c$.",
            "diagram_svg": "<svg viewBox='0 0 300 140' class='deriv-diagram-svg'><rect x='40' y='30' width='80' height='80' rx='8' fill='rgba(56,189,248,0.1)' stroke='#38bdf8'/><text x='55' y='75' fill='#38bdf8' font-size='12'>Anode (Zn)</text><rect x='180' y='30' width='80' height='80' rx='8' fill='rgba(239,68,68,0.1)' stroke='#ef4444'/><text x='192' y='75' fill='#ef4444' font-size='12'>Cathode (Cu)</text><path d='M100,30 C120,5 180,5 200,30' fill='none' stroke='#f59e0b' stroke-width='2'/><text x='135' y='18' fill='#f59e0b' font-size='11'>Salt Bridge</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Gibbs Energy & Electrical Work Relationship",
                    "marks": "1.5 Marks",
                    "math": "\\Delta G = -n F E_{\\text{cell}}, \\quad \\Delta G^\\circ = -n F E^\\circ_{\\text{cell}}",
                    "explanation": "Reversible electrical work produced equals decrease in Gibbs free energy ($w_{\\text{elec}} = -\\Delta G = nFE$). $n$ is number of moles of electrons transferred, $F = 96487\\text{ C/mol}$."
                },
                {
                    "step_num": 2,
                    "label": "Thermodynamic Reaction Isotherm Formulation",
                    "marks": "1.5 Marks",
                    "math": "\\Delta G = \\Delta G^\\circ + 2.303 RT \\log_{10} Q \\implies -n F E_{\\text{cell}} = -n F E^\\circ_{\\text{cell}} + 2.303 RT \\log_{10} Q",
                    "explanation": "Divide entire expression by $-nF$ to express in terms of cell potentials."
                },
                {
                    "step_num": 3,
                    "label": "Nernst Equation at 298 K (25 °C)",
                    "marks": "1.0 Mark",
                    "math": "E_{\\text{cell}} = E^\\circ_{\\text{cell}} - \\frac{2.303 RT}{nF}\\log_{10} Q = E^\\circ_{\\text{cell}} - \\frac{0.0591}{n}\\log_{10}\\left(\\frac{[C]^c[D]^d}{[A]^a[B]^b}\\right)",
                    "explanation": "Substitute $R = 8.314\\text{ J K}^{-1}\\text{mol}^{-1}$, $T = 298\\text{ K}$, and $F = 96487\\text{ C/mol}$, yielding numerical factor $0.0591$."
                },
                {
                    "step_num": 4,
                    "label": "Equilibrium Constant Relation",
                    "marks": "1.0 Mark",
                    "math": "\\text{At equilibrium: } E_{\\text{cell}} = 0, \\; Q = K_c \\implies E^\\circ_{\\text{cell}} = \\frac{0.0591}{n}\\log_{10} K_c \\implies \\Delta G^\\circ = -2.303 RT \\log_{10} K_c",
                    "explanation": "When cell reaches chemical equilibrium, current stops flowing ($E_{\\text{cell}} = 0$). Standard potential directly yields equilibrium constant."
                }
            ],
            "invariance_and_limiting_cases": "If $E^\\circ_{\\text{cell}} > 0 \\implies \\Delta G^\\circ < 0$ and $K_c > 1$ (spontaneous cell reaction).",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 56/1/2", "marks": 5 },
                { "year": 2024, "code": "Set 56/2/1", "marks": 5 },
                { "year": 2023, "code": "Set 56/4/1", "marks": 3 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Chemistry&chapter=2"
        },

        # ==========================================
        # MATHEMATICS CLASS 12 (CODE 041)
        # ==========================================
        {
            "id": "math_shortest_distance_skew",
            "subject": "Mathematics",
            "chapter_num": 11,
            "chapter_name": "Three-Dimensional Geometry",
            "title": "Shortest Distance Between Two Skew Lines in Space",
            "subtopic": "3D Vectors & Straight Lines",
            "standard_marks": 5,
            "statement": "Find the shortest distance between two skew lines given in vector form by $\\vec{r} = \\vec{a}_1 + \\lambda \\vec{b}_1$ and $\\vec{r} = \\vec{a}_2 + \\mu \\vec{b}_2$. Hence find condition for lines to intersect.",
            "diagram_svg": "<svg viewBox='0 0 300 140' class='deriv-diagram-svg'><line x1='30' y1='40' x2='260' y2='20' stroke='#38bdf8' stroke-width='2'/><text x='265' y='25' fill='#38bdf8' font-size='11'>L_1 (\\vec{b}_1)</text><line x1='40' y1='120' x2='270' y2='100' stroke='#f59e0b' stroke-width='2'/><text x='275' y='105' fill='#f59e0b' font-size='11'>L_2 (\\vec{b}_2)</text><circle cx='100' cy='35' r='3' fill='#38bdf8'/><text x='95' y='25' fill='#38bdf8' font-size='10'>A(\\vec{a}_1)</text><circle cx='140' cy='113' r='3' fill='#f59e0b'/><text x='140' y='130' fill='#f59e0b' font-size='10'>B(\\vec{a}_2)</text><line x1='180' y1='27' x2='180' y2='107' stroke='#10b981' stroke-width='2'/><text x='185' y='70' fill='#10b981' font-size='12'>d (SD)</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Identification of Common Perpendicular Vector",
                    "marks": "1.5 Marks",
                    "math": "\\vec{n} = \\vec{b}_1 \\times \\vec{b}_2, \\quad \\hat{n} = \\frac{\\vec{b}_1 \\times \\vec{b}_2}{|\\vec{b}_1 \\times \\vec{b}_2|}",
                    "explanation": "Skew lines are non-parallel and non-intersecting in space. The line of shortest distance is perpendicular to both lines, so its direction is along $\\vec{b}_1 \\times \\vec{b}_2$."
                },
                {
                    "step_num": 2,
                    "label": "Projection of Connecting Vector AB onto Common Normal",
                    "marks": "2.0 Marks",
                    "math": "\\vec{AB} = \\vec{a}_2 - \\vec{a}_1, \\quad d = |\\text{Projection of } \\vec{AB} \\text{ on } \\hat{n}| = |\\vec{AB} \\cdot \\hat{n}|",
                    "explanation": "Shortest distance equals magnitude of projection of vector connecting point $A(\\vec{a}_1)$ on $L_1$ to point $B(\\vec{a}_2)$ on $L_2$ onto unit normal $\\hat{n}$."
                },
                {
                    "step_num": 3,
                    "label": "Master Vector Formula & Intersection Condition",
                    "marks": "1.5 Marks",
                    "math": "d = \\left|\\frac{(\\vec{b}_1 \\times \\vec{b}_2) \\cdot (\\vec{a}_2 - \\vec{a}_1)}{|\\vec{b}_1 \\times \\vec{b}_2|}\\right|. \\quad \\text{Lines intersect if } (\\vec{b}_1 \\times \\vec{b}_2) \\cdot (\\vec{a}_2 - \\vec{a}_1) = 0",
                    "explanation": "In Cartesian form: determinant of $[(x_2-x_1), (y_2-y_1), (z_2-z_1); a_1, b_1, c_1; a_2, b_2, c_2]$ divided by denominator."
                }
            ],
            "invariance_and_limiting_cases": "If lines are parallel ($\\vec{b}_1 = \\vec{b}_2 = \\vec{b}$): $d = \\frac{|\\vec{b} \\times (\\vec{a}_2 - \\vec{a}_1)|}{|\\vec{b}|}$.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 65/1/1", "marks": 5 },
                { "year": 2025, "code": "Set 65/2/1", "marks": 5 },
                { "year": 2024, "code": "Set 65/3/1", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Mathematics&chapter=11"
        },
        {
            "id": "math_kings_property",
            "subject": "Mathematics",
            "chapter_num": 7,
            "chapter_name": "Integrals",
            "title": "King's Property of Definite Integrals (Reflection & Symmetry)",
            "subtopic": "Properties of Definite Integrals",
            "standard_marks": 5,
            "statement": "Prove that $\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx$. Hence evaluate $\\int_0^{\\pi/2} \\frac{\\sqrt{\\sin x}}{\\sqrt{\\sin x} + \\sqrt{\\cos x}}dx$.",
            "diagram_svg": "<svg viewBox='0 0 300 130' class='deriv-diagram-svg'><line x1='30' y1='100' x2='260' y2='100' stroke='#a1a1aa' stroke-width='2'/><path d='M40,100 Q100,20 150,60 T250,100' fill='rgba(56,189,248,0.15)' stroke='#38bdf8' stroke-width='2'/><text x='38' y='115' fill='#a1a1aa' font-size='10'>a</text><text x='245' y='115' fill='#a1a1aa' font-size='10'>b</text><text x='130' y='50' fill='#38bdf8' font-size='12'>f(x) \\leftrightarrow f(a+b-x)</text></svg>",
            "marking_scheme_steps": [
                {
                    "step_num": 1,
                    "label": "Substitution & Change of Variable",
                    "marks": "1.5 Marks",
                    "math": "\\text{Let } t = a + b - x \\implies dt = -dx \\implies dx = -dt",
                    "explanation": "Substitute reflection transformation. When $x = a \\implies t = b$; when $x = b \\implies t = a$."
                },
                {
                    "step_num": 2,
                    "label": "Evaluation of Definite Integral with Reversed Limits",
                    "marks": "1.5 Marks",
                    "math": "\\int_a^b f(x)dx = \\int_b^a f(a+b-t)(-dt) = -\\int_b^a f(a+b-t)dt = \\int_a^b f(a+b-t)dt",
                    "explanation": "Reversing limits changes sign: $-\\int_b^a = \\int_a^b$. Since dummy variable can be renamed $t \\to x$, $\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx$."
                },
                {
                    "step_num": 3,
                    "label": "Application to Trigonometric Quotient Integral",
                    "marks": "2.0 Marks",
                    "math": "I = \\int_0^{\\pi/2} \\frac{\\sqrt{\\sin x}}{\\sqrt{\\sin x} + \\sqrt{\\cos x}}dx = \\int_0^{\\pi/2} \\frac{\\sqrt{\\cos x}}{\\sqrt{\\cos x} + \\sqrt{\\sin x}}dx \\implies 2I = \\int_0^{\\pi/2} 1 dx = \\frac{\\pi}{2} \\implies I = \\frac{\\pi}{4}",
                    "explanation": "Adding both equations: numerator matches denominator exactly, reducing integral to $\\int 1 dx = \\pi/2$, giving $I = \\pi/4$."
                }
            ],
            "invariance_and_limiting_cases": "If $a = 0 \\implies \\int_0^a f(x)dx = \\int_0^a f(a-x)dx$. Tested in 302 shifts across JEE Main & CBSE.",
            "past_paper_appearances": [
                { "year": 2026, "code": "Set 65/1/1", "marks": 5 },
                { "year": 2025, "code": "Set 65/3/1", "marks": 3 },
                { "year": 2024, "code": "Set 65/2/2", "marks": 5 }
            ],
            "practice_link": "/practice/?exam=cbse&subject=Mathematics&chapter=7"
        }
    ]

    with open('data/derivations_cbse_12.json', 'w', encoding='utf-8') as f:
        json.dump(derivations, f, indent=2, ensure_ascii=False)
    print(f"Generated data/derivations_cbse_12.json with {len(derivations)} master derivations.")

if __name__ == '__main__':
    build_data()
