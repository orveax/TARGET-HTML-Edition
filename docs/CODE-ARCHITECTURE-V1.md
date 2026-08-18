# ORIGEX — Code Architecture & Naming V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & FROZEN  
Approval Date: 2026-08-19

## 1. Naming Prefix

ORIGEX-owned public CSS classes and custom properties use `orx-` / `--orx-` prefixes.

Examples:
- `.orx-product-card`
- `.orx-product-card__media`
- `.orx-product-card--featured`
- `--orx-primary`
- `--orx-space-md`

Bootstrap classes remain Bootstrap classes and are not renamed.

## 2. Component Naming

Use a BEM-like contract:
- Block: `.orx-component`
- Element: `.orx-component__part`
- Modifier: `.orx-component--variant`
- State: semantic class or ARIA/data state, e.g. `.is-active` only when documented centrally.

Pages may position components but may not redefine their core anatomy through page-local CSS.

## 3. JavaScript Hooks

Use `data-orx-*` for behavior hooks.

Examples:
- `data-orx-drawer`
- `data-orx-filter`
- `data-orx-accordion`
- `data-orx-config`

Rules:
- Styling must not rely solely on JS hook attributes.
- ARIA attributes are the source of truth for accessibility states where applicable.
- Event initialization must be idempotent where practical.

## 4. File Naming

Use lowercase kebab-case.

Examples:
- `product-details.html`
- `product-card.css`
- `navigation.js`
- `products.json`

No spaces, mixed case, or inconsistent separators in distributed files.

## 5. CSS Layering

Preferred architecture:
1. Bootstrap foundation.
2. ORIGEX tokens.
3. base/reset adjustments.
4. layout/grid helpers.
5. primitives.
6. components.
7. patterns/sections.
8. page profiles where genuinely required.
9. RTL helpers.
10. responsive refinements.

Page-profile CSS cannot become a repository for component hotfixes.

## 6. CSS Rules

- Use CSS logical properties for directional spacing/layout when practical.
- No arbitrary colors, radii, shadows, typography sizes or motion values outside tokens.
- Avoid `!important`; permitted only for documented interoperability exceptions.
- Avoid high-specificity selectors and deep nesting.
- Repeated values graduate into tokens/components.

## 7. JavaScript Architecture

- Vanilla JS only for ORIGEX custom behavior.
- Feature modules initialize only where relevant.
- No jQuery.
- No global namespace pollution beyond an intentionally documented ORIGEX configuration object if required.
- Core content/navigation should degrade gracefully when optional JS is unavailable.

## 8. HTML Rules

- Semantic HTML first.
- Correct `lang` and `dir` on every page.
- One logical H1 per page template unless a specific semantic reason is documented.
- Buttons for actions; anchors for navigation.
- Forms use explicit labels.
- Repeated directional data on RTL pages uses bidi-safe helpers.

## 9. Comments

Comments explain non-obvious architecture/integration points, not obvious markup.

Recommended comment types:
- component boundary.
- integration hook.
- buyer customization note where documentation benefits.
- licensing/preview placeholder note.

Do not flood production HTML with tutorial comments.

## 10. Hotfix Policy

Prohibited by default:
- `fix2.css`, `final-fix.css`, `new.css`, `temp.js` patterns.
- duplicate page-specific versions of shared components.
- inline style patches for structural design issues.

A temporary fix must be resolved into the correct foundation/component layer before page closure.

## 11. Governance

Naming and architecture changes require a documented Architecture Change Request. Normal page implementation conforms to this document.

Copyright © ORVEAX.