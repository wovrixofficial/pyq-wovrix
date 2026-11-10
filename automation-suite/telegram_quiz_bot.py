import os
import json
import random
import requests

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '9016562499:AAEhGsDtPIDMgEtbV7PFSVWdinW9XB6ex4w')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID', '@pyq_wovrix')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEET_JSON = os.path.join(REPO_ROOT, 'data', 'neet_all.json')

def load_random_neet_mcq():
    if not os.path.exists(NEET_JSON):
        print(f"File not found: {NEET_JSON}")
        return None

    with open(NEET_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Filter for high-yield questions with valid options
    valid_qs = [
        q for q in data 
        if q.get('options') and isinstance(q.get('options'), dict) 
        and q.get('correct_answer') in ['A', 'B', 'C', 'D']
        and len(q.get('options', {})) == 4
    ]

    # Prioritize 5x+ Ultra-Yield or High-Yield if available
    high_yield = [q for q in valid_qs if 'Ultra-Yield' in q.get('recurrence_tier', '') or q.get('multi_year_count', 0) >= 3]
    pool = high_yield if high_yield else valid_qs

    return random.choice(pool)

def clean_latex(text):
    if not text:
        return ''
    # Replace common LaTeX tokens with clean unicode
    clean = text.replace('\\mu', 'μ').replace('\\alpha', 'α').replace('\\beta', 'β')
    clean = clean.replace('\\pi', 'π').replace('\\theta', 'θ').replace('\\lambda', 'λ')
    clean = clean.replace('\\times', '×').replace('\\pm', '±')
    clean = clean.replace('$', '').replace('{', '').replace('}', '')
    clean = ' '.join(clean.split())
    return clean

def post_quiz_to_telegram(dry_run=False):
    q = load_random_neet_mcq()
    if not q:
        print("No valid MCQ found.")
        return

    year = q.get('year', '2026')
    subj = q.get('subject', 'NEET UG')
    chapter = q.get('ncert_chapter', '')
    repeats = q.get('multi_year_count', 1)

    raw_text = clean_latex(q.get('text', ''))
    
    # Telegram poll question max length is 300 characters
    prefix = f"🩺 [{subj} • {chapter}] ({repeats}x Repeat)\n"
    max_len = 295 - len(prefix)
    if len(raw_text) > max_len:
        raw_text = raw_text[:max_len-3] + '...'
    
    poll_question = prefix + raw_text

    options = []
    correct_idx = 0
    correct_opt = q.get('correct_answer', 'A')

    for i, key in enumerate(['A', 'B', 'C', 'D']):
        val = clean_latex(q.get('options', {}).get(key, ''))
        # Telegram option max length is 100 characters
        if len(val) > 95:
            val = val[:90] + '...'
        options.append(val if val else f"Option {key}")
        if key == correct_opt:
            correct_idx = i

    q_id = q.get('id', f'NEET_{year}')
    explanation = f"Official NTA Key: ({correct_opt}). Drill chapter twins & step rubric: https://pyq.wovrix.in/practice/?q={q_id}"
    if len(explanation) > 195:
        explanation = explanation[:190] + '...'

    print("=== DAILY TELEGRAM QUIZ PREVIEW ===")
    print(f"Question ({len(poll_question)} chars): {poll_question}")
    print(f"Options: {options}")
    print(f"Correct Option: Index {correct_idx} ({correct_opt})")
    print(f"Explanation: {explanation}")

    if dry_run or not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHANNEL_ID:
        print("\n[NOTE] Dry-run complete. Ready to auto-post daily via GitHub Actions!")
        return

    # Post live to Telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPoll"
    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'question': poll_question,
        'options': json.dumps(options),
        'is_anonymous': True,
        'type': 'quiz',
        'correct_option_id': correct_idx,
        'explanation': explanation
    }

    res = requests.post(url, data=payload, timeout=10)
    print(f"Telegram API Response: {res.status_code} - {res.text}")

if __name__ == '__main__':
    post_quiz_to_telegram(dry_run=False)
