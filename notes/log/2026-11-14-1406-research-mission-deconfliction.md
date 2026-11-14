# Research: avoiding other lunar missions (manager, 3 researchers)

Notes: `..\research_notes\Lunar mission deconfliction\` (coordination_systems.md, mission_dataset.md, plume_rules_tools.md).

## Findings
- No real "who lands where and when" system exists (NASA, ESA, CNSA, UN, industry) as of 14 Nov 2026.
  Artemis Accords s.11: self-declared, temporary safety zones with no numbers; none publicly declared. UN ATLAC still
  discussing a consultation mechanism (recommendations 2027). Open Lunar's Lunar Ledger (Sep/Oct 2025) = voluntary mission
  database, closest to a registry (API not checked).
- No working deconfliction software found. LunaNav (checked live) has no other-mission layer.
- Distances: NASA 2011 recommendations (non-binding): land >= 2.0 km from historic lander sites (whole 3-sigma ellipse
  outside), 0.5 km from impact sites; walking buffers 75 m (Apollo 11) / 225 m (Apollo 17). CORRECTION: an earlier manager
  statement of "0.75 km" was wrong. Apollo 12 landed 155 m from Surveyor 3 and sandblasted it. Rocks up to 1.5 km (Apollo).
  Metzger 2024: 2 km is a placeholder; large landers throw far more. No Starship/Blue Moon keep-out published.
- Mission list: no public file of all landers; hand-build ~15 rows (id, name, agency, lat, lon, precision, radius_km,
  date_text, status, quality, source_url). Actual positions from LROC (IM-1 -80.13/1.44; IM-2 target -84.78/29.13;
  Luna-25 crash -57.865/61.360). Planned sites mostly region names only. Crowded clusters: Mons Mouton/Nobile
  (IM-2 wreck, Griffin-1, VIPER, PROSPECT/IM-4, Chang'e-8 candidate, Artemis regions) and Shackleton (Blue Moon MK1, Chang'e-7).

## Proposed rule set (Eren decides; DECISIONS item 13)
- Lander/historic site >= 2.0 km (NASA 2011); impact site >= 0.5 km; large-lander caution radius set by user (5 km default
  is OUR assumption, labelled). Reference markers: 155 m, 1.5 km. Active mission nearby in the window -> "coordinate" flag.
- Each mission drawn as a circle sized by position precision (LROC point / target / region / unknown).
- Label: "Public announcements and NASA 2011 non-binding guidance, not an official registry or law."
