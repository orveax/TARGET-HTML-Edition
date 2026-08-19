/* ORIGEX — ORX-P01 | PG15 Markets filter runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-orx-markets-directory]');
  if (!root) return;

  const region = root.querySelector('[data-orx-region-filter]');
  const chips = Array.from(root.querySelectorAll('[data-orx-country-filter]'));
  const cards = Array.from(root.querySelectorAll('[data-orx-market-card]'));
  const empty = root.querySelector('[data-orx-markets-empty]');
  const count = root.querySelector('[data-orx-market-count]');
  let country = 'all';

  const apply = () => {
    const selectedRegion = region?.value || 'all';
    let visible = 0;

    cards.forEach((card) => {
      const regionMatch = selectedRegion === 'all' || card.dataset.region === selectedRegion;
      const countryMatch = country === 'all' || card.dataset.country === country;
      const show = regionMatch && countryMatch;
      card.hidden = !show;
      if (show) visible += 1;
    });

    if (empty) empty.hidden = visible !== 0;
    if (count) count.textContent = String(visible);
  };

  region?.addEventListener('change', apply);

  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      country = chip.dataset.orxCountryFilter || 'all';
      chips.forEach((item) => item.setAttribute('aria-pressed', String(item === chip)));
      apply();
    });
  });

  apply();
})();
