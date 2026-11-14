# Research: LunaNav (Team AFUQ) teardown

Read only, logged out, built-in browser. Sources: repo README, `docs/SCIENCE.md`, `docs/ATTRIBUTION.md`, the public GitHub repo, live site www.afuq.website.
No licence on the repo: ideas only, nothing copied.

## Who they are
- 47 commits, 2 contributors: the owner and Claude (every commit co-authored).

## Facts found
- **Geometry correct (MEASURED):** their Malapert point (-85.9119, -4.1570), 14 Nov 2026 07:00 UTC.
  Site shows Sun -0.92 deg, Earth -0.26 deg vs local horizontal; Horizons `coord@301` gives Sun -0.917,
  Earth -0.264. Match. Do not attack their ephemeris.
- **Terrain:** old `LDEM_80S_80M` (PDS GDR v2), not PGDA 90 ADJ (Barker 2023). 80 m only, 720 rays,
  **hard 150 km cap**, 2 m observer. Their own doc: "Terrain/horizon accuracy ... not independently validated."
- **Sites:** one point per NASA region, chosen on a **1 km grid** (slope <= 10 deg, most 2027 sun).
  Best result 66.8% (doc) / 66.7% (UI). Our home-server run: best on our 1 km grid 65.8%, while ridge spots
  reach ~80% with 20 m terrain (Shackleton S 79.1% vs Glaser 81.0%, MEASURED log 1400).
  So their ranking is a 1 km grid ranking that misses the narrow ridges.
- **Visibility rule:** disc centre above skyline (same as our sunset rule). Disc fraction shown only in readings.
- **Ephemeris span:** 2026-07-01 to 2028-12-31 only. No multi-year calendar possible.
- **Ranking:** "Site ranking 2027" with one-decimal % and no uncertainty, one year, one point per region.
- **Added 13-14 Nov (they are moving toward us):** "Launch delayed? delay by N days" (same site, later),
  power assessment (stored kWh = load x longest dark), Earth clearance 0/1/2/5 deg.
- **Claims handled well:** "not a NASA product", Artemis III -> IV wording correct, Earth = line of sight
  not a link, no suitability score, limits listed.
- **Credits gaps (UNVERIFIED for their submission form):** ATTRIBUTION.md lists no ElevenLabs/AI voice credit,
  no source for the "opening chime", no AI-use statement in README.
- **UX (MEASURED, this laptop, warm cache):** ~10 s to first screen on mobile emulation, then a
  "Start Mission" gate; ~35 MB decoded assets on first load (largest 5.8 MB texture); WebGL 2 needed for 3D.
  Dark theme only (0 `prefers-color-scheme` rules). Status uses text labels plus colour (colour-blind OK).
  Jargon: "7.2 deg below horizon" next to "elevation -0.92 deg" is confusing. No console errors.

## Table
| Their feature | Works? | Their mistake / limit | What we do instead |
|---|---|---|---|
| Sun/Earth ephemeris (Horizons, hourly) | Yes, matches Horizons | Ends 2028-12-31 | 5-year sky table 2027-2031 |
| Terrain horizon, 80 m, 150 km cap | Yes | Cap can drop far terrain; 80 m only; not validated | Auto-stop reach, 20 m near field, PGDA 90 ADJ, validated vs Glaser |
| One point per region (1 km grid) | Yes | Misses ridges; max ~67% | Named exact sites + whole-pole screening layer, labelled approximate |
| Site ranking 2027 | Yes | Exact % with no uncertainty, 1 year | Show 2 m vs surface spread; time-span 1-5 y |
| 2-scenario compare + launch delay | Yes | Only 2 scenarios, user picks them | Calendar: every window for a site, every site for a date |
| Power kWh | Yes | Longest dark only, no relay, no LQCIP | Battery-hours gap tolerance + relay toggle (DECISIONS 12, open) |
| Surface 3D view, stars, voice | Yes, polished | 35 MB, 10 s, WebGL needed | Light page; horizon chart is the hero |
| Earth clearance 0-5 deg | Yes | none | Match it (cheap) |
| Search over many spots / sliders filter | No | - | Core of our pitch |
| PSR / ice filter | No | - | "within X km of permanent shadow", never "ice" |
| Sun elevation at touchdown | No | - | Add (IM-2 lesson) |

## Top 5 attack points (honest, checkable; frame as "we do X", never "they are wrong")
1. **Validation:** their terrain is "not independently validated" (their words). We show S 79.1% vs Glaser 81.0%.
2. **Resolution decides the answer:** at 80 m/1 km, best spots cap near 66%; with 20 m, ridges reach ~80%.
3. **They answer "how sunny is this point"; we answer "where and when can I land"** (search + calendar).
4. **Time span:** they stop at end 2028; slips push missions past that. We cover 2027-2031.
5. **Uncertainty:** single exact % vs our 2 m mast / surface spread.

## Top 3 they do better (match them)
1. Ephemeris checked against Horizons in a test, with numbers in the doc. We have it (0.0042 deg); put it on a slide.
2. Plain "Interpretation limits" box under every result. Add ours.
3. Launch-delay button and stored-energy readout in plain words. Ours must be as easy to read.

## Open questions
- Is the 150 km cap material at their de Gerlache point? Our engine saw up to 1.06 deg change 150 -> 250 km
  at our de Gerlache site; not re-measured at theirs (UNVERIFIED).
- Their submission page (AI disclosure, video) not checked.
