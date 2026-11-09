/**
 * Wovrix PYQ Study Storage Engine
 * 100% Client-side, privacy-preserving study state (Bookmarks, Done status, Theme).
 * Zero server login required. Saved locally in browser localStorage.
 */

const STORAGE_KEYS = {
  BOOKMARKS: 'wovrix_bookmarks',
  DONE: 'wovrix_done',
  THEME: 'wovrix_theme'
};

// Initialize Theme
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

// Bookmarks API
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

function toggleBookmark(qId, subject, chapter, year) {
  const bms = getBookmarks();
  const index = bms.findIndex(b => String(b.id) === String(qId));
  let added = false;
  if (index >= 0) {
    bms.splice(index, 1);
  } else {
    bms.push({
      id: String(qId),
      subject: subject || 'General',
      chapter: chapter || '',
      year: year || '2026',
      savedAt: new Date().toISOString()
    });
    added = true;
  }
  localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bms));

  // Update UI on page
  const btn = document.getElementById('btn_bm_' + qId);
  if (btn) {
    btn.classList.toggle('bookmarked', added);
    btn.innerHTML = added ? '<span>★</span> Bookmarked' : '<span>☆</span> Bookmark';
  }
  return added;
}

// Done Status API
function getCompleted() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.DONE) || '[]');
  } catch (e) {
    return [];
  }
}

function isDone(qId) {
  const doneList = getCompleted();
  return doneList.includes(String(qId));
}

function toggleDone(qId) {
  const doneList = getCompleted();
  const qStr = String(qId);
  const index = doneList.indexOf(qStr);
  let isNowDone = false;
  if (index >= 0) {
    doneList.splice(index, 1);
  } else {
    doneList.push(qStr);
    isNowDone = true;
  }
  localStorage.setItem(STORAGE_KEYS.DONE, JSON.stringify(doneList));

  // Update card UI
  const card = document.getElementById(qId);
  if (card) {
    card.classList.toggle('is-done', isNowDone);
  }
  return isNowDone;
}

// Auto-run on load
document.addEventListener('DOMContentLoaded', initTheme);
initTheme();
