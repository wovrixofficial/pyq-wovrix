import json
import html
import os

print("[1/3] Loading master formulas...")
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/data/formulas_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

chapters = master['chapters']

# Highlighter color rotation
HIGHLIGHT_CLASSES = ['highlight-yellow', 'highlight-blue', 'highlight-green', 'highlight-peach']

def escape(s):
    return html.escape(str(s))

def render_formula_item(f, chap_subject):
    f_name = escape(f['name'])
    latex = f['latex']
    latex_escaped = escape(latex)
    note = escape(f.get('note', ''))
    high_yield = f.get('high_yield', False)
    
    star_badge = '<span class="star-pill" title="Highly Repeated in Exams">⭐ High-Yield</span>' if high_yield else ''
    
    note_html = f'<div class="formula-note"><span class="handwritten-accent">Note:</span> {note}</div>' if note else ''
    
    return f'''
      <div class="formula-item">
        <div class="formula-item-header">
          <span class="formula-name">{f_name}</span>
          <div class="formula-badges">
            {star_badge}
            <button class="btn-copy-latex" data-latex="{latex_escaped}" onclick="copyLatex(this)" title="Copy LaTeX code">📋 Copy</button>
          </div>
        </div>
        <div class="math-display">
          $${latex}$$
        </div>
        {note_html}
      </div>
    '''

def render_chapter_card(ch, idx):
    cls_title = escape(ch['class'])
    subj = escape(ch['subject'])
    icon = ch.get('icon', '📝')
    chap_title = escape(ch['chapter_title'])
    count = ch['formula_count']
    practice_url = escape(ch.get('practice_url', '/practice/'))
    topper_tip = escape(ch['formulas'][0].get('topper_tip', '⭐ Master this chapter for guaranteed marks in board and competitive exams!'))
    
    hl_class = HIGHLIGHT_CLASSES[idx % len(HIGHLIGHT_CLASSES)]
    
    formulas_html = "\n".join(render_formula_item(f, ch['subject']) for f in ch['formulas'])
    
    return f'''
    <article class="handwritten-card" data-class="{cls_title}" data-subject="{subj}" data-chapter="{chap_title.lower()}">
      <div class="washi-tape"></div>
      <div class="card-top-meta">
        <span class="sheet-tag">{icon} {cls_title} • {subj}</span>
        <span class="count-pill">{count} Formulas</span>
      </div>
      
      <h2 class="chapter-heading">
        <span class="{hl_class}">{chap_title}</span>
      </h2>
      
      <div class="formulas-container">
        {formulas_html}
      </div>
      
      <div class="topper-sticky">
        <div class="sticky-pin">📌</div>
        <div class="sticky-title">Topper's Revision Note & Traps:</div>
        <div class="sticky-text">{topper_tip}</div>
      </div>
      
      <div class="card-footer-actions">
        <a href="{practice_url}" class="btn-practice-pyq">
          ⚡ Practice {chap_title} PYQs ➔
        </a>
      </div>
    </article>
    '''

print("[2/3] Generating initial SSR HTML cards...")
ssr_cards = []
for idx, ch in enumerate(chapters[:30]): # Initial 30 high-yield chapters SSR
    ssr_cards.append(render_chapter_card(ch, idx))

ssr_html_content = "\n".join(ssr_cards)

print("[3/3] Assembling complete formula-sheets/index.html...")

full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtm.js?id=GTM-W9TG2L83"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Handwritten Formula Sheets & Revision Vault (Class 9–12 Maths, Physics, Chemistry) | Learnosha</title>
  <meta name="description" content="Free handcrafted topper formula sheets and cheat sheets for Class 9, 10, 11 & 12 (Physics, Chemistry, Maths & Biology). Authentic handwritten style, KaTeX math, memory tricks, common exam traps, and 1-click PYQ practice.">
  <link rel="canonical" href="https://learnosha.in/formula-sheets/">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/style.css?v=20261111_6">

  <!-- Google Fonts: Caveat & Kalam for Authentic Handwritten Topper Aesthetic -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Kalam:wght@400;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">

  <!-- KaTeX for crisp mathematical formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <link rel="stylesheet" href="/report-modal.css">

  <style>
    /* Handwritten Vault Specific Styles */
    :root {{
      --paper-bg: #fdfbf7;
      --paper-border: #e8e3d5;
      --paper-grid: #f1ede4;
      --ink-color: #1e293b;
      --ink-muted: #475569;
      --sticky-bg: #fef9c3;
      --sticky-border: #fde047;
      --sticky-text: #713f12;
    }}

    [data-theme="dark"] {{
      --paper-bg: #131926;
      --paper-border: #233148;
      --paper-grid: #1a2233;
      --ink-color: #f1f5f9;
      --ink-muted: #94a3b8;
      --sticky-bg: #272314;
      --sticky-border: #854d0e;
      --sticky-text: #fef08a;
    }}

    .formula-hero {{
      text-align: center;
      padding: 44px 20px 24px;
      max-width: 960px;
      margin: 0 auto;
    }}

    .handwritten-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 14px;
      border-radius: 9999px;
      font-size: 12.5px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      background: rgba(217, 119, 6, 0.12);
      color: #b45309;
      margin-bottom: 12px;
      border: 1px solid rgba(217, 119, 6, 0.25);
    }}

    [data-theme="dark"] .handwritten-badge {{
      background: rgba(245, 158, 11, 0.18);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.35);
    }}

    .formula-hero-title {{
      font-size: clamp(28px, 4.5vw, 42px);
      font-weight: 800;
      letter-spacing: -0.025em;
      line-height: 1.2;
      color: var(--text);
      margin-bottom: 12px;
    }}

    .formula-hero-title .handwritten-title-span {{
      font-family: 'Caveat', cursive;
      font-size: 1.25em;
      font-weight: 700;
      color: #d97706;
      margin-left: 4px;
      display: inline-block;
      transform: rotate(-1.5deg);
    }}

    .formula-hero-subtitle {{
      font-size: 15.5px;
      color: var(--text-muted);
      line-height: 1.6;
      max-width: 760px;
      margin: 0 auto 22px;
    }}

    /* Hero Quick Highlights */
    .hero-stat-pills {{
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 26px;
    }}

    .hero-stat-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
    }}

    .hero-actions {{
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 28px;
    }}

    .btn-print-vault {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 22px;
      border-radius: 9999px;
      background: #0f172a;
      color: #ffffff;
      font-size: 13.5px;
      font-weight: 700;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
      transition: all 0.2s ease;
    }}

    [data-theme="dark"] .btn-print-vault {{
      background: #f8fafc;
      color: #0f172a;
    }}

    .btn-print-vault:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(15, 23, 42, 0.25);
    }}

    .btn-view-toggle {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 9px 18px;
      border-radius: 9999px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .btn-view-toggle:hover {{
      border-color: var(--accent);
    }}

    /* Search & Filter Container */
    .filter-section {{
      max-width: 1080px;
      margin: 0 auto 32px;
      padding: 0 20px;
    }}

    .search-box-wrap {{
      max-width: 600px;
      margin: 0 auto 20px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      padding: 13px 20px 13px 46px;
      border-radius: 9999px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      font-size: 14.5px;
      box-shadow: var(--shadow-subtle);
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }}

    .search-icon-svg {{
      position: absolute;
      left: 17px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
    }}

    /* Class Tabs */
    .class-tabs-bar {{
      display: flex;
      justify-content: center;
      gap: 6px;
      padding: 5px;
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 9999px;
      max-width: 660px;
      margin: 0 auto 16px;
      overflow-x: auto;
    }}

    .class-tab-btn {{
      padding: 7px 16px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-muted);
      border: none;
      background: transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}

    .class-tab-btn:hover {{
      color: var(--text);
    }}

    .class-tab-btn.active {{
      background: var(--surface);
      color: var(--text);
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}

    /* Subject Chips */
    .subject-chips-bar {{
      display: flex;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .subject-chip {{
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .subject-chip:hover {{
      border-color: var(--accent);
    }}

    .subject-chip.active {{
      background: var(--accent);
      color: #ffffff;
      border-color: var(--accent);
    }}

    /* Vault Cards Grid */
    .vault-grid {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px 60px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 28px;
    }}

    @media (max-width: 768px) {{
      .vault-grid {{
        grid-template-columns: 1fr;
        gap: 22px;
      }}
    }}

    /* Handwritten Card Styles */
    .handwritten-card {{
      background-color: var(--paper-bg);
      border: 1.5px solid var(--paper-border);
      border-radius: 14px;
      padding: 24px 22px 20px;
      position: relative;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.035);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      background-image: radial-gradient(var(--paper-grid) 1.2px, transparent 1.2px);
      background-size: 18px 18px;
    }}

    .handwritten-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
    }}

    /* Studio Mode Overrides */
    body.studio-mode .handwritten-card {{
      background-color: var(--surface);
      background-image: none;
      border-color: var(--border);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-subtle);
    }}

    body.studio-mode .washi-tape {{
      display: none;
    }}

    body.studio-mode .chapter-heading span {{
      background: none !important;
      padding: 0;
      color: var(--text);
      font-family: inherit;
      font-size: 18px;
    }}

    body.studio-mode .formula-name {{
      font-family: inherit;
      font-size: 15px;
      font-weight: 700;
    }}

    /* Washi Tape Graphic */
    .washi-tape {{
      position: absolute;
      top: -10px;
      left: 50%;
      transform: translateX(-50%) rotate(-1deg);
      width: 90px;
      height: 20px;
      background: rgba(254, 240, 138, 0.55);
      border: 1px dashed rgba(202, 138, 4, 0.4);
      backdrop-filter: blur(2px);
      border-radius: 2px;
      pointer-events: none;
      z-index: 2;
    }}

    [data-theme="dark"] .washi-tape {{
      background: rgba(234, 179, 8, 0.25);
      border-color: rgba(234, 179, 8, 0.5);
    }}

    .card-top-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .sheet-tag {{
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--ink-muted);
    }}

    .count-pill {{
      font-size: 11.5px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 9999px;
      background: rgba(0,0,0,0.05);
      color: var(--ink-muted);
    }}

    [data-theme="dark"] .count-pill {{
      background: rgba(255,255,255,0.08);
    }}

    .chapter-heading {{
      margin: 0 0 16px 0;
      line-height: 1.25;
    }}

    .chapter-heading span {{
      font-family: 'Caveat', cursive;
      font-size: 26px;
      font-weight: 700;
      color: #0f172a;
      display: inline-block;
      line-height: 1.2;
    }}

    [data-theme="dark"] .chapter-heading span {{
      color: #f8fafc;
    }}

    /* Pastel Highlighters */
    .highlight-yellow {{
      background: linear-gradient(104deg, rgba(254, 240, 138, 0.3) 0.9%, rgba(254, 240, 138, 0.85) 2.4%, rgba(254, 240, 138, 0.6) 98%);
      border-radius: 4px;
      padding: 2px 8px;
    }}
    .highlight-blue {{
      background: linear-gradient(104deg, rgba(186, 230, 253, 0.3) 0.9%, rgba(186, 230, 253, 0.85) 2.4%, rgba(186, 230, 253, 0.6) 98%);
      border-radius: 4px;
      padding: 2px 8px;
    }}
    .highlight-green {{
      background: linear-gradient(104deg, rgba(187, 247, 208, 0.3) 0.9%, rgba(187, 247, 208, 0.85) 2.4%, rgba(187, 247, 208, 0.6) 98%);
      border-radius: 4px;
      padding: 2px 8px;
    }}
    .highlight-peach {{
      background: linear-gradient(104deg, rgba(254, 215, 170, 0.3) 0.9%, rgba(254, 215, 170, 0.85) 2.4%, rgba(254, 215, 170, 0.6) 98%);
      border-radius: 4px;
      padding: 2px 8px;
    }}

    [data-theme="dark"] .highlight-yellow {{
      background: rgba(234, 179, 8, 0.25);
    }}
    [data-theme="dark"] .highlight-blue {{
      background: rgba(56, 189, 248, 0.25);
    }}
    [data-theme="dark"] .highlight-green {{
      background: rgba(34, 197, 94, 0.25);
    }}
    [data-theme="dark"] .highlight-peach {{
      background: rgba(251, 146, 60, 0.25);
    }}

    /* Formula Items Container */
    .formulas-container {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      flex: 1;
    }}

    .formula-item {{
      background: rgba(255, 255, 255, 0.65);
      border: 1px solid var(--paper-border);
      border-radius: 8px;
      padding: 12px 14px;
      position: relative;
    }}

    [data-theme="dark"] .formula-item {{
      background: rgba(15, 23, 42, 0.45);
    }}

    .formula-item-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      gap: 8px;
    }}

    .formula-name {{
      font-family: 'Caveat', cursive;
      font-size: 20px;
      font-weight: 700;
      color: var(--ink-color);
      line-height: 1.2;
    }}

    .formula-badges {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }}

    .star-pill {{
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      background: #fef3c7;
      color: #92400e;
    }}

    [data-theme="dark"] .star-pill {{
      background: #78350f;
      color: #fef3c7;
    }}

    .btn-copy-latex {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .btn-copy-latex:hover {{
      background: var(--surface-alt);
      color: var(--text);
    }}

    .math-display {{
      overflow-x: auto;
      padding: 6px 0;
      color: var(--ink-color);
      font-size: 15px;
    }}

    .formula-note {{
      font-family: 'Kalam', cursive;
      font-size: 13.5px;
      color: var(--ink-muted);
      margin-top: 4px;
      line-height: 1.4;
    }}

    .handwritten-accent {{
      font-weight: 700;
      color: #d97706;
    }}

    /* Pinned Sticky Note */
    .topper-sticky {{
      background-color: var(--sticky-bg);
      border: 1px solid var(--sticky-border);
      border-left: 4px solid #eab308;
      border-radius: 6px;
      padding: 12px 14px;
      margin-top: 16px;
      color: var(--sticky-text);
      position: relative;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
      transform: rotate(-0.5deg);
    }}

    .sticky-pin {{
      position: absolute;
      top: -8px;
      right: 12px;
      font-size: 14px;
    }}

    .sticky-title {{
      font-family: 'Caveat', cursive;
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 2px;
      letter-spacing: 0.02em;
    }}

    .sticky-text {{
      font-family: 'Kalam', cursive;
      font-size: 13.5px;
      line-height: 1.45;
    }}

    /* Card Footer Practice Action */
    .card-footer-actions {{
      margin-top: 16px;
      padding-top: 12px;
      border-top: 1px dashed var(--paper-border);
    }}

    .btn-practice-pyq {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 6px;
      width: 100%;
      padding: 9px 14px;
      border-radius: 8px;
      background: #0f172a;
      color: #ffffff;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s ease;
    }}

    [data-theme="dark"] .btn-practice-pyq {{
      background: #2563eb;
    }}

    .btn-practice-pyq:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    }}

    /* Empty state */
    .empty-state {{
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
      grid-column: 1 / -1;
    }}

    .empty-state-icon {{
      font-size: 42px;
      margin-bottom: 12px;
    }}

    /* Print Stylesheet */
    @media print {{
      .site-header, .mobile-drawer, .drawer-backdrop,
      .formula-hero .hero-actions, .filter-section, .btn-practice-pyq,
      .btn-copy-latex, .site-footer, .footer-massive-learnosha {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
        color: #000000 !important;
      }}
      .formula-hero {{
        padding: 10px 0 !important;
      }}
      .formula-hero-title {{
        font-size: 24px !important;
      }}
      .vault-grid {{
        display: block !important;
        padding: 0 !important;
      }}
      .handwritten-card {{
        page-break-inside: avoid;
        margin-bottom: 20px;
        box-shadow: none !important;
        border: 1px solid #ccc !important;
        background: #ffffff !important;
      }}
      .washi-tape {{
        display: none !important;
      }}
    }}
  </style>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Handwritten Formula Sheets & Revision Vault (Class 9–12)",
    "description": "Free handwritten formula sheets for Class 9–12 Maths, Physics, Chemistry & Biology. KaTeX math, topper memory tricks, and 1-click PYQ practice.",
    "url": "https://learnosha.in/formula-sheets/",
    "publisher": {{
      "@type": "EducationalOrganization",
      "name": "Learnosha",
      "url": "https://learnosha.in"
    }}
  }}
  </script>
</head>
<body>

  <!-- Universal Header Shell -->
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="brand">
        <svg class="brand-logo-icon" width="22" height="23" viewBox="8 6 48 51" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 17V46H45" fill="none" stroke="currentColor" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M29 26.5A10 10 0 0 1 39 36.5" fill="none" stroke="#D97706" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M29 18.5A18 18 0 0 1 47 36.5" fill="none" stroke="#D97706" stroke-opacity=".6" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="29" cy="36.5" r="3" fill="#D97706"/>
        </svg>
        <span class="brand-name">LEARNOSHA</span>
      </a>

      <nav class="nav-links">
        <button id="themeToggleBtn" class="btn-theme-toggle" onclick="toggleTheme()" aria-label="Toggle Dark Mode" title="Toggle Dark/Light Mode">
          <span class="theme-icon-light">☀️</span>
          <span class="theme-icon-dark">🌙</span>
        </button>
        <button class="btn-hamburger" onclick="toggleMobileDrawer(true)" aria-label="Open Navigation Menu">
          ☰ Menu
        </button>
      </nav>
    </div>
  </header>

  <!-- Mobile Slide-Out Drawer & Backdrop -->
  <div id="drawerBackdrop" class="drawer-backdrop" onclick="toggleMobileDrawer(false)"></div>
  <aside id="mobileNavDrawer" class="mobile-drawer" style="position: fixed; top: 0; right: -420px; z-index: 9999; visibility: hidden; pointer-events: none;" aria-label="Navigation Drawer">
    <div class="drawer-header">
      <a href="/" class="brand">
        <svg class="brand-logo-icon" width="22" height="23" viewBox="8 6 48 51" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 17V46H45" fill="none" stroke="currentColor" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M29 26.5A10 10 0 0 1 39 36.5" fill="none" stroke="#D97706" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M29 18.5A18 18 0 0 1 47 36.5" fill="none" stroke="#D97706" stroke-opacity=".6" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="29" cy="36.5" r="3" fill="#D97706"/>
        </svg>
        <span class="brand-name">LEARNOSHA</span>
      </a>
      <button class="drawer-close" onclick="toggleMobileDrawer(false)" aria-label="Close Navigation Menu">✕</button>
    </div>

    <div class="drawer-goal-box">
      <div class="drawer-goal-title">Select Active Track</div>
      <div class="drawer-goal-grid">
        <button class="drawer-goal-btn" onclick="setActiveGoal('cbse'); window.location.href='/practice/?exam=cbse'">
          <span class="drawer-goal-icon">🎯</span>
          <span>CBSE 12</span>
        </button>
        <button class="drawer-goal-btn" onclick="setActiveGoal('neet'); window.location.href='/practice/?exam=neet'">
          <span class="drawer-goal-icon">🩺</span>
          <span>NEET UG</span>
        </button>
        <button class="drawer-goal-btn" onclick="setActiveGoal('jee'); window.location.href='/practice/?exam=jee'">
          <span class="drawer-goal-icon">⚡</span>
          <span>JEE Main</span>
        </button>
        <button class="drawer-goal-btn" onclick="setActiveGoal('jee-adv'); window.location.href='/practice/?exam=jee-adv'">
          <span class="drawer-goal-icon">🔥</span>
          <span>JEE Adv</span>
        </button>
        <button class="drawer-goal-btn" onclick="setActiveGoal('bitsat'); window.location.href='/practice/?exam=bitsat'">
          <span class="drawer-goal-icon">🎯</span>
          <span>BITSAT</span>
        </button>
      </div>
    </div>

    <nav class="drawer-nav">
      <a href="/formula-sheets/" class="drawer-nav-item active" onclick="toggleMobileDrawer(false)" style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid #d97706;">
        <span class="drawer-nav-icon">✍️</span>
        <div>
          <div style="font-weight: 700; color: #d97706;">Handwritten Formula Sheets</div>
          <span class="drawer-nav-desc">513+ Formulas with memory tricks & traps</span>
        </div>
      </a>
      <a href="/syllabus/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">📋</span>
        <div>
          <div>Syllabus & Blueprints</div>
          <span class="drawer-nav-desc">Official 2026–2027 marks weightage</span>
        </div>
      </a>
      <a href="/practice/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">🎯</span>
        <div>
          <div>Practice Hub</div>
          <span class="drawer-nav-desc">Chapterwise questions & sub-topic filters</span>
        </div>
      </a>
      <a href="/repeated/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">🔥</span>
        <div>
          <div>Repeats Radar</div>
          <span class="drawer-nav-desc">11-Year recurrence & twin questions</span>
        </div>
      </a>
      <a href="/paper-maker/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">📝</span>
        <div>
          <div>Paper Maker & Mock</div>
          <span class="drawer-nav-desc">Timed simulator & custom printable tests</span>
        </div>
      </a>
      <a href="/saved/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">📌</span>
        <div>
          <div>Saved Questions & Notes</div>
          <span class="drawer-nav-desc">Personal notebook & bookmarks</span>
        </div>
      </a>
    </nav>
  </aside>

  <!-- Hero Section -->
  <main>
    <section class="formula-hero">
      <div class="handwritten-badge">
        <span>✍️ Authentic Handwritten Style • Topper Revision Vault</span>
      </div>
      <h1 class="formula-hero-title">
        The Formula Sheets Vault <span class="handwritten-title-span">(Topper Notes)</span>
      </h1>
      <p class="formula-hero-subtitle">
        Every essential formula from Class 9 to 12 across Maths, Physics, Chemistry & Biology. Handcrafted with high-yield stickers, common exam traps, and 1-click PYQ bank practice.
      </p>

      <div class="hero-stat-pills">
        <span class="hero-stat-pill">📚 <strong>513</strong> Enriched Formulas</span>
        <span class="hero-stat-pill">📑 <strong>90</strong> NCERT Chapters</span>
        <span class="hero-stat-pill">✨ <strong>100% Free</strong> No Signups</span>
        <span class="hero-stat-pill">⚡ <strong>KaTeX Math</strong> Accelerated</span>
      </div>

      <div class="hero-actions">
        <button class="btn-print-vault" onclick="window.print()">
          <span>🖨️ Print / Save as PDF</span>
        </button>
        <button class="btn-view-toggle" id="viewToggleBtn" onclick="toggleViewMode()">
          <span id="viewModeIcon">📐</span>
          <span id="viewModeText">Switch to Studio View</span>
        </button>
      </div>
    </section>

    <!-- Filters Section -->
    <section class="filter-section">
      <div class="search-box-wrap">
        <svg class="search-icon-svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input 
          type="search" 
          id="formulaSearchInput" 
          class="search-input" 
          placeholder="Search 513+ formulas (e.g. Ohm's Law, Raoult, Coulomb, Nernst, Integration by parts)..." 
          autocomplete="off"
        >
      </div>

      <!-- Class Tabs -->
      <div class="class-tabs-bar" role="tablist">
        <button class="class-tab-btn active" onclick="filterClass('all', this)">All Classes (513)</button>
        <button class="class-tab-btn" onclick="filterClass('Class 12', this)">Class 12 (168)</button>
        <button class="class-tab-btn" onclick="filterClass('Class 11', this)">Class 11 (135)</button>
        <button class="class-tab-btn" onclick="filterClass('Class 10', this)">Class 10 (171)</button>
        <button class="class-tab-btn" onclick="filterClass('Class 9', this)">Class 9 (39)</button>
      </div>

      <!-- Subject Filter Chips -->
      <div class="subject-chips-bar">
        <button class="subject-chip active" onclick="filterSubject('all', this)">All Subjects</button>
        <button class="subject-chip" onclick="filterSubject('Physics', this)">⚛️ Physics</button>
        <button class="subject-chip" onclick="filterSubject('Chemistry', this)">🧪 Chemistry</button>
        <button class="subject-chip" onclick="filterSubject('Mathematics', this)">📐 Mathematics</button>
        <button class="subject-chip" onclick="filterSubject('Biology', this)">🧬 Biology</button>
      </div>
    </section>

    <!-- Formula Cards Grid -->
    <section class="vault-grid" id="vaultGrid">
      {ssr_html_content}
    </section>
  </main>

  <!-- Universal Site Footer -->
  <footer class="site-footer">
    <div class="footer-top-grid">
      <div class="footer-col-brand">
        <div class="footer-brand-title">
          <svg class="brand-logo-icon" width="22" height="23" viewBox="8 6 48 51" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 17V46H45" fill="none" stroke="currentColor" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M29 26.5A10 10 0 0 1 39 36.5" fill="none" stroke="#D97706" stroke-width="3.5" stroke-linecap="round"/>
          <path d="M29 18.5A18 18 0 0 1 47 36.5" fill="none" stroke="#D97706" stroke-opacity=".6" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="29" cy="36.5" r="3" fill="#D97706"/>
        </svg>
          <span>Learnosha</span>
        </div>
        <p class="footer-brand-desc">
          Unified previous year questions archive for CBSE Class 12 PCM, NEET UG, and JEE Main. Pure study material organized by NCERT curriculum with repeat analytics and CBT simulation.
        </p>
      </div>

      <div class="footer-col">
        <span class="footer-col-heading">CBSE Class 12</span>
        <ul class="footer-links-list">
          <li><a href="/cbse-12/physics/electric-charges-and-fields/">Physics (14 Chapters)</a></li>
          <li><a href="/cbse-12/chemistry/solutions/">Chemistry (10 Chapters)</a></li>
          <li><a href="/cbse-12/mathematics/relations-and-functions/">Mathematics (13 Chapters)</a></li>
          <li><a href="/practice/?exam=cbse">Interactive Practice Hub</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <span class="footer-col-heading">Medical (NEET UG)</span>
        <ul class="footer-links-list">
          <li><a href="/practice/?exam=neet">NEET UG 11-Year Archive</a></li>
          <li><a href="/practice/?exam=neet&subject=Physics">NEET Physics</a></li>
          <li><a href="/practice/?exam=neet&subject=Chemistry">NEET Chemistry</a></li>
          <li><a href="/practice/?exam=neet&subject=Botany">NEET Botany</a></li>
          <li><a href="/practice/?exam=neet&subject=Zoology">NEET Zoology</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <span class="footer-col-heading">Engineering (JEE Main)</span>
        <ul class="footer-links-list">
          <li><a href="/practice/?exam=jee&subject=Physics">JEE Physics (5,398 Qs)</a></li>
          <li><a href="/practice/?exam=jee&subject=Chemistry">JEE Chemistry (3,727 Qs)</a></li>
          <li><a href="/practice/?exam=jee&subject=Mathematics">JEE Mathematics (3,542 Qs)</a></li>
          <li><a href="/paper-maker/?exam=jee">3-Hour CBT Simulator</a></li>
          <li><a href="/repeated/?exam=jee">JEE Recurring Concepts</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <span class="footer-col-heading">Study Tools</span>
        <ul class="footer-links-list">
          <li><a href="/formula-sheets/">Handwritten Formula Sheets</a></li>
          <li><a href="/syllabus/">Syllabus & Weightage</a></li>
          <li><a href="/paper-maker/">Custom Paper & CBT Maker</a></li>
          <li><a href="/repeated/">Repeats & Radar</a></li>
          <li><a href="/saved/">Saved Questions Dashboard</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-legal-bar">
      <p class="disclaimer">
        Disclaimer: Independent study resource providing NCERT-aligned past paper revision, repeat pattern analytics, and step-by-step solutions for CBSE and competitive exams. Not affiliated with, endorsed by, or connected to the Central Board of Secondary Education (CBSE) or the National Testing Agency (NTA).
      </p>
      <div class="footer-copy-row">
        <span>© 2026 Learnosha (learnosha.in) • All Rights Reserved.</span>
        <span>Built for calm, focused revision.</span>
      </div>
    </div>

    <div class="footer-massive-learnosha">
      <span>LEARNOSHA</span>
    </div>
  </footer>

  <!-- Complete Master Formula Dataset -->
  <script>
    const MASTER_CHAPTERS = {json.dumps(chapters, ensure_ascii=False)};
  </script>

  <!-- Interactive Client-side Script -->
  <script>
    let currentClass = 'all';
    let currentSubject = 'all';
    let searchQuery = '';
    let isStudioMode = false;

    // Theme Toggle
    function toggleTheme() {{
      const html = document.documentElement;
      const current = html.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }}

    // View Mode Toggle (Handwritten vs Studio)
    function toggleViewMode() {{
      isStudioMode = !isStudioMode;
      document.body.classList.toggle('studio-mode', isStudioMode);
      const icon = document.getElementById('viewModeIcon');
      const text = document.getElementById('viewModeText');
      if (isStudioMode) {{
        icon.textContent = '✍️';
        text.textContent = 'Switch to Handwritten View';
      }} else {{
        icon.textContent = '📐';
        text.textContent = 'Switch to Studio View';
      }}
    }}

    // Mobile Drawer
    function toggleMobileDrawer(open) {{
      const drawer = document.getElementById('mobileNavDrawer');
      const backdrop = document.getElementById('drawerBackdrop');
      if (!drawer || !backdrop) return;
      if (open) {{
        drawer.style.visibility = 'visible';
        drawer.style.pointerEvents = 'auto';
        drawer.style.right = '0';
        backdrop.style.opacity = '1';
        backdrop.style.pointerEvents = 'auto';
      }} else {{
        drawer.style.right = '-420px';
        drawer.style.pointerEvents = 'none';
        backdrop.style.opacity = '0';
        backdrop.style.pointerEvents = 'none';
        setTimeout(() => {{
          if (drawer.style.right === '-420px') drawer.style.visibility = 'hidden';
        }}, 300);
      }}
    }}

    // Copy LaTeX expression to clipboard
    function copyLatex(btn) {{
      const latex = btn.getAttribute('data-latex') || '';
      navigator.clipboard.writeText(latex).then(() => {{
        const oldText = btn.textContent;
        btn.textContent = '✓ Copied!';
        btn.style.color = '#16a34a';
        setTimeout(() => {{
          btn.textContent = oldText;
          btn.style.color = '';
        }}, 2000);
      }}).catch(() => {{
        prompt("Copy LaTeX code:", latex);
      }});
    }}

    // Filter by Class
    function filterClass(cls, btn) {{
      currentClass = cls;
      document.querySelectorAll('.class-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderVault();
    }}

    // Filter by Subject
    function filterSubject(subj, btn) {{
      currentSubject = subj;
      document.querySelectorAll('.subject-chip').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderVault();
    }}

    // Debounced search
    const searchInput = document.getElementById('formulaSearchInput');
    let searchDebounce = null;
    searchInput.addEventListener('input', (e) => {{
      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(() => {{
        searchQuery = e.target.value.trim().toLowerCase();
        renderVault();
      }}, 150);
    }});

    // Render Vault based on filters & search
    const HIGHLIGHT_CLASSES = ['highlight-yellow', 'highlight-blue', 'highlight-green', 'highlight-peach'];

    function renderVault() {{
      const grid = document.getElementById('vaultGrid');
      
      const filtered = MASTER_CHAPTERS.filter(ch => {{
        if (currentClass !== 'all' && ch.class !== currentClass) return false;
        if (currentSubject !== 'all' && ch.subject !== currentSubject) return false;
        if (searchQuery) {{
          const inTitle = ch.chapter_title.toLowerCase().includes(searchQuery);
          const inClass = ch.class.toLowerCase().includes(searchQuery);
          const inSubj = ch.subject.toLowerCase().includes(searchQuery);
          const inFormulas = ch.formulas.some(f => 
            f.name.toLowerCase().includes(searchQuery) || 
            f.expression_raw.toLowerCase().includes(searchQuery) ||
            f.latex.toLowerCase().includes(searchQuery) ||
            (f.note && f.note.toLowerCase().includes(searchQuery))
          );
          if (!inTitle && !inClass && !inSubj && !inFormulas) return false;
        }}
        return true;
      }});

      if (filtered.length === 0) {{
        grid.innerHTML = `
          <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <h3 style="font-size:20px; font-weight:800; color:var(--text); margin-bottom:8px;">No matching formulas found</h3>
            <p style="font-size:14px; margin:0 0 16px;">Try adjusting your search terms or selecting a different class/subject filter.</p>
            <button class="btn-print-vault" onclick="clearFilters()" style="margin:0 auto;">Reset All Filters</button>
          </div>
        `;
        return;
      }}

      let html = '';
      filtered.forEach((ch, idx) => {{
        const hlClass = HIGHLIGHT_CLASSES[idx % HIGHLIGHT_CLASSES.length];
        
        let formulasHtml = '';
        ch.formulas.forEach(f => {{
          const isMatch = !searchQuery || 
            f.name.toLowerCase().includes(searchQuery) || 
            f.expression_raw.toLowerCase().includes(searchQuery) ||
            f.latex.toLowerCase().includes(searchQuery);

          const starBadge = f.high_yield ? '<span class="star-pill">⭐ High-Yield</span>' : '';
          const noteHtml = f.note ? `<div class="formula-note"><span class="handwritten-accent">Note:</span> ${{f.note}}</div>` : '';
          const latexEscaped = escapeHtml(f.latex);

          formulasHtml += `
            <div class="formula-item" style="${{isMatch ? '' : 'opacity:0.6;'}}">
              <div class="formula-item-header">
                <span class="formula-name">${{escapeHtml(f.name)}}</span>
                <div class="formula-badges">
                  ${{starBadge}}
                  <button class="btn-copy-latex" data-latex="${{latexEscaped}}" onclick="copyLatex(this)" title="Copy LaTeX">📋 Copy</button>
                </div>
              </div>
              <div class="math-display">
                $$${{f.latex}}$$
              </div>
              ${{noteHtml}}
            </div>
          `;
        }});

        const topperTip = ch.formulas[0] ? ch.formulas[0].topper_tip : '⭐ Review this sheet thoroughly before board & entrance exams.';

        html += `
          <article class="handwritten-card" data-class="${{ch.class}}" data-subject="${{ch.subject}}">
            <div class="washi-tape"></div>
            <div class="card-top-meta">
              <span class="sheet-tag">${{ch.icon || '📝'}} ${{ch.class}} • ${{ch.subject}}</span>
              <span class="count-pill">${{ch.formula_count}} Formulas</span>
            </div>
            
            <h2 class="chapter-heading">
              <span class="${{hlClass}}">${{escapeHtml(ch.chapter_title)}}</span>
            </h2>
            
            <div class="formulas-container">
              ${{formulasHtml}}
            </div>
            
            <div class="topper-sticky">
              <div class="sticky-pin">📌</div>
              <div class="sticky-title">Topper's Revision Note & Traps:</div>
              <div class="sticky-text">${{escapeHtml(topperTip)}}</div>
            </div>
            
            <div class="card-footer-actions">
              <a href="${{ch.practice_url}}" class="btn-practice-pyq">
                ⚡ Practice ${{escapeHtml(ch.chapter_title)}} PYQs ➔
              </a>
            </div>
          </article>
        `;
      }});

      grid.innerHTML = html;

      // Re-trigger KaTeX rendering on new cards
      if (window.renderMathInElement) {{
        renderMathInElement(grid, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}},
            {{left: '\\(', right: '\\)', display: false}},
            {{left: '\\[', right: '\\]', display: true}}
          ],
          throwOnError: false
        }});
      }}
    }}

    function clearFilters() {{
      currentClass = 'all';
      currentSubject = 'all';
      searchQuery = '';
      searchInput.value = '';
      document.querySelectorAll('.class-tab-btn').forEach((b, i) => b.classList.toggle('active', i === 0));
      document.querySelectorAll('.subject-chip').forEach((b, i) => b.classList.toggle('active', i === 0));
      renderVault();
    }}

    function escapeHtml(str) {{
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    // Auto-render math on DOM load
    document.addEventListener("DOMContentLoaded", function() {{
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {{
        document.documentElement.setAttribute('data-theme', savedTheme);
      }}
      if (window.renderMathInElement) {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}},
            {{left: '\\(', right: '\\)', display: false}},
            {{left: '\\[', right: '\\]', display: true}}
          ],
          throwOnError: false
        }});
      }}
    }});
  </script>
</body>
</html>
'''

os.makedirs('E:/PYQ_Wovrix_Portal/pyq-wovrix/formula-sheets', exist_ok=True)
with open('E:/PYQ_Wovrix_Portal/pyq-wovrix/formula-sheets/index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Saved E:/PYQ_Wovrix_Portal/pyq-wovrix/formula-sheets/index.html successfully!")
print(f"File size: {len(full_html)} bytes")
