# ORIGEX — V1 Foundation Freeze

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & FROZEN  
Approval Date: 2026-08-19

This document is the canonical authority for ORIGEX V1 foundation decisions. Page implementation must consume these rules. Foundation decisions are not reopened during normal page work. Any change to a frozen foundation requires a documented Design System / Architecture / Content-System Change Request.

## 1. Approved Technology Foundation

- HTML5.
- CSS3.
- Bootstrap 5.x as layout/responsive foundation only.
- Vanilla JavaScript for ORIGEX interactions.
- ORIGEX Design System controls branded components and patterns.
- `config.js` controls approved global/repeated settings.
- JSON is used for approved structured product/supplier/market data where needed.
- No React, Vue, Astro runtime, Tailwind, jQuery, mandatory Node/build process, or heavy animation framework in V1 customer package.

## 2. Design-System Hierarchy

Foundation → Primitive → Component → Pattern → Section → Page Design Profile.

Pages compose registered components. Pages do not visually fork components through local CSS. A genuinely new variant must be registered centrally before page use.

## 3. Grid / Container / Responsive System

Bootstrap grid is the structural base.

ORIGEX container profiles:
- Narrow content: max 840px.
- Standard content: max 1140px.
- Wide content: max 1320px.
- Full bleed: viewport width with controlled inner content.

Horizontal page gutters:
- Mobile: 20px.
- Tablet: 24px.
- Desktop: 32px.

Rules:
- Use the 12-column Bootstrap grid where grid layout is appropriate.
- Use logical CSS properties for directional spacing.
- Mobile is a composed layout, not compressed desktop.
- No horizontal overflow at supported QA widths.
- Arabic and English ordering is tested independently.

Primary QA widths remain: 360, 390, 412, 768, 820, 1024, 1280, 1366, 1440, 1536, 1920.

## 4. Shape / Border / Elevation Tokens

Radius tokens:
- `--orx-radius-xs: 8px`
- `--orx-radius-sm: 12px`
- `--orx-radius-md: 16px`
- `--orx-radius-lg: 24px`
- `--orx-radius-pill: 999px`

Border tokens:
- Subtle: 1px using soft border token.
- Default: 1px using standard border token.
- Strong: 2px only where hierarchy/state requires it.

Elevation:
- E0: none.
- E1: restrained surface separation.
- E2: interactive/featured card emphasis.
- E3: overlays, drawers, dropdowns/modals only.

Rules:
- No page-local radius, border or shadow language.
- Elevation communicates hierarchy/state, not decoration.

## 5. Motion / Interaction System

Duration tokens:
- Fast: 150ms.
- Standard: 250ms.
- Slow: 400ms.

Motion levels:
- Level 0: utility/legal — near-static.
- Level 1: normal business/product UI — subtle transitions.
- Level 2: selected home/landing areas — controlled premium reveals.

Approved motion uses:
- color/background/border transitions.
- restrained transform for cards/actions.
- accordion/tabs/menu/drawer/modal state transitions.
- directional arrow micro-motion.

Prohibited:
- scroll-jacking.
- continuous decorative loops.
- bouncing UI.
- motion that delays essential content.
- page-specific animation libraries.

`prefers-reduced-motion` is mandatory.

## 6. Icon System

Authority: `ICON-SYSTEM-V1.md`.

- Lucide is the single primary semantic icon family.
- Outline, 24×24 base grid, default stroke 2.
- Sizes: 14 / 16 / 20 / 24 / 32 / 40px.
- Local SVG / SVG sprite delivery.
- `currentColor` + ORIGEX semantic tokens.
- Directional icons only mirror/swap in RTL.
- Brand/social marks are separate official/separately licensed assets.
- Multiple semantic icon libraries are prohibited.

## 7. Pattern System

Authority: `PATTERN-SYSTEM-V1.md`.

Approved families:
- PT01 Route Lines.
- PT02 Trade Grid.
- PT03 Dot Matrix.
- PT04 Market Nodes.
- PT05 Packaging Geometry.
- PT06 Flow Lines.

Patterns are custom ORIGEX SVG/CSS assets. External pattern libraries are reference/exploration tools only and are not runtime dependencies or default distributed assets.

## 8. Image / Media System

Authority: `IMAGE-MEDIA-SYSTEM-V1.md`.

Core direction: Natural Industrial Premium, focused on B2B food trading, wholesale, distribution, manufacturing, logistics, products and market access.

Default asset policy:
- Third-party stock photography may be used for preview only after source/license verification.
- Third-party stock photography is not included in the buyer ZIP by default.
- Buyer ZIP uses ORVEAX-created placeholders, SVG/CSS graphics and explicitly redistributable assets only.
- Every preview/distributed asset must be logged in the Asset Register.

## 9. Media Frame System

Approved aspect-ratio families:
- Hero: 3:2 or 16:10; mobile editorial crop 4:5.
- Product: 1:1 primary.
- Supplier/brand media: 4:3; logos use controlled logo frame.
- Blog: 16:9.
- Case study/facility: 16:10 or 3:2 according to registered component.
- Avatar: 1:1 if used.

Rules:
- `object-fit` behavior is controlled centrally.
- Product, supplier logo, certification, resource and editorial frames are registered components, not arbitrary image boxes.

## 10. Data Architecture

Authority: `DATA-SCHEMA-V1.md`.

Canonical data domains:
- Products.
- Suppliers/brands.
- Markets/countries.

`config.js` does not become a CMS. Page editorial content stays in HTML; structured repeated business data uses documented JSON schemas when data-driven behavior is required.

## 11. Code Architecture / Naming

Authority: `CODE-ARCHITECTURE-V1.md`.

- ORIGEX-owned CSS classes use `orx-` prefix.
- Component naming follows BEM-like anatomy: `.orx-component`, `.orx-component__part`, `.orx-component--variant`.
- JS hooks use `data-orx-*`; styling must not depend on JS-only hook names.
- CSS tokens use `--orx-*`.
- Files use lowercase kebab-case.
- No page-specific component forks/hotfix layers without documented exception.

## 12. Browser Support

V1 targets modern evergreen browsers:
- current and previous two major desktop generations of Chrome, Edge, Firefox and Safari where practical.
- current mainstream iOS Safari and Android Chromium-based browsers.

No legacy Internet Explorer support.

Progressive enhancement is preferred: content and navigation should remain understandable when non-essential JavaScript is unavailable.

## 13. Performance Budget

- Bootstrap is the only approved general UI foundation dependency.
- No duplicate icon/component libraries.
- Core icons local.
- Below-fold imagery lazy-loaded.
- Width/height declared for raster imagery where practical.
- Modern compressed image formats preferred.
- Non-critical scripts deferred.
- Feature JS loaded/initialized only where required.
- No unoptimized multi-megabyte preview images.
- No third-party script required for core navigation/layout.
- CSS/JS duplication is a QA defect.

Performance optimization does not reopen scope or design decisions.

## 14. Content System

Authorities:
- `CONTENT-SYSTEM-V1.md`.
- `MASTER-CONTENT-ARCHITECTURE-V1.md`.
- `DEMO-CONTENT-DATASET-V1.md`.
- V1.1 Content Pack files for deferred Additional Features.

Locked rules:
- Arabic is the master commercial language.
- English is a professional adaptation, not literal translation.
- Main Features and Additional Features use the same Content Contract.
- No page or feature enters implementation before Content Status C6 — FROZEN.
- Product/supplier/market demo facts use one canonical dataset and stable IDs.
- No lorem ipsum in the commercial preview.
- Unsupported claims, fake customers, fake certifications and fake performance metrics are prohibited.
- Demo facts that can look factual must be disclosed as illustrative.
- CTA vocabulary, microcopy, form states and disclaimers follow the Content System.
- A future Additional Feature is incomplete until its full AR/EN Content Pack exists.

Content corrections that fix verified facts do not reopen the foundation. A new audience promise, writing model, or commercial-content architecture requires a Content-System Change Request.

## 15. QA Definition of Done

Authority: `QA-DEFINITION-OF-DONE-V1.md`.

A page is not closed until its Content/Page/Component Definition of Done passes. After closure, it reopens only for:
- verified bug.
- accessibility/performance/responsive defect.
- verified factual/content correction.
- formal change request.

## 16. Governance Lock

The following are frozen for V1:
- stack.
- grid/container strategy.
- typography hierarchy.
- palette/tokens.
- radii/borders/elevation.
- component registry and governance.
- icon system.
- pattern system.
- image/media strategy.
- motion system.
- data schema principles.
- code naming/architecture.
- browser support.
- content-writing mechanism.
- bilingual adaptation rules.
- demo-data consistency rules.
- CTA/microcopy/content-state rules.
- QA Definition of Done.

Normal page development cannot reopen these decisions.

Copyright © ORVEAX.
