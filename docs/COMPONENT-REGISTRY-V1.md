# ORIGEX — Unified Component Registry V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED BASE REGISTRY — V1 MAIN FEATURES  
Normalized: 2026-08-19 Hard Audit

This is the central reusable UI registry for ORIGEX. Pages consume these IDs and approved variants; they do not create local visual forks.

Authority companions:
- `DESIGN-SYSTEM-HIERARCHY-V1.md`
- `COMPONENT-DESIGN-RULES-V1.md`
- `ICON-SYSTEM-V1.md`
- `PATTERN-SYSTEM-V1.md`
- `IMAGE-MEDIA-SYSTEM-V1.md`
- `PAGE-DESIGN-PROFILE-TEMPLATE-V1.md`

Core rule:

> Define once → register → test AR/EN/mobile/accessibility → reuse everywhere → change centrally.

---

# FOUNDATIONS

## F01 — Color System
**Purpose:** brand, surface, text and semantic color roles.

**Core roles:** Primary, Primary Strong, Secondary, Accent, Background, Surface, Surface Soft, Text, Text Muted, Border, Strong Border, Success, Warning, Danger, Info.

**Rule:** colors are role-based, not page-based. Page CSS may consume tokens; it may not invent decorative palette values.

## F02 — Typography System
**Purpose:** one semantic hierarchy with independent Arabic/English metrics.

**Arabic:** Tajawal.  
**English:** Manrope.

**Roles:** Display, H1, H2, H3, H4, Body Large, Body, Small, Label/Eyebrow, UI/Button.

**Rules:**
- no arbitrary page font sizes;
- Arabic line-height is tuned independently;
- English letter-spacing is not copied into Arabic;
- mixed LTR data remains bidi-safe.

## F03 — Spacing, Grid & Layout
**Purpose:** consistent rhythm, containers and responsive composition.

**Authority:** `FOUNDATION-FREEZE-V1.md` + Bootstrap 5.3.8 infrastructure.

**Container profiles:** Narrow / Standard / Wide / Full Bleed.  
**Density profiles:** Compact / Standard / Comfortable.

**Rules:**
- logical CSS properties;
- Bootstrap grid/container infrastructure where appropriate;
- mobile is composed, not compressed desktop;
- page gutters and section spacing come from ORIGEX tokens.

## F04 — Shape, Border & Elevation
**Purpose:** control radius, borders and hierarchy/elevation.

**Radius:** XS / SM / MD / LG / Pill.  
**Elevation:** E0 / E1 / E2 / E3.

**Rule:** no page-local radius/shadow language. Elevation communicates state/hierarchy, not decoration.

## F05 — Icon System
**Authority:** `ICON-SYSTEM-V1.md`.

**Primary semantic family:** Lucide.  
**Style:** Outline.  
**Base grid:** 24×24.  
**Default stroke:** 2.  
**Sizes:** 14 / 16 / 20 / 24 / 32 / 40px.  
**Delivery:** selected local SVGs / local SVG sprite.

**Rules:**
- semantic icons use Lucide only;
- brand/social marks are separate official/licensed assets;
- no text placeholders such as `IMP`, `SUP`, `SRC`, `WA`, `×` as production icon substitutes;
- directional icons swap/mirror by meaning in RTL; never blanket-flip all SVGs;
- decorative icons use `aria-hidden="true"`;
- icon-only controls require an accessible label.

## F06 — Motion & Interaction
**Purpose:** consistent interaction feedback without decorative excess.

**Durations:** Fast 150ms / Standard 250ms / Slow 400ms.  
**Levels:** L0 / L1 / L2.

**Rules:**
- `prefers-reduced-motion` mandatory;
- no scroll-jacking, bouncing, continuous decorative loops or page-specific animation libraries;
- state changes must remain understandable without motion.

## F07 — Media & Pattern Foundations
**Authorities:** `IMAGE-MEDIA-SYSTEM-V1.md` and `PATTERN-SYSTEM-V1.md`.

**Rules:**
- registered media aspect-ratio/frame families only;
- PT01–PT06 are the only V1 ORIGEX pattern families;
- third-party stock is preview-only by default unless exact redistribution rights are logged.

---

# PRIMITIVES

## P01 — Primary Button
**Purpose:** dominant action in a decision area.  
**Variants:** Small / Default / Large.  
**States:** Default / Hover / Focus Visible / Disabled.

**Rule:** normally one dominant primary action per local decision group.

## P02 — Secondary Button
**Purpose:** explicit secondary action.  
**Strategy:** quieter surface/outline treatment; never visually competes with P01.

## P03 — Text Action
**Purpose:** tertiary navigation/action.

**Sample:**
```html
<a class="orx-text-action" href="products.html">
  <span>استعرض المنتجات</span>
  <svg class="orx-icon orx-icon--sm" aria-hidden="true"><use href="../assets/icons/sprite.svg#arrow-left"></use></svg>
</a>
```

**RTL rule:** Arabic uses the semantically correct directional icon; English uses its counterpart. No global SVG transform.

## P04 — Icon Button
**Purpose:** compact utility controls: close, menu, search, previous/next.

**Sample:**
```html
<button class="orx-icon-btn" type="button" aria-label="إغلاق القائمة">
  <svg class="orx-icon" aria-hidden="true"><use href="../assets/icons/sprite.svg#x"></use></svg>
</button>
```

**Rules:** accessible name, minimum touch target, F05 dependency.

## P05 — Badge
**Purpose:** short semantic metadata.

**Variants:** Category / Origin / Certification / Availability / Featured / Updated.

**Rule:** status is never communicated by color alone.

## P06 — Form Input
**Purpose:** text/email/tel/etc. input.  
**Rule:** visible label + help/error slot; email/tel values remain bidi-safe.

## P07 — Select
**Purpose:** finite selection.  
**Rule:** native semantics first; registered styling only.

## P08 — Textarea
**Purpose:** multi-line enquiry/context.  
**Rule:** centrally controlled minimum height and resize behavior.

## P09 — Checkbox / Radio
**Purpose:** consent and finite choices.  
**Rule:** native semantics preserved and mobile target adequate.

## P10 — Divider
**Purpose:** separate groups only where spacing alone is insufficient.

## P11 — Icon Container
**Purpose:** registered visual frame around a semantic icon in feature/process/contact/trust contexts.

**Approved sizes:** 48 / 56 / 64px.  
**Dependencies:** F01 / F04 / F05.

**Rules:**
- same icon-box grammar across compatible components;
- background/border/radius use ORIGEX tokens;
- no one-off page icon tile;
- 64px reserved for contexts that genuinely need stronger emphasis.

---

# COMPONENTS — CARD FAMILIES

## C01 — Feature Card
**Purpose:** capability, benefit or commercial function.  
**Anatomy:** P11 icon container → optional index → title → supporting copy → optional metadata.  
**Variants:** Standard / Emphasis.  
**States:** Default / Active only where semantic.

**Sample:**
```html
<article class="orx-feature-card">
  <div class="orx-icon-box orx-icon-box--md">
    <svg class="orx-icon" aria-hidden="true"><use href="../assets/icons/sprite.svg#package"></use></svg>
  </div>
  <span class="orx-feature-card__index">01</span>
  <h3 class="orx-feature-card__title">الاستيراد والتجارة</h3>
  <p class="orx-feature-card__copy">مسار تجاري واضح من المصدر إلى السوق.</p>
</article>
```

## C02 — Product Card
**Purpose:** represent a product in listing/related contexts.  
**Anatomy:** media → badges → product name → brand/origin → compact specs → action.  
**Variants:** Standard / Compact / Featured.  
**States:** Available / Unavailable / Featured.

**Rule:** Home, Products, Supplier Details and Related Products reuse the same component; pages change placement/grid, not anatomy.

## C03 — Supplier / Brand Card
**Purpose:** represent manufacturer, supplier or brand.  
**Anatomy:** C27 Logo Frame → name → country → categories → action.  
**Variants:** Standard / Featured.

## C04 — Market Card
**Purpose:** summarize a country/market opportunity.  
**Anatomy:** market identity → country → channel tags → short summary → action.

## C05 — Process Card
**Purpose:** one step inside a process/journey.  
**Anatomy:** step number → optional P11 icon → title → explanation → optional requirement/outcome.  
**Rule:** numbering/order is independently correct in AR and EN.

## C06 — Metric / Stat Card
**Purpose:** quantified fact.  
**Anatomy:** value → unit/suffix → label → optional note.  
**Rule:** meaningful factual/clearly illustrative values only; no fake decorative metrics.

## C07 — Certification Card
**Purpose:** certification/compliance item.  
**Anatomy:** controlled mark/frame → title → issuer/type → status/metadata → optional action.  
**Rule:** demo content never implies a fictional company actually owns a certificate.

## C08 — Resource / Download Card
**Purpose:** brochure, profile, datasheet, certificate or resource.  
**Anatomy:** file type/icon → title → metadata → download/view action.

## C09 — Case Study Card
**Purpose:** summarize a business proof/story.  
**Anatomy:** media → tags → title → result highlight → action.  
**Rule:** illustrative case data must be disclosed according to Demo policy.

## C10 — Contact / Department Card
**Purpose:** contact channel or department.  
**Anatomy:** P11 icon → department/title → short description → contact/action.

## C11 — CTA Card
**Purpose:** contained conversion area inside a page.  
**Anatomy:** kicker → title → supporting copy → primary action → optional secondary.  
**Rule:** does not replace S06 Final CTA.

---

# NAVIGATION & DISCLOSURE COMPONENTS

## C12 — Breadcrumb
**Purpose:** page hierarchy and recovery.  
**Rule:** semantic `<nav>`; order/direction independently tested AR/EN; aligns with SEO page identity.

## C13 — Tabs
**Purpose:** switch peer content views without page navigation.  
**Requirements:** keyboard behavior, active state, ARIA sync, mobile overflow/fallback strategy.

## C14 — Accordion
**Purpose:** progressive disclosure, primarily FAQ/details.  
**Requirements:** semantic heading/button structure, `aria-expanded`, controlled panel IDs, keyboard/native button behavior.

## C15 — Pagination
**Purpose:** navigate result pages.  
**Rule:** current page semantic state; previous/next direction correct per locale.

## C16 — Search Control
**Purpose:** keyword search in product/supplier/blog/FAQ datasets.  
**Anatomy:** label → input → registered icon utility → result count when relevant.

## C17 — Filter Group
**Purpose:** constrain directory/list results.  
**Strategy:** desktop inline/sidebar; mobile drawer when crowded.  
**Rule:** one component across Products/Suppliers/Markets/Blog; only options/data differ.

---

# DATA & CONTENT COMPONENTS

## C18 — Specification Table
**Purpose:** product/compliance/service structured data.  
**Strategy:** semantic table on desktop with approved mobile scroll/stack/definition-list behavior.

## C19 — Stat Strip
**Purpose:** compact row of 2–4 metrics.  
**Rule:** composition of C06; not a separate visual invention.

## C20 — Trust Item
**Purpose:** concise proof/principle item.  
**Anatomy:** P11 icon or approved compact icon treatment → title → short supporting line.

## C21 — Empty State
**Purpose:** no results/downloads/unavailable content.  
**Anatomy:** icon optional → clear title → explanation → recovery action.  
**Rule:** never leave a blank grid.

## C22 — Alert / Notice
**Purpose:** Info / Success / Warning / Danger messages.  
**Rule:** semantic icon + text + semantic tokens; never color-only.

---

# FORMS

## C23 — Form Field
**Purpose:** label + control + help/error composition.  
**Rule:** Contact/RFQ/Product Submission/Partner forms share this contract.

## C24 — File Upload
**Purpose:** attach product/company/document files.  
**Strategy:** accessible native input with registered styled surface and visible file rules.  
**Rule:** never imply backend upload exists when the demo is static.

## C25 — Form Status
**Purpose:** loading/success/error confirmation state.  
**Rule:** status announced accessibly and not color-only.

---

# MEDIA

## C26 — Product Media Frame
**Purpose:** consistent product imagery.  
**Strategy:** approved aspect ratio/object-fit/background treatment from Image/Media System.

## C27 — Logo Frame
**Purpose:** normalize supplier/brand logos of different proportions.  
**Strategy:** neutral controlled surface + padding + `object-fit: contain`.

## C28 — Editorial Media
**Purpose:** company/process/market visual storytelling.  
**Rule:** page selects an approved media family; it does not invent crop/aspect rules.

---

# SECTION BUILDING BLOCKS

## S01 — Section Header
**Purpose:** consistent section introduction.  
**Anatomy:** eyebrow/kicker → H2 → supporting copy → optional action.  
**Alignments:** Start / Center only.

## S02 — Split Hero
**Purpose:** primary commercial home/business hero.  
**Anatomy:** eyebrow → H1 → lead → primary/secondary actions → media/visual.  
**Rule:** max two CTAs; mobile order explicit.

## S03 — Centered Editorial Hero
**Purpose:** About/How We Work/FAQ/Resources type pages.  
**Anatomy:** breadcrumb optional → eyebrow → H1 → lead → optional action.

## S04 — Detail Hero
**Purpose:** Product/Supplier/Service/Case Study detail pages.  
**Anatomy:** breadcrumb → metadata/badges → title → summary → key actions → media/identity.

## S05 — Utility Hero
**Purpose:** 404 / Coming Soon / Privacy / Terms.  
**Strategy:** compact and low-motion.

## S06 — Final CTA
**Purpose:** close a page with one clear commercial next step.  
**Anatomy:** kicker → title → supporting copy → primary → optional secondary.  
**Rule:** one visual contract globally.

---

# GLOBAL NAVIGATION PATTERNS

## N01 — Site Header
**Purpose:** brand + primary navigation + language + primary CTA.  
**Rule:** one architecture across V1; home demos do not invent separate headers.

## N02 — Mega Menu
**Purpose:** expose major business routes without overloading top navigation.  
**Rule:** global configuration; keyboard/Escape/outside-click behavior consistent.

## N03 — Mobile Drawer
**Purpose:** mobile navigation equivalent of N01/N02.  
**Rule:** same information architecture adapted to mobile.

## N04 — Footer
**Purpose:** company summary, navigation, resources, contacts, legal/social.  
**Rule:** one architecture; repeated values may come from approved config hooks.

---

# REGISTRY GOVERNANCE

## Page Design Profile rule
A page declares registry IDs, for example:

```text
Hero: S04
Primary Cards: C02
Trust: C20
Search/Filters: C16 + C17
Data: C18
CTA: S06
Navigation: N01 + N02 + N03 + N04
```

It may not declare a page-only Product Card, Button, Badge, Form style, Icon style, Shadow, Radius, Header or Animation language.

## Variant cap
- primitives: normally max 3 visual variants;
- card families: normally max 3 variants;
- hero families: S02–S05 only;
- section header: Start / Center only;
- motion: L0 / L1 / L2 only.

A new repeated need follows this path:

```text
Need identified
→ test existing registry
→ define central variant/component if genuinely necessary
→ document/register
→ AR/EN/mobile/accessibility QA
→ reuse
```

## Bootstrap boundary
Bootstrap 5.3.8 may provide layout/infrastructure and selected behavior primitives. It cannot bypass this registry or replace ORIGEX branded components with Bootstrap defaults.

## Icon boundary
All production semantic icon examples/implementations depend on F05. Placeholder text/glyph icons from historical builds are prohibited.

## Status
This normalized registry supersedes pre-hard-audit examples while preserving established IDs C01–C28, S01–S06 and N01–N04. P11 is added without renumbering existing primitives.

Copyright © ORVEAX.
