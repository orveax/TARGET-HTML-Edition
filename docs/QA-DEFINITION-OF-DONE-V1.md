# ORIGEX — QA Definition of Done V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & FROZEN — STAGING GATE AMENDMENT 2026-08-19  
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
10. SEO & Page Identity Contract completed.
11. Registered components/variants only.
12. Arabic RTL layout pass.
13. English LTR layout pass.
14. Mobile pass at 360 / 390 / 412 widths.
15. Tablet pass at 768 / 820 widths.
16. Desktop pass at representative 1024+ widths.
17. No horizontal overflow.
18. Header/footer/navigation integration correct.
19. Keyboard navigation pass for interactive elements.
20. Visible focus states present.
21. Forms/controls have semantic labels and states.
22. ARIA/state sync correct where native HTML is insufficient.
23. `prefers-reduced-motion` behavior respected.
24. No console errors from ORIGEX code.
25. No broken internal links/assets.
26. Images/media use approved frames and ratios.
27. Asset/license status logged where applicable.
28. No TARGET/client identity or proprietary asset leakage.
29. Page-specific CSS does not fork shared components.
30. No temporary hotfix files or unresolved inline patches.
31. Search/filter/tabs/accordion/form behavior passes where present.
32. Empty/error/success states exist where required by the approved feature.
33. SEO/metadata baseline passes the dedicated SEO Gate below.
34. Documentation entry updated where buyer behavior/configuration changed.
35. Responsive content order reviewed independently in AR and EN.
36. Performance review: no unnecessary dependency, duplicate CSS/JS, raw oversized media or blocking optional script.
37. Cross-browser smoke test on supported modern browser set before milestone closure.
38. Content Status moves from C7 — Implemented to C8 — QA Passed.
39. Page status explicitly changed to CLOSED/PASS in project tracking.

## Staging Preview Gate

Authority: `STAGING-PREVIEW-GATE-V1.md`.

C8 / PASS / CLOSED means page implementation and page QA have passed. It does not by itself prove that the page is reachable through an external browser URL.

Before a page is described as staging-ready, used for owner browser review, or used as the benchmark that authorizes coding of the next page in the same family:
- a staging target must be enabled and configured.
- deployment must originate from canonical `main`.
- root `/` must resolve and provide the approved language-entry behavior.
- AR and EN deployed routes must resolve.
- deployed CSS/JS/fonts/icons/patterns/assets must load from the real deployment base path.
- the staging artifact must exclude internal `docs/`, `qa/` and `.github/` content.
- staging indexability must be explicit; default is `noindex` unless separately approved.
- at least one external mobile and one external desktop browser smoke check must pass.
- AR RTL and EN LTR must both be opened via the deployed URL.
- deployment source commit, run result and generated URL must be recorded.

For the first representative page in each milestone/page family, this gate must pass before the next page in that family enters code implementation. Content/design/SEO preparation for the next page may continue while staging is blocked.

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

## SEO / Metadata Gate

Authority: `SEO-METADATA-PAGE-NAMING-V1.md`.

A page passes SEO/metadata QA only when:
- page ID matches the canonical PG registry.
- filename/slug matches the locked naming system.
- `html[lang]` and `dir` are correct.
- H1 is unique and aligned with page intent.
- SEO title exists in AR and EN and is unique within the relevant language set.
- meta description exists in AR and EN and is page-specific.
- canonical placeholder/value points to the correct language URL strategy.
- hreflang AR/EN relationship is reciprocal where implemented.
- x-default strategy is documented where applicable.
- Open Graph title/description/image strategy is present for public pages.
- structured data, when used, matches visible content and contains no fabricated claims.
- breadcrumb labels and internal links use descriptive wording.
- indexability state is explicit: INDEX / NOINDEX / ENVIRONMENT-DEPENDENT.
- demo pages follow `DEMO-VS-PRODUCTION-POLICY-V1.md` and do not hard-code ORIGEX preview values as buyer production values.

## Demo / Production Gate

Authority: `DEMO-VS-PRODUCTION-POLICY-V1.md`.

Before package/release closure:
- demo-only contact/domain values are identified.
- preview-only assets are disclosed and excluded from buyer ZIP unless redistribution rights are documented.
- fictional demo claims are not presented as verified real-world endorsements.
- no client/personal data, credentials, analytics IDs or private endpoints remain.
- buyer-facing documentation includes a `Before You Publish` replacement checklist.
- production SEO/config values are replaceable and not tied to the live demo domain.

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
- applicable Content/Page/SEO/Demo/Component/Staging Preview Gates pass.
- critical and high-severity defects are zero.
- documentation and tracking are updated.
- unresolved scope additions are moved to backlog/change control rather than silently implemented.

## Release Gate

Authority: `RELEASE-VERSIONING-POLICY-V1.md`.

A public package/release requires:
- QA gates passed for the release scope.
- zero Critical and zero High defects.
- correct MAJOR.MINOR.PATCH classification.
- changelog updated.
- version identifiers synchronized in buyer documentation/package metadata.
- changed assets/licenses reviewed.
- demo and buyer package synchronized where applicable.
- migration/deprecation notes added when a buyer-facing change requires them.

## Reopen Rules

A closed page/component/content unit may reopen only for:
- verified bug.
- accessibility defect.
- responsive/RTL defect.
- performance regression.
- verified factual/content correction.
- approved commercial-message correction.
- verified SEO/metadata defect.
- formal Design System / Architecture / Scope / Product Governance Change Request.

A staging/deployment failure does not automatically reopen C8 when the page code itself remains valid. It creates or reopens the independent Staging Preview Gate.

Preference or visual experimentation alone does not reopen a closed item.

## Severity

- Critical: blocks use, navigation, submission candidate, or causes major broken layout/data loss/misleading commercial claim.
- High: major UI/RTL/responsive/accessibility/content-consistency/SEO-indexability failure without a reasonable workaround.
- Medium: visible issue with workaround or localized quality impact.
- Low: polish issue that does not impair use.

Submission Candidate requires zero Critical and zero High defects.

Copyright © ORVEAX.
