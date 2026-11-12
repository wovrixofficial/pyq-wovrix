import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

function verifyAll() {
  console.log('[VERIFY] Starting Official Syllabus & PDF Vault Verification...');

  // 1. Verify PDFs in curriculum_pdf/
  const expectedPdfs = [
    'Class12_Physics.pdf',
    'Class12_Chemistry.pdf',
    'Class12_Maths.pdf',
    'Class12_Biology.pdf',
    'Class12_Computer_Science.pdf',
    'Class12_English_Core.pdf',
    'Class10_Maths.pdf',
    'Class10_Science.pdf',
    'Class10_Social_Science.pdf',
    'Class10_English.pdf',
    'NEET_UG_Official_Curriculum_and_Weightage.pdf',
    'JEE_Main_Official_Curriculum_and_Weightage.pdf'
  ];

  for (const pdf of expectedPdfs) {
    const fullPath = path.join(ROOT, 'curriculum_pdf', pdf);
    if (!fs.existsSync(fullPath)) {
      throw new Error(`Missing expected PDF: ${pdf}`);
    }
    const stat = fs.statSync(fullPath);
    if (stat.size < 5000) {
      throw new Error(`PDF ${pdf} is suspiciously small: ${stat.size} bytes`);
    }
  }
  console.log(`[PASS] All ${expectedPdfs.length} official curriculum PDFs verified.`);

  // 2. Verify syllabus_entrance.json
  const entPath = path.join(ROOT, 'data', 'syllabus_entrance.json');
  const ent = JSON.parse(fs.readFileSync(entPath, 'utf-8'));

  // NEET
  if (!ent.neet || !ent.neet.subjects) throw new Error('Missing neet subjects in entrance json');
  const neetSubs = Object.keys(ent.neet.subjects);
  if (neetSubs.length !== 4) throw new Error(`Expected 4 NEET subjects, got ${neetSubs.length}`);

  let totalNeet = 0;
  for (const s of neetSubs) {
    const units = ent.neet.subjects[s];
    totalNeet += units.length;
    for (const u of units) {
      if (!u.chapter || !u.priority_tier || !u.official_status || !u.official_topics) {
        throw new Error(`Incomplete NEET unit data in ${s}: ${JSON.stringify(u)}`);
      }
    }
  }
  if (totalNeet !== 41) throw new Error(`Expected 41 NEET units, found ${totalNeet}`);
  console.log(`[PASS] NEET UG 41 chapters verified across 4 subjects with authorized topics.`);

  // JEE Main
  if (!ent.jee_main || !ent.jee_main.subjects) throw new Error('Missing jee_main subjects');
  let totalJee = 0;
  for (const s of Object.keys(ent.jee_main.subjects)) {
    const units = ent.jee_main.subjects[s];
    totalJee += units.length;
    for (const u of units) {
      if (!u.chapter || !u.priority_tier || !u.official_topics) {
        throw new Error(`Incomplete JEE unit data in ${s}: ${JSON.stringify(u)}`);
      }
    }
  }
  if (totalJee !== 54) throw new Error(`Expected 54 JEE Main units, found ${totalJee}`);
  console.log(`[PASS] JEE Main 54 units verified with authorized topics.`);

  // 3. Verify CBSE 12
  const cbse12Path = path.join(ROOT, 'data', 'syllabus_cbse_12.json');
  const cbse12 = JSON.parse(fs.readFileSync(cbse12Path, 'utf-8'));
  for (const subj of Object.keys(cbse12)) {
    const sObj = cbse12[subj];
    if (!sObj.pdf_url) throw new Error(`Missing pdf_url for CBSE 12 ${subj}`);
    for (const ch of sObj.chapters) {
      if (!ch.official_topics || ch.official_topics.trim() === '') {
        throw new Error(`Empty official_topics for CBSE 12 ${subj} chapter ${ch.chapter}`);
      }
    }
  }
  console.log('[PASS] CBSE Class 12 authorized topics and PDF links verified.');

  // 4. Verify CBSE 10
  const cbse10Path = path.join(ROOT, 'data', 'syllabus_cbse_10.json');
  const cbse10 = JSON.parse(fs.readFileSync(cbse10Path, 'utf-8'));
  for (const subj of Object.keys(cbse10)) {
    const sObj = cbse10[subj];
    if (!sObj.pdf_url) throw new Error(`Missing pdf_url for CBSE 10 ${subj}`);
    for (const ch of sObj.chapters) {
      if (!ch.official_topics || ch.official_topics.trim() === '') {
        throw new Error(`Empty official_topics for CBSE 10 ${subj} chapter ${ch.chapter}`);
      }
    }
  }
  console.log('[PASS] CBSE Class 10 authorized topics and PDF links verified.');

  // 5. Verify syllabus/index.html
  const htmlPath = path.join(ROOT, 'syllabus', 'index.html');
  const html = fs.readFileSync(htmlPath, 'utf-8');
  if (!html.includes('NEET_UG_Official_Curriculum_and_Weightage.pdf')) throw new Error('Missing NEET PDF link in html');
  if (!html.includes('JEE_Main_Official_Curriculum_and_Weightage.pdf')) throw new Error('Missing JEE Main PDF link in html');
  if (!html.includes('official-pdf-card')) throw new Error('Missing official-pdf-card CSS class in html');
  if (!html.includes('priority-badge')) throw new Error('Missing priority-badge CSS class in html');

  console.log('[PASS] syllabus/index.html UI and PDF links verified.');
  console.log('ALL VERIFICATIONS PASSED (100% OK)');
}

try {
  verifyAll();
} catch (e) {
  console.error('[FAIL]', e.message);
  process.exit(1);
}
