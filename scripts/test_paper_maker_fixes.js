import fs from 'fs';
import path from 'path';

console.log("==========================================");
console.log("TESTING PAPER MAKER MULTI-SUBJECT & OPTIONS FIXES");
console.log("==========================================");

// Load datasets
const jeeP = JSON.parse(fs.readFileSync('data/jee_physics.json', 'utf8'));
const jeeC = JSON.parse(fs.readFileSync('data/jee_chemistry.json', 'utf8'));
const jeeM = JSON.parse(fs.readFileSync('data/jee_mathematics.json', 'utf8'));
const neet = JSON.parse(fs.readFileSync('data/neet_all.json', 'utf8'));

// Normalized options function
function getNormalizedOptions(q) {
  if (!q) return null;

  // 1. Array format
  if (Array.isArray(q.options) && q.options.length > 0) {
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    return q.options.map((opt, i) => ({
      key: String(i + 1),
      letter: letters[i] || String(i + 1),
      label: `(${letters[i] || (i + 1)})`,
      text: typeof opt === 'string' ? opt : (opt.text || opt.value || '')
    }));
  }

  // 2. Object format
  if (q.options && typeof q.options === 'object') {
    // Numeric keys: '1', '2', '3', '4' (e.g. JEE Main)
    if ('1' in q.options || '2' in q.options) {
      const numToLetter = { '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E' };
      const keys = ['1', '2', '3', '4', '5'].filter(k => k in q.options);
      return keys.map(k => ({
        key: k,
        letter: numToLetter[k] || k,
        label: `(${numToLetter[k] || k})`,
        text: String(q.options[k] || '')
      }));
    }

    // Letter keys: 'A', 'B', 'C', 'D' (e.g. NEET, BITSAT)
    const letters = ['A', 'B', 'C', 'D', 'E'];
    const present = letters.filter(l => l in q.options || l.toLowerCase() in q.options);
    if (present.length > 0) {
      return present.map(l => ({
        key: l,
        letter: l,
        label: `(${l})`,
        text: String(q.options[l] ?? q.options[l.toLowerCase()] ?? '')
      }));
    }

    // Any generic keys
    const sortedKeys = Object.keys(q.options).sort();
    if (sortedKeys.length > 0) {
      return sortedKeys.map(k => ({
        key: k,
        letter: k,
        label: `(${k})`,
        text: String(q.options[k] || '')
      }));
    }
  }

  // 3. Fallback: Parse from question text if options not in object (e.g. CBSE MCQs)
  if (q.text && q.text.includes('(A)') && q.text.includes('(B)')) {
    const regex = /\(([A-D])\)\s*([^(\n]+)/g;
    let match;
    const parsed = [];
    while ((match = regex.exec(q.text)) !== null) {
      parsed.push({
        key: match[1],
        letter: match[1],
        label: `(${match[1]})`,
        text: match[2].trim()
      });
    }
    if (parsed.length >= 2) {
      return parsed;
    }
  }

  return null;
}

// TEST 1: Check options normalization for JEE Question
const sampleJee = jeeP.find(q => q.options && q.options['1']);
const jeeOpts = getNormalizedOptions(sampleJee);
console.log("\n[TEST 1] Sample JEE Question Options Normalized:");
console.log("  Question ID:", sampleJee.id);
console.log("  Original options keys:", Object.keys(sampleJee.options));
console.log("  Normalized options count:", jeeOpts.length);
console.log("  Normalized options:", jeeOpts.map(o => `${o.label} ${o.text.slice(0, 30)}`));

if (jeeOpts.length === 4 && jeeOpts[0].label === '(A)') {
  console.log("✔ PASS: JEE options normalized to (A), (B), (C), (D) successfully!");
} else {
  console.error("❌ FAIL: JEE options failed to normalize!");
  process.exit(1);
}

// TEST 2: Check options normalization for NEET Question
const sampleNeet = neet.find(q => q.options && q.options['A']);
const neetOpts = getNormalizedOptions(sampleNeet);
console.log("\n[TEST 2] Sample NEET Question Options Normalized:");
console.log("  Question ID:", sampleNeet.id);
console.log("  Original options keys:", Object.keys(sampleNeet.options));
console.log("  Normalized options count:", neetOpts.length);
console.log("  Normalized options:", neetOpts.map(o => `${o.label} ${o.text.slice(0, 30)}`));

if (neetOpts.length === 4 && neetOpts[0].label === '(A)') {
  console.log("✔ PASS: NEET options normalized to (A), (B), (C), (D) successfully!");
} else {
  console.error("❌ FAIL: NEET options failed to normalize!");
  process.exit(1);
}

// TEST 3: Multi-Subject Sampling (75 questions across 3 subjects)
function shuffleArray(arr) {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function isNumericalQuestion(q) {
  if (!q) return false;
  if (q.type === 'Numerical' || q.type === 'NVQ' || q.question_type === 'numerical') return true;
  if ((q.section || '').toLowerCase().includes('section b')) return true;
  if (/nearest integer|rounded off|numerical value|value of .* is _/i.test(q.text || '')) return true;
  return false;
}

function isValidQuestionForPaper(q, exam = 'jee') {
  if (!q || !q.text || q.text.trim().length === 0) return false;
  const normOptions = getNormalizedOptions(q);
  if (normOptions && normOptions.length >= 2) return true;
  if (isNumericalQuestion(q)) return true;
  if (exam === 'cbse') return true;
  return false;
}

function simulateMultiSubjectSampling(selectedChaptersBySubject, totalRequested) {
  const targetSubjects = Object.keys(selectedChaptersBySubject).filter(s => selectedChaptersBySubject[s].length > 0);
  const numSub = targetSubjects.length;
  const baseQuota = Math.floor(totalRequested / numSub);
  let remainder = totalRequested % numSub;

  const datasetMap = { 'Physics': jeeP, 'Chemistry': jeeC, 'Mathematics': jeeM };
  let allSampled = [];
  const sampledBySub = {};

  for (let i = 0; i < targetSubjects.length; i++) {
    const subj = targetSubjects[i];
    const quota = baseQuota + (remainder > 0 ? 1 : 0);
    if (remainder > 0) remainder--;

    const rawPool = datasetMap[subj] || [];
    const validPool = rawPool.filter(q => isValidQuestionForPaper(q, 'jee'));
    const pool = validPool.length > 0 ? validPool : rawPool;
    const selectedChs = selectedChaptersBySubject[subj];

    let matched = pool.filter(q => {
      const qCh = (q.chapter_name || q.ncert_chapter || '').toLowerCase();
      return selectedChs.some(sc => qCh.includes(sc.toLowerCase()));
    });
    if (matched.length === 0) matched = pool;

    matched.forEach(q => { q.subject = subj; });
    const sampled = shuffleArray(matched).slice(0, quota);
    sampledBySub[subj] = sampled;
  }

  targetSubjects.forEach(s => {
    allSampled = allSampled.concat(sampledBySub[s] || []);
  });

  return allSampled;
}

const mockSelected = {
  'Physics': ['Current Electricity', 'Moving Charges and Magnetism', 'Electrostatic Potential and Capacitance'],
  'Chemistry': ['Solutions', 'Chemical Kinetics', 'Electrochemistry'],
  'Mathematics': ['Matrices', 'Determinants', 'Integrals']
};

const testPaper = simulateMultiSubjectSampling(mockSelected, 75);
console.log("\n[TEST 3] Simulated 75 Question Multi-Subject Sampling:");
console.log("  Total sampled:", testPaper.length);
const subCounts = {};
testPaper.forEach(q => {
  subCounts[q.subject] = (subCounts[q.subject] || 0) + 1;
});
console.log("  Subject breakdown:", subCounts);

if (testPaper.length === 75 && subCounts['Physics'] === 25 && subCounts['Chemistry'] === 25 && subCounts['Mathematics'] === 25) {
  console.log("✔ PASS: Exactly 75 questions evenly sampled (25 Physics, 25 Chemistry, 25 Mathematics)!");
} else {
  console.error("❌ FAIL: Multi-subject distribution incorrect!");
  process.exit(1);
}

// TEST 4: Verify all 75 questions have options in question paper
let withOptions = 0;
let nvqCount = 0;
testPaper.forEach(q => {
  const opts = getNormalizedOptions(q);
  if (opts && opts.length >= 2) withOptions++;
  else if (isNumericalQuestion(q)) nvqCount++;
});
console.log("\n[TEST 4] Paper Options Verification for 75 Qs:");
console.log(`  MCQs with options rendered: ${withOptions} / 75`);
console.log(`  NVQs (Numerical Value Questions): ${nvqCount} / 75`);

if (withOptions + nvqCount === 75 && withOptions >= 30) {
  console.log("✔ PASS: 100% of questions have valid printable options or NVQ answer blanks!");
} else {
  console.error("❌ FAIL: Some questions are missing options!");
  process.exit(1);
}

console.log("\nALL VERIFICATIONS PASSED 100%!");
