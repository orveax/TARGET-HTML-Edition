# ORIGEX — Page Stage Naming V1

Product: ORIGEX / ORX-P01  
Status: APPROVED / CANONICAL  
Effective: 2026-08-19

## Purpose

The legacy page-production lifecycle used `C0–C8`. That naming collided visually with the registered Component IDs `C01–C28`.

From this decision forward, the page-production lifecycle uses the prefix `PS` = **Page Stage**.

## Canonical Page Stage Lifecycle

```text
PS0 — Brief
PS1 — Arabic Draft
PS2 — Commercial Review
PS3 — English Adaptation
PS4 — UI Fit Review
PS5 — Legal / Demo Claims Review
PS6 — FROZEN / Ready for Build
PS7 — Implemented
PS8 — QA Passed / Closed
```

## Reserved Component Namespace

`C01–C28` remains reserved exclusively for registered UI Components.

Examples:
- `C02` Product Card
- `C04` Market Card
- `C12` Breadcrumb
- `C18` Specification Table

## Migration Rule

- New page work, living trackers and new documentation use `PS0–PS8` only.
- Historical commits, QA reports and evidence using legacy `C0–C8` remain valid and are not rewritten retroactively.
- Component IDs are not renamed.
- The semantic meaning of the lifecycle stages is unchanged; this is a naming clarification only.

## Quick Reference

- `M` = Milestone
- `PG` = Page / Layout ID
- `PS` = Page Stage
- `F` = Foundation
- `PT` = Pattern
- `P` = Primitive
- `C` = Component
- `S` = Section
- `N` = Navigation

Copyright © ORVEAX.
