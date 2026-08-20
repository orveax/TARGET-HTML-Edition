# ORIGEX — PG27 Contact | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Canonical file: `contact.html`  
Status: **PS7 — IMPLEMENTED / CI QA PASS — AR+EN**

## Purpose
Provide a professional contact-routing page that helps a visitor choose the correct commercial route before submitting an enquiry. The page is not a live CRM or ticketing system in the V1 demo package.

## Canonical Content Authority
Arabic Master:
- H1: `اختر قناة التواصل المناسبة لطلبك.`
- Support: `للمنتجات، الموردين، طلبات الأسعار أو الشراكات، شارك نوع الطلب والمعلومات الأساسية حتى يصل إلى المسار الصحيح.`
- Departments: General / Buyer & RFQ / Supplier Submissions / Partnerships.

English Adaptation:
- H1: `Choose the right contact route for your enquiry.`

Frozen V1 Scope Main Features:
- contact channels
- departments
- enquiry form
- address
- business hours
- social links
- map placeholder
- CTA

## Commercial / Demo Boundaries
1. All displayed contact values are Demo fallbacks until replaced in `config.js`.
2. No form submission may imply a message was transmitted, received, ticketed, queued or assigned.
3. V1 form behavior is client-side validation + Demo confirmation only; no `fetch`, XHR, external form service, CRM or email API.
4. No response-time SLA, availability promise, office-location verification or staffed-department claim.
5. The map treatment is a non-interactive illustrative placeholder; no map SDK/API and no fabricated coordinates.
6. Social links use existing config-driven hooks and stay hidden when config values remain `#`.
7. No LocalBusiness/Organization contact-point structured-data claims are introduced from fictional Demo values.

## Contact Routing Contract
Stable route keys:
- `general` → `site.email` → `[data-orx-email="trade"]`
- `rfq` → `site.rfqEmail` → `[data-orx-email="rfq"]`
- `supplier` → `site.suppliersEmail` → `[data-orx-email="suppliers"]`
- `partner` → `site.partnersEmail` → `[data-orx-email="partners"]`

Valid URL state:
- `?topic=general`
- `?topic=rfq`
- `?topic=supplier`
- `?topic=partner`

Rules:
- missing/invalid topic normalizes to `general` without fabricating any server state.
- route-card actions select the corresponding form topic and scroll/focus the form.
- AR/EN desktop + mobile language links preserve the normalized topic.
- current topic is visible in the form and page runtime markers for QA.

## Form Contract
Required:
- enquiry type
- contact name
- business email
- message
- consent acknowledging Demo/non-live behavior

Optional:
- company / organization
- phone

Validation:
- native semantic fields + local JS validation support
- invalid fields receive `aria-invalid=true`
- summary alert receives focus on invalid submit
- successful Demo validation reveals an explicit no-transmission confirmation and does not clear the form automatically

## Page Composition
1. Breadcrumb + compact contact hero.
2. Four contact-route cards with route purpose and config-driven email.
3. Contact details strip: main phone / illustrative address / business hours.
4. Split contact workspace:
   - enquiry form
   - route summary / Demo boundary panel.
5. Illustrative map placeholder using current config address text only.
6. Config-driven social-link block; automatically absent when no verified URLs exist.
7. Final CTA to RFQ / Submit Product routes rather than duplicating their specialized forms.

## UX / Accessibility
- Arabic RTL and English LTR are first-class.
- Route cards are buttons/links with explicit accessible labels.
- Form labels remain visible; placeholder text is never the sole label.
- Error and Demo confirmation states use `role="alert"` / `role="status"` appropriately.
- All targets are keyboard accessible and maintain at least the existing global touch-target baseline.
- No page-local navigation/footer fork.
- Responsive verification: 390 / 820 / 1366 / 1536.

## SEO / Page Identity
Canonical URLs:
- `https://example.com/ar/contact.html`
- `https://example.com/en/contact.html`

Required:
- one H1
- canonical + ar/en/x-default hreflang
- OG title/description/url/image
- JSON-LD: WebPage + BreadcrumbList only
- no LocalBusiness / Organization / ContactPoint schema based on Demo contact data

## Dependencies
- `assets/css/origex-tokens.css`
- `assets/css/origex-foundation.css`
- `assets/css/origex-components.css`
- `assets/css/origex-shell.css`
- `assets/css/origex-contact.css`
- `assets/js/config.js`
- `assets/js/config-engine.js`
- `assets/js/origex-ui.js`
- `assets/js/origex-contact.js`
- local `assets/icons/sprite.svg`

## PS7 Gate — PASS
- AR/EN source/content/SEO/config-route contract: PASS
- form Demo truthfulness and zero network submission: PASS
- topic/query/language state: PASS
- config email/phone/address/business-hours/social hooks: PASS
- rendered AR/EN 390/820/1366/1536: **8/8 PASS**
- form validation + route selection + invalid topic + Demo confirmation/reset: PASS
- Global Navigation V1 + Global Footer V1: PASS
- F05 Icon Integrity: **56 AR/EN pages / 0 missing references**
- zero TARGET/client leakage: PASS
- QA evidence: `docs/PG27-QA-REPORT-V1.md` + `qa/pg27-contact/`
- final evidence commit: `7cfffde78233c087ee2381247470bb024d3689e1`

PS8 remains deployed Cloudflare browser acceptance and is not claimed by CI alone.
