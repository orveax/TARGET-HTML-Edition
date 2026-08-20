# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/origex-html-template`  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-20 — M6 IN PROGRESS / PG26–PG29 PS7 CI QA PASS / PG30 PRIVACY NEXT

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
| F05 Icon Integrity | PASS — **60 AR/EN pages / 0 missing sprite references** |
| Visual Site Map | `site-map.html` — **33 PG cards / 30 implemented / 3 pending / 60 AR+EN links**; PG30 next |
| Cloudflare Test Environment | AVAILABLE VIA MANUAL REBUILD |
| Cloudflare Auto-Deploy | DEFERRED / repair pending |
| M5 Page Production | **CODE/CI COMPLETE — PG20–PG25 PS7**; deployed PS8 acceptance remains open |
| Active Sequential Production | **M6 IN PROGRESS — PG26–PG29 PS7; PG30 Privacy NEXT** |

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
- PG29 Coming Soon — **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**.
- PG30 Privacy — **NEXT VALID PAGE PRODUCTION ACTION**.
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
- QA report: `docs/PG28-QA-REPORT-V1.md`.
- Exact Arabic H1/support and primary CTAs preserved.
- `robots=noindex,follow`; no canonical/hreflang/JSON-LD/SearchAction claim on the error asset.
- Six approved recovery routes: Home / Products / Suppliers / Resources / FAQ / Contact.
- Final source/SEO/runtime failures: **0**.
- Final rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Search/query-language/empty-reset/query-Escape interactions: **PASS**.
- Final evidence: `de86b1392f523f26dffa2d53c28145653f2f0402`.

## PG29 Final Evidence
- Profile: `docs/page-design-profiles/pg29-coming-soon-v1.md` — **PS7**.
- AR/EN: `ar/coming-soon.html` + `en/coming-soon.html`.
- CSS: `assets/css/origex-coming-soon.css`.
- Runtime: `assets/js/origex-coming-soon.js`.
- Config: `ORIGEX_CONFIG.comingSoon.launchDate` defaults empty and is buyer-defined only.
- QA runner: `.github/scripts/qa_pg29_coming_soon.py`.
- QA workflow: `.github/workflows/pg29-coming-soon-qa.yml`.
- QA report: `docs/PG29-QA-REPORT-V1.md`.
- Frozen Main Features present: logo / status message / launch date-countdown / subscribe UI / social links / contact link.
- `robots=noindex,follow`; no canonical/hreflang/JSON-LD/Event claim on the default utility asset.
- Default no-date state PASS; valid future countdown PASS; past-date no-fabrication fallback PASS.
- Demo subscribe invalid/valid/reset PASS with zero network/storage behavior.
- Placeholder social URLs remain hidden; configured public URL visibility PASS.
- Final source/config/runtime failures: **0**.
- Final rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Countdown / subscribe / social interactions: **PASS** in AR and EN.
- F05 after PG29: **60 AR/EN pages / 0 missing references**.
- Final evidence commit: `cf91343ff95c66ba544387e26506c60076610f74`.

## Preview Utility
- `site-map.html` is a noindex internal Visual Site Map / Preview Index, not PG34.
- It contains exactly PG01–PG33.
- Approved state after PG29: **30 implemented / 3 pending / 60 AR+EN page links**.
- PG30 Privacy is displayed as NEXT; pending pages expose no destination links.
- `.github/scripts/sync_preview_site_map.py` is now the maintainable synchronization authority for approved PS7 preview status, reducing large-file manual edits.
- Search and Implemented/Pending filters remain available.
- Preview QA must remain at zero failures after publication.

## Shared State
- Global Navigation V1 remains locked and centrally normalized.
- Global Footer V1 remains centrally normalized.
- F05 Icon Integrity: **60 AR/EN pages / 0 missing sprite references**.
- PG33 QA follow-up and deployed Cloudflare PS8 reviews remain parallel workstreams.

## Next Action
Start **PG30 — Privacy** through canonical content review → PS6 Page Design Profile + legal-demo/indexability contract → AR/EN implementation → sample legal structure / table of contents / updated-date handling / contact reference / legal disclaimer / responsive-accessibility QA according to frozen scope.

Copyright © ORVEAX.
