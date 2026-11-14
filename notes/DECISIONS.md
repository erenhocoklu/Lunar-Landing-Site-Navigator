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
- 2026-11-14 13:25 (Eren, engine session): **two terrain grids for the page.** (1) FRONTEND's display window: `heights.bin`,
  +/-60 km at 240 m (501x501, ~1 MB), for the 3D view only. (2) A coarse whole-cap grid (~600 m, ~4 MB, file name to agree)
  for approximate horizon masks on clicked spots, labelled approximate. Named sites keep exact masks in `sites.json`.
- 2026-11-14 14:10 (Eren, engine session): **item 8 time span: user picks 1/2/3/5 years, default 1**, time estimate before running,
  warning above 3 s.
- 2026-11-14 14:10 (Eren, engine session): **item 9 precompute physics, compute user settings live.** Eren's addition: the page must
  show that data was precomputed and WHEN (date + data versions), offer "request a newer precalculation", and say how long it
  would take. Open detail: a static page cannot run the Python itself; the request needs a route (e.g. instructions/issue, or a
  CI job). Timings to show (MEASURED): named sites ~2 min, whole pole ~4 min masks + ~2 min monthly on the home server.
- 2026-11-14 14:10 (Eren, engine session): **item 10 detail areas: the 4 named sites first** (C1, S, GR1, MP1); 9 Artemis regions
  only if official centres turn up and time allows. Eren's caveat: these 4 are the most studied; other spots may have less data,
  so the page must show the difference. Idea (engine, not built): show per-site data quality from PGDA 90's own height-error
  (`_ERR`) and effective-resolution (`_EFFRES`) layers, and whether a published reference exists.
- 2026-11-14 14:20 (Eren, engine session): **item 11 permanent-shadow layer: yes.** PGDA 90 PSR outlines (20 m, shapefile) labelled
  "permanently shadowed (LOLA model)" + one filter "sunny spot within 2 / 5 / 10 km of permanent shadow". **Why:** water ice is the
  reason missions target the south pole; ice can only last in permanent shadow, and landers need sun, so the useful question is
  "how close is a lit spot to permanent shadow". Never say "ice" or "distance to ice": shadow is a model, real ice detections are
  sparse (M3 surface ice in ~3.5% of cold traps, LCROSS 5.6 +/- 2.9 % water by mass in one plume; `reports\Lunar ice and site selection.md`).
- 2026-11-14 14:20 (Eren, engine session): **relay switch: yes.** "Relay satellite available" turns off the Earth-contact rule
  (Chang'e-7 / Queqiao-2 pattern). The LQCIP readout in item 12 stays open.
- 2026-11-14 14:20 (Eren, engine session): **3D view: do NOT stick to the old WebGL code.** Eren wants the better, more efficient
  approach. FRONTEND to propose (research `frontend-libs.md` recommends a three.js plane in polar stereographic metres; globes
  pinch at the pole). Risk to manage: a rewrite must still land before the Sun 10:30 freeze.
- 2026-11-14 14:20 (Eren, engine session): **NASA 2024 limits: we check the PDF ourselves now** (engine subagent reading NTRS
  20240009596). Until it reports, slider defaults are "example values", never "NASA".
  Result 14:30: values CONFIRMED in the text (see GOTCHAS for exact wording and labels). Usable as slider defaults with the label
  "from a 2024 NASA presentation". Note it assumes NO relay, which matches our relay switch being off by default.

- 2026-11-14 14:17 (Eren, manager session): **other-missions layer is IN the build** (item 13 as proposed: hand-built `missions.csv`, precision circles, >= 2.0 km lander / >= 0.5 km impact keep-out per NASA 2011 non-binding, user-set large-lander radius, "coordinate" flag).
  Addendum (Eren, organizer session): **mission pins are shown by default** when the page opens, not behind a toggle.
- 2026-11-14 (Eren, organizer session): **user and pitch line.** User: teams in the early planning stage of a south-pole landing
  (concept studies and proposals, incl. future CLPS-style missions) find which spots and weeks give their spacecraft enough sunlight
  and Earth contact, and re-check in seconds when the launch slips; the same view shows students and the public why the pole is hard.
  Pitch line: "The data is public, but using it takes expert tools and hours. We turn it into an answer you can check in seconds:
  which spots and weeks work, and why." Lean hard on **comparing many options vs planning one mission**.
  **Why:** the brief says existing tools are hard to use "for rapid scenario comparison"; CLPS companies plan inside private
  trajectory tools, so never claim "CLPS will fly with this" or "NASA can't do this" (log 1258).
- 2026-11-14 (Eren, organizer session): **no trajectories** (no real-time, no planned). **Why:** the route does not change Sun/Earth
  at the site (the landing date is already an input); future-mission trajectories are not public, so numbers would be invented;
  off-brief. The date slip is handled as a "landing moved by N weeks" input. Optional extra only: a past mission's real flown path
  from Horizons on its pin, if Horizons covers it (UNVERIFIED which landers it has).
- 2026-11-14 (Eren, organizer session): **no login system this weekend.** Static page stays static.
- 2026-11-14 ~14:50 (Eren, organizer session): **MUST-SHIP CUT. Build only these 5 until they work:**
  (A) real masks for the 4 named sites, (B) site-first landing-window calendar + sliders + ranking, (C) time span 1/2/3/5 y,
  (D) mission pins + keep-out filter, (E) relay switch. **No new features or decisions until A-E work**, except decisions that
  unblock them. Park new ideas for the **22:00 checkpoint**. Parked now: PSR layer (F), data-date bar + request button (G),
  three.js 3D rewrite (H, in only if working by Sun 08:00, else keep the current view), data-quality chips, mission board, agent, voice.
  Timeline: red team 15 min first (playbook rule 5); build to 22:00; Sun 10:30 freeze; everything submitted by 14:30.
  Engine told to go ~14:50; FRONTEND gets the plan after Eren's UI talk ends.
- 2026-11-14 (Eren, organizer session): **drone-project code is not copied in** (wrong physics for the Moon; written before kickoff).
  Only the pattern is reused: the LLM plans, the deterministic engine decides.

## Open, Eren decides
1. ~~**Horizon reach.**~~ Decided 2026-11-14 12:40: automatic stop (see Decided). Old note: engine recommended 250 km (MEASURED: de Gerlache changes up to 1.06 deg from 150 to 250 km, 0 deg from 250 to 300 km).
   RESEARCH's horizon-method note says ~150 km. The engine measurement is newer and more specific.
2. ~~**Sunset definition.**~~ Decided 2026-11-14 12:10: Sun centre.
3. ~~**Engine folder layout in the repo.**~~ Decided 2026-11-14 12:10: all in `pipeline/`.
4. ~~**File contract engine -> frontend.**~~ Decided 2026-11-14 12:10: as proposed (fields still to agree).
5. ~~**3D view**~~ Decided 2026-11-14 14:20: not the old WebGL; FRONTEND proposes (see Decided). Old text: **3D view: globe.gl or three.js plane.** The shared note proposes globe.gl; `frontend-libs.md` recommends no globe
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
8. ~~**Time-span control**~~ Decided 2026-11-14 14:10 (see Decided). Old text: **Time-span control (Eren asked, 14 Nov).** User picks 1 / 2 / 3 / 5 years, default 1. Alert when spots x years is big
   (MEASURED by engine: 5,000 spots x 5 y = 14.3 s in JS single thread). Supersedes "2027 by default; more years later" in item 7.
   Engine test 13:20: plausible. Full calendar ~0.7 ms per spot-year single thread (MEASURED); 5,000 x 5 y = 18 s single,
   4.5 s with 8 workers. Proposed alert: estimate = spots x years x 0.7 ms / workers, warn above 3 s. See log 1320.
9. ~~**Precompute vs live**~~ Decided 2026-11-14 14:10 with Eren's additions (see Decided). Old text: **Precompute vs live (manager proposal, Eren raised the question).** Precompute what cannot change (horizon masks, 5-year
   Sun/Earth sky table); compute live what can (calendar, user limits, mission length, time span, an updatable
   "stay X km from other missions" filter). See log 2026-11-14-1221-research-manager-design-talk.md.
   Engine test 13:20: plausible. The live part (limits + keep-out) is inside the 0.7 ms per spot-year; keep-out is negligible.
   Nothing precomputed needs recomputing on a hackathon timescale (errors far below 0.01 deg, UNVERIFIED). See log 1320.
10. ~~**Zoom levels**~~ Decided 2026-11-14 14:10: 4 named sites first (see Decided). Old text: **Zoom levels.** Whole south pole at 1 km (104,183 spots, MEASURED) + ~100 m detail precomputed for NASA's 9 candidate
    regions (~32 MB, estimate from engine's 3.6 MB per 10x10 km). Fine detail cannot be computed in the browser (PGDA has no CORS).
    Engine estimate 13:20: plausible but the heaviest item. 9 x 15x15 km at 100 m = 202,500 spots, masks ~73 MB raw / ~31 MB gz
    (8 MB per region file), ~1 h compute on the laptop (UNVERIFIED, home-server run will measure). Region centres are placeholders. See log 1320.
11. ~~**Ice layer**~~ Decided 2026-11-14 14:20 as a permanent-shadow layer (see Decided). Old text: **Ice layer.** Static layers: elevation, slope, permanent shadow (PGDA `LPSR_*`) as "possible ice", distance to nearest PSR.
    Show as a filter "lit landing spot within X km of permanent shadow"; never present PSR as confirmed ice.
12. ~~**heights.bin extent**~~ Decided 2026-11-14 13:25 by Eren: both grids (see Decided). Old text: **heights.bin extent (raised by ENGINE, 14 Nov 12:40s).** FRONTEND's draft uses a +/-60 km display window; Eren's earlier
    file-contract decision says a ~600 m grid of the whole cap. Conflict sent to Eren; not settled. Do not build either as final.
13. **FRONTEND proposals (14 Nov ~14:30), answering Decided items of 14:10-14:20. See log 2026-11-14-1430-frontend-product-plan.md.**
    a. 3D view: three.js (MIT, pinned version) `PlaneGeometry` in polar stereographic metres from `heights.bin`, curvature baked in,
       `OrbitControls`, sun as a DirectionalLight with GPU shadow maps. 3D shadows are visual only (they see the +/-60 km window);
       every number comes from horizon masks. Label it so. Click on terrain -> lat/lon -> custom spot (approximate mask from the cap grid).
    b. "Request a newer precalculation": a button that opens a pre-filled GitHub issue on the repo (title, settings, data versions);
       a maintainer runs `pipeline/` on the home server (~2 min named sites, ~6 min whole pole, MEASURED by engine) and pushes.
       A GitHub Actions job is a later option (needs Adrian's repo settings).
    c. Build order: (1) controls + calendar + funnel + ranking on the current page, (2) provenance bar + request button,
       (3) three.js view swap, (4) PSR layer + filter + data-quality chips when the engine files land.
12. **LQCIP + relay toggle (manager research, 14 Nov).** Add an ESA-style readout "longest near-continuous lit period" that ignores
    dark gaps shorter than the user's battery hours, and a "relay available" switch that disables the Earth-contact filter
    (Chang'e-7 used Queqiao-2 this way). See log research-agency-methods.
13. ~~**Other-missions layer**~~ Decided 2026-11-14 14:17 (see Decided). Old text: **Other-missions layer (manager research, 14 Nov).** Hand-built `missions.csv` (~15 rows, sources graded A/B/C); circles
    sized by position precision; keep-out filter: >= 2.0 km from landers/historic sites, >= 0.5 km from impact sites (NASA 2011,
    non-binding), user-set caution radius for large landers (default is our assumption, labelled); "coordinate" flag if a mission
    is active nearby in the chosen window. See log research-mission-deconfliction.
14. **Mission board (Eren's idea, stretch, after the core and the mission pins).** One company adds several planned missions
    (site, mission length, earliest date); one calendar shows every mission's landing windows side by side, plus overlaps.
    Same engine run N times; no trajectories, no backend. Not in the brief: scores on Creativity/Impact, not Relevance.
