import json
import os
import re

ROOT_DIR = r"E:\PYQ_Wovrix_Portal\pyq-wovrix"
DATA_DIR = os.path.join(ROOT_DIR, "data")
COMPETITIVE_JSON = r"E:\PYQ_Wovrix_Portal\competitive-exams-portal\database\competitive_syllabus_master.json"

# 1. Load competitive master data
with open(COMPETITIVE_JSON, "r", encoding="utf-8") as f:
    comp_master = json.load(f)

# 2. Build syllabus_entrance.json
with open(os.path.join(DATA_DIR, "syllabus_entrance.json"), "r", encoding="utf-8") as f:
    entrance_data = json.load(f)

# Update NEET UG
neet_items = [x for x in comp_master if x.get("exam_name") == "NEET UG"]
neet_subjects = {
    "Physics": [x for x in neet_items if x.get("subject") == "Physics"],
    "Chemistry": [x for x in neet_items if x.get("subject") == "Chemistry"],
    "Biology (Botany)": [x for x in neet_items if x.get("subject") == "Biology (Botany)"],
    "Biology (Zoology)": [x for x in neet_items if x.get("subject") == "Biology (Zoology)"],
}

entrance_data["neet"] = {
    "title": "NEET UG Official Syllabus & Statutory Chapter Weightage Blueprint",
    "conducting_body": "National Medical Commission (NMC) & National Testing Agency (NTA)",
    "total_questions": 200,
    "questions_to_attempt": 180,
    "total_marks": 720,
    "duration_minutes": 200,
    "scoring": "+4 for correct, -1 for incorrect, 0 for unattempted",
    "pdf_url": "/curriculum_pdf/NEET_UG_Official_Curriculum_and_Weightage.pdf",
    "pdf_name": "NEET_UG_Official_Curriculum_and_Weightage.pdf",
    "pdf_size": "19 KB",
    "official_citation": "Under Graduate Medical Education Board (UGMEB) Syllabus Notification, NMC / NTA",
    "subjects": {}
}

for subj, items in neet_subjects.items():
    unit_list = []
    for item in items:
        unit_list.append({
            "chapter": item.get("chapter"),
            "unit_name": item.get("unit_name"),
            "unit_no": item.get("unit_no"),
            "class_level": item.get("class_level"),
            "official_status": item.get("official_status"),
            "question_count_avg": item.get("question_count_avg"),
            "mark_weightage_range": item.get("mark_weightage_range"),
            "priority_tier": item.get("priority_tier"),
            "official_topics": item.get("official_topics"),
            "concept_archetype_sample": item.get("concept_archetype_sample"),
            "id": item.get("id"),
            # Legacy compatibility fields for existing UI helpers
            "name": item.get("chapter"),
            "marks": item.get("mark_weightage_range"),
            "avg_qs": item.get("question_count_avg"),
            "yield_tier": item.get("priority_tier"),
            "top_topics": item.get("concept_archetype_sample")
        })
    entrance_data["neet"]["subjects"][subj] = unit_list

# Update JEE Main
jee_items = [x for x in comp_master if x.get("exam_name") == "JEE Main"]
jee_subjects = {
    "Physics": [x for x in jee_items if x.get("subject") == "Physics"],
    "Chemistry": [x for x in jee_items if x.get("subject") == "Chemistry"],
    "Mathematics": [x for x in jee_items if x.get("subject") == "Mathematics"]
}

entrance_data["jee_main"] = {
    "title": "JEE Main Official Syllabus & Empirical 186-Shift Frequency Blueprint",
    "conducting_body": "National Testing Agency (NTA)",
    "total_questions": 90,
    "questions_to_attempt": 75,
    "total_marks": 300,
    "duration_minutes": 180,
    "scoring": "+4 for correct, -1 for incorrect (both MCQs & NVQs)",
    "pdf_url": "/curriculum_pdf/JEE_Main_Official_Curriculum_and_Weightage.pdf",
    "pdf_name": "JEE_Main_Official_Curriculum_and_Weightage.pdf",
    "pdf_size": "32 KB",
    "official_citation": "NTA JEE (Main) Information Bulletin & 186 Computer-Based Test Shifts Archive",
    "subjects": {}
}

for subj, items in jee_subjects.items():
    unit_list = []
    for item in items:
        unit_list.append({
            "chapter": item.get("chapter"),
            "unit_name": item.get("unit_name"),
            "unit_no": item.get("unit_no"),
            "class_level": item.get("class_level"),
            "official_status": item.get("official_status"),
            "question_count_avg": item.get("question_count_avg"),
            "mark_weightage_range": item.get("mark_weightage_range"),
            "priority_tier": item.get("priority_tier"),
            "official_topics": item.get("official_topics"),
            "concept_archetype_sample": item.get("concept_archetype_sample"),
            "id": item.get("id"),
            # Legacy compatibility fields
            "name": item.get("chapter"),
            "shift_appearances": item.get("mark_weightage_range"),
            "avg_qs": item.get("question_count_avg"),
            "yield_tier": item.get("priority_tier"),
            "top_topics": item.get("concept_archetype_sample")
        })
    entrance_data["jee_main"]["subjects"][subj] = unit_list

with open(os.path.join(DATA_DIR, "syllabus_entrance.json"), "w", encoding="utf-8") as f:
    json.dump(entrance_data, f, indent=2, ensure_ascii=False)
print("Updated syllabus_entrance.json with 41 NEET and 54 JEE units.")

# 3. Update syllabus_cbse_12.json
with open(os.path.join(DATA_DIR, "syllabus_cbse_12.json"), "r", encoding="utf-8") as f:
    cbse12_data = json.load(f)

# Define official topics and PDFs for CBSE 12
cbse12_pdfs = {
    "Physics": ("/curriculum_pdf/Class12_Physics.pdf", "Class12_Physics.pdf", "189 KB"),
    "Chemistry": ("/curriculum_pdf/Class12_Chemistry.pdf", "Class12_Chemistry.pdf", "931 KB"),
    "Mathematics": ("/curriculum_pdf/Class12_Maths.pdf", "Class12_Maths.pdf", "694 KB"),
    "Biology": ("/curriculum_pdf/Class12_Biology.pdf", "Class12_Biology.pdf", "398 KB"),
    "Computer Science": ("/curriculum_pdf/Class12_Computer_Science.pdf", "Class12_Computer_Science.pdf", "459 KB"),
    "English Core": ("/curriculum_pdf/Class12_English_Core.pdf", "Class12_English_Core.pdf", "854 KB")
}

cbse12_topics_map = {
    # Chemistry
    "Solutions": "Types of solutions, concentration expressions of solids in liquids, solubility of gases in liquids (Henry's law), solid solutions, Raoult's law, colligative properties (relative lowering of VP, elevation of BP, depression of FP, osmotic pressure), determination of molecular mass, abnormal molecular mass, Van't Hoff factor.",
    "Electrochemistry": "Redox reactions, EMF of a cell, standard electrode potential, Nernst equation and applications to chemical cells, relation between Gibbs energy and EMF, conductance in electrolytic solutions, specific and molar conductivity, variations with concentration, Kohlrausch's Law, electrolysis laws, dry cells, Galvanic cells, lead accumulator, fuel cells, corrosion.",
    "Chemical Kinetics": "Rate of reaction (average and instantaneous), factors affecting rate (concentration, temperature, catalyst), order and molecularity, rate law and specific rate constant, integrated rate equations and half-life (zero and first order only), collision theory (elementary qualitative), activation energy, Arrhenius equation.",
    "d- and f-Block Elements": "Electronic configuration, occurrence, characteristics of transition metals, general trends in first row (metallic character, ionization enthalpy, oxidation states, ionic radii, colour, catalytic properties, magnetic properties, interstitial compounds, alloy formation). Preparation and properties of K2Cr2O7 and KMnO4. Lanthanoids (electronic config, oxidation states, lanthanoid contraction consequences). Actinoids comparison.",
    "Coordination Compounds": "Ligands, coordination number, colour, magnetic properties and shapes, IUPAC nomenclature of mononuclear complexes. Bonding: Werner's theory, VBT, and CFT; structure and stereoisomerism, importance in qualitative analysis, extraction of metals and biological systems.",
    "Haloalkanes and Haloarenes": "Haloalkanes: Nomenclature, nature of C-X bond, physical and chemical properties, optical rotation mechanism (SN1 and SN2). Haloarenes: Nature of C-X bond, substitution reactions (directive influence in monosubstituted). Uses/environmental effects of dichloromethane, chloroform, iodoform, freons, DDT.",
    "Alcohols, Phenols and Ethers": "Alcohols: Nomenclature, preparation, properties of primary alcohols, test for 1°, 2°, 3°, dehydration mechanism, uses of methanol/ethanol. Phenols: Preparation, properties, acidic nature, electrophilic substitution, Kolbe, Reimer-Tiemann, uses. Ethers: Nomenclature, preparation, physical/chemical properties, Williamson synthesis.",
    "Aldehydes, Ketones and Carboxylic Acids": "Aldehydes and Ketones: Nomenclature, carbonyl nature, preparation, properties, nucleophilic addition mechanism, alpha-hydrogen reactivity, uses. Carboxylic Acids: Nomenclature, acidic nature, preparation, properties, HVZ reaction, uses.",
    "Amines": "Nomenclature, classification, structure, preparation, properties, identification of 1°, 2°, 3° amines. Diazonium salts: Preparation, chemical reactions and synthetic importance.",
    "Biomolecules": "Carbohydrates (aldoses/ketoses, monosaccharides: glucose/fructose, D-L config, oligosaccharides, polysaccharides: starch, cellulose, glycogen). Proteins (amino acids, peptide bond, primary/secondary/tertiary/quaternary structure qualitative, denaturation, enzymes). Hormones, Vitamins (classification), Nucleic Acids (DNA & RNA).",

    # Physics
    "Electric Charges and Fields": "Electric charges and conservation, Coulomb's law force between two point charges, superposition principle, continuous charge distribution. Electric field, electric field lines, electric dipole, electric field due to a dipole, torque on a dipole in uniform field. Electric flux, statement of Gauss's theorem and applications to uniformly charged infinite wire, infinite plane sheet, and thin spherical shell.",
    "Electrostatic Potential and Capacitance": "Electric potential, potential difference, electric potential due to point charge, dipole and system of charges; equipotential surfaces, electrical potential energy of a system of two point charges and electric dipoles in electrostatic field. Conductors and dielectrics, free charges and bound charges inside conductor, capacitors and capacitance, combination of capacitors in series and parallel, capacitance of parallel plate capacitor with/without dielectric, energy stored in capacitor.",
    "Current Electricity": "Electric current, drift velocity, mobility and relation with current; Ohm's law, electrical resistance, V-I characteristics (linear and non-linear), electrical energy and power, resistivity and conductivity, temperature dependence of resistance. Internal resistance of cell, potential difference and EMF of cell, combination of cells in series and parallel, Kirchhoff's laws and simple applications, Wheatstone bridge.",
    "Moving Charges and Magnetism": "Concept of magnetic field, Oersted's experiment. Biot-Savart law and application to current carrying circular loop. Ampere's law and application to infinitely long straight wire and solenoid. Force on moving charge in uniform magnetic and electric fields. Force on current-carrying conductor in uniform magnetic field, force between two parallel current-carrying conductors (definition of ampere), torque on current loop in magnetic field; moving coil galvanometer (current sensitivity and conversion to ammeter/voltmeter).",
    "Magnetism and Matter": "Bar magnet as equivalent solenoid qualitative, magnetic field lines, magnetic dipole moment of revolving electron; magnetic properties of materials: Para-, Dia- and Ferromagnetic substances with examples, magnetization, saturation, effect of temperature.",
    "Electromagnetic Induction": "Electromagnetic induction; Faraday's laws, induced EMF and current; Lenz's Law, Eddy currents. Self and mutual induction.",
    "Alternating Current": "Alternating currents, peak and RMS value of AC; reactance and impedance; LCR series circuit (phasor diagram only), resonance; power in AC circuits, power factor, wattless current. AC generator and transformer.",
    "Electromagnetic Waves": "Basic idea of displacement current, Electromagnetic waves, their characteristics, their transverse nature (qualitative idea only). Electromagnetic spectrum (radio waves, microwaves, infrared, visible, ultraviolet, X-rays, gamma rays) including elementary facts about their uses.",
    "Ray Optics and Optical Instruments": "Ray Optics: Reflection of light, spherical mirrors, mirror formula, refraction of light, total internal reflection and optical fibers, refraction at spherical surfaces, lenses, thin lens formula, lensmaker's formula, magnification, power of a lens, combination of thin lenses in contact, refraction of light through a prism. Optical instruments: Microscopes and astronomical telescopes (reflecting and refracting) and their magnifying powers.",
    "Wave Optics": "Wave Optics: Wave front and Huygens principle, reflection and refraction of plane wave at a plane surface using wave fronts. Proof of laws of reflection and refraction using Huygens principle. Interference, Young's double slit experiment and expression for fringe width, coherent sources and sustained interference of light. Diffraction due to a single slit, width of central maximum.",
    "Dual Nature of Radiation and Matter": "Dual nature of radiation, Photoelectric effect, Hertz and Lenard's observations; Einstein's photoelectric equation-particle nature of light. Experimental study of photoelectric effect, matter waves-wave nature of particles, de-Broglie relation.",
    "Atoms": "Alpha-particle scattering experiment; Rutherford's model of atom; Bohr model of hydrogen atom, energy levels, hydrogen spectrum, de-Broglie explanation of Bohr second postulate of quantization.",
    "Nuclei": "Composition and size of nucleus, nuclear force, mass-energy relation, mass defect; binding energy per nucleon and its variation with mass number, nuclear fission, nuclear fusion.",
    "Semiconductor Electronics: Materials, Devices and Simple Circuits": "Energy bands in conductors, semiconductors and insulators (qualitative ideas only). Intrinsic and extrinsic semiconductors- p and n type, p-n junction diode: I-V characteristics in forward and reverse bias, application of diode as a rectifier (half wave and full wave).",

    # Mathematics
    "Relations and Functions": "Types of relations: reflexive, symmetric, transitive and equivalence relations. One to one and onto functions.",
    "Inverse Trigonometric Functions": "Definition, range, domain, principal value branch. Graphs of inverse trigonometric functions.",
    "Matrices": "Concept, notation, order, equality, types of matrices, zero and identity matrix, transpose of a matrix, symmetric and skew symmetric matrices. Operation on matrices: Addition and multiplication and multiplication with a scalar. Non-commutativity of multiplication of matrices, invertible matrices and proof of the uniqueness of inverse.",
    "Determinants": "Determinant of a square matrix (up to 3 x 3 matrices), minors, co-factors and applications of determinants in finding the area of a triangle. Adjoint and inverse of a square matrix. Solving system of linear equations in two or three variables (having unique solution) using inverse of a matrix.",
    "Continuity and Differentiability": "Continuity and differentiability, derivative of composite functions, chain rule, derivative of inverse trigonometric functions, derivative of implicit functions. Concept of exponential and logarithmic functions. Derivatives of logarithmic and exponential functions. Logarithmic differentiation, derivative of functions expressed in parametric forms. Second order derivatives.",
    "Application of Derivatives (AOD)": "Applications of derivatives: rate of change of bodies, increasing/decreasing functions, maxima and minima (first derivative test motivated geometrically and second derivative test given as a provable tool). Simple problems.",
    "Integrals": "Integration as inverse process of differentiation. Integration of a variety of functions by substitution, by partial fractions and by parts. Fundamental Theorem of Calculus (without proof). Basic properties of definite integrals and evaluation of definite integrals.",
    "Applications of the Integrals (Area under Curves)": "Applications in finding the area under simple curves, especially lines, circles/parabolas/ellipses (in standard form only).",
    "Differential Equations": "Definition, order and degree, general and particular solutions of a differential equation. Formation of differential equation whose general solution is given. Solution of differential equations by method of separation of variables, solutions of homogeneous differential equations of first order and first degree. Solutions of linear differential equation of the type: dy/dx + py = q.",
    "Vectors": "Vectors and scalars, magnitude and direction of a vector. Direction cosines and direction ratios of a vector. Types of vectors (equal, unit, zero, parallel and collinear vectors), position vector of a point, negative of a vector, components of a vector, addition of vectors, multiplication of a vector by a scalar, position vector of a point dividing a line segment in a given ratio. Definition, properties and application of scalar (dot) product of vectors, vector (cross) product of vectors.",
    "Three Dimensional Geometry (3D)": "Direction cosines and direction ratios of a line joining two points. Cartesian equation and vector equation of a line, coplanar and skew lines, shortest distance between two lines. Angle between two lines.",
    "Linear Programming": "Introduction, related terminology such as constraints, objective function, optimization, graphical method of solution for problems in two variables, feasible and infeasible regions (bounded or unbounded), feasible and infeasible solutions, optimal feasible solutions (up to three non-trivial constraints).",
    "Probability": "Conditional probability, multiplication rule on probability, independent events, total probability, Bayes' theorem, Random variable and its probability distribution, mean of random variable.",

    # Biology
    "Sexual Reproduction in Flowering Plants": "Flower structure; development of male and female gametophytes; pollination - types, agencies and examples; outbreeding devices; pollen-pistil interaction; double fertilization; post fertilization events - development of endosperm and embryo, development of seed and formation of fruit; special modes - apomixis, parthenocarpy, polyembryony; Significance of seed dispersal and fruit formation.",
    "Human Reproduction": "Male and female reproductive systems; microscopic anatomy of testis and ovary; gametogenesis - spermatogenesis and oogenesis; menstrual cycle; fertilisation, embryo development up to blastocyst formation, implantation; pregnancy and placenta formation; parturition; lactation.",
    "Reproductive Health": "Need for reproductive health and prevention of Sexually Transmitted Infections (STIs); birth control - need and methods, contraception and medical termination of pregnancy (MTP); amniocentesis; infertility and assisted reproductive technologies - IVF, ZIFT, GIFT.",
    "Principles of Inheritance and Variation": "Heredity and variation: Mendelian inheritance; deviations from Mendelism - incomplete dominance, co-dominance, multiple alleles and inheritance of blood groups, pleiotropy; elementary idea of polygenic inheritance; chromosome theory of inheritance; chromosomes and genes; Sex determination - in humans, birds and honey bee; linkage and crossing over; sex linked inheritance - haemophilia, colour blindness; Mendelian disorders in humans - thalassemia, phenylketonuria, sickle cell anemia; chromosomal disorders in humans: Down's, Turner's and Klinefelter's syndromes.",
    "Molecular Basis of Inheritance": "Search for genetic material and DNA as genetic material; Structure of DNA and RNA; DNA packaging; DNA replication; Central Dogma; transcription, genetic code, translation; gene expression and regulation - lac operon; Genome, Human and rice genome projects; DNA fingerprinting.",
    "Evolution": "Origin of life; biological evolution and evidences for biological evolution (paleontology, comparative anatomy, embryology and molecular evidences); Darwin's contribution, modern synthetic theory of evolution; mechanism of evolution - variation (mutation and recombination) and natural selection with examples, types of natural selection; Gene flow and genetic drift; Hardy-Weinberg's principle; adaptive radiation; human evolution.",
    "Human Health and Diseases": "Pathogens; parasites causing human diseases (malaria, dengue, chikungunya, filariasis, ascariasis, typhoid, pneumonia, common cold, amoebiasis, ring worm) and their control; Basic concepts of immunology - vaccines; cancer, HIV and AIDS; Adolescence - drug and alcohol abuse.",
    "Microbes in Human Welfare": "Microbes in food processing, industrial production, sewage treatment, energy generation and as biocontrol agents and biofertilizers. Antibiotics; production and judicious use.",
    "Biotechnology - Principles and Processes": "Genetic Engineering (Recombinant DNA Technology). Restriction enzymes, cloning vectors, competent host transformation, processes of recombinant DNA technology (isolation of DNA, PCR, insertion, bioreactors, downstream processing).",
    "Biotechnology and its Applications": "Application of biotechnology in health and agriculture: Human insulin and vaccine production, stem cell technology, gene therapy; genetically modified organisms - Bt crops; transgenic animals; biosafety issues, biopiracy and patents.",
    "Organisms and Populations": "Organisms and environment: Habitat and niche, abiotic factors, adaptations; populations: population attributes, growth, birth rate, death rate, age distribution. Population interactions - mutualism, competition, predation, parasitism; population attributes - growth, birth rate and death rate, age distribution.",
    "Ecosystem": "Ecosystems: Patterns, components; productivity and decomposition; energy flow; pyramids of number, biomass, energy (nutrients cycling excluded).",
    "Biodiversity and its Conservation": "Concept of biodiversity; patterns of biodiversity; importance of biodiversity; loss of biodiversity; biodiversity conservation; hotspots, endangered organisms, extinction, Red Data Book, Sacred Groves, biosphere reserves, national parks, wildlife, sanctuaries and Ramsar sites.",

    # Computer Science
    "Python Revision Tour & Functions": "Review of Python basics, conditional statements, loops, strings, lists, tuples, dictionaries. Functions: scope, parameter passing, default parameters, positional arguments, return values.",
    "File Handling (Text, Binary & CSV)": "Need for data file handling, types of files (text, binary, CSV). Text file: opening, closing, read(), readline(), readlines(), write(), writelines(). Binary file: pickle module (dump, load). CSV file: csv module (reader, writer, delimiter).",
    "Data Structures: Stack": "Stack operations: Push, Pop, Peek using Python list. Applications of stack in expression evaluation and reversal.",
    "Computer Networks": "Evolution of networking, data communication terminologies, transmission media (wired & wireless), network devices (hub, switch, router, gateway), topologies (bus, star, tree), protocols (TCP/IP, HTTP, FTP, DNS), network security concepts.",
    "Database Concepts & Structured Query Language (SQL)": "Relational data model, domain, tuple, relation, keys (primary, candidate, alternate, foreign). SQL: DDL, DML commands, SELECT with WHERE, ORDER BY, GROUP BY, HAVING, aggregate functions (COUNT, SUM, AVG, MIN, MAX), JOINS (Cartesian product, Equi-join, Natural join).",
    "Interface Python with SQL Database": "Connecting Python with MySQL database using mysql.connector, establishing connection, creating cursor, executing queries (fetch, insert, update, delete), commit and rollback.",

    # English Core
    "Reading Comprehension (Passages)": "Unseen factual and discursive passages (with conceptual understanding, decoding, analyzing, inferring, interpreting and vocabulary). Case-based factual passages with visual data/charts.",
    "Notices, Invitations, Letters & Articles/Reports": "Short writing tasks: Notice writing, formal/informal invitation and reply. Long writing tasks: Letters based on verbal/visual input (Application for a job with bio-data/resume, Letter to Editor), Article writing and Report writing.",
    "Flamingo (Prose & Poetry) & Vistas": "Flamingo Prose: The Last Lesson, Lost Spring, Deep Water, The Rattrap, Indigo, Poets and Pancakes, The Interview, Going Places. Flamingo Poetry: My Mother at Sixty-Six, Keeping Quiet, A Thing of Beauty, A Roadside Stand, Aunt Jennifer's Tigers. Vistas Supplementary: The Third Level, The Tiger King, Journey to the End of the Earth, The Enemy, On the Face of It, Memories of Childhood."
}

for subj, info in cbse12_data.items():
    if subj in cbse12_pdfs:
        p_url, p_name, p_size = cbse12_pdfs[subj]
        info["pdf_url"] = p_url
        info["pdf_name"] = p_name
        info["pdf_size"] = p_size
        info["official_board"] = "Central Board of Secondary Education (CBSE, Delhi)"
        info["official_citation"] = "CBSE Senior School Curriculum 2025-2026 (Circular Acad-39/2025)"

    for ch in info.get("chapters", []):
        ch_title = ch.get("chapter", "").strip()
        if ch_title in cbse12_topics_map:
            ch["official_topics"] = cbse12_topics_map[ch_title]

with open(os.path.join(DATA_DIR, "syllabus_cbse_12.json"), "w", encoding="utf-8") as f:
    json.dump(cbse12_data, f, indent=2, ensure_ascii=False)
print("Updated syllabus_cbse_12.json with official topics and PDF links.")

# 4. Update syllabus_cbse_10.json
with open(os.path.join(DATA_DIR, "syllabus_cbse_10.json"), "r", encoding="utf-8") as f:
    cbse10_data = json.load(f)

cbse10_pdfs = {
    "Mathematics": ("/curriculum_pdf/Class10_Maths.pdf", "Class10_Maths.pdf", "1.0 MB"),
    "Science": ("/curriculum_pdf/Class10_Science.pdf", "Class10_Science.pdf", "288 KB"),
    "Social Science": ("/curriculum_pdf/Class10_Social_Science.pdf", "Class10_Social_Science.pdf", "1.1 MB"),
    "English Language & Literature": ("/curriculum_pdf/Class10_English.pdf", "Class10_English.pdf", "885 KB")
}

cbse10_topics_map = {
    # Mathematics
    "Real Numbers": "Fundamental Theorem of Arithmetic - statements after reviewing work done earlier and after illustrating and motivating through examples, Proofs of irrationality of sqrt(2), sqrt(3), sqrt(5).",
    "Polynomials": "Zeros of a polynomial. Relationship between zeros and coefficients of quadratic polynomials.",
    "Pair of Linear Equations in Two Variables": "Pair of linear equations in two variables and graphical method of their solution, consistency/inconsistency. Algebraic conditions for number of solutions. Solution of a pair of linear equations in two variables algebraically - by substitution, by elimination. Simple situational problems.",
    "Quadratic Equations": "Standard form of a quadratic equation ax^2 + bx + c = 0, (a != 0). Solutions of quadratic equations (only real roots) by factorization, and by using quadratic formula. Relationship between discriminant and nature of roots. Situational problems based on quadratic equations related to day to day activities to be incorporated.",
    "Arithmetic Progressions (AP)": "Motivation for studying Arithmetic Progression Derivation of the nth term and sum of the first n terms of A.P. and their application in solving daily life problems.",
    "Coordinate Geometry": "Review: Concepts of coordinate geometry, graphs of linear equations. Distance formula. Section formula (internal division).",
    "Triangles": "Definitions, examples, counter examples of similar triangles. 1. (Prove) If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio. 2. (Motivate) If a line divides two sides of a triangle in the same ratio, the line is parallel to the third side. 3. (Motivate) If in two triangles, corresponding angles are equal, their corresponding sides are proportional and the triangles are similar (AAA/AA criterion). 4. (Motivate) SSS and SAS similarity criterion.",
    "Circles": "Tangent to a circle at, point of contact. 1. (Prove) The tangent at any point of a circle is perpendicular to the radius through the point of contact. 2. (Prove) The lengths of tangents drawn from an external point to a circle are equal.",
    "Introduction to Trigonometry & Identities": "Trigonometric ratios of an acute angle of a right-angled triangle. Proof of their existence (well defined); values of the trigonometric ratios of 30°, 45° and 60°. Relationships between the ratios. Proof and applications of the identity sin^2(A) + cos^2(A) = 1. Only simple identities to be given.",
    "Some Applications of Trigonometry (Heights & Distances)": "Simple problems on heights and distances. Problems should not involve more than two right triangles. Angles of elevation / depression should be only 30°, 45°, and 60°.",
    "Areas Related to Circles": "Area of sectors and segments of a circle. Problems based on areas and perimeter / circumference of the above said plane figures. (In calculating area of segment of a circle, problems should be restricted to central angle of 60°, 90° and 120° only).",
    "Surface Areas and Volumes": "Surface areas and volumes of combinations of any two of the following: cubes, cuboids, spheres, hemispheres and right circular cylinders/cones.",
    "Statistics": "Mean, median and mode of grouped data (bimodal situation to be avoided).",
    "Probability": "Classical definition of probability. Simple problems on finding the probability of an event.",

    # Science
    "Chemical Reactions and Equations": "Chemical equation, Balanced chemical equation, implications of a balanced chemical equation, types of chemical reactions: combination, decomposition, displacement, double displacement, precipitation, endothermic exothermic reactions, oxidation and reduction.",
    "Acids, Bases and Salts": "Their definitions in terms of furnishing of H+ and OH- ions, General properties, examples and uses, neutralization, concept of pH scale (Definition relating to logarithm not required), importance of pH in everyday life; preparation and uses of Sodium Hydroxide, Bleaching powder, Baking soda, Washing soda and Plaster of Paris.",
    "Metals and Non-metals": "Properties of metals and non-metals; Reactivity series; Formation and properties of ionic compounds; Basic metallurgical processes; Corrosion and its prevention.",
    "Carbon and its Compounds": "Covalent bonding in carbon compounds. Versatile nature of carbon. Homologous series. Nomenclature of carbon compounds containing functional groups (halogens, alcohol, ketones, aldehydes, alkanes and alkynes), difference between saturated hydrocarbons and unsaturated hydrocarbons. Chemical properties of carbon compounds (combustion, oxidation, addition and substitution reaction). Ethanol and Ethanoic acid (only properties and uses), soaps and detergents.",
    "Life Processes": "'Living Being'. Basic concept of nutrition, respiration, transport and excretion in plants and animals.",
    "Control and Coordination": "Tropic movements in plants; Introduction of plant hormones; Control and co-ordination in animals: Nervous system; Voluntary, involuntary and reflex action; Chemical co-ordination: animal hormones.",
    "How do Organisms Reproduce?": "Reproduction in animals and plants (asexual and sexual) reproductive health - need and methods of family planning. Safe sex vs HIV/AIDS. Child bearing and women's health.",
    "Heredity and Evolution": "Heredity; Mendel's contribution- Laws for inheritance of traits: Sex determination: brief introduction: (topics related to evolution omitted from board curriculum).",
    "Light - Reflection and Refraction": "Reflection of light by curved surfaces; Images formed by spherical mirrors, centre of curvature, principal axis, principal focus, focal length, mirror formula (Derivation not required), magnification. Refraction; Laws of refraction, refractive index. Refraction of light by spherical lens; Image formed by spherical lenses; Lens formula (Derivation not required); Magnification. Power of a lens.",
    "Human Eye and the Colourful World": "Functioning of a lens in human eye, defects of vision and their corrections, applications of spherical mirrors and lenses. Refraction of light through a prism, dispersion of light, scattering of light, applications in daily life (excluding color of the sun at sunrise and sunset).",
    "Electricity": "Electric current, potential difference and electric current. Ohm's law; Resistance, Resistivity, Factors on which the resistance of a conductor depends. Series combination of resistors, parallel combination of resistors and its applications in daily life. Heating effect of electric current and its applications in daily life. Electric power, Interrelation between P, V, I and R.",
    "Magnetic Effects of Electric Current": "Magnetic field, field lines, field due to a current carrying conductor, field due to current carrying coil or solenoid; Force on current carrying conductor, Fleming's Left Hand Rule, Direct current. Alternating current: frequency of AC. Advantage of AC over DC. Domestic electric circuits.",
    "Our Environment": "Eco-system, Environmental problems, Ozone depletion, waste production and their solutions. Biodegradable and non-biodegradable substances."
}

for subj, info in cbse10_data.items():
    if subj in cbse10_pdfs:
        p_url, p_name, p_size = cbse10_pdfs[subj]
        info["pdf_url"] = p_url
        info["pdf_name"] = p_name
        info["pdf_size"] = p_size
        info["official_board"] = "Central Board of Secondary Education (CBSE, Delhi)"
        info["official_citation"] = "CBSE Secondary School Curriculum 2025-2026 (Classes IX-X)"

    for ch in info.get("chapters", []):
        ch_title = ch.get("chapter", "").strip()
        if ch_title in cbse10_topics_map:
            ch["official_topics"] = cbse10_topics_map[ch_title]

with open(os.path.join(DATA_DIR, "syllabus_cbse_10.json"), "w", encoding="utf-8") as f:
    json.dump(cbse10_data, f, indent=2, ensure_ascii=False)
print("Updated syllabus_cbse_10.json with official topics and PDF links.")
