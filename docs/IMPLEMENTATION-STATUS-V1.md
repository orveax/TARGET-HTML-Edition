# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/origex-html-template`  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-20 — M6 IN PROGRESS / PG26–PG28 PS7 CI QA PASS / PG29 COMING SOON NEXT

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
| Global Footer V1 | LOCKED / centrally normalized |
| F05 Icon Integrity | PASS — **58 AR/EN pages / 0 missing sprite references** |
| Visual Site Map | `site-map.html` — **33 PG cards / 29 implemented / 4 pending / 58 AR+EN links**; PG29 next |
| Cloudflare Test Environment | AVAILABLE VIA MANUAL REBUILD |
| Cloudflare Auto-Deploy | DEFERRED / repair pending |
| M5 Page Production | **CODE/CI COMPLETE — PG20–PG25 PS7**; deployed PS8 acceptance remains open |
| Active Sequential Production | **M6 IN PROGRESS — PG26–PG28 PS7; PG29 Coming Soon NEXT** |

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
- PG27 Contact — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG28 404 — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG29 Coming Soon — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG30 Privacy — NOT STARTED.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

## PG26 Final Evidence
- Profile: `docs/page-design-profiles/pg26-faq-v1.md` — PS7.
- QA report: `docs/PG26-QA-REPORT-V1.md`.
- Final source/content/SEO/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `26a2a72870b3506f098a3dd95e38c56756575e10`.

## PG27 Final Evidence
- Profile: `docs/page-design-profiles/pg27-contact-v1.md` — PS7.
- QA report: `docs/PG27-QA-REPORT-V1.md`.
- Four canonical contact routes with config-driven contact data and validation-only Demo form.
- Final source/config/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Route/query-language/invalid-topic/form interactions: PASS.
- Final evidence: `7cfffde78233c087ee2381247470bb024d3689e1`.

## PG28 Final Evidence
- Profile: `docs/page-design-profiles/pg28-404-v1.md` — **PS7**.
- AR/EN: `ar/404.html` + `en/404.html`.
- CSS: `assets/css/origex-404.css`.
- Runtime: `assets/js/origex-404.js`.
- QA runner: `.github/scripts/qa_pg28_404_v2.py`.
- QA workflow: `.github/workflows/pg28-404-qa.yml`.
- QA report: `docs/PG28-QA-REPORT-V1.md`.
- Exact Arabic H1/support and primary CTAs preserved.
- `robots=noindex,follow`; no canonical/hreflang/JSON-LD/SearchAction claim on the error asset.
- Six approved recovery routes: Home / Products / Suppliers / Resources / FAQ / Contact.
- Progressive enhancement: recovery destinations remain visible without page runtime.
- Local search supports result count, empty/reset, Escape clear and optional `?q=` language-preserved state without external search/network/storage.
- Explicit deployment boundary: HTML is the branded error document; PS8 must verify a genuine missing route returns HTTP 404.
- First QA exposed checker assumptions only; QA contract corrected to test semantic supplier-route presence rather than an artificial single-result count.
- Final source/SEO/runtime failures: **0**.
- Final rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Search / query-language / empty-reset / query-Escape interactions: **PASS** in AR and EN.
- F05 after PG28: **58 AR/EN pages / 0 missing references**.
- Final evidence commit: `de86b1392f523f26dffa2d53c28145653f2f0402`.

## Preview Utility
- `site-map.html` is a noindex internal Visual Site Map / Preview Index, not PG34.
- It contains exactly PG01–PG33.
- Current state after PG28: **29 implemented / 4 pending / 58 AR+EN page links**.
- PG29 Coming Soon is displayed as NEXT; pending pages expose no destination links.
- Search and Implemented/Pending filters remain available.
- Preview QA is required to remain at zero failures after publication.

## Shared State
- Global Navigation V1 remains locked and centrally normalized.
- Global Footer V1 remains centrally normalized.
- F05 Icon Integrity: **58 AR/EN pages / 0 missing sprite references**.
- PG33 QA follow-up and deployed Cloudflare PS8 reviews remain parallel workstreams.

## Next Action
Start **PG29 — Coming Soon** through canonical content review → PS6 Page Design Profile + SEO/prelaunch-state contract → AR/EN implementation → countdown/CTA/subscription/demo-boundary/responsive/accessibility QA according to frozen scope.

Copyright © ORVEAX.
