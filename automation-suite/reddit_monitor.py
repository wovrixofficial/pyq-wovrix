import requests
import xml.etree.ElementTree as ET
import json
import os
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

SUBREDDITS = ['CBSE', 'JEENEETards', 'CUETards']
KEYWORDS = [
    'pyq', 'previous year', 'repeat', 'marking scheme', 'derivation',
    'physics', 'chemistry', 'maths', 'neet', 'board', 'question', 'doubt'
]

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'reddit_student_leads.json')

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html)

def scan_reddit_rss():
    leads = []
    print("Scanning r/CBSE, r/JEENEETards, and r/CUETards via real-time RSS...")

    for sub in SUBREDDITS:
        url = f"https://www.reddit.com/r/{sub}/new.rss"
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            if res.status_code != 200:
                print(f"Skipping r/{sub} (Status: {res.status_code})")
                continue

            root = ET.fromstring(res.content)
            # Atom namespace
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('atom:entry', ns)

            for entry in entries:
                title_el = entry.find('atom:title', ns)
                link_el = entry.find('atom:link', ns)
                content_el = entry.find('atom:content', ns)
                author_el = entry.find('atom:author/atom:name', ns)

                title = title_el.text if title_el is not None and title_el.text else ''
                link = link_el.attrib.get('href', '') if link_el is not None else ''
                content = clean_html(content_el.text) if content_el is not None and content_el.text else ''
                author = author_el.text.replace('/u/', '') if author_el is not None and author_el.text else 'student'

                full_text = (title + " " + content).lower()
                matched = [kw for kw in KEYWORDS if kw in full_text]

                if matched:
                    leads.append({
                        'subreddit': f"r/{sub}",
                        'author': author,
                        'title': title,
                        'url': link,
                        'matched_keywords': matched,
                        'suggested_reply': (
                            f"Hey u/{author},\n\n"
                            f"If you need authentic previous year questions for this, check out the 5-year CBSE (2022-2026) and 11-year NEET UG master archive.\n\n"
                            f"• You can practice this exact chapter with official step-by-step marking rubrics here (100% free, zero login required):\n"
                            f"https://pyq.wovrix.in/practice/\n\n"
                            f"• And if you want to see which exact questions are high-probability repeat clones across board sets:\n"
                            f"https://pyq.wovrix.in/repeated/?exam=cbse"
                        )
                    })
        except Exception as e:
            print(f"Error scanning r/{sub}: {e}")

    print(f"\n[SUCCESS] Found {len(leads)} active student threads requesting PYQs/help!")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(leads, f, indent=2)
    print(f"Saved leads and suggested high-value replies to: {OUTPUT_FILE}")

    # Display top 3 live leads
    for i, lead in enumerate(leads[:3]):
        print(f"\n--- Lead #{i+1} [{lead['subreddit']}] by u/{lead['author']} ---")
        print(f"Title: {lead['title']}")
        print(f"Keywords: {lead['matched_keywords']}")
        print(f"Link: {lead['url']}")

    return leads

if __name__ == '__main__':
    scan_reddit_rss()
