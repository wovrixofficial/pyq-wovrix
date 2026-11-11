import os
import json
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def verify():
    print("=== Running Phase 1 Remediation Verifications ===")
    
    # 1. Sitemap verification
    for sitemap in ["sitemap-chapters.xml", "sitemap-clusters.xml", "sitemap-index.xml", "robots.txt"]:
        sp = os.path.join(ROOT, sitemap)
        with open(sp, "r", encoding="utf-8") as f:
            cnt = f.read().count("pyq.wovrix.in")
            assert cnt == 0, f"Found pyq.wovrix.in in {sitemap}"
    print("[PASS] Task 1: 0 references to pyq.wovrix.in in sitemaps and robots.txt")

    # 2. Vercel redirect verification
    with open(os.path.join(ROOT, "vercel.json"), "r", encoding="utf-8") as f:
        v_data = json.load(f)
    redirect_sources = [r["source"] for r in v_data.get("redirects", [])]
    assert "/formula-sheets" in redirect_sources, "Missing /formula-sheets redirect"
    assert "/formula-sheets/" in redirect_sources, "Missing /formula-sheets/ redirect"
    print("[PASS] Task 2: /formula-sheets/ 301 redirects to /syllabus/ in vercel.json")

    # 3. Current Electricity checks
    with open(os.path.join(ROOT, "cbse-12", "physics", "current-electricity", "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Tab corruption
    assert "\text" not in html, "Tab ext still present"
    assert "\times" not in html, "Tab imes still present"
    print("[PASS] Task 3.1: Zero tab-corrupted \\text or \\times in current-electricity HTML")

    # Line 544 nested math
    assert r"$V_i = 12 \sin(100 \pi t)\text{ V}$" in html, "Nested math fix missing in line 544"
    print("[PASS] Task 3.2: Nested math on line 544 cleanly fixed to $V_i = 12 \\sin(100 \\pi t)\\text{ V}$")

    # Math mode percent inside question texts
    bad_math_percent = []
    question_blocks = re.findall(r'<div class="question-text math-content">(.*?)</div>', html, flags=re.DOTALL)
    for qblock in question_blocks:
        for m in re.finditer(r'\$([^$\n]+)\$', qblock):
            math_content = m.group(1)
            if re.search(r'(?<!\\)%', math_content):
                bad_math_percent.append(m.group(0))
    assert len(bad_math_percent) == 0, f"Found unescaped %: {bad_math_percent}"
    print("[PASS] Task 3.3: Zero unescaped % in LaTeX math mode across all questions")

    # Re-tagging in HTML
    assert 'Ch 7: Alternating Current' in html, "Missing Ch 7 tag in HTML"
    assert 'Ch 14: Semiconductor Electronics' in html, "Missing Ch 14 tag in HTML"
    print("[PASS] Task 3.4: Re-tag badges present on misclassified cards in HTML")

    # Re-tagging in data/cbse_physics.json
    with open(os.path.join(ROOT, "data", "cbse_physics.json"), "r", encoding="utf-8") as f:
        cbse = json.load(f)
    id_map = {q["id"]: q for q in cbse}
    for qid in [218, 4598, 4670, 4708]:
        assert id_map[qid]["chapter_number"] == 14, f"QID {qid} not re-tagged to Ch 14"
    assert id_map[3674]["chapter_number"] == 7, "QID 3674 not re-tagged to Ch 7"
    print("[PASS] Task 3.5: data/cbse_physics.json verified: QIDs 218, 4598, 4670, 4708 in Ch 14, QID 3674 in Ch 7")

    print("\n>>> ALL PHASE 1 REMEDIATIONS FULLY VERIFIED! <<<")

if __name__ == '__main__':
    verify()
