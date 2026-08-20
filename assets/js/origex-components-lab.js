/* ORIGEX — PG32 Components / Elements QA Laboratory
   Diagnostics only: measures current registered components and never mutates their contracts.
   P09 checkbox diagnostic explicitly measures the registered .orx-check input specimen. */
(() => {
  'use strict';

  const targets = {
    'button-default': { label: 'Control M', target: 48, prop: 'height', mode: 'equal' },
    'button-large': { label: 'Control L', target: 56, prop: 'height', mode: 'equal' },
    'icon-button': { label: '48×48', target: 48, prop: 'square', mode: 'equal' },
    'input': { label: 'Control M', target: 48, prop: 'height', mode: 'equal' },
    'select': { label: 'Control M', target: 48, prop: 'height', mode: 'equal' },
    'textarea': { label: 'Textarea min', target: 144, prop: 'height', mode: 'minimum' },
    'checkbox': { label: 'Visual control', target: 20, prop: 'square', mode: 'equal', selector: '.orx-check input' },
    'upload': { label: 'Dropzone min', target: 144, prop: 'height', mode: 'minimum' },
    'pagination': { label: 'Pagination target', target: 48, prop: 'square', mode: 'equal' }
  };

  const round = value => Math.round(value * 10) / 10;
  const within = (value, target) => Math.abs(value - target) <= 0.75;

  function measure(element, config) {
    const rect = element.getBoundingClientRect();
    if (config.prop === 'square') return { width: round(rect.width), height: round(rect.height) };
    return { height: round(rect.height) };
  }

  function aligned(measurement, config) {
    const values = config.prop === 'square'
      ? [measurement.width, measurement.height]
      : [measurement.height];
    if (config.mode === 'minimum') return values.every(value => value + 0.75 >= config.target);
    return values.every(value => within(value, config.target));
  }

  function formatMeasurement(measurement) {
    if ('width' in measurement) return `${measurement.width} × ${measurement.height}px`;
    return `${measurement.height}px`;
  }

  function runDiagnostics() {
    Object.entries(targets).forEach(([key, config]) => {
      const probe = document.querySelector(config.selector || `[data-lab-probe="${key}"]`);
      const row = document.querySelector(`[data-lab-diagnostic-row="${key}"]`);
      if (!probe || !row) return;

      const measurement = measure(probe, config);
      const state = aligned(measurement, config) ? 'aligned' : 'backfit';
      row.dataset.state = state;

      const current = row.querySelector('[data-lab-current]');
      const badge = row.querySelector('[data-lab-state]');
      if (current) current.textContent = formatMeasurement(measurement);
      if (badge) {
        badge.dataset.state = state;
        badge.textContent = state === 'aligned' ? 'ALIGNED' : 'BACKFIT';
      }
    });

    document.documentElement.dataset.pg32Diagnostics = 'ready';
  }

  function setupDemoForm() {
    document.querySelectorAll('[data-lab-demo-form]').forEach(form => {
      const success = form.querySelector('[data-lab-form-success]');
      const error = form.querySelector('[data-lab-form-error]');
      const email = form.querySelector('input[type="email"]');

      form.addEventListener('submit', event => {
        event.preventDefault();
        const valid = form.checkValidity();
        if (success) success.hidden = !valid;
        if (error) error.hidden = valid;
        if (!valid) {
          form.reportValidity();
          const invalid = form.querySelector(':invalid');
          if (invalid) invalid.focus();
        }
      });

      form.addEventListener('reset', () => {
        if (success) success.hidden = true;
        if (error) error.hidden = true;
        if (email) email.removeAttribute('aria-invalid');
      });
    });
  }

  function setupErrorSpecimen() {
    document.querySelectorAll('[data-lab-error-input]').forEach(input => {
      input.setAttribute('aria-invalid', 'true');
    });
  }

  const ready = () => {
    setupDemoForm();
    setupErrorSpecimen();
    requestAnimationFrame(runDiagnostics);
    window.addEventListener('resize', () => requestAnimationFrame(runDiagnostics), { passive: true });
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready, { once: true });
  else ready();
})();
