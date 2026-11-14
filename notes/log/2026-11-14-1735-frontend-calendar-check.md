# Frontend: landing calendar checked against the engine's answer key; calendar redesign

## Cross-check (MEASURED, browser, 2026-11-14)
Against `data/windows_reference.json` (engine commit 07c5981; 2027, one landing per day at 00:00 UTC, 365 landings, 4 cases).
Page method: hourly sky from `subpoints.json` (6 h table, cubic interpolation, parallax) + `sites.json` masks.
- Sampling at whole hours: passing days page/engine: A 2 m robotic 146/146, B 2 m crew 109/109, C 0 m robotic relay 11/11,
  D 10 m robotic 192/192. Days that disagree: 0 / 1 / 0 / 0.
  The one: B 2027-02-25, page sun 94.52% vs engine 95.07% at the crew limit 95% (page fails sun, engine does not).
- Max per-day gaps: sun 0.5-1.2 points, Earth 0-0.32 points, night 1 h (13 h on one D day, no pass change).
- Sampling at half hours (h+0.5) gave 3/1/5/0 disagreements (touchdown and Earth-near-limit edges). Decision for the page:
  whole-hour sampling, same as the engine.
- ~~Open: sun-% gap likely from disc-fraction formula (page linear vs chord-area). Asked the engine.~~ Resolved 2026-11-14:
  page switched to the engine's chord-area fraction f = (acos(u) - u*sqrt(1-u^2))/pi, u = clip((horizon - el)/0.2666, -1, 1),
  and whole-hour sampling. Re-run (MEASURED): 146/146, 109/109, 11/11, 192/192, **0 disagreeing days** in all 4 cases;
  max per-day sun gap 0.047-0.088 points. One longest-darkness gap (D 10 m, landing 2027-06-20: page 43 h, engine 30 h) is a
  grazing hour (Sun centre 0.0001 deg below the horizon on the page), not a bug; no pass/fail change. Document: "longest darkness
  can differ by up to a day when the Sun grazes the horizon". Applied in the preview; the real page gets it in the build.

## Calendar redesign (preview, `design-drafts\draft-e-final.html`)
Eren: "nobody should think more than 0.5 s". Replaced the week grid with one row per month, days 1-31 left to right,
two states only (blue = good day to land, grey = not), count per month, and a live sentence on hover/click with the reason
and the numbers ("not enough sunlight (66%, you need 70%)"). Also added a "Stand at the site" view: real Sun and Earth
(true size, position, Earth phase) over the site's exact LOLA mask horizon; stars are decorative.
