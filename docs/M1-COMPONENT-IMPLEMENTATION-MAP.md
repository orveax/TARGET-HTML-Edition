# ORIGEX — M1 Component Implementation Map

Product ID: ORX-P01  
Milestone: M1 — Global System & Component Foundation  
Status: IMPLEMENTED — QA EVIDENCE MAP  
Date: 2026-08-19

Authority: `DESIGN-SYSTEM-HIERARCHY-V1.md`, `COMPONENT-REGISTRY-V1.md`, `COMPONENT-DESIGN-RULES-V1.md`, `FOUNDATION-FREEZE-V1.md`.

This file maps the frozen registry to the active M1 implementation. It does not introduce new component IDs.

## Foundations F01–F07

| ID | Implementation |
|---|---|
| F01 Color | `assets/css/origex-tokens.css` |
| F02 Typography | `origex-tokens.css` + `origex-foundation.css`; Tajawal / Manrope local assets |
| F03 Spacing | `--orx-space-*`, container/gutter/section rhythm |
| F04 Shape | radius/border/elevation tokens + surface helpers |
| F05 Icons | local Lucide subset + `assets/icons/sprite.svg` + `.orx-icon*` |
| F06 Motion | fast/standard/slow tokens + reduced-motion rules |
| F07 Media | `.orx-media*`, product/logo/editorial media families + PT01–PT06 |

## Primitives P01–P11

| ID | Implementation |
|---|---|
| P01 Primary Button | `.orx-btn.orx-btn--primary` |
| P02 Secondary Button | `.orx-btn.orx-btn--secondary` |
| P03 Text Action | `.orx-text-action` |
| P04 Icon Button | `.orx-icon-btn` |
| P05 Badge / Status | `.orx-badge` + status variants |
| P06 Input | `.orx-input` |
| P07 Select | `.orx-select` |
| P08 Textarea | `.orx-textarea` |
| P09 Checkbox / Radio | `.orx-check` |
| P10 Divider | `.orx-divider` |
| P11 Icon Container | `.orx-icon-box` + size variants |

## Components C01–C28

| ID | Implementation |
|---|---|
| C01 Feature Card | `.orx-card.orx-feature-card` |
| C02 Product Card | `.orx-card.orx-product-card` |
| C03 Supplier / Brand Card | `.orx-card.orx-supplier-card` |
| C04 Market Card | `.orx-card.orx-market-card` |
| C05 Process Card | `.orx-card.orx-process-card` |
| C06 Metric Card | `.orx-card.orx-metric-card` |
| C07 Certification Card | `.orx-card.orx-certification-card` |
| C08 Resource / Download Card | `.orx-card.orx-resource-card` |
| C09 Case Study Card | `.orx-card.orx-case-study-card` |
| C10 Contact Card | `.orx-card.orx-contact-card` |
| C11 CTA Card | `.orx-card.orx-cta-card` |
| C12 Breadcrumb | `.orx-breadcrumb` |
| C13 Tabs | `.orx-tabs*` + `origex-ui.js` keyboard behavior |
| C14 Accordion | `.orx-accordion*` + `origex-ui.js` |
| C15 Pagination | `.orx-pagination` |
| C16 Search | `.orx-search` + P06 |
| C17 Filter Group | `.orx-filter-group`, `.orx-filter-chip` + runtime event |
| C18 Specification Table | `.orx-spec` |
| C19 Stat Strip | `.orx-stat-strip` |
| C20 Trust Item | `.orx-trust-item` |
| C21 Empty State | `.orx-empty-state` |
| C22 Alert / Notice | `.orx-alert` + semantic variants |
| C23 Form Field | `.orx-field` + P06–P09 |
| C24 File Upload | `.orx-upload` + filename runtime |
| C25 Form Status | `.orx-form-status` + success/error variants |
| C26 Product Media | `.orx-product-media` / `.orx-media--product` |
| C27 Logo Frame | `.orx-logo-frame` |
| C28 Editorial Media | `.orx-editorial-media` / `.orx-media--editorial` |

## Sections S01–S06

| ID | Implementation |
|---|---|
| S01 Section Header | `.orx-section-header` + centered modifier |
| S02 Split Hero | `.orx-hero` + `.orx-hero__grid` + content/media children |
| S03 Centered Hero | `.orx-hero` composed with centered header/content/actions rules; no separate component fork |
| S04 Detail Hero | `.orx-detail-hero` |
| S05 Utility Hero | `.orx-utility-hero` |
| S06 Final CTA | `.orx-final-cta` + `.orx-final-cta__inner` |

## Navigation N01–N04

| ID | Implementation |
|---|---|
| N01 Header | `.orx-site-header*` |
| N02 Mega Menu | `.orx-mega-menu*` + `data-orx-mega-trigger` runtime |
| N03 Mobile Drawer | `.orx-mobile-drawer*` + focus/Escape/open-close runtime |
| N04 Footer | `.orx-site-footer*`, business-hours/social/config hooks |

## Bootstrap Interaction Baseline

Bootstrap 5.3.8 is packaged locally and remains infrastructure, not ORIGEX identity. The local bundle is available for approved Bootstrap behavior primitives when a page contract requires them.

The milestone plan mentions modal behavior. No ORIGEX modal ID exists in the frozen C01–C28 registry and no V1 Main Feature currently requires a custom modal component. Therefore M1 does **not** invent a new component ID or page-local modal fork. If a future V1 page contract proves a modal is required, use the approved local Bootstrap behavior with ORIGEX primitives or open formal change control if a reusable ORIGEX modal family becomes necessary.

## Config / Runtime

- `assets/js/config.js` contains eligible repeated/site-level values only.
- `assets/js/config-engine.js` enhances existing semantic HTML and does not construct core UI.
- `assets/js/origex-ui.js` handles ORIGEX navigation/disclosure/filter/upload interactions.
- Demo defaults align with `DEMO-CONTENT-DATASET-V1.md`.

## M1 QA Surfaces

- `preview/m1-components-ar.html` — Arabic RTL.
- `preview/m1-components-en.html` — English LTR.

The QA surfaces are `noindex,nofollow`, use the canonical fictional demo disclosure, and are not final PG32 or marketplace pages.

## Non-Negotiable Rule

Pages consume this system. Pages do not create replacement card, hero, navigation, spacing, icon, form or motion systems locally.

Copyright © ORVEAX.
