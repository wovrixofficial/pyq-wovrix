import re

file_path = 'E:/PYQ_Wovrix_Portal/pyq-wovrix/practice/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add global variable
if 'let targetQuestionId = null;' not in code:
    code = code.replace(
        "let currentTopic = 'all';",
        "let currentTopic = 'all';\n    let targetQuestionId = null;"
    )

# 2. Update initRouterFromURL to set targetQuestionId
code = re.sub(
    r'const urlQ = p\.get\(\'q\'\);',
    "const urlQ = p.get('q');\n      targetQuestionId = urlQ ? String(urlQ).trim() : null;",
    code
)

# 3. In applyStreamFilters, add deep link pinning before filteredQuestions = list
pin_logic = """
      // Deep Link Pinning: If targetQuestionId is present, pin that question to index 0
      if (targetQuestionId) {
        const targetQ = loadedQuestions.find(q => String(q.id) === targetQuestionId);
        if (targetQ) {
          targetQ._isPinned = true;
          list = list.filter(q => String(q.id) !== targetQuestionId);
          list.unshift(targetQ);
        }
      }

      filteredQuestions = list;"""

code = code.replace("filteredQuestions = list;", pin_logic, 1)

# 4. In renderStreamQuestionsFeed, inject banner and border highlight
card_template_old = """        html += `
          <div class="question-card" id="${qId}">"""

card_template_new = """        const isPinnedTarget = (targetQuestionId && String(qId) === targetQuestionId) || q._isPinned;
        const pinnedBanner = isPinnedTarget ? `
          <div class="pinned-question-banner" style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:10px 14px; margin-bottom:12px; display:flex; align-items:center; justify-content:space-between; gap:10px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:18px;">🎯</span>
              <div>
                <strong style="color:#1d4ed8; font-size:13px;">Selected Question #${escapeHtml(qId)}</strong>
                <span style="color:#475569; font-size:12px; margin-left:6px;">— Pinned to #1 for direct practice</span>
              </div>
            </div>
            <span style="background:#2563eb; color:#ffffff; font-size:11px; font-weight:700; padding:3px 8px; border-radius:999px;">Direct Match</span>
          </div>
        ` : '';
        const cardStyle = isPinnedTarget ? 'style="border: 2px solid #2563eb; box-shadow: 0 4px 16px rgba(37,99,235,0.18);"' : '';

        html += `
          ${pinnedBanner}
          <div class="question-card" id="${qId}" ${cardStyle}>"""

code = code.replace(card_template_old, card_template_new, 1)

# 5. Add scroll-into-view after rendering questions in feed
scroll_logic = """      // Auto-scroll to pinned target question
      if (targetQuestionId) {
        setTimeout(() => {
          const targetEl = document.getElementById(targetQuestionId) || document.getElementById(`card_${targetQuestionId}`);
          if (targetEl) {
            targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }, 150);
      }
    }"""

code = re.sub(
    r'(renderMathInCard\(.*?\);\s*\}\);\s*\}\s*catch\(.*?\)\{\}\s*\})(\s*\}\s*async function loadMoreQuestionsStream)',
    rf'\1\n{scroll_logic}\n\2',
    code
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("[SUCCESS] Patched practice/index.html with deep linking and question pinning.")
