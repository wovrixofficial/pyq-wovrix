import urllib.request
import json
import re
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def test_url(url, check_content=None, check_type=None):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            content = resp.read()
            size = len(content)
            text = content.decode('utf-8', errors='ignore') if check_content else ''
            
            passed = True
            msg = f"[OK {status}] {url} ({size} bytes)"
            if check_content and check_content not in text:
                passed = False
                msg = f"[FAIL content] {url} did not contain '{check_content}'"
            if check_type and check_type not in resp.headers.get('Content-Type', ''):
                passed = False
                msg = f"[FAIL type] {url} Content-Type was {resp.headers.get('Content-Type')}"
            print(msg)
            return passed
    except Exception as e:
        print(f"[ERROR] {url} -> {e}")
        return False

print("=== CHECKING VERIFY TARGETS ===")
# 1. Official 2026-2027 PDFs
p1 = test_url('https://learnosha.in/curriculum_pdf/NEET_UG_Official_Syllabus_2026_2027_NMC.pdf', check_type='pdf')
p2 = test_url('https://learnosha.in/curriculum_pdf/JEE_Main_Official_Syllabus_2026_2027_NTA.pdf', check_type='pdf')
p3 = test_url('https://learnosha.in/curriculum_pdf/NEET_UG_Official_Curriculum_and_Weightage.pdf', check_type='pdf')
p4 = test_url('https://learnosha.in/curriculum_pdf/JEE_Main_Official_Curriculum_and_Weightage.pdf', check_type='pdf')

# 2. Syllabus Page
p5 = test_url('https://learnosha.in/syllabus/', check_content='2026–2027')
p6 = test_url('https://learnosha.in/syllabus/', check_content='footer-massive-learnosha')

# 3. Practice Page
p7 = test_url('https://learnosha.in/practice/', check_content='footer-massive-learnosha')

all_pass = all([p1, p2, p3, p4, p5, p6, p7])
print(f"Overall status: {'ALL PASS' if all_pass else 'SOME FAILED'}")
