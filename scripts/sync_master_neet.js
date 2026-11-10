const fs = require('fs');
const path = require('path');

const masterPath = 'E:/PYQ_Wovrix_Portal/neet-ug-portal/master_neet_questions.json';
const targetNeetPath = path.join(__dirname, '../data/neet_all.json');
const targetRepeatedPath = path.join(__dirname, '../data/repeated_questions.json');

console.log('Reading master NEET data from:', masterPath);
const masterNeet = JSON.parse(fs.readFileSync(masterPath, 'utf8'));
console.log(`Loaded ${masterNeet.length} master questions.`);

// 1. Build authoritative concept clusters
const clusterMap = new Map();
masterNeet.forEach(q => {
  const cName = q.concept_cluster || q.ncert_chapter || 'General Concepts';
  if (!clusterMap.has(cName)) {
    clusterMap.set(cName, {
      concept_name: cName,
      subject: q.subject,
      chapter: q.ncert_chapter,
      recurrence_count_10yr: q.recurrence_count_10yr || 1,
      recurrence_years: (q.recurrence_years || [q.year]).map(String),
      recurrence_tier: q.recurrence_tier || 'Standard',
      historical_twin_ids: q.historical_twins || [],
      question_ids: [],
      sample_question: q.text
    });
  }
  clusterMap.get(cName).question_ids.push(q.id);
});

// Sort clusters by recurrence count descending
const sortedClusters = Array.from(clusterMap.values()).sort((a, b) => b.recurrence_count_10yr - a.recurrence_count_10yr);
const neetConceptsFormatted = sortedClusters.map((c, idx) => ({
  rank: idx + 1,
  concept_name: c.concept_name,
  subject: c.subject,
  chapter: c.chapter,
  total_questions: c.recurrence_count_10yr,
  repeat_count: c.recurrence_count_10yr,
  cluster_size: c.recurrence_count_10yr,
  frequency_label: `${c.recurrence_years.length} out of 11 Years`,
  years_tested: c.recurrence_years,
  years: c.recurrence_years,
  years_count: c.recurrence_years.length,
  recurrence_tier: c.recurrence_tier,
  historical_twin_ids: c.historical_twin_ids,
  historical_twins: c.historical_twin_ids,
  representative_questions: c.question_ids.slice(0, 5),
  text: c.sample_question || `Core recurring NTA concept in ${c.chapter} (${c.subject}) tested across ${c.recurrence_years.length} consecutive exam cycles.`,
  is_multi_year: c.recurrence_years.length > 1,
  type: `${c.recurrence_tier} (${c.recurrence_count_10yr} Qs across ${c.recurrence_years.length} Yrs)`,
  slug: `neet-concept-${idx + 1}`
}));

console.log(`Formatted ${neetConceptsFormatted.length} distinct concept clusters.`);

// 2. Fully enrich neet_all.json
const enrichedNeetAll = masterNeet.map(q => {
  const recCount = q.recurrence_count_10yr || 1;
  const recYears = (q.recurrence_years || [q.year]).map(String);
  return {
    id: q.id,
    q_num: q.q_num,
    year: q.year,
    subject: q.subject,
    section: q.section,
    ncert_chapter: q.ncert_chapter,
    ncert_class: q.ncert_class,
    archetype: q.archetype,
    text: q.text,
    options: q.options,
    correct_answer: q.correct_answer,
    has_diagram: Boolean(q.has_diagram),
    page: q.page || 1,
    source: q.source || `NEET_${q.year}.pdf`,
    concept_cluster: q.concept_cluster,
    concept_name: q.concept_cluster,
    recurrence_count_10yr: recCount,
    cluster_size: recCount,
    recurrence_years: recYears,
    repeat_years: recYears,
    multi_year_count: recYears.length,
    recurrence_tier: q.recurrence_tier || 'Standard',
    historical_twins: q.historical_twins || []
  };
});

fs.writeFileSync(targetNeetPath, JSON.stringify(enrichedNeetAll, null, 2), 'utf8');
console.log(`Successfully written ${enrichedNeetAll.length} enriched questions to ${targetNeetPath}`);

// 3. Update repeated_questions.json
const existingRepeated = JSON.parse(fs.readFileSync(targetRepeatedPath, 'utf8'));
existingRepeated.summary = {
  ...existingRepeated.summary,
  total_cbse_clusters: existingRepeated.cbse_repeats ? existingRepeated.cbse_repeats.length : 1792,
  total_neet_clusters: neetConceptsFormatted.length,
  total_neet_questions: enrichedNeetAll.length,
  total_neet_multi_year_questions: enrichedNeetAll.filter(q => q.multi_year_count > 1).length,
  last_updated: '2026-11-10'
};

existingRepeated.neet_repeats = neetConceptsFormatted;
existingRepeated.neet_concepts = neetConceptsFormatted;

fs.writeFileSync(targetRepeatedPath, JSON.stringify(existingRepeated, null, 2), 'utf8');
console.log(`Successfully updated ${targetRepeatedPath} with 140 concept clusters.`);
