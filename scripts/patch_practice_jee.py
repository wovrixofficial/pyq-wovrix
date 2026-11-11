import os

path = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\practice\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add JEE Main card in exam-select-grid
target_neet_end = """        <!-- NEET Card -->
        <div class="exam-track-card" onclick="selectExamTrack('neet')">
          <div class="exam-track-icon">🩺</div>
          <h2 class="exam-track-title">NEET UG Medical Entrance</h2>
          <p class="exam-track-desc">
            2,060 genuine questions (2016–2026) from 11-year national papers with verified NTA answer keys, 135 diagrams, and +4 / -1 scoring rules.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (520 Qs)</span>
            <span class="exam-pill-item">Chemistry (520 Qs)</span>
            <span class="exam-pill-item">Botany (520 Qs)</span>
            <span class="exam-pill-item">Zoology (500 Qs)</span>
          </div>
          <button class="btn-select-track">
            <span>Select NEET Medical Track</span>
            <span>➔</span>
          </button>
        </div>"""

replacement_with_jee = """        <!-- NEET Card -->
        <div class="exam-track-card" onclick="selectExamTrack('neet')">
          <div class="exam-track-icon">🩺</div>
          <h2 class="exam-track-title">NEET UG Medical Entrance</h2>
          <p class="exam-track-desc">
            2,060 genuine questions (2016–2026) from 11-year national papers with verified NTA answer keys, 135 diagrams, and +4 / -1 scoring rules.
          </p>
          <div class="exam-track-pills">
            <span class="exam-pill-item">Physics (520 Qs)</span>
            <span class="exam-pill-item">Chemistry (520 Qs)</span>
            <span class="exam-pill-item">Botany (520 Qs)</span>
            <span class="exam-pill-item">Zoology (500 Qs)</span>
          </div>
          <button class="btn-select-track">
            <span>Select NEET Medical Track</span>
            <span>➔</span>
          </button>
        </div>

        <!-- JEE Main Card -->
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

if target_neet_end in text:
    text = text.replace(target_neet_end, replacement_with_jee)
    print("Added JEE Main card to exam-select-grid!")
else:
    print("Warning: target_neet_end not found!")

# 2. Add JEE Main button in drawer goal box
drawer_goals_old = """      <div class="drawer-goal-options">
        <button class="drawer-goal-btn goal-toggle-pill active" data-goal="cbse" onclick="selectGoal('cbse')">🎯 CBSE 12</button>
        <button class="drawer-goal-btn goal-toggle-pill" data-goal="neet" onclick="selectGoal('neet')">🩺 NEET UG</button>
      </div>"""

drawer_goals_new = """      <div class="drawer-goal-options">
        <button class="drawer-goal-btn goal-toggle-pill active" data-goal="cbse" onclick="selectGoal('cbse')">🎯 CBSE 12</button>
        <button class="drawer-goal-btn goal-toggle-pill" data-goal="neet" onclick="selectGoal('neet')">🩺 NEET UG</button>
        <a href="/jee/" class="drawer-goal-btn goal-toggle-pill" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center;">⚡ JEE Main</a>
      </div>"""

if drawer_goals_old in text:
    text = text.replace(drawer_goals_old, drawer_goals_new)
    print("Added JEE Main to drawer goal options!")

# 3. Add JEE Main to drawer nav list
drawer_nav_old = """    <nav class="drawer-nav-list">
      <a href="/practice/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">"""

drawer_nav_new = """    <nav class="drawer-nav-list">
      <a href="/jee/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">⚡</span>
        <div>
          <div>JEE Main 5-Year Archive (101 Shifts)</div>
          <span class="drawer-nav-desc">7,880 Questions (2022–2026) with CBT Simulator</span>
        </div>
      </a>
      <a href="/practice/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">"""

if drawer_nav_old in text:
    text = text.replace(drawer_nav_old, drawer_nav_new)
    print("Added JEE Main to drawer navigation list!")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated practice/index.html successfully!")
