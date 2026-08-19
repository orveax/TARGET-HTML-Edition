# ORIGEX — PG24 Insights / Blog | QA Report V1

Date: 2026-08-20  
Status: **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**  
Canonical page: `insights.html`

## Scope Delivered
- Featured Demo article.
- Six-category filter system.
- Eight-card article grid.
- Local text search.
- Six-per-page pagination.
- Query hydration / URL state for `category`, `q`, `page`.
- AR/EN state preservation.
- Zero-result empty state.

## Editorial Safety
- Nine total editorial records are fictional ORIGEX Demo content.
- No CMS/API or new `articles.json` domain.
- No live market intelligence, legal/regulatory advice, investment advice, measured result, popularity metric or client claim.
- Listing page emits `CollectionPage` + `BreadcrumbList` only; no Article/Product/Offer/Rating schema claim.

## Source / Runtime QA
Final evidence: `qa/pg24-insights/source-report.json`.
- AR failures: 0.
- EN failures: 0.
- Runtime failures: 0.
- Canonical / hreflang / schema / client leakage / icon references: PASS.
- Article route IDs: `article-001` through `article-009` aligned to canonical PG25 route.

## Rendered / Interaction QA
Final evidence: `qa/pg24-insights/rendered-report.json`.
- AR 390 / 820 / 1366 / 1536: PASS.
- EN 390 / 820 / 1366 / 1536: PASS.
- Total responsive matrix: **8/8 PASS**.
- Category filtering: PASS.
- Search: PASS.
- Pagination / `?page=2`: PASS.
- AR/EN query preservation: PASS.
- Zero-result empty state: PASS.
- Desktop mega-menu and mobile drawer interaction: PASS.
- Horizontal overflow: none in the tested matrix.

## Shared-System Defect Found and Corrected
The first PG24 run reported only `footer-drift` on `en/insights.html`. Rendered and page interactions already passed. The defect was corrected through the canonical Global Footer V1 normalizer. The global footer gate then reported **50 AR/EN pages / 0 failures**, and PG24 was rerun to final PASS.

## Global Gates at Closure
- Global Navigation V1: PASS.
- Global Footer V1: PASS — 50 AR/EN pages / 0 failures.
- F05 Icon Integrity: PASS — 50 AR/EN pages / 0 missing sprite references.

## Evidence
- Initial failing evidence commit: `79b7757c8595354ae9efb3a1f57e5d6e3118cefc`.
- Central footer normalization commit: `1aca18259ab8ae9e28e4834636fed9308741b7a4`.
- Final PG24 PASS evidence commit: `9fd0853544bd36d46f9ad34dd3239152a7f4646f`.
- PS7 profile promotion commit: `61b461911cbe67cd264d1af649f709ad6cb6c325`.

## Remaining Gate
PS8 requires deployed Cloudflare AR/EN mobile/desktop browser acceptance under the project PS8 governance.

Copyright © ORVEAX.