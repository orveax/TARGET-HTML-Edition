# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M5 FINAL ACCEPTANCE OPEN / M6 READY  
Last Alignment: 2026-08-20 — M5 PAGE PRODUCTION CODE/CI COMPLETE / PG20–PG25 PS7 / M6 PG26 NEXT

## Project Brief
Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers, structured as reusable ORVEAX commercial IP for ThemeForest and independent distribution.

## Page Stage Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

No page enters implementation before PS6. PS8 requires applicable page QA plus deployed Cloudflare browser acceptance. Cloudflare review is a parallel final-acceptance gate and does not block continued PS6/PS7 production.

## M0 — Product Foundation Freeze — PASS / CLOSED
Scope, architecture, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED
Bootstrap 5.3.8 local foundation, Tajawal/Manrope, tokens, components, icon sprite, patterns, RTL/LTR, config runtime and global shell are implemented. F05 Icon Integrity covers **52 AR/EN pages with zero missing sprite references** at PG25 closure.

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
- PG20 Case Studies — **PS7 / CI QA PASS**.
- PG21 Case Study Details — **PS7 / CI QA PASS**.
- PG22 Downloads / Resources — **PS7 / CI QA PASS**.
- PG23 Certifications & Compliance — **PS7 / CI QA PASS**.
- PG24 Insights / Blog — **PS7 / CI QA PASS**.
- PG25 Article Details — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.

### PG25 Evidence
- Default canonical Demo article 001 remains readable as semantic HTML without JavaScript.
- Stable PG24 article IDs `article-001..009` are supported; 002–009 remain page-local Demo `<template>` records, not a new data-schema domain.
- Missing ID defaults to article 001; invalid ID shows a visible notice before article-001 fallback.
- Desktop/mobile language links preserve valid article state.
- Previous/next navigation, three related articles excluding current, Copy Link, Email, LinkedIn and WhatsApp share actions implemented.
- No CMS/API, fetch/XHR, storage or analytics dependency.
- Initial QA found only Global Navigation V1 drift; corrected centrally by `83275a173a12066af58654c2fda82b42e281d2fa`.
- Final source/editorial/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Default / invalid-ID / state-share / last-article interaction groups: PASS in AR and EN.
- Final evidence: `d6f9f74b4ef9352ab631fdd8f372d1963bb6852a`.
- QA report: `docs/PG25-QA-REPORT-V1.md`.

### Preview Utility
`site-map.html` remains a noindex internal Preview Utility outside the 33-layout product scope. After PG25 it contains **33 cards / 26 implemented / 7 pending / 52 AR+EN page links**. PG26 is the next pending page; query/hash portions are ignored by the target-existence QA so valid detail preview links do not create false broken-file defects.

M5 page production is complete. M5 remains open only for applicable PS8/deployed-browser acceptance plus any verified Critical/High closure defects.

## M6 — Support / Utility — READY / NEXT PRODUCTION MILESTONE
- PG26 FAQ — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG27 Contact — NOT STARTED.
- PG28 404 — NOT STARTED.
- PG29 Coming Soon — NOT STARTED.
- PG30 Privacy — NOT STARTED.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

M6 gate: all seven support/utility layouts implemented in AR/EN, applicable PS8 acceptance complete, utility/legal/demo boundaries verified, and zero Critical/High defects.

## M7 — Full QA & Optimization — NOT STARTED
Full AR/EN parity, claim/disclaimer, data, SEO, broken-link, responsive, accessibility, performance, cross-browser and leakage QA. Gate: zero Critical / High defects.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED
Buyer documentation, customization/deployment guides, licenses/credits, changelog, preview/listing material, final ZIP and ThemeForest submission checklist. Gate: Submission Candidate 1.0.0.

## Current Production Order
1. **M6 / PG26 — FAQ**: canonical content → PS6 Page Design Profile / SEO + FAQ contract → AR/EN build → category navigation/search/accordion/supplier-buyer/contact/responsive/accessibility QA.
2. Continue PG27–PG32 sequentially under M6.
3. In parallel, close applicable Cloudflare PS8 batches and PG33 QA follow-up.

## Change Control
New page or Main Feature family requires Scope Change or V1.1+. QA/accessibility/performance/responsive/RTL fixes may be corrected centrally without reopening scope.

## CR-001 Scope Addendum
PG33 Company Profile expanded active V1 to **33 unique layouts / approximately 66 AR+EN HTML pages**.

Copyright © ORVEAX.
