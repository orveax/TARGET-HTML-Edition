/* ORIGEX — ORX-P01 | PG09 Product Categories filter adapter | Copyright © ORVEAX */
(() => {
  'use strict';
  const group = document.querySelector('[data-pg09-filters]');
  const grid = document.querySelector('[data-pg09-grid]');
  if (!group || !grid) return;

  const cards = Array.from(grid.querySelectorAll('[data-category]'));
  const filters = Array.from(group.querySelectorAll('[data-category-filter]'));

  const apply = (value) => {
    cards.forEach((card) => {
      card.hidden = value !== 'all' && card.dataset.category !== value;
    });
    filters.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.categoryFilter === value)));
    grid.dataset.activeCategory = value;
  };

  filters.forEach((button) => button.addEventListener('click', () => apply(button.dataset.categoryFilter || 'all')));
  apply('all');
})();
