/*
 * ORIGEX — ORX-P01
 * Global Navigation v1.0.0
 * Designed & developed by ORVEAX
 * Copyright © ORVEAX
 */
(() => {
  const body = document.body;
  const mega = document.querySelector('[data-orx-mega]');
  const megaToggle = document.querySelector('[data-orx-mega-toggle]');
  const drawer = document.querySelector('[data-orx-drawer]');
  const backdrop = document.querySelector('[data-orx-backdrop]');
  const openButton = document.querySelector('[data-orx-menu-open]');
  const closeButton = document.querySelector('[data-orx-menu-close]');

  const setMega = (open) => {
    if (!mega || !megaToggle) return;
    mega.classList.toggle('is-open', open);
    megaToggle.setAttribute('aria-expanded', String(open));
  };

  const setDrawer = (open) => {
    if (!drawer || !backdrop || !openButton) return;
    drawer.dataset.open = String(open);
    backdrop.dataset.open = String(open);
    drawer.setAttribute('aria-hidden', String(!open));
    openButton.setAttribute('aria-expanded', String(open));
    body.classList.toggle('nav-open', open);

    if (open) {
      window.setTimeout(() => closeButton?.focus(), 0);
    } else {
      openButton.focus();
    }
  };

  megaToggle?.addEventListener('click', () => {
    const willOpen = !mega.classList.contains('is-open');
    setMega(willOpen);
  });

  document.addEventListener('click', (event) => {
    if (mega?.classList.contains('is-open') && !mega.contains(event.target)) {
      setMega(false);
    }
  });

  openButton?.addEventListener('click', () => setDrawer(true));
  closeButton?.addEventListener('click', () => setDrawer(false));
  backdrop?.addEventListener('click', () => setDrawer(false));
  drawer?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    if (drawer.dataset.open === 'true') setDrawer(false);
  }));

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    if (drawer?.dataset.open === 'true') {
      setDrawer(false);
      return;
    }
    if (mega?.classList.contains('is-open')) {
      setMega(false);
      megaToggle?.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1200 && drawer?.dataset.open === 'true') {
      drawer.dataset.open = 'false';
      backdrop.dataset.open = 'false';
      drawer.setAttribute('aria-hidden', 'true');
      openButton?.setAttribute('aria-expanded', 'false');
      body.classList.remove('nav-open');
    }
  });
})();
