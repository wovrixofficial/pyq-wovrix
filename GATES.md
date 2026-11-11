# Gates: Subtopic Tagging & CBSE Class 12 Integrity Reconciliation

OWNS: data/**, scripts/**, cbse-12/**, practice/**, index.html, vercel.json

Scope: Add verified subtopic tags to every question across all subjects, index in master AI database, deduplicate Current Electricity, re-assign misclassified questions, and reconcile portal counts.

- [x] G1: Every question across CBSE Physics, Chemistry, and Mathematics has a non-empty subtopic and subtopic_slug tag
  CHECK: node scripts/verify_subtopics.js --cbse
  EXPECT: CBSE subtopic tags verified on 100% of questions (10279/10279)
  EVIDENCE: automatic-evidence=v1; definition-sha256=726c605fad2f55c6129bf1c1f4743fc2dbef885b6ca32816714c7fff4e2cfe3b; exit=0; EXPECT=matched; output-sha256=1df6f4f9bbf2bcc6b3fd0c756967dbd985f7e5943c7ad10ae25f435dfca79c7c; output-bytes=63; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=86b5b58fac2f/70 entries

- [x] G2: Master AI Database (learnosha_anti_hallucination_master.db) has subtopic column populated and indexed
  CHECK: node scripts/verify_subtopics.js --db
  EXPECT: SQLite master database verified with subtopic index and populated records
  EVIDENCE: automatic-evidence=v1; definition-sha256=1f2dd2dd1cf22c7fb8dbd2c3b3871ae46cce3a4df89eebac81ec76b19608342d; exit=0; EXPECT=matched; output-sha256=efaa934f92f61fe701200c5ee8d9208456bb189c5cb6673514a563b4025bf3d3; output-bytes=74; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=86b5b58fac2f/70 entries

- [x] G3: Practice Hub UI renders subtopic pills and filters using direct subtopic_slug matching
  CHECK: node scripts/verify_subtopics.js --practice-ui
  EXPECT: Practice UI subtopic rendering and direct slug matching verified
  EVIDENCE: automatic-evidence=v1; definition-sha256=ed8ff98f5b8db4978a075c16d127c82c0c372659edf4bdb901b94baff4250366; exit=0; EXPECT=matched; output-sha256=cf3d57f62275badf94cb3021277f516d7ddacaeebb56bbc096f597f3b4f7f6f7; output-bytes=65; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=86b5b58fac2f/70 entries

- [x] G4: Current Electricity is deduplicated (cards 1905 and 1945 removed, 1854 displays 3-set badge)
  CHECK: node scripts/verify_current_electricity.js --dedup
  EXPECT: Current Electricity deduplication verified
  EVIDENCE: automatic-evidence=v1; definition-sha256=aff7055eae52f073e8fad491a94c49908ad09d59a8eb42b95aaaecc6146e50d0; exit=0; EXPECT=matched; output-sha256=aea1c3afc2578d36b32c680152c7b17b3ca61e572d14afb208419a445902501e; output-bytes=43; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=86b5b58fac2f/70 entries

- [x] G5: Diode and AC questions are removed from Current Electricity and present on Semiconductor and AC chapter pages
  CHECK: node scripts/verify_current_electricity.js --reclassification
  EXPECT: Misclassified questions correctly relocated to semiconductor and alternating-current
  EVIDENCE: automatic-evidence=v1; definition-sha256=c9cc25cb8cbbacc54625f6aacc2de98f873754ca046e64e6a6c4fae884b6ec9c; exit=0; EXPECT=matched; output-sha256=e369a9bf2f9037319cb9e1a1de093729e49929c9603acb769ca4937f1dda94f3; output-bytes=85; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=86b5b58fac2f/70 entries

- [x] G6: Homepage title and meta tags reconciled to 25,006 questions and footer legal disclaimer updated to future-proof wording
  CHECK: node scripts/verify_current_electricity.js --meta-disclaimer
  EXPECT: Title count 25006 and future-proof disclaimer verified
  EVIDENCE: automatic-evidence=v1; definition-sha256=e78ab9f29f1c692b76f3f7e1e20b51fbef9f7a804251e07147682901abac9d4c; exit=0; EXPECT=matched; output-sha256=46b54746eeff5597770010d13a5a83b4c21003d3711e39f381ce0893506e7e1f; output-bytes=55; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=86b5b58fac2f/70 entries
