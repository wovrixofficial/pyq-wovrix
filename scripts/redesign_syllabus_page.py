import re
import os

HTML_PATH = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\syllabus\index.html"
FOOTER_PATH = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\scripts\homepage_footer.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

with open(FOOTER_PATH, "r", encoding="utf-8") as f:
    homepage_footer = f.read()

# 1. Update Hero Badge & Year
html = re.sub(
    r'<span class="syllabus-badge">[\s\S]*?</span>',
    '<span class="syllabus-badge">📋 OFFICIAL CURRICULUM & WEIGHTAGE BLUEPRINTS • ACADEMIC SESSION 2026–2027</span>',
    html
)
html = html.replace("AY 2025–2026", "Academic Session 2026–2027")
html = html.replace("AY 2025-2026", "Academic Session 2026–2027")
html = html.replace("2025-2026", "2026–2027")
html = html.replace("2025–2026", "2026–2027")
html = html.replace("Circular No. Acad-39/2025", "Official Curriculum Notification 2026–2027")

# 2. Modern, Minimalist, Premium CSS
premium_css = """
    /* Premium Minimalist Track Bar */
    .syllabus-track-bar {
      display: flex;
      gap: 6px;
      background: var(--surface-alt);
      padding: 6px;
      border-radius: 9999px;
      border: 1px solid var(--border);
      max-width: 980px;
      margin: 24px auto 26px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      justify-content: center;
      flex-wrap: wrap;
    }
    .syllabus-track-bar::-webkit-scrollbar {
      display: none;
    }
    .syllabus-track-btn {
      padding: 8px 16px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-muted);
      background: transparent;
      border: none;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .syllabus-track-btn:hover {
      color: var(--text);
      background: rgba(0, 0, 0, 0.04);
    }
    .syllabus-track-btn.active {
      background: var(--surface);
      color: var(--text);
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
      font-weight: 800;
    }

    /* Sleek Document Header Card (Apple/Linear Aesthetic) */
    .official-pdf-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      margin-bottom: 22px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
      position: relative;
    }
    .pdf-meta {
      display: flex;
      align-items: center;
      gap: 14px;
      min-width: 260px;
      flex: 1;
    }
    .pdf-icon-badge {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      background: #f1f5f9;
      color: #0f172a;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border: 1px solid #e2e8f0;
      flex-shrink: 0;
    }
    .pdf-icon-badge span {
      font-size: 8.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-top: -2px;
      color: #dc2626;
    }
    .pdf-details-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .badge-session {
      font-size: 11px;
      font-weight: 700;
      color: #2563eb;
      background: rgba(37, 99, 235, 0.08);
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid rgba(37, 99, 235, 0.2);
    }
    .pdf-details-sub {
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 3px;
      line-height: 1.4;
    }
    .btn-download-pdf {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: #0f172a;
      color: #ffffff !important;
      padding: 8px 16px;
      border-radius: 9999px;
      font-size: 12.5px;
      font-weight: 700;
      text-decoration: none;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .btn-download-pdf:hover {
      background: #1e293b;
      transform: translateY(-1px);
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
    }

    /* Refined Muted Badges */
    .class-badge {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #e2e8f0;
    }
    .priority-badge {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.02em;
    }
    .priority-paramount {
      background: #fef2f2;
      color: #be123c;
      border: 1px solid #fecdd3;
    }
    .priority-guaranteed {
      background: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
    }
    .priority-high {
      background: #f0fdf4;
      color: #047857;
      border: 1px solid #bbf7d0;
    }
    .status-badge {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11.5px;
      font-weight: 600;
      background: #fffbeb;
      color: #b45309;
      border: 1px solid #fde68a;
      margin-top: 5px;
    }

    /* Refined Collapsible Topics */
    .topics-collapse {
      border: 1px solid var(--border-light);
      border-radius: 6px;
      overflow: hidden;
      background: var(--surface);
      margin-top: 10px;
    }
    .topics-collapse summary {
      padding: 8px 12px;
      font-size: 12px;
      font-weight: 700;
      color: var(--accent);
      cursor: pointer;
      background: rgba(37, 99, 235, 0.03);
      user-select: none;
    }
    .topics-collapse summary:hover {
      background: rgba(37, 99, 235, 0.06);
    }
    .topics-body {
      padding: 10px 14px;
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.6;
      border-top: 1px solid var(--border-light);
    }
"""

# Replace old CSS chunk
html = re.sub(r'/\* Official PDF Download Card & Badges \*/[\s\S]*?\.status-badge \{[\s\S]*?\}', premium_css, html)

# 3. Upgraded renderCbse12View
cbse12_fn = """    function renderCbse12View(container) {
      if (!dataCbse12 || !dataCbse12[currentSubject]) {
        container.innerHTML = '<div style="text-align:center; padding:40px; color:var(--text-muted);">Loading curriculum data...</div>';
        return;
      }

      const subData = dataCbse12[currentSubject];
      let chapters = subData.chapters;

      if (searchQuery) {
        chapters = chapters.filter(ch => 
          (ch.chapter && ch.chapter.toLowerCase().includes(searchQuery)) ||
          (ch.unit_name && ch.unit_name.toLowerCase().includes(searchQuery)) ||
          (ch.typology && ch.typology.toLowerCase().includes(searchQuery)) ||
          (ch.official_topics && ch.official_topics.toLowerCase().includes(searchQuery))
        );
      }

      const unitsMap = {};
      chapters.forEach(ch => {
        const uKey = `${ch.unit_no || 'I'}: ${ch.unit_name || ch.chapter}`;
        if (!unitsMap[uKey]) unitsMap[uKey] = { unit: ch.unit_no, name: ch.unit_name, chapters: [] };
        unitsMap[uKey].chapters.push(ch);
      });

      const totalMarks = (subData.theory_marks || 70) + (subData.internal_marks || 30);

      let html = `
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
          <div>
            <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">CBSE Class 12 ${currentSubject} (Subject Code ${subData.code})</h2>
            <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">Official Examination Blueprint: ${subData.theory_marks} Marks Theory + ${subData.internal_marks} Marks Practical/Internal = ${totalMarks} Marks.</p>
          </div>
          <div style="display:flex; gap:8px;">
            <a href="/practice/?exam=cbse&subject=${encodeURIComponent(currentSubject)}" class="btn-action-pyq">⚡ Practice All ${currentSubject} PYQs ➔</a>
          </div>
        </div>

        ${subData.pdf_url ? `
          <div class="official-pdf-card">
            <div class="pdf-meta">
              <div class="pdf-icon-badge">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
                <span>PDF</span>
              </div>
              <div>
                <div class="pdf-details-title">
                  Official CBSE Class 12 ${currentSubject} Curriculum Document
                  <span class="badge-session">Session 2026–2027</span>
                </div>
                <div class="pdf-details-sub">
                  Central Board of Secondary Education (CBSE Delhi) • Senior School Curriculum 2026–2027 • Verified PDF (${subData.pdf_size || 'Official'})
                </div>
              </div>
            </div>
            <a href="${subData.pdf_url}" target="_blank" download="${subData.pdf_name || 'CBSE_Class12_' + currentSubject + '_Syllabus_2026_27.pdf'}" class="btn-download-pdf">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              <span>Download Official PDF (2026–27)</span>
            </a>
          </div>
        ` : ''}
      `;

      Object.keys(unitsMap).forEach(uKey => {
        const u = unitsMap[uKey];
        const unitTotalMarks = u.chapters.reduce((sum, c) => sum + (c.theory_marks || 0), 0);

        html += `
          <div class="unit-section">
            <div class="unit-header">
              <span class="unit-title">📖 Unit ${uKey}</span>
              <span class="unit-marks-badge">${unitTotalMarks > 0 ? unitTotalMarks + ' Marks' : 'Official Unit'}</span>
            </div>
            <div>
              ${u.chapters.map(ch => `
                <div class="chapter-row">
                  <div class="chapter-meta-bar">
                    <div class="chapter-title-group">
                      <h3>${ch.chapter}</h3>
                      <div class="chapter-typology-tag"><strong>High-Probability Typology:</strong> ${ch.typology || 'Derivations, Case Studies, Numerical Problems'}</div>
                    </div>
                    <span class="chapter-marks-pill">${ch.theory_marks} Theory Marks</span>
                  </div>

                  <div class="cross-exam-box">
                    <span class="cross-exam-title">🎯 Entrance Overlap:</span>
                    ${ch.jee_overlap ? `<span class="overlap-chip">JEE Main: <strong>${ch.jee_overlap}</strong></span>` : ''}
                    ${ch.neet_overlap ? `<span class="overlap-chip">NEET UG: <strong>${ch.neet_overlap}</strong></span>` : ''}
                    ${ch.bitsat_overlap ? `<span class="overlap-chip">BITSAT: <strong>${ch.bitsat_overlap}</strong></span>` : ''}
                  </div>

                  ${ch.official_topics ? `
                    <details class="topics-collapse" ${searchQuery ? 'open' : ''}>
                      <summary>▶ Prescribed Official Syllabus Topics (cbseacademic.nic.in 2026–2027)</summary>
                      <div class="topics-body">
                        ${ch.official_topics}
                      </div>
                    </details>
                  ` : ''}

                  <div class="chapter-actions">
                    <a href="/practice/?exam=cbse&subject=${encodeURIComponent(currentSubject)}&chapter=${encodeURIComponent(ch.chapter)}" class="btn-action-pyq">
                      ⚡ Practice ${ch.chapter} PYQs ➔
                    </a>
                    <a href="/paper-maker/?exam=cbse&subject=${encodeURIComponent(currentSubject)}" class="btn-action-mock">
                      📝 CBT Mock Test
                    </a>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }"""

# 4. Upgraded renderCbse10View
cbse10_fn = """    function renderCbse10View(container) {
      if (!dataCbse10 || !dataCbse10[currentSubject]) {
        container.innerHTML = '<div style="text-align:center; padding:40px; color:var(--text-muted);">Loading Class 10 Foundation curriculum...</div>';
        return;
      }

      const subData = dataCbse10[currentSubject];
      let chapters = subData.chapters;

      if (searchQuery) {
        chapters = chapters.filter(ch => 
          (ch.chapter && ch.chapter.toLowerCase().includes(searchQuery)) ||
          (ch.unit_name && ch.unit_name.toLowerCase().includes(searchQuery)) ||
          (ch.official_topics && ch.official_topics.toLowerCase().includes(searchQuery))
        );
      }

      let html = `
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
          <div>
            <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">CBSE Class 10 ${currentSubject} (Subject Code ${subData.code})</h2>
            <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">Official Secondary School Blueprint: 80 Marks Theory + 20 Marks Internal Assessment = 100 Marks.</p>
          </div>
          <div style="display:flex; gap:8px;">
            <a href="/practice/?exam=cbse&subject=${encodeURIComponent(currentSubject)}" class="btn-action-pyq">⚡ Practice All ${currentSubject} PYQs ➔</a>
          </div>
        </div>

        ${subData.pdf_url ? `
          <div class="official-pdf-card">
            <div class="pdf-meta">
              <div class="pdf-icon-badge">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
                <span>PDF</span>
              </div>
              <div>
                <div class="pdf-details-title">
                  Official CBSE Class 10 ${currentSubject} Curriculum Document
                  <span class="badge-session">Session 2026–2027</span>
                </div>
                <div class="pdf-details-sub">
                  Central Board of Secondary Education (CBSE Delhi) • Secondary School Curriculum (Classes IX-X) • Verified PDF (${subData.pdf_size || 'Official'})
                </div>
              </div>
            </div>
            <a href="${subData.pdf_url}" target="_blank" download="${subData.pdf_name || 'CBSE_Class10_' + currentSubject + '_Syllabus_2026_27.pdf'}" class="btn-download-pdf">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              <span>Download Official PDF (2026–27)</span>
            </a>
          </div>
        ` : ''}
      `;

      html += `
        <div class="unit-section">
          ${chapters.map(ch => `
            <div class="chapter-row">
              <div class="chapter-meta-bar">
                <div class="chapter-title-group">
                  <h3>${ch.chapter}</h3>
                  <div class="chapter-typology-tag"><strong>Unit:</strong> ${ch.unit_no || 'I'} • ${ch.unit_name || 'Curriculum Core'}</div>
                </div>
                <span class="chapter-marks-pill">${ch.theory_marks || 6} Theory Marks</span>
              </div>

              ${ch.official_topics ? `
                <details class="topics-collapse" ${searchQuery ? 'open' : ''}>
                  <summary>▶ Prescribed Syllabus & Key Derivations (cbseacademic.nic.in 2026–2027)</summary>
                  <div class="topics-body">
                    ${ch.official_topics}
                  </div>
                </details>
              ` : ''}

              <div class="chapter-actions">
                <a href="/practice/?exam=cbse&subject=${encodeURIComponent(currentSubject)}&chapter=${encodeURIComponent(ch.chapter)}" class="btn-action-pyq">
                  ⚡ Practice Board Questions ➔
                </a>
              </div>
            </div>
          `).join('')}
        </div>
      `;

      container.innerHTML = html;
    }"""

# 5. Upgraded renderNeetView with corrected practice links
neet_fn = """    function renderNeetView(container) {
      if (!dataEntrance || !dataEntrance.neet) return;
      const neet = dataEntrance.neet;
      let subList = neet.subjects[currentSubject] || [];

      if (searchQuery) {
        subList = subList.filter(unit =>
          (unit.chapter && unit.chapter.toLowerCase().includes(searchQuery)) ||
          (unit.unit_name && unit.unit_name.toLowerCase().includes(searchQuery)) ||
          (unit.official_topics && unit.official_topics.toLowerCase().includes(searchQuery)) ||
          (unit.concept_archetype_sample && unit.concept_archetype_sample.toLowerCase().includes(searchQuery)) ||
          (unit.official_status && unit.official_status.toLowerCase().includes(searchQuery))
        );
      }

      // Map to correct practice subject key
      const practiceSubj = currentSubject.includes('Botany') ? 'Botany' : (currentSubject.includes('Zoology') ? 'Zoology' : currentSubject);

      let html = `
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div>
              <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">🩺 NEET UG ${currentSubject} Official Curriculum Blueprint</h2>
              <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">
                National Medical Commission (NMC) & NTA • Session 2026–2027 • 720 Marks (180 Questions to attempt in 200 Minutes). Scoring: +4 correct, -1 negative.
              </p>
            </div>
            <a href="/practice/?exam=neet&subject=${encodeURIComponent(practiceSubj)}" class="btn-action-pyq">Practice All NEET ${currentSubject} PYQs ➔</a>
          </div>
        </div>

        <div class="official-pdf-card">
          <div class="pdf-meta">
            <div class="pdf-icon-badge">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span>PDF</span>
            </div>
            <div>
              <div class="pdf-details-title">
                NEET (UG) Official Prescribed Curriculum & Statutory Chapter Weightage Document
                <span class="badge-session">Session 2026–2027</span>
              </div>
              <div class="pdf-details-sub">
                Under Graduate Medical Education Board (UGMEB), NMC & NTA • 41 Chapter Distribution & Rationalization Ledger (19 KB PDF)
              </div>
            </div>
          </div>
          <a href="/curriculum_pdf/NEET_UG_Official_Syllabus_2026_2027_NMC.pdf" target="_blank" download="NEET_UG_Official_Syllabus_2026_2027_NMC.pdf" class="btn-download-pdf">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Official PDF (2026–27)</span>
          </a>
        </div>

        <div class="unit-section">
          ${subList.map(unit => {
            const pTier = unit.priority_tier || unit.yield_tier || 'Guaranteed Core';
            const pClass = pTier === 'Paramount Core' ? 'priority-paramount' : pTier === 'High Yield' ? 'priority-high' : 'priority-guaranteed';
            const chName = unit.chapter || unit.name || 'Core Unit';
            const qsText = unit.question_count_avg || unit.avg_qs || '2 Qs';
            const marksText = unit.mark_weightage_range || unit.marks || '8 Marks';
            const archetype = unit.concept_archetype_sample || unit.top_topics || '';

            return `
              <div class="chapter-row">
                <div class="chapter-meta-bar">
                  <div class="chapter-title-group">
                    <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap; margin-bottom:4px;">
                      ${unit.class_level ? `<span class="class-badge">Class ${unit.class_level}</span>` : ''}
                      <span class="priority-badge ${pClass}">${pTier}</span>
                      ${unit.unit_name ? `<span style="font-size:12px; color:var(--text-muted); font-weight:600;">${unit.unit_name}</span>` : ''}
                    </div>
                    <h3 style="margin:2px 0 4px 0;">${chName}</h3>
                    ${unit.official_status && unit.official_status !== 'Active' ? `<div class="status-badge">⚠️ ${unit.official_status}</div>` : ''}
                    ${archetype ? `<div class="chapter-typology-tag" style="margin-top:6px;"><strong>Tested Archetype:</strong> ${archetype}</div>` : ''}
                  </div>
                  <div style="text-align:right; flex-shrink:0;">
                    <span class="chapter-marks-pill">${marksText}</span>
                    <div style="font-size:11.5px; font-weight:700; color:var(--accent); margin-top:3px;">${qsText}</div>
                  </div>
                </div>

                ${unit.official_topics ? `
                  <details class="topics-collapse" ${searchQuery ? 'open' : ''} style="margin-top:10px;">
                    <summary>▶ Prescribed Official Syllabus Topics (NMC UGMEB 2026–2027)</summary>
                    <div class="topics-body">
                      ${unit.official_topics}
                    </div>
                  </details>
                ` : ''}

                <div class="chapter-actions">
                  <a href="/practice/?exam=neet&subject=${encodeURIComponent(practiceSubj)}&chapter=${encodeURIComponent(chName)}" class="btn-action-pyq">
                    ⚡ Practice ${chName} ➔
                  </a>
                  <a href="/repeated/?exam=neet&subject=${encodeURIComponent(practiceSubj)}" class="btn-action-mock">
                    🔥 View Recurrence Radar
                  </a>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;

      container.innerHTML = html;
    }"""

# 6. Upgraded renderJeeMainView
jee_fn = """    function renderJeeMainView(container) {
      if (!dataEntrance || !dataEntrance.jee_main) return;
      const jee = dataEntrance.jee_main;
      let subList = jee.subjects[currentSubject] || [];

      if (searchQuery) {
        subList = subList.filter(unit =>
          (unit.chapter && unit.chapter.toLowerCase().includes(searchQuery)) ||
          (unit.unit_name && unit.unit_name.toLowerCase().includes(searchQuery)) ||
          (unit.official_topics && unit.official_topics.toLowerCase().includes(searchQuery)) ||
          (unit.concept_archetype_sample && unit.concept_archetype_sample.toLowerCase().includes(searchQuery)) ||
          (unit.official_status && unit.official_status.toLowerCase().includes(searchQuery))
        );
      }

      let html = `
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div>
              <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">⚡ JEE Main ${currentSubject} Official Curriculum Blueprint</h2>
              <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">
                National Testing Agency (NTA) • Session 2026–2027 • 186 CBT Shifts Archive (12,667 Questions). Exam: 300 Marks (75 Questions to attempt in 180 Minutes). +4 for correct, -1 for negative.
              </p>
            </div>
            <a href="/practice/?exam=jee&subject=${encodeURIComponent(currentSubject)}" class="btn-action-pyq">Practice JEE ${currentSubject} PYQs ➔</a>
          </div>
        </div>

        <div class="official-pdf-card">
          <div class="pdf-meta">
            <div class="pdf-icon-badge">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              <span>PDF</span>
            </div>
            <div>
              <div class="pdf-details-title">
                JEE (Main) Official Prescribed Curriculum & 186-Shift Frequency Blueprint
                <span class="badge-session">Session 2026–2027</span>
              </div>
              <div class="pdf-details-sub">
                National Testing Agency (NTA) • 54 Unit Empirical Frequency & Rationalization Ledger (32 KB PDF)
              </div>
            </div>
          </div>
          <a href="/curriculum_pdf/JEE_Main_Official_Syllabus_2026_2027_NTA.pdf" target="_blank" download="JEE_Main_Official_Syllabus_2026_2027_NTA.pdf" class="btn-download-pdf">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Official PDF (2026–27)</span>
          </a>
        </div>

        <div class="unit-section">
          ${subList.map(unit => {
            const pTier = unit.priority_tier || unit.yield_tier || 'Guaranteed Core';
            const pClass = pTier === 'Paramount Core' ? 'priority-paramount' : pTier === 'High Yield' ? 'priority-high' : 'priority-guaranteed';
            const chName = unit.chapter || unit.name || 'Core Unit';
            const qsText = unit.question_count_avg || unit.avg_qs || '1 - 2 Qs';
            const marksText = unit.mark_weightage_range || unit.shift_appearances || '4 - 8 Marks';
            const archetype = unit.concept_archetype_sample || unit.top_topics || '';

            return `
              <div class="chapter-row">
                <div class="chapter-meta-bar">
                  <div class="chapter-title-group">
                    <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap; margin-bottom:4px;">
                      ${unit.class_level ? `<span class="class-badge">Class ${unit.class_level}</span>` : ''}
                      <span class="priority-badge ${pClass}">${pTier}</span>
                      ${unit.unit_name ? `<span style="font-size:12px; color:var(--text-muted); font-weight:600;">${unit.unit_name}</span>` : ''}
                    </div>
                    <h3 style="margin:2px 0 4px 0;">${chName}</h3>
                    ${unit.official_status && unit.official_status !== 'Active' ? `<div class="status-badge">⚠️ ${unit.official_status}</div>` : ''}
                    ${archetype ? `<div class="chapter-typology-tag" style="margin-top:6px;"><strong>High-Frequency Tested Typology:</strong> ${archetype}</div>` : ''}
                  </div>
                  <div style="text-align:right; flex-shrink:0;">
                    <span class="chapter-marks-pill">${marksText}</span>
                    <div style="font-size:11.5px; font-weight:700; color:var(--accent); margin-top:3px;">${qsText}</div>
                  </div>
                </div>

                ${unit.official_topics ? `
                  <details class="topics-collapse" ${searchQuery ? 'open' : ''} style="margin-top:10px;">
                    <summary>▶ Prescribed Official Syllabus Topics (NTA 2026–2027)</summary>
                    <div class="topics-body">
                      ${unit.official_topics}
                    </div>
                  </details>
                ` : ''}

                <div class="chapter-actions">
                  <a href="/practice/?exam=jee&subject=${encodeURIComponent(currentSubject)}&chapter=${encodeURIComponent(chName)}" class="btn-action-pyq">
                    ⚡ Practice ${chName} ➔
                  </a>
                  <a href="/paper-maker/?exam=jee&subject=${encodeURIComponent(currentSubject)}" class="btn-action-mock">
                    📝 3-Hour CBT Simulator
                  </a>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;

      container.innerHTML = html;
    }"""

# 7. Upgraded renderBitsatView with separate direct practice buttons for English & Logic
bitsat_fn = """    function renderBitsatView(container) {
      if (!dataEntrance || !dataEntrance.bitsat) return;
      const b = dataEntrance.bitsat;

      let html = `
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:16px;">
          <h2 style="font-size:18px; font-weight:800; color:var(--text); margin:0;">🎯 BITSAT Speed Blueprint (130 Questions • 390 Marks • 180 Minutes)</h2>
          <p style="font-size:13px; color:var(--text-muted); margin:4px 0 0 0;">Scoring: Speed MCQ (+3 for correct, -1 for negative). Bonus 12 Questions unlock if all 130 questions are completed.</p>
        </div>

        <div class="unit-section">
          ${b.sections.map(sec => {
            let actionsHtml = '';
            if (sec.name.includes('English') && sec.name.includes('Logical')) {
              actionsHtml = `
                <a href="/practice/?exam=bitsat&subject=English+Proficiency" class="btn-action-pyq">
                  ⚡ Practice English Proficiency (187 Qs) ➔
                </a>
                <a href="/practice/?exam=bitsat&subject=Logical+Reasoning" class="btn-action-pyq" style="background:#2563eb;">
                  ⚡ Practice Logical Reasoning (164 Qs) ➔
                </a>
                <a href="/paper-maker/?exam=bitsat" class="btn-action-mock">
                  ⏱️ 130-Question Speed Mock
                </a>
              `;
            } else {
              actionsHtml = `
                <a href="/practice/?exam=bitsat&subject=${encodeURIComponent(sec.name)}" class="btn-action-pyq">
                  ⚡ Practice ${sec.name} MCQs ➔
                </a>
                <a href="/paper-maker/?exam=bitsat" class="btn-action-mock">
                  ⏱️ Speed Test
                </a>
              `;
            }

            return `
              <div class="chapter-row">
                <div class="chapter-meta-bar">
                  <div class="chapter-title-group">
                    <h3>${sec.part}: ${sec.name}</h3>
                    <div class="chapter-typology-tag">Speed Benchmark: <strong>${sec.speed_target}</strong> ${sec.details ? '• ' + sec.details : ''}</div>
                  </div>
                  <div style="text-align:right;">
                    <span class="chapter-marks-pill">${sec.marks} Marks</span>
                    <div style="font-size:11px; font-weight:700; color:var(--accent); margin-top:2px;">${sec.questions} Questions</div>
                  </div>
                </div>

                <div class="chapter-actions">
                  ${actionsHtml}
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;

      container.innerHTML = html;
    }"""

# Replace the render functions cleanly
html = re.sub(r'function renderCbse12View\(container\) \{[\s\S]*?\n    \}\n\n    function renderCbse10View', cbse12_fn + '\n\n    function renderCbse10View', html)
html = re.sub(r'function renderCbse10View\(container\) \{[\s\S]*?\n    \}\n\n    function renderNeetView', cbse10_fn + '\n\n    function renderNeetView', html)
html = re.sub(r'function renderNeetView\(container\) \{[\s\S]*?\n    \}\n\n    function renderJeeMainView', neet_fn + '\n\n    function renderJeeMainView', html)
html = re.sub(r'function renderJeeMainView\(container\) \{[\s\S]*?\n    \}\n\n    function renderJeeAdvView', jee_fn + '\n\n    function renderJeeAdvView', html)
html = re.sub(r'function renderBitsatView\(container\) \{[\s\S]*?\n    \}', bitsat_fn, html)

# 8. Replace SSR Header with clean Apple/Linear document card
ssr_pdf_card = """
      <div class="official-pdf-card">
        <div class="pdf-meta">
          <div class="pdf-icon-badge">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
            <span>PDF</span>
          </div>
          <div>
            <div class="pdf-details-title">
              Official CBSE Class 12 Chemistry Curriculum Document
              <span class="badge-session">Session 2026–2027</span>
            </div>
            <div class="pdf-details-sub">
              Central Board of Secondary Education (CBSE Delhi) • Senior School Curriculum 2026–2027 • Verified PDF (931 KB)
            </div>
          </div>
        </div>
        <a href="/curriculum_pdf/Class12_Chemistry.pdf" target="_blank" download="CBSE_Class12_Chemistry_Syllabus_2026_27.pdf" class="btn-download-pdf">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          <span>Download Official PDF (2026–27)</span>
        </a>
      </div>
"""
html = re.sub(r'<div class="official-pdf-card">[\s\S]*?</div>\s*</div>', ssr_pdf_card.strip(), html, count=1)

# Fix undefined Marks in SSR header
html = html.replace("Practical/Internal = undefined Marks.", "Practical/Internal = 100 Marks.")
html = html.replace("Practical/Internal.", "Practical/Internal = 100 Marks.")

# 9. Replace footer with exact homepage footer
html = re.sub(r'<footer class="site-footer">[\s\S]*?</footer>', homepage_footer, html)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("syllabus/index.html redesigned with clean minimalist aesthetic and exact homepage footer!")
