import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")

# -----------------------------------------------------------------------------
# 1. COMPREHENSIVE NCERT-ALIGNED TAXONOMY FOR CBSE CLASS 12 & ENTRANCE
# -----------------------------------------------------------------------------
TAXONOMY = {
  "cbse": {
    "Physics": {
      "1": [
        {
          "slug": "coulombs-law",
          "title": "Coulomb's Law and Superposition",
          "keywords": ["coulomb", "force between", "dielectric constant", "point charge", "quantization", "electrostatic force", "superposition"],
          "is_high_yield": True
        },
        {
          "slug": "electric-field-dipole",
          "title": "Electric Field and Dipole Moment",
          "keywords": ["dipole", "electric field", "axial", "equatorial", "torque on dipole", "field lines", "electric dipole moment", "dipole in uniform"],
          "is_high_yield": True
        },
        {
          "slug": "gauss-law-flux",
          "title": "Electric Flux and Gauss's Law",
          "keywords": ["gauss", "flux", "gaussian surface", "shell", "infinite wire", "plane sheet", "linear charge density", "surface charge density", "spherical shell"],
          "is_high_yield": True
        }
      ],
      "2": [
        {
          "slug": "electric-potential",
          "title": "Electric Potential and Equipotential",
          "keywords": ["potential", "equipotential", "work done", "conservative", "potential difference", "potential energy", "electrostatic potential", "potential gradient"],
          "is_high_yield": True
        },
        {
          "slug": "capacitors-dielectrics",
          "title": "Capacitance and Dielectric Slabs",
          "keywords": ["capacitor", "capacitance", "dielectric", "parallel plate", "energy stored", "dielectric slab", "capacitors in series", "capacitors in parallel", "charge on capacitor"],
          "is_high_yield": True
        }
      ],
      "3": [
        {
          "slug": "drift-velocity-ohms-law",
          "title": "Ohm's Law, Drift Velocity and Resistivity",
          "keywords": ["drift velocity", "relaxation time", "resistivity", "temperature coefficient", "ohm", "current density", "mobility", "resistance of", "nichrome", "conductivity", "v-i characteristic"],
          "is_high_yield": True
        },
        {
          "slug": "kirchhoff-wheatstone",
          "title": "Kirchhoff's Rules and Wheatstone Bridge",
          "keywords": ["kirchhoff", "wheatstone", "loop rule", "junction rule", "bridge balance", "galvanometer deflection", "meter bridge", "potentiometer"],
          "is_high_yield": True
        },
        {
          "slug": "cells-internal-resistance",
          "title": "Cells, EMF and Internal Resistance",
          "keywords": ["emf", "internal resistance", "terminal potential", "cells in parallel", "cells in series", "cell of emf", "battery"],
          "is_high_yield": True
        }
      ],
      "4": [
        {
          "slug": "biot-savart-law",
          "title": "Biot-Savart Law and Circular Coils",
          "keywords": ["biot", "savart", "circular coil", "magnetic field on axis", "circular loop", "center of the loop", "current carrying loop"],
          "is_high_yield": True
        },
        {
          "slug": "amperes-law-solenoid",
          "title": "Ampere's Circuital Law and Solenoids",
          "keywords": ["ampere", "circuital", "solenoid", "toroid", "parallel conductors", "force per unit length", "straight wire", "two parallel"],
          "is_high_yield": True
        },
        {
          "slug": "lorentz-force-galvanometer",
          "title": "Lorentz Force and Moving Coil Galvanometer",
          "keywords": ["lorentz", "galvanometer", "shunt", "voltmeter", "ammeter", "torque on loop", "magnetic force on charge", "cyclotron", "pitch of helical", "current sensitivity", "voltage sensitivity"],
          "is_high_yield": True
        }
      ],
      "5": [
        {
          "slug": "magnetic-properties",
          "title": "Dia, Para and Ferromagnetism",
          "keywords": ["diamagnetic", "paramagnetic", "ferromagnetic", "susceptibility", "permeability", "hysteresis", "magnetic material", "curie temperature"],
          "is_high_yield": True
        },
        {
          "slug": "magnetic-dipole-earth",
          "title": "Magnetic Dipole and Earth Elements",
          "keywords": ["dipole moment", "declination", "horizontal component", "angle of dip", "bar magnet", "magnetic field lines", "magnetic meridian", "earth's magnetic"],
          "is_high_yield": True
        }
      ],
      "6": [
        {
          "slug": "faraday-lenz-law",
          "title": "Faraday's and Lenz's Law",
          "keywords": ["faraday", "lenz", "induced emf", "flux linkage", "direction of induced", "motional emf", "induced current", "magnetic flux"],
          "is_high_yield": True
        },
        {
          "slug": "inductance-eddy",
          "title": "Self/Mutual Inductance and AC Generator",
          "keywords": ["inductance", "self induction", "mutual induction", "eddy currents", "ac generator", "solenoid", "coefficient of self", "coefficient of mutual"],
          "is_high_yield": True
        }
      ],
      "7": [
        {
          "slug": "ac-circuits-lcr",
          "title": "Series LCR Circuits and Resonance",
          "keywords": ["lcr", "resonance", "impedance", "phasor", "q factor", "inductive reactance", "capacitive reactance", "rms current", "peak voltage", "series circuit", "phase angle", "alternating voltage"],
          "is_high_yield": True
        },
        {
          "slug": "transformers-ac-power",
          "title": "Transformers and Power Factor",
          "keywords": ["transformer", "power factor", "wattless", "step up", "step down", "efficiency of transformer", "primary coil", "secondary coil", "core loss"],
          "is_high_yield": True
        }
      ],
      "8": [
        {
          "slug": "displacement-current-maxwell",
          "title": "Displacement Current and Maxwell's Equations",
          "keywords": ["displacement current", "maxwell", "continuity of current", "ampere-maxwell", "transverse nature"],
          "is_high_yield": True
        },
        {
          "slug": "em-waves-spectrum",
          "title": "EM Wave Spectrum and Applications",
          "keywords": ["spectrum", "microwaves", "x rays", "x-rays", "gamma", "ultraviolet", "infrared", "radio waves", "wavelength range", "electromagnetic wave", "frequency"],
          "is_high_yield": True
        }
      ],
      "9": [
        {
          "slug": "reflection-refraction",
          "title": "Reflection, Refraction and TIR",
          "keywords": ["refraction", "reflection", "snell", "total internal reflection", "optical fibre", "critical angle", "spherical mirror", "focal length of mirror"],
          "is_high_yield": True
        },
        {
          "slug": "lens-makers-formula",
          "title": "Lens Maker's Formula and Combinations",
          "keywords": ["lens maker", "refraction at spherical", "focal length", "combination of lenses", "power of lens", "convex lens", "concave lens"],
          "is_high_yield": True
        },
        {
          "slug": "prism-refraction",
          "title": "Prism Deviation and Refractive Index",
          "keywords": ["prism", "minimum deviation", "angle of prism", "refractive index of material", "dispersion"],
          "is_high_yield": True
        },
        {
          "slug": "microscope-telescope",
          "title": "Compound Microscope and Astronomical Telescope",
          "keywords": ["microscope", "telescope", "magnifying power", "normal adjustment", "objective lens", "eyepiece", "astronomical telescope", "reflecting telescope"],
          "is_high_yield": True
        }
      ],
      "10": [
        {
          "slug": "huygens-principle",
          "title": "Huygens Principle and Wavefronts",
          "keywords": ["huygens", "wavefront", "laws of reflection", "laws of refraction", "wave front", "secondary wavelets"],
          "is_high_yield": True
        },
        {
          "slug": "youngs-double-slit",
          "title": "Young's Double Slit and Diffraction",
          "keywords": ["interference", "young", "fringe width", "diffraction", "central maximum", "single slit", "coherent sources", "angular width", "constructive interference", "destructive interference"],
          "is_high_yield": True
        }
      ],
      "11": [
        {
          "slug": "photoelectric-effect",
          "title": "Photoelectric Effect and Einstein's Equation",
          "keywords": ["photoelectric", "stopping potential", "work function", "threshold frequency", "einstein's photoelectric", "cut-off voltage", "photoelectrons", "photon"],
          "is_high_yield": True
        },
        {
          "slug": "de-broglie-wavelength",
          "title": "De Broglie Wavelength and Matter Waves",
          "keywords": ["de broglie", "wavelength of electron", "matter wave", "davisson", "accelerating potential", "momentum of photon"],
          "is_high_yield": True
        }
      ],
      "12": [
        {
          "slug": "alpha-scattering-rutherford",
          "title": "Rutherford Alpha Scattering and Nuclear Size",
          "keywords": ["rutherford", "alpha particle", "geiger-marsden", "closest approach", "impact parameter", "gold foil"],
          "is_high_yield": True
        },
        {
          "slug": "bohr-model-hydrogen",
          "title": "Bohr Postulates and Hydrogen Spectra",
          "keywords": ["bohr", "radius of orbit", "energy levels", "lyman", "balmer", "paschen", "brackett", "pfund", "ground state", "excitation energy", "spectral series", "hydrogen atom"],
          "is_high_yield": True
        }
      ],
      "13": [
        {
          "slug": "binding-energy-fission",
          "title": "Mass Defect, Binding Energy and Fission",
          "keywords": ["mass defect", "binding energy", "fission", "fusion", "nuclear density", "nuclear force", "atomic mass unit", "q-value", "radioactivity", "half-life", "decay"],
          "is_high_yield": True
        }
      ],
      "14": [
        {
          "slug": "pn-junction-diode",
          "title": "p-n Junction and V-I Characteristics",
          "keywords": ["pn junction", "depletion layer", "barrier potential", "forward bias", "reverse bias", "p-n junction", "diode", "threshold voltage", "dynamic resistance"],
          "is_high_yield": True
        },
        {
          "slug": "rectifiers-semiconductors",
          "title": "Half/Full Wave Rectifiers and Energy Bands",
          "keywords": ["rectifier", "half wave", "full wave", "intrinsic", "extrinsic", "doping", "energy band", "valence band", "conduction band", "n-type", "p-type", "semiconductor", "zener", "led", "photodiode", "solar cell"],
          "is_high_yield": True
        }
      ]
    },
    "Chemistry": {
      "1": [
        {
          "slug": "raoults-law-ideal",
          "title": "Raoult's Law and Ideal Solutions",
          "keywords": ["raoult", "ideal solution", "azeotrope", "negative deviation", "positive deviation", "vapor pressure", "vapour pressure", "henry"],
          "is_high_yield": True
        },
        {
          "slug": "colligative-properties",
          "title": "Colligative Properties and Van't Hoff",
          "keywords": ["colligative", "freezing", "boiling", "osmotic", "van't hoff", "molarity", "molality", "mole fraction", "depression", "elevation"],
          "is_high_yield": True
        }
      ],
      "2": [
        {
          "slug": "nernst-equation",
          "title": "Nernst Equation and Cell Potential",
          "keywords": ["nernst", "cell potential", "emf of cell", "standard hydrogen", "electrode potential", "galvanic cell", "gibbs energy"],
          "is_high_yield": True
        },
        {
          "slug": "kohlrausch-conductance",
          "title": "Kohlrausch's Law and Molar Conductivity",
          "keywords": ["kohlrausch", "molar conductivity", "limiting molar", "conductance", "conductivity", "degree of dissociation", "cell constant"],
          "is_high_yield": True
        },
        {
          "slug": "batteries-corrosion",
          "title": "Batteries, Fuel Cells and Corrosion",
          "keywords": ["battery", "fuel cell", "lead storage", "corrosion", "rusting", "electrolysis", "faraday's law", "primary battery", "secondary battery"],
          "is_high_yield": True
        }
      ],
      "3": [
        {
          "slug": "order-rate-law",
          "title": "Rate Laws, Order and Molecularity",
          "keywords": ["order of reaction", "molecularity", "rate constant", "rate law", "rate of reaction", "rate expression"],
          "is_high_yield": True
        },
        {
          "slug": "integrated-rate-equations",
          "title": "Integrated Rate Equations and Half-Life",
          "keywords": ["integrated rate", "half life", "half-life", "first order", "zero order", "pseudo first order"],
          "is_high_yield": True
        },
        {
          "slug": "arrhenius-activation",
          "title": "Arrhenius Equation and Activation Energy",
          "keywords": ["arrhenius", "activation energy", "collision frequency", "collision theory", "catalyst", "temperature dependence"],
          "is_high_yield": True
        }
      ],
      "4": [
        {
          "slug": "d-block-properties",
          "title": "d-Block General Properties and Trends",
          "keywords": ["transition metal", "oxidation state", "ionization enthalpy", "magnetic behavior", "colored ion", "catalytic property", "interstitial compound", "alloy", "electronic configuration"],
          "is_high_yield": True
        },
        {
          "slug": "lanthanoid-contraction",
          "title": "Lanthanoid Contraction and Consequences",
          "keywords": ["lanthanoid", "actinoid", "contraction", "atomic radii", "lanthanide", "actinide"],
          "is_high_yield": True
        },
        {
          "slug": "kmno4-k2cr2o7",
          "title": "Potassium Dichromate and Permanganate",
          "keywords": ["dichromate", "permanganate", "kmno4", "k2cr2o7", "oxidizing agent", "chromate", "manganate"],
          "is_high_yield": True
        }
      ],
      "5": [
        {
          "slug": "iupac-coordination",
          "title": "IUPAC Nomenclature and Formulas",
          "keywords": ["iupac", "nomenclature", "formula of complex", "coordination sphere", "ligand", "coordination number", "dentate", "chelate", "werner"],
          "is_high_yield": True
        },
        {
          "slug": "isomerism-complexes",
          "title": "Isomerism in Coordination Complexes",
          "keywords": ["isomerism", "geometrical", "optical", "linkage", "coordination isomerism", "cis", "trans", "fac", "mer"],
          "is_high_yield": True
        },
        {
          "slug": "vbt-cft-theories",
          "title": "Valence Bond and Crystal Field Theory (CFT)",
          "keywords": ["crystal field", "crystal field splitting", "valence bond", "cfse", "hybridisation", "magnetic moment", "spectrochemical series", "octahedral", "tetrahedral", "high spin", "low spin"],
          "is_high_yield": True
        }
      ],
      "6": [
        {
          "slug": "sn1-sn2-mechanisms",
          "title": "SN1 and SN2 Reaction Mechanisms",
          "keywords": ["sn1", "sn2", "nucleophilic substitution", "carbocation", "inversion of configuration", "racemisation", "chirality", "haloalkane", "alkyl halide"],
          "is_high_yield": True
        },
        {
          "slug": "haloarenes-reactions",
          "title": "Haloarenes and Electrophilic Substitution",
          "keywords": ["chlorobenzene", "electrophilic substitution", "friedel crafts", "wurtz fittig", "haloarene", "resonance in chlorobenzene", "grignard"],
          "is_high_yield": True
        }
      ],
      "7": [
        {
          "slug": "acidity-phenols-prep",
          "title": "Phenols: Acidity and Electrophilic Reactions",
          "keywords": ["phenol", "acidity of phenol", "kolbe", "reimer tiemann", "picric acid", "salicylic acid", "bromine water test"],
          "is_high_yield": True
        },
        {
          "slug": "alcohols-dehydration",
          "title": "Alcohols: Lucas Test and Dehydration",
          "keywords": ["alcohol", "lucas", "dehydration", "primary secondary tertiary", "fermentation", "hydroboration", "esterification"],
          "is_high_yield": True
        },
        {
          "slug": "williamson-ethers",
          "title": "Williamson Synthesis of Ethers",
          "keywords": ["ether", "williamson", "cleavage of c-o", "ethoxyethane", "anisole", "hi reaction"],
          "is_high_yield": True
        }
      ],
      "8": [
        {
          "slug": "nucleophilic-addition-co",
          "title": "Nucleophilic Addition to Carbonyls",
          "keywords": ["nucleophilic addition", "hcn", "nahso3", "grignard", "hydrazone", "oxime", "semicarbazide", "carbonyl group", "aldehyde", "ketone"],
          "is_high_yield": True
        },
        {
          "slug": "aldol-cannizzaro",
          "title": "Aldol Condensation and Cannizzaro Reaction",
          "keywords": ["aldol", "cannizzaro", "cross aldol", "alpha hydrogen", "fehling", "tollens", "haloform", "iodoform test"],
          "is_high_yield": True
        },
        {
          "slug": "carboxylic-acids-reactions",
          "title": "Carboxylic Acids Acidity and Reactions",
          "keywords": ["carboxylic", "acidity of benzoic", "hell volhard", "decarboxylation", "hvz", "benzoic acid", "esterification", "acetic acid"],
          "is_high_yield": True
        }
      ],
      "9": [
        {
          "slug": "basicity-amines-hoffmann",
          "title": "Basicity of Amines and Hoffmann Bromamide",
          "keywords": ["basicity of amines", "hoffmann bromamide", "gabriel phthalimide", "carbylamine", "amine", "hinsberg test", "aniline"],
          "is_high_yield": True
        },
        {
          "slug": "diazonium-sandmeyer",
          "title": "Diazonium Salts and Sandmeyer Reaction",
          "keywords": ["diazonium", "sandmeyer", "gattermann", "azo dye", "coupling reaction", "benzenediazonium"],
          "is_high_yield": True
        }
      ],
      "10": [
        {
          "slug": "carbohydrates-glucose",
          "title": "Glucose, Fructose and Glycosidic Linkage",
          "keywords": ["glucose", "fructose", "glycosidic", "reducing sugar", "mutarotation", "carbohydrate", "starch", "cellulose", "glycogen", "haworth"],
          "is_high_yield": True
        },
        {
          "slug": "proteins-nucleic-acids",
          "title": "Peptide Bond, Denaturation and DNA/RNA",
          "keywords": ["peptide bond", "denaturation", "nucleic acid", "dna", "rna", "structure of protein", "amino acid", "essential amino", "vitamin", "enzyme", "double helix"],
          "is_high_yield": True
        }
      ]
    },
    "Mathematics": {
      "1": [
        {
          "slug": "equivalence-relations",
          "title": "Reflexive, Symmetric and Transitive Relations",
          "keywords": ["equivalence relation", "reflexive", "symmetric", "transitive", "relation r", "equivalence class"],
          "is_high_yield": True
        },
        {
          "slug": "one-one-onto-functions",
          "title": "Bijective, Injective and Surjective Functions",
          "keywords": ["one-one", "onto", "injective", "surjective", "bijective", "function f", "domain and codomain", "composite function"],
          "is_high_yield": True
        }
      ],
      "2": [
        {
          "slug": "principal-values-itf",
          "title": "Principal Values and Domain of ITF",
          "keywords": ["principal value", "sin^-1", "cos^-1", "tan^-1", "sec^-1", "cosec^-1", "cot^-1", "domain and range", "inverse trigonometric"],
          "is_high_yield": True
        }
      ],
      "3": [
        {
          "slug": "matrix-multiplication-transpose",
          "title": "Matrix Multiplication, Transpose and Symmetric",
          "keywords": ["multiplication of matrices", "transpose", "symmetric", "skew-symmetric", "skew symmetric", "matrix a", "order of matrix", "matrices"],
          "is_high_yield": True
        },
        {
          "slug": "inverse-elementary",
          "title": "Invertible Matrices and Elementary Operations",
          "keywords": ["invertible", "elementary row", "inverse of matrix", "identity matrix", "a^-1"],
          "is_high_yield": True
        }
      ],
      "4": [
        {
          "slug": "adjoint-inverse-system",
          "title": "Adjoint, Inverse and System of Linear Equations",
          "keywords": ["adjoint", "matrix method", "system of equations", "cramer", "unique solution", "consistent", "solve the system", "adj a"],
          "is_high_yield": True
        },
        {
          "slug": "determinant-expansion",
          "title": "Determinant Value and Minors/Cofactors",
          "keywords": ["determinant", "cofactor", "minor", "singular matrix", "value of determinant", "|a|", "determinant of order"],
          "is_high_yield": True
        }
      ],
      "5": [
        {
          "slug": "continuity-differentiation",
          "title": "Continuity and Chain Rule",
          "keywords": ["continuous", "discontinuity", "chain rule", "differentiable", "differentiability", "continuity at x", "derivative of"],
          "is_high_yield": True
        },
        {
          "slug": "logarithmic-implicit-diff",
          "title": "Logarithmic and Implicit Differentiation",
          "keywords": ["logarithmic differentiation", "implicit", "parametric", "dy/dx", "log x", "differentiate with respect to"],
          "is_high_yield": True
        },
        {
          "slug": "second-order-derivatives",
          "title": "Second Order Derivative Proofs",
          "keywords": ["d^2y/dx^2", "second order", "prove that", "show that", "second derivative"],
          "is_high_yield": True
        }
      ],
      "6": [
        {
          "slug": "increasing-decreasing",
          "title": "Increasing and Decreasing Functions",
          "keywords": ["strictly increasing", "decreasing", "intervals in which", "rate of change", "increasing or decreasing"],
          "is_high_yield": True
        },
        {
          "slug": "maxima-minima-problems",
          "title": "Maxima and Minima Word Problems",
          "keywords": ["maxima", "minima", "maximum volume", "minimum cost", "largest box", "maximum area", "local maxima", "critical points"],
          "is_high_yield": True
        }
      ],
      "7": [
        {
          "slug": "integration-by-parts-substitution",
          "title": "Integration by Parts and Substitution",
          "keywords": ["by parts", "substitution", "e^x", "partial fractions", "evaluate", "integrate", "dx", "indefinite integral"],
          "is_high_yield": True
        },
        {
          "slug": "definite-integrals-properties",
          "title": "Definite Integrals and Kings Property",
          "keywords": ["definite integral", "properties of definite", "fundamental theorem", "int_0^", "limits of integration"],
          "is_high_yield": True
        }
      ],
      "8": [
        {
          "slug": "area-bounded-curves",
          "title": "Area Bounded by Parabolas, Circles and Lines",
          "keywords": ["area of region", "bounded by", "parabola", "ellipse", "circle and line", "area enclosed", "sketch the region"],
          "is_high_yield": True
        }
      ],
      "9": [
        {
          "slug": "linear-differential-eq",
          "title": "Linear Differential Equations and IF",
          "keywords": ["integrating factor", "dy/dx + py", "linear differential", "i.f.", "first order differential"],
          "is_high_yield": True
        },
        {
          "slug": "separable-homogeneous",
          "title": "Variable Separable and Homogeneous Equations",
          "keywords": ["homogeneous", "variable separable", "general solution", "particular solution", "order and degree", "differential equation"],
          "is_high_yield": True
        }
      ],
      "10": [
        {
          "slug": "dot-cross-products",
          "title": "Scalar (Dot) and Vector (Cross) Product",
          "keywords": ["dot product", "cross product", "perpendicular vectors", "projection of vector", "angle between vectors", "scalar product", "vector product"],
          "is_high_yield": True
        },
        {
          "slug": "unit-vectors-coplanar",
          "title": "Unit Vectors and Collinearity",
          "keywords": ["unit vector", "collinear", "direction cosines", "magnitude of vector", "coplanar", "position vector"],
          "is_high_yield": True
        }
      ],
      "11": [
        {
          "slug": "shortest-distance-lines",
          "title": "Shortest Distance between Skew Lines",
          "keywords": ["shortest distance", "skew lines", "parallel lines", "vector equation of line", "distance between"],
          "is_high_yield": True
        },
        {
          "slug": "equations-of-line",
          "title": "Cartesian and Vector Equations of Lines",
          "keywords": ["cartesian equation", "direction ratios", "point of intersection", "equation of line", "angle between lines", "coplanar lines"],
          "is_high_yield": True
        }
      ],
      "12": [
        {
          "slug": "lpp-graphical-method",
          "title": "Linear Programming Graphical Solutions",
          "keywords": ["linear programming", "lpp", "corner points", "maximize", "minimize", "feasible region", "objective function", "constraints"],
          "is_high_yield": True
        }
      ],
      "13": [
        {
          "slug": "bayes-theorem",
          "title": "Bayes' Theorem and Total Probability",
          "keywords": ["bayes", "total probability", "conditional probability", "defective items", "urn", "bag contains"],
          "is_high_yield": True
        },
        {
          "slug": "independent-events",
          "title": "Independent Events and Probability Distribution",
          "keywords": ["independent events", "p(a|b)", "multiplication theorem", "random variable", "probability distribution", "mean of"],
          "is_high_yield": True
        }
      ]
    }
  },
  "neet": {
    "Physics": [
      { "slug": "mechanics-kinematics", "title": "Mechanics, Work, Energy & Rotational Dynamics", "keywords": ["motion", "velocity", "acceleration", "friction", "torque", "moment of inertia", "gravity", "gravitation", "work", "kinetic energy", "momentum"], "is_high_yield": True },
      { "slug": "thermal-oscillations-waves", "title": "Thermal Physics, Oscillations & Waves", "keywords": ["temperature", "heat", "thermodynamics", "carnot", "shm", "simple harmonic", "pendulum", "wave", "doppler", "sound", "viscosity"], "is_high_yield": True },
      { "slug": "electrodynamics-circuits", "title": "Electrostatics, Current & Magnetism", "keywords": ["electric", "current", "resistor", "magnetic", "capacitance", "inductance", "flux", "field", "potential", "charge", "emf"], "is_high_yield": True },
      { "slug": "optics-modern-physics", "title": "Ray Optics, Wave Optics & Modern Physics", "keywords": ["lens", "refraction", "reflection", "interference", "photoelectric", "wavelength", "bohr", "nucleus", "semiconductor", "diode", "atom"], "is_high_yield": True }
    ],
    "Chemistry": [
      { "slug": "physical-equilibrium-kinetics", "title": "Physical Chemistry: Equilibrium, Kinetics & Electrochemistry", "keywords": ["equilibrium", "ph", "kp", "nernst", "rate constant", "activation energy", "half life", "thermodynamics", "entropy", "solution", "colligative", "mole"], "is_high_yield": True },
      { "slug": "inorganic-bonding-periodic", "title": "Inorganic: Chemical Bonding, Periodic Trends & Coordination", "keywords": ["hybridisation", "dipole", "geometry", "vsepr", "bond order", "paramagnetic", "coordination", "ligand", "d-block", "p-block", "oxidation state"], "is_high_yield": True },
      { "slug": "organic-mechanisms-hydrocarbons", "title": "Organic: Reaction Mechanisms & Hydrocarbons", "keywords": ["nucleophilic", "electrophilic", "carbocation", "alkane", "alkene", "alkyne", "aromatic", "sn1", "sn2", "stereochemistry"], "is_high_yield": True },
      { "slug": "organic-functional-biomolecules", "title": "Organic: Functional Groups, Amines & Biomolecules", "keywords": ["alcohol", "phenol", "ether", "aldehyde", "ketone", "carboxylic", "amine", "diazonium", "glucose", "amino acid", "protein", "dna", "polymer"], "is_high_yield": True }
    ],
    "Botany": [
      { "slug": "plant-genetics-molecular", "title": "Genetics & Molecular Biology", "keywords": ["mendel", "dihybrid", "chromosome", "dna", "transcription", "translation", "allele", "gene", "mutation", "rna"], "is_high_yield": True },
      { "slug": "plant-physiology-cellular", "title": "Plant Physiology & Cell Biology", "keywords": ["photosynthesis", "c3", "c4", "calvin", "krebs", "atp", "chloroplast", "transpiration", "mitosis", "meiosis", "membrane", "cell wall"], "is_high_yield": True },
      { "slug": "morphology-reproduction-flowering", "title": "Plant Morphology & Sexual Reproduction", "keywords": ["flower", "ovule", "pollen", "pollination", "embryo", "endosperm", "seed", "fruit", "root", "stem"], "is_high_yield": True },
      { "slug": "ecology-environment", "title": "Ecology & Biodiversity", "keywords": ["ecosystem", "trophic", "pyramid", "biodiversity", "pollution", "population", "succession", "conservation"], "is_high_yield": True }
    ],
    "Zoology": [
      { "slug": "human-physiology-systems", "title": "Human Physiology & Organ Systems", "keywords": ["blood", "cardiac", "nephron", "kidney", "lungs", "neural", "hormone", "endocrine", "digestion", "circulation", "excretion"], "is_high_yield": True },
      { "slug": "human-reproduction-development", "title": "Human Reproduction & Reproductive Health", "keywords": ["spermatogenesis", "oogenesis", "ovary", "testis", "menstrual", "contraceptive", "art", "fertilization", "pregnancy", "embryo"], "is_high_yield": True },
      { "slug": "animal-classification-evolution", "title": "Animal Diversity & Evolution", "keywords": ["homologous", "analogous", "natural selection", "phylum", "chordata", "arthropoda", "darwin", "hardy weinberg", "fossil"], "is_high_yield": True },
      { "slug": "biotechnology-human-health", "title": "Biotechnology & Human Health/Disease", "keywords": ["plasmid", "restriction enzyme", "pcr", "recombinant", "antibody", "antigen", "immunity", "aids", "cancer", "vaccine"], "is_high_yield": True }
    ]
  }
}

def classify_text(text, topics_list, fallback_title, fallback_slug):
    """Matches text against topic keywords and returns (title, slug)."""
    if not text:
        return fallback_title, fallback_slug
    
    clean = text.lower()
    best_t = None
    best_score = 0
    
    for t in topics_list:
        score = 0
        for kw in t.get("keywords", []):
            kw_l = kw.lower()
            if kw_l in clean:
                # Multi-word keywords get higher specificity points
                score += 3 if " " in kw_l else 1
        if score > best_score:
            best_score = score
            best_t = t
            
    if best_t and best_score > 0:
        return best_t["title"], best_t["slug"]
    return fallback_title, fallback_slug

def process_cbse():
    print("--- Classifying CBSE Class 12 Datasets ---")
    files = {
        "Physics": os.path.join(DATA_DIR, "cbse_physics.json"),
        "Chemistry": os.path.join(DATA_DIR, "cbse_chemistry.json"),
        "Mathematics": os.path.join(DATA_DIR, "cbse_mathematics.json")
    }
    
    cbse_taxonomy = TAXONOMY["cbse"]
    total_tagged = 0
    
    for subj, fpath in files.items():
        if not os.path.exists(fpath):
            print(f"[SKIP] {fpath} not found")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            questions = json.load(f)
            
        subj_topics = cbse_taxonomy.get(subj, {})
        tagged_in_file = 0
        
        for q in questions:
            ch_num = str(q.get("chapter_number", "1"))
            ch_name = q.get("chapter_name", f"Chapter {ch_num}")
            ch_topics = subj_topics.get(ch_num, [])
            
            # Default fallback topic for chapter
            fb_title = f"{ch_name} (Core Concepts & Numericals)"
            fb_slug = re.sub(r'[^a-z0-9]+', '-', ch_name.lower()).strip('-') + "-core"
            
            q_text = (q.get("text", "") + " " + q.get("signature", "")).strip()
            
            if ch_topics:
                sub_title, sub_slug = classify_text(q_text, ch_topics, ch_topics[0]["title"], ch_topics[0]["slug"])
            else:
                sub_title, sub_slug = fb_title, fb_slug
                
            q["subtopic"] = sub_title
            q["subtopic_slug"] = sub_slug
            tagged_in_file += 1
            
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
            
        print(f"  [OK] {subj}: Tagged 100% ({tagged_in_file}/{len(questions)} questions) -> {fpath}")
        total_tagged += tagged_in_file
        
    return total_tagged

def process_repeats():
    print("\n--- Classifying Repeated Questions Vault ---")
    fpath = os.path.join(DATA_DIR, "repeated_questions.json")
    if not os.path.exists(fpath):
        return 0
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    cbse_repeats = data.get("cbse_repeats", [])
    cbse_taxonomy = TAXONOMY["cbse"]
    tagged = 0
    
    for q in cbse_repeats:
        subj = q.get("subject", "Physics")
        ch_num = str(q.get("chapter_number", "1"))
        ch_name = q.get("chapter_name", f"Chapter {ch_num}")
        ch_topics = cbse_taxonomy.get(subj, {}).get(ch_num, [])
        
        fb_title = f"{ch_name} (High-Yield Core)"
        fb_slug = re.sub(r'[^a-z0-9]+', '-', ch_name.lower()).strip('-') + "-core"
        
        q_text = q.get("text", "")
        if ch_topics:
            sub_title, sub_slug = classify_text(q_text, ch_topics, ch_topics[0]["title"], ch_topics[0]["slug"])
        else:
            sub_title, sub_slug = fb_title, fb_slug
            
        q["subtopic"] = sub_title
        q["subtopic_slug"] = sub_slug
        tagged += 1
        
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Repeated Questions: Tagged 100% ({tagged} repeat clusters)")
    return tagged

def process_neet():
    print("\n--- Classifying NEET UG Dataset ---")
    fpath = os.path.join(DATA_DIR, "neet_all.json")
    if not os.path.exists(fpath):
        return 0
    with open(fpath, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    neet_tax = TAXONOMY.get("neet", {})
    tagged = 0
    
    for q in questions:
        subj = q.get("subject", "Physics")
        topics = neet_tax.get(subj, [])
        fb_title = f"{subj} Core Concepts"
        fb_slug = f"{subj.lower()}-core"
        
        txt = q.get("text", "") + " " + q.get("concept_name", "")
        if topics:
            sub_title, sub_slug = classify_text(txt, topics, topics[0]["title"], topics[0]["slug"])
        else:
            sub_title, sub_slug = fb_title, fb_slug
            
        q["subtopic"] = sub_title
        q["subtopic_slug"] = sub_slug
        tagged += 1
        
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"  [OK] NEET UG: Tagged 100% ({tagged} questions)")
    return tagged

def process_jee():
    print("\n--- Classifying JEE Main Dataset ---")
    fpath = os.path.join(DATA_DIR, "jee_main_all.json")
    if not os.path.exists(fpath):
        return 0
    with open(fpath, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    tagged = 0
    for q in questions:
        ch = q.get("ncert_chapter", "General")
        subj = q.get("subject", "Physics")
        
        slug = re.sub(r'[^a-z0-9]+', '-', ch.lower()).strip('-')
        q["subtopic"] = ch
        q["subtopic_slug"] = slug
        tagged += 1
        
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"  [OK] JEE Main: Tagged 100% ({tagged} questions)")
    return tagged

def main():
    # Save updated taxonomy into data/chapter_topics.json
    topics_file = os.path.join(DATA_DIR, "chapter_topics.json")
    with open(topics_file, "w", encoding="utf-8") as f:
        json.dump(TAXONOMY, f, indent=2, ensure_ascii=False)
    print(f"[OK] Saved comprehensive taxonomy to {topics_file}")
    
    cbse_count = process_cbse()
    rep_count = process_repeats()
    neet_count = process_neet()
    jee_count = process_jee()
    
    print("\n=======================================================")
    print(f"SUBTOPIC TAGGING COMPLETE: {cbse_count + rep_count + neet_count + jee_count} TOTAL QUESTIONS TAGGED")
    print("=======================================================")

if __name__ == "__main__":
    main()
