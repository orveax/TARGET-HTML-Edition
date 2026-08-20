# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/origex-html-template`  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-20 — M5 PAGE PRODUCTION CODE/CI COMPLETE / PG20–PG25 PS7 / M6 PG26 NEXT

Notion `ORIGEX — ORX-P01 | Project HQ` remains the product-state authority; GitHub records implementation and evidence.

## Lifecycle
`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

PS8 requires deployed Cloudflare browser acceptance where defined. Cloudflare review remains a parallel final-acceptance stream and does not block sequential PS6/PS7 page production.

## Project Controls
| Control | Current State |
|---|---|
| M0 Product Foundation | PASS / CLOSED |
| M1 Global System & Components | PASS / CLOSED |
| Global Navigation V1 | LOCKED / centrally normalized; PG25 normalization `83275a173a12066af58654c2fda82b42e281d2fa` |
| Global Footer V1 | LOCKED / centrally normalized |
| F05 Icon Integrity | PASS — 52 AR/EN pages / 0 missing sprite references at PG25 closure |
| Visual Site Map | `site-map.html` — 33 PG cards / 26 implemented / 7 pending / 52 AR+EN links; PG26 next |
| Cloudflare Test Environment | AVAILABLE VIA MANUAL REBUILD |
| Cloudflare Auto-Deploy | DEFERRED / repair pending |
| M5 Page Production | **CODE/CI COMPLETE — PG20–PG25 PS7**; deployed PS8 acceptance remains open |
| Active Sequential Production | **M6 READY — PG26 FAQ NEXT** |

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
- PG24 Insights / Blog — **PS7 / CI QA PASS**.
- PG25 Article Details — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.

**M5 page production is CODE/CI COMPLETE.** M5 remains open only for applicable deployed Cloudflare PS8 final acceptance.

### M6 — Support / Utility
- PG26 FAQ — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG27 Contact — NOT STARTED.
- PG28 404 — NOT STARTED.
- PG29 Coming Soon — NOT STARTED.
- PG30 Privacy — NOT STARTED.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

## PG25 Final Evidence
- Profile: `docs/page-design-profiles/pg25-article-details-v1.md` — PS7.
- AR/EN: `ar/article-details.html` + `en/article-details.html`.
- CSS: `assets/css/origex-article-details.css`.
- Runtime: `assets/js/origex-article-details.js`.
- QA workflow: `.github/workflows/pg25-article-details-qa.yml`.
- QA report: `docs/PG25-QA-REPORT-V1.md`.
- Article states: `article-001..009`; default 001 remains semantic HTML, 002–009 are local `<template>` Demo editorial records.
- No CMS/API or unapproved `articles.json` domain.
- Missing ID → article-001; invalid ID → visible notice + article-001 fallback.
- AR/EN desktop + mobile language switch preserves valid article ID.
- Previous/next, three related articles excluding current, Copy Link, Email, LinkedIn and WhatsApp share actions implemented.
- First QA failed only on shared `nav-drift`; fixed centrally by Global Navigation V1 commit `83275a173a12066af58654c2fda82b42e281d2fa`.
- Final source/editorial/runtime failures: **0**.
- Final rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Default/invalid/state-share/last-boundary interactions: **PASS** in AR and EN.
- Final evidence commit: `d6f9f74b4ef9352ab631fdd8f372d1963bb6852a`.
- PS7 promotion: `ec110ccdf576d7a8a3b4fa81379a4936a369be3f`.

## Preview Utility
- `site-map.html` is a noindex internal Visual Site Map / Preview Index, not PG34.
- It contains exactly PG01–PG33.
- Current state after PG25: **26 implemented / 7 pending / 52 AR+EN page links**.
- PG26 is displayed as NEXT; pending pages intentionally expose no destination links.
- Search and Implemented/Pending filters remain available.
- Preview QA strips query/hash portions before local target-existence checks, allowing valid detail-preview links without false broken-file failures.

## Shared State
- Global Navigation V1 remains locked and centrally normalized.
- Global Footer V1 remains centrally normalized.
- F05 Icon Integrity: **52 AR/EN pages / 0 missing sprite references** at PG25 closure.
- PG33 QA follow-up and deployed Cloudflare PS8 reviews for prior milestones remain parallel workstreams.

## Next Action
Start **M6 / PG26 — FAQ** through canonical content review → PS6 Page Design Profile + SEO/FAQ contract → AR/EN implementation → category navigation/search/accordion/supplier-buyer groups/contact CTA/responsive/accessibility QA.

Copyright © ORVEAX.
