# Research: lunar ice and site selection (manager session, deep research, 4 researchers)

Report: `..\reports\Lunar ice and site selection.md` (notes in `..\research_notes\Lunar ice and site selection\`).

## Findings (sources in the report)
- NASA (CASSA) selects in stages: hard gates (slope, sunlight for the stay, Earth in view, landing accuracy, orbit/date windows, checked on a calendar), then "weighted Figures of Merit" whose weights are NOT public.
- Ice/PSR access shaped where regions were drawn ("close enough to a PSR for a moonwalk", 2022); it is not a public numeric criterion.
- Studies turn ice access into geometry: PSR within ~2 km (walking), path slope <= 15-20 deg, optional Diviner < 110 K. Wueller et al. 2026 (JGR Planets, open access): 130 sites with coordinates, 21 with an accessible < 110 K PSR within 2 km. NASA ISRU study: 5 / 10 km rover tiers.
- Data: PGDA 90 has a 20 m PSR GeoTIFF + shapefile (1,531 PSRs > 1 km2), same product as our DEM. Real ice detections are sparse (M3: ~3.5% of cold traps). PSR != ice.
- SpaceX: no public site-analysis method. NASA 2024 HLS deck (NTRS 20240009596, quoted from PDF text by a researcher): landing slope < 10 deg over 100 m, EVA slope < 20 deg over 2 km, masks Earth vis < 25% and Sun vis < 5%. Label: "NASA 2024 site-analysis masks (presentation, not formal requirements)". Open the PDF once before putting on a slide. 2019 HLS values: 0-8 deg (goal 5 deg); OIG 2026: 8 deg tilt limit.
- VIPER metrics worth copying: longest darkness while Earth is down; working days available.

## Recommendation for DECISIONS item 11 (Eren decides)
Display + filter, no ice score: PGDA 90 PSR overlay labelled "Permanently shadowed (LOLA model)", one "PSR within R km" filter with sourced presets 2 / 5 / 10 km, straight-line distance column. Never write "ice", "distance to ice" or "NASA standard".
