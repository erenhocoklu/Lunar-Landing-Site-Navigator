# Research: how ESA, China, SpaceX and NASA calculate site lighting (manager session, 3 researchers + writer)

Report: `..\reports\Agency site selection methods.md` (notes in `..\research_notes\Agency site selection methods\`).
UI side: FRONTEND log 2026-11-14-1250-frontend-ui-patterns-research.md.

## Findings
- One shared method everywhere: LOLA horizon per pixel, Sun disc fraction + Earth vs horizon, 1 h steps, 1-20 years.
- ESA (TU Berlin/DLR/Astrium): metric LQCIP = longest near-continuous lit period, ignoring dark gaps the battery survives (array height + hours of darkness). No public ESA tool. Moonlight relay dates slipping (2028 -> 2029-2031, latter unconfirmed).
- China (Zhao et al., Remote Sensing 2025): coarse 60 m NASA map to screen, then 5 m horizon + Skyfield/DE421 for finalists; slope <= 8 deg, illumination >= 35%, within 15 km hopper range of ranked cold traps; normalised-sum score. Queqiao-2 relay removed Earth visibility from Chang'e-7 preselection. Chang'e-7 missed its Aug 2026 window; good lighting ~100 days/year at its site (CGTN, preliminary).
- SpaceX/commercial: no public method (reused from earlier research).
- Speed: almost never published. Only hard number: TU Berlin 20x20 km x 1 yr from 24 h to 25 min on a 2014 GPU. Our engine is the same order of speed, not faster (estimate in report).

## Pitch rules (from the report)
- Claim: same method as agencies; a date change costs milliseconds because horizons stay valid (MEASURED 2.9 ms per site per 5-year calendar).
- Never claim: faster than NASA/ESA, "NASA takes days", 1 km map = site certification, official thresholds, knowledge of SpaceX's method, "ice".
- Still to state on a slide: horizon reach, Earth visibility rule (any part of disc vs centre), observer height.

## Candidate additions (Eren decides; added to DECISIONS open list)
- Item 12: LQCIP readout (longest lit period given battery hours) + "relay available" toggle that turns off the Earth filter.
