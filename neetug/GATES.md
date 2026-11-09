# Gates: NEET UG 10-Year Master Archive & Analytics Portal

OWNS: raw_papers/**, NEET_Chapter_Books/**, cache/**, scripts/**, master_neet_questions.json, index.html, vercel.json, package.json

Scope: Full autonomous extraction, categorization, chapter book generation, and analytics portal for 10-year NEET UG (2016-2025).

- [x] G1: Target paper inventory across 2016-2025 cataloged and structured in raw_papers
  CHECK: node scripts/verify-inventory.mjs
  EXPECT: INVENTORY_VERIFIED_2016_2025
  EVIDENCE: automatic-evidence=v1; definition-sha256=ee1207862d34d67a84c74a2ea41bd486dc29bfc2d7a7a3ab1dc6535a421848fb; exit=0; EXPECT=matched; output-sha256=930b3cbd484d728046cef6f9f44d3a238fc22c883efe77e05fb8e2ad8dae95a1; output-bytes=29; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries

- [x] G2: Multi-lane Gemini extraction engine configured with active API key pool and rate-limit guard
  CHECK: node scripts/verify-engine.mjs
  EXPECT: ENGINE_CONFIG_VALIDATED
  EVIDENCE: automatic-evidence=v1; definition-sha256=062c8b94cb5627f6fde188fb643536e7ae1cbdae17f7fb8c4c792f6b1970d094; exit=0; EXPECT=matched; output-sha256=5b9ed6208fbbbfc4078081dc0664864a48c68f58594002004d55d3c726886a93; output-bytes=24; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries

- [x] G3: NEET Question Continuity Oracle verifies question sequences (Q1-180 / Q1-200) without skips
  CHECK: node scripts/verify-oracle.mjs
  EXPECT: CONTINUITY_ORACLE_PASSED
  EVIDENCE: automatic-evidence=v1; definition-sha256=11ff8baebd969f4d7c64aec179125b4cbc7acf170ae815ab6155420be553739a; exit=0; EXPECT=matched; output-sha256=5e0e93a98e2f719f413b9e0387d7f0a030dd889989d9a0988e0b6b10ce43007b; output-bytes=25; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries

- [x] G4: Master questions database populated with verbatim text, options, KaTeX, and archetypes
  CHECK: node scripts/verify-database.mjs
  EXPECT: MASTER_DATABASE_VALIDATED
  EVIDENCE: automatic-evidence=v1; definition-sha256=19904e8d4346f43a84d509f4733e9c105ba8b9c927432a8db61953f07e874651; exit=0; EXPECT=matched; output-sha256=90ff6a8c8f062bcfe5a6094b25725417db40023693c1dbba713388ec37937ae2; output-bytes=26; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries

- [x] G5: 96 NEET Chapter Books generated across Physics, Chemistry, Botany, and Zoology
  CHECK: node scripts/verify-chapter-books.mjs
  EXPECT: CHAPTER_BOOKS_96_VALIDATED
  EVIDENCE: automatic-evidence=v1; definition-sha256=9a710c41e8d89599f204477c183e7fb266c734806f5711e242adf0878f762e45; exit=0; EXPECT=matched; output-sha256=18f001d22708608e57958bf2907ea984b09f0056e30c70926c72752588b76dd6; output-bytes=27; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries

- [x] G6: Production web application index.html built with Command Strip, High-Yield Trends, and 1-Click Practice
  CHECK: node scripts/verify-portal.mjs
  EXPECT: PORTAL_PRODUCTION_BUILD_VERIFIED
  EVIDENCE: automatic-evidence=v1; definition-sha256=2635bdd2b7d0383038a57d1587fbcaa212506c334f313564bd4b8724eeb65e3e; exit=0; EXPECT=matched; output-sha256=f1ec8cca7d8a2bde6f3fc1ed1151463098becb5e5754d03aef56ee006883dd3e; output-bytes=33; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries

- [x] G7: Automated Vercel production deployment configuration validated
  CHECK: node scripts/verify-vercel.mjs
  EXPECT: VERCEL_CONFIG_READY
  EVIDENCE: automatic-evidence=v1; definition-sha256=7dbf98cc667583ea06a510362bde430404c8e0578e6cbdede66c0a19e2b679d4; exit=0; EXPECT=matched; output-sha256=c71f8794340323a5a9a4064181ebfb23f4f32d68a7ac41acf9aa76064345ed4a; output-bytes=20; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\neet-ug-portal; path=db0133271c05/70 entries
