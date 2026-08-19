# ORIGEX — Home Family Navigation Defect Fix

Product ID: ORX-P01  
Date: 2026-08-19  
Classification: Verified Global Navigation Defect / Controlled Foundation Fix  
Status: PASS / CLOSED

## Defect
PG02, PG03 and PG04 existed as approved M2 layouts but Home-family variants were not consistently discoverable through the shared navigation. Static N02/N03 markup predated the completed Home Family.

## Correction
Shared `assets/js/origex-ui.js` now hydrates the approved Home Family navigation centrally:

- `index.html` — Home 01 / Trading & Import
- `home-02.html` — Home 02 / Wholesale & Distribution
- `home-03.html` — Home 03 / Manufacturer & Supplier
- `landing.html` — Landing / One Page

Desktop N02 Mega Menu exposes the four variants on standard Home pages. Mobile N03 Drawer exposes the four variants on all Home-family pages. The current variant receives `aria-current="page"`.

PG04 intentionally retains its compact conversion-focused desktop header and does not gain a full Mega Menu. Its brand link returns to Home 01, while PG04 remains discoverable from the other Home Mega Menus and from all mobile drawers.

## Architecture Decision
The fix is centralized in the shared UI runtime rather than duplicating navigation markup across eight AR/EN files. No dependency, page family or V1 feature was added.

M1 remains CLOSED. This change is a controlled defect correction to the frozen navigation foundation, not a foundation redesign.

## QA
Reusable regression workflow: `.github/workflows/home-navigation-regression.yml`.

Evidence: `qa/home-navigation-regression/report.json` + `run-status.txt`.

Final result:
- failures: 0
- AR routes: 4/4 resolve
- EN routes: 4/4 resolve
- Home 01/02/03 desktop Mega Menu: four Home variants present, correct order, active state, open/Escape-close PASS
- All four mobile drawers: four Home variants present, correct order, active state, open/Escape-close PASS
- Landing desktop compact-header policy: PASS
- PG01 post-fix interaction regression: PASS / failures 0

Implementation commit: `eeb42ab69ff70ef67ed107700a5bddadfea34b8c`.
Navigation QA workflow correction: `3ef7211e04ec3f5ba374720507f8547c9e3c662d`.

Copyright © ORVEAX.
