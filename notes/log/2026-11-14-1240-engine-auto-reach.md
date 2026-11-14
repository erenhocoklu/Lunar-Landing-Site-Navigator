# Engine: automatic horizon reach (Eren's idea, decided 12:40)

## Idea
Instead of a fixed reach (150 or 250 km), each ray walks outward and stops once even the tallest terrain on the whole
map (7026 m, from the DEM) could not rise above the horizon already found in that direction. The Moon's curvature makes
this happen at a finite distance. A ray that leaves the map is flagged.

## Test (MEASURED, scratchpad `speed/autostop.py`, 80 m DEM, 4 rays/deg, 0.5% step, surface observer)
| Site | Auto vs walk to map edge | Auto vs fixed 250 km | Stop distance median / max | Rays at map edge | Time auto / full |
|---|---|---|---|---|---|
| Connecting Ridge C1 | 0.0000 deg | 0.000 deg | 198 / 272 km | 0 | 189 / 239 ms |
| Shackleton rim S | 0.0000 | 0.000 | 198 / 272 km | 0 | 181 / 264 ms |
| de Gerlache rim (box) | 0.0000 | 0.000 | 198 / 272 km | 0 | 167 / 231 ms |
| Malapert (box) | 0.0000 | 0.000 | 40 / 272 km | 0 | 114 / 220 ms |
| Shackleton (box) | 0.0000 | 0.000 | 55 / 144 km | 0 | 104 / 212 ms |

Stop distances are rounded up to 64-sample blocks. The bound uses the global DEM maximum; a local maximum would stop
rays sooner (not tested).

## Result
Same answer as looking forever, faster than a fixed 250 km, and no number to defend. Pitch line:
"we search until terrain can no longer physically block the Sun."
