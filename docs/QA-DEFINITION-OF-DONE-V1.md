# ORIGEX — QA Definition of Done V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & FROZEN  
Approval Date: 2026-08-19

A page is not considered closed until all applicable checks below pass.

## Page Gate

1. Content complete for approved Main Features.
2. Page Design Profile completed.
3. Registered components/variants only.
4. Arabic RTL layout pass.
5. English LTR layout pass.
6. Mobile pass at 360 / 390 / 412 widths.
7. Tablet pass at 768 / 820 widths.
8. Desktop pass at representative 1024+ widths.
9. No horizontal overflow.
10. Header/footer/navigation integration correct.
11. Keyboard navigation pass for interactive elements.
12. Visible focus states present.
13. Forms/controls have semantic labels and states.
14. ARIA/state sync correct where native HTML is insufficient.
15. `prefers-reduced-motion` behavior respected.
16. No console errors from ORIGEX code.
17. No broken internal links/assets.
18. Images/media use approved frames and ratios.
19. Asset/license status logged where applicable.
20. No TARGET/client identity or proprietary asset leakage.
21. Page-specific CSS does not fork shared components.
22. No temporary hotfix files or unresolved inline patches.
23. Search/filter/tabs/accordion/form behavior passes where present.
24. Empty/error/success states exist where required by the approved feature.
25. SEO baseline present: title/meta, correct lang/dir, canonical/hreflang placeholders as applicable.
26. Documentation entry updated where buyer behavior/configuration changed.
27. Responsive content order reviewed independently in AR and EN.
28. Performance review: no unnecessary dependency, duplicate CSS/JS, raw oversized media or blocking optional script.
29. Cross-browser smoke test on supported modern browser set before milestone closure.
30. Page status explicitly changed to CLOSED/PASS in project tracking.

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
- no page-specific dependency is required for its core appearance.

## Milestone Gate

A milestone closes only when:
- every listed deliverable exists.
- applicable Page/Component Gates pass.
- critical and high-severity defects are zero.
- documentation and tracking are updated.
- unresolved scope additions are moved to backlog/change control rather than silently implemented.

## Reopen Rules

A closed page/component may reopen only for:
- verified bug.
- accessibility defect.
- responsive/RTL defect.
- performance regression.
- approved content correction.
- formal Design System / Architecture / Scope Change Request.

Preference or visual experimentation alone does not reopen a closed item.

## Severity

- Critical: blocks use, navigation, submission candidate, or causes major broken layout/data loss.
- High: major UI/RTL/responsive/accessibility failure without a reasonable workaround.
- Medium: visible issue with workaround or localized quality impact.
- Low: polish issue that does not impair use.

Submission Candidate requires zero Critical and zero High defects.

Copyright © ORVEAX.