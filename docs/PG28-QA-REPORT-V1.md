# ORIGEX — PG28 404 QA Report V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Page: PG28 — 404  
Files: `ar/404.html` + `en/404.html`  
Final Page Stage: **PS7 — IMPLEMENTED / CI QA PASS — AR+EN**

## Canonical Contract
PG28 implements the frozen 404 scope only:
- branded error state
- clear explanation
- Home action
- product/recovery routes
- Contact fallback

Arabic canonical content is preserved:
- H1: `الصفحة غير موجودة، لكن المسار واضح.`
- Support: `ربما تغير الرابط أو تم نقله. ارجع إلى المنتجات أو الموردين أو تواصل معنا للوصول للمعلومة المطلوبة.`
- Primary CTAs: `العودة للرئيسية` / `استعرض المنتجات`

English preserves the same recovery intent with H1 `This page is unavailable, but the route is clear.`

## Implementation
- `assets/css/origex-404.css` — branded utility composition and responsive recovery cards.
- `assets/js/origex-404.js` — local recovery filtering, result count, empty/reset/Escape behavior and optional `?q=` language-preserved state.
- Recovery routes are limited to Home / Products / Suppliers / Resources / FAQ / Contact.
- Progressive enhancement is preserved: all recovery cards are present and usable without PG28 JavaScript.
- No external search provider, redirect engine, storage, form, iframe, map provider or network submission is introduced.

## SEO / Error Contract
- `robots=noindex,follow` in both languages.
- No canonical/hreflang tags on the branded error asset.
- No JSON-LD/SearchAction/Product/Offer/Review/LocalBusiness/Organization claim.
- Open Graph metadata is present for direct preview only.
- The HTML explicitly states that production hosting must return a real HTTP 404; the page does not claim that the deployment layer is already configured.
- PS8 must verify the deployed missing-route response status before final acceptance.

## QA Evidence
Final workflow evidence commit: `de86b1392f523f26dffa2d53c28145653f2f0402`.

### Source / SEO / Runtime
`qa/pg28-404/source-report.json`
- failures: **0**
- AR failures: **0**
- EN failures: **0**
- runtime failures: **0**
- six recovery destinations present in the approved order in both languages.
- no broken local recovery target.
- navigation/footer normalization checks PASS.
- no client/TARGET leakage.

### Rendered / Responsive
`qa/pg28-404/rendered-report.json`
- AR 390: PASS
- AR 820: PASS
- AR 1366: PASS
- AR 1536: PASS
- EN 390: PASS
- EN 820: PASS
- EN 1366: PASS
- EN 1536: PASS

**8/8 responsive cases PASS.**

### Interaction
All interaction groups PASS in Arabic and English:
- local recovery search
- matching Supplier route presence
- query-state URL update
- language-link query preservation
- zero-result state
- keyboard reset
- `?q=` hydration
- Escape clear
- global mega-menu / mobile-drawer interaction

## QA Contract Correction
The first QA run exposed checker assumptions, not page defects:
1. readiness marker expected literal `data-pg28-ready` in JavaScript even though runtime correctly uses `root.dataset.pg28Ready`;
2. search assumed `supplier/مورد` must return exactly one card, while FAQ legitimately also contains supplier-related terms.

The QA contract was corrected to verify semantic behavior instead:
- readiness checks the actual dataset property implementation;
- supplier search must return at least one filtered destination and must include the Suppliers route, without incorrectly suppressing other legitimate matches.

After correction, the complete source/rendered/interaction gate passed with zero failures.

## Shared Gates
- Global Navigation V1: PASS / centrally normalized.
- Global Footer V1: PASS / centrally normalized.
- F05 Icon Integrity after PG28: **58 AR/EN pages / 0 missing sprite references**.

## Decision
**PG28 is promoted to PS7 — IMPLEMENTED / CI QA PASS — AR+EN.**

PS8 is intentionally not claimed. It requires deployed-browser acceptance plus confirmation that an actual missing URL receives HTTP 404 while rendering the branded error document.
