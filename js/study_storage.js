/**
 * Learnosha Unified Study Storage & Shell Controller
 * 100% Client-side, privacy-preserving study state (Student Name, Folders, Bookmarks, Notes, Mock History, Theme, Active Goal).
 * Zero server login required. Saved locally in browser localStorage.
 */

// Auto-migrate legacy storage keys from wovrix to learnosha
try {
  ['bookmarks', 'saved_folders', 'student_name', 'done', 'theme', 'active_goal', 'mock_history', 'active_mock_session'].forEach(k => {
    const oldV = localStorage.getItem('wovrix_' + k);
    if (oldV && !localStorage.getItem('learnosha_' + k)) {
      localStorage.setItem('learnosha_' + k, oldV);
    }
  });
} catch (_) {}

const STORAGE_KEYS = {
  BOOKMARKS: 'learnosha_bookmarks',
  FOLDERS: 'learnosha_saved_folders',
  STUDENT_NAME: 'learnosha_student_name',
  DONE: 'learnosha_done',
  THEME: 'learnosha_theme',
  ACTIVE_GOAL: 'learnosha_active_goal',
  MOCK_HISTORY: 'learnosha_mock_history',
  ACTIVE_MOCK: 'learnosha_active_mock_session'
};

// -----------------------------------------------------------------------------
// 1. THEME CONTROLLER
// -----------------------------------------------------------------------------
function initTheme() {
  const saved = localStorage.getItem(STORAGE_KEYS.THEME);
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
  updateThemeToggleUI(theme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem(STORAGE_KEYS.THEME, next);
  updateThemeToggleUI(next);
}

function updateThemeToggleUI(theme) {
  const btns = document.querySelectorAll('.btn-theme-toggle');
  btns.forEach(btn => {
    const lightIcon = btn.querySelector('.theme-icon-light');
    const darkIcon = btn.querySelector('.theme-icon-dark');
    if (lightIcon && darkIcon) {
      if (theme === 'dark') {
        lightIcon.style.display = 'inline';
        darkIcon.style.display = 'none';
      } else {
        lightIcon.style.display = 'none';
        darkIcon.style.display = 'inline';
      }
    }
  });
}

// -----------------------------------------------------------------------------
// 2. ACTIVE GOAL CONTROLLER (CBSE vs NEET)
// -----------------------------------------------------------------------------
function getActiveGoal() {
  const urlParams = new URLSearchParams(window.location.search);
  const urlExam = urlParams.get('exam');
  if (urlExam && (urlExam.toLowerCase() === 'cbse' || urlExam.toLowerCase() === 'neet')) {
    localStorage.setItem(STORAGE_KEYS.ACTIVE_GOAL, urlExam.toLowerCase());
    return urlExam.toLowerCase();
  }
  return localStorage.getItem(STORAGE_KEYS.ACTIVE_GOAL) || 'cbse';
}

function setActiveGoal(goal) {
  if (goal !== 'cbse' && goal !== 'neet') return;
  localStorage.setItem(STORAGE_KEYS.ACTIVE_GOAL, goal);
  updateGoalSwitcherUI(goal);
  window.dispatchEvent(new CustomEvent('learnosha:goalChange', { detail: { goal } }));
  window.dispatchEvent(new CustomEvent('wovrix:goalChange', { detail: { goal } }));
}

function updateGoalSwitcherUI(goal) {
  const labels = document.querySelectorAll('.active-goal-label');
  labels.forEach(el => {
    el.innerHTML = goal === 'neet' ? '🩺 NEET UG' : '🎯 CBSE Class 12';
  });
  const pills = document.querySelectorAll('.goal-toggle-pill');
  pills.forEach(p => {
    p.classList.toggle('active', p.getAttribute('data-goal') === goal);
  });
}

// -----------------------------------------------------------------------------
// 3. STUDENT PROFILE & NAME
// -----------------------------------------------------------------------------
function getStudentName() {
  return localStorage.getItem(STORAGE_KEYS.STUDENT_NAME) || '';
}

function setStudentName(name) {
  const trimmed = (name || '').trim();
  localStorage.setItem(STORAGE_KEYS.STUDENT_NAME, trimmed);
  window.dispatchEvent(new CustomEvent('learnosha:nameChange', { detail: { name: trimmed } }));
  window.dispatchEvent(new CustomEvent('wovrix:nameChange', { detail: { name: trimmed } }));
  return trimmed;
}

// -----------------------------------------------------------------------------
// 4. SAVED FOLDERS (YouTube/Instagram-style collections)
// -----------------------------------------------------------------------------
function getFolders() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.FOLDERS);
    if (!raw) {
      const def = ['Quick Bookmarks', 'Formula Traps', 'High-Yield Revision'];
      localStorage.setItem(STORAGE_KEYS.FOLDERS, JSON.stringify(def));
      return def;
    }
    return JSON.parse(raw);
  } catch (e) {
    return ['Quick Bookmarks', 'Formula Traps'];
  }
}

function createFolder(folderName) {
  const clean = (folderName || '').trim();
  if (!clean) return false;
  const folders = getFolders();
  if (!folders.includes(clean)) {
    folders.push(clean);
    localStorage.setItem(STORAGE_KEYS.FOLDERS, JSON.stringify(folders));
    return true;
  }
  return false;
}

// -----------------------------------------------------------------------------
// 5. BOOKMARKS & NOTES API
// -----------------------------------------------------------------------------
function getBookmarks() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.BOOKMARKS) || '[]');
  } catch (e) {
    return [];
  }
}

function isBookmarked(qId) {
  const bms = getBookmarks();
  return bms.some(b => String(b.id) === String(qId));
}

function getBookmarkItem(qId) {
  const bms = getBookmarks();
  return bms.find(b => String(b.id) === String(qId)) || null;
}

function saveBookmark(qId, meta) {
  const bms = getBookmarks();
  const index = bms.findIndex(b => String(b.id) === String(qId));
  const entry = {
    id: String(qId),
    subject: meta.subject || 'General',
    chapter: meta.chapter || '',
    year: meta.year || '2026',
    textSnippet: meta.textSnippet || '',
    folder: meta.folder || 'Quick Bookmarks',
    note: meta.note || '',
    savedAt: new Date().toISOString()
  };

  if (index >= 0) {
    bms[index] = { ...bms[index], ...entry };
  } else {
    bms.unshift(entry);
  }

  localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bms));
  syncBookmarkBadges();
  return true;
}

function removeBookmark(qId) {
  let bms = getBookmarks();
  bms = bms.filter(b => String(b.id) !== String(qId));
  localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bms));
  syncBookmarkBadges();
  return false;
}

function toggleBookmarkQuick(qId, subject, chapter, year, textSnippet) {
  if (isBookmarked(qId)) {
    removeBookmark(qId);
    return false;
  } else {
    saveBookmark(qId, { subject, chapter, year, textSnippet, folder: 'Quick Bookmarks' });
    return true;
  }
}

function syncBookmarkBadges() {
  const count = getBookmarks().length;
  document.querySelectorAll('.nav-bookmark-count').forEach(el => {
    el.textContent = count;
    el.style.display = count > 0 ? 'inline-flex' : 'none';
  });
}

// -----------------------------------------------------------------------------
// 6. DONE / MASTERED API
// -----------------------------------------------------------------------------
function getCompleted() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.DONE) || '[]');
  } catch (e) {
    return [];
  }
}

function isDone(qId) {
  return getCompleted().includes(String(qId));
}

function toggleDone(qId) {
  let doneList = getCompleted();
  const idStr = String(qId);
  let nowDone = false;
  if (doneList.includes(idStr)) {
    doneList = doneList.filter(id => id !== idStr);
  } else {
    doneList.push(idStr);
    nowDone = true;
  }
  localStorage.setItem(STORAGE_KEYS.DONE, JSON.stringify(doneList));
  return nowDone;
}

// -----------------------------------------------------------------------------
// 7. MOCK EXAM CRASH RECOVERY & HISTORY
// -----------------------------------------------------------------------------
function saveActiveMockSession(sessionData) {
  try {
    localStorage.setItem(STORAGE_KEYS.ACTIVE_MOCK, JSON.stringify({
      ...sessionData,
      lastSavedAt: Date.now()
    }));
  } catch (e) {
    console.error('Failed to cache active mock', e);
  }
}

function getActiveMockSession() {
  try {
    const raw = localStorage.getItem(STORAGE_KEYS.ACTIVE_MOCK);
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

function clearActiveMockSession() {
  localStorage.removeItem(STORAGE_KEYS.ACTIVE_MOCK);
}

function saveMockResultToHistory(resultData) {
  try {
    const history = JSON.parse(localStorage.getItem(STORAGE_KEYS.MOCK_HISTORY) || '[]');
    history.unshift({
      id: 'mock_' + Date.now(),
      date: new Date().toLocaleDateString('en-IN', { month: 'short', day: 'numeric', year: 'numeric' }),
      time: new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' }),
      ...resultData
    });
    localStorage.setItem(STORAGE_KEYS.MOCK_HISTORY, JSON.stringify(history));
    return true;
  } catch (e) {
    console.error('Failed to save mock result', e);
    return false;
  }
}

function getMockHistory() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.MOCK_HISTORY) || '[]');
  } catch (e) {
    return [];
  }
}

// -----------------------------------------------------------------------------
// 8. MOBILE DRAWER CONTROLLER
// -----------------------------------------------------------------------------
function toggleMobileDrawer(forceOpen) {
  const drawer = document.getElementById('mobileNavDrawer');
  const backdrop = document.getElementById('drawerBackdrop');
  if (!drawer) return;

  const isOpen = drawer.classList.contains('open');
  const shouldOpen = typeof forceOpen === 'boolean' ? forceOpen : !isOpen;

  drawer.classList.toggle('open', shouldOpen);
  if (backdrop) {
    backdrop.classList.toggle('active', shouldOpen);
  }
  document.body.style.overflow = shouldOpen ? 'hidden' : '';
}

// Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  const goal = getActiveGoal();
  updateGoalSwitcherUI(goal);
  syncBookmarkBadges();

  // Close drawer on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') toggleMobileDrawer(false);
  });
});
