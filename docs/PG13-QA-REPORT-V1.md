# ORIGEX — PG13 Supplier / Brand Details | QA Report V1

**Product:** ORX-P01  
**Milestone:** M4 — Product / Supplier / Conversion  
**Page:** PG13 — Supplier / Brand Details  
**Canonical file:** `supplier-details.html`  
**Final CI gate:** **PS7 / IMPLEMENTED / DATA + SOURCE + RENDERED + INTERACTION QA PASS**  
**PS8:** Cloudflare deployed-browser acceptance still pending.

## 1. Build Evidence

- PS6 Page Design Profile: `docs/page-design-profiles/pg13-supplier-details-v1.md` — `8742eaa18700af79442029657fe5e874f29a2de5`
- Canonical Markets dataset: `assets/data/markets.json` — `9fdd7a423f398ba5c09eb9838a28b19a3401184c`
- Supplier market relations: `assets/data/suppliers.json` — `ea79dfd33987353638891213474183e9a20a710b`
- Composition: `assets/css/origex-supplier-details.css` — initial `a8eae4f7d8b6a89f0a67858a9796533b3694791c`, UX refinement `8d32df40fd869549080a377a4f88073ad17f4551`
- Runtime: `assets/js/origex-supplier-details.js` — initial `819d6f372ec53ed5365822784085f919786a6f38`, QA observability `43bab72f14e28c2978c06f3671e05c45d420bb45`
- English: build `23786c819030cb7e1bc678f15980e21dec01e00b`; navigation alignment `5caef1625337c5b28bb27c1ef1ded1eda3ce832b`; section QA hooks / final correction `401850aef97a6eadf00a8f293dab602be47d64c8` + `a89cf2f3c836b0dbc07b8a9b8313228370108150`
- Arabic: build `a654f526302bb90aebfc45f4a6c85cba8291c508`; navigation alignment `44f485be1a2047d43823a8ea11848deb539a0651`; section QA hooks `bb41d519845dcd55c2d38ab3621e70e3b876bee4`
- QA workflow: `.github/workflows/pg13-supplier-details-qa.yml` — `cacece8c9cc1883415d58eaf037da92dca52f253`
- Final QA evidence commit: `d16e8d86279de5242f15a71535248a40fe878c4c`

## 2. Data Contract Completion — Improvement Added During Build

`docs/DATA-SCHEMA-V1.md` already declared `assets/data/markets.json` as a canonical structured-data domain, but the repository did not contain the file before PG13.

PG13 closed that implementation gap without changing the approved schema:

- Added six fictional / illustrative GCC market records: Qatar, Saudi Arabia, UAE, Kuwait, Bahrain and Oman.
- Reused the existing `marketIds` field in `suppliers.json`.
- Linked all four demo suppliers to three illustrative markets each.
- No market relation represents distribution rights, exclusivity, registration, representation or a live commercial relationship.

This is a backward-compatible data completion, not an Architecture Change Request.

## 3. Data Integrity QA — PASS

- Suppliers: 4.
- Products: 12.
- Markets: 6.
- Supplier → product relations: 12; missing = 0.
- Supplier → market relations: 12; missing = 0.
- Default supplier `supplier-noura` exists.
- Product records remain canonical in `products.json`; no duplicate supplier-level product objects were introduced.
- Market records remain canonical in `markets.json`; no duplicated market objects were introduced in supplier records.

Canonical evidence: `qa/pg13-supplier-details/source-report.json` — failures 0.

## 4. Source / Page Contract QA — PASS

Arabic and English source checks pass for:

- one semantic H1;
- `ar/rtl` and `en/ltr`;
- duplicate HTML IDs = 0;
- self canonical;
- AR / EN / x-default hreflang;
- Open Graph baseline;
- WebPage + BreadcrumbList + demo Organization JSON-LD;
- canonical supplier/product/market data hooks;
- loading, error, noscript and explicit demo disclosure states;
- Supplier parent navigation current-state on desktop, mega-menu and mobile;
- local asset and icon references;
- no TARGET/client leakage;
- JavaScript syntax;
- Global Navigation V1 normalization check.

## 5. Rendered Responsive QA — PASS

`qa/pg13-supplier-details/rendered-report.json` reports **0 failures** for all eight cases:

| Language | Width | Result |
|---|---:|---|
| Arabic | 390 | PASS |
| Arabic | 820 | PASS |
| Arabic | 1366 | PASS |
| Arabic | 1536 | PASS |
| English | 390 | PASS |
| English | 820 | PASS |
| English | 1366 | PASS |
| English | 1536 | PASS |

The rendered gate validates:

- successful canonical JSON load;
- default Noura supplier state;
- product/category/market/certification counts;
- linked product and category routes;
- no horizontal overflow;
- RTL/LTR direction;
- supplier-aware header RFQ synchronization;
- minimum displayed touch-target threshold;
- desktop mega-menu open/Escape behavior;
- mobile drawer open/close behavior.

## 6. Interaction QA — PASS

The workflow separately validates:

- `supplier-nordvale` query-param switch;
- linked product/category/market counts after supplier switch;
- localized supplier name update;
- supplier ID preservation on language switch;
- supplier-aware RFQ route;
- Organization JSON-LD identifier update;
- BluePort zero-certification empty state;
- invalid supplier ID fallback to `supplier-noura` with visible fallback state;
- Arabic supplier query + RTL + language preservation.

All interaction failure arrays are empty.

## 7. Navigation Governance Defect Found and Corrected

The initial PG13 build placed the supplier query directly into the static Global Header CTA. This worked functionally but created structural drift from `GLOBAL-NAVIGATION-CONTRACT-V1`.

Correction:

- Restored the static header CTA to canonical `rfq.html` + `data-orx-header-cta` in AR and EN.
- Kept supplier-aware query synchronization in PG13 runtime after data resolution.
- Final `normalize_global_navigation.py --check` = PASS.

The first GitHub Actions run correctly detected `global-navigation-drift` in English. After correction, the rerun returned source failures 0 and final `run-status.txt = PASS`. This defect is therefore closed with automated regression evidence.

## 8. UX / Maintainability Improvements Added During Build

1. **Canonical market data completion** — implemented the missing `markets.json` domain already declared by the frozen schema.
2. **Category interaction targets** — increased minimum interactive height/padding for mobile/tablet usability.
3. **Market information density** — responsive three-column market grid on suitable widths.
4. **Global navigation governance** — removed page-local header structure drift and kept the header canonical.
5. **Runtime QA observability** — added `loading / ready / error`, active supplier ID and relation counts to the page root for deterministic CI testing.
6. **Section QA hooks** — added stable `data-pg13-section` markers for page-level regression testing and future maintenance.

None of these changes expands the frozen V1 commercial scope.

## 9. Final Decision

**PG13 is promoted to PS7 / IMPLEMENTED / CI QA PASS.**

Canonical evidence:

- `qa/pg13-supplier-details/source-report.json` — failures 0.
- `qa/pg13-supplier-details/rendered-report.json` — failures 0; responsive 8/8 PASS; interaction suites PASS.
- `qa/pg13-supplier-details/run-status.txt` — PASS.
- Evidence commit: `d16e8d86279de5242f15a71535248a40fe878c4c`.

## 10. Remaining Gate

PG13 is **not PS8** yet. Final acceptance still requires the current revision to pass deployed Cloudflare AR/EN mobile + desktop browser review under the project-wide PS8 closure matrix.
