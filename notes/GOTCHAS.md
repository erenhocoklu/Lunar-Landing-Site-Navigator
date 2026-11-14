# Gotchas

Append, never delete. Strike through with a date when fixed.

- **README is in Romanian.** The NASA submission must be English.
- **PGDA box centre "Shackleton rim 89.77 S 188.1 E" is on the inner crater wall** (MEASURED 8.6% sun), not a site point. Do not use it as a site.
- **Malapert rays toward the equator leave the 80S grid past ~180 km.** Masks there are cut short; handle or state it.
  (2026-11-14, engine seed check: this only bites at 250 km reach, not at 150 km. Relevant to DECISIONS open item 1.)
  (2026-11-14 12:40, engine: with the automatic stop, 0/360 rays reached the map edge at the Malapert box centre; every ray
  stopped first. Not a problem there. Spots further out than Malapert must still be checked; the code flags edge hits.)
- **Horizons uses DE441, the DEM uses DE421.** Effect is tiny; state it in the README.
- **20 m tiles over the network cost ~23 s per 20 km window** (MEASURED). Cache them locally.
- **Frame trap: Mean Earth (ME) vs Principal Axis (PA).** Horizons `coord@301`, LOLA and USGS use ME. Using PA shifts
  Sun/Earth az/el by ~0.02 deg and a pole site by ~660 m (MEASURED in `ephem-libs.md` tests).
- **PGDA sends no CORS header.** The browser cannot read the COGs; terrain must be baked in Python (`frontend-libs.md`).
- **The page needs a web server now** (frontend, 2026-11-14): `index.html` fetches `data/subpoints.json`, so opening it
  as a local file fails. Use GitHub Pages or `python -m http.server` in the repo folder.
- **Horizons names the frame `MOON_ME` in observer headers** (`Target pole/equ : MOON_ME`), not `MEAN_ME`. Check for both.
- **Horizons high-precision ME model is valid only for A.D. 1550-2650** (VERIFIED, Horizons manual). Fine for us; do not extrapolate.
- **Demo limits:** 30 s video OR max 7 slides including the title. One over = not eligible for global judging.
- **New teammates must be on the NASA Members tab before submission closes.** No additions after. Team is 5, so 4 must be at judging (local rule).
- **No mentor here knows planetary data** (mentor sheet, 14 Nov). Do not expect a mentor to validate Sun/Earth numbers.
- **AI media:** AI images need a visible watermark; no NASA logos in AI content; nobody under 18 in any media.
- **The 5 m 87S mosaic (PGDA 81, 3.47 GB) reaches only ~91 km.** Good for close detail, too short for full horizons.
- **Surface (0 m) values at one point are fragile** (engine, home-server runs 14 Nov): a 0.7 deg slope within 100 m moved
  C1 from 84.5% to 55.8%. The site height source (80 m vs 20 m DEM, 5 m difference) moved S from 56% to 84%. Take site height
  from the 20 m DEM and headline 2 m mast values. See log 1400.
- **1 km pole map undersells narrow ridges** (best spot 65.8% vs ~80% at C1/S) and 75% of spots have rays that hit the map edge.
  Label it a screening layer.
- **Longitude sign:** use east longitude (137.3 W = 222.7 E). Use true north, not grid north, for azimuths.
- **Do not reuse LunaNav code:** it has no licence. Other 2026 teams' code is a judging risk even under MIT.
- **Wording:** the crewed landing moved to Artemis IV (2028). Say "Artemis south-pole candidate regions".
  Never claim "planners told us X" or "NASA can't do this".
- ~~**NASA HLS 2024 thresholds** (Earth visible >= 25%, slope < 10 deg over 100 m, within 6 deg of the pole) are UNVERIFIED
  until someone confirms them in the PDF. Label them as NASA's only after that.~~ Checked 2026-11-14 14:30 (engine subagent,
  NTRS 20240009596 full text via API; images not checked). VERIFIED: Dwyer Cianciolo (NASA LaRC), "Artemis Human Landing System
  Update", seminar presentation, Aug 2024, no technical review. Listed as "Key Artemis III Landing Requirements" (p.19): land within
  6 deg latitude of the pole, landing slope < 10 deg over 100 m, EVA slope < 20 deg over 2 km, land within 100 m of target,
  direct-to-Earth comm (no relay), lit for the surface stay. Only map masks (pp.23-24), no time period stated: Earth visibility < 25%
  and Sun visibility < 5% excluded. **Label:** requirements "as listed in a NASA presentation (2024)"; the 25% / 5% values
  "visibility masks used in that presentation's maps". Never "NASA standard".
- **Longest darkness can differ by up to a day when the Sun grazes the horizon** (engine + frontend cross-check, 14 Nov):
  a 0.0001 deg difference split one 43 h night into 30 h + 12 h. Show night lengths as approximate near the limit. See log 1440.
