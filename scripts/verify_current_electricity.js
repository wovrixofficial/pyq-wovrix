import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

const currElecFile = path.join(ROOT, 'cbse-12', 'physics', 'current-electricity', 'index.html');
const semiFile = path.join(ROOT, 'cbse-12', 'physics', 'semiconductor-electronics-materials-devices-and-simple-circuits', 'index.html');
const acFile = path.join(ROOT, 'cbse-12', 'physics', 'alternating-current', 'index.html');
const indexFile = path.join(ROOT, 'index.html');

const arg = process.argv[2];

if (arg === '--dedup') {
  const ceHtml = fs.readFileSync(currElecFile, 'utf8');

  const has1854 = ceHtml.includes('href="/practice/?q=1854#card_1854"');
  const has1854Badge = ceHtml.includes('Appeared in 3 Board Sets (2025 Series 55-2)');
  const has1905 = ceHtml.includes('href="/practice/?q=1905#card_1905"');
  const has1945 = ceHtml.includes('href="/practice/?q=1945#card_1945"');

  if (has1854 && has1854Badge && !has1905 && !has1945) {
    console.log('Current Electricity deduplication verified');
    process.exit(0);
  } else {
    console.error('Dedup check failed:', { has1854, has1854Badge, has1905, has1945 });
    process.exit(1);
  }
}

if (arg === '--reclassification') {
  const ceHtml = fs.readFileSync(currElecFile, 'utf8');
  const semiHtml = fs.readFileSync(semiFile, 'utf8');
  const acHtml = fs.readFileSync(acFile, 'utf8');

  // Verify removed from current electricity
  const ceHasDiodes = ceHtml.includes('href="/practice/?q=4598#card_4598"') || ceHtml.includes('href="/practice/?q=218#card_218"');
  const ceHasAc = ceHtml.includes('href="/practice/?q=3674#card_3674"');

  // Verify added to respective chapters
  const semiHasDiodes = semiHtml.includes('href="/practice/?q=4598#card_4598"') && semiHtml.includes('href="/practice/?q=218#card_218"');
  const acHasAc = acHtml.includes('href="/practice/?q=3674#card_3674"');

  if (!ceHasDiodes && !ceHasAc && semiHasDiodes && acHasAc) {
    console.log('Misclassified questions correctly relocated to semiconductor and alternating-current');
    process.exit(0);
  } else {
    console.error('Reclassification check failed:', { ceHasDiodes, ceHasAc, semiHasDiodes, acHasAc });
    process.exit(1);
  }
}

if (arg === '--meta-disclaimer') {
  const idxHtml = fs.readFileSync(indexFile, 'utf8');
  const ceHtml = fs.readFileSync(currElecFile, 'utf8');

  const hasTitle25006 = idxHtml.includes('25,006 Qs') || idxHtml.includes('25,006 Questions');
  const hasFutureProofDisclaimerIdx = idxHtml.includes('Disclaimer: Independent study resource providing NCERT-aligned past paper revision') && !idxHtml.includes('educational non-commercial study');
  const hasFutureProofDisclaimerCe = ceHtml.includes('Disclaimer: Independent study resource providing NCERT-aligned past paper revision');

  if (hasTitle25006 && hasFutureProofDisclaimerIdx && hasFutureProofDisclaimerCe) {
    console.log('Title count 25006 and future-proof disclaimer verified');
    process.exit(0);
  } else {
    console.error('Meta/Disclaimer check failed:', { hasTitle25006, hasFutureProofDisclaimerIdx, hasFutureProofDisclaimerCe });
    process.exit(1);
  }
}

console.error('Unknown argument. Use --dedup, --reclassification, or --meta-disclaimer');
process.exit(2);
