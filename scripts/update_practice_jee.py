import os

CHAPTERS_JEE_JS = '''
    const CHAPTERS_JEE = {
      Physics: [
        { name: "Motion in a Plane & Kinematics", count: "500 Qs", highYield: true },
        { name: "Current Electricity", count: "383 Qs", highYield: true },
        { name: "Electrostatic Potential and Capacitance", count: "300 Qs", highYield: true },
        { name: "Work, Energy and Power", count: "287 Qs", highYield: true },
        { name: "Moving Charges and Magnetism", count: "249 Qs", highYield: true },
        { name: "Ray Optics and Optical Instruments", count: "232 Qs", highYield: true },
        { name: "Laws of Motion & Friction", count: "177 Qs", highYield: true },
        { name: "Units and Measurements", count: "152 Qs", highYield: true },
        { name: "Rotational Motion & System of Particles", count: "151 Qs", highYield: true },
        { name: "Electric Charges and Fields", count: "144 Qs", highYield: false },
        { name: "Thermodynamics & Kinetic Theory", count: "139 Qs", highYield: false },
        { name: "Wave Optics", count: "132 Qs", highYield: false },
        { name: "Atoms and Nuclei", count: "125 Qs", highYield: false },
        { name: "Electromagnetic Induction & AC", count: "124 Qs", highYield: false },
        { name: "Dual Nature of Radiation and Matter", count: "98 Qs", highYield: false },
        { name: "Oscillations and Waves", count: "82 Qs", highYield: false },
        { name: "Semiconductor Electronics", count: "77 Qs", highYield: false },
        { name: "Gravitation", count: "75 Qs", highYield: false },
        { name: "Properties of Bulk Matter & Fluids", count: "68 Qs", highYield: false },
        { name: "Magnetism and Matter", count: "15 Qs", highYield: false },
        { name: "Electromagnetic Waves", count: "10 Qs", highYield: false }
      ],
      Chemistry: [
        { name: "Equilibrium", count: "683 Qs", highYield: true },
        { name: "Chemical Bonding and Molecular Structure", count: "159 Qs", highYield: true },
        { name: "d- and f-Block Elements", count: "158 Qs", highYield: true },
        { name: "Structure of Atom", count: "139 Qs", highYield: false },
        { name: "Thermodynamics (Chemistry)", count: "130 Qs", highYield: false },
        { name: "Solutions", count: "107 Qs", highYield: false },
        { name: "Chemical Kinetics", count: "107 Qs", highYield: false },
        { name: "Biomolecules", count: "105 Qs", highYield: false },
        { name: "Coordination Compounds", count: "84 Qs", highYield: false },
        { name: "Organic: Amines & Nitrogen Compounds", count: "80 Qs", highYield: false },
        { name: "Organic: Carbonyl Compounds (Aldehydes & Ketones)", count: "77 Qs", highYield: false },
        { name: "Electrochemistry", count: "76 Qs", highYield: false },
        { name: "Organic: Alcohols, Phenols & Ethers", count: "56 Qs", highYield: false },
        { name: "Organic: Hydrocarbons & Haloalkanes", count: "44 Qs", highYield: false },
        { name: "Classification of Elements & Periodicity", count: "27 Qs", highYield: false },
        { name: "p-Block Elements", count: "7 Qs", highYield: false }
      ],
      Mathematics: [
        { name: "Trigonometric Functions", count: "416 Qs", highYield: true },
        { name: "Three Dimensional Geometry & Vectors", count: "301 Qs", highYield: true },
        { name: "Continuity and Differentiability", count: "186 Qs", highYield: true },
        { name: "Coordinate Geometry: Conic Sections", count: "184 Qs", highYield: true },
        { name: "Matrices and Determinants", count: "170 Qs", highYield: true },
        { name: "Probability", count: "147 Qs", highYield: false },
        { name: "Application of Derivatives", count: "141 Qs", highYield: false },
        { name: "Integrals & Definite Integration", count: "140 Qs", highYield: false },
        { name: "Coordinate Geometry: Straight Lines & Circles", count: "138 Qs", highYield: false },
        { name: "Statistics & Mathematical Reasoning", count: "135 Qs", highYield: false },
        { name: "Differential Equations", count: "127 Qs", highYield: false },
        { name: "Sequences and Series", count: "87 Qs", highYield: false },
        { name: "Binomial Theorem", count: "87 Qs", highYield: false },
        { name: "Permutations and Combinations", count: "81 Qs", highYield: false },
        { name: "Complex Numbers & Quadratic Equations", count: "66 Qs", highYield: false }
      ]
    };
'''

with open('practice/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update title and meta description
html = html.replace(
    '<title>Learnosha | Chapterwise Practice Engine (CBSE 12 & NEET UG)</title>',
    '<title>Learnosha | Chapterwise Practice Engine (CBSE 12, NEET UG & JEE Main)</title>'
)
html = html.replace(
    'content="Step-by-step chapterwise practice engine for CBSE Class 12 PCM and NEET UG.',
    'content="Step-by-step chapterwise practice engine for CBSE Class 12, NEET UG, and JEE Main.'
)

# 2. Add CSS for JEE options & NVQ & CBT Switch banner
jee_css = '''
    /* JEE Main Specific Question Styles */
    .jee-options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin: 16px 0;
    }
    @media (max-width: 640px) {
      .jee-options-grid {
        grid-template-columns: 1fr;
      }
    }
    .jee-opt-btn {
      padding: 10px 14px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      background: var(--surface-alt);
      color: var(--text);
      font-size: 14.5px;
      cursor: pointer;
      text-align: left;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.15s ease;
    }
    .jee-opt-btn:hover {
      border-color: var(--accent);
      background: var(--surface);
    }
    .jee-opt-btn.correct {
      background: #ecfdf5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 700;
    }
    .jee-opt-btn.incorrect {
      background: #fef2f2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
    }
    .jee-nvq-box {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 16px 0;
      flex-wrap: wrap;
    }
    .jee-nvq-input {
      padding: 10px 16px;
      border: 2px solid var(--border);
      border-radius: var(--radius-sm);
      background: var(--surface);
      color: var(--text);
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 700;
      outline: none;
      width: 200px;
      transition: border-color 0.15s ease;
    }
    .jee-nvq-input:focus {
      border-color: var(--accent);
    }
    .jee-nvq-feedback {
      font-size: 13.5px;
      font-weight: 700;
    }
    .jee-cbt-switch-banner {
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 4px solid var(--accent);
      border-radius: var(--radius-md);
      padding: 14px 20px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      font-size: 13.5px;
      font-weight: 600;
      flex-wrap: wrap;
      box-shadow: var(--shadow-sm);
    }
'''
html = html.replace('/* Step-by-Step Practice Engine Styles */', '/* Step-by-Step Practice Engine Styles */\n' + jee_css)

# 3. Update JEE Exam Track Card in Step 1
old_jee_card = '''        <!-- JEE Main Card -->
        <div class="exam-track-card" onclick="window.location.href='/jee/'">
          <div class="exam-track-icon">⚡</div>
          <h2 class="exam-track-title">JEE Main Engineering Entrance</h2>
          <p class="exam-track-desc">
            12,667 authentic past examination questions (2019–2026) across 186 official NTA shifts with 3-hour CBT mock simulator, numerical value questions (NVQ), and step solutions.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (5,398 Qs)</span>
            <span class="exam-pill-item">Chemistry (3,727 Qs)</span>
            <span class="exam-pill-item">Mathematics (3,542 Qs)</span>
            <span class="exam-pill-item">186 Shifts (8 Years)</span>
          </div>
          <button class="btn-select-track">
            <span>Launch JEE Main CBT Track</span>
            <span>➔</span>
          </button>
        </div>'''

new_jee_card = '''        <!-- JEE Main Card -->
        <div class="exam-track-card" onclick="selectExamTrack('jee')">
          <div class="exam-track-icon">⚡</div>
          <h2 class="exam-track-title">JEE Main Engineering Entrance</h2>
          <p class="exam-track-desc">
            12,667 authentic past examination questions (2019–2026) across 186 official NTA shifts with chapterwise step practice, numerical value questions (NVQ), and step solutions.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (5,398 Qs)</span>
            <span class="exam-pill-item">Chemistry (3,727 Qs)</span>
            <span class="exam-pill-item">Mathematics (3,542 Qs)</span>
            <span class="exam-pill-item">186 Shifts (8 Years)</span>
          </div>
          <button class="btn-select-track">
            <span>Select JEE Engineering Track</span>
            <span>➔</span>
          </button>
        </div>'''

# normalize line endings for replace
html = html.replace(old_jee_card.replace('\r\n', '\n'), new_jee_card.replace('\r\n', '\n'))

# 4. Update drawer goal options
old_drawer_jee = '<a href="/jee/" class="drawer-goal-btn goal-toggle-pill" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center;">⚡ JEE Main</a>'
new_drawer_jee = '<button class="drawer-goal-btn goal-toggle-pill" data-goal="jee" onclick="selectGoal(\'jee\')">⚡ JEE Main</button>'
html = html.replace(old_drawer_jee, new_drawer_jee)

# 5. Insert CHAPTERS_JEE after CHAPTERS_NEET
chapters_neet_end_marker = '      ]\n    };'
idx = html.find('const CHAPTERS_NEET = {')
if idx != -1:
    end_idx = html.find('    };', idx) + 6
    html = html[:end_idx] + '\n' + CHAPTERS_JEE_JS + html[end_idx:]

# 6. Update initRouterFromURL
html = html.replace(
    "if (urlExam && (urlExam === 'cbse' || urlExam === 'neet')) {",
    "if (urlExam && (urlExam === 'cbse' || urlExam === 'neet' || urlExam === 'jee')) {"
)

# 7. Update renderSubjectScreen
old_subj_screen = '''    function renderSubjectScreen() {
      const isCbse = currentExam === 'cbse';
      document.getElementById('subjStageBadge').innerText = `${isCbse ? 'CBSE CLASS 12' : 'NEET UG'} • STEP 2 OF 3`;
      document.getElementById('subjStageHeading').innerText = `Select ${isCbse ? 'CBSE Class 12' : 'NEET UG'} Subject`;
      document.getElementById('subjStageSubtitle').innerText = isCbse
        ? 'Choose Physics, Chemistry, or Mathematics to practice board questions with step-wise derivations.'
        : 'Choose Physics, Chemistry, Botany, or Zoology with verified NTA answer keys.';

      const container = document.getElementById('subjectCardsContainer');
      const subjects = isCbse ? [
        { name: 'Physics', icon: '⚛️', count: '3,258 Qs', desc: '14 Chapters • Electric Charges to Semiconductors with step marking.' },
        { name: 'Chemistry', icon: '🧪', count: '3,023 Qs', desc: '10 Chapters • Solutions, Electrochemistry to Biomolecules.' },
        { name: 'Mathematics', icon: '📐', count: '3,998 Qs', desc: '13 Chapters • Matrices, Integrals, 3D Geometry to Probability.' }
      ] : [
        { name: 'Physics', icon: '⚛️', count: '520 Qs', desc: 'Mechanics, Electrodynamics, Optics & Modern Physics.' },
        { name: 'Chemistry', icon: '🧪', count: '520 Qs', desc: 'Physical, Inorganic, and Reaction Mechanism Organic Chemistry.' },
        { name: 'Botany', icon: '🌿', count: '520 Qs', desc: 'Genetics, Cell Biology, Plant Physiology & Ecology.' },
        { name: 'Zoology', icon: '🐾', count: '500 Qs', desc: 'Human Physiology, Reproduction, Evolution & Health.' }
      ];'''

new_subj_screen = '''    function renderSubjectScreen() {
      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      const isJee = currentExam === 'jee';
      
      const badgeText = isCbse ? 'CBSE CLASS 12' : (isNeet ? 'NEET UG' : 'JEE MAIN');
      document.getElementById('subjStageBadge').innerText = `${badgeText} • STEP 2 OF 3`;
      document.getElementById('subjStageHeading').innerText = `Select ${isCbse ? 'CBSE Class 12' : (isNeet ? 'NEET UG' : 'JEE Main')} Subject`;
      document.getElementById('subjStageSubtitle').innerText = isCbse
        ? 'Choose Physics, Chemistry, or Mathematics to practice board questions with step-wise derivations.'
        : (isNeet ? 'Choose Physics, Chemistry, Botany, or Zoology with verified NTA answer keys.' : 'Choose Physics, Chemistry, or Mathematics with official NTA answer keys, MCQs and NVQs.');

      const container = document.getElementById('subjectCardsContainer');
      let subjects = [];
      if (isCbse) {
        subjects = [
          { name: 'Physics', icon: '⚛️', count: '3,258 Qs', desc: '14 Chapters • Electric Charges to Semiconductors with step marking.' },
          { name: 'Chemistry', icon: '🧪', count: '3,023 Qs', desc: '10 Chapters • Solutions, Electrochemistry to Biomolecules.' },
          { name: 'Mathematics', icon: '📐', count: '3,998 Qs', desc: '13 Chapters • Matrices, Integrals, 3D Geometry to Probability.' }
        ];
      } else if (isNeet) {
        subjects = [
          { name: 'Physics', icon: '⚛️', count: '520 Qs', desc: 'Mechanics, Electrodynamics, Optics & Modern Physics.' },
          { name: 'Chemistry', icon: '🧪', count: '520 Qs', desc: 'Physical, Inorganic, and Reaction Mechanism Organic Chemistry.' },
          { name: 'Botany', icon: '🌿', count: '520 Qs', desc: 'Genetics, Cell Biology, Plant Physiology & Ecology.' },
          { name: 'Zoology', icon: '🐾', count: '500 Qs', desc: 'Human Physiology, Reproduction, Evolution & Health.' }
        ];
      } else {
        subjects = [
          { name: 'Physics', icon: '⚛️', count: '5,398 Qs', desc: 'Kinematics, Mechanics, Electrodynamics, Optics, AC & Modern Physics.' },
          { name: 'Chemistry', icon: '🧪', count: '3,727 Qs', desc: 'Physical, Inorganic, Coordination Compounds & Organic Reaction Mechanisms.' },
          { name: 'Mathematics', icon: '📐', count: '3,542 Qs', desc: 'Calculus, Vectors & 3D Geometry, Conics, Matrices & Probability.' }
        ];
      }'''

html = html.replace(old_subj_screen.replace('\r\n', '\n'), new_subj_screen.replace('\r\n', '\n'))

# 8. Update renderChapterScreen & filterChapterCards
old_ch_screen = '''    function renderChapterScreen() {
      const isCbse = currentExam === 'cbse';
      document.getElementById('chapterStageHeading').innerText = `${currentSubject} Chapters (${isCbse ? 'CBSE 12' : 'NEET UG'})`;
      document.getElementById('chapterStageSubtitle').innerText = `Select any chapter below to load its questions, or practice all chapters combined.`;

      document.getElementById('chapterSearchInput').value = '';
      filterChapterCards('all');
    }

    function filterChapterCards(filterType) {
      document.getElementById('chFilterAll').classList.toggle('active', filterType === 'all');
      document.getElementById('chFilterHighYield').classList.toggle('active', filterType === 'highyield');

      const isCbse = currentExam === 'cbse';
      const list = isCbse ? CHAPTERS_CBSE[currentSubject] : CHAPTERS_NEET[currentSubject];'''

new_ch_screen = '''    function renderChapterScreen() {
      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      const label = isCbse ? 'CBSE 12' : (isNeet ? 'NEET UG' : 'JEE Main');
      document.getElementById('chapterStageHeading').innerText = `${currentSubject} Chapters (${label})`;
      document.getElementById('chapterStageSubtitle').innerText = `Select any chapter below to load its questions, or practice all chapters combined.`;

      document.getElementById('chapterSearchInput').value = '';
      filterChapterCards('all');
    }

    function filterChapterCards(filterType) {
      document.getElementById('chFilterAll').classList.toggle('active', filterType === 'all');
      document.getElementById('chFilterHighYield').classList.toggle('active', filterType === 'highyield');

      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      const list = isCbse ? CHAPTERS_CBSE[currentSubject] : (isNeet ? CHAPTERS_NEET[currentSubject] : CHAPTERS_JEE[currentSubject]);'''

html = html.replace(old_ch_screen.replace('\r\n', '\n'), new_ch_screen.replace('\r\n', '\n'))

# 9. Update renderStreamScreen URL and filter logic
old_stream_url = '''      const cacheBust = '?v=20261110_8';
      const url = currentExam === 'cbse'
        ? `/data/cbse_${currentSubject.toLowerCase()}.json${cacheBust}`
        : `/data/neet_all.json${cacheBust}`;'''

new_stream_url = '''      const cacheBust = '?v=20261111_2';
      let url = '';
      if (currentExam === 'cbse') {
        url = `/data/cbse_${currentSubject.toLowerCase()}.json${cacheBust}`;
      } else if (currentExam === 'neet') {
        url = `/data/neet_all.json${cacheBust}`;
      } else {
        url = `/data/jee_${currentSubject.toLowerCase()}.json${cacheBust}`;
      }'''

html = html.replace(old_stream_url.replace('\r\n', '\n'), new_stream_url.replace('\r\n', '\n'))

# 10. Update stream filtering for JEE
old_ch_filter = '''      // Filter by chapter
      if (currentChapter !== 'all') {
        if (currentExam === 'cbse') {
          const chNum = parseInt(currentChapter, 10);
          if (!isNaN(chNum)) {
            list = list.filter(q => q.chapter_number === chNum);
          } else {
            list = list.filter(q => (q.chapter_name || '').toLowerCase().includes(currentChapter.toLowerCase()));
          }
        } else {
          list = list.filter(q => {
            const ch = (q.chapter || q.chapter_name || '').toLowerCase();
            return ch.includes(currentChapter.toLowerCase()) || currentChapter.toLowerCase().includes(ch);
          });
        }
      }'''

new_ch_filter = '''      // Filter by chapter
      if (currentChapter !== 'all') {
        if (currentExam === 'cbse') {
          const chNum = parseInt(currentChapter, 10);
          if (!isNaN(chNum)) {
            list = list.filter(q => q.chapter_number === chNum);
          } else {
            list = list.filter(q => (q.chapter_name || '').toLowerCase().includes(currentChapter.toLowerCase()));
          }
        } else if (currentExam === 'neet') {
          list = list.filter(q => {
            const ch = (q.chapter || q.chapter_name || '').toLowerCase();
            return ch.includes(currentChapter.toLowerCase()) || currentChapter.toLowerCase().includes(ch);
          });
        } else if (currentExam === 'jee') {
          list = list.filter(q => {
            const ch = (q.ncert_chapter || '').toLowerCase();
            return ch.includes(currentChapter.toLowerCase()) || currentChapter.toLowerCase().includes(ch);
          });
        }
      }'''

html = html.replace(old_ch_filter.replace('\r\n', '\n'), new_ch_filter.replace('\r\n', '\n'))

# 11. Update options rendering and solution action in stream
old_options_render = '''        let optionsHtml = '';
        if (currentExam === 'neet' && q.options) {
          optionsHtml = '<div class="neet-options-grid">';
          ['A', 'B', 'C', 'D'].forEach(optKey => {
            const optVal = q.options[optKey] || '';
            optionsHtml += `
              <div class="neet-opt-btn" id="opt_${qId}_${optKey}" onclick="checkNeetOption('${qId}', '${optKey}', '${q.correct_answer}')">
                <span class="opt-label">${optKey}</span>
                <span class="opt-text">${escapeHtml(optVal)}</span>
              </div>
            `;
          });
          optionsHtml += '</div>';
        }

        // Action Buttons
        const solBtnLabel = currentExam === 'neet' ? '💡 Solution' : (hasCachedSol ? '✓ Step Solution' : '💡 Solution & Rubric');
        const solAction = currentExam === 'neet' 
          ? `toggleNeetSolution('${qId}', '${q.correct_answer || 'A'}', '${year}', '${escapeHtml(source)}')`
          : `toggleCbseSolution('${qId}', '${currentSubject}', '${year}', '${marksDisplay}')`;'''

new_options_render = '''        let optionsHtml = '';
        if (currentExam === 'neet' && q.options) {
          optionsHtml = '<div class="neet-options-grid">';
          ['A', 'B', 'C', 'D'].forEach(optKey => {
            const optVal = q.options[optKey] || '';
            optionsHtml += `
              <div class="neet-opt-btn" id="opt_${qId}_${optKey}" onclick="checkNeetOption('${qId}', '${optKey}', '${q.correct_answer}')">
                <span class="opt-label">${optKey}</span>
                <span class="opt-text">${escapeHtml(optVal)}</span>
              </div>
            `;
          });
          optionsHtml += '</div>';
        } else if (currentExam === 'jee') {
          if (q.type === 'MCQ' && q.options) {
            optionsHtml = '<div class="jee-options-grid">';
            for (let k of ['1', '2', '3', '4']) {
              if (q.options[k]) {
                optionsHtml += `
                  <div class="jee-opt-btn" id="opt_${qId}_${k}" onclick="checkJeeOption('${qId}', '${k}', '${q.correct_answer}')">
                    <span class="opt-label">(${k})</span>
                    <span class="opt-text math-content">${q.options[k]}</span>
                  </div>
                `;
              }
            }
            optionsHtml += '</div>';
          } else if (q.type === 'Numerical') {
            optionsHtml = `
              <div class="jee-nvq-box">
                <input type="text" class="jee-nvq-input" id="input_${qId}" placeholder="Enter numerical answer...">
                <button class="btn-card-action active" onclick="checkJeeNumerical('${qId}', '${q.correct_answer}')" style="background:var(--accent); color:#ffffff; font-weight:700;">Check Answer</button>
                <span id="feedback_${qId}" class="jee-nvq-feedback"></span>
              </div>
            `;
          }
        }

        // Action Buttons
        const solBtnLabel = currentExam === 'cbse' ? (hasCachedSol ? '✓ Step Solution' : '💡 Solution & Rubric') : '💡 View Solution';
        const solAction = currentExam === 'neet' 
          ? `toggleNeetSolution('${qId}', '${q.correct_answer || 'A'}', '${year}', '${escapeHtml(source)}')`
          : (currentExam === 'jee'
              ? `toggleJeeSolution('${qId}', '${q.correct_answer || ''}', '${escapeHtml(q.shift_name || '')}')`
              : `toggleCbseSolution('${qId}', '${currentSubject}', '${year}', '${marksDisplay}')`);'''

html = html.replace(old_options_render.replace('\r\n', '\n'), new_options_render.replace('\r\n', '\n'))

# 12. Add toggleJeeSolution, checkJeeOption, checkJeeNumerical helper functions
jee_helpers = '''
    function checkJeeOption(qId, selectedOpt, correctOpt) {
      for (let k of ['1', '2', '3', '4']) {
        const el = document.getElementById(`opt_${qId}_${k}`);
        if (el) {
          if (String(k) === String(correctOpt)) el.classList.add('correct');
          else if (String(k) === String(selectedOpt)) el.classList.add('incorrect');
        }
      }
    }

    function checkJeeNumerical(qId, correctVal) {
      const input = document.getElementById(`input_${qId}`);
      const fb = document.getElementById(`feedback_${qId}`);
      if (!input || !fb) return;
      const userVal = input.value.trim();
      if (!userVal) return;
      if (String(userVal) === String(correctVal)) {
        fb.innerHTML = `<span style="color:#059669;">✓ Correct! Answer: ${correctVal} (+4)</span>`;
        input.style.borderColor = '#059669';
      } else {
        fb.innerHTML = `<span style="color:#dc2626;">✗ Incorrect. Official key: ${correctVal} (-1)</span>`;
        input.style.borderColor = '#dc2626';
      }
    }

    function toggleJeeSolution(qId, correctAnswer, shiftName) {
      const box = document.getElementById('sol_' + qId);
      if (!box) return;

      if (box.classList.contains('open')) {
        box.classList.remove('open');
        return;
      }

      const q = filteredQuestions.find(item => (item.id || '') === qId);
      const solText = q && q.solution ? q.solution : 'Official NTA Answer Key and evaluation step.';

      box.innerHTML = `
        <div class="sol-header">
          <span class="sol-badge-cached">✓ Official NTA Answer Key: Option (${correctAnswer || 'Key Verified'})</span>
          <span class="q-marks-pill">+4 / -1</span>
        </div>
        <div class="math-content" style="line-height:1.75; margin-top:10px; font-size:14.5px;">
          ${solText}
        </div>
      `;
      box.classList.add('open');

      if (window.renderMathInElement) {
        renderMathInElement(box, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\\\(', right: '\\\\)', display: false },
            { left: '\\\\[', right: '\\\\]', display: true }
          ],
          throwOnError: false
        });
      }
    }
'''

html = html.replace('function showToast(msg) {', jee_helpers + '\n    function showToast(msg) {')

# 13. Add CBT switch banner when stream rendered
old_feed_start = "      const slice = filteredQuestions.slice(0, displayedQuestionsCount);\n      let html = '';"
new_feed_start = """      const slice = filteredQuestions.slice(0, displayedQuestionsCount);
      let html = '';
      if (currentExam === 'jee') {
        html += `
          <div class="jee-cbt-switch-banner">
            <span>⚡ <strong>JEE Main Chapterwise Practice:</strong> Practicing 12,667 questions topic by topic. Looking for 3-Hour full shift mock papers?</span>
            <a href="/jee/" class="btn-step-back" style="background:var(--accent); color:#ffffff; border-color:var(--accent); text-decoration:none;">Launch CBT Simulator ➔</a>
          </div>
        `;
      }"""

html = html.replace(old_feed_start.replace('\r\n', '\n'), new_feed_start.replace('\r\n', '\n'))

with open('practice/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("practice/index.html updated successfully with complete JEE Main step wizard!")
