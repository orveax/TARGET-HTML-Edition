# ORX-P01 — Global Shell V1

**Product:** ORIGEX  
**Owner:** ORVEAX  
**Status:** IMPLEMENTED — BUILD STAGE 04  
**Primary language:** Arabic / RTL  
**Secondary language:** English / LTR

## Scope Implemented

- sticky premium header
- ORIGEX light logo treatment
- desktop navigation rail
- accessible mega menu
- Arabic-first language hierarchy
- static Arabic and English page trees
- mobile/tablet navigation drawer
- commercial CTA hierarchy
- multi-route premium footer
- demo-safe contact placeholders using `example.com`
- keyboard Escape handling and outside-click close behavior
- reduced-motion compatibility through the shared design system
- internal multi-device preview frame now targets `/ar/` and `/en/` pages

## Architecture

```text
ar/
  index.html
en/
  index.html
assets/
  brand/
    origex-logo-light.svg
  css/
    tokens.css
    base.css
    components.css
    rtl.css
    shell.css
  js/
    navigation.js
preview/
  device-frame.html
  _frame/
```

## Fidelity Principle

The shell preserves the reusable interaction and information architecture learned from the mature TARGET implementation — premium navigation, mega menu, mobile drawer, route hierarchy and structured footer — while rebuilding it as clean static HTML/CSS/Vanilla JS under the independent ORIGEX identity.

No TARGET company data, client contacts, client logos, supplier information or proprietary client claims are included.

## Language Rule

Arabic is the canonical default review experience. English is always implemented in the same milestone and may not lag behind the Arabic shell.

## Preview Rule

The responsive preview frame remains an internal development/QA utility under `preview/`. It is not part of the customer-facing production experience and must be removed/excluded from the final marketplace production package.

## Current Build Boundary

The content canvas inside `ar/index.html` and `en/index.html` is intentionally temporary. It exists only to verify the global shell and will be replaced by the full Home 01 fidelity build in the next stage.

Future route links already use the planned page filenames. Routes not yet built are expected to remain pending until their page milestone is implemented.

## Next Stage

**Stage 05 — Home 01: TARGET-derived Fidelity Baseline under ORIGEX identity.**
