# ORIGEX — PG16 For Suppliers | QA Report V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Page: PG16 — For Suppliers  
Canonical file: `for-suppliers.html`  
Final gate: **PS7 / IMPLEMENTED / CI QA PASS**  
Date: 2026-08-19

## 1. Build Evidence

- PS6 Page Design Profile: `docs/page-design-profiles/pg16-for-suppliers-v1.md` — initial commit `72d08e703cb5256985bc9bfcb956bb0e878987dd`.
- Composition: `assets/css/origex-for-suppliers.css` — `567f634de28917b65038b59494f0dbe2777a115d`.
- English: `en/for-suppliers.html` — `a0f454013bf1f4c97657b22f86b8a2161fdb9dd4`.
- Arabic: `ar/for-suppliers.html` — `faec3797936cd9512848e7ac302af9316ed9550f`.
- Automated QA workflow: `.github/workflows/pg16-for-suppliers-qa.yml`.
- Final evidence commit: `85298bb66688e66b95bb66c5a4313264b2761c5a`.

## 2. Frozen Page Composition

Eight controlled sections:

1. Hero / supplier readiness summary
2. Supplier value proposition
3. Qualification criteria
4. Four-step supplier route
5. Required information / documents
6. Commercial boundaries
7. Supplier FAQ
8. Final CTA

No supplier dashboard, account, paid listing, verification badge, automatic acceptance, exclusivity workflow or live onboarding state was added.

## 3. Commercial Safety / Content QA

PASS:

- submission is explicitly not acceptance, representation or distribution;
- no exclusivity or territory rights are implied;
- certification references are not presented as verification;
- target-market references are not registration or guaranteed market entry;
- regulatory/legal sufficiency is not invented;
- demo/backend disclosure remains explicit;
- no TARGET/client content leakage;
- Arabic and English preserve the same commercial meaning.

The first source QA rule falsely flagged the phrase `No guaranteed market entry` because the regex searched the prohibited phrase without understanding its negation. The gate was corrected to require the explicit negative boundary instead of treating the phrase itself as a claim.

## 4. Shared-Shell Improvements Triggered During PG16

### Global Footer V1

Administrator observation identified real cross-page footer drift. PG16 triggered a global correction rather than a page-local patch:

- `docs/GLOBAL-FOOTER-CONTRACT-V1.md` established N04 as one canonical footer.
- `.github/scripts/normalize_global_footer.py` provides deterministic normalization.
- `.github/workflows/global-footer-qa.yml` enforces the contract.
- Final Global Footer QA: **34 AR/EN pages / failures 0 / PASS**.
- Final normalization evidence: `d169100bca1f14dab42cafab81f1812fb7c94184`.

### Global Navigation V1

PG16 source QA also identified structural navigation drift. Existing canonical navigation logic was converted from check-only enforcement to deterministic normalize + check + commit:

- Workflow hardening: `f4e34c876f7a2e77d2ea59983a90f9c84b9f1249`.
- PG16/global normalization: `f8f368506a1d796c0b7f27eebc14b4da8e228a86`.

The page now consumes both Global Navigation V1 and Global Footer V1 rather than carrying local shell forks.

## 5. Source QA

Final `qa/pg16-for-suppliers/source-report.json`:

- failures: 0
- AR failures: 0
- EN failures: 0
- exact eight-section composition: PASS
- single H1: PASS
- AR RTL / EN LTR: PASS
- canonical / AR-EN-x-default hreflang: PASS
- WebPage + BreadcrumbList baseline: PASS
- required CSS/assets/icons: PASS
- Supplier parent navigation + For Suppliers current state: PASS
- Global Footer V1 hooks: PASS
- six FAQ triggers with valid `aria-controls`: PASS
- no unapproved page-specific JavaScript: PASS

## 6. Rendered / Responsive QA

Final `qa/pg16-for-suppliers/rendered-report.json`:

- Arabic 390: PASS
- Arabic 820: PASS
- Arabic 1366: PASS
- Arabic 1536: PASS
- English 390: PASS
- English 820: PASS
- English 1366: PASS
- English 1536: PASS

**8/8 responsive cases PASS.**

Verified in rendered browser:

- no horizontal overflow;
- correct RTL/LTR direction;
- eight controlled sections render;
- Global Footer V1 exists with business-hours hook;
- Submit Product routes exist;
- touch-target floor passes;
- desktop mega-menu open/Escape interaction passes;
- mobile drawer open/close passes.

## 7. Accordion QA Improvement

The initial Selenium native click test on the deep FAQ section produced `ElementClickInterceptedException` in both languages even though all page responsive cases passed. Review of C14 showed no accordion overlay defect; the page uses a global sticky header and the native driver click was a brittle auto-scroll interaction.

The interaction gate was improved to test accessibility behavior directly:

1. scroll the second FAQ trigger to viewport center;
2. focus the button;
3. activate with `Enter`;
4. verify `aria-expanded=true` and visible panel;
5. activate with `Space`;
6. verify `aria-expanded=false` and hidden panel.

Final result:

- English accordion keyboard: PASS
- Arabic accordion keyboard: PASS

This is stronger evidence than a synthetic pointer click because it validates the frozen C14 keyboard contract.

## 8. Final Decision

`qa/pg16-for-suppliers/run-status.txt` = **PASS**.

PG16 is promoted to:

**PS7 / IMPLEMENTED / CI QA PASS — AR+EN**

Cloudflare deployed-browser acceptance remains a separate PS8 gate for the M4 batch.

## 9. Next M4 Page

**PG17 — Submit Your Product**.

PG17 must consume the same Global Navigation V1 and Global Footer V1 and introduce the actual supplier product-submission form states, validation, file-upload/demo-backend disclosure and conversion flow defined by the frozen V1 scope.

Copyright © ORVEAX.
