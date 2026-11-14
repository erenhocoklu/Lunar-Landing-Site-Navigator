# Frontend: how agencies and companies show landing-site data (UI research)

Requested by RESEARCH (manager) for Eren. Web research by a Claude subagent, 2026-11-14. Read-only; no code reused.
Labels: CONFIRMED = seen at the URL; INFERRED = not seen directly.

## Bottom line
- **LunaNav (rival 2026 team, afuq.website)** is live and polished: 9-region Sun ranking, A-vs-B scenario compare,
  "launch delayed by N days", timeline lanes, horizon panorama (CONFIRMED, live). It has **no multi-year start-date
  calendar, no threshold sliders, no PSR overlay, one point per region** (as far as seen). Our calendar + sliders is the
  differentiator: lead the pitch with it.
- **ESA Lunar Lander study (De Rosa et al. 2012, arxiv.org/pdf/1208.5587, Fig. 3)**: Sun fraction -> lit/dark bands at a
  stated 50% threshold -> drop lit < 10 h -> drop dark < 60 h -> longest quasi-continuous lit period (CONFIRMED). Maps onto our
  min-sunlight and longest-night sliders.
- Agency public material (Artemis region maps, SVS 5228/5027) is static outlines or videos; **no date-picking calendar found**
  (CONFIRMED for pages fetched; INFERRED for slides not opened).

## Per source (one pattern each)
| Source | Copy / avoid |
|---|---|
| LROC QuickMap (now hosted by Intuitive Machines) | Copy the always-visible "lat,lon" box and the Sun/Earth compass. Avoid raw dataset names as layer names. |
| NASA SVS 5228 / 5027, Artemis III regions page | Avoid animation as the only way to the answer: static answer first, animation optional. |
| De Rosa 2012 (ESA), DLR/Glaser maps | Copy: write the threshold, height, filters and years on the chart itself. |
| Chang'e-7 site paper (Zhao et al. 2025, Remote Sensing 17:1121, abstract only) | Copy the funnel idea: show how many dates/sites pass each filter. |
| SpaceX HLS, IM-2, ispace | Marketing renders only; IM-2 target shown as a box without uncertainty (landed ~250 m off). Avoid targets without uncertainty. |
| LunaNav | Copy the ">=" lower-bound marker and a plain "What this means" line. Avoid dark-only theme and colour-only Sun/Earth lanes. |

## Top 5 UI patterns for our calendar + map + sliders
1. **Pass/fail calendar with the reason visible**: months x start dates; a failing cell shows which limit failed (sun / Earth /
   night glyph), not only a colour. (De Rosa Fig. 3 logic)
2. **Stacked lanes for the chosen date**: Sun, Earth, Both, longest-night bar, with slider thresholds as dashed lines. (LunaNav, De Rosa)
3. **Filter funnel next to the sliders**: "312 dates -> 41 pass sunlight -> 18 pass Earth". (Chang'e-7 screening idea)
4. **Ranking table**: bars + exact %, a tab per metric, ">=" when a dark spell is cut by the window edge. (LunaNav)
5. **Map with its settings printed on it** ("2 m mast, 2027-2029, Sun >= 50%"), lat,lon box, Sun/Earth compass,
   PSR as hatched outlines (never an "ice" colour). (De Rosa captions, QuickMap)

## Accessibility
- Continuous maps: viridis or cividis; never rainbow/jet or red-green.
- Pass/fail: blue/orange plus shape (filled vs hollow, tick vs cross).
- PSR: hatching or outline. Sun and Earth: position + label, not colour only.
- Light theme default for the projector, dark optional; text contrast >= 4.5:1.
- Sliders keyboard-operable with the value as text; calendar cells get aria-labels with the date and the failing reason.

## Not checked
NASA Eyes, ESA Moonlight UI, Chang'e-7 figures (MDPI 403), Moon Trek's interface.
Unverified claim seen in passing: "Artemis III became a LEO test" (do not quote; GOTCHAS already says crewed landing moved to Artemis IV).
