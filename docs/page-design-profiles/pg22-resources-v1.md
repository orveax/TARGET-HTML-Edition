# ORIGEX — PG22 Downloads / Resources | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M5 — Proof / Resources / Compliance / Content  
Status: PS7 — IMPLEMENTED / CI QA PASS — AR+EN  
Canonical file: `resources.html`

## Purpose
Provide a commercially safe resource-library page where buyers can organize and distribute company, product, supplier, compliance and market-reference files without fabricating real documents or licensing claims.

## Canonical Content Authority
Arabic Master:
- H1: `ملفات ومعلومات يمكن الرجوع إليها قبل التواصل.`
- Support: `نظم الملف التعريفي، الكتيبات، أوراق البيانات، الشهادات والمستندات حسب النوع واللغة.`
- Resources: Company Profile / Product Datasheet / Supplier Checklist / Compliance Example / Market Brief Placeholder.

English Adaptation:
- H1: `Commercial files and information available before the conversation.`

## Frozen Main Features
Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.
1. Resource categories
2. Company profile
3. Brochures / product information assets
4. Datasheets
5. Certificates / compliance examples
6. Language tags
7. Download actions

## Resource / Licensing Contract
- No unverified third-party file enters the page or buyer package.
- PG22 ships five ORVEAX-authored UTF-8 Demo text resources under `assets/resources/` so every download action resolves to a real local file.
- Files are illustrative placeholders, not client documents, legal certificates, regulatory approvals, product specifications or live market intelligence.
- Buyer must replace Demo resources with verified, permissioned production files.
- No PDF is fabricated merely to make a button look real.
- Resource registration authority: `docs/RESOURCE-ASSET-REGISTER-V1.md` plus Notion Assets & Licensing.

## Demo Resource Set
1. Company Profile Demo — bilingual text asset.
2. Product Datasheet Demo — bilingual text asset.
3. Supplier Checklist Demo — bilingual text asset.
4. Compliance Example Demo — bilingual text asset.
5. Market Brief Placeholder — bilingual text asset.

Each card exposes:
- category;
- file type;
- Demo status;
- Arabic + English language tags;
- short purpose;
- local download action;
- contextual preview link only where the target page already exists.

## Filter Contract
Approved categories:
- `all`
- `company`
- `product`
- `supplier`
- `compliance`
- `market`

Runtime: `assets/js/origex-resources.js`.
Allowed:
- category filtering;
- visible count;
- `aria-pressed` state;
- `?category=<value>` hydration;
- valid category preservation across AR/EN language switch;
- accessible zero-result state.

Prohibited:
- remote downloads;
- analytics/tracking dependency;
- fake file-size claims;
- fake version/history claims;
- binary/PDF claims for text Demo files;
- unregistered downloadable assets.

## Information Architecture
Breadcrumb → Hero / resource-boundary note → category filter → resource grid → replacement guidance → Final CTA.

## Visual Direction
Premium document-library UI; restrained B2B cards; visible file/type/status/language metadata; download CTA must read as a real utility action, not decorative content. One column mobile, two tablet, three desktop where readable. Filter bar may scroll internally on narrow screens without page overflow.

## Navigation / Footer
- Standard Global Navigation V1.
- Explore current state; Resources current in Mega Menu.
- Locked mobile drawer includes Resources and marks it current through the global normalizer.
- Footer consumes Global Footer V1 exactly.
- Language switch preserves a valid `category` query parameter.

## SEO / Page Identity
### Arabic
- File: `ar/resources.html`
- Title: `الموارد والتنزيلات التجارية | ORIGEX`
- Description: `مكتبة Demo منظمة للملف التعريفي وأوراق البيانات وقوائم المورد والامتثال ومراجع السوق مع توضيح اللغة وحالة الملف.`
- H1: `ملفات ومعلومات يمكن الرجوع إليها قبل التواصل.`
- Canonical: `https://example.com/ar/resources.html`

### English
- File: `en/resources.html`
- Title: `Commercial Downloads & Resources | ORIGEX`
- Description: `An organized Demo library for company-profile, product, supplier, compliance and market-reference files with clear language and file-state metadata.`
- H1: `Commercial files and information available before the conversation.`
- Canonical: `https://example.com/en/resources.html`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. No Product/Offer/Certification claims in structured data.

## Accessibility / Responsive
- one H1;
- filter buttons keyboard-operable with `aria-pressed`;
- visible resource count in `aria-live=polite` context;
- download links have descriptive accessible names;
- hidden cards use `hidden`;
- no horizontal page overflow at 390/820/1366/1536;
- touch-target baseline applies;
- Arabic RTL / English LTR verified separately.

## PS7 Closure Evidence — 2026-08-20
- AR/EN pages implemented.
- Five local registered Demo resources exist and match the resource register.
- Source/runtime/resource QA failures: 0.
- Rendered AR/EN × 390/820/1366/1536: 8/8 PASS.
- Category query hydration, language preservation, keyboard reset and empty-state interactions: PASS.
- Download path existence and `.txt` / UTF-8 type accuracy: PASS.
- Global Navigation V1 + Global Footer V1: PASS.
- F05 Icon Integrity: 46 AR/EN pages / 0 missing sprite references at closure.
- Final QA evidence commit: `630b626d0180d2c62dd8112531bddb5f419b1bc6`.
- PS8 remains gated by deployed Cloudflare browser acceptance.

Copyright © ORVEAX.