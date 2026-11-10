# PYQ Wovrix • Automated Multi-Channel Traffic & Growth Suite

An autonomous distribution engine that drives student traffic to [https://pyq.wovrix.in](https://pyq.wovrix.in) across Telegram, Reddit, YouTube Shorts, Instagram Reels, and GitHub.

---

## 1. 🩺 Telegram Daily Quiz Bot (100% Automated via GitHub Actions)
Runs every morning at **8:00 AM IST (02:30 UTC)** with zero server maintenance.

- **What it does**: Pulls a high-yield question from the 2,060 NEET archive and posts a native, interactive Telegram Quiz Poll with 4 clickable options, official NTA answer key, and link to the chapter twins on `pyq.wovrix.in`.
- **How to Activate**:
  1. Open Telegram and search for `@BotFather`.
  2. Send `/newbot`, name it, and copy the **API Token**.
  3. Create your public channel (e.g. `t.me/pyq_wovrix`) and add your bot as an **Administrator**.
  4. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
  5. Add two repository secrets:
     - `TELEGRAM_BOT_TOKEN`: Your bot API token.
     - `TELEGRAM_CHANNEL_ID`: Your channel handle (e.g. `@pyq_wovrix` or chat ID).
  6. That's it! GitHub Actions will run `.github/workflows/daily-telegram-quiz.yml` automatically every day.

---

## 2. 🎬 YouTube Shorts & Instagram Reels Generator
Programmatically converts high-probability repeat questions and CBSE step-by-step rubrics into 1080x1920 vertical video reels in 1.5 seconds.

- **Run command**:
  ```bash
  python automation-suite/generate_reels_and_shorts.py
  ```
- **Output**:
  - `automation-suite/output_reels/sample_reel_rectifier.mp4` (1080x1920 60fps vertical reel ready to upload to YouTube Shorts & Instagram Reels).
  - `automation-suite/output_reels/sample_reel_caption.txt` (Optimized viral caption with hooks and hashtags).

---

## 3. 💬 Reddit Student Doubt & PYQ Monitor
Listens in real time for Indian high school students asking for previous year questions, derivations, and solutions on `r/CBSE`, `r/JEENEETards`, and `r/CUETards`.

- **Run command**:
  ```bash
  python automation-suite/reddit_monitor.py
  ```
- **Output**:
  - Scans active threads and saves matching leads to `automation-suite/reddit_student_leads.json`.
  - Crafts helpful, step-by-step answers citing official CBSE/NEET marking keys and linking directly to chapter practice on `pyq.wovrix.in`.

---

## 4. ⭐ GitHub SEO Resource Engine
Google gives exceptionally high search authority to GitHub READMEs for student queries.
- Curate a standalone repository `awesome-cbse-neet-pyq` with direct links to `https://pyq.wovrix.in/repeated/` and `https://pyq.wovrix.in/practice/`.
- Add keywords: `cbse-class-12`, `neet-ug-2026`, `pyq`, `marking-scheme`, `ncert-solutions`.
