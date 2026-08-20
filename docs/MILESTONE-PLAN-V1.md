# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M6 FINAL ACCEPTANCE OPEN / **M7 READY — ENTRY GATE PASS**  
Last Alignment: 2026-08-20 — **33 AR + 33 EN / M6 PAGE PRODUCTION COMPLETE / SYSTEMIC P0 PASS / GLOBAL AR-EN REGRESSION PASS / M7 READY**

## Project Brief
Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers, structured as reusable ORVEAX commercial IP for ThemeForest and independent distribution.

## Page Stage Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

No page enters implementation before PS6. PS8 requires applicable page QA plus deployed Cloudflare browser acceptance. Cloudflare review remains a parallel final-acceptance gate.

## Canonical Product Scope
- CR-001 active V1 scope: **33 unique layouts**.
- Language production: **33 Arabic + 33 English = 66 HTML pages**.
- Filename parity: PASS.
- Preview Utility: **33 implemented / 0 pending / 66 links / failures 0**.
- F05 Icon Integrity: **66 pages / 0 missing references**.

## M0 — Product Foundation Freeze — PASS / CLOSED
Scope, architecture, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED
Bootstrap 5.3.8 local foundation, Tajawal/Manrope, tokens, components, icon sprite, patterns, RTL/LTR, config runtime and global shell are implemented and centrally owned.

## M2 — Global Shell & Home Family — FINAL ACCEPTANCE OPEN
- PG01 Home 01 — **PS8 / PASS / CLOSED**.
- PG02 Home 02 — **PS7 / CI QA PASS**.
- PG03 Home 03 — **PS7 / CI QA PASS**.
- PG04 Landing — **PS7 / CI QA PASS**.

Open gate: deployed Cloudflare acceptance for PG02–PG04.

## M3 — Company / Business / Market — FINAL ACCEPTANCE OPEN
- PG05 About — PS7.
- PG06 How We Work — PS7.
- PG07 Capabilities — PS7.
- PG08 Service Details — PS7.
- PG14 Market Access — PS7.
- PG15 Markets / Countries — PS7.
- PG33 Company Profile — **PS7 / page-specific QA follow-up open**.

Open gate: PG33 follow-up plus applicable Cloudflare PS8 batch acceptance.

## M4 — Product / Supplier / Conversion — PAGE PRODUCTION CODE/CI COMPLETE
PG09–PG13 and PG16–PG19 are PS7 / CI QA PASS. Canonical product/supplier/market relations and conversion flows are implemented. Cloudflare PS8 batch acceptance remains open.

## M5 — Proof / Resources / Compliance / Content — PAGE PRODUCTION CODE/CI COMPLETE
PG20–PG25 are PS7 / CI QA PASS. Cloudflare PS8 acceptance remains open where applicable.

## M6 — Support / Utility / Components — PAGE PRODUCTION CODE/CI COMPLETE
PG26 FAQ through PG32 Components / Elements are **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.

PG32 final page gate:
- canonical content / frozen Main Features PASS;
- 11/11 card families;
- 17/17 C12–C28 references;
- 11/11 primitives;
- 9/9 diagnostics;
- source / registry / diagnostic failures 0;
- rendered AR/EN × 390/820/1366/1536 = 8/8 PASS;
- zero final document overflow;
- navigation / disclosure / form / modal / language interactions PASS.

### M6 Remaining Closure Conditions
M6 page production is complete and its pre-M7 systemic/regression prerequisite is PASS. Final milestone acceptance remains open for:
- applicable deployed Cloudflare PS8 acceptance;
- PG28 real deployed HTTP-404 verification;
- PG30/PG31 production legal replacement/review before real publication;
- PG33 page-specific QA follow-up;
- zero unresolved Critical / High defects.

## Pre-M7 Systemic Reconciliation — PASS
The approved shared-system sequence was executed before M7:

`Token → Foundation → Component → Shell/Runtime → Global AR/EN Regression`

Results:
- SYS-01 semantic surface / foreground / contrast: PASS.
- SYS-02 STD-DIM01 dimension tiers: PASS.
- SYS-03 shared 48px touch targets: PASS.
- SYS-04 N03 drawer focus containment / Escape / focus return: PASS.
- PG32 after backfit: **9/9 diagnostic probes ALIGNED in Arabic and English**.
- Representative systemic browser gate: **16/16 PASS** with zero overflow.
- Global AR/EN regression: **33 Arabic + 33 English / filename parity true / 264 rendered cases / 0 failures**.
- Initial Pattern SVG path defect (`/assets/assets/patterns/...`) was corrected centrally and the full matrix reran to PASS.
- Final regression evidence commit: `0514f2a617cd2737533337a679fb1b5601dd267f`.
- Formal checkpoint: `docs/PRE-M7-FINAL-ALIGNMENT-2026-08-20.md`.

## M7 — Full QA & Optimization — READY / ENTRY GATE PASS / NOT STARTED
M7 begins only when explicitly started. Its execution sequence is the sequential **PG01→PG33 second-pass review** against VQ1 and the frozen Website Standards.

Required review dimensions:
- AR/EN parity and RTL/LTR quality;
- visual hierarchy, typography, spacing and responsive behavior;
- navigation and conversion UX;
- accessibility and keyboard/focus behavior;
- content/demo/claim boundaries;
- SEO and route integrity;
- performance, browser/runtime errors and overflow;
- cross-page consistency;
- asset/licensing integrity;
- zero unresolved Critical / High defects.

Rules:
- repeated defects must be fixed in the shared system, not page-by-page;
- page-local fixes are for verified page-specific defects only;
- shared-system changes require targeted regression before continuing;
- PS8 deployment acceptance continues in parallel and is not silently inferred from CI.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED
Buyer documentation, customization/deployment guides, licenses/credits, changelog, preview/listing material, final ZIP and ThemeForest submission checklist. Gate: Submission Candidate 1.0.0.

## Current Production Order
1. **Start M7** with PG01→PG33 sequential second-pass review.
2. Correct page-specific visual/UX/content/accessibility/performance defects; repeated gaps remain shared-system fixes.
3. Preserve AR/EN parity and rerun targeted regression after shared corrections.
4. In parallel, close applicable Cloudflare PS8 batches, PG28 HTTP-404 verification, PG30/PG31 production legal replacement/review and PG33 page-specific QA follow-up.
5. M7 exit: zero unresolved Critical / High defects and approved release-quality regression state.

## Change Control
New page or Main Feature family requires Scope Change or V1.1+. QA/accessibility/performance/responsive/RTL fixes may be corrected centrally without reopening scope.

## CR-001 Scope Addendum
PG33 Company Profile expanded active V1 to **33 unique layouts / 66 AR+EN HTML pages**.

Copyright © ORVEAX.
