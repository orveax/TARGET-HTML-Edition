# ORIGEX — Icon System V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Primary Icon Family: Lucide  
Style: Outline

## 1. Purpose

ORIGEX uses one controlled semantic icon language across all pages and components. Icons support meaning, navigation, actions and hierarchy; they are not decorative substitutes for content.

## 2. Primary System

- Primary semantic icon library: Lucide.
- Delivery: local SVG assets / SVG sprite in the customer package.
- No CDN dependency for core icons.
- No second semantic icon library in V1.
- Bootstrap Icons are not used as a parallel semantic system.
- Brand/social logos are handled separately as official or separately licensed brand assets.

## 3. Visual Grammar

- Base grid: 24 × 24.
- Default stroke: 2.
- Large decorative/feature icons may use 1.75–2 only when visually required.
- Line caps and joins follow the Lucide source grammar.
- Icons inherit `currentColor` unless a semantic state requires a token.
- No page-specific icon color palettes.

## 4. Size Scale

Approved icon sizes:
- XS: 14px.
- SM: 16px.
- MD: 20px.
- LG: 24px.
- XL: 32px.
- 2XL: 40px.

Most interface controls use 16 / 20 / 24px. 32 / 40px are reserved for feature, hero or controlled icon-box use.

## 5. Semantic Registry

### I01 — Navigation
Examples: menu, close, home, chevron, external link.

### I02 — Actions
Examples: search, filter, download, upload, send, plus, minus, edit, print.

### I03 — Status
Examples: check, info, warning, error, clock, availability indicators.

### I04 — Business / Capability
Examples: briefcase, building, route, handshake, warehouse, truck.

### I05 — Product
Examples: package, boxes, tag, barcode, scale, layers.

### I06 — Supplier / Brand
Examples: factory, building, badge, users, handshake.

### I07 — Market
Examples: globe, map, map-pin, route, navigation.

### I08 — Documents / Compliance
Examples: file-text, file-check, download, shield-check, badge-check.

### I09 — Contact
Examples: phone, mail, map-pin, clock, message-circle.

### I10 — Directional
Examples: arrow-left/right, chevron-left/right, previous/next.

### I11 — Brand / Social
Not Lucide. Official or separately licensed brand assets only.

## 6. Canonical Mapping Rule

A semantic concept maps to one default icon across the product. Examples:
- Product → Package.
- Product Category → Boxes.
- Brand → Tag.
- Country / Origin → MapPin or Globe according to context.
- Shelf Life / Date → Calendar.
- Storage → Warehouse.
- Datasheet / Document → FileText.
- Download → Download.
- RFQ / Send Enquiry → Send.
- Certification / Compliance → BadgeCheck or ShieldCheck.
- Search → Search.
- Filter → SlidersHorizontal / Filter according to the documented component.

Pages may not select a different icon for the same semantic meaning without updating this central system.

## 7. Icon Box Component

Approved icon-box sizes:
- Small: 48 × 48.
- Medium: 56 × 56.
- Large: 64 × 64.

Icon-box radius, border, background and color must use ORIGEX tokens. A page cannot invent a new icon container style locally.

## 8. RTL / LTR Rules

Only direction-dependent icons mirror or swap under RTL:
- arrows.
- chevrons.
- previous / next.
- forward / back.
- directional navigation cues.

Semantic icons do NOT mirror:
- phone.
- mail.
- globe.
- package.
- truck.
- warehouse.
- certificate.
- search.
- download.
- calendar.
- clock.
- user.

Global `scaleX(-1)` rules on all SVG icons are prohibited.

## 9. Accessibility

Decorative icon:
```html
<svg class="orx-icon" aria-hidden="true">...</svg>
```

Icon-only control:
```html
<button class="orx-icon-btn" type="button" aria-label="بحث">
  <svg class="orx-icon" aria-hidden="true">...</svg>
</button>
```

Rules:
- Essential meaning must not depend on icon alone.
- Status must include text or another accessible label, not color/icon only.
- Icon-only controls require an accessible name.
- Focus behavior belongs to the interactive control, not the SVG.

## 10. Motion

Allowed:
- color transition.
- subtle 1–2px directional movement for arrows.
- controlled chevron rotation for disclosure components.
- restrained scale only where interaction benefits.

Prohibited:
- looping/bouncing icons.
- random rotation.
- decorative glow as standard UI.
- motion that delays or obscures meaning.

`prefers-reduced-motion` must be respected.

## 11. Asset Packaging

Recommended structure:
```text
assets/
└── icons/
    ├── sprite.svg
    ├── brands/
    └── README.md
```

Only icons required by ORIGEX V1 should ship in the production package where practical. License notices and attribution requirements are retained in the licensing/credits documentation.

## 12. Custom Icons

A custom ORIGEX icon is allowed only when the approved Lucide library does not provide a semantically adequate option.

Custom icon requirements:
- same 24 × 24 base grid.
- same visual weight and stroke grammar.
- registry entry before use.
- documented purpose.
- no page-local one-off SVG styling.

## 13. Component Integration

Registered ORIGEX components consume this icon system. A page cannot bypass the component registry to introduce its own icon style.

Examples:
- P04 Icon Button uses approved I01/I02/I10 icons.
- C01 Feature Card uses approved I04–I09 semantic icons.
- C05 Process Card uses one mapped semantic icon per step.
- C07 Certification Card uses I08.
- C10 Contact Card uses I09.
- C13/C14/C15 navigation/disclosure controls use I10.

## 14. Governance

Any new icon meaning must answer:
1. Is an existing semantic mapping already available?
2. Is the icon necessary for comprehension or navigation?
3. Does it match the approved visual grammar?
4. Does it behave correctly in RTL and LTR?
5. Is licensing/distribution clear?

If the answer requires a new mapping or custom icon, update this file before page implementation.

Copyright © ORVEAX.
