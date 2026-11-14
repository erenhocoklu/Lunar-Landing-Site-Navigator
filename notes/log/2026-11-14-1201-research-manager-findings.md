# RESEARCH (manager session): findings filed into the vault

Source: message from the RESEARCH session, 14 Nov. Filed by the organizer.
Sources: `reports\Lunar landing site tools prior art.md` (+ `research_notes\`), `dem-products.md`, `horizon-method.md`,
concept section of `space-apps-alba-iulia-2026.md`.

## Where it went
- Official rules, judging, team rules, Horizons call form -> CONTEXT.md
- Concept proposal (not red-teamed) -> DECISIONS.md open item 7
- Traps (demo limits, AI media, 5 m mosaic reach, longitude sign, LunaNav licence, wording, HLS thresholds) -> GOTCHAS.md

## Prior art (summary)
- The terrain-horizon Sun/Earth view is table stakes: 4+ 2026 teams built it (LunaNav, with ElevenLabs voice and no licence;
  LunarWindow, a date-slip API; lunar-horizon; LunaTrace). Iris Datalabs API ranks sites by average sunlight.
- NASA practice: date first, then site. Lighting shifts 2-3 weeks per year. 9 Artemis candidate regions (2024): Peak near Cabeus B,
  Haworth, Malapert Massif, Mons Mouton Plateau, Mons Mouton, Nobile Rim 1, Nobile Rim 2, de Gerlache Rim 2, Slater Plain.
- Crew surface stay 5.75-6.25 days (2022: 6.5 days of continuous sunlight). Robotic landers land at local sunrise and work one lunar day (~12-14 days).
- IM-2 lesson: low Sun hurt landing navigation.
- Gap: nobody searches many nearby spots x dates against user constraints and gives a reason.

## Validation targets (RESEARCH)
- Shackleton floor: 0% sun.
- Connecting Ridge: ~80-90% long-run (published 85.7%, 88.0%).
- 10 PGDA pixels on a scatter plot against the product 69 maps.

## Contradictions and gaps for Eren
1. **Horizon reach:** RESEARCH says ~150 km; ENGINE measured and recommends 250 km. Still DECISIONS open item 1.
2. **Connecting Ridge numbers are different metrics.** ENGINE: 76.2% vs Glaser 76.0% for **2027 only**. RESEARCH: 85.7% / 88.0%
   **long-run**. Both can be right. On a slide, always state the time span next to the number.
3. **Team size:** RESEARCH assumes 5 members (at least 4 present); the README lists 2. Confirm.
4. **Globe:** the shared note proposes globe.gl; the concept says "not doing a globe as the main screen". DECISIONS open item 5.
