# Decisions

Only decided items go under Decided. Open items wait in "Open, Eren decides".
Never delete; strike through with a date.

## Decided
- 2026-11-14 (engine brief): DEM = PGDA product 90 LOLA (80 m whole file + 20 m tiles over /vsicurl),
  MOON_ME frame of DE421, polar stereographic, sphere R = 1737400 m.
- 2026-11-14 (engine brief): JPL Horizons for Sun and Earth positions.
- 2026-11-14 (engine brief): own NumPy ray march with the exact spherical elevation formula (no horizon library).
- 2026-11-14 (engine brief): Python precomputes; the static page reads files.
- 2026-11-14 (engine brief): the frontend owns the page ephemeris; the engine keeps per-site Horizons series as the reference.
- 2026-11-14 12:10 (Eren, engine session): **sunset = Sun centre** (disc half hidden, fraction 0.5), the same point Horizons
  reports. Used for "time to sunset" and "longest night". Sunlight % stays the disc-fraction average.
- 2026-11-14 12:10 (Eren, engine session): **all Python in the repo's `pipeline/`** (next to the frontend's `make_subpoints.py`):
  `dem.py`, `horizon.py`, `metrics.py`, `build_sites.py`, `tests/`. The DEM stays outside git.
- 2026-11-14 12:10 (Eren, engine session): **file contract engine -> page:** `sites.json` (360-bin masks + stats for named sites,
  exact) + `heights.bin` + `terrain_meta.json` (~600 m grid of the whole cap for drawing and for approximate masks on clicked
  spots, labelled approximate in the UI). Exact fields still to agree with FRONTEND CODE.
- 2026-11-14 12:40 (Eren, engine session): **horizon reach = automatic stop, no fixed km.** Each ray walks outward and stops
  once even the tallest terrain on the map (7026 m) could not rise above the horizon already found, or at the map edge.
  MEASURED: identical (0.0000 deg) to walking every ray to the map edge at 5 sites, same as 250 km, and faster (104-189 ms).

## Open, Eren decides
1. ~~**Horizon reach.**~~ Decided 2026-11-14 12:40: automatic stop (see Decided). Old note: engine recommended 250 km (MEASURED: de Gerlache changes up to 1.06 deg from 150 to 250 km, 0 deg from 250 to 300 km).
   RESEARCH's horizon-method note says ~150 km. The engine measurement is newer and more specific.
2. ~~**Sunset definition.**~~ Decided 2026-11-14 12:10: Sun centre.
3. ~~**Engine folder layout in the repo.**~~ Decided 2026-11-14 12:10: all in `pipeline/`.
4. ~~**File contract engine -> frontend.**~~ Decided 2026-11-14 12:10: as proposed (fields still to agree).
5. **3D view: globe.gl or three.js plane.** The shared note proposes globe.gl; `frontend-libs.md` recommends no globe
   framework (globes pinch near 90S) and a three.js plane in polar stereographic metres. Check what FRONTEND CODE already uses.
   The RESEARCH concept proposal (item 7) lists "globe as the main screen" under "not doing".
7. **Concept proposal (RESEARCH, 14 Nov; not yet red-teamed with the full team).**
   - One engine, a site x date table. Lead view: site-first landing-window calendar. Second view: date-first ranking.
   - Time span: 2027 by default; more years later if cheap.
   - Mission presets, labelled: Artemis crew ~6 days continuous sunlight; robotic ~13 days (one lunar day).
   - Coverage: ~1 km map of the whole south pole + ~100 m detail where the user clicks. Gate: time one spot in the engine first.
   - Sliders are the real controls. Optional AI agent turns plain requests into visible slider values and explains results;
     the engine does every calculation. AI key in a proxy, or the agent runs locally only.
   - Voice (ElevenLabs): last extra, one non-engine teammate, pre-generated audio, cut at the 10:30 freeze.
   - Not doing: globe as the main screen, collision system, flat horizon, invented "NASA standards".
   - Red-team checks still open: QuickMap Compute Visibility output; Teams tab + 78 repos for any grid search; HLS 2024 thresholds in the PDF.
8. **Time-span control (Eren asked, 14 Nov).** User picks 1 / 2 / 3 / 5 years, default 1. Alert when spots x years is big
   (MEASURED by engine: 5,000 spots x 5 y = 14.3 s in JS single thread). Supersedes "2027 by default; more years later" in item 7.
9. **Precompute vs live (manager proposal, Eren raised the question).** Precompute what cannot change (horizon masks, 5-year
   Sun/Earth sky table); compute live what can (calendar, user limits, mission length, time span, an updatable
   "stay X km from other missions" filter). See log 2026-11-14-1221-research-manager-design-talk.md.
10. **Zoom levels.** Whole south pole at 1 km (104,183 spots, MEASURED) + ~100 m detail precomputed for NASA's 9 candidate
    regions (~32 MB, estimate from engine's 3.6 MB per 10x10 km). Fine detail cannot be computed in the browser (PGDA has no CORS).
11. **Ice layer.** Static layers: elevation, slope, permanent shadow (PGDA `LPSR_*`) as "possible ice", distance to nearest PSR.
    Show as a filter "lit landing spot within X km of permanent shadow"; never present PSR as confirmed ice.
