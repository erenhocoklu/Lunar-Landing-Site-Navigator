# Credits, licences and sources

The NASA Space Apps 2026 Participant Terms require every source to be cited and every
non-NASA material to be freely available or OSI-licensed, with its licence listed here.
Add a line for every library, dataset, paper or tool the moment it is used.

## Our own work
- All code in this repository was written by team Peaks of Light during the event. Unless a
  LICENSE file says otherwise, NASA distributes Space Apps solutions under Apache-2.0.

## NASA data
| Source | Used for | Link |
|---|---|---|
| JPL Horizons API (DE441 ephemeris, MOON_ME frame) | Sub-solar and sub-Earth points 2026-2030 (`data/subpoints.json`, made by `pipeline/make_subpoints.py`); topocentric values used to check the page | https://ssd.jpl.nasa.gov/horizons/ |
| NASA GSFC PGDA product 90, LOLA south-pole DEM (`LDEM_80S_*MPP_ADJ`, Barker et al. 2023) | Terrain heights and horizon masks (engine) | https://pgda.gsfc.nasa.gov/products/90 |
| NASA GSFC PGDA product 69, LOLA illumination and Earth-visibility maps | Validation of our sunlight and Earth-visibility percentages | https://pgda.gsfc.nasa.gov/products/69 |

## Papers (site coordinates and validation numbers)
- Gläser, P. et al. (2018). Illumination conditions at the lunar poles: implications for future exploration. Planetary and Space Science 162. Sites C1 (Connecting Ridge) and S (Shackleton rim). https://ntrs.nasa.gov/citations/20170007365
- De Rosa, D. et al. (2012). Characterisation of potential landing sites for the European Space Agency's Lunar Lander project. Planetary and Space Science 74. Sites GR1 (de Gerlache rim) and MP1 (Malapert). https://arxiv.org/abs/1208.5587
- Mazarico, E. et al. (2011). Illumination conditions of the lunar polar regions using LOLA topography. Icarus 211. Horizon method.

## Third-party software
| Package | Licence | Where |
|---|---|---|
| IBM Plex Sans, IBM Plex Mono (Google Fonts) | SIL Open Font License 1.1 | `index.html` |
| Saira Condensed (Google Fonts) | SIL Open Font License 1.1 | `index.html` |
| Python standard library | PSF License | `pipeline/` |
