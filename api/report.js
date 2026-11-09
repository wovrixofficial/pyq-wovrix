// Vercel Serverless Function to receive student question reports & solution synchronizations
import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
  res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method === 'POST') {
    try {
      const data = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
      const action = data.action || 'report_issue';

      if (action === 'sync_solution') {
        const solutionEntry = {
          qid: String(data.qid || ''),
          subject: data.subject || '',
          solution: data.solution || '',
          stepRubric: data.stepRubric || '',
          timestamp: data.timestamp || new Date().toISOString()
        };
        console.log('[WOVRIX_SOLUTION_SYNC]', JSON.stringify(solutionEntry));

        return res.status(200).json({
          success: true,
          message: 'Solution synced for overnight morning compilation into permanent cache.',
          qid: solutionEntry.qid
        });
      }

      // Default: Question Issue Report
      const report = {
        qid: String(data.qid || 'unknown'),
        subject: data.subject || 'general',
        year: data.year || '2026',
        chapter: data.chapter || '',
        issues: data.issues || [],
        notes: data.notes || '',
        timestamp: data.timestamp || new Date().toISOString()
      };

      console.log('[WOVRIX_REPORT_LOG]', JSON.stringify(report));

      return res.status(200).json({
        success: true,
        message: 'Report logged successfully for morning auto-fix cycle.',
        reportId: `rep_${Date.now()}`
      });
    } catch (e) {
      return res.status(400).json({ success: false, error: e.message });
    }
  }

  return res.status(200).json({
    status: 'online',
    service: 'Wovrix PYQ Report & Solution Sync Service'
  });
}
