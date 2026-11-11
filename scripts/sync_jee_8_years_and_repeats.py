import os
import json

ROOT = r"E:\PYQ_Wovrix_Portal\pyq-wovrix"

# =========================================================
# 1. UPDATE JEE/INDEX.HTML TO 8-YEAR (2019-2026, 12,667 QS, 186 SHIFTS)
# =========================================================
jee_html_path = os.path.join(ROOT, "jee", "index.html")
with open(jee_html_path, "r", encoding="utf-8") as f:
    jee_text = f.read()

# Title & Meta
jee_text = jee_text.replace(
    "<title>Learnosha | JEE Main 5-Year Master Shift Archive (2022–2026) & CBT Simulator</title>",
    "<title>Learnosha | JEE Main 8-Year Master Shift Archive (2019–2026) & CBT Simulator</title>"
)
jee_text = jee_text.replace(
    "All 101 official JEE Main shifts from 2022 through 2026. 7,880 authentic questions across Physics, Chemistry, and Mathematics with NTA keys and step-by-step solutions.",
    "All 186 official JEE Main shifts from 2019 through 2026. 12,667 authentic questions across Physics, Chemistry, and Mathematics with NTA keys and step-by-step solutions."
)

# Hero Title & Description
jee_text = jee_text.replace(
    '<h1 class="hero-title">JEE Main Master Shift Archive & CBT Simulator (2022–2026)</h1>',
    '<h1 class="hero-title">JEE Main 8-Year Master Shift Archive & CBT Simulator (2019–2026)</h1>'
)
jee_text = jee_text.replace(
    "Practice across all 101 official shifts conducted by the National Testing Agency (5 complete exam cycles: 2022, 2023, 2024, 2025 & 2026).",
    "Practice across all 186 official shifts conducted by the National Testing Agency (8 complete exam cycles from 2019 through 2026). Featuring authentic questions across Physics, Chemistry, and Mathematics with NTA keys and step-by-step solutions."
)

# KPIs
jee_text = jee_text.replace(
    '<div class="kpi-num" id="kpiTotalQs">7,880</div>',
    '<div class="kpi-num" id="kpiTotalQs">12,667</div>'
)
jee_text = jee_text.replace(
    '<div class="kpi-num">101</div>\n          <div class="kpi-label">Official Shifts</div>',
    '<div class="kpi-num">186</div>\n          <div class="kpi-label">Official Shifts</div>'
)
jee_text = jee_text.replace(
    '<div class="kpi-num">5 Years</div>\n          <div class="kpi-label">2022 • 2023 • 2024 • 2025 • 2026</div>',
    '<div class="kpi-num">8 Years</div>\n          <div class="kpi-label">2019–2026 (186 Shifts)</div>'
)

# Year Switcher Pills (All 8 Years)
old_year_pills = """          <div class="subj-pill-grid" id="yearPillGrid">
            <button class="subj-pill active" onclick="setYear('ALL', this)">All 5 Years (101 Shifts • 7,880 Qs)</button>
            <button class="subj-pill" onclick="setYear('2026', this)">⚡ 2026 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2025', this)">📅 2025 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2024', this)">🎯 2024 (20 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2023', this)">📅 2023 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2022', this)">📅 2022 (24 Shifts)</button>
          </div>"""

new_year_pills = """          <div class="subj-pill-grid" id="yearPillGrid">
            <button class="subj-pill active" onclick="setYear('ALL', this)">All 8 Years (186 Shifts • 12,667 Qs)</button>
            <button class="subj-pill" onclick="setYear('2026', this)">⚡ 2026 (19 Shifts • 1,378 Qs)</button>
            <button class="subj-pill" onclick="setYear('2025', this)">📅 2025 (19 Shifts • 1,326 Qs)</button>
            <button class="subj-pill" onclick="setYear('2024', this)">🎯 2024 (20 Shifts • 1,786 Qs)</button>
            <button class="subj-pill" onclick="setYear('2023', this)">📅 2023 (19 Shifts • 1,390 Qs)</button>
            <button class="subj-pill" onclick="setYear('2022', this)">📅 2022 (24 Shifts • 2,000 Qs)</button>
            <button class="subj-pill" onclick="setYear('2021', this)">📅 2021 (26 Shifts • 2,135 Qs)</button>
            <button class="subj-pill" onclick="setYear('2020', this)">📅 2020 (27 Shifts • 1,142 Qs)</button>
            <button class="subj-pill" onclick="setYear('2019', this)">📅 2019 (32 Shifts • 1,510 Qs)</button>
          </div>"""

if old_year_pills in jee_text:
    jee_text = jee_text.replace(old_year_pills, new_year_pills)
    print("Updated year switcher to all 8 years in jee/index.html")
else:
    print("Warning: old_year_pills exact match not found!")

# Loading state text
jee_text = jee_text.replace("Loading 7,880 verified JEE Main questions...", "Loading 12,667 verified JEE Main questions...")

with open(jee_html_path, "w", encoding="utf-8") as f:
    f.write(jee_text)
print("Saved jee/index.html")


# =========================================================
# 2. UPDATE PRACTICE/INDEX.HTML JEE CARD
# =========================================================
practice_path = os.path.join(ROOT, "practice", "index.html")
with open(practice_path, "r", encoding="utf-8") as f:
    p_text = f.read()

old_p_jee = """        <!-- JEE Main Card -->
        <div class="exam-track-card" onclick="window.location.href='/jee/'">
          <div class="exam-track-icon">⚡</div>
          <h2 class="exam-track-title">JEE Main Engineering Entrance</h2>
          <p class="exam-track-desc">
            7,880 authentic past examination questions (2022–2026) across 101 official NTA shifts with 3-hour CBT mock simulator, numerical value questions (NVQ), and step solutions.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (2,782 Qs)</span>
            <span class="exam-pill-item">Chemistry (2,629 Qs)</span>
            <span class="exam-pill-item">Mathematics (2,469 Qs)</span>
            <span class="exam-pill-item">101 CBT Shifts</span>
          </div>
          <button class="btn-select-track">
            <span>Launch JEE Main CBT Track</span>
            <span>➔</span>
          </button>
        </div>"""

new_p_jee = """        <!-- JEE Main Card -->
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
        </div>"""

if old_p_jee in p_text:
    p_text = p_text.replace(old_p_jee, new_p_jee)
    print("Updated JEE card in practice/index.html to 12,667 questions")
    with open(practice_path, "w", encoding="utf-8") as f:
        f.write(p_text)


# =========================================================
# 3. UPDATE REPEATED/INDEX.HTML (ADD JEE RECURRENCE RADAR CARD)
# =========================================================
repeated_path = os.path.join(ROOT, "repeated", "index.html")
with open(repeated_path, "r", encoding="utf-8") as f:
    rep_text = f.read()

target_neet_rep = """        <div class="exam-track-card" onclick="selectExamTrack('neet')">
          <div class="exam-track-icon">🩺</div>
          <h2 class="exam-track-title">NEET UG 11-Year Master Radar (2016–2026)</h2>
          <p class="exam-track-desc">
            140 comprehensive concept tiers spanning 2016–2026 national papers mapping 2,039 of 2,060 questions to recurring core formula archetypes and biological mechanisms.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (30+ Clusters)</span>
            <span class="exam-pill-item">Chemistry (35+ Clusters)</span>
            <span class="exam-pill-item">Botany (38+ Clusters)</span>
            <span class="exam-pill-item">Zoology (37+ Clusters)</span>
          </div>
          <button class="btn-select-track">
            <span>Explore NEET Medical Repeats</span>
            <span>➔</span>
          </button>
        </div>"""

replacement_with_jee_rep = """        <div class="exam-track-card" onclick="selectExamTrack('neet')">
          <div class="exam-track-icon">🩺</div>
          <h2 class="exam-track-title">NEET UG 11-Year Master Radar (2016–2026)</h2>
          <p class="exam-track-desc">
            140 comprehensive concept tiers spanning 2016–2026 national papers mapping 2,039 of 2,060 questions to recurring core formula archetypes and biological mechanisms.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (30+ Clusters)</span>
            <span class="exam-pill-item">Chemistry (35+ Clusters)</span>
            <span class="exam-pill-item">Botany (38+ Clusters)</span>
            <span class="exam-pill-item">Zoology (37+ Clusters)</span>
          </div>
          <button class="btn-select-track">
            <span>Explore NEET Medical Repeats</span>
            <span>➔</span>
          </button>
        </div>

        <!-- JEE Main Recurrence Radar Card -->
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
        </div>"""

if target_neet_rep in rep_text:
    rep_text = rep_text.replace(target_neet_rep, replacement_with_jee_rep)
    print("Added JEE Main Recurrence Radar card to repeated/index.html")

# Drawer in repeated/index.html
rep_drawer_old = """      <div class="drawer-goal-options">
        <button class="drawer-goal-btn goal-toggle-pill active" data-goal="cbse" onclick="selectGoal('cbse')">🎯 CBSE 12</button>
        <button class="drawer-goal-btn goal-toggle-pill" data-goal="neet" onclick="selectGoal('neet')">🩺 NEET UG</button>
      </div>"""

rep_drawer_new = """      <div class="drawer-goal-options">
        <button class="drawer-goal-btn goal-toggle-pill active" data-goal="cbse" onclick="selectGoal('cbse')">🎯 CBSE 12</button>
        <button class="drawer-goal-btn goal-toggle-pill" data-goal="neet" onclick="selectGoal('neet')">🩺 NEET UG</button>
        <a href="/jee/" class="drawer-goal-btn goal-toggle-pill" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center;">⚡ JEE Main</a>
      </div>"""

if rep_drawer_old in rep_text:
    rep_text = rep_text.replace(rep_drawer_old, rep_drawer_new)

# Drawer nav item in repeated/index.html
rep_nav_old = """    <nav class="drawer-nav-list">
      <a href="/practice/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">"""

rep_nav_new = """    <nav class="drawer-nav-list">
      <a href="/jee/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">⚡</span>
        <div>
          <div>JEE Main 8-Year Archive (186 Shifts)</div>
          <span class="drawer-nav-desc">12,667 Questions (2019–2026) with CBT Simulator</span>
        </div>
      </a>
      <a href="/practice/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">"""

if rep_nav_old in rep_text:
    rep_text = rep_text.replace(rep_nav_old, rep_nav_new)

with open(repeated_path, "w", encoding="utf-8") as f:
    f.write(rep_text)
print("Saved repeated/index.html")

# =========================================================
# 4. UPDATE INDEX.HTML DRAWER & FOOTER
# =========================================================
index_path = os.path.join(ROOT, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_text = f.read()

idx_text = idx_text.replace(
    "<div>JEE Main 5-Year Archive (101 Shifts)</div>\n          <span class=\"drawer-nav-desc\">7,880 Questions (2022–2026) with CBT Simulator</span>",
    "<div>JEE Main 8-Year Archive (186 Shifts)</div>\n          <span class=\"drawer-nav-desc\">12,667 Questions (2019–2026) with CBT Simulator</span>"
)
idx_text = idx_text.replace(
    '<li><a href="/jee/">JEE Main 5-Year CBT Simulator (101 Shifts)</a></li>',
    '<li><a href="/jee/">JEE Main 8-Year CBT Simulator (186 Shifts • 12,667 Qs)</a></li>'
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_text)
print("Saved index.html")
print("=== All 8-Year & Repeated JEE Updates Complete! ===")
