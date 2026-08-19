# ORIGEX — PG17 Submit Your Product | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: PS6 — FROZEN / BUILD IMPLEMENTED / QA GATE OPEN  
Canonical file: `submit-product.html`

## Purpose

Provide a structured supplier/manufacturer product-submission form that captures the minimum company, product, packaging, origin, commercial and document information needed for an initial review.

PG17 is a template demo flow. It does **not** transmit, persist, approve, verify or register any submitted information until the buyer connects the form to a real backend or form-processing service.

## Frozen Main Features

Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.

1. Company information
2. Product information
3. Category
4. Origin
5. Packaging
6. MOQ
7. Certifications / document references
8. File-upload UI
9. Consent
10. Validation
11. Submission state

No account creation, supplier dashboard, automatic approval, live onboarding, paid listing, territory assignment, ecommerce, CRM submission, server upload or database persistence is included in V1.

## Funnel Role

PG16 For Suppliers → **PG17 Submit Your Product** → initial-review demo state → next commercial conversation.

Primary user question: **What information do I need to provide, and can I submit it in one clear flow?**

## Arabic Content Contract

### Hero
- Eyebrow: `تقديم منتج B2B`
- H1: `قدّم منتجك بمعلومات تجارية قابلة للمراجعة.`
- Lead: `أدخل بيانات الشركة والمنتج والمنشأ والتعبئة والحد الأدنى للطلب والمستندات المتاحة في نموذج واحد منظم.`
- Primary CTA: `ابدأ نموذج التقديم`
- Secondary CTA: `راجع متطلبات المورد`

### Form Groups

#### 01 Company Information
Required:
- Company Name / اسم الشركة
- Company Role / صفة الشركة — Manufacturer / Supplier / Brand Owner
- Contact Name / اسم مسؤول التواصل
- Business Email / البريد التجاري

Optional:
- Phone / الهاتف
- Website / الموقع الإلكتروني

#### 02 Product Information
Required:
- Product Name / اسم المنتج
- Category / الفئة
- Country of Origin / بلد المنشأ
- Pack Size / حجم العبوة
- Packaging / Case Configuration / التعبئة وتكوين الكرتون
- MOQ / الحد الأدنى للطلب أو طريقة تحديده

Optional:
- Storage Requirements / متطلبات التخزين
- Shelf Life / مدة الصلاحية
- Target Market / Channel / السوق أو القناة المستهدفة
- Availability Notes / ملاحظات التوفر

Frozen demo categories:
- Ambient Foods
- Beverages
- Dairy
- Frozen
- Confectionery
- Ingredients

#### 03 Certifications & Documents
Optional:
- Certification / compliance references textarea.
- File upload: one supporting file for demo interaction.

Accepted demo file extensions:
- PDF
- JPG / JPEG
- PNG
- DOC / DOCX

Maximum demo file size: **10 MB**.

The selected file is never uploaded by the V1 demo. The UI may display the local filename only.

#### 04 Consent
Required acknowledgement:

Arabic: `أفهم أن هذا نموذج تجريبي داخل القالب، وأن البيانات والملفات لا يتم إرسالها أو حفظها حتى يتم ربط النموذج بخدمة معالجة فعلية.`

English: `I understand this is a template demo form and that data/files are not transmitted or stored until the form is connected to a real processing service.`

## English Content Contract

### Hero
- Eyebrow: `B2B Product Submission`
- H1: `Submit your product with commercial information that can be reviewed.`
- Lead: `Provide company, product, origin, packaging, MOQ and available document information through one structured submission flow.`
- Primary CTA: `Start Submission Form`
- Secondary CTA: `Review Supplier Requirements`

English preserves the Arabic commercial meaning without stronger claims.

## Validation Contract

Native HTML constraint validation is the first layer.

Page runtime may additionally validate:
- file extension;
- file size <= 10 MB;
- explicit consent;
- demo submission state.

Validation must not contact a network endpoint.

### Success State

Arabic: `تم التحقق من بيانات النموذج داخل العرض التوضيحي. لم يتم إرسال أو حفظ أي بيانات أو ملفات. اربط النموذج بخدمة معالجة فعلية قبل النشر.`

English: `The demo submission has been validated. No data or files were transmitted or stored. Connect the form to a real processing service before publication.`

### File Error State

Arabic: `اختر ملف PDF أو JPG أو PNG أو DOC/DOCX بحجم لا يتجاوز 10 MB.`

English: `Choose a PDF, JPG, PNG or DOC/DOCX file no larger than 10 MB.`

## Commercial / Legal Boundaries

Visible disclosure must state:
- product submission does not imply acceptance, representation or distribution;
- no exclusivity or territory right is created;
- certification references are not automatically verified;
- market references do not imply product registration or guaranteed entry;
- regulatory requirements vary by product and market;
- the template does not determine legal/regulatory sufficiency;
- demo data must be replaced by verified business information before production use.

## Information Architecture

Breadcrumb → Hero / submission summary → Demo disclosure → Structured Form → Review-before-submit summary → Submission status → Alternative route / final CTA.

## Visual Direction

- Professional trade dossier / submission workflow, not a SaaS onboarding dashboard.
- Split hero with a compact `What to prepare` panel.
- Form presented in three clear groups with numbered headings.
- Required/optional distinction must be visible in text, not color alone.
- File upload uses existing C24 Upload component.
- Status uses C25 Form Status.
- Consent uses P09 Checkbox.
- Final route uses S06 Final CTA.
- Reuse M1 components/tokens only; no new component family.

## Navigation / Footer Contract

- Supplier family parent is current in desktop navigation.
- Mega-menu `Submit Your Product` is current.
- Mobile `Submit Your Product` is current.
- Header follows `GLOBAL-NAVIGATION-CONTRACT-V1.md`.
- Footer consumes **N04 Global Footer V1** exactly; no page-local footer variant.

## Interaction Contract

Page runtime: `assets/js/origex-submit-product.js`.

Allowed responsibilities:
- expose selected filename;
- reject unsupported file type or >10 MB file;
- preserve native form validation;
- prevent actual submit/network transmission;
- show accessible error/success status;
- focus final status after valid demo submit.

Prohibited responsibilities:
- fetch/AJAX submission;
- localStorage/sessionStorage persistence;
- automatic supplier approval;
- fake upload progress;
- fake reference number;
- analytics dependency.

## SEO / Page Identity Contract

SEO ID: PG17.  
Indexability: INDEX candidate.

### Arabic
- File: `ar/submit-product.html`
- Title: `تقديم منتج غذائي B2B | ORIGEX`
- Meta Description: `نموذج منظم لتقديم بيانات الشركة والمنتج والمنشأ والتعبئة وMOQ والمستندات المتاحة للمراجعة الأولية.`
- H1: `قدّم منتجك بمعلومات تجارية قابلة للمراجعة.`
- Canonical: `https://example.com/ar/submit-product.html`
- Breadcrumb: `الموردون / تقديم منتج`

### English
- File: `en/submit-product.html`
- Title: `Submit a B2B Food Product | ORIGEX`
- Meta Description: `A structured product-submission form for company, product, origin, packaging, MOQ and available document information before an initial review.`
- H1: `Submit your product with commercial information that can be reviewed.`
- Canonical: `https://example.com/en/submit-product.html`
- Breadcrumb: `Suppliers / Submit Product`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. No supplier-rating, verification or offer structured claims.

## Accessibility / Responsive

- one semantic H1;
- visible labels for every form control;
- required fields identified with text/`required` semantics;
- error/success status exposed through `role=status` / `role=alert` as appropriate;
- upload input keyboard accessible;
- no horizontal overflow at 390 / 820 / 1366 / 1536;
- AR RTL / EN LTR independently verified;
- touch targets follow shared component floor;
- reduced-motion inherited globally.

## Automated QA Gate

- Workflow: `.github/workflows/pg17-submit-product-qa.yml`.
- Evidence: `qa/pg17-submit-product/`.
- Source gate checks required fields, file contract, demo-backend safety, SEO, icons, Global Navigation V1 and Global Footer V1.
- Rendered gate checks AR/EN at 390 / 820 / 1366 / 1536, touch targets and global navigation interactions.
- Interaction gate verifies empty-form rejection, keyboard consent, valid demo success, zero fetch/XHR requests, invalid-file rejection and valid-file filename state.

## Exit Gate

PS7 only after AR+EN build plus source/SEO/assets/icons/navigation/footer/form semantics/file validation/native validation/consent/success state/responsive/interaction QA PASS.

PS8 remains gated by deployed Cloudflare browser acceptance.

Copyright © ORVEAX.