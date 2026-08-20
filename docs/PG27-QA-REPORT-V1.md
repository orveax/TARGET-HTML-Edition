# ORIGEX — PG27 Contact | QA Report V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Page: PG27 — Contact  
Canonical file: `contact.html`  
Final page stage: **PS7 — IMPLEMENTED / CI QA PASS — AR+EN**

## 1. Authority
Canonical content:
- Arabic Master PG27: `اختر قناة التواصل المناسبة لطلبك.`
- English Adaptation PG27: `Choose the right contact route for your enquiry.`
- Frozen V1 scope: contact channels, departments, enquiry form, address, business hours, social links, map placeholder and CTA.

Frozen implementation contract:
- `docs/page-design-profiles/pg27-contact-v1.md`

## 2. Implemented Surface
- `ar/contact.html`
- `en/contact.html`
- `assets/css/origex-contact.css`
- `assets/js/origex-contact.js`
- `.github/scripts/qa_pg27_contact.py`
- `.github/scripts/qa_pg27_contact_ci.py`
- `.github/workflows/pg27-contact-qa.yml`

## 3. Contact Routing
Stable routes:
- `general` → general trade contact
- `rfq` → Buyer & RFQ
- `supplier` → Supplier Submissions
- `partner` → Partnerships / Distribution

The page supports normalized `?topic=` state and preserves the selected route across Arabic/English desktop and mobile language links.

Contact values are not duplicated business facts. They consume the existing `config.js` / `config-engine.js` hooks for:
- trade / RFQ / suppliers / partners email
- phone
- address
- business hours
- social links

## 4. Demo / Claim Safety
The enquiry form is validation-only in the commercial Demo package.

Verified boundaries:
- no `fetch` / XHR / CRM / external form provider;
- no generated ticket/reference number;
- no message-sent or message-received claim;
- no response-time SLA;
- no verified-office/location claim from Demo content;
- no embedded map provider or fabricated coordinates;
- social links remain hidden while config URLs remain `#`;
- JSON-LD remains WebPage + BreadcrumbList only, with no fictional LocalBusiness / Organization / ContactPoint claims.

## 5. Initial QA Findings and Corrections
The first QA cycle correctly exposed two real accessibility/touch defects:
1. the main phone link did not meet the page touch-target floor;
2. the consent checkbox rendered below the page touch-target floor.

Both were corrected in `assets/css/origex-contact.css` rather than ignored by QA.

The first source checker also contained two false-positive expectations:
- the readiness marker was written through `dataset` rather than as a literal source string;
- the negative disclosure `No guaranteed response time` was incorrectly matched as a positive response guarantee.

The QA assertions were corrected rather than weakening the page content.

A subsequent headless-Chrome pointer-scroll issue affected only the reset-button click after success/focus changes. Responsive hit-area checks were already clean and form behavior itself was correct. QA was therefore refactored into a maintainable standalone runner, with reset activation exercised by keyboard Enter in CI while the public button touch target remains independently verified across all responsive cases.

## 6. Final QA Evidence
Evidence commit:
- `7cfffde78233c087ee2381247470bb024d3689e1`

Final status:
- `qa/pg27-contact/run-status.txt` → **PASS**

Source / config / runtime:
- AR failures: **0**
- EN failures: **0**
- runtime failures: **0**
- config failures: **0**
- routes: **4 / 4 canonical routes**
- form field contract: PASS

Rendered responsive matrix:
- AR 390: PASS
- AR 820: PASS
- AR 1366: PASS
- AR 1536: PASS
- EN 390: PASS
- EN 820: PASS
- EN 1366: PASS
- EN 1536: PASS

Rendered total: **8/8 PASS**.

Interaction groups:
- AR route: PASS
- AR query/language: PASS
- AR invalid topic: PASS
- AR form: PASS
- EN route: PASS
- EN query/language: PASS
- EN invalid topic: PASS
- EN form: PASS

## 7. Shared-System Gates
- Global Navigation V1: PASS / centrally normalized.
- Global Footer V1: PASS / centrally normalized.
- F05 Icon Integrity after PG27: **56 AR/EN pages / 0 missing sprite references**.
- No TARGET/client-specific leakage detected.

## 8. Decision
**PG27 is promoted to PS7 — IMPLEMENTED / CI QA PASS — AR+EN.**

PS8 is not claimed here. Deployed Cloudflare browser acceptance remains the separate final page-acceptance gate.

Next sequential production page: **PG28 — 404**.

Copyright © ORVEAX.
