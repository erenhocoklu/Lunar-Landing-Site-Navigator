# Engine: heavy runs on the home server (session engine-heavy-runs)

Ran on a team member's home server (outputs not in the repo).
Numbers are MEASURED by that session. The laptop engine session has read its report but has not re-run them.

## Data checks
- 80 m and 20 m DEM downloaded, sizes match (20 m: 2.7 GB in 638 s).
- 5-year sky table vs per-site Horizons: max error Sun el 0.00068, Earth el 0.00055, Earth az 0.0060 deg (matches laptop).

## Named sites (5 years 2027-2031)
- **Using 20 m terrain beyond 5 km changes nothing:** NEAR = 5/10/20/40 km and 20 m everywhere agree within 0.04 points.
- **The site's own height value matters most.** Shackleton S: site height from 80 m DEM -> 55.85% (= laptop's 55.8%);
  from 20 m DEM (5.3 m higher) -> 83.7% with 80 m terrain, **79.1% with 20 m near terrain** (Glaser 2018: 81.0%). 2 m mast: 83.4%.
- Laptop's earlier 70.0% (log 1300) is superseded. Likely cause (engine reading, not re-tested): the laptop took the max of the
  20 m near mask and a full 80 m mask, so blurry 80 m terrain next to the site still counted.
- **Connecting Ridge C1 at the surface is fragile:** 84.5% (80 m only) vs 55.8% (20 m near terrain), caused by a 0.7 deg
  slope within 100 m of the site; ignoring terrain closer than 100 m gives 81.6%. 2 m mast: 85.6% (Glaser 2 m: 88.0%).
  The laptop's 76.2% "match" (2027 only, 80 m) was luck. Do not quote C1 surface values.

## Whole pole (1 km)
- Masks: 104,185 spots in 252 s on 12 workers (2.4 ms/spot); 37.5 MB raw, 15.0 MB gz.
- 75% of spots have at least one ray that reached the map edge before the automatic stop: horizon may be slightly low there.
- Fast masks vs reference (200 spots): 0.26 deg low on average; sun % +0.96 points on average, +11.7 at worst.
- Monthly sun/Earth % for 60 months: 132 s; 12.5 MB raw, 7.5 MB gz (0.5% steps).
- Best 5-year sun on the 1 km grid: 65.8%. The grid misses narrow ridges (C1, S), so the map undersells the best spots.

## Consequences for the build (recommendation, Eren decides)
1. Site height from the 20 m DEM; 20 m terrain to 5-10 km, 80 m beyond.
2. Show 2 m mast values as the headline; surface values swing with tiny slopes. Validation slide: S 2 m 83.4% / surface 79.1%
   vs Glaser 81.0% surface; C1 2 m 85.6% vs Glaser 88.0% 2 m.
3. The 1 km map is a screening layer, labelled approximate; named sites carry the real numbers.
