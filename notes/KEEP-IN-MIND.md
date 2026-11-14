# Keep in mind

Short reminders that must survive the weekend. Source for each in brackets. Never delete; strike through with a date.

## From the LunaNav teardown (log 2026-11-14-1310)
- **Do not compete on what they already do well.** Their Sun/Earth positions match Horizons (MEASURED), and their
  3D view, voice and Arabic version are polished. A globe, voice or "site + date in, % out" is not our edge.
- **Our edge, in one line:** they answer "how sunny is this point"; we answer "where and when can I land".
  Search over many spots + landing-window calendar + filter sliders.
- **Validation goes on a slide.** Their terrain is "not independently validated" (their docs). Ours: Shackleton S
  2 m mast 83.4% / surface 79.1% vs Glaser 2018 81.0% (MEASURED, log 1400). Plus browser ephemeris max 0.0042 deg vs Horizons.
- **Resolution changes the answer.** 1 km grid best ~66%; 20 m near terrain finds ridges near 80%. Say this, with numbers.
- **Show a range, not one exact %.** 2 m mast vs surface spread. Never a bare one-decimal number.
- **Cover past 2028.** Their data ends 31 Dec 2028; ours runs 2027-2031. Slips push missions later.
- **Match them on three things:** a plain "limits" note under every result; the Horizons check shown with numbers;
  launch-delay and battery readouts in plain words.
- **Cheap wins they have that we lack:** Earth clearance option (0/1/2/5 deg). They lack: Sun elevation at touchdown,
  permanent-shadow filter, relay toggle, search. Build those.
- **Pitch tone:** "we do X", never "they are wrong". Do not mention their commit dates.

## Rules hygiene (CONTEXT.md, teardown)
- **Our git history must start after Sat 14 Nov 08:30.** Space Apps forbids work before the hackathon.
- **Credit every AI tool and asset**, including any AI voice (ElevenLabs) and any sound effect. Missing credits are easy to spot.
- **Load fast.** Their first screen takes ~10 s and ~35 MB. Keep ours light; test on weak Wi-Fi.
- **Light mode for the projector.** Their site is dark only.
- **Plain words for the public.** Avoid labels like "7.2 deg below horizon" next to "elevation -0.92 deg" without explanation.
- **No code, text or images from LunaNav.** Their repo has no licence (all rights reserved). Ideas only.
