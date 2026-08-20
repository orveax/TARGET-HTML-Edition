# ORIGEX — PG29 Coming Soon | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Canonical file: `coming-soon.html`  
Status: PS6 — FROZEN FOR BUILD

## Purpose
Provide a premium bilingual under-construction / prelaunch state that keeps the visitor oriented, exposes verified contact paths, and supports an optional buyer-configured launch date without fabricating dates, countdowns, subscriptions, or social availability.

## Canonical Content Authority
Arabic Master:
- H1: `نجهز هذه الصفحة بمعلوماتها التجارية الكاملة.`
- Support: `استخدم بيانات التواصل الحالية إذا كان لديك طلب عاجل، أو عد لاحقًا بعد اكتمال التحديث.`
- CTA: `تواصل معنا`
- Rule: any launch date or countdown is buyer-configured and never fabricated.

English Adaptation:
- H1: `We’re preparing this page with its complete commercial information.`
- Rule: countdown/date is buyer-configured, never fabricated.

## Frozen V1 Main Features
- logo
- status message
- launch date / countdown
- subscribe UI
- social links
- contact link

## Page Composition
1. Standard Global Navigation V1 shell.
2. Branded Coming Soon hero with ORIGEX logo/status treatment and canonical H1/support.
3. Optional launch panel driven only by `ORIGEX_CONFIG.comingSoon.launchDate`.
4. Countdown displayed only when a valid future date is configured.
5. Neutral “date not configured” state when no valid date exists; no invented fallback date.
6. Demo subscribe UI with email validation only and explicit no-network/no-subscription disclosure.
7. Social links rendered only for configured non-placeholder URLs.
8. Contact CTA to `contact.html` plus direct configured email fallback.
9. Standard Global Footer V1.

## Launch / Countdown Contract
- New `comingSoon` config block is allowed because launch date/countdown is a frozen PG29 feature and `config.js` is the approved buyer customization layer.
- `launchDate` defaults to an empty string.
- Runtime may parse an ISO-compatible configured date and calculate days/hours/minutes/seconds locally.
- Invalid, empty or past dates must not generate a fake countdown.
- No browser storage, remote time service, network request or timezone claim is required.
- Countdown is presentation only and must not imply a guaranteed launch commitment.

## Subscribe UI Contract
- V1 includes subscription UI, not a subscription backend.
- Form validates email locally and never sends network requests.
- Success state must state that Demo validation passed and that a real email/marketing endpoint must be connected before production.
- No subscriber count, CRM list, newsletter-delivery or consent-record claim is fabricated.
- Form submission must not use fetch, XHR, external action URL, localStorage or sessionStorage.

## Social Contract
- Existing `ORIGEX_CONFIG.social` is authoritative.
- Links with `#`, empty, invalid or disabled values remain hidden.
- No social platform follower/count/availability claims.
- Use generic text links + local icons only; do not add third-party logo assets.

## SEO / Page Identity Contract
Classification: **NOINDEX / ENVIRONMENT-DEPENDENT UTILITY**.

Required:
- `<meta name="robots" content="noindex,follow">`
- no canonical/hreflang requirement for the default commercial-package utility asset
- Open Graph metadata may describe the prelaunch state
- no Product / Offer / Organization / Event structured-data claim for a fabricated launch
- no Event schema or `startDate` unless a production buyer deliberately replaces the utility implementation with verified launch data

Page identity:
- SEO ID: PG29
- File AR: `ar/coming-soon.html`
- File EN: `en/coming-soon.html`
- Title AR: `قريبًا | ORIGEX`
- Title EN: `Coming Soon | ORIGEX`
- Meta AR: `صفحة تجهيز مؤقتة ضمن قالب ORIGEX، مع وسيلة تواصل وحالة إطلاق قابلة للضبط دون اختلاق موعد.`
- Meta EN: `A configurable ORIGEX coming-soon utility with contact access and an optional buyer-defined launch state without a fabricated date.`
- H1 AR/EN: canonical master above
- Breadcrumb: not required for this utility state
- Primary internal links: Contact / Home

## UX / Accessibility
- Arabic RTL and English LTR are first-class.
- Exactly one H1.
- Status message is text, not color-only.
- Countdown units have visible labels and an accessible aggregate status line.
- Timer updates must not create a high-frequency live-region announcement.
- Subscribe field has an explicit label, correct email input type, local validation, clear error/success states and keyboard-accessible controls.
- Reduced motion follows the global system.
- Responsive verification: 390 / 820 / 1366 / 1536.

## Design Direction
- Premium, minimal launch-state composition rather than a generic maintenance screen.
- Strong brand field, large status typography, compact utility modules.
- Use ORIGEX tokens, Tajawal/Manrope and local icon sprite only.
- No third-party image, animation library, date library or background video.

## Dependencies
- `assets/css/origex-tokens.css`
- `assets/css/origex-foundation.css`
- `assets/css/origex-components.css`
- `assets/css/origex-shell.css`
- `assets/css/origex-coming-soon.css`
- `assets/js/config.js`
- `assets/js/config-engine.js`
- `assets/js/origex-ui.js`
- `assets/js/origex-coming-soon.js`
- `assets/icons/sprite.svg`

## PS7 Gate
Promote only after:
- exact Arabic canonical H1/support/CTA intent PASS
- English meaning parity PASS
- NOINDEX utility contract PASS
- default no-date state PASS
- valid future configured date countdown PASS
- invalid/past date no-fabrication behavior PASS
- Demo subscribe local validation + zero-network behavior PASS
- configured social visibility / placeholder hiding PASS
- contact link + configured email fallback PASS
- rendered AR/EN 390/820/1366/1536 PASS
- Global Navigation V1 + Global Footer V1 PASS
- F05 Icon Integrity PASS
- zero TARGET/client leakage

PS8 remains deployed browser acceptance and must verify the configured buyer/demo deployment state rather than assuming a launch date exists.
