# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/origex-html-template`  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-20 — M5 IN PROGRESS / PG20–PG24 PS7 CI QA PASS / PG25 NEXT

Notion `ORIGEX — ORX-P01 | Project HQ` remains the product-state authority; GitHub records implementation and evidence.

## Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

PS8 requires deployed Cloudflare browser acceptance where defined. Cloudflare review remains a parallel final-acceptance stream.

## Project Controls
| Control | Current State |
|---|---|
| M0 Product Foundation | PASS / CLOSED |
| M1 Global System & Components | PASS / CLOSED |
| Global Navigation V1 | LOCKED / centrally normalized |
| Global Footer V1 | PASS — 50 AR/EN pages / 0 failures at PG24 closure |
| F05 Icon Integrity | PASS — 50 AR/EN pages / 0 missing sprite references |
| Visual Site Map | `site-map.html` — 33 PG cards / 25 implemented / 8 pending / 50 AR+EN links; QA gate active |
| Cloudflare Test Environment | AVAILABLE VIA MANUAL REBUILD |
| Cloudflare Auto-Deploy | DEFERRED / repair pending |
| Active Production Milestone | M5 IN PROGRESS — PG20–PG24 PS7; PG25 next |

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
- PG09 Product Categories — **PS7 / CI QA PASS**.
- PG10 Products Grid — **PS7 / CI QA PASS**.
- PG11 Product Details — **PS7 / CI QA PASS**.
- PG12 Suppliers / Brands — **PS7 / CI QA PASS**.
- PG13 Supplier / Brand Details — **PS7 / CI QA PASS**.
- PG16 For Suppliers — **PS7 / CI QA PASS**.
- PG17 Submit Product — **PS7 / CI QA PASS**.
- PG18 RFQ — **PS7 / CI QA PASS**.
- PG19 Become Distributor / Partner — **PS7 / CI QA PASS**.

**M4 page production is code/CI complete.** Cloudflare PS8 batch acceptance remains open.

### M5 — Proof / Resources / Compliance / Content
- PG20 Case Studies — **PS7 / CI QA PASS**.
- PG21 Case Study Details — **PS7 / CI QA PASS**.
- PG22 Downloads / Resources — **PS7 / CI QA PASS**.
- PG23 Certifications & Compliance — **PS7 / CI QA PASS**.
- PG24 Insights / Blog — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG25 Article Details — **NEXT VALID PAGE PRODUCTION ACTION**.

### M6 — Support / Utility
PG26–PG32 remain NOT STARTED.

## PG24 Final Evidence
- Profile: `docs/page-design-profiles/pg24-insights-v1.md`.
- AR/EN: `ar/insights.html` + `en/insights.html`.
- CSS: `assets/css/origex-insights.css`.
- Runtime: `assets/js/origex-insights.js`.
- Editorial model: 9 fictional Demo records — 1 featured + 8 grid; no CMS/API and no new `articles.json` schema domain.
- Categories: buying / product / market / distribution / supplier.
- Runtime: local search, category filtering, 6-per-page pagination, `category/q/page` query hydration and AR/EN state preservation.
- First QA found only shared Global Footer V1 drift in `en/insights.html`; corrected centrally via footer normalizer commit `1aca18259ab8ae9e28e4834636fed9308741b7a4`.
- Final source/editorial/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Category/search/pagination/query/language-preservation/empty-state: PASS.
- Final QA evidence: `9fd0853544bd36d46f9ad34dd3239152a7f4646f`.
- PS7 promotion: `61b461911cbe67cd264d1af649f709ad6cb6c325`.
- QA report: `docs/PG24-QA-REPORT-V1.md`.

## Preview Utility
- `site-map.html` is a noindex internal Visual Site Map / Preview Index, not PG34.
- It contains exactly PG01–PG33.
- Current content after PG24: **25 implemented / 8 pending / 50 AR+EN page links**.
- Implemented pages expose AR/EN links; pending pages intentionally expose no broken destinations.
- Search and Implemented/Pending filters remain available.

## Shared State
- Global Navigation V1 remains locked and centrally normalized.
- Global Footer V1: **50 AR/EN pages / 0 failures** at PG24 closure.
- F05 Icon Integrity: **50 AR/EN pages / 0 missing sprite references**.
- PG33 QA follow-up and deployed Cloudflare PS8 reviews remain parallel workstreams.

## Next Action
Prepare **PG25 — Article Details** through canonical content review → PS6 Page Design Profile / SEO + article-detail editorial contract → AR/EN implementation → article ID, metadata, typography, share-link, related-article and responsive QA.

Copyright © ORVEAX.
