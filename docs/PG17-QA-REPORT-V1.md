# ORIGEX — PG17 Submit Your Product | QA Report V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Page: PG17 — Submit Your Product  
Canonical file: `submit-product.html`  
Final gate: **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**  
Date: 2026-08-20

## 1. Build Evidence

- PS6 Page Design Profile: `docs/page-design-profiles/pg17-submit-product-v1.md` — initial freeze `09aab106024189553b5c2ecf5d452ec5ba55125d`.
- Composition: `assets/css/origex-submit-product.css` — initial `6e139d4615da9efd0bcb08e4bb371c2c4501a0cf`.
- Runtime: `assets/js/origex-submit-product.js` — `47e540096e5494d4e9ea12682f82d9faf911be7d`.
- English page: `en/submit-product.html` — `f2d286335f65cbbcc849389b7998cd8a52894730`.
- Arabic page: `ar/submit-product.html` — `f79934ffe74bc703085794c49fcefd7f8e2f0ac6`.
- Automated QA workflow: `.github/workflows/pg17-submit-product-qa.yml` — initial `3f530250a888cca590211e1d6be320565575f25a`.
- Final PG17 evidence: `168d4d4b9687421fc0a6f73c3fc268bd94028fda`.
- PS7 promotion: `b778967d4b3fa6c28274ce974e5d07ef6fa97796`.

## 2. Frozen Conversion Flow

PG17 implements the V1 supplier product-submission route:

1. Hero / preparation summary.
2. Explicit demo/no-backend disclosure.
3. Company-information fields.
4. Product/category/origin/packaging/MOQ fields.
5. Optional storage/shelf-life/market/availability context.
6. Certification/compliance references.
7. Optional supporting-file UI.
8. Required consent.
9. Browser validation and accessible status.
10. Alternative route back to supplier preparation / supplier directory.

No account, supplier portal, CRM submission, server upload, database persistence, automatic verification/approval, fake upload progress or fake reference number exists in V1.

## 3. Form / Data Safety Contract

Required fields:
- company name;
- company role;
- contact name;
- business email;
- product name;
- category;
- country of origin;
- pack size;
- packaging/case configuration;
- MOQ / MOQ approach;
- explicit demo consent.

Optional supporting file:
- PDF;
- JPG/JPEG;
- PNG;
- DOC/DOCX;
- maximum 10 MB.

The runtime displays the selected local filename only. It does not transmit or persist the selected file.

## 4. Runtime Safety QA

`assets/js/origex-submit-product.js` passed the safety gate:

- no `fetch()`;
- no `XMLHttpRequest`;
- no `localStorage`;
- no `sessionStorage`;
- `event.preventDefault()` blocks real form submission;
- allowed extension whitelist is explicit;
- 10 MB size contract is explicit;
- invalid file resets the input and exposes an accessible error;
- valid demo submission exposes/focuses the success status.

Final runtime failures: **0**.

## 5. Source QA

Final `qa/pg17-submit-product/source-report.json`:

- overall failures: **0**;
- Arabic failures: **0**;
- English failures: **0**;
- runtime failures: **0**;
- exact page composition: hero / disclosure / form / review / CTA;
- single H1 per language;
- correct RTL/LTR;
- canonical + AR/EN/x-default hreflang;
- required field semantics PASS;
- upload accept-list PASS;
- accessible success/error status PASS;
- Supplier parent + Submit Product current navigation PASS;
- Global Navigation V1 PASS;
- Global Footer V1 PASS;
- no TARGET/client leakage.

The initial source QA falsely treated the negative phrase about `guaranteed entry` as an unsupported positive claim. The gate was corrected to require the explicit negative commercial boundary instead.

## 6. Rendered / Responsive QA

Final `qa/pg17-submit-product/rendered-report.json`:

- Arabic 390: PASS
- Arabic 820: PASS
- Arabic 1366: PASS
- Arabic 1536: PASS
- English 390: PASS
- English 820: PASS
- English 1366: PASS
- English 1536: PASS

**8/8 responsive cases PASS.**

Verified:
- no horizontal overflow;
- correct RTL/LTR direction;
- form and file control render once;
- Global Footer V1 / business-hours hook present;
- touch-target floor PASS;
- desktop mega-menu interaction PASS;
- mobile drawer interaction PASS.

## 7. Validation / Consent Interaction

The initial Selenium run used a native pointer click for the deep consent checkbox and produced `ElementClickInterceptedException`. The form itself had no overlay defect.

The QA was strengthened to follow keyboard accessibility behavior:

1. scroll consent to viewport center;
2. focus consent;
3. activate with `Space`;
4. verify selected state;
5. submit by keyboard;
6. verify the demo success status;
7. verify no Fetch/XHR network request occurred.

Final:
- EN validation + keyboard consent: PASS;
- AR validation + keyboard consent: PASS;
- empty form never reaches success: PASS;
- valid form reaches demo success: PASS;
- network requests: **0**.

## 8. File Interaction QA

Final:
- EN unsupported extension → accessible error: PASS;
- AR unsupported extension → accessible error: PASS;
- EN valid PDF filename state: PASS;
- AR valid PDF filename state: PASS.

The first rendered run also identified the consent input itself below the 24px visual touch-target floor. PG17 composition was corrected centrally for this page in `63d432bfbd95b7e58200928840fd5f93e800d9d6`; the final 8/8 responsive run passed.

## 9. Global Footer Hardening Triggered by PG17

PG17 exposed a concurrency edge case: Global Navigation and Global Footer bots could both normalize a newly created page and attempt to push to `main` at nearly the same time.

The Footer workflow was hardened with `git pull --rebase origin main` before push:
- workflow hardening: `11981d17f005be050e43f6e47e0cc9640e17a06f`;
- final PG17-inclusive footer normalization/evidence: `2ab90a97a439636a55505c1683e86aaa44cb78aa`.

Current Global Footer V1 result after PG17:
- **36 AR/EN pages checked**;
- **0 failures**;
- PASS.

## 10. Final Decision

`qa/pg17-submit-product/run-status.txt` = **PASS**.

PG17 is promoted to:

**PS7 / IMPLEMENTED / CI QA PASS — AR+EN**

Cloudflare deployed-browser acceptance remains a separate PS8 gate for the M4 batch.

## 11. Next M4 Page

**PG18 — Request a Quote / RFQ**.

PG18 should reuse the same global shell and form-safety principles while introducing buyer details, product selection, quantity, destination, target timing, notes, attachment UI, consent, validation and demo confirmation state.

Copyright © ORVEAX.