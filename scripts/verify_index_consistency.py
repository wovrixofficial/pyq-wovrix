import re

INDEX_PATH = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\index.html"

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# 1. Check all chapters meta
chapter_matches = re.findall(
    r'<div class="ch-info">\s*<h3>(.*?)</h3>\s*<span class="ch-meta">(\d+)\s+distinct problems\s+•\s+(\d+)\s+appearances</span>\s*</div>',
    html
)

print(f"Total Chapter Cards found: {len(chapter_matches)} (Expected: 37)")
if len(chapter_matches) != 37:
    errors.append(f"Expected 37 chapter cards, found {len(chapter_matches)}")

sum_distinct = sum(int(m[1]) for m in chapter_matches)
sum_appearances = sum(int(m[2]) for m in chapter_matches)

print(f"Sum of Chapter Distinct Problems: {sum_distinct} (Expected: 7761)")
print(f"Sum of Chapter Appearances: {sum_appearances} (Expected: 10279)")

if sum_distinct != 7761:
    errors.append(f"Distinct sum mismatch: got {sum_distinct}, expected 7761")
if sum_appearances != 10279:
    errors.append(f"Appearances sum mismatch: got {sum_appearances}, expected 10279")

# 2. Check distinct <= appearances for every chapter
for title, dist, app in chapter_matches:
    d = int(dist)
    a = int(app)
    if d > a:
        errors.append(f"Chapter '{title}' has distinct ({d}) > appearances ({a})! Impossible!")
    elif d == 0 or a == 0:
        errors.append(f"Chapter '{title}' has 0 count!")

# 3. Check Hero and Chips
hero_lead_m = re.search(r'<strong>(10,279) official CBSE board question appearances</strong> \(deduplicated into <strong>(7,761) canonical PYQs</strong>\)', html)
if not hero_lead_m:
    errors.append("Hero lead numbers do not match 10,279 and 7,761!")

chip_m = re.search(r'CBSE 12 PCM \(10,279 Qs • 7,761 Canonical\)', html)
if not chip_m:
    errors.append("Portal chip numbers do not match 10,279 and 7,761!")

# 4. Check Subject Badges
subj_badges = re.findall(r'<span class="subj-badge">([\d,]+)\s+Questions\s+\(([\d,]+)\s+Distinct\)</span>', html)
print(f"Subject badges found: {subj_badges}")
expected_subj = [("3,258", "2,355"), ("3,023", "2,423"), ("3,998", "2,983")]
if subj_badges != expected_subj:
    errors.append(f"Subject badges do not match expected {expected_subj}! Got {subj_badges}")

# 5. Check FAQ
if "11 complete exam cycles from 2016 through 2026. This encompasses 8,089" in html:
    errors.append("FAQ contains outdated 11 cycles / 8,089 text!")

if "Are the step-marking rubrics official?" in html:
    errors.append("FAQ still has risky 'rubrics official' question title!")

if "follow CBSE's official marking pattern" not in html and "follows CBSE's official marking pattern" not in html:
    errors.append("FAQ does not state 'follow CBSE's official marking pattern'!")

# 6. Check Footer Links
footer_med = re.search(r'<span class="footer-col-heading">Medical Entrance</span>[\s\S]*?</ul>', html)
if not footer_med:
    errors.append("Medical Entrance footer section not found!")
else:
    footer_neet_links = re.findall(r'href="([^"]+)"', footer_med.group(0))
    print(f"Footer Medical Entrance links ({len(footer_neet_links)}): {footer_neet_links}")
    if len(footer_neet_links) != len(set(footer_neet_links)):
        errors.append(f"Medical Entrance footer links have duplicates: {footer_neet_links}")
    expected_links = [
        "/practice/?exam=neet",
        "/practice/?exam=neet&subject=Physics",
        "/practice/?exam=neet&subject=Chemistry",
        "/practice/?exam=neet&subject=Botany",
        "/practice/?exam=neet&subject=Zoology"
    ]
    if footer_neet_links != expected_links:
        errors.append(f"Medical Entrance footer links {footer_neet_links} != {expected_links}")

if '<li><a href="/practice/">Parallel Set Comparison</a></li>' in html:
    errors.append("Parallel Set Comparison still points to generic /practice/!")

if errors:
    print(f"\nFAILED with {len(errors)} errors:")
    for e in errors:
        print(f"  ❌ {e}")
    exit(1)
else:
    print("\n✅ ALL AUDIT GATES PASSED PERFECTLY! 100% MATHEMATICAL & EDITORIAL INTEGRITY.")
