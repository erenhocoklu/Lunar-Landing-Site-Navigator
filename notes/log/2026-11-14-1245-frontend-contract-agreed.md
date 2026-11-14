# Frontend: contract fields agreed with the engine (except heights.bin)

Engine replied OK to the 2026-11-14-1215 proposal with 5 changes. Frontend accepts 1-4.

1. **Reach**: `"reach": "auto"` (Eren's 12:40 decision: a ray stops when even the DEM maximum, 7026 m, cannot rise
   above the horizon found so far; engine MEASURED 0.0000 deg difference vs walking to the map edge at 5 sites).
   Per site `stop_km_max` and `edge_rays`; `truncated = edge_rays > 0`.
2. **Bins**: bin k = true azimuth [k, k+1) deg clockwise from north, value = max of 4 sub-rays. Look up by interpolating
   between bin centres k+0.5. **Frontend TODO:** the page's `profAt` treats k as the bin value at azimuth k; shift by 0.5 deg.
3. `"dem": "LDEM_80S_80MPP_ADJ"`, `"dem_near": null` until the 20 m near field exists.
4. `reference_stats` per site per mast (window 2027 hourly): `sun_pct` (disc-fraction mean), `earth_pct` (any part of a
   0.95 deg Earth disc above the mask), `longest_night_h` (Sun centre below the mask). Site B `validated: false`
   (55% vs Glaser 81%, unexplained, do not quote).
   **Frontend TODO:** the page currently counts Earth visible when more than half the disc is up; align with "any part".
5. **heights.bin: OPEN for Eren** (added to DECISIONS by the engine). Eren decided a ~600 m grid of the whole cap
   (display + approximate masks for clicked spots). The frontend's +/-60 km window cannot give click masks (rays need
   ~200-270 km). Options: (a) one whole-cap 600 m grid ~1013x1013 ~4 MB (UNVERIFIED size), (b) 240 m display window +
   coarse whole-cap grid, (c) no browser masks, precomputed 1 km pole masks (~16 MB gz). Frontend recommends (a):
   one file, and a clicked spot gets a real (approximate) terrain horizon in the browser.

Delivery: engine ships `sites.json` (A-D, masts 0/2/10, 2027 reference stats) ~1 h after Eren says start.
