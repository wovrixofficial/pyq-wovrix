import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');
const DATA_DIR = path.join(ROOT, 'data');

const arg = process.argv[2];

if (arg === '--cbse') {
  const files = ['cbse_physics.json', 'cbse_chemistry.json', 'cbse_mathematics.json'];
  let total = 0;
  let tagged = 0;

  for (const f of files) {
    const p = path.join(DATA_DIR, f);
    const data = JSON.parse(fs.readFileSync(p, 'utf8'));
    total += data.length;
    for (const q of data) {
      if (q.subtopic && q.subtopic.trim() !== '' && q.subtopic_slug && q.subtopic_slug.trim() !== '') {
        tagged++;
      }
    }
  }

  if (total === 10279 && tagged === 10279) {
    console.log(`CBSE subtopic tags verified on 100% of questions (${tagged}/${total})`);
    process.exit(0);
  } else {
    console.error(`Mismatch: tagged ${tagged} out of ${total}`);
    process.exit(1);
  }
}

if (arg === '--db') {
  try {
    const res = execSync(`python "${path.join(__dirname, 'verify_db.py')}"`, { encoding: 'utf8' });
    console.log(res.trim());
    process.exit(0);
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
}

if (arg === '--practice-ui') {
  const practicePath = path.join(ROOT, 'practice', 'index.html');
  const content = fs.readFileSync(practicePath, 'utf8');

  const hasTagRender = content.includes('q-subtopic-tag') && content.includes('q.subtopic');
  const hasDirectSlugMatch = content.includes('q.subtopic_slug === currentTopic');

  if (hasTagRender && hasDirectSlugMatch) {
    console.log('Practice UI subtopic rendering and direct slug matching verified');
    process.exit(0);
  } else {
    console.error('Practice UI verification failed:', { hasTagRender, hasDirectSlugMatch });
    process.exit(1);
  }
}

console.error('Unknown argument. Use --cbse, --db, or --practice-ui');
process.exit(2);
