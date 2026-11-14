# Where we are (Sat 14 Nov, 15:10)

Snapshot by the organizer. Overwrite this file at each checkpoint; history lives in `log/`.

## Must-ship (DECISIONS "MUST-SHIP CUT")
| # | Feature | State |
|---|---|---|
| A | Real horizon masks, 4 named sites | done (engine `sites.json`); browser matches engine within 0.1 points (MEASURED, log 1535) |
| B | Landing-window calendar + sliders + ranking | built, local only; 0 disagreeing days vs engine answer key in 4 cases (MEASURED, log 1735) |
| C | Time span 1/2/3/5 y | built (planner panel) |
| D | Mission pins + keep-out filter | NOT built; FRONTEND 2 session prompt prepared |
| E | Relay switch | built |

Validation: Shackleton S surface 79.1% vs Glaser 81.0%; C1 2 m 85.6% vs 88.0% (engine, MEASURED). Browser ephemeris max 0.0042 deg vs Horizons.

## Code on GitHub (Eren's fork, not yet in a PR)
- `engine` branch: pipeline + outputs (5 commits, 14:23-14:36).
- `frontend-snapshot` branch: on top of `engine`, a WIP copy of the page (`index.html`, `CREDITS.md`, `subpoints.json`,
  `make_subpoints.py`) taken 15:10 from FRONTEND 1's working tree. FRONTEND 1 keeps working on `frontend-mvp` locally.
- The redesign (`design-drafts\draft-e-final.html`) is NOT in git yet.
- `team-notes` branch = PR #2 (these notes).

## Conflict to resolve (Eren + Adrian)
Adrian's `main` moved: README now in English (PR #1 merged) and **PR #3 "mission simulator with best launch dates"**
(`mission.html`, ~2000 lines, merged 14:15): patched-conic trajectories from Nova Scotia, delta-v, Meeus ephemeris,
Open-Meteo launch weather, its own site viability and best window.
- It overlaps our calendar (B) and contradicts our decision "no trajectories" (DECISIONS, organizer session).
- It uses a different ephemeris (Meeus) from ours (Horizons); two answers for the same site and date can differ.
- Our branches are based on 8fb9aea and will need a rebase onto the new `main` before any PR.
- Team must pick one story for the pitch: our calendar, Adrian's simulator, or the simulator as a side page clearly labelled.

## People
5 members; 3 not named in the notes; roles not agreed; 3 new members must be on the NASA Members tab.

## Next
- Eren + Adrian: resolve the PR #3 overlap (one product, one ephemeris for numbers shown).
- FRONTEND 2: mission pins (D). SUBMISSION session: README/AI-use/credits/demo drafts.
- 22:00 checkpoint: pick from the parked list.
