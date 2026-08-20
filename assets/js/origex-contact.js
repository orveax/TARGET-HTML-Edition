/* ORIGEX — PG27 Contact routing + demo form runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const root = document.querySelector('[data-pg27-root]');
  if (!root) return;

  const validTopics = new Set(['general', 'rfq', 'supplier', 'partner']);
  const params = new URLSearchParams(window.location.search);
  const requestedTopic = params.get('topic') || 'general';
  let topic = validTopics.has(requestedTopic) ? requestedTopic : 'general';

  const form = root.querySelector('[data-pg27-form]');
  const topicSelect = root.querySelector('[data-pg27-topic-select]');
  const routeButtons = Array.from(root.querySelectorAll('[data-pg27-route]'));
  const routeCards = Array.from(root.querySelectorAll('[data-pg27-route-card]'));
  const languageLinks = Array.from(document.querySelectorAll('.orx-lang-switch, .orx-mobile-nav a[lang]'));
  const errorBox = root.querySelector('[data-pg27-error]');
  const successBox = root.querySelector('[data-pg27-success]');
  const routeName = root.querySelector('[data-pg27-route-name]');
  const routeEmail = root.querySelector('[data-pg27-route-email]');
  const socialBlock = root.querySelector('[data-pg27-social]');
  const lang = document.documentElement.lang === 'ar' ? 'ar' : 'en';

  const labels = {
    general: { ar: 'استفسار عام', en: 'General enquiry', selector: '[data-pg27-email="general"]' },
    rfq: { ar: 'المشترون وطلبات الأسعار', en: 'Buyer & RFQ', selector: '[data-pg27-email="rfq"]' },
    supplier: { ar: 'تقديم الموردين', en: 'Supplier submissions', selector: '[data-pg27-email="supplier"]' },
    partner: { ar: 'الشراكات والتوزيع', en: 'Partnerships & distribution', selector: '[data-pg27-email="partner"]' }
  };

  const updateUrl = () => {
    const url = new URL(window.location.href);
    url.search = '';
    url.searchParams.set('topic', topic);
    window.history.replaceState({}, '', url);
  };

  const syncLanguageLinks = () => {
    languageLinks.forEach((link) => {
      const raw = link.getAttribute('href');
      if (!raw) return;
      const base = raw.split('?')[0];
      link.setAttribute('href', `${base}?topic=${encodeURIComponent(topic)}`);
    });
  };

  const syncSummary = () => {
    const meta = labels[topic];
    if (routeName) routeName.textContent = meta[lang];
    if (routeEmail) {
      const source = root.querySelector(meta.selector);
      routeEmail.textContent = source?.textContent?.trim() || '';
    }
  };

  const applyTopic = ({ updateHistory = true, focusForm = false } = {}) => {
    if (!validTopics.has(topic)) topic = 'general';
    routeCards.forEach((card) => card.dataset.active = String(card.dataset.pg27RouteCard === topic));
    routeButtons.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.pg27Route === topic)));
    if (topicSelect && topicSelect.value !== topic) topicSelect.value = topic;
    root.dataset.pg27Topic = topic;
    syncSummary();
    syncLanguageLinks();
    if (updateHistory) updateUrl();
    if (focusForm) {
      document.querySelector('#contact-form')?.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
      window.setTimeout(() => topicSelect?.focus(), 80);
    }
  };

  routeButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const next = button.dataset.pg27Route;
      if (!validTopics.has(next)) return;
      topic = next;
      applyTopic({ focusForm: true });
    });
  });

  topicSelect?.addEventListener('change', () => {
    const next = topicSelect.value;
    topic = validTopics.has(next) ? next : 'general';
    applyTopic();
  });

  const requiredFields = form ? Array.from(form.querySelectorAll('[required]')) : [];
  requiredFields.forEach((field) => {
    const clearInvalid = () => field.removeAttribute('aria-invalid');
    field.addEventListener('input', clearInvalid);
    field.addEventListener('change', clearInvalid);
  });

  form?.addEventListener('submit', (event) => {
    event.preventDefault();
    if (errorBox) errorBox.hidden = true;
    if (successBox) successBox.hidden = true;
    root.dataset.pg27FormState = 'idle';

    let firstInvalid = null;
    requiredFields.forEach((field) => {
      const valid = field.validity.valid;
      field.setAttribute('aria-invalid', String(!valid));
      if (!valid && !firstInvalid) firstInvalid = field;
    });

    if (firstInvalid) {
      root.dataset.pg27FormState = 'invalid';
      if (errorBox) {
        errorBox.hidden = false;
        errorBox.focus();
      }
      firstInvalid.focus();
      return;
    }

    root.dataset.pg27FormState = 'demo-confirmed';
    if (successBox) {
      successBox.hidden = false;
      successBox.focus();
    }
  });

  form?.addEventListener('reset', () => {
    window.setTimeout(() => {
      topic = 'general';
      if (errorBox) errorBox.hidden = true;
      if (successBox) successBox.hidden = true;
      root.dataset.pg27FormState = 'idle';
      requiredFields.forEach((field) => field.removeAttribute('aria-invalid'));
      applyTopic();
    }, 0);
  });

  const syncSocialVisibility = () => {
    if (!socialBlock) return;
    const links = Array.from(socialBlock.querySelectorAll('[data-orx-social-link]'));
    socialBlock.hidden = !links.some((link) => !link.hidden && link.getAttribute('href') && link.getAttribute('href') !== '#');
  };

  applyTopic({ updateHistory: requestedTopic !== topic || !params.has('topic') });
  syncSocialVisibility();
  root.dataset.pg27FormState = 'idle';
  root.dataset.pg27Ready = 'true';
})();
