/* ORIGEX — PG26 FAQ local search/category runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg26-root]');
  if (!root) return;

  const validCategories = new Set(['all', 'buyers', 'suppliers', 'products', 'rfq', 'distribution', 'demo']);
  const params = new URLSearchParams(window.location.search);
  const requestedCategory = params.get('category') || 'all';
  let category = validCategories.has(requestedCategory) ? requestedCategory : 'all';
  let query = (params.get('q') || '').trim();

  const search = root.querySelector('[data-pg26-search]');
  const categoryButtons = Array.from(root.querySelectorAll('[data-pg26-category]'));
  const items = Array.from(root.querySelectorAll('[data-faq-item]'));
  const groups = Array.from(root.querySelectorAll('[data-faq-group]'));
  const count = root.querySelector('[data-pg26-result-count]');
  const empty = root.querySelector('[data-pg26-empty]');
  const resets = Array.from(root.querySelectorAll('[data-pg26-reset]'));
  const languageLinks = Array.from(document.querySelectorAll('.orx-lang-switch, .orx-mobile-nav a[lang]'));
  const lang = document.documentElement.lang || 'en';

  const normalize = (value) => String(value || '').toLocaleLowerCase(lang === 'ar' ? 'ar' : 'en').trim();

  const updateUrl = () => {
    const url = new URL(window.location.href);
    url.search = '';
    if (category !== 'all') url.searchParams.set('category', category);
    if (query) url.searchParams.set('q', query);
    window.history.replaceState({}, '', url);
  };

  const syncLanguageLinks = () => {
    languageLinks.forEach((link) => {
      const raw = link.getAttribute('href');
      if (!raw) return;
      const base = raw.split('?')[0];
      const next = new URL(base, window.location.href);
      next.search = '';
      if (category !== 'all') next.searchParams.set('category', category);
      if (query) next.searchParams.set('q', query);
      link.setAttribute('href', next.pathname.split('/').slice(-2).join('/') === base ? `${base}${next.search}` : `${base}${next.search}`);
    });
  };

  const updateCategoryCounts = (normalizedQuery) => {
    const counts = { buyers: 0, suppliers: 0, products: 0, rfq: 0, distribution: 0, demo: 0 };
    items.forEach((item) => {
      const categoryName = item.dataset.faqCategory;
      const haystack = normalize(item.dataset.faqSearch || item.textContent);
      if (!normalizedQuery || haystack.includes(normalizedQuery)) counts[categoryName] += 1;
    });
    Object.entries(counts).forEach(([key, value]) => {
      const target = root.querySelector(`[data-pg26-category-count="${key}"]`);
      if (target) target.textContent = String(value);
    });
    const total = root.querySelector('[data-pg26-category-count="all"]');
    if (total) total.textContent = String(Object.values(counts).reduce((sum, value) => sum + value, 0));
  };

  const apply = ({ updateHistory = true } = {}) => {
    const normalizedQuery = normalize(query);
    let visible = 0;

    items.forEach((item) => {
      const categoryMatch = category === 'all' || item.dataset.faqCategory === category;
      const haystack = normalize(item.dataset.faqSearch || item.textContent);
      const queryMatch = !normalizedQuery || haystack.includes(normalizedQuery);
      const show = categoryMatch && queryMatch;
      item.hidden = !show;
      if (show) visible += 1;
    });

    groups.forEach((group) => {
      const hasVisibleItem = Array.from(group.querySelectorAll('[data-faq-item]')).some((item) => !item.hidden);
      group.hidden = !hasVisibleItem;
    });

    categoryButtons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.pg26Category === category));
    });

    if (search && search.value !== query) search.value = query;
    if (count) count.textContent = String(visible);
    if (empty) empty.hidden = visible !== 0;

    updateCategoryCounts(normalizedQuery);
    if (updateHistory) updateUrl();
    syncLanguageLinks();
    root.dataset.pg26Category = category;
    root.dataset.pg26Query = query;
    root.dataset.pg26Results = String(visible);
  };

  categoryButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const next = button.dataset.pg26Category;
      if (!validCategories.has(next)) return;
      category = next;
      apply();
    });
  });

  search?.addEventListener('input', () => {
    query = search.value.trim();
    apply();
  });

  search?.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || !search.value) return;
    event.preventDefault();
    query = '';
    search.value = '';
    apply();
  });

  resets.forEach((button) => {
    button.addEventListener('click', () => {
      category = 'all';
      query = '';
      if (search) search.value = '';
      apply();
      search?.focus();
    });
  });

  if (search) search.value = query;
  apply({ updateHistory: requestedCategory !== category });
  root.dataset.pg26Ready = 'true';
})();
