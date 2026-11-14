# Research: has the landing-window calendar been tried? why not in industry? (manager, 3 researchers)

Notes: `..\research_notes\Landing window calendar prior attempts\` (earlier_attempts.md, what_sets_dates.md, critiques_failures.md).

## Verdict
- Not built before as a public interactive, constraint-driven tool (absence of evidence, not proof; Space Apps 2026 gallery and most of 78 repos unchecked).
- The analysis itself is old: static one-rule studies tied to one mission (ESA 2012 shelved, VIPER 2024 cancelled then revived, Wueller 2026 = closest: 130 sites, midsummer 2025-2032, fixed 6.5-day rule). Iris Datalabs API = averages only. NASA Ames Lunar Browser (STK) outputs lighting-constrained landing windows internally (snippet only).
- Industry: trajectory design sets the date; lighting anchors the landing day (robotic, land at local sunrise) or filters opportunities (crewed: ~55 descents/yr from NRHO). No standalone lighting calendar product; it lives inside trajectory tools.
- No lander lost to a wrong lighting forecast; tipped landers died from panels facing away (IM-1, IM-2, SLIM). Low Sun hurt IM-2 navigation.
- Slips: 1 day absorbed, missed window ~1 month, missed season ~1 year (Chang'e-7). NASA OIG: CLPS task orders slip ~14 months on average (critiques note).
- Not a flight tool: CLPS companies own their planning. Users = early studies, proposals, teaching, public.

## Pitch framing (recommended, Eren decides)
- "Trajectory gives you candidate dates; we show in seconds which sites survive them." Never claim it picks launch dates.
- Crewed = column view (date -> sites). Robotic = row view (site -> calendar). Keep both.
- Show ranges, an assumptions box (DEM, mast height, Earth rule, "geometry only, not a radio link"), Sun elevation at touchdown, one validation number.
