/**
 * Learnosha Privacy-Friendly Telemetry & Analytics
 * Tracks chapter visits and study interactions with zero invasive cookies.
 */
(function() {
  const GA_ID = window.LEARNOSHA_GA_ID || window.WOVRIX_GA_ID || 'G-LEARNOSHA';
  
  // Custom lightweight event logger
  const logEvent = function(eventName, eventParams) {
    try {
      if (window.gtag) {
        window.gtag('event', eventName, eventParams);
      }
      // Internal telemetry storage for popular chapters
      const popular = JSON.parse(localStorage.getItem('learnosha_visited_chapters') || localStorage.getItem('wovrix_visited_chapters') || '{}');
      const ch = eventParams?.chapter || 'general';
      popular[ch] = (popular[ch] || 0) + 1;
      localStorage.setItem('learnosha_visited_chapters', JSON.stringify(popular));
    } catch (e) {}
  };

  window.trackLearnoshaEvent = logEvent;
  window.trackWovrixEvent = logEvent;

  // Track initial page view
  document.addEventListener('DOMContentLoaded', function() {
    const path = window.location.pathname;
    const urlParams = new URLSearchParams(window.location.search);
    const subject = urlParams.get('subject') || 'all';
    const exam = urlParams.get('exam') || 'cbse';

    logEvent('page_view', {
      path: path,
      subject: subject,
      exam: exam
    });
  });
})();
