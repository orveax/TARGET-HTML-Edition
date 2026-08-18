# ORIGEX — Simple Customization Guide

Product: ORX-P01  
Owner / Author: ORVEAX  
Status: V1 FOUNDATION

ORIGEX supports two customization paths:

1. **Direct HTML/CSS editing** for developers and advanced buyers.
2. **Simple Config editing** for buyers who want to change common global settings from one file.

The simple path is powered by:

- `assets/js/config.js` — buyer-editable settings.
- `assets/js/config-engine.js` — applies the settings; normally do not edit.
- `assets/css/config-ui.css` — styles config-driven UI such as the announcement bar and floating actions.

## 1. Start here

Open:

`assets/js/config.js`

Only change values on the right side of each setting. Keep text values inside quotes and Boolean values as `true` or `false`.

## 2. Theme colors

The `theme` section controls the principal global color tokens:

- `primary`
- `primaryStrong`
- `secondary`
- `accent`
- `background`
- `surface`
- `surfaceSoft`
- `text`
- `textMuted`

Use six-digit HEX values such as `#15343B`.

Example:

```js
theme: {
  primary: "#15343B",
  accent: "#C47A4A"
}
```

The config engine validates color values before applying them.

## 3. Company information

The `site` section centralizes common information:

- English company name.
- Arabic company name.
- Main email.
- Partner/supplier email.
- Phone.
- WhatsApp number.
- Arabic address.
- English address.

Pages may expose these values using config hooks so the buyer does not need to search across multiple HTML files.

## 4. Header controls

The `ui` section can control:

- Sticky header on/off.
- Mega menu on/off.
- Header CTA on/off.
- Header CTA Arabic label.
- Header CTA English label.
- Header CTA destination.

Example:

```js
headerCta: {
  enabled: true,
  labelAr: "اطلب عرض سعر",
  labelEn: "Request a Quote",
  link: "rfq.html"
}
```

## 5. Announcement / Top Bar

The announcement bar can be enabled or disabled without deleting HTML.

Controls include:

- `enabled`
- `dismissible`
- Arabic text.
- English text.
- Optional link.
- Arabic/English link labels.

Set `enabled: false` or `features.showAnnouncementBar: false` to disable it.

## 6. Social media links

Edit links under `social`:

- LinkedIn.
- Instagram.
- Facebook.
- X.
- YouTube.
- TikTok.

Use `#` for an unused network. Config-rendered social areas automatically skip placeholder links.

## 7. Business hours

Business hours are maintained separately for Arabic and English so direction and wording remain correct.

Example:

```js
ar: [
  { days: "الأحد — الخميس", hours: "09:00 — 18:00" },
  { days: "الجمعة — السبت", hours: "مغلق" }
]
```

Equivalent English rows are defined under `en`.

## 8. Floating WhatsApp

Set the number under:

`site.whatsapp`

Then enable or disable using:

- `ui.floatingWhatsApp`
- `features.showFloatingWhatsApp`

The engine generates the `wa.me` URL automatically after removing spaces and punctuation from the number.

## 9. Back to top

Enable/disable with:

`features.showBackToTop`

The button appears only after the visitor scrolls down the page.

## 10. Config hooks for template developers

Reusable HTML can read config values through these attributes:

```html
<span data-config-text="site.phone"></span>
<a data-config-href="ui.headerCta.link">...</a>
<div data-config-visible="features.showBusinessHours">...</div>
```

Special render targets:

```html
<div class="orx-config-hours" data-orx-business-hours></div>
<nav class="orx-config-social" data-orx-social-links></nav>
```

All new global/contact/footer components should use these hooks where practical.

## 11. What config.js should NOT control

To keep ORIGEX simple, fast and maintainable, `config.js` is not a page builder or CMS.

Do not place these responsibilities in the global config:

- Long page content.
- Complete About/Services copy.
- Product catalog records.
- Supplier/brand records.
- Blog articles.
- Page layout construction.
- Complex animation timelines.

Structured product/supplier/market content should use dedicated data files where appropriate, while page-specific copy remains editable HTML.

## 12. Progressive enhancement rule

ORIGEX pages must remain readable and structurally usable without the config engine. Config enhances common customization but must not be the only source of essential page content.

## 13. Arabic-first rule

The config layer must preserve the product language contract:

- Arabic is primary/default.
- English is secondary/full.
- Arabic and English labels are stored separately when language-specific wording is required.
- The config layer must never force one language string into both directions.

## 14. Recommended buyer workflow

1. Duplicate the original package before editing.
2. Update `config.js` first.
3. Replace logo and image assets.
4. Edit page-specific HTML copy.
5. Replace product/supplier demo data.
6. Test Arabic RTL.
7. Test English LTR.
8. Test responsive layouts.
9. Deploy.

Copyright © ORVEAX.
