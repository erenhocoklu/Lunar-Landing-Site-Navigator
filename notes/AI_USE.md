# AI use log (for the NASA submission)

The submission must describe how AI tools were used. One line per use. "Human check" says what a person verified.

| Time | Session | Tool / model | What it did | Human check |
|---|---|---|---|---|
| 2026-11-14 morning | research (DEM) | Claude Code | Compared LOLA DEM products, chose PGDA 90; drafted horizon method | Eren read the notes |
| 2026-11-14 morning | research (ephemeris) | Claude Code | Tested browser ephemeris routes against live Horizons | Results are test output |
| 2026-11-14 morning | research (prior art) | Claude Code | Surveyed existing tools and other teams' repos | Eren read the report |
| 2026-11-14 morning | research (frontend) | Claude Code | Surveyed frontend libraries for a south-pole view | Eren read the notes |
| 2026-11-14 morning | engine | Claude Code | Scratchpad tests: DEM header, projection, mask speed, first validation vs Glaser 2018 | Numbers compared to published values |
| 2026-11-14 ~11:00-12:00 | frontend | Claude Code | Translated index.html to English; wrote `pipeline/make_subpoints.py`; replaced the fake Sun/Earth model with real Horizons data; added sites, date picker, sunset/Earthset headline, CREDITS.md | Browser values checked against 6 live Horizons az/el values (max 0.0042 deg); Eren reviewed the page |
| 2026-11-14 morning | research (manager) | Claude Code, 4 research agents | Read NASA guides, tested a Horizons call, deep prior-art research, drafted concept proposal | Eren reviewed; concept not yet red-teamed |
| 2026-11-14 11:59 | organizer | Claude Code | Set up this vault | Eren approved the structure |
| 2026-11-14 12:01 | engine | Claude Code | Checked the seeded measurement note, filled package licences from installed metadata | Licences read from package metadata; GDAL/PROJ still to check |
| 2026-11-14 ~13:30-14:00 | engine (home server) | Claude Code | Downloaded 20 m DEM, ran named-site and whole-pole computations on Eren's home server | Numbers compared with Glaser 2018 and the laptop runs |
| 2026-11-14 13:20 | engine | Claude Code | Benchmarked the landing-window calendar (items 8-10) in Node; estimated region sizes | Timings are test output; region sizes are estimates |
| 2026-11-14 13:00 | engine | Claude Code | Diagnosed the Shackleton S miss (time window vs terrain resolution vs mast height) | Numbers are test output vs Glaser 2018 |
| 2026-11-14 12:40 | engine | Claude Code | Implemented Eren's automatic-reach idea in a test script and compared it to full-length rays | Exact match checked by test (0.0000 deg at 5 sites) |
| 2026-11-14 ~11:30-12:20 | research (events) | Claude Code | Read the organisers' mentor sheet, ranked mentors for our build, built a two-day schedule page | Eren reviewed the page |
| 2026-11-14 12:25 | engine | Claude Code | Benchmarks: mask speed vs accuracy, whole-pole masks, 5-year Horizons table, time layer in Python and JS | Timings are test output; sky table checked against per-site Horizons |
| 2026-11-14 12:21 | research (manager) | Claude Code | Design talk: time-span control, precompute vs live, layers, read engine benchmarks | Benchmarks from engine log; proposals await Eren |
| 2026-11-14 12:39 | research (manager) | Claude Code, 4 research agents + report writer | Deep research: ice/PSR data, NASA site selection, SpaceX/commercial, ice layer design | Sources cited in report; conflicts resolved explicitly |
| 2026-11-14 12:50 | frontend | Claude Code, 1 research agent | Surveyed how NASA, ESA, CNSA papers, companies and the rival LunaNav display landing-site lighting/Earth/windows; ranked 5 UI patterns (log 2026-11-14-1250) | Claims marked CONFIRMED/INFERRED with URLs; Eren to review |
| 2026-11-14 12:52 | research (manager) | Claude Code, 3 research agents + report writer | Deep research: ESA, China, SpaceX, compute speed and common practice | Sources cited in report; one note's engine claim corrected (disc, not point) |
| 2026-11-14 12:58 | research (manager) | Claude Code, 3 research agents | Red-team research: was the calendar idea tried, what sets landing dates, failure modes | Verdict written by manager from notes; snippets marked |
| 2026-11-14 13:10 | research | Claude Code, built-in browser | LunaNav teardown: read their repo docs, commits and live site (read only, logged out); checked one of their numbers against Horizons (log 2026-11-14-1310) | Horizons match measured; other claims quoted from their docs; Eren to review |
