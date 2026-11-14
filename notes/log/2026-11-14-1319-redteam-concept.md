# Red team: landing-window calendar concept (DECISIONS item 7)

Read only. Inputs: DECISIONS, GOTCHAS, CONTEXT, prior-art report, logs 1258, 1310, 1400, 1430, playbook rules 5/6/17.
No new measurements; every number below is quoted from those files with its original label.

## Verdicts
1. **Worst problem (fixable, must fix): search and exact numbers live in different places.** Exact values exist only for
   4 named sites; the searchable whole-pole layer is 1 km, misses ridges (best 65.8% vs ~80% at C1/S, MEASURED log 1400),
   worst +11.7 points vs reference, 75% of spots hit the map edge. A jury question "so your search finds the wrong spots?"
   has no answer today. Fix: precompute a small exact grid (e.g. 5 x 5 km at 100 m, 20 m near terrain) around each of the
   4 named sites, so "best spot within N km of my site, for my window" is exact. The 1 km layer stays a labelled screening map.
2. **Rivals (fixable):** LunaNav has ranking 2027 + "launch delayed N days" + voice, ends 2028-12-31; LunarWindow has the
   date-slip framing, API only; Wueller 2026 is a static 130-site calendar 2025-2032 with one fixed rule; Iris = averages.
   Ours: every window 2027-2031 under user limits, 20 m terrain, validated vs Glaser, relay and PSR filters.
   QuickMap Compute Visibility is STILL UNCHECKED: open it before anyone says "no tool does this".
3. **Useful? (fine, with framing):** trajectory sets dates; lighting filters them (log 1258). Users = early studies,
   proposals, CLPS re-plans after slips (OIG: ~14 months average slip), teaching. Pitch line: "Trajectory gives you
   candidate dates; we show in seconds which sites survive them." Never claim it picks launch dates.
4. **Numbers (fixable):** the planned validation slide mixes heights (S 2 m 83.4% vs Glaser surface 81.0%). Compare like
   for like: S surface 79.1 vs 81.0, C1 2 m 85.6 vs 88.0. Sun is validated, Earth contact is not: add one Earth check vs
   PGDA 69 average or say it is unvalidated. Show 2 m vs surface as a range, not one decimal. NASA 25%/5% = map masks
   in a 2024 seminar deck with no time period: label exactly as GOTCHAS says.
5. **Scope (fixable, cut now):** cut in this order: AI agent, voice, three.js rewrite (keep old view; horizon chart + calendar
   are the hero), request-precalc button (static text), data-quality chips, LQCIP readout, whole-pole layer polish.
   Keep: calendar + funnel for 4 sites + local grids, sliders, mast 0/2/10, relay switch, PSR distance per site, provenance line.
6. **AI agent (fails rule 17):** sliders already do the job; "plain request -> slider values" is bolted on. Cut. Failure
   reasons in cells come from the engine as plain text, no LLM needed.
7. **Slide 1:** "Your landing slipped. Which south-pole sites still work, and on which dates? Every landing window
   2027-2031 against 20 m NASA LOLA terrain; sunlight within 2 points of a published study. Geometry only, not a flight tool."

## Side note for the organizer
Log files 1320-1430 carry times later than the laptop clock at this writing (13:19 local). Check the file naming times.
