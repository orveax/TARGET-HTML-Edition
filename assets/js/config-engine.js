/*
 * ORIGEX — ORX-P01
 * Simple Customization Engine — V1
 * M1 implementation seed; not a released product version.
 * Designed & developed by ORVEAX
 * Copyright © ORVEAX
 *
 * Principle: enhance existing semantic HTML; do not construct core UI/components here.
 */

(() => {
  const cfg = window.ORIGEX_CONFIG;
  if (!cfg) return;

  const root = document.documentElement;
  const isArabic = (root.lang || "").toLowerCase().startsWith("ar");

  const get = (path) => path.split(".").reduce((value, key) => value?.[key], cfg);

  const safeUrl = (value) => {
    if (typeof value !== "string" || !value.trim()) return "";
    if (value === "#") return "#";
    try {
      const url = new URL(value, window.location.href);
      return ["http:", "https:", "mailto:", "tel:"].includes(url.protocol) ? value : "";
    } catch (_) {
      return "";
    }
  };

  const isHex = (value) => typeof value === "string" && /^#[0-9a-fA-F]{6}$/.test(value);

  const themeMap = {
    primary: "--orx-primary",
    primaryStrong: "--orx-primary-strong",
    secondary: "--orx-secondary",
    accent: "--orx-accent",
    background: "--orx-bg",
    surface: "--orx-surface",
    surfaceSoft: "--orx-surface-soft",
    text: "--orx-text",
    textMuted: "--orx-text-muted"
  };

  Object.entries(themeMap).forEach(([key, variable]) => {
    const value = cfg.theme?.[key];
    if (isHex(value)) root.style.setProperty(variable, value);
  });

  document.querySelectorAll("[data-config-text]").forEach((element) => {
    const value = get(element.dataset.configText);
    if (value !== undefined && value !== null) element.textContent = String(value);
  });

  document.querySelectorAll("[data-config-href]").forEach((element) => {
    const value = safeUrl(get(element.dataset.configHref));
    if (value) element.setAttribute("href", value);
  });

  document.querySelectorAll("[data-config-visible]").forEach((element) => {
    element.hidden = !Boolean(get(element.dataset.configVisible));
  });

  document.querySelectorAll("[data-orx-site-name]").forEach((element) => {
    element.textContent = isArabic ? (cfg.site?.nameAr || cfg.site?.name || "") : (cfg.site?.name || "");
  });

  const header = document.querySelector("[data-orx-site-header]");
  if (header && cfg.ui?.stickyHeader === false) header.classList.add("orx-site-header--static");

  document.querySelectorAll("[data-orx-mega-menu]").forEach((element) => {
    if (cfg.ui?.megaMenu === false) element.hidden = true;
  });

  document.querySelectorAll("[data-orx-header-cta]").forEach((element) => {
    const enabled = cfg.features?.showHeaderCta !== false && cfg.ui?.headerCta?.enabled !== false;
    element.hidden = !enabled;
    if (!enabled) return;

    const label = isArabic ? cfg.ui?.headerCta?.labelAr : cfg.ui?.headerCta?.labelEn;
    const href = safeUrl(cfg.ui?.headerCta?.link);
    if (label) element.textContent = label;
    if (href) element.setAttribute("href", href);
  });

  document.querySelectorAll("[data-orx-announcement]").forEach((bar) => {
    const enabled = cfg.features?.showAnnouncementBar !== false && cfg.ui?.announcementBar?.enabled !== false;
    bar.hidden = !enabled;
    if (!enabled) return;

    const text = isArabic ? cfg.ui?.announcementBar?.textAr : cfg.ui?.announcementBar?.textEn;
    const linkLabel = isArabic ? cfg.ui?.announcementBar?.linkLabelAr : cfg.ui?.announcementBar?.linkLabelEn;
    const href = safeUrl(cfg.ui?.announcementBar?.link);

    const message = bar.querySelector("[data-orx-announcement-text]");
    const link = bar.querySelector("[data-orx-announcement-link]");
    const close = bar.querySelector("[data-orx-announcement-close]");

    if (message && text) message.textContent = text;
    if (link) {
      if (href && linkLabel) {
        link.hidden = false;
        link.textContent = linkLabel;
        link.setAttribute("href", href);
      } else {
        link.hidden = true;
      }
    }

    if (close) {
      close.hidden = cfg.ui?.announcementBar?.dismissible === false;
      close.addEventListener("click", () => {
        bar.hidden = true;
      });
    }
  });

  document.querySelectorAll("[data-orx-email='sales']").forEach((element) => {
    if (!cfg.site?.email) return;
    element.textContent = cfg.site.email;
    if (element.matches("a")) element.href = `mailto:${cfg.site.email}`;
  });

  document.querySelectorAll("[data-orx-email='partners']").forEach((element) => {
    if (!cfg.site?.partnersEmail) return;
    element.textContent = cfg.site.partnersEmail;
    if (element.matches("a")) element.href = `mailto:${cfg.site.partnersEmail}`;
  });

  document.querySelectorAll("[data-orx-phone]").forEach((element) => {
    if (!cfg.site?.phone) return;
    element.textContent = cfg.site.phone;
    if (element.matches("a")) element.href = `tel:${String(cfg.site.phone).replace(/[^+\d]/g, "")}`;
  });

  document.querySelectorAll("[data-orx-address]").forEach((element) => {
    element.textContent = isArabic ? (cfg.site?.addressAr || "") : (cfg.site?.addressEn || "");
  });

  document.querySelectorAll("[data-orx-business-hours]").forEach((target) => {
    const enabled = cfg.features?.showBusinessHours !== false && cfg.businessHours?.enabled !== false;
    target.hidden = !enabled;
    if (!enabled) return;

    const rows = isArabic ? cfg.businessHours?.ar : cfg.businessHours?.en;
    if (!Array.isArray(rows)) return;

    const fragment = document.createDocumentFragment();
    rows.forEach((row) => {
      const item = document.createElement("div");
      item.className = "orx-business-hours__row";

      const days = document.createElement("span");
      days.textContent = row.days || "";

      const hours = document.createElement("strong");
      hours.textContent = row.hours || "";

      item.append(days, hours);
      fragment.appendChild(item);
    });
    target.replaceChildren(fragment);
  });

  document.querySelectorAll("[data-orx-social-link]").forEach((link) => {
    const key = link.dataset.orxSocialLink;
    const href = safeUrl(cfg.social?.[key]);
    const enabled = cfg.features?.showSocialLinks !== false && cfg.social?.enabled !== false && href && href !== "#";
    link.hidden = !enabled;
    if (enabled) link.setAttribute("href", href);
  });

  document.querySelectorAll("[data-orx-floating-whatsapp]").forEach((link) => {
    const enabled = cfg.features?.showFloatingWhatsApp !== false && cfg.ui?.floatingWhatsApp !== false;
    const number = String(cfg.site?.whatsapp || "").replace(/\D/g, "");
    link.hidden = !(enabled && number);
    if (enabled && number) link.href = `https://wa.me/${number}`;
  });

  document.querySelectorAll("[data-orx-back-to-top]").forEach((button) => {
    const enabled = cfg.features?.showBackToTop !== false && cfg.ui?.backToTop !== false;
    if (!enabled) {
      button.hidden = true;
      return;
    }

    const sync = () => {
      button.hidden = window.scrollY < 500;
    };

    button.addEventListener("click", () => {
      const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
    });

    window.addEventListener("scroll", sync, { passive: true });
    sync();
  });
})();
