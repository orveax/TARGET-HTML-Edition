/*
 * ORIGEX — ORX-P01
 * Simple Customization Config — Schema V1
 * M1 implementation seed; not a released product version.
 * Designed & developed by ORVEAX
 * Copyright © ORVEAX
 *
 * EDIT THIS FILE for approved common website changes.
 * Do not use this file as a CMS or page builder.
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

    headerCta: {
      enabled: true,
      labelAr: "اطلب عرض سعر",
      labelEn: "Request a Quote",
      link: "rfq.html"
    },

    announcementBar: {
      enabled: true,
      dismissible: true,
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
    showHeaderCta: true,
    showFloatingWhatsApp: true,
    showBackToTop: true
  }
};
