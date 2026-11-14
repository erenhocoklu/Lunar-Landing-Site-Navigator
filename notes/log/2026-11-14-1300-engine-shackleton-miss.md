# Engine: Shackleton rim S miss, first diagnosis

Site S (Glaser 2018): -89.7849, 203.97 E. Published surface average illumination 81.0%.
All MEASURED (scratchpad), auto reach, 4 rays/deg, Sun as a disc, surface observer unless stated.

| Terrain | 1 year (2027) | 5 years (2027-2031) |
|---|---|---|
| 80 m only | 55.4% | 55.8% |
| 20 m near field (0-10 km) + 80 m far field | 70.3% | 70.0% |
| same, mast 2 m | | 82.8% |
| same, mast 10 m | | 86.3% |

## What this says
- **Not the time window:** 1 year vs 5 years changes < 0.5 points.
- **Terrain sharpness is the main cause:** 80 m terrain blurs the narrow rim and its close surroundings. Using 20 m within 10 km
  moves the result from 55.8% to 70.0%.
- **11 points still missing** at the surface (70.0 vs 81.0). Untested suspects: Glaser's terrain was sharper than 20 m near the
  site, exact coordinate, near-field radius (10 km here). Do not quote S until explained.
- Connecting Ridge C1 matched with 80 m only (76.2 vs 76.0); it should be re-run with the 20 m near field too, since the
  match may be partly luck.

## Consequence for the build
Named sites need the 20 m near field (decided DEM plan already says "20 m tiles near field"). The 1 km map spots will be
blurrier than named sites; label map values as approximate.
