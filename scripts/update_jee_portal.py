import os

p = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\jee\index.html"
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Title & Meta
text = text.replace(
    "<title>Learnosha | JEE Main 2024 Master Shift Archive & CBT Simulator</title>",
    "<title>Learnosha | JEE Main 5-Year Master Shift Archive (2022–2026) & CBT Simulator</title>"
)
text = text.replace(
    "All 20 official JEE Main 2024 shifts (January & April sessions). 1,786 authentic questions across Physics, Chemistry, and Mathematics with NTA keys and full solutions.",
    "All 101 official JEE Main shifts from 2022 through 2026. 7,880 authentic questions across Physics, Chemistry, and Mathematics with NTA keys and step-by-step solutions."
)

# 2. Hero Title & Description
text = text.replace(
    '<h1 class="hero-title">JEE Main Master Shift Archive & CBT Simulator (2024–2026)</h1>',
    '<h1 class="hero-title">JEE Main Master Shift Archive & CBT Simulator (2022–2026)</h1>'
)
text = text.replace(
    "Practice across all 58 official shifts conducted by the National Testing Agency (2024, 2025 & 2026 January and April sessions).",
    "Practice across all 101 official shifts conducted by the National Testing Agency (5 complete exam cycles: 2022, 2023, 2024, 2025 & 2026)."
)

# 3. KPIs
text = text.replace(
    '<div class="kpi-num" id="kpiTotalQs">1,786</div>',
    '<div class="kpi-num" id="kpiTotalQs">7,880</div>'
)
text = text.replace(
    '<div class="kpi-num">58</div>',
    '<div class="kpi-num">101</div>'
)
text = text.replace(
    '<div class="kpi-num">3 Years</div>\n          <div class="kpi-label">2024 • 2025 • 2026</div>',
    '<div class="kpi-num">5 Years</div>\n          <div class="kpi-label">2022 • 2023 • 2024 • 2025 • 2026</div>'
)

# 4. Year Switcher
old_pills = """          <div class="subj-pill-grid" id="yearPillGrid">
            <button class="subj-pill active" onclick="setYear('ALL', this)">All Shifts (58 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2026', this)">⚡ 2026 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2025', this)">📅 2025 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2024', this)">🎯 2024 (20 Shifts)</button>
          </div>"""

new_pills = """          <div class="subj-pill-grid" id="yearPillGrid">
            <button class="subj-pill active" onclick="setYear('ALL', this)">All 5 Years (101 Shifts • 7,880 Qs)</button>
            <button class="subj-pill" onclick="setYear('2026', this)">⚡ 2026 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2025', this)">📅 2025 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2024', this)">🎯 2024 (20 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2023', this)">📅 2023 (19 Shifts)</button>
            <button class="subj-pill" onclick="setYear('2022', this)">📅 2022 (24 Shifts)</button>
          </div>"""

if old_pills in text:
    text = text.replace(old_pills, new_pills)
else:
    print("Warning: old_pills exact match not found!")

# 5. Loading Text
text = text.replace("Loading 1,786 verified JEE Main questions...", "Loading 7,880 verified JEE Main questions...")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated jee/index.html to 5-Year 7,880 questions!")
