/* ORIGEX — ORX-P01 | M1 UI Runtime | Copyright © ORVEAX */
(() => {
  'use strict';

  const qsa = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // N01/N02/N03 global navigation structure is canonical static HTML.
  // JS owns behavior only; it must not inject, remove, reorder or relabel business navigation routes.
  // Authority: docs/GLOBAL-NAVIGATION-CONTRACT-V1.md

  // Mobile drawer — N03
  const drawer = document.querySelector('[data-orx-mobile-drawer]');
  const openers = qsa('[data-orx-drawer-open]');
  const closers = qsa('[data-orx-drawer-close]');
  const focusableSelector = [
    'a[href]',
    'button:not([disabled])',
    'input:not([disabled])',
    'select:not([disabled])',
    'textarea:not([disabled])',
    '[tabindex]:not([tabindex="-1"])'
  ].join(',');
  let lastFocused = null;

  const drawerFocusables = () => drawer
    ? qsa(focusableSelector, drawer).filter((element) => !element.hidden && element.getAttribute('aria-hidden') !== 'true')
    : [];

  const setDrawer = (open) => {
    if (!drawer) return;
    if (open) lastFocused = document.activeElement;
    drawer.setAttribute('aria-hidden', String(!open));
    document.body.classList.toggle('orx-nav-open', open);
    openers.forEach((button) => button.setAttribute('aria-expanded', String(open)));
    if (open) {
      drawerFocusables()[0]?.focus();
    } else if (lastFocused instanceof HTMLElement) {
      lastFocused.focus();
      lastFocused = null;
    }
  };

  const trapDrawerFocus = (event) => {
    if (!drawer || drawer.getAttribute('aria-hidden') !== 'false' || event.key !== 'Tab') return;
    const focusables = drawerFocusables();
    if (!focusables.length) {
      event.preventDefault();
      return;
    }

    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    const active = document.activeElement;

    if (!drawer.contains(active)) {
      event.preventDefault();
      (event.shiftKey ? last : first).focus();
      return;
    }
    if (event.shiftKey && active === first) {
      event.preventDefault();
      last.focus();
      return;
    }
    if (!event.shiftKey && active === last) {
      event.preventDefault();
      first.focus();
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

  // Keyboard contract for transient navigation.
  document.addEventListener('keydown', (event) => {
    trapDrawerFocus(event);
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
