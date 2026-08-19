# ORIGEX — M1 Global System & Component Foundation QA Report

Product ID: ORX-P01  
Milestone: M1  
Date: 2026-08-19  
Result: **PASS / CLOSED**  
Critical defects: 0  
High defects: 0

## Scope

This report closes the reusable system foundation required before PG01–PG32 page production. It validates repository structure, frozen-system conformity, local dependency delivery, registered component coverage, AR/EN source contracts, RTL/LTR logic, accessibility foundations, reduced-motion behavior, config integration and license traceability.

It does not replace M2 page-level visual QA or the M7 full responsive/browser matrix.

## Gate Results

| Gate | Result | Evidence |
|---|---|---|
| Bootstrap 5.3.8 exact local baseline | PASS | `assets/vendor/bootstrap/` + local MIT license |
| Arabic / English local typography assets | PASS | Tajawal + Manrope under `assets/fonts/`, OFL notices included |
| Design tokens | PASS | `assets/css/origex-tokens.css` |
| Typography / spacing / container foundation | PASS | `assets/css/origex-foundation.css` |
| Grid / responsive helpers | PASS | frozen container/gutter rules implemented |
| Radius / border / elevation | PASS | tokenized foundation |
| Motion + reduced motion | PASS | global tokens + `prefers-reduced-motion` fallbacks |
| Lucide local subset | PASS | `assets/icons/lucide/` + generated `assets/icons/sprite.svg` + combined license |
| PT01–PT06 | PASS | all six ORVEAX-owned SVG patterns implemented |
| P01–P11 | PASS | mapped in `M1-COMPONENT-IMPLEMENTATION-MAP.md` |
| C01–C28 | PASS | mapped to central component classes/runtime; no page-local fork |
| S01–S06 | PASS | section/hero/final-CTA foundations mapped |
| N01–N04 | PASS | header, mega menu, drawer and footer foundation |
| Config schema / engine | PASS | canonical demo defaults aligned; semantic enhancement only |
| Global shell | PASS | announcement/header/nav/drawer/footer/floating utilities foundation |
| AR component QA surface | PASS — SOURCE/STRUCTURE | `preview/m1-components-ar.html`, `lang=ar`, `dir=rtl`, noindex |
| EN component QA surface | PASS — SOURCE/STRUCTURE | `preview/m1-components-en.html`, `lang=en`, `dir=ltr`, noindex |
| Core runtime CDN dependency | PASS | runtime references local vendor/font/icon/CSS/JS paths; repository scan found no CDN runtime references |
| Demo disclosure / client leakage | PASS | canonical fictional disclosure used; no `targetft` leakage found in active repository search |
| Asset / license register | PASS | `ASSET-LICENSE-REGISTER-V1.md` updated to verified M1 baseline |
| Vendor integrity | PASS | `M1-VENDOR-SHA256.txt`; vendor commit `9fd274d0ca5ce0fd7760285e103f2f779ef6f334` |

## Accessibility / Interaction Baseline

Implemented at M1:
- skip-to-content link;
- visible `:focus-visible` baseline;
- semantic header/nav/main/section/footer patterns in QA surfaces;
- keyboard tabs with RTL/LTR directional handling;
- accordion `aria-expanded` / `aria-controls` contract;
- mega-menu and mobile-drawer Escape handling;
- mobile drawer focus transfer and restoration;
- reduced-motion fallback;
- form labels/status patterns;
- bidi-safe helper for email/phone/SKU/unit use.

## RTL / LTR Closure

- Arabic QA surface uses `lang="ar" dir="rtl"` and Bootstrap RTL CSS.
- English QA surface uses `lang="en" dir="ltr"` and Bootstrap LTR CSS.
- directional action icons have left/right variants in the local sprite.
- drawer direction is reading-start aware: LTR enters from left; RTL enters from right.
- logical CSS properties are used for inline positioning where practical.

## Registry Reconciliation

The frozen M1 milestone text mentions modal behavior, while C01–C28 contains no ORIGEX modal component ID. M1 does not invent a new ID. The local Bootstrap bundle supplies an approved behavior primitive if a later page contract requires a modal; a reusable ORIGEX modal family requires change control before entering the registry.

This interpretation preserves the frozen component architecture and prevents a page-local component fork.

## QA Surfaces and Browser Matrix

The two QA surfaces provide the canonical M1 review surface. This closure is based on repository/source/component-contract verification available in the implementation environment.

Full live visual observation across the frozen width/browser matrix remains part of normal page QA from M2 onward and the complete M7 gate. A visual defect found later may trigger a foundation fix under QA/change-control rules without reopening M0 scope.

## Exit Decision

M1 exit criteria are satisfied for page production:
- one reusable foundation exists;
- required local dependencies and licenses are present;
- registered components and navigation families have central implementations;
- Arabic/English QA surfaces exist;
- no core CDN is required;
- config/runtime boundaries are normalized;
- asset/license traceability is established;
- no Critical or High structural blocker remains.

**Decision: M1 CLOSED. M2 / PG01 may start.**

Copyright © ORVEAX.
