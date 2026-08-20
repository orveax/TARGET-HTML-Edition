# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M5 FINAL ACCEPTANCE OPEN / M6 IN PROGRESS  
Last Alignment: 2026-08-20 — PG26–PG31 PS7 CI QA PASS / PG32 COMPONENTS NEXT

## Project Brief
Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers, structured as reusable ORVEAX commercial IP for ThemeForest and independent distribution.

## Page Stage Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

No page enters implementation before PS6. PS8 requires applicable page QA plus deployed Cloudflare browser acceptance. Cloudflare review is a parallel final-acceptance gate and does not block continued PS6/PS7 production.

## M0 — Product Foundation Freeze — PASS / CLOSED
Scope, architecture, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED
Bootstrap 5.3.8 local foundation, Tajawal/Manrope, tokens, components, icon sprite, patterns, RTL/LTR, config runtime and global shell are implemented. F05 Icon Integrity covers **64 AR/EN pages with zero missing sprite references** after PG31.

## M2 — Global Shell & Home Family — FINAL ACCEPTANCE OPEN
- PG01 Home 01 — **PS8 / PASS / CLOSED**.
- PG02 Home 02 — **PS7 / CI QA PASS**.
- PG03 Home 03 — **PS7 / CI QA PASS**.
- PG04 Landing — **PS7 / CI QA PASS**.
Open gate: PG02–PG04 deployed Cloudflare acceptance.

## M3 — Company / Business / Market — FINAL ACCEPTANCE OPEN
- PG05 About — **PS7 / CI QA PASS**.
- PG06 How We Work — **PS7 / CI QA PASS**.
- PG07 Capabilities — **PS7 / CI QA PASS**.
- PG08 Service Details — **PS7 / CI QA PASS**.
- PG14 Market Access — **PS7 / CI QA PASS**.
- PG15 Markets / Countries — **PS7 / CI QA PASS**.
- PG33 Company Profile — **PS7 IMPLEMENTED / QA FOLLOW-UP OPEN**.
Open gate: PG33 follow-up plus Cloudflare batch acceptance.

## M4 — Product / Supplier / Conversion — PAGE PRODUCTION CODE/CI COMPLETE
PG09–PG13 and PG16–PG19 are **PS7 / CI QA PASS**. Canonical product/supplier/market relations and conversion flows are implemented. Cloudflare PS8 batch acceptance remains open before milestone closure.

## M5 — Proof / Resources / Compliance / Content — PAGE PRODUCTION CODE/CI COMPLETE
PG20–PG25 are **PS7 / CI QA PASS**. M5 remains open only for applicable PS8/deployed-browser acceptance plus any verified Critical/High closure defects.

## M6 — Support / Utility / Components — IN PROGRESS
- PG26 FAQ — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG27 Contact — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG28 404 — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG29 Coming Soon — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG30 Privacy — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG31 Terms — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG32 Components / Elements Library — **NEXT VALID PAGE PRODUCTION ACTION**.

### PG26 Evidence
- Final source/content/SEO/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `26a2a72870b3506f098a3dd95e38c56756575e10`.
- QA report: `docs/PG26-QA-REPORT-V1.md`.

### PG27 Evidence
- Four canonical contact routes with config-driven contact data and validation-only Demo form.
- Final source/config/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Route/query-language/invalid-topic/form interactions: PASS.
- Final evidence: `7cfffde78233c087ee2381247470bb024d3689e1`.
- QA report: `docs/PG27-QA-REPORT-V1.md`.

### PG28 Evidence
- Branded 404 recovery layout in Arabic and English.
- `robots=noindex,follow`; six approved local recovery routes.
- Final source/SEO/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `de86b1392f523f26dffa2d53c28145653f2f0402`.
- QA report: `docs/PG28-QA-REPORT-V1.md`.

### PG29 Evidence
- Buyer-configured `launchDate` defaults empty; no fabricated date or countdown.
- Demo subscribe and social-config behavior PASS with zero network/storage behavior.
- Final source/config/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `cf91343ff95c66ba544387e26506c60076610f74`.
- QA report: `docs/PG29-QA-REPORT-V1.md`.

### PG30 Evidence
- Exact Arabic canonical Intro + English meaning parity: PASS.
- Eight canonical Privacy sections and eight TOC anchors: PASS.
- Shared `assets/css/origex-legal.css` established.
- `robots=noindex,follow`; no fabricated review/effective date, named-law compliance or fake Cookie/Consent UI.
- Final source/legal/SEO failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `13dab1fe2c8711687b38e87eec5032ff3f038b8c`.
- QA report: `docs/PG30-QA-REPORT-V1.md`.

### PG31 Evidence
- Exact Arabic canonical Terms Intro + English Demo boundary: PASS.
- Eight canonical Terms sections / eight TOC anchors / numbered long-form structure: PASS.
- Shared contextual legal navigation Privacy / Terms: PASS.
- Shared legal shell normalized to the **STD-DIM01 48px Control M** tier for legal TOC/context controls.
- Semantic 4-row customization matrix follows **STD-DATA01**, preserving table relationships with internal horizontal scrolling on narrow screens.
- No fabricated effective date, liability cap, warranty exclusion, governing jurisdiction, venue or arbitration forum.
- `robots=noindex,follow`; no legal structured-data claim; no PG31-specific JavaScript.
- Final source/legal/standards failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- TOC / context navigation / language switch / table focus interactions: PASS.
- Final evidence: `d626862192626418ed806101dd60288d69456d09`.
- PS7 promotion: `db4d36867c9a00eecf079f4ac5089de7d59411c4`.
- QA report: `docs/PG31-QA-REPORT-V1.md`.
- Global F05: **64 AR/EN pages / 0 missing references**.

### Preview Utility
`site-map.html` remains a noindex internal Preview Utility outside the 33-layout product scope. Target approved state after PG31 is **33 cards / 32 implemented / 1 pending / 64 AR+EN page links**. PG32 Components / Elements is NEXT. `.github/scripts/sync_preview_site_map.py` synchronizes approved PS7 preview state before Preview QA.

M6 page-production gate after PG32: all seven support/utility layouts implemented in AR/EN and page-level CI gates pass. Final milestone closure still additionally requires applicable PS8 acceptance, utility/legal/demo boundaries, post-PG32 systemic backfit/regression and zero Critical/High defects.

## M7 — Full QA & Optimization — NOT STARTED
Full AR/EN parity, claim/disclaimer, data, SEO, broken-link, responsive, accessibility, performance, cross-browser and leakage QA. Gate: zero Critical / High defects.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED
Buyer documentation, customization/deployment guides, licenses/credits, changelog, preview/listing material, final ZIP and ThemeForest submission checklist. Gate: Submission Candidate 1.0.0.

## Current Production Order
1. **M6 / PG32 — Components / Elements Library**: build as the **Design System QA Laboratory + Buyer Component Reference**, consuming frozen standards from first implementation.
2. After PG32: execute the approved systemic backfit order → global AR/EN regression → sequential PG01→PG33 second-pass review.
3. In parallel, close applicable Cloudflare PS8 batches and PG33 QA follow-up.

## Change Control
New page or Main Feature family requires Scope Change or V1.1+. QA/accessibility/performance/responsive/RTL fixes may be corrected centrally without reopening scope.

## CR-001 Scope Addendum
PG33 Company Profile expanded active V1 to **33 unique layouts / approximately 66 AR+EN HTML pages**.

Copyright © ORVEAX.
