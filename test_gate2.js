import fs from 'fs';

const hubs = [
  'cbse-12/physics/index.html',
  'cbse-12/chemistry/index.html',
  'cbse-12/mathematics/index.html',
  'index.html',
  'practice/index.html',
  'repeated/index.html'
];

let hasError = false;
const mojibakePatterns = [/â€™/, /â€œ/, /â€\x9d/, /Ã/, /â€”/];

for (const hub of hubs) {
  if (fs.existsSync(hub)) {
    const content = fs.readFileSync(hub, 'utf8');
    for (const pat of mojibakePatterns) {
      if (pat.test(content)) {
        console.error(`Encoding issue in ${hub} matching ${pat}`);
        hasError = true;
      }
    }
  }
}

if (hasError) {
  process.exit(1);
} else {
  console.log('ENCODING_OK');
}
