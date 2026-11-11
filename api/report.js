// Vercel Serverless Function to receive & query student question reports & solutions
// Persists directly to GitHub repository issues via authenticated GitHub REST API.

const GITHUB_REPO = 'wovrixofficial/pyq-wovrix';
const GITHUB_TOKEN = process.env.GITHUB_TOKEN;

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // GET: Retrieve all pending student reports from GitHub
  if (req.method === 'GET') {
    try {
      const ghRes = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/issues?labels=student-report&state=open&per_page=50`, {
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'User-Agent': 'WovrixReportsAPI',
          'Accept': 'application/vnd.github.v3+json'
        }
      });

      if (!ghRes.ok) {
        return res.status(200).json({ status: 'online', reports: [], count: 0, note: 'GitHub sync fallback' });
      }

      const issues = await ghRes.json();
      const parsedReports = [];

      for (const iss of issues) {
        // Try extracting JSON payload from issue body
        const jsonMatch = iss.body && iss.body.match(/```json\s*([\s\S]*?)\s*```/);
        if (jsonMatch) {
          try {
            const data = JSON.parse(jsonMatch[1]);
            data.issueNumber = iss.number;
            data.issueUrl = iss.html_url;
            parsedReports.push(data);
          } catch (_) {
            parsedReports.push({
              qid: iss.title.replace(/[^0-9]/g, '') || 'N/A',
              notes: iss.title,
              issueNumber: iss.number,
              timestamp: iss.created_at
            });
          }
        } else {
          parsedReports.push({
            qid: iss.title.replace(/[^0-9]/g, '') || 'N/A',
            notes: iss.title,
            issueNumber: iss.number,
            timestamp: iss.created_at
          });
        }
      }

      return res.status(200).json({
        status: 'online',
        service: 'Learnosha Report & Solution Sync Service',
        count: parsedReports.length,
        reports: parsedReports
      });
    } catch (err) {
      return res.status(200).json({ status: 'online', reports: [], error: err.message });
    }
  }

  // POST: Create a new report or sync a solution to GitHub
  if (req.method === 'POST') {
    try {
      let data = req.body;
      if (typeof data === 'string') {
        try { data = JSON.parse(data); } catch (_) {}
      }
      if (!data || typeof data !== 'object') {
        return res.status(400).json({ success: false, error: 'Invalid JSON payload' });
      }

      const action = data.action || 'report_issue';

      // 1. Solution Synchronization
      if (action === 'sync_solution') {
        const qid = String(data.qid || 'unknown');
        const subject = data.subject || 'General';
        const solution = data.solution || '';

        const issuePayload = {
          title: `[Solution Sync] Question #${qid} (${subject})`,
          body: `### Auto-Synced Solution from Client\n\n- **Question ID**: #${qid}\n- **Subject**: ${subject}\n- **Timestamp**: ${data.timestamp || new Date().toISOString()}\n\n#### Solution Content:\n${solution}\n\n\`\`\`json\n${JSON.stringify(data, null, 2)}\n\`\`\``,
          labels: ['sync-solution', 'solution-queue']
        };

        const ghRes = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/issues`, {
          method: 'POST',
          headers: {
            'Authorization': `token ${GITHUB_TOKEN}`,
            'User-Agent': 'WovrixReportsAPI',
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
          },
          body: JSON.stringify(issuePayload)
        });

        const ghData = ghRes.ok ? await ghRes.json() : null;

        return res.status(200).json({
          success: true,
          message: 'Solution synced to central GitHub queue for morning batch.',
          qid: qid,
          issueNumber: ghData ? ghData.number : null
        });
      }

      // 2. Question Issue Report
      const qid = String(data.qid || 'N/A');
      const subject = data.subject || 'CBSE';
      const year = data.year || 'PYQ';
      const chapter = data.chapter || '';
      const issues = Array.isArray(data.issues) ? data.issues : [];
      const notes = data.notes || '';

      const issuePayload = {
        title: `[Student Report] Question #${qid} (${subject} ${year}): ${issues.join(', ') || 'Issue'}`,
        body: `### Student Question Error Report\n\n- **Question ID**: #${qid}\n- **Subject**: ${subject}\n- **Year**: ${year}\n- **Chapter**: ${chapter}\n- **Issues Reported**: ${issues.join(', ') || 'General'}\n- **Student Notes**: ${notes || 'None'}\n- **Page URL**: ${data.url || 'Direct'}\n- **Timestamp**: ${data.timestamp || new Date().toISOString()}\n\n\`\`\`json\n${JSON.stringify(data, null, 2)}\n\`\`\``,
        labels: ['student-report', subject.toLowerCase().replace(/[^a-z0-9]/g, '')]
      };

      const ghRes = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/issues`, {
        method: 'POST',
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'User-Agent': 'WovrixReportsAPI',
          'Content-Type': 'application/json',
          'Accept': 'application/vnd.github.v3+json'
        },
        body: JSON.stringify(issuePayload)
      });

      const ghData = ghRes.ok ? await ghRes.json() : null;

      return res.status(200).json({
        success: true,
        message: 'Report logged to central GitHub repository.',
        qid: qid,
        issueNumber: ghData ? ghData.number : null,
        issueUrl: ghData ? ghData.html_url : null
      });
    } catch (e) {
      return res.status(500).json({ success: false, error: e.message });
    }
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
