# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/origex-html-template`  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-20 — M6 IN PROGRESS / PG26–PG27 PS7 CI QA PASS / PG28 404 NEXT

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
| F05 Icon Integrity | PASS — **56 AR/EN pages / 0 missing sprite references** |
| Visual Site Map | `site-map.html` — **33 PG cards / 28 implemented / 5 pending / 56 AR+EN links**; PG28 next |
| Cloudflare Test Environment | AVAILABLE VIA MANUAL REBUILD |
| Cloudflare Auto-Deploy | DEFERRED / repair pending |
| M5 Page Production | **CODE/CI COMPLETE — PG20–PG25 PS7**; deployed PS8 acceptance remains open |
| Active Sequential Production | **M6 IN PROGRESS — PG26 + PG27 PS7; PG28 404 NEXT** |

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
- PG28 404 — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG29 Coming Soon — NOT STARTED.
- PG30 Privacy — NOT STARTED.
- PG31 Terms — NOT STARTED.
- PG32 Components / Elements Library — NOT STARTED.

## PG26 Final Evidence
- Profile: `docs/page-design-profiles/pg26-faq-v1.md` — PS7.
- QA report: `docs/PG26-QA-REPORT-V1.md`.
- 18 semantic FAQ items / 6 groups in AR and EN.
- Search/category/query/language/accordion/empty-reset interactions: PASS.
- Final source/content/SEO/runtime failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Final evidence: `26a2a72870b3506f098a3dd95e38c56756575e10`.

## PG27 Final Evidence
- Profile: `docs/page-design-profiles/pg27-contact-v1.md` — **PS7**.
- AR/EN: `ar/contact.html` + `en/contact.html`.
- CSS: `assets/css/origex-contact.css`.
- Runtime: `assets/js/origex-contact.js`.
- QA runner: `.github/scripts/qa_pg27_contact.py`.
- CI interaction adapter: `.github/scripts/qa_pg27_contact_ci.py`.
- QA workflow: `.github/workflows/pg27-contact-qa.yml`.
- QA report: `docs/PG27-QA-REPORT-V1.md`.
- Four canonical routes: `general` / `rfq` / `supplier` / `partner`.
- Existing `config.js` hooks drive route emails, phone, address, business hours and social links.
- `?topic=` hydration and invalid-topic normalization implemented; AR/EN desktop/mobile language links preserve normalized topic state.
- Enquiry form is validation-only Demo behavior with no fetch/XHR/CRM/external form provider and explicit no-transmission confirmation.
- Map remains an illustrative local placeholder with no provider, coordinates or location-verification claim.
- Social block stays hidden while config URLs remain `#`.
- First QA identified real phone/consent touch-target defects; fixed in page CSS.
- QA was refactored from large inline YAML into a maintainable standalone runner; headless reset activation uses keyboard semantics while responsive hit-area QA independently verifies the public control size.
- Final source/config/runtime failures: **0**.
- Final rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Route / query-language / invalid-topic / form validation-success-reset interactions: **PASS** in AR and EN.
- F05 after PG27: **56 AR/EN pages / 0 missing references**.
- Final evidence commit: `7cfffde78233c087ee2381247470bb024d3689e1`.
- PS7 promotion: `bdd732bd8bb969dad17c4aca05111d4a53a05379`.

## Preview Utility
- `site-map.html` is a noindex internal Visual Site Map / Preview Index, not PG34.
- It contains exactly PG01–PG33.
- Current state after PG27: **28 implemented / 5 pending / 56 AR+EN page links**.
- PG28 404 is displayed as NEXT; pending pages intentionally expose no destination links.
- Search and Implemented/Pending filters remain available.
- Preview QA: **0 failures**; evidence `e522f94c27b17609ac179c1c012f9f9ed2f0390d`.

## Shared State
- Global Navigation V1 remains locked and centrally normalized.
- Global Footer V1 remains centrally normalized.
- F05 Icon Integrity: **56 AR/EN pages / 0 missing sprite references**.
- PG33 QA follow-up and deployed Cloudflare PS8 reviews remain parallel workstreams.

## Next Action
Start **PG28 — 404** through canonical content review → PS6 Page Design Profile + SEO/recovery-route contract → AR/EN implementation → branded error state / home + recovery links / contact fallback / responsive / accessibility QA.

Copyright © ORVEAX.
