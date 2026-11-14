# Credits pending

The repo's `CREDITS.md` is the master list (Participant Terms: every source cited, every non-NASA item
free or OSI-licensed, licence listed). Add new items here; Eren or Adrian moves them into the repo and
strikes them through here with a date.

| Item | Type (package/dataset/paper/media) | Licence | Used where | Added by |
|---|---|---|---|---|
| ~~NumPy~~ | package | ~~BSD-3-Clause (UNVERIFIED, check)~~ superseded 2026-11-14 by engine row below | engine | organizer seed |
| ~~GDAL / rasterio (whichever the engine uses)~~ | package | ~~MIT (UNVERIFIED, check)~~ superseded 2026-11-14 by engine rows below | engine | organizer seed |
| ~~pyproj~~ | package | ~~MIT (UNVERIFIED, check)~~ superseded 2026-11-14 by engine row below | engine tests | organizer seed |
| NumPy 2.4.2 | package | BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 (VERIFIED, installed package metadata) | engine | engine |
| SciPy 1.17.1 | package | BSD-3-Clause (VERIFIED, metadata classifier "OSI Approved :: BSD License") | engine (map_coordinates) | engine |
| rasterio 1.5.2 | package | BSD-3-Clause (VERIFIED, installed package metadata) | engine (DEM reading, /vsicurl) | engine |
| GDAL 3.12.2 (bundled inside the rasterio wheel) | library | MIT (UNVERIFIED here; GDAL's own licence file not read) | engine via rasterio | engine |
| pyproj 3.8.0 | package | MIT (VERIFIED, installed package metadata) | engine tests (projection cross-check) | engine |
| PROJ 9.8.1 (bundled inside the pyproj wheel) | library | MIT (UNVERIFIED here; PROJ licence file not read) | via pyproj | engine |
| affine 3.0.1 | package | BSD-3-Clause (VERIFIED, metadata; rasterio dependency) | via rasterio | engine |
| pytest 9.2.0 | package | MIT (VERIFIED, metadata) | engine tests | engine |
| LOLA LDEM_80S_80MPP_ADJ / 20MPP_ADJ (PGDA product 90, Barker et al. 2023, doi:10.3847/PSJ/acf3e1) | dataset | NASA data (cite paper + data doi:10.60903/gsfcpgda-lola-spole) | engine | engine |
| JPL Horizons API | dataset/service | NASA/JPL | engine (per-site Sun/Earth reference) | engine |
| Glaser et al. 2018 (C1, S illumination values) | paper | citation only | engine validation | engine |
| JPL Horizons API (sub-solar/sub-Earth points, q 14,15,19,20) | dataset/service | NASA/JPL | `data/subpoints.json` via `pipeline/make_subpoints.py`; page checks | frontend (in repo CREDITS.md, uncommitted) |
| De Rosa et al. 2012 (GR1, MP1 coordinates), arXiv:1208.5587 | paper | citation only | site list in `index.html` | frontend (in repo CREDITS.md, uncommitted) |
| IBM Plex Sans/Mono, Saira Condensed (Google Fonts) | media (font) | SIL OFL 1.1 (UNVERIFIED, check) | `index.html` (Adrian's original page) | frontend (in repo CREDITS.md, uncommitted) |
| Dwyer Cianciolo 2024, "Artemis Human Landing System Update" (NASA LaRC presentation, NTRS 20240009596) | paper/presentation | citation only (NASA) | slider defaults (slope, Earth/Sun masks, 6 deg) | engine |
| pyshp 3.1.8 | package | MIT (VERIFIED, installed package metadata) | engine (`build_psr.py`, reads the PSR shapefile) | engine |
| shapely 2.2.0 | package | BSD-3-Clause (VERIFIED, installed package metadata) | engine (`build_psr.py`, simplify + distance) | engine |
| LPSR_80S_20MPP_ADJ PSR shapefile (PGDA product 90, Barker et al. 2023) | dataset | NASA data (cite with the DEM) | `data/psr.json`, `psr_km` | engine |
