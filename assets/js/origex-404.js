/* ORIGEX — PG28 local recovery search | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg28-root]');
  if (!root) return;

  const input = root.querySelector('[data-pg28-search]');
  const cards = Array.from(root.querySelectorAll('[data-pg28-recovery-card]'));
  const count = root.querySelector('[data-pg28-count]');
  const empty = root.querySelector('[data-pg28-empty]');
  const resetButtons = Array.from(root.querySelectorAll('[data-pg28-reset]'));
  const languageLinks = Array.from(document.querySelectorAll('.orx-lang-switch, .orx-mobile-nav a[lang]'));
  const params = new URLSearchParams(window.location.search);
  const initialQuery = (params.get('q') || '').trim().slice(0, 80);

  const normalize = (value) => String(value || '').trim().toLocaleLowerCase(document.documentElement.lang || undefined);

  const syncLanguageLinks = (query) => {
    languageLinks.forEach((link) => {
      const raw = link.getAttribute('href');
      if (!raw) return;
      const base = raw.split('?')[0];
      link.setAttribute('href', query ? `${base}?q=${encodeURIComponent(query)}` : base);
    });
  };

  const syncUrl = (query) => {
    const url = new URL(window.location.href);
    url.search = '';
    if (query) url.searchParams.set('q', query);
    window.history.replaceState({}, '', url);
  };

  const apply = ({ updateHistory = true, focus = false } = {}) => {
    const rawQuery = (input?.value || '').trim().slice(0, 80);
    const query = normalize(rawQuery);
    let visible = 0;

    cards.forEach((card) => {
      const haystack = normalize(`${card.textContent} ${card.dataset.pg28Search || ''}`);
      const matches = !query || haystack.includes(query);
      card.hidden = !matches;
      if (matches) visible += 1;
    });

    if (count) {
      count.textContent = String(visible);
      count.dataset.pg28ResultCount = String(visible);
    }
    if (empty) empty.hidden = visible !== 0;
    root.dataset.pg28Query = rawQuery;
    root.dataset.pg28ResultCount = String(visible);
    syncLanguageLinks(rawQuery);
    if (updateHistory) syncUrl(rawQuery);
    if (focus) input?.focus();
  };

  input?.addEventListener('input', () => apply());
  input?.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || !input.value) return;
    input.value = '';
    apply({ focus: true });
  });

  resetButtons.forEach((button) => {
    button.addEventListener('click', () => {
      if (input) input.value = '';
      apply({ focus: true });
    });
  });

  if (input && initialQuery) input.value = initialQuery;
  apply({ updateHistory: initialQuery !== (params.get('q') || '') });
  root.dataset.pg28Ready = 'true';
})();
