# ORIGEX — PG31 Terms | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Canonical file: `terms.html`  
Status: PS6 — FROZEN FOR BUILD

## Purpose
Provide a professional bilingual sample Terms of Use layout for the ORIGEX commercial template while making it explicit that the content is a structural Demo only and is not ready-to-publish legal terms for any business or jurisdiction.

## Canonical Content Authority
Arabic Master:
- Exact Intro: `هذه شروط نموذجية لأغراض تصميم القالب فقط ولا تمثل شروط استخدام جاهزة لأي نشاط تجاري. استبدلها بنص قانوني مناسب لنشاطك ودولتك قبل النشر.`
- Sections: Site Use / Information Accuracy / Enquiries / IP / External Links / Liability Placeholder / Governing Law Placeholder / Contact.

English Adaptation:
- Exact boundary: `Sample terms for template demonstration only; not ready-to-publish legal terms.`
- English must preserve Arabic meaning without strengthening any legal or commercial claim.

VQ1 / Website Standards Baseline requirements:
- build directly on the shared legal reading shell;
- TOC / anchors / numbering;
- AR/EN long-form parity;
- lists and semantic tables;
- contextual navigation;
- Demo / legal boundary;
- consume frozen Website Standards from first implementation;
- no broad legacy-page backfit during PG31.

## Frozen V1 Main Features
1. Legal Demo hero and boundary.
2. Legal sibling/context navigation: Privacy / Terms.
3. Status / updated-date / contact metadata.
4. Accessible Table of Contents.
5. Eight canonical Terms sections.
6. Long-form lists and one semantic customization matrix.
7. Before-publish checklist.
8. Contact / Home CTA.

## Page Composition
1. Global Navigation V1.
2. Terms hero with explicit `DEMO LEGAL TEMPLATE` framing.
3. Prominent canonical Demo disclaimer.
4. Context navigation between `privacy.html` and `terms.html`.
5. Metadata row: Demo status / updated-date placeholder / configured contact.
6. Section header + TOC + long-form reading column.
7. Eight sections in this exact order:
   - Site Use
   - Information Accuracy
   - Enquiries
   - Intellectual Property
   - External Links
   - Liability Placeholder
   - Governing Law Placeholder
   - Contact
8. Semantic customization matrix outside the eight canonical clauses.
9. Replace-before-production checklist.
10. Contact / Home CTA.
11. Global Footer V1.

## Legal-Demo Contract
- The page demonstrates structure, hierarchy and customization points only.
- It must not create enforceable terms for ORIGEX Demo or for a future buyer by implication.
- It must not claim that browsing alone forms a contract, that all information is accurate, that an enquiry is accepted, that products are available, or that a supplier/distributor relationship exists.
- It must not invent warranty exclusions, liability caps, indemnities, governing law, court venue, arbitration rules, consumer-right waivers, sanctions/export obligations, tax rules, payment terms or IP ownership beyond the template-level customization instruction.
- `Liability` and `Governing Law` remain explicit placeholders that require buyer/legal-adviser replacement.
- External-link language must not imply ORVEAX controls third-party destinations.
- Enquiry / RFQ / supplier / partner form references remain non-binding Demo routes until the buyer defines real legal/commercial handling.
- Product, market, certification and resource content remains illustrative where already marked Demo in the product.

## Updated-Date Contract
- No effective date or legal-review date is fabricated.
- Default visible value: `Replace before production` / `يُستبدل قبل النشر`.
- The buyer replaces this only after the production terms have actually been reviewed.
- Runtime/build date is never treated as legal-review evidence.

## Contact Contract
- Use the existing `data-orx-email="trade"` config hook.
- Demo email remains configurable and must not be presented as a legal-department address.
- General contact route: `contact.html`.

## Context Navigation Contract
- A compact legal navigation block appears before the long-form document.
- `Privacy` links to `privacy.html`.
- `Terms` links to `terms.html` and carries `aria-current="page"` on PG31.
- The global mega/mobile navigation remains unchanged; PG31 stays under the `Explore` context.

## Structured Data / Table Contract
The customization matrix is presentation content, not legal advice.
- Semantic `<table>` with `<caption>`, `<thead>`, `<tbody>`, `<th scope>`.
- Columns: Area / Demo state / Buyer action.
- Use a horizontal-scroll wrapper on narrow screens where necessary.
- Do not collapse relational table data into generic cards by default.
- Mixed LTR values inside Arabic remain directionally readable.

## SEO / Page Identity Contract
Classification: **NOINDEX — DEMO LEGAL SAMPLE / BUYER REVIEW REQUIRED**.

Required default behavior:
- `<meta name="robots" content="noindex,follow">`
- no canonical / hreflang requirement for the unreviewed Demo legal sample
- Open Graph may identify it as a Demo Terms template
- no legal / jurisdiction / TermsOfService structured-data claim
- buyer may deliberately change indexability only after replacing the sample with reviewed production terms

Page identity:
- SEO ID: PG31
- File AR: `ar/terms.html`
- File EN: `en/terms.html`
- Title AR: `شروط الاستخدام — نموذج توضيحي | ORIGEX`
- Title EN: `Terms of Use — Demo Template | ORIGEX`
- Meta AR: `هيكل توضيحي لشروط الاستخدام ضمن قالب ORIGEX، يجب استبداله ومراجعته قانونيًا وفق نشاط الموقع ودولته قبل النشر.`
- Meta EN: `A sample ORIGEX Terms of Use structure that must be replaced and legally reviewed for the buyer's real business and jurisdiction before publication.`
- H1 AR: `شروط الاستخدام — نموذج توضيحي قابل للتخصيص.`
- H1 EN: `Terms of use — a customization-ready Demo structure.`

## Standards Adoption — First Implementation
PG31 consumes the frozen Website Standards baseline directly.

### STD-DIM01
- Reusable legal TOC/context controls use the approved **48px Control M / touch target** tier.
- No page-local arbitrary interactive sizes.

### STD-DATA01
- Semantic customization matrix preserves row/column relationships.
- Responsive horizontal scrolling is preferred over meaning-destroying card conversion.
- AR/LTR mixed data behavior is verified.

### Bilingual / Accessibility
- Arabic RTL / English LTR are first-class.
- Exactly one H1.
- Eight matching section IDs and equivalent user goal / legal boundary.
- Native anchors with visible focus states.
- Long Arabic and English copy must wrap without clipping or horizontal page overflow.
- Inline email / URL values remain readable in RTL.
- Desktop sticky TOC becomes normal flow below 992px.
- Responsive verification: 390 / 820 / 1366 / 1536.

## Design Direction
- Reuse `assets/css/origex-legal.css`; no separate PG31 stylesheet unless a verified page-only need exists.
- Premium editorial/legal reading layout, not a wall of equal cards.
- Contextual sibling navigation is distinct from the main global navigation.
- Lists and the semantic matrix are integrated into the reading rhythm.
- No PG31-specific JavaScript: native anchors + global shell/config runtime only.

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
Promote only after:
- exact Arabic canonical Intro PASS;
- exact English Demo boundary PASS;
- all 8 frozen Terms sections PASS in the same order;
- TOC / anchor / numbering integrity PASS;
- contextual Privacy / Terms navigation PASS;
- lists + semantic table + STD-DATA01 responsive behavior PASS;
- updated-date placeholder / no fabricated effective or review date PASS;
- configurable contact hook PASS;
- NOINDEX legal-demo contract PASS;
- no invented liability / governing-law / venue / warranty / contract / enquiry-acceptance claim PASS;
- no PG31-specific JS PASS;
- STD-DIM01 48px legal navigation/control target PASS;
- rendered AR/EN 390/820/1366/1536 = 8/8 PASS;
- keyboard / focus / TOC / language-switch interactions PASS;
- Global Navigation V1 + Global Footer V1 PASS;
- F05 Icon Integrity PASS;
- zero TARGET/client leakage.

PS8 remains deployed browser acceptance. A real production website must replace and legally review this Demo content before any claim that its Terms are publication-ready.
