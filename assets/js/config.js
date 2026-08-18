/*
 * ORIGEX — ORX-P01
 * Simple Customization Config v1.0.0
 * Designed & developed by ORVEAX
 * Copyright © ORVEAX
 *
 * Edit this file to change the most common global settings without touching
 * the HTML templates. Keep values inside quotes unless the value is true/false.
 */

window.ORIGEX_CONFIG = {
  site: {
    name: "ORIGEX",
    nameAr: "أوريجكس",
    email: "sales@example.com",
    partnersEmail: "partners@example.com",
    phone: "+000 0000 0000",
    whatsapp: "+00000000000",
    addressAr: "المدينة، الدولة",
    addressEn: "City, Country"
  },

  theme: {
    primary: "#15343B",
    primaryStrong: "#0D252B",
    secondary: "#3F6F68",
    accent: "#C47A4A",
    background: "#FAF8F4",
    surface: "#FFFFFF",
    surfaceSoft: "#F3EFE8",
    text: "#20282C",
    textMuted: "#667278"
  },

  ui: {
    stickyHeader: true,
    megaMenu: true,
    announcementBar: {
      enabled: true,
      textAr: "حلول تجارة وتوزيع أغذية للشركات — من المصدر إلى السوق.",
      textEn: "B2B food trading and distribution — from source to market.",
      link: "contact.html",
      linkLabelAr: "تواصل معنا",
      linkLabelEn: "Contact us"
    },
    floatingWhatsApp: true,
    backToTop: true
  },

  social: {
    enabled: true,
    linkedin: "#",
    instagram: "#",
    facebook: "#",
    x: "#",
    youtube: "#",
    tiktok: "#"
  },

  businessHours: {
    enabled: true,
    timezone: "Local Time",
    ar: [
      { days: "الأحد — الخميس", hours: "09:00 — 18:00" },
      { days: "الجمعة — السبت", hours: "مغلق" }
    ],
    en: [
      { days: "Sunday — Thursday", hours: "09:00 — 18:00" },
      { days: "Friday — Saturday", hours: "Closed" }
    ]
  },

  features: {
    showSocialLinks: true,
    showBusinessHours: true,
    showAnnouncementBar: true,
    showFloatingWhatsApp: true,
    showBackToTop: true
  }
};
