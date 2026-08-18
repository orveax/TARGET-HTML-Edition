# ORIGEX — Preview & Responsive QA Policy

**Product:** ORX-P01  
**Owner:** ORVEAX  
**Status:** ACTIVE — applies to every preview until production packaging.

## Language Rule

1. Arabic is the default preview language.
2. English is the secondary preview language.
3. Every reviewable page must expose both Arabic and English.
4. Review artifacts must not show English-only content unless the artifact is explicitly an English-language QA case.

## Preview Modes

Every reviewable page should be available as:

- **Raw Preview** — the page without review chrome.
- **Device Frame Preview** — preview-only responsive test frame.

The Device Frame is not product UI and must be excluded/removed before final production/marketplace packaging.

## Common Screen Matrix

### Primary QA Set

| Class | Viewport |
|---|---:|
| Mobile Small | 360 × 800 |
| iPhone Common | 390 × 844 |
| Mobile Large | 412 × 915 |
| Tablet Portrait | 768 × 1024 |
| Large Tablet | 1024 × 1366 |
| Laptop Common | 1366 × 768 |
| Desktop | 1440 × 900 |
| Full HD | 1920 × 1080 |

### Minimum page gate

No page may be marked responsive PASS until it has been checked at minimum on:

- 390 × 844
- 768 × 1024
- 1024 × 1366
- 1366 × 768
- 1440 × 900

and in **both Arabic and English**.

## Device Frame Requirements

The preview frame must remain simple and review-focused:

- Arabic/English switch
- screen-size selector
- grid view for common screens
- focus view for one exact viewport
- raw-page link
- visible viewport dimensions
- no dependency on production navigation or page code

## Production Removal Rule

Everything under `preview/` is review infrastructure unless explicitly promoted later. Marketplace packaging scripts/checklists must exclude the preview frame itself while preserving the actual template pages and documentation.
