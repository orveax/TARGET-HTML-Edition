# Page Fidelity Matrix

This matrix is the mandatory conversion control for TARGET HTML Edition.

## Status vocabulary

- `PENDING` — not converted yet
- `BASELINE` — copied/reproduced for fidelity, not yet commercially generalized
- `MATCHED` — section/function verified against the source website
- `GENERALIZED` — client-specific content/assets replaced without reducing the experience
- `QA PASS` — responsive, RTL/LTR, interaction and visual QA complete

## Public page inventory

| # | Source route | HTML Edition route | Conversion | Visual | Interaction | RTL/LTR | Commercial generalization |
|---|---|---|---|---|---|---|---|
| 01 | `index.html` | `index.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
| 02 | `about.html` | `about.html` | PENDING | PENDING | PENDING | PENDING | PENDING |
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

The homepage cannot be marked `MATCHED` unless every source section is accounted for.

| Section / system | Status | Rule |
|---|---|---|
| Global header | PENDING | Preserve desktop + mobile behavior |
| Mega menu | PENDING | Preserve hierarchy and interactions |
| Language toggle | PENDING | Preserve AR/EN + dir switching |
| Hero | PENDING | Preserve composition, hierarchy and responsive behavior |
| Commercial route visual | PENDING | Preserve the visual/functional concept |
| Trust strip / facts | PENDING | Preserve full card/fact family |
| How We Work / capability cards | PENDING | Preserve all cards and content roles |
| Product/category section | PENDING | Preserve complete category family |
| Why / differentiation section | PENDING | Preserve full section |
| Process / steps | PENDING | Preserve all steps |
| Supplier/opportunity CTA | PENDING | Preserve conversion intent |
| FAQ / supporting conversion content if present | PENDING | Do not silently remove |
| Global footer | PENDING | Preserve full navigation/resource/contact hierarchy |
| Contextual utilities | PENDING | Reproduce only where source behavior exists |

## Non-negotiable rule

A section may only be removed when:

1. it contains client-only information that cannot legally or commercially ship, **and**
2. an equivalent generic component preserves the same UX role, **or**
3. the removal is explicitly documented as a marketplace product decision.

No section is removed merely to make the code shorter.
