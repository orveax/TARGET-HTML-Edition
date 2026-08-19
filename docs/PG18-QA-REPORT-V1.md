# ORIGEX — PG18 RFQ / Request a Quote | QA Report V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Page: PG18 — RFQ / Request a Quote  
Canonical file: `rfq.html`  
Final gate: **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**  
Date: 2026-08-20

## 1. Build Evidence

- PS6 profile: `docs/page-design-profiles/pg18-rfq-v1.md` — initial commit `c17266235168c1671a3dc85a10de9a206e99c098`.
- Composition: `assets/css/origex-rfq.css` — initial commit `202ebde1e726056dabd777dc8fccaa5235783664`.
- Runtime: `assets/js/origex-rfq.js` — `a87838202d1cd5b52c1e89817efa5ac621c577b8`.
- English: `en/rfq.html` — `e3f4456a33e26b6c427bd5177af7e0ed67e87411`.
- Arabic: `ar/rfq.html` — `76ebefb190b7f5768a3290b381d756018bd1541d`.
- Canonical QA gate: `.github/workflows/pg18-rfq-regression-qa.yml` — `b222e8afbe147ad6e4f305a9a232fd850cd19cca`.
- Final regression evidence: `016e76e8b620a69c8041d9fc19321ad625ed345d` plus synchronized final evidence `0b3dec61a1a7ac861deca6018e6ca97f6420eabc`.
- PS7 promotion: `5cea82f2f3ded2ea277350c9aec29ce1c4545c8b`.

## 2. Frozen RFQ Scope

The page implements the frozen V1 RFQ contract only:

1. Buyer details
2. Product selection
3. Quantity + quantity unit
4. Destination / port / city
5. Target timing
6. Notes / specifications
7. One optional attachment
8. Required consent
9. Validation
10. Browser-only confirmation state

No price engine, live quotation, cart, checkout, payment, stock reservation, automatic quotation number, CRM submission, server upload or delivery promise was added.

## 3. Product Context Improvement

PG18 closes the Product Details → RFQ path instead of forcing the buyer to select the product again.

- Runtime reads the canonical local `assets/data/products.json` dataset.
- `?product=<product-id>` preselects a valid product.
- The selected product is summarized using category, origin and pack information.
- A valid product ID is preserved when switching AR ↔ EN.
- An invalid ID does not silently substitute another product; the selector stays empty and the page shows neutral guidance.

This keeps PG11 and PG18 on the same product relationship without duplicating product data.

## 4. Demo / Network Safety

PASS:

- product selector may fetch only the local `products.json` file;
- form submit is intercepted in the browser;
- no POST/PUT/PATCH/DELETE submission exists;
- no XHR, localStorage or sessionStorage persistence exists;
- attachment selection remains local UI only;
- no price or request number is generated;
- success copy explicitly states that nothing was transmitted or stored.

## 5. Source / Data / Runtime QA

Final `qa/pg18-rfq/source-report.json`:

- total failures: **0**
- Arabic page failures: **0**
- English page failures: **0**
- product dataset: **12 Demo products**
- duplicate product IDs: **0**
- runtime safety failures: **0**

Verified contracts include AR/EN language and direction, H1, frozen section order, required fields, file contract, status semantics, Global Footer V1 and no TARGET/client leakage.

## 6. Rendered / Responsive QA

Final `qa/pg18-rfq/rendered-report.json`:

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
- RTL/LTR direction;
- product selector loads 12 Demo products + placeholder;
- interactive controls meet the touch-target floor after the shared-shell correction.

## 7. Interaction QA

Final interaction failures are empty for:

- `en-query`
- `ar-query`
- `en-validation`
- `ar-validation`
- `en-file`
- `ar-file`

This validates product query hydration, language preservation, invalid-ID safety, required fields, keyboard consent, Demo confirmation, expected local-data network boundary, invalid file rejection and valid filename state.

## 8. Shared-Shell Improvement Discovered During PG18

The first rendered gate reported exactly one undersized anchor in every AR/EN viewport. The first assumption was the consent checkbox, so its non-shrink behavior was strengthened in `0d3fd234d6c271150527514d81bb4c195dc619c1`.

A more diagnostic rerun then identified the remaining element as a small icon-only anchor. Review showed a structural gap in the M1 shell: distributed pages expose `orx-whatsapp` and `orx-back-to-top` directly, while the 44–48px floating hit-area contract had only been defined for children of `.orx-floating`.

The correction was made centrally in `assets/css/origex-shell.css`:

- direct WhatsApp utility: 48px desktop / 44px mobile;
- direct Back-to-Top utility: 48px desktop / 44px mobile;
- fixed non-overlapping positions;
- shared border/background/shadow/hit-area treatment.

Central fix commit: `2bb66bb15cde77511d5436a0ca73f6b88c7f5bd0`.

The subsequent PG18 rerun passed all eight viewports with zero touch-target failures. This is a reusable M1 shell improvement, not a PG18-only patch.

## 9. Global Footer / Shared Shell

N04 Global Footer V1 remains enforced across **38 AR/EN pages** with **0 failures**, including both RFQ pages.

The temporary/superseded PG18 workflow was removed, and PG18 now retains one canonical fast regression workflow to avoid duplicate QA noise.

## 10. Final Decision

`qa/pg18-rfq/run-status.txt` = **PASS**.

PG18 is promoted to:

**PS7 / IMPLEMENTED / CI QA PASS — AR+EN**

Cloudflare deployed-browser acceptance remains the separate PS8 gate.

## 11. Next M4 Page

**PG19 — Become Distributor / Partner**.

PG19 should reuse the same Global Navigation V1, Global Footer V1, form-safety policy and corrected floating utility contract.

Copyright © ORVEAX.
