with open('repeated/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''      let optionsHtml = '';
      if (q.options && typeof q.options === 'object') {
        optionsHtml = '<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin:14px 0;">';
        ['A', 'B', 'C', 'D'].forEach(opt => {
          if (q.options[opt]) {
            const isCorrect = q.correct_answer === opt;
            optionsHtml += `
              <div style="background:${isCorrect ? '#ecfdf5' : 'var(--surface-alt)'}; border:1px solid ${isCorrect ? '#059669' : 'var(--border)'}; padding:10px 14px; border-radius:6px; font-size:14px;">
                <strong>(${opt})</strong> ${escapeHtml(q.options[opt])}
                ${isCorrect ? '<span style="color:#059669; font-weight:800; float:right;">✓ Official Key</span>' : ''}
              </div>
            `;
          }
        });
        optionsHtml += '</div>';
      }'''

replacement = '''      let optionsHtml = '';
      if (q.options && typeof q.options === 'object') {
        optionsHtml = '<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin:14px 0;">';
        const keysToUse = ['1', '2', '3', '4'].some(k => k in q.options) ? ['1', '2', '3', '4'] : ['A', 'B', 'C', 'D'];
        keysToUse.forEach(opt => {
          if (q.options[opt]) {
            const isCorrect = String(q.correct_answer) === String(opt);
            optionsHtml += `
              <div style="background:${isCorrect ? '#ecfdf5' : 'var(--surface-alt)'}; border:1px solid ${isCorrect ? '#059669' : 'var(--border)'}; padding:10px 14px; border-radius:6px; font-size:14px;">
                <strong>(${opt})</strong> <span class="math-content">${q.options[opt]}</span>
                ${isCorrect ? '<span style="color:#059669; font-weight:800; float:right;">✓ Official Key</span>' : ''}
              </div>
            `;
          }
        });
        optionsHtml += '</div>';
      }'''

if target in text:
    text = text.replace(target, replacement)
    with open('repeated/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated options handling in repeated/index.html")
else:
    print("Target not found for options handling")
