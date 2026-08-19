# ORIGEX — Change Request CR-001 — PG33 Company Profile

Product ID: ORX-P01  
Owner: ORVEAX  
Date: 2026-08-19  
Status: APPROVED

## Change

Add one new V1 layout:

**PG33 — Company Profile / الملف التعريفي**  
Canonical filename: `company-profile.html`  
Languages: Arabic + English  
Milestone ownership: M3 — Company / Business / Market

## Scope Impact

Previous V1 scope:
- 32 unique layouts
- approximately 64 AR + EN HTML pages

Approved scope after CR-001:
- **33 unique layouts**
- approximately **66 AR + EN HTML pages**

No existing PG ID is repurposed or removed.

## Reason

The validated TARGET reference includes a high-value Company Profile web page that gives buyers a strong B2B trust/resource pattern: focused company overview, quick facts, internal exploration routes, document/resource presentation and a conversion route.

This pattern adds commercial value beyond the About page and is reusable across trading, distribution, supplier and manufacturer template variants.

## Source Reference

Reference only:
- `orveax/target/src/pages/company-profile.astro`

Reusable pattern:
- focused profile hero;
- company snapshot / at-a-glance facts;
- routes to deeper website sections;
- company-profile resource/document panel;
- document metadata / trust layer;
- final commercial CTA.

## Separation Rule

Do not transfer TARGET-specific facts, Qatar claims, names, documents, contact information, proprietary assets or verified-file metadata.

ORIGEX implementation must use fictional/demo content and ORVEAX-owned/distributable media only.

## Navigation Impact

PG33 is added to the canonical Company group in `GLOBAL-NAVIGATION-CONTRACT-V1.md`.

## Page Gate

PG33 follows the same PS lifecycle:
PS0 → PS6 frozen content/design/SEO contract → PS7 implementation/CI QA → PS8 deployed final acceptance.

## Decision

CR-001 is approved. The product architecture is updated to 33 layouts. No redesign or technology change is introduced.

Copyright © ORVEAX.