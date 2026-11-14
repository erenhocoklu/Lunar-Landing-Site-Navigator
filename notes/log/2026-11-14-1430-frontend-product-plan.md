# Frontend: product plan answering Eren's 14:10-14:20 decisions (proposal, not built)

Inputs: DECISIONS Decided items 8, 9, 10, 11, relay switch, 3D view; UI research log 2026-11-14-1250; engine relay message.

## 3D view (Decided: not the old WebGL; FRONTEND proposes)
- three.js (MIT; pinned CDN version, ESM import map) `PlaneGeometry` in polar stereographic metres, heights from `heights.bin`
  (+/-60 km, 240 m, 501 x 501), curvature drop d^2/2R baked into z, vertical exaggeration slider, `OrbitControls`.
- Lighting: DirectionalLight from the real Sun direction (page ephemeris) with GPU shadow maps. These shadows are **visual only**
  (they only see the +/-60 km window). Every number on the page comes from 360-bin horizon masks. The UI says so.
- Sites as markers; PSR outlines as lines; click on terrain -> x,y -> lat/lon -> custom spot with an approximate mask from
  `cap_heights.bin` (browser ray march, engine's auto-stop rule).
- Why not keep the old code: no camera controls, picking or shadows; three.js gives those tested. Why not a globe: globes pinch at
  90 S (frontend-libs.md). Estimate 2-3 h (UNVERIFIED). Fallback if not at parity by Sat 22:00: keep the old view.

## Controls (Decided items 8 and new controls)
- Years 1/2/3/5 (default 1), estimate before running = spots x years x 0.7 ms / workers (engine MEASURED 0.7 ms per
  spot-year), warn above 3 s.
- Mission preset (6 d crew / 13 d robotic, labelled), sliders: min sunlight %, min Earth contact %, max longest night h,
  Sun elevation at touchdown. Defaults labelled "example values" until the NASA 2024 PDF check reports.
- Mast height 0 / 2 / 10 m, **default 2 m** (engine: 0 m single-point values are fragile; C1 84% -> 56% within 100 m).
- "Relay satellite available" switch: turns off the Earth-contact rule.
- PSR filter "sunny spot within 2 / 5 / 10 km of permanent shadow". Never the word "ice".

## Views (UI research top 5)
1. Lead: landing-window calendar per site, a failing cell shows WHICH limit failed (glyph + aria-label), not only colour.
2. Filter funnel next to the sliders ("N dates pass each limit").
3. Stacked Sun / Earth / Both lanes for the chosen date with thresholds as dashed lines.
4. Ranking table, bars + exact %, ">=" when a dark spell is cut by the window edge.
5. Map/3D with its settings printed on it. viridis/cividis, blue/orange + shape, light theme default.

## Provenance (Decided item 9)
- Bar: "Precomputed <date> UTC from <DEM>, <ephemeris>; page ephemeris 2026-2030". Needs `generated_utc` + versions in every
  data file (frontend adds it to `subpoints.json`; engine to `sites.json`, `terrain_meta.json`, `cap_meta.json`).
- "Request a newer precalculation": opens a pre-filled GitHub issue (no backend). A maintainer runs `pipeline/` on the home server
  (named sites ~2 min, whole pole ~4 min masks + ~2 min monthly, engine MEASURED) and pushes. GitHub Actions later, needs Adrian.

## Data quality (Decided item 10)
- Per-site chip: published reference yes/no, PGDA 90 `_ERR` and `_EFFRES` at the site (engine to supply), "approximate, 600 m"
  for custom spots.

## Needs from the engine
`psr.json` (PGDA 90 PSR outlines, simplified, polar metres), per-site `err_m`/`effres_m`/`psr_km`, `generated_utc` + versions.

Status: waiting for Eren's go on the plan and build order.
