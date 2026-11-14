# Frontend: engine files wired in, browser matches the engine

Copied from `engine-wt\data\` (engine branch, uncommitted there) into the repo's `data\` (uncommitted, branch `frontend-mvp`):
`sites.json`, `heights.bin`, `terrain_meta.json`, `cap_heights.bin`, `cap_meta.json`. The page's loader read `sites.json` without
changes (masks keyed "0"/"2"/"10").

## Cross-check (MEASURED)
Page set to first landing date 2027-01-01, span 1 y (8760 h, the engine's 2027 window), each mast height; browser values
(page ephemeris from `subpoints.json`, engine masks) vs `reference_stats.by_mast` in `sites.json`:
- Sun %: max difference 0.10 points (A 2 m: 85.80 vs 85.90). Earth %: max 0.04 points. Longest night: max 1 h.
- All 12 site x mast combinations agree within those bounds. Two independent ephemeris paths (engine: per-site Horizons;
  page: sub-point table + parallax) give the same answer.

Example (2027, 2 m mast): A 85.8% sun, B 83.5%, C 48.2%, D 72.7% (MEASURED in the browser; engine: 85.9 / 83.6 / 48.2 / 72.7).
Validation against papers stays the engine's domain (see engine notes: S surface 79.1 vs Glaser 81.0, C1 2 m 85.6 vs 88.0).

## Not yet used by the page
`heights.bin` / `terrain_meta.json` (3D view) and `cap_heights.bin` / `cap_meta.json` (640 m, 950 x 950: approximate masks
for custom spots). `err_m`, `effres_m`, `psr_km` are null in this version.
