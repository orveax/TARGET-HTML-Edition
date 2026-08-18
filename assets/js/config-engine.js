/*
 * ORIGEX — ORX-P01
 * Simple Customization Engine v1.0.0
 * Designed & developed by ORVEAX
 * Copyright © ORVEAX
 */

(() => {
  const cfg = window.ORIGEX_CONFIG;
  if (!cfg) return;

  const root = document.documentElement;
  const isArabic = (root.lang || "").toLowerCase().startsWith("ar");

  const get = (path) => path.split(".").reduce((value, key) => value?.[key], cfg);
  const isHex = (value) => typeof value === "string" && /^#[0-9a-fA-F]{6}$/.test(value);
  const safeUrl = (value) => {
    if (typeof value !== "string" || !value.trim()) return "";
    if (value === "#") return "#";
    try {
      const url = new URL(value, window.location.href);
      if (["http:", "https:", "mailto:", "tel:"].includes(url.protocol)) return value;
    } catch (_) {}
    return "";
  };

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

  const header = document.querySelector(".orx-site-header");
  if (header && cfg.ui?.stickyHeader === false) header.classList.add("orx-header--static");
  if (cfg.ui?.megaMenu === false) document.querySelectorAll(".orx-mega").forEach((element) => element.hidden = true);

  const directEmails = document.querySelectorAll(".orx-mega-direct a[href^='mailto:']");
  if (directEmails[0] && cfg.site?.email) {
    directEmails[0].textContent = cfg.site.email;
    directEmails[0].href = `mailto:${cfg.site.email}`;
  }
  if (directEmails[1] && cfg.site?.partnersEmail) {
    directEmails[1].textContent = cfg.site.partnersEmail;
    directEmails[1].href = `mailto:${cfg.site.partnersEmail}`;
  }

  const shouldShowAnnouncement = cfg.features?.showAnnouncementBar !== false && cfg.ui?.announcementBar?.enabled !== false;
  if (shouldShowAnnouncement && header) {
    const bar = document.createElement("div");
    bar.className = "orx-announcement";
    bar.setAttribute("role", "region");
    bar.setAttribute("aria-label", isArabic ? "إعلان الموقع" : "Site announcement");

    const text = isArabic ? cfg.ui.announcementBar.textAr : cfg.ui.announcementBar.textEn;
    const label = isArabic ? cfg.ui.announcementBar.linkLabelAr : cfg.ui.announcementBar.linkLabelEn;
    const href = safeUrl(cfg.ui.announcementBar.link);

    const inner = document.createElement("div");
    inner.className = "container orx-announcement__inner";
    const message = document.createElement("span");
    message.textContent = text || "";
    inner.appendChild(message);

    if (href && label) {
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      inner.appendChild(link);
    }

    bar.appendChild(inner);
    header.parentNode.insertBefore(bar, header);
  }

  document.querySelectorAll("[data-orx-business-hours]").forEach((target) => {
    if (cfg.features?.showBusinessHours === false || cfg.businessHours?.enabled === false) {
      target.hidden = true;
      return;
    }
    const rows = isArabic ? cfg.businessHours?.ar : cfg.businessHours?.en;
    if (!Array.isArray(rows)) return;
    target.replaceChildren(...rows.map((row) => {
      const item = document.createElement("div");
      item.className = "orx-config-hours__row";
      const days = document.createElement("span");
      const hours = document.createElement("strong");
      days.textContent = row.days || "";
      hours.textContent = row.hours || "";
      item.append(days, hours);
      return item;
    }));
  });

  document.querySelectorAll("[data-orx-social-links]").forEach((target) => {
    if (cfg.features?.showSocialLinks === false || cfg.social?.enabled === false) {
      target.hidden = true;
      return;
    }
    const labels = { linkedin: "LinkedIn", instagram: "Instagram", facebook: "Facebook", x: "X", youtube: "YouTube", tiktok: "TikTok" };
    const fragment = document.createDocumentFragment();
    Object.entries(labels).forEach(([key, label]) => {
      const href = safeUrl(cfg.social?.[key]);
      if (!href || href === "#") return;
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      fragment.appendChild(link);
    });
    target.replaceChildren(fragment);
  });

  const showWhatsapp = cfg.features?.showFloatingWhatsApp !== false && cfg.ui?.floatingWhatsApp !== false;
  if (showWhatsapp && cfg.site?.whatsapp) {
    const number = String(cfg.site.whatsapp).replace(/\D/g, "");
    if (number) {
      const link = document.createElement("a");
      link.className = "orx-floating-action orx-floating-action--whatsapp";
      link.href = `https://wa.me/${number}`;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.setAttribute("aria-label", isArabic ? "تواصل عبر واتساب" : "Contact via WhatsApp");
      link.textContent = "WA";
      document.body.appendChild(link);
    }
  }

  const showBackToTop = cfg.features?.showBackToTop !== false && cfg.ui?.backToTop !== false;
  if (showBackToTop) {
    const button = document.createElement("button");
    button.className = "orx-floating-action orx-floating-action--top";
    button.type = "button";
    button.setAttribute("aria-label", isArabic ? "العودة إلى أعلى الصفحة" : "Back to top");
    button.textContent = "↑";
    button.hidden = true;
    button.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
    const sync = () => button.hidden = window.scrollY < 500;
    window.addEventListener("scroll", sync, { passive: true });
    sync();
    document.body.appendChild(button);
  }
})();
