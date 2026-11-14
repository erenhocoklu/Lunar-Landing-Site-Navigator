# Manager session: design talk with Eren after the engine benchmarks (14 Nov)

## What happened
- Eren asked for a **time-span control: 1 / 2 / 3 / 5 years**, default 1, with an **alert when the request will take longer**.
- Eren raised: data can change (new landings, other objects), so should everything be recomputed live?
  Manager position (not yet decided): physics does not change, so precompute it; compute everything user-specific live.
  - Does NOT change: Sun/Earth positions (orbital physics, predictable decades ahead); terrain/horizon (landers are metres,
    DEM pixels 20-80 m, horizons set by terrain km away). New DEM releases are years apart: rerun the pipeline.
  - DOES change: other missions' positions (keep-out zones), the user's limits, mission length, time span, zoomed area.
  - Proposal: precompute horizon masks + 5-year sky table; compute the calendar, limits and an updatable
    "stay X km from other missions" filter live in the browser.
- Eren asked for more layers: elevation, light, ice, all over 5 years. Split proposed:
  - Static (compute once): elevation, slope, permanent shadow / possible ice (PGDA `LPSR_*`), distance to nearest PSR.
  - Time-varying (5 years): Sun light, Earth contact.
  - Ice framing: landing spots are never in ice (PSR = 0% sun); the useful metric is "lit spot within X km of PSR".
- Scope clarified with Eren: **south polar cap only** (DEM covers ~300 km from the pole), not the whole Moon.

## Reading of the engine benchmarks (log 2026-11-14-1225, all MEASURED there)
- One site x 5 years in JS = 2.9 ms, so the calendar for any site can be computed live from masks + sky table.
- Whole pole at 1 km: 104,183 spots, ~13 min offline; masks ~16 MB gzipped; monthly summaries 12.5 MB (daily 380 MB is too big).
- 5,000 spots x 5 years in JS = 14.3 s single thread: the alert is needed (Web Workers could cut it; UNVERIFIED).
- Browser cannot read the PGDA DEM (no CORS), so ~100 m detail must be precomputed offline for chosen areas
  (~3.6 MB per 10x10 km, engine estimate).
- PGDA box centres are poor site points (Connecting Ridge box centre 36% sun vs C1 76%, MEASURED by engine): use published coordinates.

## Open questions (added to DECISIONS "Open, Eren decides")
- Item 8: time-span control 1-5 years with alert.
- Item 9: precompute physics, live filters on top (incl. other-missions keep-out list).
- Item 10: 100 m detail areas = NASA's 9 candidate regions (~32 MB, estimate); whole pole at 1 km.
- Item 11: ice/PSR layer as "distance from a lit spot to permanent shadow".
