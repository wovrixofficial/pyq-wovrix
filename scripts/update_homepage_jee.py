with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update title and meta
html = html.replace(
    '<title>Learnosha | CBSE Class 12 PCM (5-Year) & NEET UG (11-Year) Master Archive</title>',
    '<title>Learnosha | CBSE Class 12, NEET UG & JEE Main Master Past Paper Archive (24,994 Qs)</title>'
)
html = html.replace(
    'content="Previous-year questions archive for CBSE Class 12 PCM (2022–2026, 10,279 questions) and NEET UG (2016–2026, 2,060 questions).',
    'content="Previous-year questions archive for CBSE Class 12 PCM (10,279 Qs), NEET UG (2,060 Qs), and JEE Main (12,667 Qs across 186 shifts from 2019–2026).'
)
html = html.replace(
    '<meta property="og:title" content="Learnosha | CBSE Class 12 PCM (5-Year) & NEET UG (11-Year) Master Archive">',
    '<meta property="og:title" content="Learnosha | CBSE Class 12, NEET UG & JEE Main Master Past Paper Archive (24,994 Qs)">'
)
html = html.replace(
    '<meta name="twitter:title" content="Learnosha | CBSE Class 12 PCM (5-Year) & NEET UG (11-Year) Master Archive">',
    '<meta name="twitter:title" content="Learnosha | CBSE Class 12, NEET UG & JEE Main Master Past Paper Archive (24,994 Qs)">'
)

# 2. Update Hero section
html = html.replace(
    '<span>CBSE CLASS 12 PCM & NEET UG MASTER ARCHIVE</span>',
    '<span>CBSE CLASS 12 PCM • NEET UG • JEE MAIN 8-YEAR MASTER ARCHIVE</span>'
)
old_hero_lead = '''        <p class="hero-editorial-lead">
          <strong>10,279 official CBSE board question appearances</strong> (deduplicated into <strong>7,761 canonical PYQs</strong>) across 5 years (2022–2026) and <strong>2,060 verified NEET UG problems</strong> across 11 years (2016–2026). Pure NCERT alignment, multi-year frequency filters, and zero distractions.
        </p>'''
new_hero_lead = '''        <p class="hero-editorial-lead">
          <strong>10,279 official CBSE board question appearances</strong> (2022–2026), <strong>2,060 verified NEET UG problems</strong> (2016–2026), and <strong>12,667 authentic JEE Main questions</strong> across 186 official shifts (2019–2026). Pure NCERT alignment, multi-year frequency filters, and zero distractions.
        </p>'''
html = html.replace(old_hero_lead, new_hero_lead)

# 3. Update drawer goal options
old_drawer_jee = '<a href="/jee/" class="drawer-goal-btn goal-toggle-pill" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center;">⚡ JEE Main</a>'
new_drawer_jee = '<button class="drawer-goal-btn goal-toggle-pill" data-goal="jee" onclick="selectGoal(\'jee\')">⚡ JEE Main</button>'
html = html.replace(old_drawer_jee, new_drawer_jee)

# 4. Update drawer nav item
html = html.replace(
    '<div>JEE Main 2024 (20 Shifts)</div>',
    '<div>JEE Main 8-Year Archive (186 Shifts)</div>'
)

# 5. Update Practice Hub pillar card chip
html = html.replace(
    '<a href="/jee/" class="portal-chip" style="background:#eff6ff; color:#1d4ed8; font-weight:700;">⚡ JEE Main (1,786 Qs)</a>',
    '<a href="/practice/?exam=jee" class="portal-chip" style="background:#eff6ff; color:#1d4ed8; font-weight:700;">⚡ JEE Main (12,667 Qs • 186 Shifts)</a>'
)

# 6. Update Repeats Radar pillar card chips
html = html.replace(
    '<span class="portal-chip">140 NEET Concept Clusters</span>\n            <span class="portal-chip">1,792 CBSE Clusters</span>\n            <span class="portal-chip">Historical Twin Linking</span>',
    '<span class="portal-chip">22 JEE Core Archetypes (302x)</span>\n            <span class="portal-chip">1,792 CBSE Clusters</span>\n            <span class="portal-chip">140 NEET Concept Clusters</span>'
)

# 7. Add JEE Track Button to Bento switcher
old_bento_switcher = '''        <div class="bento-track-switcher-centered">
          <button id="bentoCbseBtn" class="bento-track-btn active" onclick="switchRecurrenceTrack('cbse')">
            <span>🎯 CBSE Class 12</span>
            <span class="track-badge">1,792 Clones</span>
          </button>
          <button id="bentoNeetBtn" class="bento-track-btn" onclick="switchRecurrenceTrack('neet')">
            <span>🩺 NEET UG Medical</span>
            <span class="track-badge">140 Clusters</span>
          </button>
        </div>'''

new_bento_switcher = '''        <div class="bento-track-switcher-centered">
          <button id="bentoJeeBtn" class="bento-track-btn active" onclick="switchRecurrenceTrack('jee')">
            <span>⚡ JEE Main Entrance</span>
            <span class="track-badge">22 Archetypes (302x)</span>
          </button>
          <button id="bentoCbseBtn" class="bento-track-btn" onclick="switchRecurrenceTrack('cbse')">
            <span>🎯 CBSE Class 12</span>
            <span class="track-badge">1,792 Clones</span>
          </button>
          <button id="bentoNeetBtn" class="bento-track-btn" onclick="switchRecurrenceTrack('neet')">
            <span>🩺 NEET UG Medical</span>
            <span class="track-badge">140 Clusters</span>
          </button>
        </div>'''

html = html.replace(old_bento_switcher, new_bento_switcher)

# 8. Add JEE Bento Grid markup before CBSE grid
jee_bento_grid = '''      <!-- JEE Main Repeats Grid (Default) -->
      <div id="recurrenceJeeGrid" class="bento-grid">
        <!-- Card 1: Math King's Property -->
        <div class="bento-repeat-card">
          <div class="bento-card-top">
            <span class="bento-freq-badge purple">⚡ 8 OF 8 YEARS • 302x FREQUENCY</span>
            <span class="bento-subj-pill">Mathematics • 4 Marks</span>
          </div>
          <h3 class="bento-concept-title">King's Property & Symmetry in Definite Integrals</h3>
          <div class="math-content" style="background:var(--surface-alt); padding:8px 12px; border-radius:6px; font-size:13.5px; margin:10px 0; overflow-x:auto;">
            $$\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx$$
          </div>
          <p class="bento-question-text">
            Tested across 186 shifts from 2019 to 2026. Fundamental symmetry property converting complex trigonometric/logarithmic numerators into cancelled constant integrands.
          </p>
          <div class="bento-years-chips-row">
            <span class="bento-years-label">Tested Shifts:</span>
            <span class="bento-chip">2026</span>
            <span class="bento-chip">2025</span>
            <span class="bento-chip">2024</span>
            <span class="bento-chip">2023</span>
            <span class="bento-chip">2022</span>
            <span class="bento-chip">2021</span>
            <span class="bento-chip">+180 Shifts</span>
          </div>
          <a href="/repeated/?exam=jee&subject=Mathematics" class="bento-card-action">
            <span>Explore 302x Integrals Pattern</span>
            <span>➔</span>
          </a>
        </div>

        <!-- Card 2: Physics Dielectrics -->
        <div class="bento-repeat-card">
          <div class="bento-card-top">
            <span class="bento-freq-badge">⚡ 8 OF 8 YEARS • 258x FREQUENCY</span>
            <span class="bento-subj-pill">Physics • 4 Marks</span>
          </div>
          <h3 class="bento-concept-title">Capacitors with Dielectric Slabs & Stored Energy</h3>
          <div class="math-content" style="background:var(--surface-alt); padding:8px 12px; border-radius:6px; font-size:13.5px; margin:10px 0; overflow-x:auto;">
            $$C' = \\frac{\\epsilon_0 A}{(d-t) + \\frac{t}{K}},\\quad U = \\frac{1}{2}CV^2$$
          </div>
          <p class="bento-question-text">
            Appearing in nearly every JEE Main shift. Inserting dielectric slab with battery connected vs disconnected, electric field shifts, and electrostatic force between plates.
          </p>
          <div class="bento-years-chips-row">
            <span class="bento-years-label">Tested Shifts:</span>
            <span class="bento-chip">2026</span>
            <span class="bento-chip">2025</span>
            <span class="bento-chip">2024</span>
            <span class="bento-chip">2023</span>
            <span class="bento-chip">2022</span>
            <span class="bento-chip">+180 Shifts</span>
          </div>
          <a href="/repeated/?exam=jee&subject=Physics" class="bento-card-action">
            <span>Explore 258x Capacitance Pattern</span>
            <span>➔</span>
          </a>
        </div>

        <!-- Card 3: Chemistry CFSE -->
        <div class="bento-repeat-card">
          <div class="bento-card-top">
            <span class="bento-freq-badge blue">⚡ 8 OF 8 YEARS • 183x FREQUENCY</span>
            <span class="bento-subj-pill">Chemistry • 4 Marks</span>
          </div>
          <h3 class="bento-concept-title">Crystal Field Stabilization Energy (CFSE) & Magnetic Moment</h3>
          <div class="math-content" style="background:var(--surface-alt); padding:8px 12px; border-radius:6px; font-size:13.5px; margin:10px 0; overflow-x:auto;">
            $$\\mu = \\sqrt{n(n+2)}\\text{ BM},\\quad \\Delta_o > P\\text{ (Low Spin)}$$
          </div>
          <p class="bento-question-text">
            High vs low spin octahedral complexes, pairing energy comparison, spectrochemical series ligand strength, and spin-only magnetic moments.
          </p>
          <div class="bento-years-chips-row">
            <span class="bento-years-label">Tested Shifts:</span>
            <span class="bento-chip">2026</span>
            <span class="bento-chip">2025</span>
            <span class="bento-chip">2024</span>
            <span class="bento-chip">2023</span>
            <span class="bento-chip">2022</span>
            <span class="bento-chip">+180 Shifts</span>
          </div>
          <a href="/repeated/?exam=jee&subject=Chemistry" class="bento-card-action">
            <span>Explore 183x Coordination Pattern</span>
            <span>➔</span>
          </a>
        </div>
      </div>
'''

html = html.replace(
    '<!-- CBSE Repeats Grid (Default) -->\n      <div id="recurrenceCbseGrid" class="bento-grid">',
    jee_bento_grid + '\n      <!-- CBSE Repeats Grid -->\n      <div id="recurrenceCbseGrid" class="bento-grid" style="display:none;">'
)

# 9. Update switchRecurrenceTrack function in JS
old_switch_func = '''  function switchRecurrenceTrack(track) {
    const isCbse = track === 'cbse';
    const cbseBtn = document.getElementById('bentoCbseBtn');
    const neetBtn = document.getElementById('bentoNeetBtn');
    const cbseGrid = document.getElementById('recurrenceCbseGrid');
    const neetGrid = document.getElementById('recurrenceNeetGrid');

    if (cbseBtn) cbseBtn.classList.toggle('active', isCbse);
    if (neetBtn) neetBtn.classList.toggle('active', !isCbse);
    if (cbseGrid) cbseGrid.style.display = isCbse ? 'grid' : 'none';
    if (neetGrid) neetGrid.style.display = isCbse ? 'none' : 'grid';

    if (window.renderMathInElement) {
      const activeEl = isCbse ? cbseGrid : neetGrid;
      if (activeEl) {
        renderMathInElement(activeEl, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ],
          throwOnError: false
        });
      }
    }
  }'''

new_switch_func = '''  function switchRecurrenceTrack(track) {
    const cbseBtn = document.getElementById('bentoCbseBtn');
    const neetBtn = document.getElementById('bentoNeetBtn');
    const jeeBtn = document.getElementById('bentoJeeBtn');
    const cbseGrid = document.getElementById('recurrenceCbseGrid');
    const neetGrid = document.getElementById('recurrenceNeetGrid');
    const jeeGrid = document.getElementById('recurrenceJeeGrid');

    if (cbseBtn) cbseBtn.classList.toggle('active', track === 'cbse');
    if (neetBtn) neetBtn.classList.toggle('active', track === 'neet');
    if (jeeBtn) jeeBtn.classList.toggle('active', track === 'jee');

    if (cbseGrid) cbseGrid.style.display = track === 'cbse' ? 'grid' : 'none';
    if (neetGrid) neetGrid.style.display = track === 'neet' ? 'grid' : 'none';
    if (jeeGrid) jeeGrid.style.display = track === 'jee' ? 'grid' : 'none';

    if (window.renderMathInElement) {
      const activeEl = track === 'cbse' ? cbseGrid : (track === 'neet' ? neetGrid : jeeGrid);
      if (activeEl) {
        renderMathInElement(activeEl, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\\\(", right: "\\\\)", display: false },
            { left: "\\\\[", right: "\\\\]", display: true }
          ],
          throwOnError: false
        });
      }
    }
  }'''

html = html.replace(old_switch_func, new_switch_func)

# 10. Also render math on initial DOM load for the default active Bento grid
html = html.replace(
    "document.addEventListener('DOMContentLoaded', () => {\n    initThreeDHero();\n  });",
    "document.addEventListener('DOMContentLoaded', () => {\n    initThreeDHero();\n    if (window.renderMathInElement) {\n      const activeBento = document.getElementById('recurrenceJeeGrid') || document.getElementById('recurrenceCbseGrid');\n      if (activeBento) renderMathInElement(activeBento, { delimiters: [{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}] });\n    }\n  });"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully with complete JEE Main presence!")
