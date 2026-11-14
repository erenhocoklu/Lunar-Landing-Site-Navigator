# Frontend + engine: merge plan agreed (waits for Eren's push decision)

- Engine branch `engine` (worktree `engine-wt`): 4 local commits b6af83d..6b35b0b on top of 8fb9aea (English translation,
  PR #1). Engine treats them as final; later additions come as new commits on top, engine paths only.
- Proposal (Eren decides at push time): one linear history, one PR to Adrian that supersedes PR #1:
  8fb9aea (translation) -> engine commits -> frontend commits on top.
- Path split: engine commits `pipeline/` engine files + `data/{sites,psr,heights,terrain_meta,cap_heights,cap_meta}`.
  Frontend commits only `index.html`, `CREDITS.md`, `pipeline/make_subpoints.py`, `data/subpoints.json` (never copies of engine files).
- Frontend re-copied the engine's rebuilt data files into its working tree for testing; stamp `versions.code` = 74c264f.
- Design: the real page will follow `design-drafts\draft-e-final.html` once Eren approves (right panel = numbers in plain
  language, bottom drawer = Timeline + Landing calendar, full-screen LOLA 3D).
