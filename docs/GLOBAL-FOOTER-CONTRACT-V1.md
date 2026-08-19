# ORIGEX — Global Footer Contract V1

Product ID: ORX-P01  
Owner: ORVEAX  
Component: N04 — Footer  
Status: APPROVED / CANONICAL  
Effective: 2026-08-19

## 1. Purpose

This contract freezes one global footer structure for all standard AR/EN ORIGEX pages. A page may change its main content, current navigation state and conversion route, but it must not create a page-local footer fork.

The canonical baseline is the M1 N04 implementation already used by the Home family and supported by `assets/css/origex-shell.css`, `assets/js/config.js` and `assets/js/config-engine.js`.

## 2. Non-Negotiable Rule

- Exactly one `<footer class="orx-site-footer" data-orx-global-footer="v1">` per page.
- Arabic and English use the same structural composition.
- Labels/copy are localized; information architecture is not.
- Page-specific footer columns, page-specific link groups, alternate footer grids or local footer recoloring are prohibited.
- Footer contact values remain valid HTML fallbacks and expose the approved config hooks.
- Future pages consume N04; they do not recreate it.

## 3. Canonical Information Architecture

Four-column desktop composition:

1. **Brand** — ORIGEX light logo + fictional-demo company description.
2. **Explore** — Products / Suppliers / Markets / Resources.
3. **Contact** — trade email / phone / illustrative address.
4. **Business Hours** — config-driven bilingual business-hours rows.

Bottom strip:

- Product label: `ORIGEX — B2B Food Trading & Distribution HTML Template`
- Demo ownership/disclosure line.

Responsive behavior follows the shared N04 rules in `origex-shell.css`; page CSS must not override footer layout.

## 4. Required Hooks

Every canonical footer must contain:

- `.orx-site-footer`
- `[data-orx-global-footer="v1"]`
- `.orx-footer__grid`
- `.orx-footer__brand`
- `.orx-footer__title`
- `.orx-footer__links`
- `[data-orx-email="trade"]`
- `[data-orx-phone]`
- `[data-orx-address]`
- `[data-orx-business-hours]`
- `.orx-footer__bottom`

`config-engine.js` may enhance fallback contact/business-hours values but does not construct the footer.

## 5. Arabic Fallback Copy

Brand description:

`شركة تجريبية داخل قالب ORIGEX لعرض تجربة تجارة غذائية B2B تربط المنتجات والموردين والمشترين وشركاء التوزيع.`

Column labels:

- استكشف
- تواصل
- ساعات العمل

Explore links:

- المنتجات
- الموردون
- الأسواق
- الموارد

Contact fallback:

- `trade@example.com`
- `+974 0000 0000`
- `الدوحة، قطر — توضيحي`

Bottom disclosure:

`بيانات العرض توضيحية · © ORVEAX`

Email/phone fallbacks use `.orx-bidi` in RTL.

## 6. English Fallback Copy

Brand description:

`A fictional company inside the ORIGEX template demonstrating a B2B food-trading experience connecting products, suppliers, buyers and distribution partners.`

Column labels:

- Explore
- Contact
- Business Hours

Explore links:

- Products
- Suppliers
- Markets
- Resources

Contact fallback:

- `trade@example.com`
- `+974 0000 0000`
- `Doha, Qatar — illustrative`

Bottom disclosure:

`Demo data only · © ORVEAX`

## 7. Footer vs. Page Content Boundary

The footer does not change to advertise the current page. Page-specific conversion content belongs in the page Final CTA (S06), not N04.

Examples of prohibited drift:

- replacing the four-column footer with `Explore / Company / Actions` on detail pages;
- removing business-hours hooks from selected page families;
- adding supplier/product IDs to footer links;
- using a separate disclosure sentence only on one page;
- using different logo size, footer class family or grid structure by page.

## 8. Governance / Automation

Canonical enforcement:

- `.github/scripts/normalize_global_footer.py`
- `.github/workflows/global-footer-qa.yml`

The normalizer is deterministic. `--check` fails when any existing AR/EN page differs from the canonical N04 footer.

Page-level QA workflows should include the global-footer check where practical. Global footer drift is a shared-shell defect and does not become a page-specific design choice.

## 9. Exceptions

There is currently **no footer exception** in V1. PG04 Landing may use an intentionally compact header, but its Page Design Profile still maps Navigation to `N01/N03/N04`; therefore it uses the same N04 footer.

Any future exception requires an approved Change Request and an explicit amendment to this contract.

Copyright © ORVEAX.
