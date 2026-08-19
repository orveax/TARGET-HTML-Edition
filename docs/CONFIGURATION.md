# ORIGEX — Configuration Contract V1

Product ID: ORX-P01  
Owner / Author: ORVEAX  
Status: APPROVED CONFIG CONTRACT — M1 SEED

ORIGEX provides a small global customization layer for common repeated settings. It is intentionally not a CMS, page builder or replacement for page content/data architecture.

## 1. Active Files

```text
assets/js/config.js
assets/js/config-engine.js
```

- `config.js` — buyer-editable global/repeated settings.
- `config-engine.js` — applies approved settings to existing semantic HTML; normally not buyer-edited.

There is no dedicated `config-ui.css`. Config-driven UI is styled by the registered ORIGEX component/global CSS implemented during M1.

## 2. Core Principle

The engine **enhances existing HTML**. It does not construct the site's core components, navigation, announcement bar, floating actions or page meaning from JavaScript.

Every important piece of UI must exist as valid semantic HTML first, with config hooks attached where useful.

## 3. Buyer-Editable Domains

### `site`
- `name`
- `nameAr`
- `email`
- `partnersEmail`
- `phone`
- `whatsapp`
- `addressAr`
- `addressEn`

### `theme`
- `primary`
- `primaryStrong`
- `secondary`
- `accent`
- `background`
- `surface`
- `surfaceSoft`
- `text`
- `textMuted`

Colors use six-digit HEX values. The engine validates them before applying CSS variables.

### `ui`
- sticky header
- mega-menu availability
- header CTA
- announcement bar
- floating WhatsApp
- back to top

### `social`
- LinkedIn
- Instagram
- Facebook
- X
- YouTube
- TikTok

Use `#` for an unused social link. Registered social markup hides unusable placeholders.

### `businessHours`
Arabic and English rows are maintained separately so language/direction remain correct.

### `features`
Approved simple visibility flags for repeated/global UI only.

## 4. Generic Config Hooks

### Text
```html
<span data-config-text="site.phone">+000 0000 0000</span>
```

### Href
```html
<a data-config-href="ui.headerCta.link" href="rfq.html">...</a>
```

### Visibility
```html
<div data-config-visible="features.showBusinessHours">...</div>
```

The HTML fallback remains valid if JavaScript is unavailable.

## 5. Registered Semantic Hooks

These hooks are the V1 contract used by shared components.

### Site identity
```html
<span data-orx-site-name>ORIGEX</span>
```

### Header
```html
<header data-orx-site-header>...</header>
<div data-orx-mega-menu>...</div>
<a data-orx-header-cta href="rfq.html">Request a Quote</a>
```

### Announcement
```html
<div data-orx-announcement>
  <span data-orx-announcement-text>...</span>
  <a data-orx-announcement-link href="contact.html">...</a>
  <button data-orx-announcement-close type="button" aria-label="Close announcement">...</button>
</div>
```

The close control uses the registered Lucide/Icon Button component during M1; the config engine does not create an icon itself.

### Email
```html
<a data-orx-email="sales" href="mailto:sales@example.com">sales@example.com</a>
<a data-orx-email="partners" href="mailto:partners@example.com">partners@example.com</a>
```

### Phone
```html
<a data-orx-phone href="tel:+0000000000">+000 0000 0000</a>
```

### Address
```html
<span data-orx-address>City, Country</span>
```

### Business hours
```html
<div data-orx-business-hours>
  <!-- valid fallback rows may exist here -->
</div>
```

### Social links
Each link owns its network key:
```html
<a data-orx-social-link="linkedin" href="#">LinkedIn</a>
<a data-orx-social-link="instagram" href="#">Instagram</a>
```

Brand/social marks use separately approved official/licensed assets; they are not Lucide semantic icons.

### Floating WhatsApp
```html
<a data-orx-floating-whatsapp href="#" aria-label="Contact via WhatsApp">...</a>
```

The component exists in HTML; config only controls its URL/visibility.

### Back to top
```html
<button data-orx-back-to-top type="button" aria-label="Back to top">...</button>
```

The engine uses smooth scrolling unless `prefers-reduced-motion: reduce` is active.

## 6. What `config.js` Must Not Control

Do not put these into global config:
- long page copy;
- complete About/Services sections;
- page layout construction;
- product catalog records;
- supplier/brand records;
- market records;
- blog/article bodies;
- complex per-page state;
- animation timelines.

Page editorial copy stays in HTML. Approved structured repeated business data follows `DATA-SCHEMA-V1.md`.

## 7. Content / SEO Boundary

`config.js` may supply repeated company identity/contact values, but it does not replace:
- Page Content Contracts;
- H1/page copy;
- registered SEO title/meta/canonical/hreflang contracts;
- demo-data governance.

Those remain controlled by the Content/SEO authorities.

## 8. Progressive Enhancement

A page must remain readable, navigable and commercially understandable without the config engine.

Config may replace repeated values and enable/disable approved global utilities; it may not be the only source of essential meaning.

## 9. Arabic / English Rule

- Arabic is the master commercial language.
- English is complete and professionally adapted.
- Language-specific labels are stored separately when needed.
- The config layer never forces one language string into both directions.
- phone/email/SKU-like values remain bidi-safe in markup/CSS.

## 10. M1 Implementation Rule

Before M1 closes:
1. all global components that use config expose only the documented hooks;
2. old class-coupled config selectors are prohibited;
3. Lucide icons live in the Icon System, never generated as text glyphs by config JS;
4. config engine has no page-specific dependency;
5. AR/EN fallback HTML is tested with config JS disabled;
6. buyer documentation reflects the exact shipped hooks.

## 11. Change Control

Adding a genuinely repeated global setting is allowed only after checking that it reduces buyer editing effort without turning config into a content management layer.

A page-specific value does not become global merely because it is convenient to access from JavaScript.

Copyright © ORVEAX.
