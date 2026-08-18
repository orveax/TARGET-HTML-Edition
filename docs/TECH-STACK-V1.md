# ORIGEX — V1 Technology Stack

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED

## 1. Approved V1 Stack

ORIGEX V1 uses:

- HTML5.
- CSS3.
- Bootstrap 5.x as the responsive/layout foundation.
- Vanilla JavaScript for product-specific interactions.
- ORIGEX Design System for all branded visual components.
- `config.js` for simple global customization.
- JSON data files where structured product/supplier/market data is useful.

## 2. Bootstrap Role

Bootstrap is infrastructure, not the visual identity.

Approved Bootstrap usage:
- Grid.
- Containers.
- Responsive breakpoints.
- Flex/display/spacing utilities where they reduce unnecessary custom CSS.
- Selected accessibility-tested interaction primitives when they provide clear value.

ORIGEX does not use Bootstrap's default visual language as the product design system.

The following remain ORIGEX-owned components:
- Buttons.
- Cards.
- Forms.
- Product cards.
- Supplier cards.
- Market cards.
- Headers and navigation composition.
- Section families.
- Hero families.
- CTAs.
- Colors.
- Typography.
- Motion language.

## 3. Architecture Order

Bootstrap Foundation
→ ORIGEX Tokens
→ ORIGEX Primitives
→ ORIGEX Components
→ ORIGEX Patterns
→ Sections
→ Page Design Profiles

A page must never override an approved ORIGEX component simply because Bootstrap provides an alternative default component.

## 4. JavaScript Rule

Use Vanilla JavaScript for ORIGEX-specific behavior.

Typical use cases:
- navigation behavior.
- tabs and accordions.
- filters/search/sorting.
- form validation.
- config engine.
- announcement bar.
- WhatsApp/back-to-top controls.
- lightweight modal/off-canvas behavior where needed.

Bootstrap JavaScript may be used selectively for stable primitives, but no ORIGEX page may depend on a large third-party JavaScript framework.

## 5. Explicit V1 Exclusions

- No React.
- No Vue.
- No Astro runtime in the customer package.
- No Tailwind.
- No jQuery.
- No mandatory Node/build process.
- No heavy animation framework as a core dependency.

The buyer must be able to edit files and run the template as a conventional static HTML package.

## 6. Buyer Experience

Beginner:
- edits `config.js`.
- follows Quick Start documentation.

Intermediate buyer:
- edits HTML and Bootstrap layout classes.

Developer:
- works with ORIGEX tokens, registered components, Vanilla JS and structured data files.

## 7. Performance Rule

Bootstrap must not become an excuse for dependency bloat.

- Use production/minified assets in the final package.
- Load only required project scripts.
- Keep custom JavaScript modular.
- Lazy-load below-fold media.
- No jQuery compatibility layer.
- No third-party script is required to render the core content.

## 8. Change Control

This technology decision is locked for ORIGEX V1. Changing the primary framework/foundation requires an explicit architecture change record because it affects every page, component, documentation example and QA path.

Copyright © ORVEAX.
