# ORIGEX — PG30 Privacy | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Canonical file: `privacy.html`  
Status: PS7 — IMPLEMENTED / CI QA PASS

## Purpose
Provide a professional bilingual sample privacy-policy layout for the ORIGEX commercial template while making it explicit that the text is a structural Demo and is not ready-to-publish legal advice or a jurisdiction-specific privacy policy.

## Canonical Content Authority
Arabic Master:
- Intro: `هذا نص نموذجي يوضح هيكل صفحة سياسة الخصوصية داخل القالب. يجب مراجعته وتعديله بواسطة صاحب الموقع أو مستشاره القانوني وفقًا لطريقة جمع البيانات والقوانين المطبقة قبل النشر.`
- Sections: Information Collected / Use / Cookies / Third Parties / Retention / Rights / Contact / Update Date.

English Adaptation:
- `Sample privacy structure only; buyer/legal adviser must adapt to actual data practices and applicable law.`

ORVEAX STD-CNS01:
- do not add a cookie banner merely because websites often have one;
- consent UI is only appropriate when actual technologies or legal requirements justify it;
- no fake consent controls or persistence claims;
- commercial-template privacy/consent patterns must disclose buyer integration/legal-review responsibility.

## Frozen V1 Main Features
- sample legal structure
- table of contents
- updated-date state
- contact reference
- legal disclaimer

## Page Composition
1. Standard Global Navigation V1 shell.
2. Privacy hero with explicit `DEMO LEGAL TEMPLATE` framing.
3. Prominent legal-demo disclaimer preserving the exact Arabic canonical Intro and English meaning parity.
4. Policy metadata row: page status, updated-date placeholder, configured contact reference.
5. Accessible Table of Contents.
6. Eight canonical sections in this order:
   - Information Collected
   - Use
   - Cookies
   - Third Parties
   - Retention
   - Rights
   - Contact
   - Update Date
7. Final replace-before-production checklist / contact CTA.
8. Standard Global Footer V1.

## Legal-Demo Content Contract
- The page demonstrates structure and writing hierarchy only.
- It must not claim compliance with GDPR, CCPA, Qatar PDPL, Saudi PDPL, UAE PDPL or any other law.
- It must not state that a specific legal basis, retention period, data transfer mechanism, DPO, supervisory authority, processor list or user right definitely applies.
- Any examples use conditional language such as `may`, `if used`, `where applicable`, and must direct the buyer to document actual practices.
- The template must not fabricate analytics, tracking, cookies, CRM, marketing automation or third-party processor usage.
- The Cookies section must explicitly state that ORIGEX does not add a consent banner by default and that the buyer should add one only when the real technology/legal implementation requires it.
- The existing static Demo forms do not justify claiming that production submissions are stored or processed by ORIGEX.

## Updated-Date Contract
- No real policy effective date is fabricated in the commercial package.
- Default visible value: `Replace before production` / `يُستبدل قبل النشر`.
- Buyer must replace it after legal review and whenever the production policy materially changes.
- No automatic current-date generation is used because that would falsely imply a legal review occurred on build/runtime date.

## Contact Contract
- Use `ORIGEX_CONFIG.site.email` through the existing `data-orx-email="trade"` hook.
- Demo email remains clearly configurable and does not create a privacy-office/DPO claim.
- Contact route points to `contact.html`.

## SEO / Page Identity Contract
Classification: **NOINDEX — DEMO LEGAL SAMPLE / BUYER REVIEW REQUIRED**.

Required default commercial-package behavior:
- `<meta name="robots" content="noindex,follow">`
- no canonical/hreflang requirement for the unreviewed Demo legal sample
- Open Graph may describe the page as a template privacy structure
- no LegalService, Organization, PrivacyPolicy or jurisdiction-specific structured-data claim
- buyer may deliberately change indexability only after replacing the sample with reviewed production legal content

Page identity:
- SEO ID: PG30
- File AR: `ar/privacy.html`
- File EN: `en/privacy.html`
- Title AR: `سياسة الخصوصية — نموذج توضيحي | ORIGEX`
- Title EN: `Privacy Policy — Demo Template | ORIGEX`
- Meta AR: `هيكل توضيحي لصفحة سياسة الخصوصية ضمن قالب ORIGEX، يجب مراجعته وتعديله وفق ممارسات البيانات والقوانين الفعلية قبل النشر.`
- Meta EN: `A sample ORIGEX privacy-policy structure that must be adapted to the buyer's real data practices and applicable law before publication.`
- H1 AR: `سياسة الخصوصية — نموذج توضيحي قابل للتخصيص.`
- H1 EN: `Privacy policy — a customization-ready Demo structure.`
- Primary internal links: Contact / Home

## UX / Accessibility
- Arabic RTL and English LTR first-class.
- Exactly one H1.
- Table of Contents uses real anchor links and descriptive labels.
- Each policy section uses a unique heading ID and semantic `<section>`.
- Sticky desktop TOC must fall back to normal flow on mobile/tablet.
- Minimum interactive target sizing follows shared system.
- Focus states remain visible.
- No legal meaning is encoded by color alone.
- Responsive verification: 390 / 820 / 1366 / 1536.

## Design Direction
- Premium editorial/legal layout rather than a wall of text.
- Narrow readable measure for long-form content.
- Sticky TOC on large screens, stacked on smaller screens.
- Strong legal-demo disclosure near the top.
- Reusable `origex-legal.css` shared with PG31 Terms.
- No page-specific JavaScript required; native anchors plus global shell/config runtime are sufficient.

## Dependencies
- `assets/css/origex-tokens.css`
- `assets/css/origex-foundation.css`
- `assets/css/origex-components.css`
- `assets/css/origex-shell.css`
- `assets/css/origex-legal.css`
- `assets/js/config.js`
- `assets/js/config-engine.js`
- `assets/js/origex-ui.js`
- `assets/icons/sprite.svg`

## PS7 Gate
PASS — final evidence `13dab1fe2c8711687b38e87eec5032ff3f038b8c`:
- exact Arabic canonical Intro PASS
- English meaning parity PASS
- all 8 frozen privacy sections PASS
- Table of Contents/anchor integrity PASS
- updated-date placeholder/no fabricated legal-review date PASS
- configurable contact reference PASS
- NOINDEX legal-demo contract PASS
- no fabricated law/compliance/processor/cookie-technology claims PASS
- no fake cookie/consent banner PASS
- rendered AR/EN 390/820/1366/1536 = 8/8 PASS
- keyboard/focus/touch target checks PASS
- Global Navigation V1 + Global Footer V1 PASS
- F05 Icon Integrity PASS — 62 pages / 0 missing references
- zero TARGET/client leakage

PS8 remains deployed browser acceptance after the buyer/demo deployment state is verified. The sample must not be treated as publication-ready legal text at PS8 without explicit buyer legal replacement/review.
