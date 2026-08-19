# ORIGEX — B2B Food Trading & Distribution HTML Template

**Product ID:** ORX-P01  
**Owner / Author:** ORVEAX  
**Status:** Product Foundation complete — M1 clean implementation start

ORIGEX is a premium Arabic-first bilingual HTML template product for B2B food trading, import, wholesale, distribution, manufacturers, suppliers and market-access workflows.

This repository is the commercial ORIGEX product. It is intentionally separated from the original TARGET client implementation.

## Start Here

**Canonical project control:** [`docs/PROJECT-HQ-V1.md`](docs/PROJECT-HQ-V1.md)

Do not start implementation from historical commits or reference/source-map files.

## Current State

```text
M0 — PRODUCT FOUNDATION: CLOSED / COMPLETE
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: CLEAN START / READY
M2–M8: NOT STARTED
```

A hard audit on 2026-08-19 removed pre-foundation Build 02–05 implementation and superseded planning files from the active tree. Git history remains the archive.

## Frozen V1 Stack

- HTML5
- CSS3
- Bootstrap 5.3.8 — infrastructure/layout foundation
- Vanilla JavaScript
- ORIGEX Design System
- `config.js` customization layer
- JSON structured data where approved
- Arabic RTL + English LTR

No React, Vue, Astro runtime, Tailwind, jQuery, mandatory Node/build process or heavy animation framework in the V1 buyer package.

## Scope

- 32 unique layouts
- Arabic + English ready pages
- V1 Main Features only
- Additional Features preserved in V1.1 backlog
- static-first, responsive, accessible and SEO-ready architecture

See [`docs/SCOPE-FREEZE-V1-FINAL.md`](docs/SCOPE-FREEZE-V1-FINAL.md).

## Core Control Files

- [`PROJECT-HQ-V1.md`](docs/PROJECT-HQ-V1.md) — current state and authority map
- [`PROJECT-RULES-V1.md`](docs/PROJECT-RULES-V1.md) — implementation rules
- [`IMPLEMENTATION-STATUS-V1.md`](docs/IMPLEMENTATION-STATUS-V1.md) — live execution tracker
- [`PRODUCT-FOUNDATION-COMPLETE-V1.md`](docs/PRODUCT-FOUNDATION-COMPLETE-V1.md) — foundation closure
- [`MILESTONE-PLAN-V1.md`](docs/MILESTONE-PLAN-V1.md) — delivery sequence
- [`QA-DEFINITION-OF-DONE-V1.md`](docs/QA-DEFINITION-OF-DONE-V1.md) — exit gates
- [`ASSET-LICENSE-REGISTER-V1.md`](docs/ASSET-LICENSE-REGISTER-V1.md) — dependencies/assets/licensing

## Implementation Rule

Before a page is built:

1. confirm PG ID / filename;
2. confirm V1 Main Features;
3. freeze content at C6;
4. complete the Page Design Profile;
5. use registered components only;
6. identify asset/license needs;
7. build Arabic and English together;
8. close only after full QA and Content C8.

## Repository Rule

Current branch policy is `main` only unless ORVEAX explicitly changes it.

Historical TARGET-derived source maps may inform fidelity, but client identity, contacts, proprietary data, client assets and unsupported claims must never enter ORIGEX.

Copyright © ORVEAX.
