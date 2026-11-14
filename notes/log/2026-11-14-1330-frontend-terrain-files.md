# Frontend: terrain files agreed (Eren chose option b, 13:25)

- `data/heights.bin` + `data/terrain_meta.json`: +/-60 km at 240 m, 501 x 501, Float32 LE, row 0 = north (+y), NaN nodata.
  Display only (3D view).
- `data/cap_heights.bin` + `data/cap_meta.json`: whole cap, 600 m, x/y -304000..+304000 m, 1013 x 1013, Float32 LE,
  ~4.1 MB (~2 MB gz, engine estimate, UNVERIFIED). Used by the browser for approximate masks at clicked/typed spots.
  Frontend asked for `dem_max_m` (7026) in `cap_meta.json` so the browser ray march uses the engine's auto-stop rule.
  The page will label those masks "approximate, 600 m terrain".
- Engine note: Shackleton S with the 20 m near field reads 70% (5 years) vs Glaser 81%: still unvalidated, do not quote.
- Files arrive once Eren says start building `pipeline/`.
- Engine confirmed: `cap_meta.json` gets `"dem_max_m": 7026.33`, the max of the full-resolution 80 m DEM, deliberately
  not the 600 m grid's own (lower) max, so rays stop slightly later and stay safe. Browser auto-stop must use the same rule:
  bound(d) = atan2((R+dem_max)*cos(d/R) - r0, (R+dem_max)*sin(d/R)), made non-increasing (reverse running max);
  stop when best elevation >= bound at the next step, or the ray leaves the grid. R = 1737400 m.
