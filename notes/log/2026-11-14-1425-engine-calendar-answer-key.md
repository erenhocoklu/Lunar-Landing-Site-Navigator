# Engine: calendar answer key for MUST-SHIP (B) (branch `engine`, commit 07c5981, local only)

- (A) real masks for the 4 named sites: already done (sites.json, log 1340; page loads it, frontend cross-check log 1535).
- (B) support: `pipeline/windows.py` = Python reference of FRONTEND's calendar definition (log 1505); writes
  `data/windows_reference.json` (229 KB): 2027, one landing/day at 00:00 UTC, per day pass + failing limits + numbers.
- (C) time span: FRONTEND's sky table already runs 2026-2036; nothing needed from the engine.

## Answer-key results (MEASURED, hourly sky, sites.json masks, FRONTEND's example presets, not requirements)
| Case | Passing landing days 2027 | Main first-failing limit |
|---|---|---|
| A C1, 2 m, robotic 13 d | 146 / 365 | Earth (117), sun (92) |
| B S, 2 m, crew 6 d | 109 / 365 | sun (155), Earth (96) |
| C GR1, 0 m, robotic, relay on | 11 / 365 | sun (331) |
| D MP1, 10 m, robotic | 192 / 365 | sun (95), night (59) |

Asked FRONTEND to compare day by day and report disagreements. Risk flagged: if the page evaluates at 6 h steps,
night lengths and touchdown cells near the limits will differ from the hourly key. 13 tests pass.
