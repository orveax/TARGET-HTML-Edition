# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M4 FINAL ACCEPTANCE OPEN / M5 IN PROGRESS  
Last Alignment: 2026-08-20 — PG20–PG24 PS7 / PG25 NEXT

## Project Brief
Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers, structured as reusable ORVEAX commercial IP for ThemeForest and independent distribution.

## Page Stage Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

No page enters implementation before PS6. PS8 requires applicable page QA plus deployed Cloudflare browser acceptance. Cloudflare review is a parallel final-acceptance gate and does not block continued PS6/PS7 production.

## M0 — Product Foundation Freeze — PASS / CLOSED
Scope, architecture, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED
Bootstrap 5.3.8 local foundation, Tajawal/Manrope, tokens, components, icon sprite, patterns, RTL/LTR, config runtime and global shell are implemented. F05 Icon Integrity now covers **50 AR/EN pages with zero missing sprite references** at PG24 closure.

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

## M5 — Proof / Resources / Compliance / Content — IN PROGRESS
- PG20 Case Studies — **PS7 / CI QA PASS**.
- PG21 Case Study Details — **PS7 / CI QA PASS**.
- PG22 Downloads / Resources — **PS7 / CI QA PASS**.
- PG23 Certifications & Compliance — **PS7 / CI QA PASS**.
- PG24 Insights / Blog — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG25 Article Details — **NEXT VALID PAGE PRODUCTION ACTION**.

### PG24 Evidence
- 9 fictional Demo editorial records: 1 featured + 8 grid.
- No CMS/API and no new `articles.json` domain.
- Search + category filter + 6-per-page pagination + `category/q/page` query state + AR/EN preservation implemented with Vanilla JS.
- First QA found only a shared Global Footer V1 drift in EN; corrected centrally by `1aca18259ab8ae9e28e4834636fed9308741b7a4`.
- Final source/editorial/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Search / category / pagination / language-preservation / empty-state interactions: PASS.
- Final evidence: `9fd0853544bd36d46f9ad34dd3239152a7f4646f`.
- QA report: `docs/PG24-QA-REPORT-V1.md`.

### Preview Utility
`site-map.html` remains a noindex internal Preview Utility outside the 33-layout product scope. After PG24 it contains **33 cards / 25 implemented / 8 pending / 50 AR+EN page links**; pending pages intentionally have no broken links.

M5 exit still requires PG25, applicable PS8 acceptance, SEO/editorial/demo controls and zero Critical/High defects.

## M6 — Support / Utility — NOT STARTED
PG26 FAQ, PG27 Contact, PG28 404, PG29 Coming Soon, PG30 Privacy, PG31 Terms and PG32 Components remain pending.

## M7 — Full QA & Optimization — NOT STARTED
Full AR/EN parity, claim/disclaimer, data, SEO, broken-link, responsive, accessibility, performance, cross-browser and leakage QA. Gate: zero Critical / High defects.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED
Buyer documentation, customization/deployment guides, licenses/credits, changelog, preview/listing material, final ZIP and ThemeForest submission checklist. Gate: Submission Candidate 1.0.0.

## Current Production Order
1. **PG25 — Article Details**: canonical content → PS6 Page Design Profile / SEO/editorial-detail contract → AR/EN build → ID/metadata/typography/share/related/responsive QA.
2. Continue M6 sequentially after M5 page production.
3. In parallel, close Cloudflare PS8 batches and PG33 QA follow-up.

## Change Control
New page or Main Feature family requires Scope Change or V1.1+. QA/accessibility/performance/responsive/RTL fixes may be corrected centrally without reopening scope.

## CR-001 Scope Addendum
PG33 Company Profile expanded active V1 to **33 unique layouts / approximately 66 AR+EN HTML pages**.

Copyright © ORVEAX.
