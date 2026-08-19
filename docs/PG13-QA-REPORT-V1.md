# ORIGEX — PG13 Supplier / Brand Details | QA Report V1

**Product:** ORX-P01  
**Milestone:** M4 — Product / Supplier / Conversion  
**Page:** PG13 — Supplier / Brand Details  
**Canonical file:** `supplier-details.html`  
**Current gate:** BUILD IMPLEMENTED / SOURCE + DATA QA PASS / RENDERED QA PENDING

## 1. Build Evidence

- PS6 Page Design Profile: `docs/page-design-profiles/pg13-supplier-details-v1.md` — `8742eaa18700af79442029657fe5e874f29a2de5`
- Canonical Markets dataset: `assets/data/markets.json` — `9fdd7a423f398ba5c09eb9838a28b19a3401184c`
- Supplier market relations: `assets/data/suppliers.json` — `ea79dfd33987353638891213474183e9a20a710b`
- Composition: `assets/css/origex-supplier-details.css` — initial `a8eae4f7d8b6a89f0a67858a9796533b3694791c`, UX refinement `8d32df40fd869549080a377a4f88073ad17f4551`
- Runtime: `assets/js/origex-supplier-details.js` — `819d6f372ec53ed5365822784085f919786a6f38`
- English: `en/supplier-details.html` — build `23786c819030cb7e1bc678f15980e21dec01e00b`, navigation alignment `5caef1625337c5b28bb27c1ef1ded1eda3ce832b`
- Arabic: `ar/supplier-details.html` — build `a654f526302bb90aebfc45f4a6c85cba8291c508`, navigation alignment `44f485be1a2047d43823a8ea11848deb539a0651`
- Source evidence: `qa/pg13-supplier-details/source-report.json` — initial `b076c19c90c8690e0b9e54ba98bca428323128bd`
- Gate status: `qa/pg13-supplier-details/run-status.txt`

## 2. Data Contract Completion — Improvement Added During Build

`docs/DATA-SCHEMA-V1.md` already declared `assets/data/markets.json` as a canonical structured-data domain, but that file did not exist in the repository before PG13.

PG13 closed that implementation gap without changing the approved schema:

- Added six fictional / illustrative GCC market records: Qatar, Saudi Arabia, UAE, Kuwait, Bahrain and Oman.
- Reused the existing `marketIds` field in `suppliers.json`.
- Linked all four demo suppliers to three illustrative markets each.
- No market relation represents distribution rights, exclusivity, registration, representation or a live commercial relationship.

This is a backward-compatible data completion, not an Architecture Change Request.

## 3. Data Integrity QA

PASS:

- 4 supplier records.
- 12 product records.
- 6 market records.
- 12 supplier → product relation references checked.
- Missing supplier → product relations: 0.
- 12 supplier → market relation references checked.
- Missing supplier → market relations: 0.
- Default supplier `supplier-noura` exists.
- Product records remain canonical in `products.json`; no duplicate supplier-level product objects were introduced.
- Market records remain canonical in `markets.json`; no duplicated market objects were introduced in supplier records.

## 4. Source / Page Contract QA

Arabic and English source review PASS for:

- one semantic H1 per page;
- correct `lang` and `dir` (`ar/rtl`, `en/ltr`);
- no duplicate HTML IDs found in the source review;
- self canonical;
- AR / EN / x-default hreflang;
- Open Graph baseline;
- WebPage JSON-LD;
- BreadcrumbList JSON-LD;
- demo Organization JSON-LD with no Offer, rating, verified certification, legal identifier or territory-right claims;
- canonical data hooks for suppliers, products and markets;
- visible loading, error, noscript and disclosure states;
- Supplier family parent navigation state;
- supplier ID language-preservation runtime hook;
- product-detail and RFQ route generation;
- category deep links to the existing products grid.

## 5. Runtime Contract QA

Source-level runtime inspection PASS:

- Vanilla JavaScript only.
- Parallel load of `suppliers.json`, `products.json`, `markets.json`.
- `?id=<supplier-id>` active-supplier contract.
- Missing / invalid supplier ID visibly falls back to `supplier-noura` rather than fabricating a record.
- Active supplier ID is preserved on the language switch.
- Header CTA remains structurally canonical; PG13 runtime may update its RFQ query after supplier resolution.
- Linked products resolve from the canonical product dataset.
- Linked markets resolve from the canonical market dataset.
- Certification IDs render as Demo references only.
- Organization JSON-LD updates from the selected fictional record without commercial rights or ecommerce claims.

## 6. Navigation Governance Defect Found and Corrected

During QA, the initial PG13 build placed the supplier query directly into the static Global Header CTA. The page worked, but this created structural drift from `GLOBAL-NAVIGATION-CONTRACT-V1` / `normalize_global_navigation.py`.

Correction:

- Restored the static header CTA to the canonical `rfq.html` + `data-orx-header-cta` structure in AR and EN.
- Kept supplier query synchronization inside the PG13 runtime after data resolution.
- Supplier Details already exists in the centralized navigation family mapping and correctly inherits `Suppliers` / `Suppliers & Brands` as its parent current state.

This removes page-local navigation drift while preserving the supplier-aware conversion route.

## 7. UX Improvements Added During Build

Two non-scope-expanding refinements were added:

1. **Category touch targets** — category links now have a larger minimum interaction height and padding for clearer mobile/tablet interaction.
2. **Market information density** — the market block becomes a three-column grid on suitable widths while remaining single-column on smaller screens.

These changes improve usability and information scanning without adding new product features or changing the data contract.

## 8. QA Not Yet Claimed

The following are **not yet marked PASS**:

- rendered AR/EN QA at 390 / 820 / 1366 / 1536;
- horizontal overflow inspection in a real browser;
- computed touch-target dimensions;
- runtime supplier switch to another supplier such as `supplier-nordvale`;
- invalid-ID fallback observation in a rendered browser;
- language switch query preservation in a rendered browser;
- keyboard / mobile drawer / mega-menu interaction observation;
- final deployed Cloudflare browser acceptance.

The available execution environment could not clone / resolve GitHub for a browser-based local checkout, so source/data QA is intentionally separated from rendered acceptance.

## 9. Current Decision

**Do not promote PG13 to PS7 yet.**

Current status:

`PS6 / BUILD IMPLEMENTED / DATA + SOURCE QA PASS / RENDERED-RESPONSIVE QA PENDING`

## 10. Next Gate

Run rendered QA for AR + EN at 390 / 820 / 1366 / 1536 and verify:

- no horizontal overflow;
- category and CTA touch targets;
- Noura default load;
- `supplier-nordvale` switch;
- invalid supplier fallback;
- product relation cards and routes;
- market relation cards;
- certification empty/non-empty states;
- active supplier preserved across language switch;
- Supplier parent current-state in desktop and mobile navigation;
- RFQ query synchronization;
- keyboard interaction.

After those pass, promote PG13 to **PS7 / CI QA PASS**. Cloudflare deployed-browser review remains required before PS8.
