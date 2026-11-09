# Acceptance Gates: PYQ Wovrix UI Remediation & Feature Architecture

- [x] GATE-CSS-RESTORE: Core CSS contains all component and mobile dock classes
  CHECK: node -e "const fs = require('fs'); const css = fs.readFileSync('style.css', 'utf8'); const required = ['.question-card', '.chapter-header-box', '.card-action', '.repeat-pill', '.page-container', '.breadcrumbs', '.question-detail-card', '.mobile-bottom-dock', '.site-header']; const missing = required.filter(c => !css.includes(c)); if (missing.length > 0) { console.error('Missing classes:', missing); process.exit(1); } console.log('ALL_CSS_OK');"
  EXPECT: ALL_CSS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=1b16f61cd807e1edb0aec76d8ef11a1b8a3660d1bb9009f105b6cbd35074c422; exit=0; EXPECT=matched; output-sha256=2168688c384d546fde29dd66cba346e32194c474a49532288e7cf559d41c82af; output-bytes=11; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\pyq-wovrix; path=a420252d42b2/70 entries

- [x] GATE-ENCODING-CLEANSE: Chapter hubs have zero encoding mojibake
  CHECK: node test_gate2.js
  EXPECT: ENCODING_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=90da179af21146d9cba15931a28478aad98bddbb01a8efda2dae62a2261780b6; exit=0; EXPECT=matched; output-sha256=a88055e1e081485e3e5567c4b64d3504b408c25e3703de2ca101d9ef344444f8; output-bytes=12; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\pyq-wovrix; path=a420252d42b2/70 entries

- [x] GATE-SUBJECT-HUBS: Subject directory root hubs exist for Physics, Chemistry and Maths
  CHECK: node -e "const fs = require('fs'); const hubs = ['cbse-12/physics/index.html', 'cbse-12/chemistry/index.html', 'cbse-12/mathematics/index.html']; const missing = hubs.filter(h => !fs.existsSync(h)); if (missing.length > 0) { console.error('Missing:', missing); process.exit(1); } console.log('HUBS_OK');"
  EXPECT: HUBS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=776c52fcb48d0c67009f70a459a5d7136d47273108352ac940a3dac97d07f187; exit=0; EXPECT=matched; output-sha256=49afa70f4ecc118523a7d3ebdf90116dacf00484896260e8f2efcf291970209a; output-bytes=8; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\pyq-wovrix; path=a420252d42b2/70 entries

- [x] GATE-ASSETS-AND-404: 404 page and root favicon exist
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('404.html') || !fs.existsSync('favicon.ico')) { console.error('Missing 404 or favicon'); process.exit(1); } console.log('ASSETS_OK');"
  EXPECT: ASSETS_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=8f3e63a459a5ba1f0ef5ae6f9a3784f803b0178c651580fe509c0a813051f88c; exit=0; EXPECT=matched; output-sha256=1f6d03ca8b1ae6e363174024ce973ac82280164a38bf87c20e198d5112c4b9be; output-bytes=10; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\pyq-wovrix; path=a420252d42b2/70 entries

- [x] GATE-REPEATED-QUESTIONS: Dedicated repeated questions hub and extracted dataset exist
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('repeated/index.html') || !fs.existsSync('data/repeated_questions.json')) { console.error('Missing repeated hub or data'); process.exit(1); } const data = JSON.parse(fs.readFileSync('data/repeated_questions.json', 'utf8')); if (!data.multi_year_repeats || data.multi_year_repeats.length < 19) { console.error('Incomplete data'); process.exit(1); } console.log('REPEATED_OK');"
  EXPECT: REPEATED_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=fec1263a3e816c7a6e4e7dbcdb2c2c28885d163f4ef73ec758a7f2f9ee6a8773; exit=0; EXPECT=matched; output-sha256=8e6934985b30c17d91c86815b95649ca18da1f37a8e83a88b2b1afca10a35711; output-bytes=12; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\pyq-wovrix; path=a420252d42b2/70 entries

- [x] GATE-PAPER-MAKER: Custom Board Paper Maker page with print layout exists
  CHECK: node -e "const fs = require('fs'); if (!fs.existsSync('paper-maker/index.html')) { console.error('Missing paper maker'); process.exit(1); } const html = fs.readFileSync('paper-maker/index.html', 'utf8'); if (!html.includes('@media print') || !html.includes('generatePaper')) { console.error('Missing print CSS or logic'); process.exit(1); } console.log('PAPER_MAKER_OK');"
  EXPECT: PAPER_MAKER_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=d18ee212de64a2155f1a4057f31db8ed12ab62791eab6cd722ff6567d43dabd4; exit=0; EXPECT=matched; output-sha256=ced89eea8e15b25663b0caad1854d988c2fa76ee12e27f6d4859da52de7201b3; output-bytes=15; shell=C:\Windows\system32\cmd.exe; cwd=C:\Users\Srijan\.gemini\antigravity\scratch\pyq-wovrix; path=a420252d42b2/70 entries
