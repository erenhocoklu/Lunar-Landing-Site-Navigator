# Engine + frontend: calendar cross-check passed (2027, 4 cases x 365 landing days)

Page (JS, 6 h sub-point table + cubic interpolation, sampled at whole hours) vs engine answer key (Python, hourly Horizons table),
same sites.json masks. After the page switched to the engine's chord-area Sun-disc formula (MEASURED by FRONTEND):
- Passing days identical: A 146/146, B 109/109, C 11/11, D 192/192. **Disagreeing days: 0 of 1,460.**
- Max per-day sun gap 0.047-0.088 points; Earth gap <= 0.32 points; night gap 1 h, one grazing case below.
- Before the switch (linear disc fraction): 1 disagreeing day (B 2027-02-25, sun 94.52 vs 95.07 at a 95% limit).

Grazing case: D 10 m, landing 2027-06-20: night 43 h (page) vs 30 h (engine). At 2027-07-01 17:00 the Sun centre sits
0.0001 deg from the horizon: below it on the page, above it in the engine, so one long run vs two runs. 0.0001 deg is far below
the two ephemeris paths' agreement (~0.005 deg); neither is wrong. No pass/fail change.
