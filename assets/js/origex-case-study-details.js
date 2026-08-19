/* ORIGEX — ORX-P01 | PG21 Case Study Details runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg21-root]');
  if (!root) return;

  const templates = Array.from(root.querySelectorAll('template[data-case-record]'));
  if (!templates.length) return;

  const records = templates.map((template) => ({
    id: template.dataset.caseId,
    title: template.dataset.caseTitle,
    category: template.dataset.caseCategory,
    focus: template.dataset.caseFocus,
    label: template.dataset.caseLabel,
    summary: template.dataset.caseSummary,
    template
  }));
  const byId = new Map(records.map((record) => [record.id, record]));
  const params = new URLSearchParams(window.location.search);
  const requested = params.get('id');
  const fallback = records[0];
  const record = (requested && byId.get(requested)) || fallback;
  const invalid = Boolean(requested && !byId.has(requested));

  const text = document.documentElement.lang === 'ar'
    ? {
        fallback: 'معرّف الحالة غير متاح في بيانات Demo، لذلك تم عرض الحالة التوضيحية الافتراضية.',
        prev: 'الحالة السابقة',
        next: 'الحالة التالية',
        related: 'شاهد الحالة التوضيحية',
        titleSuffix: 'تفاصيل حالة Demo | ORIGEX'
      }
    : {
        fallback: 'That case ID is not available in the Demo set, so the default illustrative case is shown.',
        prev: 'Previous case',
        next: 'Next case',
        related: 'View Demo case',
        titleSuffix: 'Demo Case Details | ORIGEX'
      };

  const target = root.querySelector('[data-orx-case-detail-target]');
  if (target) target.replaceChildren(record.template.content.cloneNode(true));

  const setText = (selector, value) => {
    const node = root.querySelector(selector);
    if (node) node.textContent = value || '';
  };
  setText('[data-orx-case-title]', record.title);
  setText('[data-orx-case-summary]', record.summary);
  setText('[data-orx-case-label]', record.label);
  setText('[data-orx-case-category]', record.category);
  setText('[data-orx-case-focus]', record.focus);

  const title = document.querySelector('title');
  if (title) title.textContent = `${record.title} | ORIGEX`;

  const notice = root.querySelector('[data-orx-case-fallback]');
  if (notice) {
    notice.hidden = !invalid;
    if (invalid) notice.querySelector('[data-orx-case-fallback-text]').textContent = text.fallback;
  }

  const index = records.findIndex((item) => item.id === record.id);
  const previous = records[(index - 1 + records.length) % records.length];
  const next = records[(index + 1) % records.length];
  const setCaseLink = (selector, item, label) => {
    const link = root.querySelector(selector);
    if (!link) return;
    link.href = `case-study-details.html?id=${encodeURIComponent(item.id)}`;
    link.querySelector('[data-orx-case-nav-label]').textContent = label;
    link.querySelector('[data-orx-case-nav-title]').textContent = item.title;
  };
  setCaseLink('[data-orx-case-prev]', previous, text.prev);
  setCaseLink('[data-orx-case-next]', next, text.next);

  const relatedTarget = root.querySelector('[data-orx-related-cases]');
  if (relatedTarget) {
    const sameFocus = records.filter((item) => item.id !== record.id && item.focus === record.focus);
    const others = records.filter((item) => item.id !== record.id && item.focus !== record.focus);
    const related = [...sameFocus, ...others].slice(0, 2);
    relatedTarget.replaceChildren(...related.map((item) => {
      const article = document.createElement('article');
      article.className = 'orx-case-detail-related-card';
      const badges = document.createElement('div');
      badges.className = 'orx-case-study-card__tags';
      badges.innerHTML = `<span class="orx-badge">${item.category}</span><span class="orx-badge">${item.focus}</span>`;
      const heading = document.createElement('h3');
      heading.textContent = item.title;
      const summary = document.createElement('p');
      summary.textContent = item.summary;
      const link = document.createElement('a');
      link.className = 'orx-text-action';
      link.href = `case-study-details.html?id=${encodeURIComponent(item.id)}`;
      link.textContent = text.related;
      article.append(badges, heading, summary, link);
      return article;
    }));
  }

  document.querySelectorAll('.orx-lang-switch, .orx-mobile-nav a[lang]').forEach((link) => {
    try {
      const url = new URL(link.href, window.location.href);
      if (url.pathname.endsWith('/case-study-details.html')) {
        url.searchParams.set('id', record.id);
        link.href = `${url.pathname}${url.search}`;
      }
    } catch (_) {}
  });
})();