# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M5 FINAL ACCEPTANCE OPEN / M6 IN PROGRESS  
Last Alignment: 2026-08-20 — PG26–PG29 PS7 CI QA PASS / PG30 PRIVACY NEXT

## Project Brief
Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers, structured as reusable ORVEAX commercial IP for ThemeForest and independent distribution.

## Page Stage Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

No page enters implementation before PS6. PS8 requires applicable page QA plus deployed Cloudflare browser acceptance. Cloudflare review is a parallel final-acceptance gate and does not block continued PS6/PS7 production.

## M0 — Product Foundation Freeze — PASS / CLOSED
Scope, architecture, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED
Bootstrap 5.3.8 local foundation, Tajawal/Manrope, tokens, components, icon sprite, patterns, RTL/LTR, config runtime and global shell are implemented. F05 Icon Integrity covers **60 AR/EN pages with zero missing sprite references** after PG29.

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
- PG28 404 — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG29 Coming Soon — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG30 Privacy — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

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
- Branded 404 recovery layout in Arabic and English with exact frozen Arabic H1/support/CTA intent.
- `robots=noindex,follow`; no canonical/hreflang/JSON-LD/SearchAction claim on the error asset.
- Six approved local recovery routes: Home / Products / Suppliers / Resources / FAQ / Contact.
- Progressive enhancement plus local search/result-count/empty-reset/Escape/query-language state; no network/storage/search provider.
- Deployment boundary is explicit: HTML cannot set response status; PS8 must verify a genuinely missing route returns HTTP 404.
- Final source/SEO/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Search/query-language/empty-reset/query-Escape interactions: PASS.
- Final evidence: `de86b1392f523f26dffa2d53c28145653f2f0402`.
- QA report: `docs/PG28-QA-REPORT-V1.md`.

### PG29 Evidence
- Exact Arabic H1/support/Contact CTA intent PASS; English meaning parity PASS.
- Frozen Main Features present: logo / status message / launch date-countdown / subscribe UI / social links / contact link.
- `ORIGEX_CONFIG.comingSoon.launchDate` is the only launch-date authority and defaults to empty.
- Default no-date state PASS; valid future countdown PASS; past-date no-fabrication fallback PASS.
- Demo subscribe invalid/valid/reset PASS with zero network/storage behavior.
- Placeholder social URLs remain hidden; configured public URL visibility PASS.
- `robots=noindex,follow`; no canonical/hreflang/JSON-LD/Event claim on the default utility asset.
- Final source/config/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Countdown / subscribe / social interactions: PASS in AR and EN.
- Final evidence: `cf91343ff95c66ba544387e26506c60076610f74`.
- QA report: `docs/PG29-QA-REPORT-V1.md`.
- Global F05: **60 AR/EN pages / 0 missing references**.

### Preview Utility
`site-map.html` remains a noindex internal Preview Utility outside the 33-layout product scope. Approved state after PG29 is **33 cards / 30 implemented / 3 pending / 60 AR+EN page links**. PG30 Privacy is NEXT. `.github/scripts/sync_preview_site_map.py` now synchronizes approved PS7 preview state before the preview QA gate.

M6 gate: all seven support/utility layouts implemented in AR/EN, applicable PS8 acceptance complete, utility/legal/demo boundaries verified, and zero Critical/High defects.

## M7 — Full QA & Optimization — NOT STARTED
Full AR/EN parity, claim/disclaimer, data, SEO, broken-link, responsive, accessibility, performance, cross-browser and leakage QA. Gate: zero Critical / High defects.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED
Buyer documentation, customization/deployment guides, licenses/credits, changelog, preview/listing material, final ZIP and ThemeForest submission checklist. Gate: Submission Candidate 1.0.0.

## Current Production Order
1. **M6 / PG30 — Privacy**: canonical content → PS6 Page Design Profile / legal-demo + indexability contract → AR/EN build → sample legal structure / table of contents / updated-date handling / contact reference / legal disclaimer / responsive-accessibility QA.
2. Continue PG31–PG32 sequentially under M6.
3. In parallel, close applicable Cloudflare PS8 batches and PG33 QA follow-up.

## Change Control
New page or Main Feature family requires Scope Change or V1.1+. QA/accessibility/performance/responsive/RTL fixes may be corrected centrally without reopening scope.

## CR-001 Scope Addendum
PG33 Company Profile expanded active V1 to **33 unique layouts / approximately 66 AR+EN HTML pages**.

Copyright © ORVEAX.
