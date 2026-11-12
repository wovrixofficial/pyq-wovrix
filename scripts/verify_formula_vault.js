import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

console.log("[VERIFY] Starting Handwritten Formula Sheets Vault Verification...");

// 1. Check data/formulas_master.json
const masterPath = path.join(ROOT, 'data', 'formulas_master.json');
if (!fs.existsSync(masterPath)) throw new Error("Missing data/formulas_master.json");
const master = JSON.parse(fs.readFileSync(masterPath, 'utf-8'));
if (master.total_formulas < 500) throw new Error(`Expected at least 500 formulas, got ${master.total_formulas}`);
if (master.total_chapters < 80) throw new Error(`Expected at least 80 chapters, got ${master.total_chapters}`);
console.log(`[PASS] Master dataset verified: ${master.total_formulas} formulas across ${master.total_chapters} chapters.`);

// 2. Check formula-sheets/index.html
const htmlPath = path.join(ROOT, 'formula-sheets', 'index.html');
if (!fs.existsSync(htmlPath)) throw new Error("Missing formula-sheets/index.html");
const html = fs.readFileSync(htmlPath, 'utf-8');
const requiredKeywords = [
  '<!DOCTYPE html>',
  '<title>Handwritten Formula Sheets',
  'Caveat:wght',
  'Kalam:wght',
  'katex.min.css',
  'katex.min.js',
  'washi-tape',
  'topper-sticky',
  'btn-print-vault',
  'formulaSearchInput',
  'footer-massive-learnosha'
];
for (const kw of requiredKeywords) {
  if (!html.includes(kw)) throw new Error(`Missing '${kw}' in formula-sheets/index.html`);
}
console.log("[PASS] formula-sheets/index.html markup, fonts, and scripts verified.");

// 3. Check vercel.json
const vercelPath = path.join(ROOT, 'vercel.json');
const vercel = JSON.parse(fs.readFileSync(vercelPath, 'utf-8'));
for (const r of (vercel.redirects || [])) {
  if (r.source === '/formula-sheets' || r.source === '/formula-sheets/') {
    throw new Error(`Unexpected redirect for ${r.source} in vercel.json`);
  }
}
console.log("[PASS] vercel.json verified: No redirect blocking /formula-sheets/.");

// 4. Check navigation links in other pages
for (const relPage of ['index.html', 'practice/index.html', 'syllabus/index.html']) {
  const p = path.join(ROOT, relPage);
  const content = fs.readFileSync(p, 'utf-8');
  if (!content.includes('/formula-sheets/')) {
    throw new Error(`Missing '/formula-sheets/' link in ${relPage}`);
  }
  console.log(`[PASS] Navigation link verified in ${relPage}`);
}

console.log("\nALL VERIFICATIONS PASSED (100% OK)");
