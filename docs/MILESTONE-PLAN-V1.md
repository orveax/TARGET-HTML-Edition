# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M4 FINAL ACCEPTANCE OPEN / M5 IN PROGRESS  
Last Alignment: 2026-08-20 — PG20–PG23 PS7 / PG24 NEXT

## Project Brief

Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers. The product must be marketable on ThemeForest, easy for beginner buyers to customize, fast, responsive, accessible, and structured as an ORVEAX commercial product rather than a one-off client website.

## Success Definition

Submission Candidate 1.0.0 must include:
- approved/frozen product foundation and 33-layout V1 architecture after CR-001;
- complete Arabic-first + English LTR page set;
- one reusable ORIGEX design system and registered component architecture;
- coherent fictional Demo datasets/content for products, suppliers, markets, cases and resources;
- `config.js` customization layer;
- SEO/Page Identity contracts, demo-safety rules and licensing controls;
- responsive/RTL/accessibility/performance QA;
- beginner-friendly documentation and clean marketplace package.

## Page Stage Lifecycle

Authority: `CONTENT-SYSTEM-V1.md`.

`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance`

`C01–C28` is reserved for Component IDs.

No page enters implementation before PS6. PS8 requires the applicable page QA and deployed Cloudflare browser acceptance defined by the QA/PS8 governance documents.

Cloudflare review is a **parallel final-acceptance gate**. It does not block continued PS6/PS7 production of subsequent pages while the test environment remains available through Manual Rebuild.

## M0 — Product Foundation Freeze — PASS / CLOSED

Product positioning, V1/V1.1 split, design system, page architecture, technology, content, SEO, demo policy, data schema, release policy and QA governance are frozen.

## M1 — Global System & Component Foundation — PASS / CLOSED

Implemented:
- Bootstrap 5.3.8 local foundation;
- Tajawal / Manrope local typography;
- tokens, primitives, components, sections and navigation;
- local icon sprite and licensing baseline;
- PT01–PT06 patterns;
- RTL/LTR and reduced-motion foundations;
- `config.js` + config engine;
- global shell.

A permanent **Global F05 Icon Integrity QA** gate scans distributed AR/EN pages against the canonical sprite. At PG23 closure the gate covered **48 AR/EN pages with zero missing sprite references**.

## M2 — Global Shell & Home Family — FINAL ACCEPTANCE OPEN

Pages:
- PG01 Home 01 — **PS8 / PASS / CLOSED**.
- PG02 Home 02 — **PS7 / CI QA PASS**.
- PG03 Home 03 — **PS7 / CI QA PASS**.
- PG04 Landing — **PS7 / CI QA PASS**.

Open gate: PG02–PG04 deployed Cloudflare browser acceptance before PS8.

## M3 — Company / Business / Market — FINAL ACCEPTANCE OPEN

Pages:
- PG05 About — **PS7 / CI QA PASS**.
- PG06 How We Work — **PS7 / CI QA PASS**.
- PG07 Capabilities — **PS7 / CI QA PASS**.
- PG08 Service Details — **PS7 / CI QA PASS**.
- PG14 Market Access — **PS7 / CI QA PASS**.
- PG15 Markets / Countries — **PS7 / CI QA PASS**.
- PG33 Company Profile — **PS7 IMPLEMENTED / QA FOLLOW-UP OPEN** under CR-001.

Open gate: PG33 follow-up evidence plus M3 Cloudflare batch acceptance before milestone closure.

## M4 — Product / Supplier / Conversion Core — PAGE PRODUCTION CODE/CI COMPLETE

Pages:
- PG09 Product Categories — **PS7 / CI QA PASS**.
- PG10 Products Grid — **PS7 / CI QA PASS**.
- PG11 Product Details — **PS7 / CI QA PASS**.
- PG12 Suppliers / Brands Directory — **PS7 / CI QA PASS**.
- PG13 Supplier / Brand Details — **PS7 / CI QA PASS**.
- PG16 For Suppliers — **PS7 / CI QA PASS**.
- PG17 Submit Product — **PS7 / CI QA PASS**.
- PG18 RFQ — **PS7 / CI QA PASS**.
- PG19 Become Distributor / Partner — **PS7 / CI QA PASS**.

M4 implementation evidence includes canonical product/supplier/market JSON relationships, search/filter/detail flows, supplier readiness, product submission, RFQ and distributor/partner qualification flows.

**Open M4 gate:** deployed Cloudflare PS8 batch acceptance. M4 is not declared closed until that gate passes.

## M5 — Proof / Resources / Compliance / Content — IN PROGRESS

Pages:
- PG20 Case Studies — **PS7 / IMPLEMENTED / CI QA PASS**.
- PG21 Case Study Details — **PS7 / IMPLEMENTED / CI QA PASS**.
- PG22 Downloads / Resources — **PS7 / IMPLEMENTED / CI QA PASS**.
- PG23 Certifications & Compliance — **PS7 / IMPLEMENTED / CI QA PASS**.
- PG24 Insights / Blog — **NEXT VALID PAGE PRODUCTION ACTION**.
- PG25 Article Details — NOT STARTED.

PG20 final evidence:
- six fictional Demo cases remain editorial HTML; no unapproved `cases.json` schema domain;
- source/runtime failures: 0;
- rendered AR/EN × 390/820/1366/1536: 8/8 PASS;
- filter query hydration / language preservation / keyboard reset / empty state: PASS;
- final evidence commit: `d559056fe2b6b6bd88b7d0debf371f19525e0d80`;
- QA authority: `docs/PG20-QA-REPORT-V1.md`.

PG21 final evidence:
- six PG20-aligned fictional Demo detail records remain editorial HTML `<template>` content; no unapproved `cases.json` domain;
- source/runtime failures: 0;
- rendered AR/EN × 390/820/1366/1536: 8/8 PASS;
- valid/invalid case-ID handling, AR/EN preservation, previous/next and related-case behavior: PASS;
- final evidence commit: `7b5be6b72985026d003f48da5f7b3674fb84fcf6`;
- QA authority: `docs/PG21-QA-REPORT-V1.md`.

PG22 final evidence:
- five ORVEAX-authored bilingual UTF-8 Demo resources registered in `docs/RESOURCE-ASSET-REGISTER-V1.md`;
- no fabricated PDF, certificate, regulatory approval, live-market file or third-party redistribution assumption;
- source/runtime/resource-register failures: 0;
- download target existence and TXT/UTF-8 type accuracy: PASS;
- rendered AR/EN × 390/820/1366/1536: 8/8 PASS;
- category query hydration / language preservation / keyboard reset / empty state: PASS;
- final evidence commit: `630b626d0180d2c62dd8112531bddb5f419b1bc6`;
- QA authority: `docs/PG22-QA-REPORT-V1.md`.

PG23 final evidence:
- six Demo certification/document categories, four quality steps, four storage/handling principles, four-node traceability Demo and document-status matrix;
- no fabricated certificate number, issuer, expiry date, audit result, approval or regulatory status;
- initial QA failed only on canonical navigation drift; fixed centrally by Global Navigation V1 commit `cbb144ac0d431a1f2d0253acaaca8cb7cfa8ac24`;
- source/claim failures: 0;
- rendered AR/EN × 390/820/1366/1536: 8/8 PASS;
- final evidence commit: `2629c2d26a478376c4903771981451bccc4d2003`;
- QA authority: `docs/PG23-QA-REPORT-V1.md`.

### Preview Utility
`site-map.html` is a noindex internal Visual Site Map showing all **PG01–PG33**. It is not a new product layout and does not modify the 33-layout scope. Current QA: 33 cards / 24 implemented / 9 pending / 48 linked AR+EN pages / PASS. Evidence: `50c0d8e3f9ff2908d736c7312c02774f6e962770`.

Gate: all M5 pages PS8 + SEO + demo-proof/resource/download/licensing controls + zero Critical/High milestone defects.

## M6 — Support / Utility — NOT STARTED

Pages:
- PG26 FAQ;
- PG27 Contact;
- PG28 404;
- PG29 Coming Soon;
- PG30 Privacy;
- PG31 Terms;
- PG32 Components / Elements Library.

Gate: full 33-layout AR/EN V1 exists and all applicable pages complete final acceptance.

## M7 — Full QA & Optimization — NOT STARTED

Includes:
- content and AR/EN parity;
- demo-claim/disclaimer scan;
- data consistency;
- page naming/SEO metadata;
- HTML/CSS/JS integrity;
- broken links/assets/console errors;
- full responsive + RTL/LTR matrix;
- keyboard/accessibility/reduced motion;
- performance cleanup;
- cross-browser smoke testing;
- client/TARGET leakage scan;
- final marketplace visual polish.

Gate: zero Critical and zero High defects.

## M8 — Documentation / Licensing / Marketplace Package — NOT STARTED

Includes:
- buyer documentation / Getting Started;
- file structure and customization guides;
- Demo-data replacement / Before You Publish checklist;
- forms/RFQ integration and deployment docs;
- SEO/hreflang guide;
- credits/licenses/assets register;
- changelog/version/support information;
- preview screenshots/listing copy;
- final ZIP + ThemeForest submission checklist.

Gate: Submission Candidate **1.0.0** approved.

## Current Production Order

1. **PG24 — Insights / Blog**: canonical content review → PS6 Page Design Profile / SEO + editorial contract → AR/EN build → featured/category/search/pagination/responsive QA.
2. Continue PG25 sequentially under M5.
3. In parallel, close pending Cloudflare PS8 batches for M2/M3/M4 and completed M5 pages, plus PG33 QA follow-up.

## Change Control

After Product Foundation closure:
- new page or Main Feature family = Scope Change or V1.1+;
- foundation/technology/component/content/SEO/product-governance change = formal Change Request;
- QA/accessibility/performance/responsive/RTL fixes do not reopen scope;
- verified defects may be corrected centrally without reopening product architecture;
- Additional Features remain V1.1 backlog.

## CR-001 Scope Addendum

PG33 Company Profile was added under M3. Active V1 scope is **33 unique layouts / approximately 66 AR+EN HTML pages**. Historical 32-layout statements describe the pre-CR baseline only.

Copyright © ORVEAX.
