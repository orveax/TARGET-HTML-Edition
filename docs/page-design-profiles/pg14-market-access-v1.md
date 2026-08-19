# ORIGEX — PG14 Market Access | Page Design Profile V1

Product ID: ORX-P01  
Page ID: PG14  
Milestone: M3 — Company, Business & Market  
Status: C6 — FROZEN FOR BUILD  
Owner: ORVEAX  
Language: Arabic-first RTL + English LTR

## 1. Canonical Purpose

PG14 explains a structured market-access decision route for a B2B food product without making market-entry, regulatory, buyer-demand, distribution or sales guarantees.

Audience: manufacturers, suppliers, brand owners, distributors and commercial teams evaluating a defined product against a target market and channel context.

Primary outcome: help the visitor understand what information is reviewed before a route-to-market conversation can progress.

## 2. Frozen V1 Scope

Exactly seven page blocks:
1. Market Access Hero.
2. Market-Entry Model.
3. Channel Model.
4. Fit Criteria.
5. Route-to-Market Process.
6. Opportunity Review.
7. Final CTA.

No market-size data, buyer lists, regulatory approvals, live country statistics, guaranteed distributor access, exclusivity claims or sales projections are included in V1.

## 3. Canonical Content Contract

### Arabic
H1: `دخول السوق يبدأ بتقييم المنتج والقناة والشريك المناسب.`

Support: `نظم المعلومات الأساسية للمنتج وحدد السوق والقنوات والمتطلبات قبل الانتقال إلى التفاوض أو التوزيع.`

Primary CTA: `راجع فرصة السوق`

### English
H1: `Market entry starts with product, channel and partner fit.`

Primary CTA: `Review Market Opportunity`

English implementation copy must preserve the Arabic commercial meaning and must not create stronger claims.

## 4. Section Intent

### 01 — Hero
State that market access begins with product facts, market context, channel relevance and partner fit before any commercial execution.

### 02 — Market-Entry Model
Present the evaluation model as four decision inputs:
- Product readiness.
- Market context.
- Channel relevance.
- Partner / operating fit.

### 03 — Channel Model
Use illustrative channel families only:
- Modern Retail.
- Wholesale.
- HoReCa.
- Specialty.
- Institutional.

Channels are examples for template demonstration, not buyer relationships or availability claims.

### 04 — Fit Criteria
Show what improves an initial review:
- defined product/specification.
- origin and supplier/manufacturer context.
- packaging and commercial information.
- target market.
- intended channel.
- relevant documents where available.

Also show what is not enough: undeveloped ideas or missing product/commercial basics.

### 05 — Route-to-Market Process
Four-step implementation model:
1. Define Product & Market.
2. Review Fit & Information.
3. Frame Channel & Partner Route.
4. Decide Commercial Next Step.

### 06 — Opportunity Review
Summarize three possible demo outcomes:
- Proceed to structured commercial discussion.
- Clarify missing information.
- Hold / redirect the opportunity.

No outcome implies acceptance or guarantee.

### 07 — Final CTA
Primary route: `Review Market Opportunity` / `راجع فرصة السوق`.
Secondary route: Markets / Countries page where relevant.

## 5. Design Direction

- Use the existing ORIGEX M1 shell, typography, spacing, buttons, cards, icons and final CTA.
- Market-access identity should feel analytical and commercial rather than geographic-tourism oriented.
- Hero visual is a CSS/HTML commercial route matrix; no new stock imagery is required.
- Reuse registered Lucide sprite icons only.
- Use logical properties and direction-neutral composition.
- Final aesthetic polish remains M7; functional/responsive/RTL defects are fixed now.

## 6. Component Mapping

- N01 Header.
- N02 Mega Menu.
- N03 Mobile Drawer.
- N04 Footer.
- S01 Section Header.
- S02 Split Hero.
- S06 Final CTA.
- C01 Feature Card.
- C04 Market Card where suitable.
- C05 Process Card.
- C11 CTA Card.
- C12 Breadcrumb.
- C22 Alert / Notice.
- P01/P02 Buttons.
- P11 Icon Container.

No new component family is introduced.

## 7. Market Navigation IA

PG14 belongs to the Market navigation family.

Required shared navigation state:
- Desktop Mega Menu: `Market Access` active when PG14 is current.
- Mobile Drawer: Market Access and Markets are discoverable as a reusable Market group.
- PG15 `Markets / Countries` will share the same Market group when built.

## 8. SEO / Page Identity Contract

SEO ID / Page ID: PG14  
Indexability: INDEX candidate  
Slug/File AR: `/ar/market-access.html`  
Slug/File EN: `/en/market-access.html`

Title AR: `الوصول إلى السوق وقنوات التوزيع | ORIGEX`  
Title EN: `Market Access & Route-to-Market | ORIGEX`

Meta Description AR: `صفحة توضيحية لتنظيم تقييم المنتج والسوق والقناة والشريك قبل الانتقال إلى مسار تجاري أو توزيع محتمل.`  
Meta Description EN: `A demo market-access page for structuring product, market, channel and partner-fit review before a potential commercial or distribution route.`

H1 AR: `دخول السوق يبدأ بتقييم المنتج والقناة والشريك المناسب.`  
H1 EN: `Market entry starts with product, channel and partner fit.`

Canonical AR: `https://example.com/ar/market-access.html`  
Canonical EN: `https://example.com/en/market-access.html`

hreflang: ar / en / x-default  
x-default: English demo route.

OG Title AR/EN: aligned to SEO title.  
OG Description AR/EN: aligned to page purpose.  
OG Image: existing ORIGEX-owned demo hero asset or neutral registered media placeholder.  
Schema: WebPage + BreadcrumbList only.

Breadcrumb AR: الرئيسية → الوصول إلى السوق  
Breadcrumb EN: Home → Market Access

Primary internal links:
- Capabilities.
- Markets / Countries.
- Submit Your Product.
- RFQ / Contact where appropriate.

## 9. Demo / Claims Controls

- All market/channel scenarios are illustrative template content.
- No market size, growth rate, buyer name, listing, regulation or approval claim is asserted.
- No guarantee of market entry, distributor appointment, exclusivity, buyer acceptance or commercial performance.
- Buyer must replace demo market content with verified business information before publication.

## 10. QA Exit Gate

Before PG14 can be marked C7 / CI QA PASS:
- AR/EN content parity.
- exact canonical H1s.
- seven frozen blocks present.
- canonical/hreflang/OG/schema valid.
- local assets only.
- all sprite icon references resolve.
- no TARGET/client/CDN leakage.
- Market navigation active/discoverable on desktop and mobile.
- responsive checks at 390 / 820 / 1366 / 1536 for AR + EN.
- no horizontal overflow.
- RTL/LTR correct.
- touch targets meet baseline.
- demo disclosure visible.

C8 remains dependent on the M3 Cloudflare batch browser acceptance gate.

Copyright © ORVEAX.
