# EGM Design Specification: Unified PYQ Wovrix Platform & Mobile Architecture

**Document ID**: `EGM-SPEC-2026-001`  
**Status**: `Draft (Elephant Phase)`  
**Author**: Antigravity (Elephant Agent)  
**Target Date**: Academic Session 2026  
**Scope**: `pyq.wovrix.in` (CBSE Class 12 PCM + NEET UG 10-Year Master Archive)

---

## 1. Problem Statement & Objectives

### Current State & Friction Points
1. **Visual & Copy Disconnect**: Previous iterations retained residual marketing slogans ("Zero-Latency", "Exam Intelligence", "Verified KaTeX Math") that detract from a calm, focused revision environment.
2. **Fragmented Portals**: CBSE Class 12 PCM and NEET UG lived as disparate modules rather than a coherent multi-exam study suite.
3. **Mobile Readability on Budget Devices**: Long mathematical expressions and chemical formulas occasionally risk viewport clipping if not wrapped in dedicated overflow scrollers. Touch targets on some category tags fall below the 48px ergonomic threshold.

### Core Objectives
- **Zero-Slop Guarantee**: Ban all hyperbolic AI adjectives and synthetic marketing claims. Every label must represent an empirical dataset property (e.g., "7,769 Distinct Board Questions", "333 Verified Board Papers").
- **Unified Exam Architecture**: Integrate CBSE Class 12 PCM and NEET UG under a single domain hierarchy with seamless cross-navigation.
- **Flawless Mobile Ergonomics**: Native-like bottom dock, frictionless chapter drawer, and 60FPS KaTeX mathematical rendering with horizontal momentum scroll.

---

## 2. Design System & Typography

### Typography Matrix
| Role | Family | Weight | Purpose |
| :--- | :--- | :--- | :--- |
| **Display / Headings** | `Plus Jakarta Sans` | 800, 900 | High-contrast, clean modern editorial tone. |
| **Mathematical / Academic**| `Newsreader` (Serif) | 400, 500, Italic | Authentic NCERT paper aesthetics for formulas and editorial notes. |
| **UI Controls & Body** | `Plus Jakarta Sans` | 500, 600 | Maximum legibility across small mobile displays. |
| **Technical & Metadata** | `JetBrains Mono` | 600, 700 | Series codes, question IDs, years, marks, and set citations. |

### Color Palette (Monochrome Architectural)
- **Background (`--bg`)**: `#fcfcfb` (Subtle off-white warm paper tone, reducing eye strain).
- **Surface (`--surface`)**: `#ffffff` (Card containers, elevation shadows).
- **Ink / Text (`--text`)**: `#18181b` (Deep obsidian black, AA/AAA contrast).
- **Secondary Ink (`--text-muted`)**: `#52525b` (Subtext, syllabus outlines).
- **Borders (`--border`)**: `#e4e4e7` (Precise 1px drafting lines).
- **Accent (`--accent`)**: `#2563eb` (Precise architectural cobalt for active navigation states).

---

## 3. Structural Layout & Ergonomics

### A. Landing Page Hero (Desktop & Mobile)
- **Background**: Full-bleed architectural SVG featuring an angled exam paper booklet with technical isometric wireframes (Gaussian cube, prism ray dispersion, harmonic waves, solenoid cylinder, drafting set square).
- **Left Column**: Clean, large editorial type (`clamp(38px, 4.4vw, 58px)`) with direct CTAs (`Open Practice Hub ➔`, `NEET UG Archive ➔`, `Browse Chapters ↓`).
- **Mobile Behavior**: Graphic gracefully shifts to an ambient watermark behind a frosted glass container (`rgba(252, 252, 251, 0.92)` + `backdrop-filter: blur(10px)`), preserving 100% text contrast.

### B. Live Telemetry Status Strip
Technical status cells displaying live verified counts:
- `CBSE 12 PCM`: 2022–2026 Papers (333 Papers)
- `DISTINCT QUESTIONS`: 7,769 Problems
- `PARALLEL SET CLONES`: 2,510 Clones
- `NCERT CHAPTERS`: 37 Syllabi
- `NEET UG ARCHIVE`: 2,060 Questions (2016–2026, 135 Diagrams)

### C. Unified Directory Grid
- 3 distinct subject columns: Physics (14 chapters), Chemistry (10 chapters), Mathematics (13 chapters).
- NEET UG 10-Year entrance card featuring Physics, Chemistry, Botany, and Zoology.

### D. Architectural Footer
- Edge-to-edge massive typographic `WOVRIX` wordmark.
- Clean 4-column directory for CBSE, NEET UG, Practice Tools, and Fair Dealing Disclaimer.

---

## 4. Mobile Ergonomics & Math Overflow Safety

1. **KaTeX Overflow Safety**:
   ```css
   .math-content {
     overflow-x: auto;
     -webkit-overflow-scrolling: touch;
     padding: 4px 0;
     max-width: 100%;
   }
   ```
2. **Touch Targets**: Minimum `48px × 48px` bounding box for all interactive buttons and filter chips.
3. **Mobile Sticky Quick-Dock**: Persistent bottom navigation bar on screens `< 768px` enabling instant switching between Practice, CBSE Chapters, NEET UG, and Search.

---

## 5. Verification Oracles & Acceptance Gates

- [ ] **Gate 1 (Zero-Slop)**: Codebase scan confirms zero occurrences of "0ms", "Zero-Latency", "AI-Powered", "Exam Intelligence", or "Verified KaTeX".
- [ ] **Gate 2 (Mobile Viewport)**: Chrome DevTools audit at `375px × 812px` (iPhone) and `768px × 1024px` (iPad) confirms 0 horizontal scroll blowout.
- [ ] **Gate 3 (NEET UG Stitching)**: Direct navigation to `/neetug/` renders 2,060 questions, interactive archetypes, diagrams, and Zen reading mode.
- [ ] **Gate 4 (Performance)**: First Contentful Paint (FCP) < 1.0s on 4G emulation.
