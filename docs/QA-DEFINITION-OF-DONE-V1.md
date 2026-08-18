# ORIGEX — QA Definition of Done V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & FROZEN  
Approval Date: 2026-08-19

A page is not considered closed until all applicable checks below pass.

## Page Gate

1. Content Contract exists and follows `CONTENT-SYSTEM-V1.md`.
2. Content reached C6 — FROZEN before implementation.
3. Arabic master copy is complete for approved Main Features.
4. English adaptation is complete and commercially equivalent, not merely literal translation.
5. Required demo/factual/legal disclaimers are present.
6. Canonical demo entities and values match `DEMO-CONTENT-DATASET-V1.md` and `DATA-SCHEMA-V1.md`.
7. Primary/secondary CTA wording follows the approved CTA vocabulary or has a documented exception.
8. Required empty/loading/success/error/validation microcopy exists where applicable.
9. Page Design Profile completed.
10. Registered components/variants only.
11. Arabic RTL layout pass.
12. English LTR layout pass.
13. Mobile pass at 360 / 390 / 412 widths.
14. Tablet pass at 768 / 820 widths.
15. Desktop pass at representative 1024+ widths.
16. No horizontal overflow.
17. Header/footer/navigation integration correct.
18. Keyboard navigation pass for interactive elements.
19. Visible focus states present.
20. Forms/controls have semantic labels and states.
21. ARIA/state sync correct where native HTML is insufficient.
22. `prefers-reduced-motion` behavior respected.
23. No console errors from ORIGEX code.
24. No broken internal links/assets.
25. Images/media use approved frames and ratios.
26. Asset/license status logged where applicable.
27. No TARGET/client identity or proprietary asset leakage.
28. Page-specific CSS does not fork shared components.
29. No temporary hotfix files or unresolved inline patches.
30. Search/filter/tabs/accordion/form behavior passes where present.
31. Empty/error/success states exist where required by the approved feature.
32. SEO baseline present: title/meta, correct lang/dir, canonical/hreflang placeholders as applicable.
33. Documentation entry updated where buyer behavior/configuration changed.
34. Responsive content order reviewed independently in AR and EN.
35. Performance review: no unnecessary dependency, duplicate CSS/JS, raw oversized media or blocking optional script.
36. Cross-browser smoke test on supported modern browser set before milestone closure.
37. Content Status moves from C7 — Implemented to C8 — QA Passed.
38. Page status explicitly changed to CLOSED/PASS in project tracking.

## Content Gate

A content unit is considered implementation-ready only at C6 — FROZEN.

Required checks:
- audience and commercial goal are explicit.
- primary user question is answered.
- Arabic master is reviewed.
- English adaptation preserves the same facts, promise and action.
- unsupported quality/performance claims are removed.
- demo facts are disclosed as illustrative where needed.
- product/supplier/market values are internally consistent.
- CTA is explicit and appropriate to the user decision.
- labels/microcopy/states are complete.
- legal/demo text exists where required.
- content length has been reviewed against the intended component/layout.

Additional Features use this same gate. A feature is not “ready” because UI copy has been improvised inside code.

## Component Gate

A component is considered registry-ready only when:
- hierarchy/purpose documented.
- anatomy documented.
- approved variants documented.
- default/hover/focus/disabled/active states defined where applicable.
- RTL/LTR behavior defined.
- responsive behavior defined.
- accessibility behavior defined.
- sample markup exists.
- sample content follows the canonical Content System.
- no page-specific dependency is required for its core appearance.

## Milestone Gate

A milestone closes only when:
- every listed deliverable exists.
- applicable Content/Page/Component Gates pass.
- critical and high-severity defects are zero.
- documentation and tracking are updated.
- unresolved scope additions are moved to backlog/change control rather than silently implemented.

## Reopen Rules

A closed page/component/content unit may reopen only for:
- verified bug.
- accessibility defect.
- responsive/RTL defect.
- performance regression.
- verified factual/content correction.
- approved commercial-message correction.
- formal Design System / Architecture / Scope Change Request.

Preference or visual experimentation alone does not reopen a closed item.

## Severity

- Critical: blocks use, navigation, submission candidate, or causes major broken layout/data loss/misleading commercial claim.
- High: major UI/RTL/responsive/accessibility/content-consistency failure without a reasonable workaround.
- Medium: visible issue with workaround or localized quality impact.
- Low: polish issue that does not impair use.

Submission Candidate requires zero Critical and zero High defects.

Copyright © ORVEAX.
