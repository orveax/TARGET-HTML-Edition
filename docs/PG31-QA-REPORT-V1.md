# ORIGEX — PG31 Terms QA Report V1

Product ID: ORX-P01  
Page: PG31 — Terms  
Canonical file: `terms.html`  
Status: **PS7 — IMPLEMENTED / CI QA PASS**  
Date: 2026-08-20

## Scope
PG31 was implemented directly against the frozen Website Standards baseline and the shared legal reading shell established for PG30. The page is a bilingual commercial-template legal Demo, not publication-ready Terms of Use.

## Canonical Content
Arabic exact Intro:
`هذه شروط نموذجية لأغراض تصميم القالب فقط ولا تمثل شروط استخدام جاهزة لأي نشاط تجاري. استبدلها بنص قانوني مناسب لنشاطك ودولتك قبل النشر.`

English boundary:
`Sample terms for template demonstration only; not ready-to-publish legal terms.`

Eight frozen sections:
1. Site Use
2. Information Accuracy
3. Enquiries
4. Intellectual Property
5. External Links
6. Liability Placeholder
7. Governing Law Placeholder
8. Contact

## Implementation
- AR: `ar/terms.html`
- EN: `en/terms.html`
- Shared legal UI: `assets/css/origex-legal.css`
- Page profile: `docs/page-design-profiles/pg31-terms-v1.md`
- QA runner: `.github/scripts/qa_pg31_terms.py`
- QA workflow: `.github/workflows/pg31-terms-qa.yml`

No PG31-specific JavaScript was introduced.

## Standards Consumed From First Implementation
### STD-DIM01
- Legal TOC and contextual legal navigation use the 48px Control M / target tier.
- Shared legal CSS was normalized once rather than patched locally in PG31.

### STD-DATA01
- The customization matrix uses semantic table anatomy: caption / thead / tbody / scoped column and row headers.
- Narrow screens preserve row/column relationships through an internal horizontal-scroll wrapper.
- The document itself does not gain horizontal overflow.

### Bilingual / Accessibility
- Arabic RTL and English LTR.
- One H1 per language.
- Equivalent section IDs, order and legal boundary.
- Arabic mixed-LTR email is explicitly isolated.
- Sticky desktop TOC becomes normal flow below 992px.
- Context navigation, TOC, language counterpart and table focus are keyboard-verifiable.

## Legal-Demo Safety
PASS:
- `robots=noindex,follow`.
- No canonical or hreflang requirement on the unreviewed Demo legal sample.
- No legal/jurisdiction structured-data claim.
- No fabricated effective date or legal-review date.
- No default liability cap or universal warranty exclusion.
- No named governing country/court/arbitration forum.
- No implication that a Demo enquiry/RFQ/submission creates acceptance, supply, representation, exclusivity or pricing obligation.
- No claim that external destinations are controlled or guaranteed by ORVEAX.
- Contact remains configurable through the existing `data-orx-email="trade"` hook.

## Final Source / Standards QA
`qa/pg31-terms/source-report.json`
- Global failures: **0**.
- CSS failures: **0**.
- Arabic: 8 sections / 8 TOC links / 2 long-form lists / 4 semantic-table rows / 0 failures.
- English: 8 sections / 8 TOC links / 2 long-form lists / 4 semantic-table rows / 0 failures.

## Final Rendered QA
`qa/pg31-terms/rendered-report.json`
- Arabic 390 / 820 / 1366 / 1536: **4/4 PASS**.
- English 390 / 820 / 1366 / 1536: **4/4 PASS**.
- Total rendered matrix: **8/8 PASS**.
- TOC / legal context / language switch / semantic table focus: **PASS** in AR and EN.
- Mobile semantic table uses internal scrolling and does not create document overflow.

## Global Gates
- Global Navigation V1: PASS.
- Global Footer V1: PASS.
- F05 Icon Integrity after PG31: **64 AR/EN pages / 0 missing references**.

## Evidence
- PS6 profile: `d53ca6f4ba82de90714829eeb7020a72ba72cb10`
- Shared legal standards update: `bb3cd43ab37a24b1c21092c2941e0e63980a1610`
- EN build: `d2913ba0e89ac9cf52bf6f7cad09c396dc459b8f`
- AR build: `52e6539830bd0df5b936ad70160063a9a7e3411f`
- QA runner: `bb7fc8a7203bcfff4aa6c5213b8d7894de4e3895`
- QA workflow: `40e7d5815ae2ceef0de4945323c473c972b40c54`
- Final QA evidence: `d626862192626418ed806101dd60288d69456d09`
- PS7 profile promotion: `db4d36867c9a00eecf079f4ac5089de7d59411c4`

## Remaining Gate
PS8 remains deployed Cloudflare browser acceptance. The Demo Terms must be replaced and legally reviewed for the real production business before any publication-ready legal claim.

## Next Canonical Action
PG32 — Components / Elements Library: implement as the **Design System QA Laboratory + Buyer Component Reference** using the frozen standards baseline from first implementation.
