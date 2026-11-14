# Frontend: PSR outlines received; design draft D

- Copied from `engine-wt\data\` into the repo's `data\` (uncommitted): `psr.json` (1,531 PSRs >= 1 km^2, simplified 120 m,
  polar stereographic metres; label "permanently shadowed (LOLA model)") and the rebuilt `sites.json` with `psr_km`
  (A 6.06, B 2.43, C 7.17, D 12.74 km, engine MEASURED). Not yet drawn or used by the page.
- Browser rule for clicked spots (engine): distance to the simplified polygons, up to ~120 m off; fine for the 2/5/10 km filter.
- Design: Eren rejected the first planner look. Drafts in `design-drafts\` (outside the repo, served locally):
  A lanes (ESA figure), B mission control (NASA Eyes/QuickMap), C wall calendar, D lunar ops = Eren's drone-dashboard layout
  (status bar, left panel, full-screen 3D, bottom drawer) with real LOLA terrain (three.js 0.160.0, MIT, from jsdelivr) lit by the
  real Sun, and real engine masks. Eren asked for the drone-dashboard style; D is waiting for his go to become the real page.
- New credit when D ships: three.js (MIT) -> CREDITS-PENDING.
