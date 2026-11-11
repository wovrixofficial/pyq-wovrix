import os

with open('repeated/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update title and meta description
html = html.replace(
    '<title>High-Yield Repeats Radar (CBSE 12 & NEET UG) | Learnosha</title>',
    '<title>High-Yield Repeats Radar (CBSE 12, NEET UG & JEE Main) | Learnosha</title>'
)
html = html.replace(
    'content="Proprietary repetition frequency radar for CBSE Class 12 and NEET UG.',
    'content="Proprietary repetition frequency radar for CBSE Class 12, NEET UG, and JEE Main.'
)

# 2. Update JEE Card in Step 1
old_jee_card = '''        <!-- JEE Main Recurrence Radar Card -->
        <div class="exam-track-card" onclick="window.location.href='/jee/'">
          <div class="exam-track-icon">⚡</div>
          <h2 class="exam-track-title">JEE Main 8-Year Recurrence Radar (2019–2026)</h2>
          <p class="exam-track-desc">
            Top 22 recurring concept archetypes analyzed across 12,667 questions and 186 shifts, including King's Property integration (302x), capacitor dielectrics (258x), and matrix adjoint identities (225x).
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Maths (302x King's Property)</span>
            <span class="exam-pill-item">Physics (258x Dielectrics)</span>
            <span class="exam-pill-item">Chemistry (183x CFSE)</span>
            <span class="exam-pill-item">22 Core Archetypes</span>
          </div>
          <button class="btn-select-track">
            <span>Explore JEE Main Repeats</span>
            <span>➔</span>
          </button>
        </div>'''

new_jee_card = '''        <!-- JEE Main Recurrence Radar Card -->
        <div class="exam-track-card" onclick="selectExamTrack('jee')">
          <div class="exam-track-icon">⚡</div>
          <h2 class="exam-track-title">JEE Main 8-Year Recurrence Radar (2019–2026)</h2>
          <p class="exam-track-desc">
            Top 22 recurring concept archetypes analyzed across 12,667 questions and 186 shifts, including King's Property integration (302x), capacitor dielectrics (258x), and matrix adjoint identities (225x).
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Maths (302x King's Property)</span>
            <span class="exam-pill-item">Physics (258x Dielectrics)</span>
            <span class="exam-pill-item">Chemistry (183x CFSE)</span>
            <span class="exam-pill-item">22 Core Archetypes</span>
          </div>
          <button class="btn-select-track">
            <span>Explore JEE Main Repeats</span>
            <span>➔</span>
          </button>
        </div>'''

html = html.replace(old_jee_card.replace('\r\n', '\n'), new_jee_card.replace('\r\n', '\n'))

# 3. Update drawer goal option
old_drawer_jee = '<a href="/jee/" class="drawer-goal-btn goal-toggle-pill" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center;">⚡ JEE Main</a>'
new_drawer_jee = '<button class="drawer-goal-btn goal-toggle-pill" data-goal="jee" onclick="selectGoal(\'jee\')">⚡ JEE Main</button>'
html = html.replace(old_drawer_jee, new_drawer_jee)

# 4. Update initRouterFromURL
html = html.replace(
    "if (urlExam && (urlExam === 'cbse' || urlExam === 'neet')) {",
    "if (urlExam && (urlExam === 'cbse' || urlExam === 'neet' || urlExam === 'jee')) {"
)

# 5. Update renderSubjectScreen
old_subj_screen = '''    function renderSubjectScreen() {
      const isCbse = currentExam === 'cbse';
      document.getElementById('subjStageBadge').innerText = `${isCbse ? 'CBSE CLASS 12' : 'NEET UG'} • STEP 2 OF 3`;
      document.getElementById('subjStageHeading').innerText = `Select ${isCbse ? 'CBSE Class 12' : 'NEET UG'} Subject`;

      const container = document.getElementById('subjectCardsContainer');
      const subjects = isCbse ? [
        { name: 'Physics', icon: '⚛️', count: '540+ Clusters', desc: 'Optics, Current Electricity, Capacitance, AC & Semiconductors.' },
        { name: 'Chemistry', icon: '🧪', count: '610+ Clusters', desc: 'Solutions, Electrochemistry, Kinetics, Coordination & Aldehydes.' },
        { name: 'Mathematics', icon: '📐', count: '640+ Clusters', desc: 'Matrices, Determinants, Integrals, Vectors & 3D Geometry.' }
      ] : [
        { name: 'Physics', icon: '⚛️', count: '30+ Concept Tiers', desc: 'Photoelectric effect, Ray Optics, Modern Physics & Rotational.' },
        { name: 'Chemistry', icon: '🧪', count: '35+ Concept Tiers', desc: 'Coordination, Chemical Bonding, Electrochemistry & Kinetics.' },
        { name: 'Botany', icon: '🌿', count: '28+ Concept Tiers', desc: 'Genetics, Molecular Basis, Photosynthesis & Cell Division.' },
        { name: 'Zoology', icon: '🐾', count: '26+ Concept Tiers', desc: 'Human Reproduction, Evolution, Health and Disease.' }
      ];'''

new_subj_screen = '''    function renderSubjectScreen() {
      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      const badgeText = isCbse ? 'CBSE CLASS 12' : (isNeet ? 'NEET UG' : 'JEE MAIN');
      document.getElementById('subjStageBadge').innerText = `${badgeText} • STEP 2 OF 3`;
      document.getElementById('subjStageHeading').innerText = `Select ${isCbse ? 'CBSE Class 12' : (isNeet ? 'NEET UG' : 'JEE Main')} Subject`;

      const container = document.getElementById('subjectCardsContainer');
      let subjects = [];
      if (isCbse) {
        subjects = [
          { name: 'Physics', icon: '⚛️', count: '540+ Clusters', desc: 'Optics, Current Electricity, Capacitance, AC & Semiconductors.' },
          { name: 'Chemistry', icon: '🧪', count: '610+ Clusters', desc: 'Solutions, Electrochemistry, Kinetics, Coordination & Aldehydes.' },
          { name: 'Mathematics', icon: '📐', count: '640+ Clusters', desc: 'Matrices, Determinants, Integrals, Vectors & 3D Geometry.' }
        ];
      } else if (isNeet) {
        subjects = [
          { name: 'Physics', icon: '⚛️', count: '30+ Concept Tiers', desc: 'Photoelectric effect, Ray Optics, Modern Physics & Rotational.' },
          { name: 'Chemistry', icon: '🧪', count: '35+ Concept Tiers', desc: 'Coordination, Chemical Bonding, Electrochemistry & Kinetics.' },
          { name: 'Botany', icon: '🌿', count: '28+ Concept Tiers', desc: 'Genetics, Molecular Basis, Photosynthesis & Cell Division.' },
          { name: 'Zoology', icon: '🐾', count: '26+ Concept Tiers', desc: 'Human Reproduction, Evolution, Health and Disease.' }
        ];
      } else {
        subjects = [
          { name: 'Physics', icon: '⚛️', count: '8 Core Archetypes', desc: 'Capacitor Dielectrics (258x), Photoelectric (215x), Rolling (198x), Drift Velocity (188x).' },
          { name: 'Chemistry', icon: '🧪', count: '7 Core Archetypes', desc: 'CFSE (183x), Chemical Equilibrium (176x), First-Order Kinetics (172x), Aldol (165x).' },
          { name: 'Mathematics', icon: '📐', count: '7 Core Archetypes', desc: 'King\\'s Property Integrals (302x), Matrix Adjoints (225x), Skew Lines (218x), Binomial (198x).' }
        ];
      }'''

html = html.replace(old_subj_screen.replace('\r\n', '\n'), new_subj_screen.replace('\r\n', '\n'))

# 6. Update renderRadarScreen
old_radar_screen = '''    function renderRadarScreen() {
      const isCbse = currentExam === 'cbse';
      document.getElementById('radarStageHeading').innerText = `${currentSubject} Recurrence Radar (${isCbse ? 'CBSE 12' : 'NEET UG'})`;
      
      const vaultBanner = document.getElementById('radarNeetVaultBanner');
      if (vaultBanner) vaultBanner.style.display = isCbse ? 'none' : 'block';

      const slider = document.getElementById('repeatFrequencySlider');
      const ticks = document.getElementById('sliderTicksContainer');

      if (isCbse) {
        slider.min = "2";
        slider.max = "6";
        slider.value = "2";
        minFrequency = 2;
        document.getElementById('sliderValueText').innerText = "2x (Duplicates & Clones)";
        ticks.innerHTML = '<span>2x (Twins & Clones)</span><span>3x (High Yield)</span><span>4x (Frequent Pattern)</span><span>5x+ (Core Master Repeats)</span>';
      } else {
        slider.min = "2";
        slider.max = "30";
        slider.value = "2";
        minFrequency = 2;
        document.getElementById('sliderValueText').innerText = "2x Appearances";
        ticks.innerHTML = '<span>2x (All Recurrent)</span><span>10x (High Yield)</span><span>20x (Core Frequency)</span><span>30x (Every Single Year)</span>';
      }

      applyRadarFilters();
    }'''

new_radar_screen = '''    function renderRadarScreen() {
      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      const label = isCbse ? 'CBSE 12' : (isNeet ? 'NEET UG' : 'JEE Main');
      document.getElementById('radarStageHeading').innerText = `${currentSubject} Recurrence Radar (${label})`;
      
      const vaultBanner = document.getElementById('radarNeetVaultBanner');
      if (vaultBanner) vaultBanner.style.display = (isCbse || !isNeet) ? 'none' : 'block';

      const slider = document.getElementById('repeatFrequencySlider');
      const ticks = document.getElementById('sliderTicksContainer');

      if (isCbse) {
        slider.min = "2";
        slider.max = "6";
        slider.value = "2";
        minFrequency = 2;
        document.getElementById('sliderValueText').innerText = "2x (Duplicates & Clones)";
        ticks.innerHTML = '<span>2x (Twins & Clones)</span><span>3x (High Yield)</span><span>4x (Frequent Pattern)</span><span>5x+ (Core Master Repeats)</span>';
      } else if (isNeet) {
        slider.min = "2";
        slider.max = "30";
        slider.value = "2";
        minFrequency = 2;
        document.getElementById('sliderValueText').innerText = "2x Appearances";
        ticks.innerHTML = '<span>2x (All Recurrent)</span><span>10x (High Yield)</span><span>20x (Core Frequency)</span><span>30x (Every Single Year)</span>';
      } else {
        slider.min = "2";
        slider.max = "300";
        slider.value = "2";
        minFrequency = 2;
        document.getElementById('sliderValueText').innerText = "2x Appearances";
        ticks.innerHTML = '<span>2x (All Patterns)</span><span>50x (High Yield)</span><span>150x (Core Frequency)</span><span>300x (King\\'s Property)</span>';
      }

      applyRadarFilters();
    }'''

html = html.replace(old_radar_screen.replace('\r\n', '\n'), new_radar_screen.replace('\r\n', '\n'))

# 7. Update applyRadarFilters to pull jee_repeats
old_apply_filters = '''      const isCbse = currentExam === 'cbse';
      const rawList = isCbse ? (repeatsData.cbse_repeats || []) : (repeatsData.neet_repeats || []);'''

new_apply_filters = '''      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      let rawList = [];
      if (isCbse) rawList = repeatsData.cbse_repeats || [];
      else if (isNeet) rawList = repeatsData.neet_repeats || [];
      else rawList = repeatsData.jee_repeats || [];'''

html = html.replace(old_apply_filters.replace('\r\n', '\n'), new_apply_filters.replace('\r\n', '\n'))

# 8. Update KaTeX delimiters in renderDrillScreen
html = html.replace(
    "delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}],",
    "delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}, {left: '\\\\(', right: '\\\\)', display: false}, {left: '\\\\[', right: '\\\\]', display: true}],"
)

with open('repeated/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("repeated/index.html updated successfully with complete JEE Main Recurrence Radar!")
