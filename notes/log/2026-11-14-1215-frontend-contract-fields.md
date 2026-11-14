# Frontend: proposed file-contract fields to the engine

The three files are decided (DECISIONS); the fields are not. Sent to Engine Code for agreement:

- `data/sites.json`: per site `id, name, lat, lon_e, source, truncated`, `masks` keyed by mast height in m
  (`"0"`, `"2"`, `"10"`), each 360 horizon elevations in deg, true azimuth clockwise from north, curvature included.
  Optional `reference_stats` per site and mast (engine's sun %, Earth %, longest night) so the page can show
  engine-vs-browser agreement. Same 4 site ids and coordinates as the page (A C1, B Shackleton S, C GR1, D MP1).
- `data/heights.bin`: Float32 little-endian, row-major, row 0 = north edge (+y), metres above the 1737.4 km sphere,
  NaN = no data. Display only (3D view), e.g. +/-60 km at 240 m (501 x 501, ~1 MB, UNVERIFIED estimate).
- `data/terrain_meta.json`: `nx, ny, pixel_m, x_min, y_max, crs, source, h_min, h_max`; +x toward 90 E, +y toward 0 E.

Open with the engine: azimuth bin convention (bin start vs bin centre), window size, delivery time.
The page's current `sites.json` loader expects `mask_deg`; it will be changed to `masks[mast]` once the engine confirms.
