/**
 * Learnosha In-App Universal Question Reporting Modal
 * Saves student reports locally in localStorage and syncs to API queue.
 */
(function() {
  // Inject modal markup once per page
  if (document.getElementById('questionReportModalOverlay')) return;

  const modalHtml = `
    <div id="questionReportModalOverlay" class="report-modal-overlay" onclick="handleReportBackdropClick(event)">
      <div class="report-modal-card" onclick="event.stopPropagation()">
        <div id="reportModalFormView">
          <div class="report-modal-header">
            <div>
              <h3 class="report-modal-title">
                <span>🚩</span> Report an Issue
              </h3>
              <div class="report-modal-subtitle" id="reportModalSubtitle">
                Question Details
              </div>
            </div>
            <button class="report-modal-close" onclick="closeReportModal()" aria-label="Close modal">&times;</button>
          </div>

          <form id="reportIssueForm" onsubmit="submitQuestionReport(event)">
            <input type="hidden" id="reportFieldQId" name="qid">
            <input type="hidden" id="reportFieldSubject" name="subject">
            <input type="hidden" id="reportFieldYear" name="year">
            <input type="hidden" id="reportFieldChapter" name="chapter">

            <div class="report-issue-list">
              <label class="report-issue-label">
                <input type="checkbox" name="issue" value="incorrect_marks">
                <span><strong>Incorrect Marks</strong> (e.g. 1M vs 2M/3M/4M/5M)</span>
              </label>
              <label class="report-issue-label">
                <input type="checkbox" name="issue" value="katex_math_broken">
                <span><strong>KaTeX / Formula Error</strong> (unrendered or broken symbols)</span>
              </label>
              <label class="report-issue-label">
                <input type="checkbox" name="issue" value="missing_diagram_or_text">
                <span><strong>Missing Diagram / Truncated Text</strong></span>
              </label>
              <label class="report-issue-label">
                <input type="checkbox" name="issue" value="missing_solution">
                <span><strong>Request Step Solution / Explanation</strong></span>
              </label>
              <label class="report-issue-label">
                <input type="checkbox" name="issue" value="wrong_chapter">
                <span><strong>Wrong Chapter / Classification</strong></span>
              </label>
              <label class="report-issue-label">
                <input type="checkbox" name="issue" value="other">
                <span><strong>Other Issue</strong></span>
              </label>
            </div>

            <textarea 
              id="reportNotesInput" 
              class="report-notes-textarea" 
              placeholder="Optional: What went wrong or what should the correct value be?"
              rows="3"></textarea>

            <div class="report-modal-actions">
              <button type="button" class="btn-report-cancel" onclick="closeReportModal()">Cancel</button>
              <button type="submit" class="btn-report-submit" id="btnSubmitReport">
                <span>Save to System</span> &rarr;
              </button>
            </div>
          </form>
        </div>

        <div id="reportModalSuccessView" class="report-success-state" style="display: none;">
          <div class="report-success-icon">✓</div>
          <h4 class="report-success-title">Report Saved to System</h4>
          <p class="report-success-desc">
            Your report for <strong id="reportSuccessQId">this question</strong> has been queued.<br>
            Our automated morning validation pipeline will audit and resolve the error.
          </p>
        </div>
      </div>
    </div>
  `;

  const container = document.createElement('div');
  container.innerHTML = modalHtml;
  document.body.appendChild(container.firstElementChild);
})();

function openReportModal(qId, subject, year, chapter, marks) {
  const overlay = document.getElementById('questionReportModalOverlay');
  const subEl = document.getElementById('reportModalSubtitle');
  const formView = document.getElementById('reportModalFormView');
  const successView = document.getElementById('reportModalSuccessView');
  const form = document.getElementById('reportIssueForm');

  if (!overlay) return;

  document.getElementById('reportFieldQId').value = qId || '';
  document.getElementById('reportFieldSubject').value = subject || '';
  document.getElementById('reportFieldYear').value = year || '';
  document.getElementById('reportFieldChapter').value = chapter || '';
  document.getElementById('reportNotesInput').value = '';

  // Uncheck all
  form.querySelectorAll('input[name="issue"]').forEach(cb => cb.checked = false);

  subEl.innerText = `Question #${qId || 'N/A'} · ${subject || 'CBSE'} · ${year || 'PYQ'}${chapter ? ' · ' + chapter : ''}`;
  formView.style.display = 'block';
  successView.style.display = 'none';

  overlay.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeReportModal() {
  const overlay = document.getElementById('questionReportModalOverlay');
  if (overlay) {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }
}

function handleReportBackdropClick(e) {
  if (e.target.id === 'questionReportModalOverlay') {
    closeReportModal();
  }
}

function submitQuestionReport(e) {
  e.preventDefault();

  const qId = document.getElementById('reportFieldQId').value;
  const subject = document.getElementById('reportFieldSubject').value;
  const year = document.getElementById('reportFieldYear').value;
  const chapter = document.getElementById('reportFieldChapter').value;
  const notes = document.getElementById('reportNotesInput').value.trim();

  const checkedIssues = [];
  document.querySelectorAll('#reportIssueForm input[name="issue"]:checked').forEach(cb => {
    checkedIssues.push(cb.value);
  });

  if (checkedIssues.length === 0 && !notes) {
    alert('Please select at least one issue or type a brief note.');
    return;
  }

  const reportPayload = {
    qid: qId,
    subject: subject,
    year: year,
    chapter: chapter,
    issues: checkedIssues,
    notes: notes,
    timestamp: new Date().toISOString(),
    url: window.location.href,
    userAgent: navigator.userAgent
  };

  // 1. Save to local storage
  try {
    const existing = JSON.parse(localStorage.getItem('wovrix_pyq_reports') || '[]');
    existing.push(reportPayload);
    localStorage.setItem('wovrix_pyq_reports', JSON.stringify(existing));
  } catch (err) {
    console.warn('LocalStorage save error:', err);
  }

  // 2. Dispatch to serverless endpoint /api/report (best effort)
  try {
    if (navigator.sendBeacon) {
      navigator.sendBeacon('/api/report', JSON.stringify(reportPayload));
    } else {
      fetch('/api/report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(reportPayload)
      }).catch(() => {});
    }
  } catch (_) {}

  // 3. Show success state
  document.getElementById('reportSuccessQId').innerText = `Question #${qId}`;
  document.getElementById('reportModalFormView').style.display = 'none';
  document.getElementById('reportModalSuccessView').style.display = 'block';

  setTimeout(() => {
    closeReportModal();
  }, 2200);
}

// Global escape key listener
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeReportModal();
});
