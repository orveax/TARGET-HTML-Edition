# ORIGEX — PG15 Markets / Countries | Page Design Profile V1

Product: ORX-P01  
Milestone: M3 — Company / Business / Market  
Status: C6 — FROZEN FOR BUILD  
Canonical files: `ar/markets.html` + `en/markets.html`

## Source Authorities
- `docs/SCOPE-FREEZE-V1-FINAL.md` — PG15 Main Features.
- Notion Arabic Master Content — PG15.
- Notion English Adaptation — PG15.
- `docs/SEO-METADATA-PAGE-NAMING-V1.md`.
- M1 shared shell, component registry and ORIGEX design tokens.

## Commercial Purpose
Provide a reusable market-directory experience that demonstrates how a B2B food-trading template can organize country-level commercial context without presenting unverified market intelligence as fact.

## Frozen Main Features
1. Region / country filters.
2. Country cards.
3. Market map.
4. Channel tags.
5. Market overview.
6. CTA.

No additional V1.1 market intelligence, live trade data, regulatory datasets, buyer directories or dynamic external APIs are enabled in V1.

## Canonical Demo Markets
- Qatar
- Saudi Arabia
- United Arab Emirates
- Kuwait
- Bahrain
- Oman

All market facts beyond country identity are illustrative demo content. Buyer must replace market/channel notes with verified business information before publication.

## Page Structure
1. Hero + visible breadcrumb + demo disclosure.
2. Market Overview — explains how to read the demo directory.
3. Filter Surface — region selector + country filter chips.
4. Market Map — schematic GCC demo-region visualization; explicitly not geographic intelligence.
5. Country Cards — six canonical demo markets with channel tags and non-claim guidance.
6. Final CTA — route to PG14 Market Access / opportunity review.

## Interaction Contract
- Country chips filter the market cards client-side with minimal vanilla JS.
- Region selector supports `all` and `gcc`; current V1 demo dataset is GCC-only but control remains reusable for buyer expansion.
- Empty state is available if buyer configuration creates a filter combination with no results.
- No external map API.

## Visual Direction
- Premium B2B directory, not tourism or destination marketing.
- Market cards prioritize decision context and channel families over flags/decorative imagery.
- Schematic map is an abstract commercial network, not a geographic map.
- Final visual polish is deferred to M7; functional/responsive/RTL defects are fixed in page production.

## RTL / LTR
- Arabic: native RTL ordering and alignment.
- English: native LTR ordering and alignment.
- Filters, cards, channel tags and map labels must not rely on physical left/right properties.

## SEO / Page Identity
Arabic title: `الأسواق والدول | ORIGEX`  
English title: `Markets & Countries | ORIGEX`  
Canonical filenames: `markets.html`.  
AR/EN canonical + hreflang + x-default required.  
Structured data: `WebPage` + `BreadcrumbList` only; no fabricated LocalBusiness/market-statistics schema.

## QA Exit Gate
- Exactly six frozen PG15 feature families represented.
- Six canonical demo market cards present AR/EN.
- Filters work and preserve direction/accessibility.
- Market map is schematic and carries illustrative disclaimer.
- Channel tags present on every market card.
- No TARGET/client/CDN leakage.
- All local assets and icon references resolve.
- AR/EN rendered QA at 390 / 820 / 1366 / 1536 passes with no horizontal overflow.
- Shared Market navigation marks `markets.html` current on desktop/mobile.

Copyright © ORVEAX.
