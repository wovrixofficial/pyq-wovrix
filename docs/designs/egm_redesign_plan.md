# EGM Specification: Universal Architecture & Streamlined Practice Engine

**Specification ID**: `EGM-SPEC-2026-002`  
**Status**: `Approved for Implementation`  
**Scope**: Full Platform Redesign (`/index.html`, `/practice/index.html`, `/neetug/index.html`, `/cbse-12/...`)

---

## 1. Problem Diagnosis (The Disconnect & Friction)

### 1.1 Cognitive Overload in the Practice Hub
The existing `/practice/index.html` attempted to serve as an analytical cockpit with 15+ concurrent filter pills (archetypes, yield frequencies, years, marks, classes, subjects, sets). For a student revising for board exams or NEET, this created extreme friction: questions felt scattered "here and there".

### 1.2 Fragmented Visual Systems
1. **NEET UG (`/neetug/`)**: Rendered in a disconnected dark/neon color scheme with separate headers and typography, making it feel like a completely different website.
2. **CBSE Hub (`/cbse-12/`)**: Warm paper aesthetic, but lacked seamless one-click cross-navigation back to NEET and the Practice Hub.
3. **Landing Page (`/index.html`)**: Contained encoding artifacts (`2022?"2026`) and lacked cohesive tabs linking directly into both CBSE and NEET chapters.

---

## 2. Universal Design System Invariants

Every page across the entire platform must share identical visual primitives:

| Element | Specification | Rationale |
| :--- | :--- | :--- |
| **Color Scheme** | Warm Editorial Paper (`--bg: #fcfcfb`, `--card-bg: #ffffff`, `--border: #e4e4e7`, `--text: #18181b`, `--accent: #2563eb`) | Eliminates eye strain; renders math formulas like physical printed paper. |
| **Typography** | `Plus Jakarta Sans` (UI / Headings), `Newsreader` (Question & Math Serif), `JetBrains Mono` (Paper & Question Metadata) | Clear visual separation between UI controls, mathematical questions, and exam metadata. |
| **Site Header** | Sticky, unified header featuring the universal SVG `WOVRIX / PYQ` vector logo, exam switcher (`CBSE 12 PCM`, `NEET UG 10-Yr`, `Interactive Practice Hub`), and search shortcut. | Seamless navigation without feeling dropped into disconnected sub-sites. |
| **Site Footer** | Full-width architectural `WOVRIX` typographic wordmark + 4-column directory for CBSE, NEET, Practice, and Legal Disclaimers. | Professional brand grounding on every single page. |

---

## 3. Simplified Interactive Practice Engine (`/practice/index.html`)

### 3.1 Chapter-First Book Reader Protocol
Replace the multi-pill cockpit with an authentic 3-step physical exam book interface:

1. **Top Exam Toggle**: `[ CBSE Class 12 PCM ]` | `[ NEET UG (2016-2026) ]`
2. **Subject Selector**:
   - CBSE: `Physics` | `Chemistry` | `Mathematics`
   - NEET: `Physics` | `Chemistry` | `Botany` | `Zoology`
3. **Chapter Selector**: Clean dropdown or horizontal scroll list showing exact question counts (e.g., *Electrostatics (248 Qs)*, *Solutions (312 Qs)*).
4. **Section Navigation Tabs**:
   - For CBSE: `All` | `Section A (1M MCQs)` | `Section B (2M)` | `Section C (3M)` | `Section D (Case Study / 4M)` | `Section E (5M Long)`
   - For NEET: `All` | `Section A (Core 35)` | `Section B (Optional 15)`
5. **Question Card Layout**:
   - Authentic NCERT typography with KaTeX math rendering.
   - Clean metadata pill: `2026 Set 1 (56-1-1)` or `NEET 2024`.
   - Multi-year repeat alert (e.g., `🔁 Repeated across 2024, 2026`).
   - Dedicated "Show Solution & Marking Scheme" accordion.
   - Mastered / Bookmark quick buttons.

---

## 4. Homepage 3D Interactive Hero (`/index.html`)

- **Interactive 3D Geometric Canvas**: Zero static hero images. Uses Three.js hardware-accelerated rendering featuring 4 floating wireframe geometric shapes (Icosahedron, Dodecahedron, Octahedron, Torus) that subtly follow cursor movement with smooth linear interpolation (lerp).
- **All Core Text Preserved**: Verified dataset counts (7,769 CBSE Distinct Questions, 2,060 NEET UG Questions, 333 Papers).
- **Clean UTF-8 Typography**: Fixes all character encoding issues (en-dashes `–` instead of `?"`).
- **Interactive Multi-Exam Switcher**: Instant switching between CBSE PCM chapter directory and NEET UG subject directory directly on the homepage.

---

## 5. NEET UG Re-Theming (`/neetug/index.html`)

- Complete CSS re-theming from dark/neon to the platform-standard warm paper design system (`style.css`).
- Unified header with the universal logo and direct cross-links to CBSE 12 PCM and Practice Hub.
- Uniform cards, options list, diagram views, and solution reveals matching CBSE format.
