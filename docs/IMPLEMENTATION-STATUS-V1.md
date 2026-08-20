# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/origex-html-template`  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-20 — M6 IN PROGRESS / PG26 FAQ PS7 CI QA PASS / PG27 CONTACT NEXT

Notion `ORIGEX — ORX-P01 | Project HQ` remains the product-state authority; GitHub records implementation and evidence.

## Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

PS8 requires deployed Cloudflare browser acceptance where defined. Cloudflare review remains a parallel final-acceptance stream and does not block sequential PS6/PS7 page production.

## Project Controls
| Control | Current State |
|---|---|
| M0 Product Foundation | PASS / CLOSED |
| M1 Global System & Components | PASS / CLOSED |
| Global Navigation V1 | LOCKED / centrally normalized |
| Global Footer V1 | LOCKED / centrally normalized; PG26 AR shell normalized centrally during build |
| F05 Icon Integrity | PASS — **54 AR/EN pages / 0 missing sprite references** |
| Visual Site Map | `site-map.html` — **33 PG cards / 27 implemented / 6 pending / 54 AR+EN links**; PG27 next |
| Cloudflare Test Environment | AVAILABLE VIA MANUAL REBUILD |
| Cloudflare Auto-Deploy | DEFERRED / repair pending |
| M5 Page Production | **CODE/CI COMPLETE — PG20–PG25 PS7**; deployed PS8 acceptance remains open |
| Active Sequential Production | **M6 IN PROGRESS — PG26 PS7; PG27 Contact NEXT** |

## Page Production Snapshot
### M2 — Home Family
- PG01 Home 01 — **PS8 / PASS / CLOSED**.
- PG02 Home 02 — **PS7 / CI QA PASS**.
- PG03 Home 03 — **PS7 / CI QA PASS**.
- PG04 Landing — **PS7 / CI QA PASS**.

### M3 — Company / Business / Market
- PG05 About — **PS7 / CI QA PASS**.
- PG06 How We Work — **PS7 / CI QA PASS**.
- PG07 Capabilities — **PS7 / CI QA PASS**.
- PG08 Service Details — **PS7 / CI QA PASS**.
- PG14 Market Access — **PS7 / CI QA PASS**.
- PG15 Markets / Countries — **PS7 / CI QA PASS**.
- PG33 Company Profile — **PS7 IMPLEMENTED / QA FOLLOW-UP OPEN**.

### M4 — Product / Supplier / Conversion
PG09–PG13 and PG16–PG19 are **PS7 / CI QA PASS**. M4 page production is code/CI complete; Cloudflare PS8 batch acceptance remains open.

### M5 — Proof / Resources / Compliance / Content
PG20–PG25 are **PS7 / CI QA PASS**. M5 page production is CODE/CI COMPLETE; applicable deployed Cloudflare PS8 final acceptance remains open.

### M6 — Support / Utility
- PG26 FAQ — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG27 Contact — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG28 404 — NOT STARTED.
- PG29 Coming Soon — NOT STARTED.
- PG30 Privacy — NOT STARTED.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

## PG26 Final Evidence
- Profile: `docs/page-design-profiles/pg26-faq-v1.md` — PS7.
- AR/EN: `ar/faq.html` + `en/faq.html`.
- CSS: `assets/css/origex-faq.css`.
- Runtime: `assets/js/origex-faq.js`.
- QA workflow: `.github/workflows/pg26-faq-qa.yml`.
- QA report: `docs/PG26-QA-REPORT-V1.md`.
- Content model: **18 semantic FAQ records / 6 groups** in each language; no `faq.json`, CMS or remote API.
- Exact Arabic Master Q/A for product-submission acceptance and pricing preserved.
- Remaining FAQ copy derives only from frozen ORIGEX product/supplier/RFQ/distribution/compliance/Demo rules.
- Progressive enhancement: FAQ content remains readable without PG26 runtime; JavaScript owns search/category/query/language state only; C14 remains the single accordion runtime.
- Search + category AND filtering + dynamic group/count state + zero-result/reset + Escape clear implemented.
- Query hydration: `category` + `q`; invalid category normalizes to all.
- AR/EN desktop and mobile language links preserve normalized search/category state.
- First QA rendered/interactions were already clean; source checker exposed three marker/live-region expectation mismatches only. QA contract corrected in `3d37726f53fb26e01bcfe26277e44f2faa30cca1` and full workflow rerun.
- Final source/content/SEO/runtime failures: **0**.
- Final rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Accordion keyboard, category, query/language, invalid category and empty/reset/Escape interactions: **PASS** in AR and EN.
- Final evidence commit: `26a2a72870b3506f098a3dd95e38c56756575e10`.
- PS7 promotion: `051efff575a48eeead1aeeb93bb00e88dbe748c0`.
- Global F05 after PG26: **54 pages / 0 missing references**.

## Preview Utility
- `site-map.html` is a noindex internal Visual Site Map / Preview Index, not PG34.
- It contains exactly PG01–PG33.
- Current state after PG26: **27 implemented / 6 pending / 54 AR+EN page links**.
- PG27 Contact is NEXT; pending pages intentionally expose no destination links.
- Search and Implemented/Pending filters remain available.
- Preview QA strips query/hash portions before local target-existence checks.

## Shared State
- Global Navigation V1 remains locked and centrally normalized.
- Global Footer V1 remains centrally normalized.
- F05 Icon Integrity: **54 AR/EN pages / 0 missing sprite references**.
- PG33 QA follow-up and deployed Cloudflare PS8 reviews for prior milestones remain parallel workstreams.

## Next Action
Start **PG27 — Contact** through canonical content review → PS6 Page Design Profile / SEO/contact-routing contract → AR/EN implementation → contact-route/form/config/demo-safety/responsive/accessibility QA.

Copyright © ORVEAX.
