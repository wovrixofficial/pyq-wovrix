with open('repeated/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''        return `
          <div class="repeat-item-card" onclick="openConceptDrill(${idx})">
            <div>
              <div class="repeat-top-bar">
                <span class="repeat-chapter-pill">${escapeHtml(chName)}</span>
                <span class="repeat-badge-hero">🔥 ${rep}x Tested</span>
              </div>
              <h3 class="repeat-concept-title">${escapeHtml(title)}</h3>
              ${tierBadge}
              <div class="repeat-years-row">
                ${years.slice(0, 6).map(y => `<span class="repeat-year-chip">${y}</span>`).join('')}
                ${years.length > 6 ? `<span class="repeat-year-chip">+${years.length - 6} more</span>` : ''}
              </div>
            </div>
            <div class="repeat-card-footer">
              <span>Inspect Question Twins (${twinCount})</span>
              <span>➔</span>
            </div>
          </div>
        `;
      }).join('');'''

replacement = '''        const formulaHtml = item.formula ? `<div class="math-content" style="background:var(--surface-alt); padding:8px 12px; border-radius:6px; font-size:13px; margin:8px 0; overflow-x:auto;">$$${item.formula}$$</div>` : '';

        return `
          <div class="repeat-item-card" onclick="openConceptDrill(${idx})">
            <div>
              <div class="repeat-top-bar">
                <span class="repeat-chapter-pill">${escapeHtml(chName)}</span>
                <span class="repeat-badge-hero">🔥 ${rep}x Tested</span>
              </div>
              <h3 class="repeat-concept-title">${escapeHtml(title)}</h3>
              ${formulaHtml}
              ${tierBadge}
              <div class="repeat-years-row">
                ${years.slice(0, 6).map(y => `<span class="repeat-year-chip">${y}</span>`).join('')}
                ${years.length > 6 ? `<span class="repeat-year-chip">+${years.length - 6} more</span>` : ''}
              </div>
            </div>
            <div class="repeat-card-footer">
              <span>Inspect Question Twins (${twinCount})</span>
              <span>➔</span>
            </div>
          </div>
        `;
      }).join('');

      if (window.renderMathInElement) {
        renderMathInElement(container, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\\\(', right: '\\\\)', display: false },
            { left: '\\\\[', right: '\\\\]', display: true }
          ],
          throwOnError: false
        });
      }'''

if target in text:
    text = text.replace(target, replacement)
    with open('repeated/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully inserted formula rendering in repeated/index.html!")
else:
    print("Target string not found in repeated/index.html")
