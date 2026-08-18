# ORX-P01 — Gate 03 Design System Foundation

**Status:** ACTIVE  
**Started:** 2026-08-19  
**Product:** ORIGEX  
**Owner:** ORVEAX

## Locked Inputs

- Arabic-first presentation
- English secondary language
- Arabic font: Tajawal
- English font: Manrope
- ORIGEX core palette
- Origin Route Mark
- Premium Trade / Origin / Market Access visual personality

## Foundation Files

- `assets/css/tokens.css`
- `assets/css/base.css`
- `assets/css/components.css`
- `assets/css/rtl.css`

## Preview QA Infrastructure

- `preview/device-frame.html`
- `preview/_frame/preview-frame.css`
- `preview/_frame/preview-frame.js`
- `docs/PREVIEW-POLICY.md`

The preview frame is **not production UI**. It exists only during build/review and must be excluded from the final product package.

## Required Preview Behavior

- Arabic opens by default.
- English is always available.
- Grid mode shows the common device matrix.
- Focus mode renders a selected viewport at exact dimensions.
- Raw Preview opens the current page without review chrome.

## Common Viewports

Primary matrix:

- 360 × 800
- 390 × 844
- 412 × 915
- 768 × 1024
- 1024 × 1366
- 1366 × 768
- 1440 × 900
- 1920 × 1080

## Gate 03 Remaining Work

- [x] color tokens
- [x] font-family tokens
- [x] typography hierarchy tokens
- [x] Arabic-first direction baseline
- [x] common responsive preview frame
- [x] bilingual preview controls
- [ ] global layout primitives final QA
- [ ] header/navigation component system
- [ ] footer component system
- [ ] form primitives
- [ ] table/data primitives
- [ ] shared icon integration rules
- [ ] first-page implementation proof

## Exit Rule

Gate 03 closes only after the shared system can support the first complete production page without page-specific architecture hacks.
