import os

p = r"E:\PYQ_Wovrix_Portal\pyq-wovrix\jee\index.html"
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Head: ensure Learnosha theme styling and KaTeX font compatibility
head_target = """  <link rel="stylesheet" href="/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">"""

head_replacement = """  <link rel="stylesheet" href="/style.css?v=20261110_7">
  <!-- KaTeX for math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>"""

if head_target in text:
    text = text.replace(head_target, head_replacement)
    print("Updated head tags in jee/index.html")

# 2. Update Header: Learnosha logo, theme toggle button, clean back button
old_header = """  <!-- Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="brand">
        <svg class="brand-logo-icon" width="22" height="22" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="32" height="32" rx="7" fill="#18181b"/>
          <path d="M6 10L11 23L16 14L21 23L26 10" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="16" cy="14" r="2.2" fill="#3b82f6"/>
        </svg>
        <span class="brand-name">LEARNOSHA <span class="brand-slash">/</span> <span class="brand-sub">JEE</span></span>
      </a>

      <nav class="nav-links">
        <a href="/" class="btn-act" style="font-size:12px;">← Back to All Exams</a>
      </nav>
    </div>
  </header>"""

new_header = """  <!-- Header -->
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="brand">
        <svg class="brand-logo-icon" width="22" height="22" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="32" height="32" rx="7" fill="#18181b"/>
          <path d="M6 10L11 23L16 14L21 23L26 10" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="16" cy="14" r="2.2" fill="#3b82f6"/>
        </svg>
        <span class="brand-name">LEARNOSHA <span class="brand-slash">/</span> <span class="brand-sub">JEE MAIN</span></span>
      </a>

      <nav class="nav-links">
        <a href="/practice/" class="btn-act" style="font-size:12.5px; font-weight:700;">🎯 Practice Hub</a>
        <button id="themeToggleBtn" class="btn-theme-toggle" onclick="toggleTheme()" aria-label="Toggle Dark Mode" title="Toggle Dark/Light Mode">
          <span class="theme-icon-light">☀️</span>
          <span class="theme-icon-dark">🌙</span>
        </button>
      </nav>
    </div>
  </header>"""

if old_header in text:
    text = text.replace(old_header, new_header)
    print("Updated header in jee/index.html")

# 3. Clean up Hero Actions Bar: remove broken developer markdown links!
old_actions = """      <div class="hero-actions-bar">
        <button class="btn-act primary" onclick="toggleCBTMode()" id="cbtToggleBtn">
          <i class="fa-solid fa-stopwatch"></i> Start CBT Mock Mode
        </button>
        <button class="btn-act" onclick="toggleAllSolutions()" id="solToggleBtn">
          <i class="fa-solid fa-lightbulb"></i> Reveal All Solutions
        </button>
        <a href="../jee-main-portal/JEE_MAIN_MASTER_AI_VAULT.md" download="JEE_MAIN_MASTER_AI_VAULT.md" class="btn-act" title="Download Master Markdown Vault for AI Ingestion">
          <i class="fa-solid fa-robot"></i> Master AI Vault (.md)
        </a>
        <a href="../jee-main-portal/JEE_AI_SUPER_PROMPT.md" download="JEE_AI_SUPER_PROMPT.md" class="btn-act" title="Download System Prompt for ChatGPT / Claude">
          <i class="fa-solid fa-terminal"></i> AI Prompt (.md)
        </a>
      </div>"""

new_actions = """      <div class="hero-actions-bar">
        <button class="btn-act primary" onclick="toggleCBTMode()" id="cbtToggleBtn">
          ⏱️ Start 3-Hour CBT Test Mode
        </button>
        <button class="btn-act" onclick="toggleAllSolutions()" id="solToggleBtn">
          💡 Show Solutions & NTA Answer Keys
        </button>
        <a href="/practice/" class="btn-act">
          🎯 Back to Practice Hub
        </a>
      </div>"""

if old_actions in text:
    text = text.replace(old_actions, new_actions)
    print("Removed developer vault links and cleaned hero actions bar!")
else:
    print("Warning: old_actions not found!")

# 4. Add theme script before closing </body>
footer_target = "  <script src=\"/js/study_storage.js?v=20261110_7\"></script>"
if footer_target not in text:
    text = text.replace("</body>", """  <script src="/js/study_storage.js?v=20261110_7"></script>
  <script>
    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('learnosha_theme', next);
    }
    const savedTheme = localStorage.getItem('learnosha_theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
  </script>
</body>""")
    print("Added theme toggle script and study_storage.js")

with open(p, "w", encoding="utf-8") as f:
    f.write(text)

print("Unified jee/index.html with Learnosha UI successfully!")
