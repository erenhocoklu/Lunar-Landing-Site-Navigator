# Context

## What we build
Lunar Landing Site Navigator (NASA Space Apps 2026). A static web page: pick a south-pole site and a date,
see where the Sun (power) and Earth (direct radio contact) are against the **real LOLA terrain horizon**,
and how long each stays up. Concept under discussion: a site x date table (date-first for crewed
missions, site-first landing-window calendar for robotic landers). See the shared note for the full idea.

## Deadlines (Sun 15 Nov, local time)
- Feature freeze **10:30**
- Pitch form **15:00**, pitches **15:30**
- NASA submission **18:50**: click "Submit for Judging", not just save
- Repo public and every link tested logged out at least 1 h before the deadline
- **Team target: everything submitted by 14:30.** NASA's own hard limit is Sun 23:59 local, but the local lead's 18:50 applies.

## Official rules (NASA guides, read 14 Nov; source: RESEARCH session)
- Demo: **30 s video OR max 7 slides including the title**, English or English subtitles. Over the limit = not eligible for global judging.
- All links public, no login. English everywhere.
- At least 1 NASA data source used for real. Cite every reference (code, data, images, fonts). No copyrighted music or images.
- AI: describe AI use; AI images carry a visible watermark; AI code/data acknowledged in text and metadata; AI must not come up
  with the idea itself; no NASA logos in AI content; nobody under 18 in any media.
- Judging: Impact, Creativity, Validity, Relevance (NASA data core), Presentation, 1-5 each, 20% each. Ties: Impact, then Validity.
  Global nominees 3 Dec, finalists 17 Dec, winners 26 Jan 2027.
- Team: NASA max 6 members, all on the team page, same local event, none waitlisted, no additions after submission closes.
  Local rulebook: at least 2/3 of the team present at judging.
- NASA restriction: no bilateral activity with China or Chinese-owned entities.

## Horizons call (TESTED PASS by RESEARCH, ~1 s per call)
`https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='10'` (Sun) or `'399'` (Earth)
`&EPHEM_TYPE='OBSERVER'&CENTER='coord@301'&COORD_TYPE='GEODETIC'&SITE_COORD='E-lon,lat,0'&START_TIME=..&STOP_TIME=..&STEP_SIZE='1h'&QUANTITIES='4'`
Frame MEAN_ME, east longitude, UTC, smooth sphere R = 1737.4 km, no terrain, no refraction.

## Disqualifier watch
Invented numbers, non-English submission text, links that need a login, copyrighted media,
any sign of work done before kickoff (Sat 14 Nov 08:30).

## Team
- Adrian: repo owner.
- Eren: no write access to Adrian's repo; pushes to his fork and opens PRs.
- ~~Team size: UNCLEAR. The README lists Adrian and Eren; RESEARCH wrote "for 5 members, at least 4 present". Eren to confirm.~~ (2026-11-14 12:21)
- Team size: **5** (Eren confirmed 14 Nov 12:21): Eren, Adrian + 3 (names to add). All 5 must be on the NASA Members tab.
  Local 2/3 rule = at least **4 present** at judging (not in the global guide; local rulebook per RESEARCH). Roles across 5 not agreed.

## Mentors (organisers' sheet, 14 Nov; details in log 2026-11-14-1221)
No mentor covers space or planetary data. Saturday-only: Skytek (Cisteian, Stîngaciu) until 18:00. Python/algorithms: Valentin Mariș.
Sunday mentoring ends 15:00.

## Current state of the repo page (RESEARCH, 14 Nov)
`index.html` already has real engine logic (horizon ray march with curvature, Sun disc, Earth visibility, yearly stats, 10 m mast)
but runs on generated terrain, sine-wave Sun/Earth positions and a 46 km reach. The weekend work swaps in LOLA terrain and real ephemeris.

## Work areas and ownership
| Area | Owns |
|---|---|
| ENGINE (Python) | DEM reading, horizon masks, stats, validation; owns `sites.json` masks; keeps per-site Horizons series as the reference |
| FRONTEND | page, map/3D view, browser ephemeris (inline in `index.html`, no `ephem.js`; `data/subpoints.json` from one Horizons call; MEASURED max 0.0042 deg vs Horizons, n = 6, see log 2026-11-14-1201) |
| ORGANIZER (these notes) | keeps these notes true; flags contradictions; no features |

## File locations
- This repo: README, CREDITS.md, index.html, `pipeline/` (Python), `data/subpoints.json`, `notes/` (these notes).
- DEM: `LDEM_80S_80MPP_ADJ.TIF` (181 MB, PGDA product 90). Not in git; download from https://pgda.gsfc.nasa.gov/products/90
- Research reports (DEM products, horizon method, ephemeris libraries, prior art, frontend libraries) are on Eren's
  laptop; ask him for a copy. Their key findings are already in these notes.

## Data sources
- LOLA DEM: PGDA product 90 (`LDEM_80S_*MPP_ADJ`, Barker et al. 2023): 80 m whole file + 20 m tiles over /vsicurl.
- Ephemeris: JPL Horizons (DE441, MOON_ME frame, `coord@301`).
- Validation: PGDA product 69 illumination / Earth-visibility maps; Glaser 2018 (C1, S); De Rosa 2012 (GR1, MP1).

## Credits
The repo's `CREDITS.md` is the master list. New items go to `CREDITS-PENDING.md` here first.
