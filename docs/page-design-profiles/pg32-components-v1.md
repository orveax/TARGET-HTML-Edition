# ORIGEX — PG32 Components / Elements Library | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Canonical file: `components.html`  
Status: **PS7 — IMPLEMENTED / CI QA PASS — AR+EN**

## Purpose
Create the final V1 Components / Elements Library as both a buyer-facing component reference and the ORIGEX Design System QA Laboratory. PG32 must demonstrate the frozen V1 component system with realistic B2B food-trading content, while intentionally exposing current systemic reconciliation targets instead of hiding them with page-local overrides.

## Canonical Content Authority
Arabic Master:
- H1: `مكونات ORIGEX بمحتوى واقعي جاهز للاختبار والتخصيص.`
- Support: `استعرض الأزرار، الكروت، النماذج، الجداول، الحالات، والأنماط باستخدام أمثلة تجارية من نفس تجربة القالب.`
- Samples: Product Card / Supplier Card / Market Card / Certification / Resource / RFQ / Alerts.

English Adaptation:
- H1: `ORIGEX components demonstrated with realistic, customization-ready content.`
- Samples: Product / Supplier / Market / Certification / Resource / RFQ / Alerts.
- English preserves Arabic commercial meaning and does not strengthen claims.

## Frozen V1 Main Features
Per `docs/SCOPE-FREEZE-V1-FINAL.md`:
- buttons;
- cards;
- badges;
- headings;
- tabs;
- accordions;
- forms;
- tables;
- alerts;
- stats;
- timelines;
- CTA blocks;
- product UI;
- supplier UI;
- market UI;
- utility states.

Scope reconciliation:
- Timeline is demonstrated by a sequential C05 Process Card composition. No new Timeline component ID is created.
- Overlay/modal proof uses local Bootstrap 5.3.8 behavior with ORIGEX primitives because the frozen C01–C28 registry has no modal component ID.
- Language and Market controls are demonstrated as separate concepts; Market selector uses registered P07 Select rather than inventing a new selector component family.

## PG32 Canonical Role
PG32 is the approved combination of:
1. Design System reference;
2. visual QA laboratory;
3. buyer component reference;
4. state matrix;
5. AR/EN + RTL/LTR test surface;
6. size / surface / contrast proof page.

It must expose inconsistency before release. Known VQ1 systemic gaps remain visible as `BACKFIT` findings where applicable. PG32 does not silently repair the whole system before the approved post-PG32 systemic backfit phase.

## Registry Coverage Contract
### Foundations F01–F07
Color, typography, spacing/layout, shape/elevation, Lucide icons, motion, media.

### Primitives P01–P11
Primary/secondary/text/icon actions, badges, input/select/textarea/check, divider, icon containers.

### Core Components C01–C28
All registered component families must be represented either as a rendered specimen or an explicit contract/reference specimen:
- C01–C11 commercial cards;
- C12–C17 navigation/disclosure/search/filter;
- C18–C22 data/trust/utility;
- C23–C25 form/file/status;
- C26–C28 media/logo/editorial.

### Sections S01–S06
Page composition must consume registered section/header/hero/final-CTA patterns and identify them in the buyer reference.

### Navigation N01–N04
The actual page shell demonstrates Header, Mega Menu, Mobile Drawer and Footer. No page-local navigation fork.

## Page Composition
1. Global Navigation V1 + announcement bar.
2. Breadcrumb + component-lab hero with canonical H1/support.
3. Demo / QA-laboratory boundary notice.
4. Buyer quick index and coverage summary.
5. Foundations & semantic surfaces.
6. Dimension diagnostics: target tier vs current computed component behavior.
7. Typography and heading hierarchy.
8. Primitive/state matrix: actions, badges, inputs, select, textarea, checkbox/radio, divider, icon containers.
9. Commercial card families: Feature, Product, Supplier, Market, Process, Metric, Certification, Resource, Case Study, Contact, CTA.
10. Tabs / Accordion / Pagination / Search / Filter / Breadcrumb interaction reference.
11. Data & trust: specification table, stat strip, trust item, empty state, alerts.
12. Forms: normal/help/error/disabled states, upload, success/error form statuses, RFQ Demo state.
13. Media: product frame, supplier logo frame, editorial frame + fallback guidance.
14. Localization & shell: Language vs Market separation, announcement, social/discovery config state, Mobile Drawer / Mega Menu references.
15. Overlay behavior specimen using Bootstrap modal + ORIGEX primitives; no new component ID.
16. Buyer customization map: config / tokens / data / page content ownership.
17. Do / Don’t examples and known systemic backfit findings.
18. Final CTA + Global Footer V1.

## Diagnostic Contract
PG32 may use small page-specific JavaScript only for QA/demo enhancement:
- read computed dimensions of selected registered controls;
- compare them with frozen target tiers;
- render `ALIGNED` or `BACKFIT` status without changing the component CSS;
- validate Demo form locally with zero network/storage;
- never rewrite global tokens/components from the page runtime.

Required diagnostic targets:
- default button target 48px;
- large button target 56px;
- icon button target 48×48px;
- input/select target 48px;
- textarea minimum 144px;
- checkbox/radio visual control 20px;
- upload minimum 144px;
- pagination/action target 48px where used.

The lab must detect current mismatches rather than cosmetically overriding them.

## Surface / Contrast Contract
Reference pairings must use semantic tokens and visibly distinguish:
- surface + primary text;
- soft surface + readable text;
- primary + white foreground;
- primary-strong + white foreground;
- accent reference with dark foreground target.

Known VQ1 color gaps may be labeled `BACKFIT`; PG32 does not present a low-contrast pair as approved.

## Forms / State Contract
Show at minimum:
- normal field;
- help text;
- required state;
- error anatomy with `aria-invalid` + associated message;
- disabled control;
- checkbox/radio;
- upload empty state;
- success form status;
- error form status;
- Demo submit route with zero fetch/XHR/storage.

## Structured Data / Table Contract
- Semantic `<table>` relationships preserved.
- PG32 reference tables use wrappers that allow internal horizontal scrolling when needed.
- No blanket mobile card conversion for relational data.
- Mixed LTR data inside Arabic remains readable.

## Localization Contract
- Arabic = RTL / Tajawal; English = LTR / Manrope.
- Language selector and Market selector are explicitly separate concepts.
- Language must never infer country/market.
- AR mixed data includes email, phone, SKU/unit and URL examples.
- Equivalent component/state coverage in AR and EN.

## Interaction Contract
Must verify:
- Mega Menu open / Escape;
- Mobile Drawer open / close;
- Tabs keyboard behavior;
- Accordion open / close;
- Bootstrap modal open / close / focus return where supported;
- Demo form local validation/status;
- language counterpart route;
- no network submission by PG32 runtime.

## SEO / Page Identity Contract
Classification: **INDEXABLE COMPONENT REFERENCE / DEMO CONTENT**.

AR:
- Title: `مكونات وعناصر ORIGEX | مكتبة التصميم`
- Meta: `مرجع مكونات ORIGEX بالعربية لعرض الأزرار والكروت والنماذج والجداول والحالات ومكونات التجارة الغذائية B2B.`
- Canonical: `https://example.com/ar/components.html`

EN:
- Title: `ORIGEX Components & Elements | Design System Library`
- Meta: `ORIGEX component reference demonstrating buttons, cards, forms, tables, states and B2B food-trading UI patterns.`
- Canonical: `https://example.com/en/components.html`

Both:
- reciprocal AR/EN/x-default alternates;
- WebPage + BreadcrumbList JSON-LD only;
- no Product/Offer/Review/Organization-performance claims;
- Demo content disclosure visible in body.

## CSS Ownership
- Existing global components remain in `origex-components.css`.
- PG32 may add `origex-components-lab.css` only for specimen composition, measurement/reference layouts, diagnostic badges and QA-lab presentation.
- PG32 CSS must not override registered `.orx-btn`, `.orx-card`, `.orx-input`, `.orx-tabs`, `.orx-accordion`, shell or media component anatomy.

## Runtime Ownership
- Existing interactions remain in `origex-ui.js` and Bootstrap bundle.
- `origex-components-lab.js` is limited to diagnostic display + local Demo form state.
- No fetch/XHR, localStorage, sessionStorage or remote dependency.

## PQE Adoption in PG32
PG32 provides first visible proof for:
- PQE-01 component contract coverage;
- PQE-02 dimension/color diagnostic surface;
- PQE-04 long/mixed/missing-state stress examples;
- PQE-06 progressive enhancement: core specimens/content remain understandable without page JS;
- PQE-07 buyer customization ownership map;
- PQE-13 Arabic optical QA surface;
- PQE-15 buyer reference value.

It does **not** claim the later systemic backfit, full M7 regression, PQS score or marketplace reviewer simulation are complete.

## Responsive / Accessibility Gate
Verify AR + EN at 390 / 820 / 1366 / 1536:
- no document horizontal overflow;
- specimen grids reflow without fixed-height clipping;
- 1 H1;
- heading hierarchy coherent;
- focus-visible available on interactive controls;
- tables scroll internally when needed;
- controls remain keyboard reachable;
- active/disabled/error/status meaning is not color-only;
- icons are registered through F05;
- reduced-motion foundation remains respected.

## PS7 Closure Evidence — 2026-08-20
PASS.

- Canonical AR H1 + Support: PASS.
- Canonical EN H1: PASS.
- Frozen PG32 Main Features represented: PASS.
- Registry coverage: 11/11 card families, 17/17 C12–C28 references, 11/11 primitives, 9/9 dimension diagnostics per language.
- Source / Content / Registry / Diagnostic failures: **0**.
- Rendered AR/EN × 390/820/1366/1536: **8/8 PASS**.
- Document horizontal overflow: **0** in all eight final cases.
- Mega Menu / Mobile Drawer / Tabs keyboard / Accordion / Demo form / Modal dismissal / language route: PASS.
- Runtime remains non-mutating and zero-network/storage.
- Global Navigation V1 + Global Footer V1: PASS.
- F05 Icon Integrity: **66 AR/EN pages / 0 missing sprite references**.
- Final isolated V4 gate: `95d8cf97557b2787fca293bb2f661d1481101787` → PASS.
- QA report: `docs/PG32-QA-REPORT-V1.md`.

### QA Root-Cause Findings
PG32 successfully exposed and helped close page-blocking issues at their correct ownership layer:
- N03 closed Mobile Drawer document-overflow defect corrected centrally in `origex-shell.css`.
- PG32 narrow specimen/form/file containment corrected in the lab composition layer without overriding reusable component contracts.
- Modal verification hardened against brittle auto-scroll geometry while preserving keyboard/accessibility checks.

### Diagnostic Outcome
The lab intentionally continues to report shared component dimension mismatches as `BACKFIT`. Those are not hidden or page-patched. They now become direct inputs to the approved post-PG32 **systemic backfit**.

## PS8 Boundary
PS8 remains deployed Cloudflare browser acceptance. PG32 is not claimed PS8 by this profile.

## Next Sequence
`Systemic Backfit → Global AR/EN Regression → Sequential PG01→PG33 Second-Pass Review → M7 Full QA / Optimization`

Copyright © ORVEAX.
