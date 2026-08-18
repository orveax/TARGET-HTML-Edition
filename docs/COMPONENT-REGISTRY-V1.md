# ORIGEX — Unified Component Registry V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: LOCKED BASE REGISTRY — V1 MAIN FEATURES

This is the central component authority for ORIGEX. Pages must consume these components and approved variants without page-specific redesign.

---

## F01 — Color System

**Hierarchy:** Foundation  
**Purpose:** control brand, surface, text and semantic color roles.

**Strategy:** colors are role-based, not page-based. Pages cannot introduce decorative colors outside the token system.

**Core roles:** Primary, Primary Strong, Secondary, Accent, Background, Surface, Surface Soft, Text, Text Muted, Border, Success, Warning, Danger, Info.

**Sample:**
```css
:root {
  --orx-primary:#15343B;
  --orx-primary-strong:#0D252B;
  --orx-secondary:#3F6F68;
  --orx-accent:#C47A4A;
  --orx-bg:#FAF8F4;
}
```

**Rule:** page CSS may consume tokens; it may not invent page-only palette values.

---

## F02 — Typography System

**Hierarchy:** Foundation  
**Purpose:** one readable hierarchy in Arabic and English.

**Strategy:** same semantic hierarchy, independently tuned Arabic/English metrics.

**Arabic:** Tajawal.  
**English:** Manrope.

**Roles:** Display, H1, H2, H3, H4, Body Large, Body, Small, Label/Eyebrow, UI/Button.

**Sample:**
```html
<span class="orx-eyebrow">المنتجات</span>
<h2 class="orx-h2">منتجات مختارة للسوق.</h2>
<p class="orx-body">معلومات تجارية واضحة للمشتري والمورد.</p>
```

**Rule:** no arbitrary page font sizes; add a semantic type token if a real repeated need exists.

---

## F03 — Spacing & Layout

**Hierarchy:** Foundation  
**Strategy:** tokenized spacing + standard containers + logical properties.

**Families:** XS, SM, MD, LG, XL section spacing; compact/standard/comfortable component density.

**Sample:**
```css
.orx-section { padding-block: var(--orx-section-space); }
.container { width:min(100% - 2rem,1200px); margin-inline:auto; }
```

**Rule:** spacing differences communicate hierarchy, not decoration.

---

# PRIMITIVES

## P01 — Primary Button

**Hierarchy:** Primitive  
**Purpose:** primary action in a decision area.

**Strategy:** high contrast, solid treatment, one dominant primary per local action group.

**Variants:** Small / Default / Large.  
**States:** default / hover / focus-visible / disabled.

**Sample:**
```html
<a class="orx-btn orx-btn--primary" href="rfq.html">اطلب عرض سعر</a>
```

**RTL:** directional icon mirrors; text remains naturally RTL.  
**Don't:** create different radius/color per page.

---

## P02 — Secondary Button

**Hierarchy:** Primitive  
**Purpose:** secondary but explicit action.

**Strategy:** outline or quiet surface; never compete visually with P01.

**Sample:**
```html
<a class="orx-btn orx-btn--secondary" href="products.html">استعرض المنتجات</a>
```

---

## P03 — Text Action

**Hierarchy:** Primitive  
**Purpose:** tertiary navigation/action.

**Sample:**
```html
<a class="orx-text-action" href="how-we-work.html">تعرف على طريقة العمل <span aria-hidden="true">↖</span></a>
```

**Rule:** arrow is directional and mirrored between RTL/LTR.

---

## P04 — Icon Button

**Hierarchy:** Primitive  
**Purpose:** compact utility controls: close, menu, search, previous/next.

**Strategy:** always has accessible name; minimum touch target.

**Sample:**
```html
<button class="orx-icon-btn" type="button" aria-label="إغلاق القائمة">×</button>
```

---

## P05 — Badge

**Hierarchy:** Primitive  
**Purpose:** short semantic metadata.

**Approved semantic variants:** Category / Origin / Certification / Availability / Featured / Updated.

**Sample:**
```html
<span class="orx-badge orx-badge--origin">Italy</span>
```

**Rule:** never communicate status by color alone.

---

## P06 — Form Input

**Hierarchy:** Primitive  
**Purpose:** standard text/email/tel input.

**Strategy:** visible label, help/error slot, consistent height/radius.

**Sample:**
```html
<label class="orx-field">
  <span class="orx-field__label">البريد الإلكتروني</span>
  <input class="orx-input" type="email" name="email" autocomplete="email">
</label>
```

**RTL:** email/tel values use bidi-safe LTR behavior.

---

## P07 — Select

**Hierarchy:** Primitive  
**Purpose:** finite choice selection.

**Sample:**
```html
<label class="orx-field">
  <span class="orx-field__label">الفئة</span>
  <select class="orx-select" name="category"><option>المشروبات</option></select>
</label>
```

---

## P08 — Textarea

**Hierarchy:** Primitive  
**Purpose:** multi-line enquiry/context.

**Rule:** default minimum height controlled centrally; no page-specific resize styling.

---

## P09 — Checkbox / Radio

**Hierarchy:** Primitive  
**Purpose:** consent and finite selections.

**Rule:** native semantics preserved; large enough mobile target.

---

## P10 — Divider

**Hierarchy:** Primitive  
**Purpose:** separate groups when spacing alone is insufficient.

**Rule:** not decorative clutter.

---

# COMPONENTS — CARD FAMILIES

## C01 — Feature Card

**Hierarchy:** Component  
**Purpose:** capability, benefit or commercial function.

**Anatomy:** icon → optional index → title → supporting copy → optional metadata.

**Strategy:** clear information card; moderate density; no hidden essential content.

**Approved variants:** Standard / Emphasis.  
**States:** default / active where semantically needed.

**Sample:**
```html
<article class="orx-feature-card">
  <div class="orx-card-head"><span class="orx-card-icon">IMP</span><span class="orx-card-index">01</span></div>
  <h3>الاستيراد والتجارة</h3>
  <p>مسار واضح من المنتج إلى السوق.</p>
</article>
```

**Rule:** every Feature Card in ORIGEX uses the same anatomy and base spacing.

---

## C02 — Product Card

**Hierarchy:** Component  
**Purpose:** represent a product in listing/related-product contexts.

**Anatomy:** media → badges → product name → brand/origin → compact specs → action.

**Approved variants:** Standard / Compact / Featured.  
**States:** available / unavailable / featured.

**Sample:**
```html
<article class="orx-product-card">
  <a class="orx-product-card__media" href="product-details.html"><img src="..." alt="Product name"></a>
  <div class="orx-product-card__body">
    <span class="orx-badge orx-badge--origin">Türkiye</span>
    <h3><a href="product-details.html">Premium Product</a></h3>
    <p>Brand Name · 12 × 500 g</p>
    <a class="orx-text-action" href="product-details.html">تفاصيل المنتج</a>
  </div>
</article>
```

**Rule:** a Product Card on Home, Products, Supplier Details and Related Products remains the same component. Page changes grid placement only.

---

## C03 — Supplier / Brand Card

**Hierarchy:** Component  
**Purpose:** represent manufacturer, supplier or brand.

**Anatomy:** controlled logo frame → name → country → categories → action.

**Approved variants:** Standard / Featured.

**Sample:**
```html
<article class="orx-supplier-card">
  <div class="orx-supplier-card__logo"><img src="..." alt="Brand name"></div>
  <h3>Brand Name</h3>
  <p>Spain · Dairy & Ambient Food</p>
  <a class="orx-text-action" href="supplier-details.html">عرض المورد</a>
</article>
```

---

## C04 — Market Card

**Hierarchy:** Component  
**Purpose:** summarize a country/market opportunity.

**Anatomy:** market code/flag placeholder → country → channel tags → short summary → action.

**Sample:**
```html
<article class="orx-market-card">
  <span class="orx-market-card__code">QA</span>
  <h3>Qatar</h3>
  <p>Retail · Wholesale · HoReCa</p>
</article>
```

---

## C05 — Process Card

**Hierarchy:** Component  
**Purpose:** one step inside a process/journey.

**Anatomy:** step number → icon → title → explanation → optional requirement/outcome.

**Sample:**
```html
<article class="orx-process-card">
  <span class="orx-process-card__step">01</span>
  <h3>مراجعة المنتج</h3>
  <p>نراجع الفئة والمواصفات والملاءمة التجارية.</p>
</article>
```

**Rule:** step numbering direction is visually correct in Arabic and English.

---

## C06 — Metric / Stat Card

**Hierarchy:** Component  
**Purpose:** present a quantified fact.

**Anatomy:** value → unit/suffix → label → optional note.

**Rule:** only for meaningful factual/demo values; no decorative fake metrics.

---

## C07 — Certification Card

**Hierarchy:** Component  
**Purpose:** present a certificate/compliance item.

**Anatomy:** certificate mark placeholder → title → issuer/type → status/metadata → optional action.

**Sample:**
```html
<article class="orx-cert-card">
  <span class="orx-cert-card__mark">ISO</span>
  <h3>Quality Management</h3>
  <p>Demo certification placeholder</p>
</article>
```

**Rule:** demo content must never imply a fictional company actually owns a certificate.

---

## C08 — Resource / Download Card

**Hierarchy:** Component  
**Purpose:** downloadable brochure, profile, datasheet, certificate or resource.

**Anatomy:** file type → title → metadata → download/view action.

**Sample:**
```html
<article class="orx-resource-card">
  <span class="orx-resource-card__type">PDF</span>
  <h3>Company Profile</h3>
  <p>English · 4.2 MB</p>
  <a class="orx-text-action" href="#">تحميل</a>
</article>
```

---

## C09 — Case Study Card

**Hierarchy:** Component  
**Purpose:** summarize business proof/story.

**Anatomy:** media → category/market tags → title → result highlight → action.

---

## C10 — Contact / Department Card

**Hierarchy:** Component  
**Purpose:** expose a contact channel or department.

**Anatomy:** icon → department/title → short description → email/phone/action.

---

## C11 — CTA Card

**Hierarchy:** Component  
**Purpose:** contained conversion area inside a page.

**Anatomy:** kicker → title → supporting copy → primary action → optional secondary action.

**Rule:** does not replace the global Final CTA section; used where a contained decision block is needed.

---

# NAVIGATION & DISCLOSURE

## C12 — Breadcrumb

**Hierarchy:** Component  
**Purpose:** page hierarchy and recovery.

**Rule:** semantic nav; direction/order checked independently in RTL and LTR.

**Sample:**
```html
<nav class="orx-breadcrumb" aria-label="مسار الصفحة"><a href="index.html">الرئيسية</a><span>/</span><span aria-current="page">المنتجات</span></nav>
```

---

## C13 — Tabs

**Hierarchy:** Component  
**Purpose:** switch related content views without navigation.

**Strategy:** use only when content categories are peers.

**Requirements:** keyboard behavior, active state, ARIA sync, mobile horizontal overflow or dropdown fallback when needed.

---

## C14 — Accordion

**Hierarchy:** Component  
**Purpose:** progressive disclosure, mainly FAQ/details.

**Sample:**
```html
<article class="orx-accordion-item">
  <h3><button aria-expanded="false" aria-controls="faq-1">ما الحد الأدنى للطلب؟</button></h3>
  <div id="faq-1" hidden>يتم تحديده حسب المنتج.</div>
</article>
```

---

## C15 — Pagination

**Hierarchy:** Component  
**Purpose:** navigate result pages.

**Rule:** previous/next direction mirrors visually in RTL/LTR; current page has semantic state.

---

## C16 — Search Control

**Hierarchy:** Component  
**Purpose:** keyword search in product/supplier/blog/FAQ datasets.

**Anatomy:** label → input → clear/search utility → result count when relevant.

---

## C17 — Filter Group

**Hierarchy:** Component  
**Purpose:** constrain directory/list results.

**Strategy:** desktop inline/sidebar; mobile drawer when crowded.

**Rule:** filter UI stays one component across Products, Suppliers, Markets and Blog; only options change.

---

# DATA & CONTENT COMPONENTS

## C18 — Specification Table

**Hierarchy:** Component  
**Purpose:** product/compliance/service structured data.

**Strategy:** semantic table on desktop, documented scroll/stack behavior on mobile.

**Sample:**
```html
<table class="orx-spec-table">
  <tbody><tr><th scope="row">Pack Size</th><td>12 × 500 g</td></tr></tbody>
</table>
```

---

## C19 — Stat Strip

**Hierarchy:** Pattern/Component  
**Purpose:** compact row of 2–4 metrics.

**Rule:** built from C06 Metric Cards; no separate visual invention.

---

## C20 — Trust Item

**Hierarchy:** Component  
**Purpose:** concise proof/principle item in trust strips.

**Anatomy:** icon/code → title → short supporting line.

---

## C21 — Empty State

**Hierarchy:** Component  
**Purpose:** no search/filter results, no downloads, or unavailable content.

**Anatomy:** clear title → explanation → recovery action.

**Rule:** never leave blank grids.

---

## C22 — Alert / Notice

**Hierarchy:** Primitive/Component  
**Purpose:** contextual Info / Success / Warning / Danger messages.

**Rule:** semantic colors + icon/text; no decorative use.

---

# FORMS

## C23 — Form Field

**Hierarchy:** Component  
**Purpose:** compose label + control + help/error.

**Anatomy:** label → required marker → control → help/error slot.

**Rule:** all Contact/RFQ/Product Submission/Partner forms use this same field contract.

---

## C24 — File Upload

**Hierarchy:** Component  
**Purpose:** attach product/company/document files.

**Strategy:** accessible native input with styled surface; file rules visible.

**Rule:** never imply upload backend exists if demo is static; documentation identifies integration point.

---

## C25 — Form Status

**Hierarchy:** Component  
**Purpose:** loading/success/error confirmation state.

**Rule:** status announced accessibly and not color-only.

---

# MEDIA

## C26 — Product Media Frame

**Hierarchy:** Component  
**Purpose:** consistent product imagery.

**Strategy:** controlled aspect ratios and object-fit behavior.

**Rule:** same media frame in Product Card and Product Details variants where applicable.

---

## C27 — Logo Frame

**Hierarchy:** Component  
**Purpose:** normalize supplier/brand logos of different proportions.

**Strategy:** neutral background, controlled padding, contain fit.

---

## C28 — Editorial Media

**Hierarchy:** Component  
**Purpose:** company/process/market visual storytelling.

**Rule:** aspect-ratio families defined centrally; page selects family, not arbitrary crop rules.

---

# SECTION BUILDING BLOCKS

## S01 — Section Header

**Hierarchy:** Section primitive  
**Purpose:** consistent start of content sections.

**Anatomy:** eyebrow/kicker → H2 → supporting copy → optional action.

**Approved alignments:** Start / Center.  
**Rule:** no new heading anatomy per page.

**Sample:**
```html
<header class="orx-section-head">
  <div><span class="orx-eyebrow">المنتجات</span><h2>فئات مختارة للسوق.</h2></div>
  <p>استعرض المنتجات حسب الفئة والمنشأ والعلامة.</p>
</header>
```

---

## S02 — Split Hero

**Hierarchy:** Section  
**Purpose:** primary commercial home/business hero.

**Anatomy:** eyebrow → H1 → lead → primary/secondary actions → media/visual.

**Rule:** maximum two CTAs; mobile content order explicitly defined.

---

## S03 — Centered Editorial Hero

**Hierarchy:** Section  
**Purpose:** About, How We Work, FAQ, resources-type pages where content is primary.

**Anatomy:** breadcrumb optional → eyebrow → H1 → lead → optional action.

---

## S04 — Detail Hero

**Hierarchy:** Section  
**Purpose:** Product, Supplier, Service and Case Study detail pages.

**Anatomy:** breadcrumb → metadata/badges → title → summary → key actions → detail media/identity.

---

## S05 — Utility Hero

**Hierarchy:** Section  
**Purpose:** 404, Coming Soon, Privacy, Terms.

**Strategy:** compact and low-motion.

---

## S06 — Final CTA

**Hierarchy:** Section  
**Purpose:** close a page with one clear commercial next step.

**Anatomy:** kicker → title → supporting copy → primary action → optional secondary.

**Rule:** one visual contract globally; content changes by page goal.

---

# GLOBAL NAVIGATION PATTERNS

## N01 — Site Header

**Hierarchy:** Pattern  
**Purpose:** brand + primary navigation + language + primary CTA.

**Strategy:** one header architecture across the full product.

**Rule:** pages do not create their own header versions in V1; Home demos may change content emphasis through approved header state only, not architecture.

---

## N02 — Mega Menu

**Hierarchy:** Pattern  
**Purpose:** expose primary business routes without overloading top nav.

**Rule:** configured globally; keyboard/escape/click-outside behavior consistent.

---

## N03 — Mobile Drawer

**Hierarchy:** Pattern  
**Purpose:** mobile navigation equivalent of N01/N02.

**Rule:** not a separate IA; same destinations and priorities adapted for mobile.

---

## N04 — Footer

**Hierarchy:** Pattern  
**Purpose:** company summary, navigation, resources, contacts, legal/social.

**Rule:** one footer architecture; content/config values may vary globally only.

---

# GOVERNANCE SUMMARY

## Page usage rule

A Page Design Profile may declare:
```text
Hero: S04 Detail Hero
Cards: C02 Product Card + C07 Certification Card
Filters: C16 Search + C17 Filter Group
Data: C18 Specification Table
CTA: S06 Final CTA
```

It may not declare:
```text
Custom Product Card just for this page
New Button shape because hero looks empty
Different badge colors unrelated to semantic meaning
Page-only form styling
```

## Variant cap

To prevent template bloat:
- Primitive: normally max 3 visual variants.
- Card family: normally max 3 variants.
- Hero family: only the four approved V1 families.
- Section header: Start or Center only.
- Motion: Levels 0 / 1 / 2 only.

A new variant requires registry change before page use.

## Source authority

This registry + `DESIGN-SYSTEM-HIERARCHY-V1.md` + `COMPONENT-DESIGN-RULES-V1.md` are the V1 component authority.

Copyright © ORVEAX.
