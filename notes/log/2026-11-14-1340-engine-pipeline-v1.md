# Engine: pipeline v1 built (branch `engine`, worktree `engine-wt`, uncommitted)

Worktree `space-apps-alba-iulia-2026\engine-wt` on new branch `engine` (from `english-ui`), so FRONTEND's uncommitted
files in the main clone stay untouched. Nothing committed or pushed.

## Files
- `pipeline/dem.py`, `horizon.py`, `metrics.py`, `build_sites.py`, `build_terrain.py`, `tests/test_engine.py`, `README.md`.
- `data/sites.json` (60 KB), `heights.bin` (1.0 MB, 500x500 at 240 m), `cap_heights.bin` (3.6 MB, 950x950 at **640 m**) + metas.
  640 m instead of 600 m: exact 8x8 block means of the 80 m DEM.

## Checks (MEASURED)
- 11 tests pass, including a regression against the independent home-server code: S 0 m 79.1%, S 2 m 83.4%, C1 2 m 85.6%
  match to 0.1 points.
- Orientation: Malapert MP1 height 4945 m in the cap grid vs 4969 m in the 80 m DEM.

## 5-year sun % (2027-2031, 20 m terrain within 10 km, 80 m beyond, auto reach)
| Site | 0 m | 2 m | 10 m | Earth 2 m | Longest night 2 m | Reference |
|---|---|---|---|---|---|---|
| A C1 | 55.8 | 85.6 | 92.3 | 58.6% | 146 h | Glaser 2018: 76.0 (0 m), 88.0 (2 m) |
| B S | 79.1 | 83.4 | 86.3 | 57.0% | 216 h | Glaser 2018: 81.0 (0 m) |
| C GR1 | 21.8 | 47.3 | 71.7 | 56.8% | 651 h | none checked |
| D MP1 | 41.0 | 72.0 | 79.2 | 64.5% | 349 h | none checked; 7 bins hit the map edge |
GR1 and MP1 are unvalidated; the large 0 m -> 2 m jumps again show near-site slopes matter.

## Problems
- PGDA `_ERR` / `_EFFRES` 20 m layers did not read (tile decode error, then HTTP 403 to GDAL while curl worked). The DEM kept
  working after a pause. `err_m` / `effres_m` are null; retry later. Do not hammer PGDA.
- `psr_km` null until `build_psr.py` (next).
