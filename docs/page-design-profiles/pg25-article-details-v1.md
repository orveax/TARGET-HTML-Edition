# ORIGEX — PG25 Article Details | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M5 — Proof / Resources / Compliance / Content  
Status: PS6 — FROZEN FOR BUILD  
Canonical file: `article-details.html`

## Purpose
Provide a premium readable B2B editorial-detail layout connected to PG24 Insights, demonstrating article metadata, structured typography, share actions, related content and a commercial next step without introducing a CMS or presenting Demo editorial material as live market intelligence.

## Canonical Content Authority
Arabic Master:
- Title: `ما المعلومات التي يحتاجها المشتري قبل طلب السعر؟`
- Thesis: `RFQ المفيد يبدأ بهوية المنتج والكمية والوجهة والتوقيت ومتطلبات التعبئة والمستندات المطلوبة.`
- CTA: `لديك طلب محدد؟ أرسل RFQ منظم.`

English Adaptation:
- Title: `What Information Does a Buyer Need Before Requesting a Quote?`
- CTA: `Have a specific requirement? Submit a structured RFQ.`

PG24 Insights provides the stable Demo article IDs, titles, categories, dates, reading times and excerpts for `article-001..009`. Article 001 is the canonical fully specified PG25 example. Article 002–009 detail bodies are clearly labeled ORIGEX Demo editorial extensions derived from their frozen PG24 listing topics; they are not live market intelligence or external factual claims.

## Frozen Main Features
Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.
1. Article header
2. Metadata
3. Content typography
4. Share links
5. Related articles
6. CTA

## Editorial / Demo Contract
- All nine V1 article states are fictional ORIGEX Demo editorial content.
- No live market data, price forecast, legal/regulatory advice, investment advice, measured commercial outcome, client claim, certification claim or guarantee.
- No new `articles.json` domain is introduced in V1.
- Core fallback content remains semantic HTML for article 001 so the page remains meaningful without JavaScript.
- Alternate article states are stored as page-local semantic `<template data-article-template>` records.
- Dates and reading times are Demo metadata inherited from PG24 and do not imply current research.

## Article State Contract
Canonical query: `?id=article-001` through `?id=article-009`.
- Missing `id` → article-001.
- Valid `id` → render matching Demo record.
- Invalid `id` → visible neutral invalid-ID notice + article-001 fallback; do not silently imply the invalid record exists.
- AR/EN language switch preserves a valid `id`; invalid/missing state normalizes to article-001.
- Related articles exclude the current article and link to stable PG24 IDs.
- Previous/next article navigation is allowed as a usability enhancement inside the approved related-content family.

## Share Contract
- Share actions are user-initiated only.
- Include Copy Link plus Email / LinkedIn / WhatsApp links.
- Runtime may compose the current page URL for these actions.
- No analytics, tracking pixels or auto-open behavior.
- Copy action uses the Clipboard API when available and a safe fallback.

## Runtime Contract
Runtime: `assets/js/origex-article-details.js`.
Allowed:
- hydrate valid article ID;
- render page-local template record;
- preserve valid ID across language switch;
- update previous/next and related links;
- generate user-initiated share URLs;
- accessible copy-status feedback.

Prohibited:
- remote API/CMS fetch;
- local/session storage;
- analytics dependency;
- fabricated view/share counts;
- dynamic SEO mutation intended to emulate server-side article routes.

## Information Architecture
Breadcrumb → Article Header / Metadata → Editorial Boundary → Article Body → Share Actions → Previous/Next → Related Articles → Commercial CTA.

## Visual Direction
Premium B2B editorial detail page: constrained reading column, strong title hierarchy, compact metadata, restrained callouts, readable lists/checklists, sticky-capable but non-obstructive share rail on wide screens, one-column mobile flow, no lifestyle-blog decoration.

## Navigation / Footer
- Standard Global Navigation V1.
- `article-details.html` parent mapping = `insights.html`.
- Explore current; Insights current in Mega Menu and Mobile Drawer.
- Global Footer V1 exact.
- Language switch preserves valid article ID.

## SEO / Page Identity
Because V1 demonstrates multiple article states through a query parameter in one static HTML file, the static SEO contract represents the canonical Demo default article (`article-001`). Buyers must create dedicated static routes or CMS-backed article URLs before production indexing of multiple articles.

### Arabic
- File: `ar/article-details.html`
- Title: `ما المعلومات التي يحتاجها المشتري قبل طلب السعر؟ | ORIGEX`
- Description: `مقال Demo يوضح المعلومات الأساسية التي تجعل طلب السعر أكثر وضوحًا: المنتج والكمية والوجهة والتوقيت والتعبئة والمستندات.`
- H1: `ما المعلومات التي يحتاجها المشتري قبل طلب السعر؟`
- Canonical: `https://example.com/ar/article-details.html`

### English
- File: `en/article-details.html`
- Title: `What Information Does a Buyer Need Before Requesting a Quote? | ORIGEX`
- Description: `A Demo article showing the core information behind a clearer RFQ: product identity, quantity, destination, timing, packaging and required documents.`
- H1: `What Information Does a Buyer Need Before Requesting a Quote?`
- Canonical: `https://example.com/en/article-details.html`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, `Article` + `BreadcrumbList` JSON-LD for the default Demo article only. No author biography claim, Organization endorsement, Review, Rating, Offer or performance schema.

## Accessibility / Responsive
- one visible H1 after hydration;
- semantic `<article>` and heading hierarchy;
- metadata readable without icons alone;
- share buttons/links have accessible labels;
- copy feedback uses `aria-live=polite`;
- related cards and previous/next links keyboard accessible;
- no horizontal overflow at 390/820/1366/1536;
- touch-target baseline applies;
- Arabic RTL / English LTR tested independently;
- reduced-motion foundation inherited.

## Exit Gate
PS7 only after source/editorial-safety/runtime/navigation/footer/icon/client-leak QA + rendered AR/EN 390/820/1366/1536 + valid/default/invalid ID + language preservation + copy/share + previous/next + related-article interaction QA all PASS. PS8 remains gated by deployed Cloudflare browser acceptance.

QA rerun trigger: canonical Global Navigation V1 normalized after initial `nav-drift` evidence; PG25 must pass again on the normalized shell before PS7 promotion.

Copyright © ORVEAX.
