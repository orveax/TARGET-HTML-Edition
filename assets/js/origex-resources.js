/* ORIGEX — ORX-P01 | PG22 Resources runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg22-root]');
  if (!root) return;

  const cards = Array.from(root.querySelectorAll('[data-orx-resource-card]'));
  const buttons = Array.from(root.querySelectorAll('[data-orx-resource-filter]'));
  const count = root.querySelector('[data-orx-resource-count]');
  const empty = root.querySelector('[data-orx-resource-empty]');
  const valid = new Set(buttons.map((button) => button.dataset.orxResourceFilter));
  const params = new URLSearchParams(window.location.search);
  const requested = params.get('category');
  const initial = requested && valid.has(requested) ? requested : 'all';

  const apply = (category, updateUrl = true) => {
    if (!valid.has(category)) category = 'all';
    let visible = 0;
    cards.forEach((card) => {
      const show = category === 'all' || card.dataset.resourceCategory === category;
      card.hidden = !show;
      if (show) visible += 1;
    });
    buttons.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.orxResourceFilter === category)));
    if (count) count.textContent = String(visible);
    if (empty) empty.hidden = visible !== 0;
    root.dataset.pg22Filter = category;
    root.dataset.pg22Visible = String(visible);

    if (updateUrl) {
      const url = new URL(window.location.href);
      if (category === 'all') url.searchParams.delete('category');
      else url.searchParams.set('category', category);
      history.replaceState({}, '', `${url.pathname}${url.search}${url.hash}`);
    }

    document.querySelectorAll('.orx-lang-switch, .orx-mobile-nav a[lang]').forEach((link) => {
      try {
        const url = new URL(link.href, window.location.href);
        if (!url.pathname.endsWith('/resources.html')) return;
        if (category === 'all') url.searchParams.delete('category');
        else url.searchParams.set('category', category);
        link.href = `${url.pathname}${url.search}`;
      } catch (_) {}
    });
  };

  buttons.forEach((button) => button.addEventListener('click', () => apply(button.dataset.orxResourceFilter)));
  apply(initial, false);
  root.dataset.pg22Ready = 'true';
})();