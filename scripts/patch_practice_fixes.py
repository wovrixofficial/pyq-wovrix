import re

HTML_PATH = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\practice\index.html"
FOOTER_PATH = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\scripts\homepage_footer.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

with open(FOOTER_PATH, "r", encoding="utf-8") as f:
    homepage_footer = f.read()

# 1. Replace router subject normalization
old_subj_norm = """      if (urlSubj) {
        currentSubject = urlSubj.charAt(0).toUpperCase() + urlSubj.slice(1).toLowerCase();
      }"""

new_subj_norm = """      if (urlSubj) {
        const canonicalList = [
          'Physics', 'Chemistry', 'Mathematics', 'Biology', 'Botany', 'Zoology',
          'English Proficiency', 'Logical Reasoning', 'Computer Science', 'English Core',
          'Social Science', 'Science', 'English Language & Literature'
        ];
        const clean = decodeURIComponent(urlSubj).trim();
        if (clean.toLowerCase().includes('english') && clean.toLowerCase().includes('logic')) {
          currentSubject = 'English Proficiency';
        } else if (clean.toLowerCase().includes('botany')) {
          currentSubject = 'Botany';
        } else if (clean.toLowerCase().includes('zoology')) {
          currentSubject = 'Zoology';
        } else {
          const found = canonicalList.find(s => s.toLowerCase() === clean.toLowerCase());
          currentSubject = found || (clean.charAt(0).toUpperCase() + clean.slice(1));
        }
      }"""

assert old_subj_norm in html, "Could not find old_subj_norm in practice/index.html"
html = html.replace(old_subj_norm, new_subj_norm, 1)

# 2. Fix subtitle in renderSubjectScreen
old_sub_subtitle = """      document.getElementById('subjStageSubtitle').innerText = isCbse
        ? 'Choose Physics, Chemistry, or Mathematics to practice board questions with step-wise derivations.'
        : (isNeet ? 'Choose Physics, Chemistry, Botany, or Zoology with verified NTA answer keys.' : 'Choose Physics, Chemistry, or Mathematics with official NTA answer keys, MCQs and NVQs.');"""

new_sub_subtitle = """      if (currentExam === 'cbse') {
        document.getElementById('subjStageSubtitle').innerText = 'Choose Physics, Chemistry, or Mathematics to practice board questions with step-wise derivations.';
      } else if (currentExam === 'neet') {
        document.getElementById('subjStageSubtitle').innerText = 'Choose Physics, Chemistry, Botany, or Zoology with verified NTA answer keys.';
      } else if (currentExam === 'bitsat') {
        document.getElementById('subjStageSubtitle').innerText = 'Choose Physics, Chemistry, Mathematics, English Proficiency, or Logical Reasoning for BITSAT speed drills.';
      } else if (currentExam === 'jee-adv') {
        document.getElementById('subjStageSubtitle').innerText = 'Choose Physics, Chemistry, or Mathematics with official IIT JEE Advanced question papers.';
      } else {
        document.getElementById('subjStageSubtitle').innerText = 'Choose Physics, Chemistry, or Mathematics with official NTA answer keys, MCQs and NVQs.';
      }"""

assert old_sub_subtitle in html, "Could not find old_sub_subtitle in practice/index.html"
html = html.replace(old_sub_subtitle, new_sub_subtitle, 1)

# 3. Fix label in renderChapterScreen
old_chapter_heading = """      const isCbse = currentExam === 'cbse';
      const isNeet = currentExam === 'neet';
      const label = isCbse ? 'CBSE 12' : (isNeet ? 'NEET UG' : 'JEE Main');
      document.getElementById('chapterStageHeading').innerText = `${currentSubject} Chapters (${label})`;"""

new_chapter_heading = """      const examLabels = {
        'cbse': 'CBSE 12',
        'neet': 'NEET UG',
        'jee': 'JEE Main',
        'jee-adv': 'JEE Advanced',
        'bitsat': 'BITSAT'
      };
      const label = examLabels[currentExam] || 'CBSE 12';
      document.getElementById('chapterStageHeading').innerText = `${currentSubject} Chapters (${label})`;"""

assert old_chapter_heading in html, "Could not find old_chapter_heading in practice/index.html"
html = html.replace(old_chapter_heading, new_chapter_heading, 1)

# 4. Fix filterChapterCards NEET subject lookup
old_neet_lookup = """      let list = [];
      if (currentExam === 'cbse') list = CHAPTERS_CBSE[currentSubject];
      else if (currentExam === 'neet') list = CHAPTERS_NEET[currentSubject];"""

new_neet_lookup = """      let list = [];
      if (currentExam === 'cbse') list = CHAPTERS_CBSE[currentSubject];
      else if (currentExam === 'neet') {
        const k = currentSubject.includes('Botany') ? 'Botany' : (currentSubject.includes('Zoology') ? 'Zoology' : currentSubject);
        list = CHAPTERS_NEET[k] || CHAPTERS_NEET[currentSubject] || [];
      }"""

assert old_neet_lookup in html, "Could not find old_neet_lookup in practice/index.html"
html = html.replace(old_neet_lookup, new_neet_lookup, 1)

# 5. Fix chapter matching in applyStreamFilters
old_stream_match = """          const normTarget = currentChapter.toLowerCase().replace(/\(.*?\)/g, '').replace(/&/g, 'and').replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();
          list = list.filter(q => {
            const raw = (q.ncert_chapter || '').toLowerCase();
            if (raw.includes(currentChapter.toLowerCase())) return true;
            const normRaw = raw.replace(/\(.*?\)/g, '').replace(/&/g, 'and').replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();
            return normRaw.includes(normTarget) || normTarget.includes(normRaw);
          });"""

new_stream_match = """          const normTarget = currentChapter.toLowerCase().replace(/\(.*?\)/g, '').replace(/&/g, 'and').replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();
          const targetWords = normTarget.split(' ').filter(w => w.length > 2);
          list = list.filter(q => {
            const raw = (q.ncert_chapter || q.chapter_name || q.chapter || '').toLowerCase();
            if (raw.includes(currentChapter.toLowerCase())) return true;
            const normRaw = raw.replace(/\(.*?\)/g, '').replace(/&/g, 'and').replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();
            if (normRaw.includes(normTarget) || normTarget.includes(normRaw)) return true;
            const matchCount = targetWords.filter(w => normRaw.includes(w)).length;
            return matchCount >= Math.min(2, targetWords.length);
          });"""

assert old_stream_match in html, "Could not find old_stream_match in practice/index.html"
html = html.replace(old_stream_match, new_stream_match, 1)

# 6. Replace practice footer with exact homepage footer
html = re.sub(r'<footer class="site-footer">[\s\S]*?</footer>', homepage_footer, html)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("practice/index.html patched with 100% precision!")
