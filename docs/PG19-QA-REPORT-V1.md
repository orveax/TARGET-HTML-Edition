# ORIGEX — PG19 Become Distributor / Partner | QA Report V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Page: PG19 — Become Distributor / Partner  
Current Gate: **PS7 — IMPLEMENTED / CI QA PASS**  
Date: 2026-08-20

## Build Evidence

- Arabic: `ar/become-partner.html`
- English: `en/become-partner.html`
- Page Design Profile: `docs/page-design-profiles/pg19-become-partner-v1.md`
- Composition: `assets/css/origex-partner.css`
- Runtime: `assets/js/origex-partner.js`
- Canonical market data: `assets/data/markets.json`
- QA workflow: `.github/workflows/pg19-partner-qa.yml`

## Canonical Functionality

PG19 implements the frozen V1 partnership flow:
- partnership value;
- qualification criteria;
- company profile form;
- primary market / territory selection;
- coverage description;
- sales/distribution channel selection;
- product-category interest selection;
- operating capability / portfolio notes;
- optional portfolio upload UI;
- required consent;
- browser-only Demo confirmation.

The page does not create appointment, exclusivity, territory reservation, distribution rights, pricing, allocation or backend submission.

## Data / Runtime QA

Authority: `qa/pg19-partner/source-report.json`.

Final result:
- source failures: **0**;
- data failures: **0**;
- runtime failures: **0**;
- canonical markets loaded: **6**;
- market IDs unique: PASS;
- required AR/EN market properties: PASS;
- no localStorage/sessionStorage: PASS;
- no XHR / POST submission: PASS;
- file-type and 10 MB rules present: PASS;
- Global Navigation V1 drift check: PASS;
- Global Footer V1 drift check: PASS;
- TARGET/client leakage scan: PASS.

## Rendered Responsive QA

Authority: `qa/pg19-partner/rendered-report.json`.

| Language | 390 | 820 | 1366 | 1536 |
|---|---:|---:|---:|---:|
| Arabic RTL | PASS | PASS | PASS | PASS |
| English LTR | PASS | PASS | PASS | PASS |

Result: **8/8 PASS**.

Verified:
- no horizontal overflow;
- correct RTL/LTR direction;
- touch targets >=24px;
- desktop mega-menu open/Escape behavior;
- mobile drawer open/close behavior;
- six-page-section contract.

## Interaction QA

### Market Query
PASS in AR and EN:
- `?market=market-ae` preselects the correct Demo market;
- market summary becomes visible;
- valid market ID is preserved across language switching;
- invalid market ID does not silently fall back;
- invalid market query produces visible guidance.

### Group Validation
PASS in AR and EN:
- form success is blocked when no channel is selected;
- form success is blocked when no category is selected;
- channel/category errors are exposed visibly;
- selecting at least one channel and one category permits Demo confirmation after native required fields and consent are valid;
- runtime QA state records the selected group counts.

### Portfolio File UI
PASS in AR and EN:
- invalid extension is rejected;
- valid PDF filename is displayed;
- no file is transmitted or persisted.

## Improvement / Shared Defect Closed

The first source gate found a shared F05 Icon System defect: distributed pages referenced `sprite.svg#message-circle` for the floating WhatsApp control, but the symbol was absent from the canonical sprite.

Resolution:
- central F05 fix: `assets/icons/sprite.svg`;
- fix commit: `6af5333ac397fb2895c12fc1d5074de0388d14fe`;
- no page-local icon workaround was introduced.

A permanent global icon-integrity gate was also added:
- workflow: `.github/workflows/global-icon-integrity-qa.yml`;
- workflow commit: `d5e1dcdc3a2f740570b4cbd3bf42f4a022ac256d`;
- evidence: `qa/global-icon-integrity/`;
- current coverage: **40 AR/EN pages**;
- registered symbols: **33**;
- referenced symbols: **28**;
- missing references: **0**;
- status: **PASS**.

## Final Evidence

- first diagnostic evidence: `9c7439f8502109361638bfe4d79c08c1666a042c` — correctly failed on the shared missing icon;
- final PG19 evidence: `599b6854eb20555ddb5c6f7b3068e9cd1361f2a0` — PASS;
- page profile promotion: `290e3171e0d43502082a9fb2ecd161a485f947fd`.

## Gate Decision

**PG19 = PS7 / IMPLEMENTED / CI QA PASS — AR+EN.**

M4 page production is now code/CI complete for PG09–PG13 and PG16–PG19. M4 remains open until its required deployed Cloudflare PS8 acceptance is completed. Page production may continue into M5 under the approved parallel-PS8 governance rule.

Copyright © ORVEAX.
