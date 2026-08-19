# ORIGEX — V1 Technology Stack

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Exact Bootstrap Baseline: **5.3.8**

This file is the exact technology-version authority. Where broader foundation documents use the family label `Bootstrap 5.x`, this document fixes the ORIGEX V1 implementation/package baseline to **Bootstrap 5.3.8**.

## 1. Approved V1 Stack

ORIGEX V1 uses:

- HTML5.
- CSS3.
- Bootstrap **5.3.8** as responsive/layout infrastructure.
- Vanilla JavaScript for ORIGEX-specific interactions.
- ORIGEX Design System for all branded visual components.
- `config.js` for simple global customization.
- JSON data files where structured product/supplier/market data is useful.

## 2. Bootstrap Delivery

Buyer-package core layout/navigation must not depend on a CDN.

M1 must package the required Bootstrap 5.3.8 compiled production files locally under:

```text
assets/vendor/bootstrap/
```

The exact shipped files and MIT notice must be logged in `ASSET-LICENSE-REGISTER-V1.md`.

Documentation may show CDN usage as an optional alternative, never as the required runtime.

## 3. Bootstrap Role

Bootstrap is infrastructure, not ORIGEX visual identity.

Approved Bootstrap usage:
- Grid.
- Containers.
- Breakpoints.
- Selected flex/display/spacing utilities.
- Selected behavior primitives such as Collapse/Offcanvas only when M1 determines they reduce custom code without changing the ORIGEX visual/component contract.

ORIGEX does not use default Bootstrap visual components as substitutes for the product design system.

ORIGEX-owned visual components include:
- buttons;
- cards;
- forms;
- product/supplier/market UI;
- navigation composition;
- sections/heroes;
- CTAs;
- typography/colors;
- shape/elevation;
- icon containers;
- motion language.

## 4. Architecture Order

```text
Bootstrap 5.3.8 Infrastructure
→ ORIGEX Tokens
→ ORIGEX Primitives
→ ORIGEX Components
→ ORIGEX Patterns
→ ORIGEX Sections
→ Page Design Profiles
```

A page must never override an approved ORIGEX component simply because Bootstrap offers a default alternative.

## 5. JavaScript Rule

Use Vanilla JavaScript for ORIGEX-specific behavior.

Typical use cases:
- navigation behavior;
- tabs/accordions;
- filters/search/sorting;
- form validation;
- config engine;
- announcement/global utility behavior;
- lightweight UI state.

Bootstrap JavaScript may be used selectively for stable primitives. The decision must be consistent across the project; page-level mixed implementations are prohibited.

## 6. Explicit V1 Exclusions

- No React.
- No Vue.
- No Astro runtime in the buyer package.
- No Tailwind.
- No jQuery.
- No mandatory Node/build process.
- No heavy animation framework as a core dependency.

The buyer must be able to edit and run the template as a conventional static HTML package.

## 7. Buyer Experience

Beginner:
- edits `config.js`;
- follows Getting Started documentation.

Intermediate buyer:
- edits HTML and approved Bootstrap layout utilities/classes.

Developer:
- works with ORIGEX tokens, registered components, Vanilla JS and structured data files.

## 8. Dependency Boundary

Core dependency families for V1:

1. Bootstrap 5.3.8 — layout/responsive infrastructure.
2. Lucide — selected local semantic SVG icons, exact asset snapshot verified during M1.
3. Approved fonts — delivery only after redistribution/licensing verification.

No duplicate UI/icon framework is added for convenience.

## 9. Performance Rule

- Use production/minified vendor assets in the final package.
- Load only required ORIGEX scripts.
- Keep custom JS modular and page-aware.
- Lazy-load below-fold media.
- No jQuery compatibility layer.
- No third-party runtime is required for core content meaning.
- Avoid shipping unused full icon libraries or unnecessary vendor modules.

## 10. Change Control

This technology decision is locked for ORIGEX V1. A primary framework/version-family change requires an explicit Architecture Change Request because it affects pages, components, documentation and QA.

Patch-level security/defect updates inside the Bootstrap 5.3 line must still be deliberately reviewed and recorded rather than silently replaced.

Copyright © ORVEAX.
