const fs = require('fs');
const path = require('path');

function scan(dir) {
  let count = 0;
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) count += scan(p);
    else if (p.endsWith('.html')) {
      const txt = fs.readFileSync(p, 'utf8');
      if (txt.includes('2022?"2026') || txt.includes('CLASS 12 ?') || txt.includes('Portal z"')) {
        count++;
      }
    }
  }
  return count;
}

const errs = scan('cbse-12');
if (errs > 0) {
  console.error('Corrupted files count:', errs);
  process.exit(1);
}
console.log('ENCODING_OK');
