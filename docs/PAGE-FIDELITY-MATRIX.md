# Page Fidelity Matrix

This matrix is the mandatory conversion control for TARGET HTML Edition.

## Status vocabulary

- `PENDING` — not converted yet
- `BASELINE` — copied/reproduced for fidelity, not yet fully verified
- `MATCHED` — section/function verified against the source website
- `GENERALIZED` — client-specific content/assets replaced without reducing the experience
- `QA PASS` — responsive, RTL/LTR, interaction and visual QA complete

## Public page inventory

| # | Source route | HTML Edition route | Conversion | Visual | Interaction | RTL/LTR | Commercial generalization |
|---|---|---|---|---|---|---|---|
| 01 | `index.html` | `ar/index.html` + `en/index.html` | GENERALIZED | BASELINE | BASELINE | BASELINE | GENERALIZED |
| 02 | `about.html` | `ar/about.html` + `en/about.html` | GENERALIZED | BASELINE | BASELINE | BASELINE | GENERALIZED |
| 03 | `capabilities.html` | `how-we-work.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 04 | `products-companies.html` | `products-companies.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 05 | `qatar-market.html` | `market.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 06 | `suppliers.html` | `suppliers.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 07 | `contact.html` | `contact.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 08 | `company-profile.html` | `resources.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 09 | `faq.html` | `faq.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 10 | `privacy.html` | `privacy.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 11 | `terms.html` | `terms.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 12 | `404.html` | `404.html` | PENDING | PENDING | PENDING | PENDING | PENDING |

## Homepage section control

The homepage cannot be marked `MATCHED` until every source section is accounted for and responsive visual comparison is complete.

| Section / system | Status | Current implementation |
|---|---|---|
| Global header | BASELINE | Premium sticky shell exists in AR/EN |
| Mega menu | BASELINE | Hierarchy and open/close interaction preserved |
| Language toggle | BASELINE | Dedicated `/ar/` and `/en/` routes; Arabic is primary |
| Hero | BASELINE | Eyebrow, H1, lead, 2 CTAs, media composition preserved |
| Commercial route visual | BASELINE | Source → ORIGEX → Market route preserved |
| Trust strip / facts | BASELINE | 4/4 trust items preserved |
| How We Work / capability cards | BASELINE | 4/4 cards preserved with number, role and metadata |
| Product/category section | BASELINE | Editorial panel + 5/5 categories + explore route |
| Why / differentiation section | BASELINE | 4/4 differentiation cards preserved |
| Process / steps | BASELINE | 4/4 ordered steps preserved |
| Supplier/opportunity CTA | BASELINE | RFQ / sales conversion intent generalized |
| FAQ / supporting conversion | BASELINE | 3/3 accessible accordion items; first open |
| Final conversion CTA | BASELINE | Kicker, headline, lead, disclaimer and 2 CTAs |
| Global footer | BASELINE | Full route/contact/legal hierarchy preserved |
| Contextual utilities | BASELINE | Language, mobile drawer, resource/contact routes preserved |

## Home 01 Build 04 notes — 2026-08-19

- Arabic and English are separate ready-to-use pages; Arabic remains the default review language.
- Home 01 now accounts for all H01–H08 source sections.
- Client-specific Qatar/TARGET copy and identity were generalized while preserving the same UX role and section density.
- No ecommerce cart/checkout behavior was introduced; conversion remains B2B RFQ/product-enquiry oriented.
- Static structural QA and JavaScript syntax QA passed locally.
- `MATCHED` and `QA PASS` remain blocked until full visual/responsive review is completed against the source and the common-screen preview matrix.

## About Build 05 control — 2026-08-19

| Section | Status | Current implementation |
|---|---|---|
| A01 Hero | BASELINE | Eyebrow, H1, lead, profile resource link, commercial media and 2 facts |
| A02 Who We Are | BASELINE | 2 explanatory paragraphs, editorial panel and 4/4 facts |
| A03 Vision & Mission | BASELINE | 2/2 full content cards |
| A04 Commercial Role | BASELINE | Source → ORIGEX → Market three-node flow |
| A05 Commercial Clarity | BASELINE | 4/4 trust cards + boundary note |
| A06 Final Conversion | BASELINE | Company Profile panel + product/opportunity CTA panel |

- Arabic and English are separate ready-to-use pages; Arabic remains primary.
- TARGET/Qatar client identity and owned imagery were removed and replaced with reusable B2B demo content/CSS artwork without reducing the source section roles.
- Static HTML structure, section counts, AR/EN pairing and client-data leakage checks passed locally.
- Visual screenshot QA remains pending because the current Chromium environment does not produce a stable screenshot session; no false `MATCHED`/`QA PASS` status is recorded.

## Non-negotiable rule

A section may only be removed when:

1. it contains client-only information that cannot legally or commercially ship, **and**
2. an equivalent generic component preserves the same UX role, **or**
3. the removal is explicitly documented as a marketplace product decision.

No section is removed merely to make the code shorter.
