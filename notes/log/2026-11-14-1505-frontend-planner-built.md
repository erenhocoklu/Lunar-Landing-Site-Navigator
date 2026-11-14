# Frontend: mission planner built (step 1-2 of the 1430 plan; local only, not committed)

Branch `frontend-mvp` in the local clone. Not committed, not pushed (waits for Eren's "push").

## Built
- **Planner panel** above the 3D view: site picker, first landing date (UTC), time span 1/2/3/5 y, mission presets
  (Crew 6 d, Robotic 13 d, Custom), sliders (mission length, min sunlight %, min Earth contact %, max longest night h,
  Sun above horizon at touchdown), mast 0/2/10 m (default 2 m; disabled until `sites.json` masks load), relay switch.
  Limits labelled "example values, not NASA requirements". Preset values (UNVERIFIED, examples): crew 6 d, sun >= 95%,
  Earth >= 50%, night <= 0 h; robotic 13 d, sun >= 70%, Earth >= 50%, night <= 48 h; touchdown >= 0 deg.
- **Landing-window calendar** (lead view): month rows x day cells, one landing at 00:00 UTC per day. Pass = filled blue;
  fail = hollow orange with the glyph of the first failing limit (sun, Earth, night, touchdown); every cell has an
  aria-label/tooltip with all failing limits and the numbers. Settings printed above the calendar. Click = timeline jumps there.
- **Funnel** under the sliders: landing days -> enough sun -> enough Earth (or "relay: skipped") -> night -> touchdown.
- **Ranking table**: every site under the same limits, sorted by passing landing days; first passing date; span sun %,
  Earth %, longest night ("≥" when clipped by the span edge); data column.
- **Provenance bar** at the top: ephemeris version + `generated_utc` + coverage, terrain mask status, and
  "Request a newer precalculation" = pre-filled GitHub issue (title, current data, settings, expected 2-6 min run).
- **Data-quality line** per site card: flat / LOLA / approximate mask, `err_m`, `effres_m` when the engine supplies them,
  published reference yes/no, "engine result not yet validated" when `validated: false`.
- Rules aligned with the engine: mask bin k = [k, k+1) looked up between bin centres; Earth visible = any part of the disc;
  night = Sun centre below the horizon.
- `sites.json` loader now reads the agreed format: per site `masks` keyed by mast height ("0", "2", "10"), 360 values each,
  plus top-level `generated_utc` / `versions`.
- `pipeline/make_subpoints.py`: now asks Horizons for 6 h steps directly, 2026-01-01 to 2036-01-01 (so a 5-year span can start
  up to 2031), and writes `generated_utc` + `versions`. `data/subpoints.json`: 14,609 rows, 556 KB (MEASURED).

## Measured (local browser test, flat horizon, so the numbers are placeholders and must not be quoted)
- 5-year rebuild of 4 sites: 87-89 ms in the browser (MEASURED, Chromium in the app's browser pane). Engine estimate shown: 14 ms.
- Robotic preset, 1 y from 2026-11-14, Connecting Ridge: 78 of 353 landing days pass (flat horizon; do not quote).
- Calendar cell click moves the timeline to that landing day (checked: 2027-01-13 -> t = 60 d).

## Not done / open
- Play button and the 3D yearly-average modes not re-tested (browser pane hidden, animation frames paused).
- Stacked Sun/Earth lanes for the chosen date (UI pattern 2) not built yet.
- Waiting on the engine: `sites.json` (masks, err/effres, psr_km, versions), `psr.json`, `heights.bin`, `cap_heights.bin`.
- Next: three.js view (step 3), PSR layer + filter (step 4).
