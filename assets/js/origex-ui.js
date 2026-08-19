/* ORIGEX — ORX-P01 | M1 UI Runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const qsa = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Controlled global-navigation layer: expose the approved M2 Home Family
  // consistently from N02/N03 without duplicating page-local navigation markup.
  const hydrateHomeFamilyNavigation = () => {
    const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    const homeFiles = new Set(['index.html', 'home-02.html', 'home-03.html', 'landing.html']);
    const labels = isArabic
      ? {
          title: 'نماذج الرئيسية',
          items: [
            ['index.html', 'الرئيسية 01 — التجارة والاستيراد'],
            ['home-02.html', 'الرئيسية 02 — الجملة والتوزيع'],
            ['home-03.html', 'الرئيسية 03 — المصنع والمورد'],
            ['landing.html', 'Landing — صفحة مركزة']
          ]
        }
      : {
          title: 'Home Variants',
          items: [
            ['index.html', 'Home 01 — Trading & Import'],
            ['home-02.html', 'Home 02 — Wholesale & Distribution'],
            ['home-03.html', 'Home 03 — Manufacturer & Supplier'],
            ['landing.html', 'Landing — One Page']
          ]
        };

    qsa('[data-orx-mega-menu]').forEach((menu) => {
      const grid = menu.querySelector('.orx-mega-menu__grid');
      if (!grid || grid.querySelector('[data-orx-home-variants]')) return;

      const group = document.createElement('div');
      group.className = 'orx-mega-menu__group';
      group.dataset.orxHomeVariants = '';
      group.style.gridColumn = '1 / -1';
      group.style.gridTemplateColumns = 'repeat(4, minmax(0, 1fr))';

      const title = document.createElement('strong');
      title.textContent = labels.title;
      title.style.gridColumn = '1 / -1';
      group.append(title);

      labels.items.forEach(([href, text]) => {
        const link = document.createElement('a');
        link.href = href;
        link.textContent = text;
        link.dataset.orxHomeVariantLink = href;
        if (href === currentFile) link.setAttribute('aria-current', 'page');
        group.append(link);
      });

      grid.prepend(group);
    });

    qsa('.orx-mobile-nav').forEach((nav) => {
      qsa('a', nav).forEach((link) => {
        const href = (link.getAttribute('href') || '').split('#')[0];
        if (homeFiles.has(href)) link.remove();
      });

      const fragment = document.createDocumentFragment();
      labels.items.forEach(([href, text]) => {
        const link = document.createElement('a');
        link.href = href;
        link.textContent = text;
        link.dataset.orxHomeVariantLink = href;
        if (href === currentFile) link.setAttribute('aria-current', 'page');
        fragment.append(link);
      });
      nav.prepend(fragment);
    });
  };

  // M3 company/business IA: keep About, How We Work and Capabilities discoverable
  // from all shared navigation surfaces. Future approved routes may appear before build.
  const hydrateCompanyNavigation = () => {
    const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    const activeCompanyFile = currentFile === 'service-details.html' ? 'capabilities.html' : currentFile;
    const companyFiles = new Set(['about.html', 'how-we-work.html', 'capabilities.html']);
    const labels = isArabic
      ? {
          title: 'الشركة وطريقة العمل',
          items: [
            ['about.html', 'عن الشركة'],
            ['how-we-work.html', 'كيف نعمل'],
            ['capabilities.html', 'القدرات والخدمات']
          ]
        }
      : {
          title: 'Company & Process',
          items: [
            ['about.html', 'About'],
            ['how-we-work.html', 'How We Work'],
            ['capabilities.html', 'Capabilities & Services']
          ]
        };

    qsa('[data-orx-mega-menu]').forEach((menu) => {
      const grid = menu.querySelector('.orx-mega-menu__grid');
      if (!grid || grid.querySelector('[data-orx-company-links]')) return;

      const group = document.createElement('div');
      group.className = 'orx-mega-menu__group';
      group.dataset.orxCompanyLinks = '';

      const title = document.createElement('span');
      title.className = 'orx-mega-menu__title';
      title.textContent = labels.title;
      group.append(title);

      labels.items.forEach(([href, text]) => {
        const link = document.createElement('a');
        link.href = href;
        link.textContent = text;
        link.dataset.orxCompanyLink = href;
        if (href === activeCompanyFile) link.setAttribute('aria-current', 'page');
        group.append(link);
      });

      grid.append(group);
    });

    qsa('.orx-mobile-nav').forEach((nav) => {
      qsa('a', nav).forEach((link) => {
        const href = (link.getAttribute('href') || '').split('#')[0];
        if (companyFiles.has(href)) link.remove();
      });

      const fragment = document.createDocumentFragment();
      labels.items.forEach(([href, text]) => {
        const link = document.createElement('a');
        link.href = href;
        link.textContent = text;
        link.dataset.orxCompanyLink = href;
        if (href === activeCompanyFile) link.setAttribute('aria-current', 'page');
        fragment.append(link);
      });

      const lastHome = nav.querySelector('[data-orx-home-variant-link]:last-of-type');
      if (lastHome) lastHome.after(fragment);
      else nav.prepend(fragment);
    });
  };

  // M3 market IA: expose Market Access and Markets in desktop/mobile navigation.
  const hydrateMarketNavigation = () => {
    const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    const marketFiles = new Set(['market-access.html', 'markets.html']);
    const labels = isArabic
      ? {
          items: [
            ['market-access.html', 'الوصول إلى السوق'],
            ['markets.html', 'الأسواق والدول']
          ]
        }
      : {
          items: [
            ['market-access.html', 'Market Access'],
            ['markets.html', 'Markets & Countries']
          ]
        };

    qsa('[data-orx-mega-menu]').forEach((menu) => {
      labels.items.forEach(([href, text]) => {
        const link = menu.querySelector(`a[href="${href}"]`);
        if (!link) return;
        link.textContent = text;
        link.dataset.orxMarketLink = href;
        link.removeAttribute('aria-current');
        if (href === currentFile) link.setAttribute('aria-current', 'page');
      });
    });

    qsa('.orx-mobile-nav').forEach((nav) => {
      qsa('a', nav).forEach((link) => {
        const href = (link.getAttribute('href') || '').split('#')[0];
        if (marketFiles.has(href)) link.remove();
      });

      const fragment = document.createDocumentFragment();
      labels.items.forEach(([href, text]) => {
        const link = document.createElement('a');
        link.href = href;
        link.textContent = text;
        link.dataset.orxMarketLink = href;
        if (href === currentFile) link.setAttribute('aria-current', 'page');
        fragment.append(link);
      });

      const lastCompany = nav.querySelector('[data-orx-company-link]:last-of-type');
      const lastHome = nav.querySelector('[data-orx-home-variant-link]:last-of-type');
      if (lastCompany) lastCompany.after(fragment);
      else if (lastHome) lastHome.after(fragment);
      else nav.prepend(fragment);
    });
  };

  // M4 product IA: expose Product Categories and Products centrally.
  // Product Details is treated as a child of Products for current-state semantics.
  const hydrateProductNavigation = () => {
    const isArabic = document.documentElement.lang.toLowerCase().startsWith('ar');
    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    const activeProductFile = currentFile === 'product-details.html' ? 'products.html' : currentFile;
    const productFiles = new Set(['product-categories.html', 'products.html']);
    const labels = isArabic
      ? {
          items: [
            ['product-categories.html', 'فئات المنتجات'],
            ['products.html', 'كل المنتجات']
          ]
        }
      : {
          items: [
            ['product-categories.html', 'Product Categories'],
            ['products.html', 'All Products']
          ]
        };

    qsa('[data-orx-mega-menu]').forEach((menu) => {
      labels.items.forEach(([href, text]) => {
        const link = menu.querySelector(`a[href="${href}"]`);
        if (!link) return;
        link.textContent = text;
        link.dataset.orxProductLink = href;
        link.removeAttribute('aria-current');
        if (href === activeProductFile) link.setAttribute('aria-current', 'page');
      });
    });

    qsa('.orx-mobile-nav').forEach((nav) => {
      qsa('a', nav).forEach((link) => {
        const href = (link.getAttribute('href') || '').split('#')[0];
        if (productFiles.has(href)) link.remove();
      });

      const fragment = document.createDocumentFragment();
      labels.items.forEach(([href, text]) => {
        const link = document.createElement('a');
        link.href = href;
        link.textContent = text;
        link.dataset.orxProductLink = href;
        if (href === activeProductFile) link.setAttribute('aria-current', 'page');
        fragment.append(link);
      });

      const lastHome = nav.querySelector('[data-orx-home-variant-link]:last-of-type');
      if (lastHome) lastHome.after(fragment);
      else nav.prepend(fragment);
    });
  };

  hydrateHomeFamilyNavigation();
  hydrateProductNavigation();
  // Keep this separator so the retired one-time PG14 workflow cannot reapply the patch.
  hydrateCompanyNavigation();
  hydrateMarketNavigation();

  // Mobile drawer — N03
  const drawer = document.querySelector('[data-orx-mobile-drawer]');
  const openers = qsa('[data-orx-drawer-open]');
  const closers = qsa('[data-orx-drawer-close]');
  let lastFocused = null;

  const setDrawer = (open) => {
    if (!drawer) return;
    if (open) lastFocused = document.activeElement;
    drawer.setAttribute('aria-hidden', String(!open));
    document.body.classList.toggle('orx-nav-open', open);
    openers.forEach((button) => button.setAttribute('aria-expanded', String(open)));
    if (open) {
      const focusTarget = drawer.querySelector('button, a, input, select, textarea, [tabindex]:not([tabindex="-1"])');
      focusTarget?.focus();
    } else if (lastFocused instanceof HTMLElement) {
      lastFocused.focus();
    }
  };

  openers.forEach((button) => button.addEventListener('click', () => setDrawer(true)));
  closers.forEach((button) => button.addEventListener('click', () => setDrawer(false)));
  drawer?.querySelector('[data-orx-drawer-backdrop]')?.addEventListener('click', () => setDrawer(false));

  // Mega menu — N02
  qsa('[data-orx-mega-trigger]').forEach((trigger) => {
    const id = trigger.getAttribute('aria-controls');
    const menu = id ? document.getElementById(id) : null;
    if (!menu) return;

    const setOpen = (open) => {
      trigger.setAttribute('aria-expanded', String(open));
      menu.hidden = !open;
    };

    trigger.addEventListener('click', (event) => {
      event.preventDefault();
      setOpen(trigger.getAttribute('aria-expanded') !== 'true');
    });

    document.addEventListener('click', (event) => {
      if (!menu.hidden && !menu.contains(event.target) && !trigger.contains(event.target)) setOpen(false);
    });
  });

  // Tabs — C13
  qsa('[data-orx-tabs]').forEach((tabs) => {
    const list = tabs.querySelector('[role="tablist"]');
    const tabButtons = qsa('[role="tab"]', tabs);
    const panels = qsa('[role="tabpanel"]', tabs);
    if (!list || !tabButtons.length) return;

    const activate = (tab, moveFocus = true) => {
      tabButtons.forEach((button) => {
        const selected = button === tab;
        button.setAttribute('aria-selected', String(selected));
        button.tabIndex = selected ? 0 : -1;
      });
      panels.forEach((panel) => panel.hidden = panel.id !== tab.getAttribute('aria-controls'));
      if (moveFocus) tab.focus();
    };

    tabButtons.forEach((tab) => tab.addEventListener('click', () => activate(tab, false)));
    list.addEventListener('keydown', (event) => {
      const current = tabButtons.indexOf(document.activeElement);
      if (current < 0) return;
      const dir = document.documentElement.dir === 'rtl' ? -1 : 1;
      let next = null;
      if (event.key === 'ArrowRight') next = (current + dir + tabButtons.length) % tabButtons.length;
      if (event.key === 'ArrowLeft') next = (current - dir + tabButtons.length) % tabButtons.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabButtons.length - 1;
      if (next !== null) {
        event.preventDefault();
        activate(tabButtons[next]);
      }
    });
  });

  // Accordion — C14
  qsa('[data-orx-accordion-trigger]').forEach((button) => {
    const id = button.getAttribute('aria-controls');
    const panel = id ? document.getElementById(id) : null;
    if (!panel) return;
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!open));
      panel.hidden = open;
    });
  });

  // Filter chips — C17 foundation behavior
  qsa('[data-orx-filter-group]').forEach((group) => {
    qsa('[data-orx-filter]', group).forEach((filter) => {
      filter.addEventListener('click', () => {
        const multi = group.dataset.orxFilterMode === 'multi';
        if (!multi) qsa('[data-orx-filter]', group).forEach((item) => item.setAttribute('aria-pressed', 'false'));
        const next = multi ? filter.getAttribute('aria-pressed') !== 'true' : true;
        filter.setAttribute('aria-pressed', String(next));
        group.dispatchEvent(new CustomEvent('orx:filter-change', { bubbles: true }));
      });
    });
  });

  // File input — C24
  qsa('[data-orx-file-input]').forEach((input) => {
    input.addEventListener('change', () => {
      const label = input.closest('[data-orx-upload]')?.querySelector('[data-orx-file-name]');
      if (label) label.textContent = input.files?.[0]?.name || label.dataset.emptyLabel || 'No file selected';
    });
  });

  // Escape closes transient navigation.
  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    if (drawer?.getAttribute('aria-hidden') === 'false') setDrawer(false);
    qsa('[data-orx-mega-trigger][aria-expanded="true"]').forEach((trigger) => {
      trigger.setAttribute('aria-expanded', 'false');
      const menu = document.getElementById(trigger.getAttribute('aria-controls'));
      if (menu) menu.hidden = true;
      trigger.focus();
    });
  });

  // Back-to-top fallback when config engine is not present.
  qsa('[data-orx-back-to-top]:not([data-config-managed])').forEach((button) => {
    const sync = () => button.hidden = window.scrollY < 500;
    button.addEventListener('click', () => window.scrollTo({ top: 0, behavior: reducedMotion() ? 'auto' : 'smooth' }));
    window.addEventListener('scroll', sync, { passive: true });
    sync();
  });
})();
