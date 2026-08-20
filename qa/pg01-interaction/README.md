# PG01 Rendered Interaction QA

Generated: 2026-08-20T01:26:39Z

| Lang | Mode | Result | Checks |
|---|---|---|---|
| AR | desktop | PASS | mega_present=PASS · mega_open=PASS · mega_escape_close=PASS · faq_present=PASS · faq_toggle=PASS · announcement_present=PASS · announcement_close=PASS |
| AR | mobile | PASS | drawer_present=PASS · drawer_open=PASS · drawer_escape_close=PASS |
| EN | desktop | PASS | mega_present=PASS · mega_open=PASS · mega_escape_close=PASS · faq_present=PASS · faq_toggle=PASS · announcement_present=PASS · announcement_close=PASS |
| EN | mobile | PASS | drawer_present=PASS · drawer_open=PASS · drawer_escape_close=PASS |

## Scope

- Desktop: mega menu open + Escape close, FAQ open/close, announcement dismiss.
- Mobile: drawer open + Escape close + body scroll-lock state.
- AR and EN are executed independently in rendered Chrome.
