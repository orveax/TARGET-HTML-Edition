# ORIGEX — PG29 Coming Soon | QA Report V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Page: PG29 — Coming Soon / Under Construction  
Canonical file: `coming-soon.html`  
Status: **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**

## Final Result
PASS.

## Content / Scope
- Arabic canonical H1 PASS: `نجهز هذه الصفحة بمعلوماتها التجارية الكاملة.`
- Arabic support + Contact CTA intent PASS.
- English adaptation meaning parity PASS.
- Frozen V1 Main Features present: logo / status message / launch date-countdown / subscribe UI / social links / contact link.

## Prelaunch / Countdown Safety
- `ORIGEX_CONFIG.comingSoon.launchDate` is the only launch-date authority.
- Default config value is empty.
- Default state shows no fabricated countdown.
- Valid future configured date activates local days/hours/minutes/seconds countdown.
- Past configured date returns to a neutral review state and does not show a false active countdown.
- No network time service, browser storage or timezone claim.

## Subscribe UI Safety
- Demo validation only.
- Invalid email state PASS.
- Valid email Demo confirmation PASS.
- Reset state PASS.
- No form action, fetch, XHR, localStorage or sessionStorage.
- No subscription-created / CRM / subscriber-count claim.

## Social / Contact
- Placeholder `#` social URLs remain hidden.
- Configured public social URL becomes visible through the existing config layer.
- Placeholder restoration hides the social block again.
- Contact page link and configured email fallback PASS.

## SEO / Utility State
- `robots=noindex,follow` PASS.
- No canonical / hreflang requirement on the package utility asset.
- No JSON-LD / Event / fabricated launch structured data.
- Open Graph utility metadata present.

## Responsive / Interaction
Rendered browser matrix:
- Arabic 390: PASS
- Arabic 820: PASS
- Arabic 1366: PASS
- Arabic 1536: PASS
- English 390: PASS
- English 820: PASS
- English 1366: PASS
- English 1536: PASS

Interaction groups:
- AR countdown: PASS
- AR subscribe: PASS
- AR social: PASS
- EN countdown: PASS
- EN subscribe: PASS
- EN social: PASS

## Shared Gates
- Global Navigation V1: PASS.
- Global Footer V1: PASS.
- F05 Icon Integrity after PG29: **60 AR/EN pages / 0 missing sprite references**.
- TARGET/client leakage: 0.

## Evidence
- `qa/pg29-coming-soon/run-status.txt` = PASS.
- `qa/pg29-coming-soon/source-report.json` failures = 0.
- `qa/pg29-coming-soon/rendered-report.json` failures = 0.
- Final QA evidence commit: `cf91343ff95c66ba544387e26506c60076610f74`.
- F05 report: `qa/global-icon-integrity/report.json` = 60 pages / 0 missing references.

## PS8 Remaining Gate
Deployed browser acceptance remains required. PG29 PS8 must verify the actual buyer/demo configuration state and must not assume that a launch date or social URL has been configured.

## Next Sequential Page
PG30 — Privacy.

Copyright © ORVEAX.
