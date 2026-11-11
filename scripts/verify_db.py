import sqlite3
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(ROOT, "data", "learnosha_anti_hallucination_master.db")

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("PRAGMA table_info(verified_questions)")
cols = [r[1] for r in c.fetchall()]
assert "subtopic" in cols and "subtopic_slug" in cols, "Columns missing"

c.execute("SELECT COUNT(*) FROM verified_questions WHERE subtopic IS NULL OR subtopic = ''")
empty_cnt = c.fetchone()[0]
assert empty_cnt == 0, f"Empty subtopics: {empty_cnt}"

c.execute("SELECT name FROM sqlite_master WHERE type = 'index'")
idx = [r[0] for r in c.fetchall()]
assert "idx_vh_subtopic" in idx, "Missing idx_vh_subtopic"
assert "idx_vh_subtopic_slug" in idx, "Missing idx_vh_subtopic_slug"

print("SQLite master database verified with subtopic index and populated records")
sys.exit(0)
