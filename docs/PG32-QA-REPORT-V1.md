# ORIGEX — PG32 Components / Elements Library | QA Report V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Page: PG32 — Components / Elements Library  
Canonical files: `ar/components.html`, `en/components.html`  
Final stage: **PS7 — IMPLEMENTED / CI QA PASS**  
Date: 2026-08-20

## Final Decision
PG32 passes its page-level PS7 gate as both the buyer-facing Components / Elements Library and the ORIGEX Design System QA Laboratory.

The page intentionally exposes current systemic dimension findings as `ALIGNED` / `BACKFIT`; a `BACKFIT` diagnostic is not a PG32 failure. The approved post-PG32 sequence owns the systemic remediation: shared backfit → global AR/EN regression → sequential PG01→PG33 second-pass review.

## Source / Registry Coverage
Final source report: **0 failures**.

Per language:
- 11 / 11 commercial card families represented;
- 17 / 17 C12–C28 core component references represented;
- 11 / 11 primitives represented;
- 9 / 9 dimension diagnostic rows represented;
- registered F05 icon references only.

Coverage includes F01–F07, P01–P11, C01–C28, S01–S06 and N01–N04 through rendered specimens or explicit contract/reference specimens.

## Canonical Content / Scope
PASS:
- Arabic canonical H1 and support;
- English meaning-equivalent H1;
- frozen PG32 Main Features: buttons, cards, badges, headings, tabs, accordions, forms, tables, alerts, stats, timeline/process composition, CTA blocks, Product UI, Supplier UI, Market UI and utility states;
- Product / Supplier / Market / Certification / Resource / RFQ / Alert samples;
- Language and Market shown as separate concepts;
- buyer customization ownership map;
- Do / Don’t guidance and known backfit findings;
- visible Demo / QA-laboratory boundary.

## Runtime / Truthfulness
PASS:
- `origex-components-lab.js` measures current computed dimensions without mutating global component contracts;
- local Demo form only; zero network submission;
- no `fetch`, XHR, `localStorage` or `sessionStorage` dependency;
- Bootstrap modal behavior used without inventing a new C01–C28 component ID.

## Rendered QA
Final matrix: **8 / 8 PASS**.

Viewports:
- Arabic RTL: 390 / 820 / 1366 / 1536;
- English LTR: 390 / 820 / 1366 / 1536.

Final document-overflow result: **0** at all eight cases.

Interaction suites:
- Arabic desktop: PASS;
- Arabic mobile: PASS;
- English desktop: PASS;
- English mobile: PASS;
- Mega Menu open / Escape: PASS;
- Mobile Drawer open / close: PASS;
- Tabs keyboard behavior: PASS;
- Accordion behavior: PASS;
- Demo form state: PASS;
- Bootstrap modal open / dismissal: PASS using an accessible alternate dismiss control;
- reciprocal language route: PASS.

## Root-Cause Corrections During PG32 QA
PG32 acted as intended and exposed shared/system defects rather than hiding them locally.

1. **N03 closed Mobile Drawer overflow**
   - 390px AR/EN overflow was traced to the transformed off-canvas drawer participating in document scroll width.
   - Corrected centrally in `origex-shell.css` using containment / clipping behavior rather than a PG32-only overflow hack.

2. **PG32 narrow form/file specimen containment**
   - Native file-input / form-track overflow was corrected in the PG32 specimen-composition layer without overriding the reusable form component contract.

3. **Modal QA semantics**
   - Interaction verification was hardened so test correctness does not depend on brittle auto-scroll / floating-control click geometry.
   - Final isolated V4 gate confirms dismissal behavior in both languages.

## Dimension Diagnostic Result
The QA laboratory correctly reports current shared-system reconciliation targets. Examples remain visible as `BACKFIT` where the active reusable component does not yet meet the frozen target tier.

This evidence is an input to the approved systemic backfit; it is not silently patched in PG32.

## Global Gates
- Global Navigation V1: PASS.
- Global Footer V1: PASS.
- F05 Icon Integrity after PG32: **66 AR/EN pages / 0 missing sprite references**.
- Final PG32 isolated gate: **PASS**.

## Evidence
- `qa/pg32-components/run-status.txt` → `PASS`.
- `qa/pg32-components/source-report.json` → failures `[]`.
- `qa/pg32-components/rendered-report.json` → failures `[]`, 8/8 rendered PASS, all interaction suites PASS.
- Final isolated V4 evidence commit: `95d8cf97557b2787fca293bb2f661d1481101787`.
- Final gate source revision: `9dcb46877d23b65e2f2f2406cb50ec22f81d6a04`.

## PS8 Boundary
PG32 is **not** promoted to PS8 by this report. PS8 remains deployed Cloudflare browser acceptance under the product governance model.

## Next Gate
PG32 completes the V1 page-production sequence at PS7. Proceed to:

`Systemic Backfit → Global AR/EN Regression → Sequential PG01→PG33 Second-Pass Review → M7 Full QA / Optimization`

Copyright © ORVEAX.
