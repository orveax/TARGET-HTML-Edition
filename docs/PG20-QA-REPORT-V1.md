# ORIGEX — PG20 Case Studies QA Report V1

Product ID: ORX-P01  
Page: PG20 — Case Studies  
Milestone: M5 — Proof / Resources / Compliance / Content  
Final Page Stage: **PS7 — IMPLEMENTED / CI QA PASS**  
Date: 2026-08-20

## Authority

- Page profile: `docs/page-design-profiles/pg20-case-studies-v1.md`
- Arabic: `ar/case-studies.html`
- English: `en/case-studies.html`
- Composition: `assets/css/origex-case-studies.css`
- Runtime: `assets/js/origex-case-studies.js`
- QA workflow: `.github/workflows/pg20-case-studies-qa.yml`

## Scope Verified

Frozen PG20 features verified:
- filters;
- six fictional Demo case-study cards;
- industry/category tags;
- qualitative result highlights;
- commercial CTA.

No new structured-data domain was introduced. PG20 remains editorial HTML because the frozen V1 Data Schema only defines products, suppliers and markets.

## Source / Runtime QA

Final evidence: `qa/pg20-case-studies/source-report.json`.

Result: **PASS — failures 0**.

Verified:
- AR `lang=ar dir=rtl` and EN `lang=en dir=ltr`;
- exact canonical H1 parity;
- sections: hero / library / boundary / CTA;
- six stable IDs `case-001`–`case-006`;
- five frozen filter values;
- visible Demo/illustrative labels;
- no `cases.json` architecture drift;
- no Fetch/XHR/localStorage/sessionStorage runtime behavior;
- self canonical + AR/EN/x-default hreflang;
- WebPage + BreadcrumbList structured data only;
- no Review/Rating/Offer performance schema;
- Global Navigation V1 alignment;
- Global Footer V1 alignment;
- no TARGET/client leakage;
- all referenced sprite icons registered.

## Rendered / Interaction QA

Final evidence: `qa/pg20-case-studies/rendered-report.json`.

Result: **PASS — failures 0**.

Responsive matrix:
- AR 390 — PASS
- AR 820 — PASS
- AR 1366 — PASS
- AR 1536 — PASS
- EN 390 — PASS
- EN 820 — PASS
- EN 1366 — PASS
- EN 1536 — PASS

Interactions:
- AR filter/query — PASS
- AR empty state — PASS
- EN filter/query — PASS
- EN empty state — PASS

Verified behavior:
- `?focus=distribution` hydrates two matching cases;
- current filter exposes `aria-pressed=true`;
- valid focus query is preserved across language switch;
- keyboard activation resets to All Cases;
- All Cases removes the focus query;
- zero-result future state displays the accessible empty-state surface;
- result count stays synchronized;
- desktop mega menu and mobile drawer behavior pass;
- no horizontal page overflow after final fix;
- touch-target floor passes.

## Defects / Improvements During QA

### 1. Data-governance improvement — no `cases.json`

The frozen data authority defines structured JSON only for products, suppliers and markets. A new case-study JSON domain would have been an unnecessary schema expansion. PG20 therefore uses editorial HTML with lightweight DOM filtering.

### 2. Navigation-contract conflict corrected before closure

The first Page Design Profile draft assumed Case Studies should be current in the mobile drawer. `GLOBAL-NAVIGATION-CONTRACT-V1.md` explicitly omits Case Studies from the locked flat mobile order while exposing it in the Resources & Support mega group. The page profile was corrected rather than creating a page-local navigation fork.

### 3. 390px horizontal-overflow defect

Initial rendered evidence passed Source/Runtime and all interactions but failed AR/EN at 390px with horizontal overflow. Root cause was the no-wrap filter row retaining min-content width inside the flexible layout.

Correction:
- logical `min-inline-size:0` applied to relevant flex/grid children;
- filter group constrained to the available inline size;
- filter chips use `flex:0 0 auto`;
- horizontal scrolling remains inside the filter group only;
- long editorial content receives safe wrapping.

Fix commit: `020097b889ec04df899e414647fcf3d89181d7d4`.

Final evidence commit: `d559056fe2b6b6bd88b7d0debf371f19525e0d80`.

## Shared-System Evidence

- Global Footer V1: PASS after PG20 addition.
- F05 Icon Integrity: PASS; active scan expanded to 42 AR/EN pages with zero missing sprite references at PG20 build time.
- Global Navigation V1 remains locked; no IA change was introduced.

## Final Decision

**PG20 = PS7 / IMPLEMENTED / CI QA PASS.**

Cloudflare deployed-browser acceptance remains required before PS8 final page acceptance.

Next valid page-production action: **PG21 — Case Study Details**.

Copyright © ORVEAX.
