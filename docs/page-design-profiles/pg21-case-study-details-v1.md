# ORIGEX — PG21 Case Study Details | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M5 — Proof / Resources / Compliance / Content  
Status: **PS7 — IMPLEMENTED / CI QA PASS — AR+EN**  
Canonical file: `case-study-details.html`

## Purpose

Provide the detail-layout counterpart to PG20 Case Studies using fictional, clearly labelled Demo evidence. The page demonstrates how a B2B food-trading case can be structured from challenge to illustrative result without presenting template content as a real client engagement.

## Canonical Content Authority

Arabic Master:
- Demo Case: `تجهيز منتج غذائي لدخول قناة تجزئة جديدة — حالة توضيحية.`
- Structure: Challenge → Context → Objective → Approach → Process → Illustrative Result → Metrics Disclaimer → Related Cases → CTA.
- Disclaimer: `النتيجة مثال توضيحي وليست نتيجة مشروع حقيقي.`

English Adaptation:
- Demo: `Preparing a food product for a new retail channel — Demo Case Study.`
- Disclaimer: `Illustrative result only; not a real client engagement.`

## Frozen Main Features

Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.

1. Challenge
2. Context
3. Approach
4. Process
5. Result
6. Metrics
7. Related case studies
8. CTA

The canonical Arabic Master additionally defines Objective and Metrics Disclaimer as required content inside the frozen detail structure.

## Editorial / Data Contract

PG21 remains editorial HTML. No `cases.json` domain is introduced because `docs/DATA-SCHEMA-V1.md` freezes structured JSON domains to products, suppliers and markets.

The six PG20 Demo case IDs remain stable:
- `case-001` — Ambient Foods / Market Access
- `case-002` — Beverages / Distribution
- `case-003` — Dairy / Supplier Readiness
- `case-004` — Frozen / RFQ & Buying
- `case-005` — Confectionery / Distribution
- `case-006` — Ingredients / Product Information

PG21 stores all editorial case-detail copy in HTML `<template>` records. JavaScript selects and renders the requested record; it does not own canonical editorial copy.

## Query / Runtime Contract

Canonical query parameter: `?id=case-001` through `?id=case-006`, matching PG20 links.

Runtime: `assets/js/origex-case-study-details.js`.

Required behavior:
- hydrate valid `id` on load;
- default to `case-001` when no ID is supplied;
- invalid ID shows a visible Demo fallback notice and renders `case-001` rather than blank content;
- language switch preserves the resolved case ID;
- previous/next case controls remain within the six-case Demo set;
- related cases exclude the currently rendered case;
- runtime updates visible case label/title/sections only from HTML template records;
- no network requests, storage, analytics dependency or remote content source.

## Detail Content Structure

Each Demo record includes:
- industry/category tag;
- commercial focus tag;
- Challenge;
- Context;
- Objective;
- Approach;
- three-step Process;
- Illustrative Result;
- qualitative Metrics / review signals;
- explicit Metrics Disclaimer;
- related-case navigation.

Metrics are qualitative review signals only. No revenue, ROI, growth percentage, conversion uplift, sales volume, client logo, testimonial, rating, award or measured commercial result may appear in V1 Demo content.

## Proof / Commercial Boundaries

Visible disclosure states:
- all cases are fictional Demo scenarios;
- the page is not evidence of a real client engagement;
- results and metrics are illustrative workflow examples, not measured outcomes;
- no case implies guaranteed market entry, sales, appointment, pricing, availability or regulatory approval;
- buyers must replace Demo evidence with verified, permissioned content before production publication.

## Information Architecture

Breadcrumb → Detail Hero → Demo/Fallback Notice → Challenge + Context → Objective + Approach → Process → Illustrative Result + Metrics Disclaimer → Related Cases → Final CTA.

## Visual Direction

- editorial B2B proof layout, not agency portfolio styling;
- strong reading hierarchy and restrained surfaces;
- one-column mobile reading flow;
- desktop uses a primary reading column plus sticky case-facts rail only where it remains readable;
- process is presented as three numbered steps using existing design tokens;
- result block uses accent/sand treatment rather than success-green achievement styling;
- related cases reuse compact case-study-card language;
- no decorative charts because metrics are qualitative and unmeasured.

## Navigation / Footer Contract

- Standard Global Navigation V1.
- PG21 is a detail page mapped to `case-studies.html` as its Explore parent by the locked navigation normalizer.
- `Case Studies` is current in the Mega Menu; no new top-level/mobile route is added.
- Language switch preserves the resolved `id` query parameter at runtime.
- Global Footer V1 is consumed exactly; no page-local variant.

## SEO / Page Identity Contract

SEO ID: PG21.  
Indexability: INDEX candidate as a reusable detail layout.

### Arabic
- File: `ar/case-study-details.html`
- Title: `تفاصيل دراسة حالة تجارية B2B | ORIGEX`
- Meta Description: `صفحة Demo تفصيلية توضح بناء دراسة حالة B2B من التحدي والسياق إلى المنهج والعملية والنتيجة التوضيحية بدون ادعاء نتائج عملاء حقيقية.`
- Canonical: `https://example.com/ar/case-study-details.html`
- Breadcrumb: `الرئيسية / دراسات الحالة / تفاصيل الحالة`

### English
- File: `en/case-study-details.html`
- Title: `B2B Case Study Details | ORIGEX`
- Meta Description: `A fictional B2B food-trading case-study detail layout covering challenge, context, approach, process and illustrative result without real-client performance claims.`
- Canonical: `https://example.com/en/case-study-details.html`
- Breadcrumb: `Home / Case Studies / Case Details`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. No Review, Rating, Offer, QuantitativeValue or performance-result structured claims.

## Accessibility / Responsive

- exactly one semantic H1 in the rendered document;
- case record change updates the H1 and document title without stealing focus on initial load;
- fallback notice uses `role=status`;
- previous/next and related-case links are descriptive and keyboard accessible;
- process numbers are decorative, labels remain textual;
- no horizontal overflow at 390 / 820 / 1366 / 1536;
- RTL/LTR independently verified;
- reduced-motion inherited globally.

## PS7 Closure Evidence — 2026-08-20

- Source/runtime failures: **0**.
- AR/EN sections: hero / notice / detail / navigation / related / CTA.
- Six stable Demo case records in each language.
- Rendered responsive QA: **8/8 PASS** across AR/EN × 390 / 820 / 1366 / 1536.
- Valid `case-004` query hydration: PASS.
- Invalid `case-999` fallback to `case-001` with visible status: PASS.
- AR/EN language switch preserves resolved case ID: PASS.
- Previous/next navigation: PASS.
- Related-case exclusion/count: PASS.
- Global Navigation V1 / Global Footer V1 / F05 Icon Integrity: PASS.
- Final QA evidence commit: `7b5be6b72985026d003f48da5f7b3674fb84fcf6`.
- QA authority: `docs/PG21-QA-REPORT-V1.md`.

## Exit Gate

PS7 complete. PS8 remains gated by deployed Cloudflare browser acceptance.

Copyright © ORVEAX.