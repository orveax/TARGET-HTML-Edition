# ORIGEX — PG18 RFQ / Request a Quote | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: PS7 — IMPLEMENTED / CI QA PASS — AR+EN  
Canonical file: `rfq.html`

## Purpose

Provide a structured buyer-facing Request for Quotation flow that captures the minimum commercial requirement needed to begin an RFQ review without implying price, availability, acceptance or a live backend.

PG18 is a template demo flow. It may load the canonical local `products.json` dataset for product selection, but it does **not** transmit, persist, price, approve or submit an RFQ until the buyer connects the form to a real processing service.

## Frozen Main Features

Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.

1. Buyer details
2. Product selection
3. Quantity
4. Destination
5. Target timing
6. Notes
7. Attachment UI
8. Consent
9. Validation
10. Confirmation state

No pricing engine, cart, checkout, payment, stock reservation, CRM submission, server upload, quotation PDF generation, automatic quote number or live availability check is included in V1.

## Funnel Role

Product / Product Details / Header RFQ CTA → **PG18 Request a Quote** → browser-only validated confirmation → real commercial follow-up after integration.

## Product Selection Contract

- Canonical source: `assets/data/products.json`.
- Runtime may load the local JSON file only to populate the product selector and show a compact selected-product summary.
- Query parameter: `?product=<product-id>`.
- A valid product ID preselects the matching product and preserves it across AR/EN language switching.
- An invalid product ID does **not** silently substitute another product. The selector remains empty and a neutral guidance state is shown.
- All product records remain fictional Demo data.

## Required Fields

### Buyer Details
Required:
- Company / Organization Name
- Contact Name
- Business Email

Optional:
- Phone

### RFQ Requirement
Required:
- Product
- Quantity
- Quantity Unit
- Destination / Port / City
- Target Timing

Optional:
- Notes / specifications
- One supporting attachment

Quantity units:
- Units
- Cases
- Pallets
- Containers

Target timing options:
- As soon as commercially possible
- Within 30 days
- Within 60–90 days
- Planning / exploratory

## Attachment Contract

Accepted Demo extensions:
- PDF
- JPG / JPEG
- PNG
- DOC / DOCX

Maximum Demo file size: **10 MB**.

The selected file is never uploaded by V1. The UI may display the local filename only.

## Consent

Required acknowledgement:

Arabic: `أفهم أن هذا نموذج طلب عرض سعر تجريبي داخل القالب، وأن البيانات والملفات لا يتم إرسالها أو حفظها حتى يتم ربط النموذج بخدمة معالجة فعلية.`

English: `I understand this is a template demo RFQ and that data/files are not transmitted or stored until the form is connected to a real processing service.`

## Confirmation State

Arabic: `تم التحقق من طلب عرض السعر داخل العرض التوضيحي. لم يتم إرسال أو حفظ أي بيانات أو ملفات، ولم يتم إنشاء سعر أو رقم طلب. اربط النموذج بخدمة معالجة فعلية قبل النشر.`

English: `The demo RFQ has been validated. No data or files were transmitted or stored, and no price or request number was generated. Connect the form to a real processing service before publication.`

## Commercial Boundaries

Visible disclosure must state:
- this is not a live quotation;
- no price, availability, allocation or delivery commitment is generated;
- product selection uses fictional Demo records;
- target timing is a buyer requirement, not a delivery promise;
- attachment selection is local UI only;
- legal/regulatory and import requirements vary by product and destination;
- Demo data must be replaced with verified commercial information before production use.

## Information Architecture

Breadcrumb → RFQ Hero / buyer-intent summary → Demo disclosure → Buyer Details → Product & Quantity → Destination & Timing → Notes / Attachment → Consent & Review → Confirmation state → Alternative routes.

## Visual Direction

- Professional B2B buying request / trade brief, not ecommerce checkout.
- Split hero with a compact `What makes an RFQ reviewable` panel.
- Form groups use numbered dossier sections.
- Selected-product summary uses existing product/fact card language.
- Required/optional semantics appear in text, not color alone.
- Attachment uses C24 Upload.
- Confirmation/error states use C25 Form Status.
- Consent uses P09 Checkbox.
- Reuse M1 components/tokens only; no new component family.

## Navigation / Footer Contract

- Standard Global Navigation V1.
- RFQ remains the global header primary CTA route; no separate top-level mega-menu item is added.
- Language switch preserves a valid `product` query parameter.
- Footer consumes N04 Global Footer V1 exactly; no page-local footer variant.

## Runtime Contract

Page runtime: `assets/js/origex-rfq.js`.

Allowed responsibilities:
- load canonical local `products.json`;
- populate product selector;
- hydrate valid `?product=` selection;
- preserve valid product ID on language switch;
- display selected-product summary;
- validate attachment extension and <= 10 MB size;
- preserve native field validation;
- prevent actual form submission;
- show accessible error / confirmation states.

Prohibited responsibilities:
- POST/PUT/PATCH/DELETE requests;
- remote API submission;
- localStorage/sessionStorage persistence;
- price calculation;
- fake availability;
- fake quote/request number;
- fake upload progress;
- analytics dependency.

## SEO / Page Identity Contract

SEO ID: PG18.  
Indexability: INDEX candidate.

### Arabic
- File: `ar/rfq.html`
- Title: `طلب عرض سعر لتجارة الأغذية B2B | ORIGEX`
- Meta Description: `نموذج RFQ منظم لبيانات المشتري والمنتج والكمية والوجهة والتوقيت والملاحظات قبل بدء مراجعة تجارية.`
- H1: `حوّل احتياج الشراء إلى طلب عرض سعر أوضح.`
- Canonical: `https://example.com/ar/rfq.html`
- Breadcrumb: `المنتجات / طلب عرض سعر`

### English
- File: `en/rfq.html`
- Title: `B2B Food Trading RFQ / Request a Quote | ORIGEX`
- Meta Description: `A structured RFQ form for buyer details, product, quantity, destination, target timing, notes and supporting attachment information.`
- H1: `Turn your buying requirement into a clearer RFQ.`
- Canonical: `https://example.com/en/rfq.html`
- Breadcrumb: `Products / Request a Quote`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. No Offer, price, inventory or quotation structured claims.

## Accessibility / Responsive

- one semantic H1;
- visible labels for every form control;
- required controls use native `required` semantics;
- status uses `role=status` / `role=alert`;
- file input keyboard accessible;
- consent touch target >= 24 px;
- no horizontal overflow at 390 / 820 / 1366 / 1536;
- AR RTL / EN LTR verified independently;
- reduced-motion inherited globally.

## Automated QA Gate

- Canonical fast gate: `.github/workflows/pg18-rfq-regression-qa.yml`.
- Evidence: `qa/pg18-rfq/`.
- Source/Data/Runtime failures: 0.
- Canonical dataset: 12 Demo products with unique IDs.
- Rendered gate: AR/EN × 390 / 820 / 1366 / 1536 = 8/8 PASS.
- Query gate: valid product prefill + selected-product summary + language preservation PASS; invalid ID non-fallback + guidance PASS.
- Form gate: required fields + keyboard consent + browser-only confirmation PASS.
- Network boundary: no submission fetch; local `products.json` fetch only.
- File gate: invalid extension rejection + valid local filename state PASS.
- Shared-shell regression discovered and corrected: direct `orx-whatsapp` / `orx-back-to-top` utilities now receive canonical 44–48px hit areas through `assets/css/origex-shell.css`.

## Exit Gate

**PS7 / IMPLEMENTED / CI QA PASS — AR+EN.**

PS8 remains gated by deployed Cloudflare browser acceptance.

Copyright © ORVEAX.
