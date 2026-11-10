# Acceptance Gates: PYQ Wovrix UI Remediation & Phase 1 Foundation

- [x] GATE-CSS-RESTORE: Core CSS contains all component and mobile dock classes
  CHECK: node -e "const fs = require('fs'); const css = fs.readFileSync('style.css', 'utf8'); const required = ['.question-card', '.chapter-header-box', '.card-action', '.repeat-pill', '.page-container', '.breadcrumbs', '.question-detail-card', '.mobile-bottom-dock', '.site-header', '[data-theme=\"dark\"]']; const missing = required.filter(c => !css.includes(c)); if (missing.length > 0) { console.error('Missing classes:', missing); process.exit(1); } console.log('ALL_CSS_OK');"
  EXPECT: ALL_CSS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=ffa7024792960972a6ebabf0d2869af9cb2ba94cb9f76acc24a72e3f25b83dd3; exit=0; EXPECT=matched; output-sha256=2168688c384d546fde29dd66cba346e32194c474a49532288e7cf559d41c82af; output-bytes=11; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-ENCODING-CLEANSE: Chapter hubs have zero encoding mojibake
  CHECK: node test_gate2.js
  EXPECT: ENCODING_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=90da179af21146d9cba15931a28478aad98bddbb01a8efda2dae62a2261780b6; exit=0; EXPECT=matched; output-sha256=a88055e1e081485e3e5567c4b64d3504b408c25e3703de2ca101d9ef344444f8; output-bytes=12; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-SUBJECT-HUBS: Subject directory root hubs exist for Physics, Chemistry and Maths
  CHECK: node -e "const fs = require('fs'); const hubs = ['cbse-12/physics/index.html', 'cbse-12/chemistry/index.html', 'cbse-12/mathematics/index.html']; const missing = hubs.filter(h => !fs.existsSync(h)); if (missing.length > 0) { console.error('Missing:', missing); process.exit(1); } console.log('HUBS_OK');"
  EXPECT: HUBS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=776c52fcb48d0c67009f70a459a5d7136d47273108352ac940a3dac97d07f187; exit=0; EXPECT=matched; output-sha256=49afa70f4ecc118523a7d3ebdf90116dacf00484896260e8f2efcf291970209a; output-bytes=8; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-ASSETS-AND-404: 404 page and root favicon exist
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('404.html') || !fs.existsSync('favicon.ico')) { console.error('Missing 404 or favicon'); process.exit(1); } console.log('ASSETS_OK');"
  EXPECT: ASSETS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=8f3e63a459a5ba1f0ef5ae6f9a3784f803b0178c651580fe509c0a813051f88c; exit=0; EXPECT=matched; output-sha256=1f6d03ca8b1ae6e363174024ce973ac82280164a38bf87c20e198d5112c4b9be; output-bytes=10; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-REPEATED-QUESTIONS: Dedicated repeated questions hub and extracted dataset exist
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('repeated/index.html') || !fs.existsSync('data/repeated_questions.json')) { console.error('Missing repeated hub or data'); process.exit(1); } const data = JSON.parse(fs.readFileSync('data/repeated_questions.json', 'utf8')); if (!data.multi_year_repeats || data.multi_year_repeats.length < 19) { console.error('Incomplete data'); process.exit(1); } console.log('REPEATED_OK');"
  EXPECT: REPEATED_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=fec1263a3e816c7a6e4e7dbcdb2c2c28885d163f4ef73ec758a7f2f9ee6a8773; exit=0; EXPECT=matched; output-sha256=8e6934985b30c17d91c86815b95649ca18da1f37a8e83a88b2b1afca10a35711; output-bytes=12; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-PAPER-MAKER: Custom Board Paper Maker page with print layout exists
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('paper-maker/index.html')) { console.error('Missing paper maker'); process.exit(1); } const html = fs.readFileSync('paper-maker/index.html', 'utf8'); if (!html.includes('generatePrintableView') || !html.includes('renderPaperSheet')) { console.error('Missing print CSS or logic'); process.exit(1); } console.log('PAPER_MAKER_OK');"
  EXPECT: PAPER_MAKER_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=370a010ea34e4260a88158253b0b19ce73aa1cc886b331d1ffbbb403412d196c; exit=0; EXPECT=matched; output-sha256=ced89eea8e15b25663b0caad1854d988c2fa76ee12e27f6d4859da52de7201b3; output-bytes=15; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-TRUST-PAGES: About, Privacy, Contact, and Takedown pages exist
  CHECK: node -e "const fs = require('fs'); const pages = ['about/index.html', 'privacy/index.html', 'contact/index.html', 'takedown/index.html']; const missing = pages.filter(p => !fs.existsSync(p)); if (missing.length > 0) { console.error('Missing trust pages:', missing); process.exit(1); } console.log('TRUST_PAGES_OK');"
  EXPECT: TRUST_PAGES_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=1a7053766c26e8c9e833a050a4bb786e675a483b856d82fb86c7bcf983c028ac; exit=0; EXPECT=matched; output-sha256=21607034c540e19a8de21444693777b0c348382c1741ae033735e1ed60413b5e; output-bytes=15; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-STUDY-STORAGE: Client-side study storage and theme switcher script exists
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('js/study_storage.js')) { console.error('Missing study_storage.js'); process.exit(1); } const content = fs.readFileSync('js/study_storage.js', 'utf8'); if (!content.includes('toggleBookmark') || !content.includes('toggleTheme')) { console.error('Missing study functions'); process.exit(1); } console.log('STORAGE_OK');"
  EXPECT: STORAGE_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=7603d2472488dba5b95126c2b112de96e87b448b50a63db8688bd13b88a384a4; exit=0; EXPECT=matched; output-sha256=cff69e113741c44aa7e3e4b8f9c61a5f2de03e71950f4993a4740a75eb76ef9b; output-bytes=11; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-MATH-RECLASSIFY: Determinants chapter has at least 100 questions
  CHECK: node -e "const fs = require('fs'); const data = JSON.parse(fs.readFileSync('data/cbse_mathematics.json', 'utf8')); const det = data.filter(q => q.chapter_name === 'Determinants'); if (det.length < 100) { console.error('Determinants count too low:', det.length); process.exit(1); } console.log('MATH_RECLASSIFY_OK');"
  EXPECT: MATH_RECLASSIFY_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=888f1411df819d73559d13d16dbce12cc128b350e95394c3c8990f0509c675ca; exit=0; EXPECT=matched; output-sha256=0e26e3bae4beb7b457c25e2efcf21e8ac46edc95710656bb52738676b226fb42; output-bytes=19; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-SITEMAP-XML: Sitemap XML exists and indexes all platform routes
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('sitemap.xml')) { console.error('Missing sitemap.xml'); process.exit(1); } const xml = fs.readFileSync('sitemap.xml', 'utf8'); if (!xml.includes('https://pyq.wovrix.in/about/') || !xml.includes('https://pyq.wovrix.in/practice/')) { console.error('Incomplete sitemap'); process.exit(1); } console.log('SITEMAP_OK');"
  EXPECT: SITEMAP_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=a46324a08262eb6939236b3072b5d56d195542c75c00cae15e34f31d9621e4a4; exit=0; EXPECT=matched; output-sha256=b0edf2b690fe1c883312a8284e73bebd441d76681249c00994f3d3c1b3209132; output-bytes=11; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-LINK-INTEGRITY: Zero broken NEET links or dead neetug links
  CHECK: python scripts/verify_links.py
  EXPECT: Link Integrity Audit: PASSED (0 broken NEET or dead /neetug/ links across all files!)
  EVIDENCE: automatic-evidence=v1; definition-sha256=80a9be66dabfc515a191fa838c263b652624dc41ae9351d1b744f58bb6cb38f2; exit=0; EXPECT=matched; output-sha256=76d930bf8ef508e2b03a4425fe8ec46100f6e094103b351e0f207e01f966d7b4; output-bytes=87; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-REPEATS-FREQUENCY-SLIDER: Repeat page has dynamic frequency slider and strict repeat dataset
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('repeated/index.html', 'utf8'); const data = JSON.parse(fs.readFileSync('data/repeated_questions.json', 'utf8')); if (!html.includes('repeatFrequencySlider') || !data.cbse_repeats || data.cbse_repeats.length < 100) { console.error('Missing slider or data'); process.exit(1); } console.log('REPEATS_SLIDER_OK');"
  EXPECT: REPEATS_SLIDER_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=d4c3ee44cbe9583e9271786efde6b6bc866117fa433a09e35c57af10fa472de2; exit=0; EXPECT=matched; output-sha256=550aff02ff3a157efb0f14c69b673b32e51a3ff4bfa7ffce952d3d2f303ba64e; output-bytes=18; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-PAPER-MAKER-NEET: Paper Maker generates both CBSE board papers and NEET UG mock papers
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('paper-maker/index.html', 'utf8'); if (!html.includes('examCardNeet') || !html.includes('CHAPTERS_NEET') || !html.includes('setWizardExam')) { console.error('Missing NEET paper maker'); process.exit(1); } console.log('PAPER_MAKER_NEET_OK');"
  EXPECT: PAPER_MAKER_NEET_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=35be65c2f2cee05e4f8060ba78fa732f5360e3861c9c198a2afa2088c275310a; exit=0; EXPECT=matched; output-sha256=73802653e4fc07eae9bf69f1d3d20abb6d8813a7931b02e307aa5eb798718074; output-bytes=20; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries


- [x] GATE-NEET-CURATED-REPEATS: NEET curated high-yield repeat clusters ingested and max repeats verified
  CHECK: node -e "const fs = require('fs'); const data = JSON.parse(fs.readFileSync('data/repeated_questions.json', 'utf8')); if (!data.summary || data.summary.neet_max_repeats < 30 || data.neet_repeats.length < 50) { console.error('NEET repeats not ingested'); process.exit(1); } console.log('NEET_REPEATS_OK');"
  EXPECT: NEET_REPEATS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=4b2bf30011fa2c991fad521c2c3887c5c01e21c6bc38c2d9cecc795d1268b4dc; exit=0; EXPECT=matched; output-sha256=d6259353e61e01b9f8ffb2f52ce4362a7812ac1209d2984c59a3592881b56bb4; output-bytes=16; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries
- [x] GATE-PRACTICE-WIZARD: Practice hub contains 4-stage streamlined practice wizard (exam, subject, chapter, stream)
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('practice/index.html', 'utf8'); if (!html.includes('viewStepExam') || !html.includes('viewStepSubject') || !html.includes('viewStepChapter') || !html.includes('viewStepStream')) { console.error('Missing 4-stage practice wizard'); process.exit(1); } console.log('PRACTICE_WIZARD_OK');"
  EXPECT: PRACTICE_WIZARD_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=7be29b14f07ecde9553efb4df853c4d43b5c40b9eaf0b87988d54a71c80f611d; exit=0; EXPECT=matched; output-sha256=c411cc772af8ba700b7f3e2a8d7aaddabf78dc632eba0806635e4ee2ffa3a5b3; output-bytes=19; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-LOCAL-14B-PIPELINE: Local Qwen 14B solver script exists and monitors model paths
  CHECK: python scripts/local_qwen_solver.py --status
  EXPECT: === LOCAL 14B QWEN SOLVER PIPELINE STATUS ===
  EVIDENCE: automatic-evidence=v1; definition-sha256=479f8ec4e97dafc9134e49e7c5b3e04a1422e45ccfa75187f43dc57ac3257fd1; exit=0; EXPECT=matched; output-sha256=2b7c8609cf181281e4eb9e24c8c3bc510ddb2beb4947025792fbe1a6fcf26a61; output-bytes=296; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-COMPREHENSIVE-REPEATS: Comprehensive scan yields over 1,500 CBSE clusters and 100+ NEET patterns
  CHECK: node -e "const fs = require('fs'); const data = JSON.parse(fs.readFileSync('data/repeated_questions.json', 'utf8')); if (data.summary.cbse_verified_repeat_clusters < 1500 || data.summary.neet_verified_repeat_clusters < 100) { console.error('Low cluster count'); process.exit(1); } console.log('COMPREHENSIVE_REPEATS_OK');"
  EXPECT: COMPREHENSIVE_REPEATS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=e148cdc536498b42d3ac3454ccac5abb856bbd3544cd7b8766accd8574d6cbcf; exit=0; EXPECT=matched; output-sha256=ebbd9c85b394c177535e496decb1745fcb43cc95a598fbc6eab0c37d270302f3; output-bytes=25; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-SAVED-DASHBOARD: Personal saved dashboard exists with collections, note editor, and mock history
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('saved/index.html')) { console.error('Missing saved page'); process.exit(1); } const html = fs.readFileSync('saved/index.html', 'utf8'); if (!html.includes('folder-chip') || !html.includes('mockHistoryContainer') || !html.includes('exportStudyData')) { console.error('Missing saved dashboard logic'); process.exit(1); } console.log('SAVED_DASHBOARD_OK');"
  EXPECT: SAVED_DASHBOARD_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=1d4c4c7fa22ec4f2697bd5740aa99e8fb56555e653e32456a60316a0a7be5921; exit=0; EXPECT=matched; output-sha256=9004c4e0461ed1563f4807d3d1790b320f68bca6ff0c20463c4996f754077661; output-bytes=19; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-ZERO-UNCLASSIFIED: Zero unclassified questions across CBSE Math, Physics, and Chemistry
  CHECK: node -e "const fs = require('fs'); ['data/cbse_mathematics.json', 'data/cbse_physics.json', 'data/cbse_chemistry.json'].forEach(f => { const data = JSON.parse(fs.readFileSync(f, 'utf8')); const uncl = data.filter(q => q.chapter_name === 'Unclassified'); if (uncl.length > 0) { console.error(f, 'has unclassified:', uncl.length); process.exit(1); } }); console.log('ZERO_UNCLASSIFIED_OK');"
  EXPECT: ZERO_UNCLASSIFIED_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=a026f9578d97d5929436221efb8a4bd8ad6927c59eed8358a66a0712de5aa9bc; exit=0; EXPECT=matched; output-sha256=06dc3f6de08976409ff28d8385b7e53ef6a454e54b1b35f2171761ae536679df; output-bytes=21; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-MOCK-SIMULATOR: Paper maker has 4-step wizard, interactive timed mock engine, and CBT palette
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('paper-maker/index.html', 'utf8'); if (!html.includes('launchInteractiveMock') || !html.includes('cbtJumpTo') || !html.includes('saveActiveMockSession') || !html.includes('reportCardModal')) { console.error('Missing mock simulator components'); process.exit(1); } console.log('MOCK_SIMULATOR_OK');"
  EXPECT: MOCK_SIMULATOR_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=3c0f80685ca9b8dd4b76c34a5e2c5cd6c7ba4d74b107bd007b35a3b965f7db93; exit=0; EXPECT=matched; output-sha256=5afdc4e8117f2aa1bf833861dfd8e096a723097786bae879a23ca2745f54d062; output-bytes=18; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-MOBILE-DRAWER: Universal mobile drawer and backdrop exist across all core pages
  CHECK: node -e "const fs = require('fs'); ['index.html', 'practice/index.html', 'repeated/index.html', 'paper-maker/index.html', 'saved/index.html'].forEach(f => { const html = fs.readFileSync(f, 'utf8'); if (!html.includes('mobileNavDrawer') || !html.includes('drawerBackdrop')) { console.error(f, 'missing mobile drawer'); process.exit(1); } }); console.log('MOBILE_DRAWER_OK');"
  EXPECT: MOBILE_DRAWER_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=7257b05dba9c717cd3cb310e65ad40cb25e63f97a7cd7cb1c218222c51bee3f9; exit=0; EXPECT=matched; output-sha256=fd49655fa487d3c67ccfdfaa015acad08a735548de44c6a4d832224e8b9681df; output-bytes=17; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-COPYRIGHT-BRANDING: Footer copyright uses modern Wovrix (wovrix.in) branding
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('index.html', 'utf8'); if (html.includes('Wovrix Technologies') || !html.includes('Wovrix (wovrix.in)')) { console.error('Copyright string mismatch'); process.exit(1); } console.log('COPYRIGHT_BRANDING_OK');"
  EXPECT: COPYRIGHT_BRANDING_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=4df07e45e93a8234bde1d5bb3014e20b25ced83ddf3c7fc42215ce080e04f07e; exit=0; EXPECT=matched; output-sha256=8266199fb66d7888a768af422815756d1d1718d468a38695665db11b6e2906e8; output-bytes=22; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-UNIVERSAL-DRAWER: Desktop and mobile headers have clean minimal design with slide-out side menu
  CHECK: node -e "const fs = require('fs'); ['index.html', 'practice/index.html', 'repeated/index.html', 'paper-maker/index.html', 'saved/index.html'].forEach(f => { const html = fs.readFileSync(f, 'utf8'); if (!html.includes('btn-hamburger') || !html.includes('mobile-nav-drawer')) { console.error(f, 'missing universal drawer'); process.exit(1); } }); console.log('UNIVERSAL_DRAWER_OK');"
  EXPECT: UNIVERSAL_DRAWER_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=6f6b377b48fd1f74b389b521227ad1be2f5db65ff5f5f6305660050a2677ea83; exit=0; EXPECT=matched; output-sha256=3ea878f4aa57aa9f78b3ef09e0a0eed9a63a3f485f65630017fae66b0149ce18; output-bytes=20; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-HOMEPAGE-BENTO: Homepage has modern Dual-Track Recurrence Leaderboard Bento with CBSE & NEET
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('index.html', 'utf8'); if (html.includes('169 Repeated PYQs') || !html.includes('recurrence-bento') || !html.includes('switchRecurrenceTrack')) { console.error('Outdated repeat radar section or missing bento'); process.exit(1); } console.log('HOMEPAGE_BENTO_OK');"
  EXPECT: HOMEPAGE_BENTO_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=97dc29f70376a81ab71c23aa4e4cb01cf824f2a0a9e91b4a9a5b8bab525c8b08; exit=0; EXPECT=matched; output-sha256=74fa49a784fabc9f72841b1c065eaa0fcc8fbc06899f5c5df3340cc9d8d62f4c; output-bytes=18; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-NEET-REPEAT-SYNC: NEET dataset enriched with repeat clusters from repeated_questions.json
  CHECK: node -e "const fs = require('fs'); const neet = JSON.parse(fs.readFileSync('data/neet_all.json', 'utf8')); const withCluster = neet.filter(q => q.cluster_size && q.cluster_size >= 2); if (withCluster.length < 50) { console.error('NEET repeat clusters missing in neet_all.json:', withCluster.length); process.exit(1); } console.log('NEET_REPEAT_SYNC_OK');"
  EXPECT: NEET_REPEAT_SYNC_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=f4dedf4269acd0e9e667bd1d26e7db36248414928e50475e0743b32f23d6a9cd; exit=0; EXPECT=matched; output-sha256=4554d0f8c82ef0683c4a590945a642f6fad3907142858c3c6c4df8c75be36a25; output-bytes=20; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-DARK-CONTRAST: Dark mode hero and glass cards have high-contrast tokens and Three.js dynamic sync
  CHECK: node -e "const fs = require('fs'); const css = fs.readFileSync('style.css', 'utf8'); const html = fs.readFileSync('index.html', 'utf8'); if (!css.includes('.hero-fullscreen-viewport') || !html.includes('updateThreeTheme')) { process.exit(1); } console.log('DARK_CONTRAST_OK');"
  EXPECT: DARK_CONTRAST_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=603a96977cd11471bb143a1cc9c90ff2bfef748293f2fdfadc1cef0535efd344; exit=0; EXPECT=matched; output-sha256=1ea4c55c41e219b8fa92e00bda90c39d103d74519297bfcb136535c4c8591102; output-bytes=17; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-TOPIC-SELECTOR: Chapter topic taxonomy exists and topic selector pills render in practice hub
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('data/chapter_topics.json')) { console.error('Missing chapter_topics.json'); process.exit(1); } const html = fs.readFileSync('practice/index.html', 'utf8'); if (!html.includes('topic-pill') || !html.includes('filterByTopic')) { console.error('Missing topic selector in practice hub'); process.exit(1); } console.log('TOPIC_SELECTOR_OK');"
  EXPECT: TOPIC_SELECTOR_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=be7958ec03adc4fe88f09d54246af09363ff1c0cb9b1f0d0dbb86b4b1e2733a0; exit=0; EXPECT=matched; output-sha256=7650b60c8178ea5471a2936b679b99fcd95b6e2a4c5ea04f707f6c5602383753; output-bytes=18; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-PROPRIETARY-PROTECTION: Raw AI Vault files and download links are removed from public distribution
  CHECK: node -e "const fs = require('fs'); if (fs.existsSync('vault')) { console.error('vault/ directory still exists'); process.exit(1); } const indexHtml = fs.readFileSync('index.html', 'utf8'); const repHtml = fs.readFileSync('repeated/index.html', 'utf8'); if (indexHtml.includes('Download AI Vault') || repHtml.includes('Download AI Vault') || indexHtml.includes('NEET_UG_10_YEAR_MASTER_AI_VAULT.md')) { console.error('Found public vault download links'); process.exit(1); } console.log('PROPRIETARY_PROTECTION_OK');"
  EXPECT: PROPRIETARY_PROTECTION_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=b01f55d5701e904f969f9df9f315add80ee01c26824ef058999410b7450bd558; exit=0; EXPECT=matched; output-sha256=cbddd0cd4f44780a2f561f6ca27d564e59c008468695ba71855b641927b1f7c9; output-bytes=26; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-NEET-140-CLUSTERS: Authoritative 140 concept clusters and 2000+ repeat questions synced
  CHECK: node -e "const fs = require('fs'); const rep = JSON.parse(fs.readFileSync('data/repeated_questions.json', 'utf8')); const neet = JSON.parse(fs.readFileSync('data/neet_all.json', 'utf8')); if (rep.neet_concepts.length < 140) { console.error('Expected at least 140 concept clusters, got', rep.neet_concepts.length); process.exit(1); } const repeats = neet.filter(q => q.multi_year_count > 1 || q.cluster_size >= 2); if (repeats.length < 2000) { console.error('Expected at least 2000 repeat questions, got', repeats.length); process.exit(1); } console.log('NEET_140_CLUSTERS_OK');"
  EXPECT: NEET_140_CLUSTERS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=6b4574a94c185ad2acddc8b6cc4c6eb3e480399eeef8ff96c128c9fe2750f5c6; exit=0; EXPECT=matched; output-sha256=7101406940cfb6c41334447bacd14647301f0082558c617641d2ef9d180d779c; output-bytes=21; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-HEADER-BOOKMARK-CLEAN: Desktop header hides bookmark pill and horizontal links into slide drawer
  CHECK: node -e "const fs = require('fs'); const css = fs.readFileSync('style.css', 'utf8'); if (!css.includes('.nav-bookmark-pill') || !css.includes('display: none !important')) { console.error('Bookmark pill not hidden in header'); process.exit(1); } console.log('HEADER_BOOKMARK_CLEAN_OK');"
  EXPECT: HEADER_BOOKMARK_CLEAN_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=000ad87c934b56c636c70bd6777042a8d124fde14f38b8bb9690708b8085af6b; exit=0; EXPECT=matched; output-sha256=87641894133830d6a0b7c444ab349fdbd795d0b2aefa87899845f101092dd096; output-bytes=25; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-HEADER-CENTER-EMPTY: Header center is completely clean with zero goal pills across all pages
  CHECK: node -e "const fs = require('fs'); ['index.html', 'practice/index.html', 'repeated/index.html', 'paper-maker/index.html', 'saved/index.html'].forEach(f => { const html = fs.readFileSync(f, 'utf8'); const header = html.slice(html.indexOf('<header'), html.indexOf('</header>')); if (header.includes('goal-switcher-container') || header.includes('nav-link-desktop')) { console.error('Found links or goal switcher in header:', f); process.exit(1); } }); console.log('HEADER_CENTER_EMPTY_OK');"
  EXPECT: HEADER_CENTER_EMPTY_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=48d7199d3f3f7d0bffe467f05bc5e5b6969d9369af8c056f6427eb6629880c05; exit=0; EXPECT=matched; output-sha256=0cd15edc5568a866e87e594bf78e7ad0eac3f92b936368a6ec13b12a645bdd10; output-bytes=23; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-KATEX-HOMEPAGE: KaTeX scripts loaded and auto-rendered on homepage cards
  CHECK: node -e "const fs = require('fs'); const html = fs.readFileSync('index.html', 'utf8'); if (!html.includes('katex.min.js') || !html.includes('auto-render.min.js') || !html.includes('triggerKaTeXRendering')) { console.error('KaTeX missing in index.html'); process.exit(1); } console.log('KATEX_HOMEPAGE_OK');"
  EXPECT: KATEX_HOMEPAGE_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=e5877c63969c6d36c80091b62c99a18e4a6fb4a9803e762336cfb987fc9c9693; exit=0; EXPECT=matched; output-sha256=5364720f7e7fdf18733ee5f0f6aeaca4555bc7e38feec35194c837e54d80c66d; output-bytes=18; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries

- [x] GATE-NEET-CHEM-AVAILABLE: NEET Chemistry has 520 questions and verified repeats count
  CHECK: node -e "const fs = require('fs'); const neet = JSON.parse(fs.readFileSync('data/neet_all.json', 'utf8')); const chem = neet.filter(q => (q.subject || '').toLowerCase() === 'chemistry'); if (chem.length !== 520) { console.error('Chem count expected 520, got', chem.length); process.exit(1); } const rep = chem.filter(q => (q.multi_year_count && q.multi_year_count > 1) || (q.repeat_years && q.repeat_years.length > 1)); if (rep.length < 500) { console.error('Repeat chem count too low:', rep.length); process.exit(1); } console.log('NEET_CHEM_OK');"
  EXPECT: NEET_CHEM_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=4faa28f121349b5ca4edb40346dd76c684b4f66f78cf41ee6c7116a7efd2794b; exit=0; EXPECT=matched; output-sha256=8110f6a0348bf73012e8a1d72a1aed2ac5d572b98417375fa3ef1f9ece5e020a; output-bytes=13; shell=C:\Windows\system32\cmd.exe; cwd=E:\PYQ_Wovrix_Portal\pyq-wovrix; path=da30d265da33/70 entries



