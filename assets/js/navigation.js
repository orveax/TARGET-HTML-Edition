/*
 * ORIGEX — ORX-P01
 * Global Navigation v1.1.0
 * Designed & developed by ORVEAX
 * Copyright © ORVEAX
 */
(() => {
  /* Backward-compatible Config Loader.
   * Existing pages only need navigation.js. New pages may load config.js and
   * config-engine.js explicitly before navigation.js for clearer source order.
   */
  const bootConfig = () => {
    const current = document.currentScript;
    if (!current?.src) return;

    const jsBase = new URL("./", current.src);
    const assetsBase = new URL("../", jsBase);

    if (!document.querySelector("link[data-orx-config-ui]")) {
      const css = document.createElement("link");
      css.rel = "stylesheet";
      css.href = new URL("css/config-ui.css", assetsBase).href;
      css.dataset.orxConfigUi = "true";
      document.head.appendChild(css);
    }

    const loadEngine = () => {
      if (document.querySelector("script[data-orx-config-engine]")) return;
      const engine = document.createElement("script");
      engine.src = new URL("config-engine.js", jsBase).href;
      engine.defer = true;
      engine.dataset.orxConfigEngine = "true";
      document.body.appendChild(engine);
    };

    if (window.ORIGEX_CONFIG) {
      loadEngine();
      return;
    }

    if (document.querySelector("script[data-orx-config]")) return;
    const config = document.createElement("script");
    config.src = new URL("config.js", jsBase).href;
    config.dataset.orxConfig = "true";
    config.addEventListener("load", loadEngine, { once: true });
    document.body.appendChild(config);
  };

  bootConfig();

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
