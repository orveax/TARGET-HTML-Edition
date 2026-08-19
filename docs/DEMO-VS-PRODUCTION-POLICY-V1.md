# ORIGEX — Demo vs Production Policy V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Approval Date: 2026-08-19

This document separates ThemeForest/demo presentation behavior from buyer production behavior.

## 1. Core Rule

The ORIGEX live demo is a controlled fictional commercial experience. The buyer package is a production-ready template foundation that requires the buyer to replace demo identity, contact data, domain values and business-specific claims before publishing.

Demo data must never silently become production data.

## 2. Demo Identity

The demo may use fictional:
- company names.
- supplier/brand names.
- product names.
- market examples.
- case studies.
- contact data placeholders.

Rules:
- fictional facts remain internally consistent through the Demo Dataset.
- no fake real-world endorsement.
- no real client identity leakage.
- no fabricated certification/award/review presented as a real claim.
- illustrative commercial metrics must be labeled clearly when they could be interpreted as factual.

## 3. Demo Contact Data

Demo contact values use controlled placeholders, for example:
- non-operational example email/domain values where appropriate.
- clearly fictional phone/WhatsApp examples.
- illustrative address wording.

No personal or client contact information is shipped unintentionally.

## 4. Demo Assets

Preview stock photography may be used only after license/source verification and according to the Image/Media System.

Third-party preview photography is not included in the buyer ZIP by default unless explicit redistribution rights are recorded.

Buyer package visual defaults use ORVEAX-owned placeholders, SVG/CSS graphics or assets with documented redistribution rights.

## 5. Demo SEO / Indexability

The ThemeForest/live-preview deployment may use `noindex` or equivalent environment controls when appropriate to prevent fictional demo pages from being treated as a real operating business.

The buyer package itself remains SEO-ready and includes documented canonical/hreflang/metadata placeholders.

Production SEO is never hard-coded to the ORIGEX demo domain.

## 6. Production Replacement Checklist

Before production deployment, the buyer should replace or confirm:

- site/company name.
- logo and brand assets.
- production domain.
- email addresses.
- phone/WhatsApp.
- physical address.
- social links.
- legal entity details.
- privacy/terms content.
- products and product specifications.
- suppliers/brands.
- markets/countries.
- certifications and compliance claims.
- case studies/testimonials.
- downloadable documents.
- metadata titles/descriptions.
- canonical/hreflang URLs.
- Open Graph image/URLs.
- structured data values.
- analytics/integration IDs if added by buyer.

## 7. Config vs Editorial Replacement

Global repeated business identity belongs in approved `config.js` fields.

Editorial content, products, suppliers, markets and legal text remain in HTML/approved data files according to the Content/Data Architecture. `config.js` must not become a CMS.

## 8. Production Safety Rules

Prohibited in the commercial package:
- live ORVEAX/client API keys.
- analytics IDs tied to ORVEAX/client accounts.
- production credentials.
- private endpoints.
- personal data.
- TARGET/client identity or proprietary assets.
- demo canonical URLs that cannot be changed.

## 9. Documentation Requirement

Buyer documentation must contain a visible `Before You Publish` checklist based on this policy.

The final M8 package review must confirm that demo-only values and preview-only assets are clearly disclosed.

## 10. Change Control

Demo presentation may evolve without changing production architecture, but any change that affects what is shipped to buyers, indexability defaults, data ownership or required replacement steps must update this policy and the packaging checklist.

Copyright © ORVEAX.