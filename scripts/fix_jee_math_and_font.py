import os

p = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\jee\index.html"
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update CSS: improve font, math rendering, and dark mode styles
old_css_block = """    .q-body {
      font-size: 15px;
      line-height: 1.6;
      color: var(--text);
      margin-bottom: 18px;
      white-space: pre-wrap;
      font-family: inherit;
    }

    .opt-btn {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px 14px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--surface);
      cursor: pointer;
      font-size: 14px;
      color: var(--text);
      text-align: left;
      transition: all 0.15s ease;
    }

    .opt-btn:hover {
      background: var(--surface-alt);
    }

    .opt-btn.correct {
      background: #ecfdf5;
      border-color: #10b981;
      color: #065f46;
      font-weight: 600;
    }

    .opt-btn.wrong {
      background: #fef2f2;
      border-color: #ef4444;
      color: #991b1b;
    }

    .opt-tag {
      font-family: var(--font-mono);
      font-weight: 700;
      background: var(--surface-alt);
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 12px;
      flex-shrink: 0;
    }

    /* Numerical input container */
    .nvq-box {
      display: flex;
      gap: 10px;
      align-items: center;
      margin-bottom: 16px;
      max-width: 320px;
    }

    .nvq-input {
      flex: 1;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 700;
      outline: none;
    }

    .q-sol-pane {
      display: none;
      margin-top: 16px;
      padding: 16px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-md);
      font-size: 13px;
      color: #334155;
      line-height: 1.6;
      white-space: pre-wrap;
    }

    .q-sol-pane.open {
      display: block;
    }"""

new_css_block = """    .q-body {
      font-size: 15.5px;
      line-height: 1.7;
      color: var(--text);
      margin-bottom: 18px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    .opt-btn {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--surface);
      cursor: pointer;
      font-size: 14.5px;
      line-height: 1.5;
      color: var(--text);
      text-align: left;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .opt-btn:hover {
      background: var(--surface-alt);
      border-color: var(--accent);
    }

    .opt-btn.correct {
      background: #ecfdf5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 700;
    }

    .opt-btn.wrong {
      background: #fef2f2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
    }

    .opt-tag {
      font-family: var(--font-mono);
      font-weight: 800;
      background: var(--surface-alt);
      border: 1px solid var(--border);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 12px;
      flex-shrink: 0;
    }

    .opt-text {
      flex: 1;
      font-size: 14.5px;
    }

    /* Numerical input container */
    .nvq-box {
      display: flex;
      gap: 10px;
      align-items: center;
      margin-bottom: 16px;
      max-width: 320px;
    }

    .nvq-input {
      flex: 1;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 700;
      outline: none;
      background: var(--surface);
      color: var(--text);
    }

    .q-sol-pane {
      display: none;
      margin-top: 16px;
      padding: 18px 20px;
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      font-size: 14px;
      color: var(--text);
      line-height: 1.7;
    }

    .q-sol-pane.open {
      display: block;
    }

    /* Dark Mode Tokens */
    [data-theme="dark"] .q-sol-pane {
      background: #111827;
      border-color: #374151;
      color: #f3f4f6;
    }

    [data-theme="dark"] .opt-btn {
      background: #111827;
      border-color: #374151;
      color: #f3f4f6;
    }

    [data-theme="dark"] .opt-btn:hover {
      background: #1f2937;
      border-color: #60a5fa;
    }

    [data-theme="dark"] .opt-btn.correct {
      background: rgba(16, 185, 129, 0.22) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
    }

    [data-theme="dark"] .opt-btn.wrong {
      background: rgba(239, 68, 68, 0.22) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
    }

    /* KaTeX equation overflow guard */
    .katex-display {
      overflow-x: auto;
      overflow-y: hidden;
      padding: 6px 0;
    }"""

if old_css_block in text:
    text = text.replace(old_css_block, new_css_block)
    print("Replaced CSS typography and dark mode blocks!")
else:
    print("Warning: old_css_block not found!")

# 2. Update card generation: add math-content class to q-body, opt-text, and q-sol-pane
old_card_gen = """          <div class="q-body">${q.text}</div>

          ${optionsHtml}

          <div class="q-sol-pane ${showSolutionsGlobally ? 'open' : ''}" id="sol_${q.id}">
            <div style="font-weight:700; color:#0f172a; margin-bottom:6px;">
              Official Answer Key: Option (${q.correct_answer || 'N/A'})
            </div>
            ${q.solution || 'Detailed step-by-step solution available in Master Vault.'}
          </div>"""

new_card_gen = """          <div class="q-body math-content">${q.text}</div>

          ${optionsHtml}

          <div class="q-sol-pane math-content ${showSolutionsGlobally ? 'open' : ''}" id="sol_${q.id}">
            <div style="font-weight:800; color:var(--accent); margin-bottom:8px; font-size:13.5px;">
              ✓ Official Answer Key: Option (${q.correct_answer || 'N/A'})
            </div>
            <div style="line-height:1.7;">${q.solution || 'Official evaluation key and derivation steps.'}</div>
          </div>"""

if old_card_gen in text:
    text = text.replace(old_card_gen, new_card_gen)
    print("Updated card generation with math-content classes!")
else:
    print("Warning: old_card_gen not found!")

# 3. Update options rendering: add opt-text math-content
old_opt_gen = """                <button class="opt-btn" onclick="checkOption('${q.id}', '${k}', '${q.correct_answer}', this)">
                  <span class="opt-tag">(${k})</span>
                  <span>${q.options[k]}</span>
                </button>"""

new_opt_gen = """                <button class="opt-btn" onclick="checkOption('${q.id}', '${k}', '${q.correct_answer}', this)">
                  <span class="opt-tag">(${k})</span>
                  <span class="opt-text math-content">${q.options[k]}</span>
                </button>"""

if old_opt_gen in text:
    text = text.replace(old_opt_gen, new_opt_gen)
    print("Updated options rendering with math-content class!")
else:
    print("Warning: old_opt_gen not found!")

# 4. Add renderMath function and trigger it in renderMore, toggleSolution, toggleAllSolutions
old_render_end = """        container.appendChild(card);
      });

      visibleIndex += nextBatch.length;
      document.getElementById('loadMoreWrap').style.display = (visibleIndex >= FILTERED_QUESTIONS.length) ? 'none' : 'block';
    }"""

new_render_end = """        container.appendChild(card);
      });

      visibleIndex += nextBatch.length;
      document.getElementById('loadMoreWrap').style.display = (visibleIndex >= FILTERED_QUESTIONS.length) ? 'none' : 'block';
      renderMath(container);
    }

    function renderMath(targetEl) {
      const el = targetEl || document.getElementById('questionsStream');
      if (!el) return;
      if (window.renderMathInElement) {
        try {
          renderMathInElement(el, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\\\(', right: '\\\\)', display: false },
              { left: '\\\\[', right: '\\\\]', display: true }
            ],
            throwOnError: false
          });
        } catch (e) {
          console.warn('KaTeX render error:', e);
        }
      } else {
        setTimeout(() => renderMath(el), 120);
      }
    }"""

if old_render_end in text:
    text = text.replace(old_render_end, new_render_end)
    print("Added renderMath helper and container render trigger!")
else:
    print("Warning: old_render_end not found!")

# 5. Update toggleSolution to trigger renderMath when opened
old_toggle_sol = """    function toggleSolution(qid) {
      const pane = document.getElementById(`sol_${qid}`);
      const btnText = document.getElementById(`solBtnText_${qid}`);
      const isOpen = pane.classList.contains('open');
      if (isOpen) {
        pane.classList.remove('open');
        btnText.textContent = 'View Solution';
      } else {
        pane.classList.add('open');
        btnText.textContent = 'Hide Solution';
      }
    }"""

new_toggle_sol = """    function toggleSolution(qid) {
      const pane = document.getElementById(`sol_${qid}`);
      const btnText = document.getElementById(`solBtnText_${qid}`);
      const isOpen = pane.classList.contains('open');
      if (isOpen) {
        pane.classList.remove('open');
        if (btnText) btnText.textContent = 'View Solution';
      } else {
        pane.classList.add('open');
        if (btnText) btnText.textContent = 'Hide Solution';
        renderMath(pane);
      }
    }"""

if old_toggle_sol in text:
    text = text.replace(old_toggle_sol, new_toggle_sol)
    print("Updated toggleSolution to call renderMath!")

# 6. Update toggleAllSolutions to trigger renderMath
old_toggle_all = """    function toggleAllSolutions() {
      showSolutionsGlobally = !showSolutionsGlobally;
      document.querySelectorAll('.q-sol-pane').forEach(p => {
        if (showSolutionsGlobally) p.classList.add('open');
        else p.classList.remove('open');
      });"""

new_toggle_all = """    function toggleAllSolutions() {
      showSolutionsGlobally = !showSolutionsGlobally;
      document.querySelectorAll('.q-sol-pane').forEach(p => {
        if (showSolutionsGlobally) {
          p.classList.add('open');
          renderMath(p);
        } else {
          p.classList.remove('open');
        }
      });"""

if old_toggle_all in text:
    text = text.replace(old_toggle_all, new_toggle_all)
    print("Updated toggleAllSolutions to call renderMath!")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print("Finished fixing math and font rendering in jee/index.html!")
