# ORIGEX — PG26 FAQ | QA Report V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Page: PG26 — FAQ  
Canonical file: `faq.html`  
Final Status: **PASS — PS7 ELIGIBLE**  
Date: 2026-08-20

## Scope Verified
PG26 implements the frozen V1 FAQ feature family:
- category navigation;
- local search;
- accessible accordion;
- buyer/supplier plus product/RFQ/distribution/demo groups;
- contact/RFQ CTA.

## Content / Demo Governance
- 18 semantic FAQ records across six groups in both Arabic and English.
- Arabic Master exact approved Q/A preserved for product-submission acceptance and pricing.
- Remaining support answers are refinements derived only from frozen ORIGEX product, supplier, RFQ, distribution, compliance and Demo/integration rules.
- No live availability, price, certification, partnership, market-entry or acceptance guarantee is introduced.
- No `faq.json`, CMS or remote API domain was introduced.
- No TARGET/client leakage detected.

## Architecture
- FAQ content is semantic HTML and remains readable without PG26 JavaScript.
- `assets/js/origex-faq.js` owns only local search, category filtering, query-string hydration, language-state preservation, counts, empty/reset and Escape-to-clear behavior.
- Registered C14 in `assets/js/origex-ui.js` remains the sole accordion open/close runtime.
- Global Navigation V1 and Global Footer V1 remain canonical.

## Source / Runtime QA
Final `qa/pg26-faq/source-report.json`:
- overall failures: **0**;
- Arabic failures: **0**;
- English failures: **0**;
- runtime failures: **0**;
- FAQ items: **18 AR / 18 EN**;
- groups: buyers / suppliers / products / rfq / distribution / demo.

Verified controls include:
- lang/dir and one H1;
- SEO canonical/hreflang/Open Graph baseline;
- WebPage + BreadcrumbList schema only;
- no prohibited Product/Offer/Review/Rating schema;
- 18 C14 semantic button/region relationships;
- search, seven category controls, live result region, empty/reset state;
- FAQ current state in Mega Menu and Mobile Drawer;
- Global Footer V1;
- no unapproved `assets/data/faq.json`;
- icon references registered;
- canonical Arabic Q/A text preserved.

## Rendered Responsive QA
Final `qa/pg26-faq/rendered-report.json`:

| Language | 390 | 820 | 1366 | 1536 |
|---|---:|---:|---:|---:|
| Arabic RTL | PASS | PASS | PASS | PASS |
| English LTR | PASS | PASS | PASS | PASS |

Total: **8/8 PASS**.

Verified at each representative viewport:
- no horizontal viewport overflow;
- correct directionality;
- 18 initial FAQ records visible;
- practical touch targets;
- desktop Mega Menu open/Escape behavior;
- mobile drawer open/close behavior.

## Interaction QA
All final interaction arrays are empty:
- AR/EN native C14 Enter open + Space close;
- RFQ category → exactly three results / only RFQ group visible / URL state set;
- combined `category=rfq&q=endpoint` hydration;
- desktop/mobile language links preserve category + query;
- invalid category normalizes to `all`;
- zero-result state;
- reset restores all 18 items;
- Escape clears active search.

## First-Run Finding and Correction
The first run returned three source-check failures only:
- checker expected a literal `data-pg26-ready` string while runtime correctly produced the attribute through `root.dataset.pg26Ready`;
- checker required `aria-live` on the numeric result element itself although the live region correctly wrapped it.

Rendered and interaction QA were already fully PASS. The QA checker was corrected to validate the actual DOM/accessibility contract, then the complete workflow was rerun. No page-local workaround was introduced.

## Global F05
After PG26 creation:
- pages checked: **54 AR/EN pages**;
- missing sprite references: **0**.

## Evidence
- PS6 profile: `docs/page-design-profiles/pg26-faq-v1.md`
- AR: `ar/faq.html`
- EN: `en/faq.html`
- CSS: `assets/css/origex-faq.css`
- Runtime: `assets/js/origex-faq.js`
- Workflow: `.github/workflows/pg26-faq-qa.yml`
- Final evidence commit: `26a2a72870b3506f098a3dd95e38c56756575e10`
- Final status: `qa/pg26-faq/run-status.txt` = PASS

## Gate Decision
**PG26 is approved for PS7 — Implemented / CI QA PASS.**

PS8 is not granted here. Deployed Cloudflare AR/EN mobile/desktop acceptance remains required under the canonical PS8 Closure Matrix.

Next sequential page-production action: **PG27 — Contact**.

Copyright © ORVEAX.
