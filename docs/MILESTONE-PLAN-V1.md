# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M5 FINAL ACCEPTANCE OPEN / M6 IN PROGRESS  
Last Alignment: 2026-08-20 — PG26–PG27 PS7 CI QA PASS / PG28 404 NEXT

## Project Brief
Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers, structured as reusable ORVEAX commercial IP for ThemeForest and independent distribution.

## Page Stage Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

No page enters implementation before PS6. PS8 requires applicable page QA plus deployed Cloudflare browser acceptance. Cloudflare review is a parallel final-acceptance gate and does not block continued PS6/PS7 production.

## M0 — Product Foundation Freeze — PASS / CLOSED
Scope, architecture, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED
Bootstrap 5.3.8 local foundation, Tajawal/Manrope, tokens, components, icon sprite, patterns, RTL/LTR, config runtime and global shell are implemented. F05 Icon Integrity now covers **56 AR/EN pages with zero missing sprite references** after PG27.

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

## M6 — Support / Utility — IN PROGRESS
- PG26 FAQ — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG27 Contact — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG28 404 — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG29 Coming Soon — NOT STARTED.
- PG30 Privacy — NOT STARTED.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

### PG26 Evidence
- 18 semantic FAQ items / 6 groups in AR and EN.
- Search/category/query/language/accordion/empty-reset interaction groups PASS.
- Final source/content/SEO/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `26a2a72870b3506f098a3dd95e38c56756575e10`.
- QA report: `docs/PG26-QA-REPORT-V1.md`.

### PG27 Evidence
- Four canonical contact routes: General / Buyer & RFQ / Supplier Submissions / Partnerships.
- Existing `config.js` controls route emails, phone, address, business hours and social links.
- `?topic=` query hydration, normalization and AR/EN language-state preservation implemented.
- Demo enquiry form validates locally only; no fetch/XHR/CRM/external endpoint and no message-sent claim.
- Illustrative map placeholder has no external provider/coordinates; social channels remain hidden while config URLs are unconfigured.
- First QA exposed actual main-phone and consent touch-target defects; both fixed in page CSS.
- QA architecture was improved by extracting the large inline runner from YAML into `.github/scripts/qa_pg27_contact.py` with a CI interaction adapter for headless reset activation.
- Final source/config/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Route / query-language / invalid-topic / form interaction groups: PASS in AR and EN.
- Final evidence: `7cfffde78233c087ee2381247470bb024d3689e1`.
- QA report: `docs/PG27-QA-REPORT-V1.md`.
- PS7 promotion: `bdd732bd8bb969dad17c4aca05111d4a53a05379`.
- Global F05: **56 AR/EN pages / 0 missing references**.

### Preview Utility
`site-map.html` remains a noindex internal Preview Utility outside the 33-layout product scope. After PG27 it contains **33 cards / 28 implemented / 5 pending / 56 AR+EN page links**. PG28 404 is NEXT. Preview QA failures = **0**, evidence `e522f94c27b17609ac179c1c012f9f9ed2f0390d`.

M6 gate: all seven support/utility layouts implemented in AR/EN, applicable PS8 acceptance complete, utility/legal/demo boundaries verified, and zero Critical/High defects.

## M7 — Full QA & Optimization — NOT STARTED
Full AR/EN parity, claim/disclaimer, data, SEO, broken-link, responsive, accessibility, performance, cross-browser and leakage QA. Gate: zero Critical / High defects.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED
Buyer documentation, customization/deployment guides, licenses/credits, changelog, preview/listing material, final ZIP and ThemeForest submission checklist. Gate: Submission Candidate 1.0.0.

## Current Production Order
1. **M6 / PG28 — 404**: canonical content → PS6 Page Design Profile / SEO + recovery-route contract → AR/EN build → branded error state / home + recovery links / contact fallback / responsive/accessibility QA.
2. Continue PG29–PG32 sequentially under M6.
3. In parallel, close applicable Cloudflare PS8 batches and PG33 QA follow-up.

## Change Control
New page or Main Feature family requires Scope Change or V1.1+. QA/accessibility/performance/responsive/RTL fixes may be corrected centrally without reopening scope.

## CR-001 Scope Addendum
PG33 Company Profile expanded active V1 to **33 unique layouts / approximately 66 AR+EN HTML pages**.

Copyright © ORVEAX.
