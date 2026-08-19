# ORIGEX — PG19 Become Distributor / Partner | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: PS6 — FROZEN FOR BUILD  
Canonical file: `become-partner.html`

## Purpose

Provide a structured distributor / commercial-partner qualification flow for companies that want to discuss territory, channel or distribution opportunities. The page captures operating context needed for an initial partnership review without implying appointment, exclusivity, territory rights, guaranteed product access or acceptance.

PG19 is a template demo flow. It may load the canonical local `markets.json` dataset to populate market / territory interest, but it does **not** transmit, persist, approve or create a partnership relationship until connected to a real processing service.

## Canonical Content Authority

Arabic master:
- H1: `شراكة التوزيع تبدأ بفهم السوق والقدرة التشغيلية.`
- Support: `شارك مناطق التغطية، قنوات البيع، فئات المنتجات، والقدرات الحالية لتقييم فرص التعاون المناسبة.`
- CTA: `تقدم كشريك توزيع`

English adaptation:
- H1: `Distribution partnerships start with market and operating capability.`

## Frozen Main Features

Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.

1. Partnership value
2. Qualification criteria
3. Markets / territories
4. Company profile form
5. Portfolio upload UI
6. CTA

No distributor appointment, territory reservation, exclusivity decision, contract workflow, pricing, commission model, account creation, CRM submission or live partner approval is included in V1.

## Funnel Role

Market Access / Markets / Global Partnership route → **PG19 Become Distributor / Partner** → browser-only validated qualification state → real commercial review after integration.

## Data Contract

- Canonical market source: `assets/data/markets.json`.
- Runtime loads the local JSON file only to populate the primary market / territory selector and compact market context.
- Query parameter: `?market=<market-id>`.
- A valid market ID preselects the matching Demo market and preserves it across AR/EN language switching.
- An invalid market ID does not silently substitute another market; the selector remains empty and a neutral guidance state is shown.
- All market records remain fictional / illustrative Demo data and do not imply rights or active relationships.

## Partnership Value

The page may explain that a structured partner profile helps clarify:
- market and territory coverage;
- sales / distribution channels;
- product-category fit;
- operating capability;
- readiness for a commercial discussion.

It must not promise appointment, exclusivity, lead volume, sales volume or a specific territory.

## Qualification Criteria

Visible qualification guidance:
- identifiable legal / trading company;
- defined operating market / territory;
- active channel access relevant to the opportunity;
- product-category fit;
- operational capability appropriate to the stated role;
- willingness to provide verifiable commercial information before a real appointment decision.

These are review inputs, not automatic acceptance criteria.

## Required Form Fields

### Company Profile
Required:
- Company / Organization Name
- Contact Name
- Business Email
- Company Role

Optional:
- Phone
- Website

Company Role options:
- Distributor
- Importer
- Wholesaler
- Retail / Key-Account Operator
- Foodservice / HORECA Supplier
- Other Commercial Partner

### Market / Territory
Required:
- Primary Market / Territory from canonical Demo markets
- Coverage Description

Optional:
- Additional Markets / Territories notes

### Commercial Fit
Required group validation:
- At least one Sales / Distribution Channel
- At least one Product Category Interest

Approved channel options:
- Retail
- Wholesale
- Foodservice / HORECA
- Modern Trade / Key Accounts
- E-commerce
- Institutional / Projects

Approved category options reuse the frozen six categories:
- Ambient Foods
- Beverages
- Dairy
- Frozen
- Confectionery
- Ingredients

### Capability / Notes
Optional:
- Operating capability notes
- Existing portfolio / represented categories summary
- One portfolio / company-profile attachment

## Portfolio Upload Contract

Accepted Demo extensions:
- PDF
- JPG / JPEG
- PNG
- DOC / DOCX

Maximum Demo file size: **10 MB**.

The selected file is never uploaded by V1. The UI may display the local filename only.

## Consent

Required acknowledgement:

Arabic: `أفهم أن هذا نموذج شراكة تجريبي داخل القالب، وأن إرسال البيانات أو اختيار السوق لا يعني القبول أو التعيين أو الحصرية أو منح حقوق توزيع، وأن البيانات والملفات لا يتم إرسالها أو حفظها حتى يتم ربط النموذج بخدمة معالجة فعلية.`

English: `I understand this is a template demo partnership form; providing information or selecting a market does not imply acceptance, appointment, exclusivity or distribution rights, and data/files are not transmitted or stored until the form is connected to a real processing service.`

## Confirmation State

Arabic: `تم التحقق من نموذج الشراكة داخل العرض التوضيحي. لم يتم إرسال أو حفظ أي بيانات أو ملفات، ولم يتم إنشاء تعيين أو حصرية أو حقوق توزيع. اربط النموذج بخدمة معالجة فعلية قبل النشر.`

English: `The demo partnership profile has been validated. No data or files were transmitted or stored, and no appointment, exclusivity or distribution rights were created. Connect the form to a real processing service before publication.`

## Commercial Boundaries

Visible disclosure must state:
- this is a Demo qualification flow, not a partner appointment;
- no exclusivity, territory reservation or distribution right is created;
- market records are illustrative Demo data;
- channel / category selections describe the applicant's stated profile only;
- attachment selection is local UI only;
- legal, regulatory, import and appointment requirements vary by market and product;
- Demo data must be replaced with verified commercial information before production use.

## Information Architecture

Breadcrumb → Partnership Hero → Partnership Value → Qualification Criteria → Demo disclosure → Company Profile → Market / Territory → Channels / Categories → Capability / Portfolio Upload → Consent / Demo Confirmation → Final CTA.

## Visual Direction

- Premium B2B partnership / distribution profile, not a recruitment form.
- Split hero with compact `What makes a partner profile reviewable` panel.
- Partnership value uses three concise reusable cards.
- Qualification criteria use a restrained checklist / fact treatment.
- Form groups use numbered dossier sections consistent with PG17/PG18 conversion family.
- Market summary uses existing market/fact visual language.
- Channel and category groups use accessible checkbox cards with visible focus and >=24px controls.
- Portfolio upload uses C24 Upload semantics.
- Confirmation/error states use C25 Form Status.
- Reuse M1 components/tokens only; no new component family.

## Navigation / Footer Contract

- Standard Global Navigation V1.
- `Market Access` is the current top-level family.
- `Become Distributor / Partner` is current inside Mega Menu and mobile drawer.
- Language switch preserves a valid `market` query parameter.
- Footer consumes N04 Global Footer V1 exactly; no page-local footer variant.

## Runtime Contract

Page runtime: `assets/js/origex-partner.js`.

Allowed responsibilities:
- load canonical local `markets.json`;
- populate primary market selector;
- hydrate valid `?market=` selection;
- preserve valid market ID on language switch;
- display compact selected-market context;
- enforce at least one channel and one category selection;
- validate portfolio extension and <=10 MB size;
- preserve native required-field validation;
- prevent actual form submission;
- show accessible error / confirmation states.

Prohibited responsibilities:
- POST/PUT/PATCH/DELETE requests;
- remote API submission;
- localStorage/sessionStorage persistence;
- fake partner score;
- fake appointment / approval status;
- fake exclusivity / territory reservation;
- fake upload progress;
- analytics dependency.

## SEO / Page Identity Contract

SEO ID: PG19.  
Indexability: INDEX candidate.

### Arabic
- File: `ar/become-partner.html`
- Title: `كن موزعًا أو شريكًا تجاريًا | ORIGEX`
- Meta Description: `نموذج شراكة وتوزيع B2B منظم لمعلومات الشركة والسوق والتغطية والقنوات وفئات المنتجات والقدرات التشغيلية.`
- H1: `شراكة التوزيع تبدأ بفهم السوق والقدرة التشغيلية.`
- Canonical: `https://example.com/ar/become-partner.html`
- Breadcrumb: `الوصول إلى السوق / كن موزعًا أو شريكًا`

### English
- File: `en/become-partner.html`
- Title: `Become a Distributor / Commercial Partner | ORIGEX`
- Meta Description: `A structured B2B distributor and partner qualification form covering company profile, market, territory, channels, categories and operating capability.`
- H1: `Distribution partnerships start with market and operating capability.`
- Canonical: `https://example.com/en/become-partner.html`
- Breadcrumb: `Market Access / Become Distributor / Partner`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. No Offer, appointment, territory-right or exclusivity structured claims.

## Accessibility / Responsive

- one semantic H1;
- visible labels for every form control;
- required controls use native `required` semantics where applicable;
- grouped channel/category controls have `fieldset` + `legend` and programmatic error state;
- status uses `role=status` / `role=alert`;
- file input keyboard accessible;
- checkbox hit areas >=24 px and non-shrinking;
- no horizontal overflow at 390 / 820 / 1366 / 1536;
- AR RTL / EN LTR verified independently;
- reduced-motion inherited globally.

## QA Rerun Note — 2026-08-20

The first PG19 source gate found one shared F05 defect: distributed pages referenced `message-circle` for the floating WhatsApp control while the symbol was missing from the canonical sprite. The symbol was added centrally in commit `6af5333ac397fb2895c12fc1d5074de0388d14fe`. PG19 remains PS6 until the full post-fix QA rerun records PASS. A global F05 icon-integrity workflow now guards all distributed AR/EN pages against missing sprite references.

## Exit Gate

PS7 only after AR+EN build plus source/SEO/assets/icons/navigation/footer/market-data/query-hydration/group validation/attachment/native validation/consent/confirmation/responsive/interaction QA PASS.

PS8 remains gated by deployed Cloudflare browser acceptance.

Copyright © ORVEAX.
