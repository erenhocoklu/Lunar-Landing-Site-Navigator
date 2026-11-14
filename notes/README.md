# Team notes (Peaks of Light, Space Apps Alba Iulia 2026)

Shared notes for the event: what we build, what is decided, what is still open, traps we found,
and the logs of each piece of work. Use them to get everyone on the same page.

**To discuss or disagree:** comment on the pull request that added these notes, or open an issue.
Point to the file and the item number (e.g. "DECISIONS open item 5").

## Files
| File | What is in it |
|---|---|
| `CONTEXT.md` | what we build, deadlines, official rules, data, who owns what |
| `DECISIONS.md` | decided items, and the open list ("Open, Eren decides") |
| `GOTCHAS.md` | traps found so far |
| `STATUS.md` | where we are now (overwritten at each checkpoint) |
| `KEEP-IN-MIND.md` | short reminders for the pitch and the build (our edge vs rival teams, rules hygiene) |
| `AI_USE.md` | running log of AI use (the NASA submission must describe it) |
| `CREDITS-PENDING.md` | packages, data and papers to copy into the repo's `CREDITS.md` |
| `log/` | one note per piece of work, newest last |

## Rules for anyone (human or AI) adding to these notes
### Before work
1. Read `CONTEXT.md`, `GOTCHAS.md`, `DECISIONS.md` and the last 2 notes in `log/`.
2. Items under "Open, Eren decides" are NOT decided: do not build on them as fact.

### After work
1. Add one note: `log/YYYY-MM-DD-HHMM-<area>-<topic>.md` (area = engine, frontend, research, organizer).
   Contents: what you did, what you measured (with the command or test), what changed, open questions.
2. Architecture, paths or run commands changed -> update `CONTEXT.md`.
3. You need a choice made -> add it to "Open, Eren decides" in `DECISIONS.md`. Only Eren moves it to Decided.
4. Hit a trap -> append to `GOTCHAS.md`.
5. Used an AI tool -> one line in `AI_USE.md`.
6. Added a package, dataset, paper or media file -> one line in `CREDITS-PENDING.md`.

### Writing rules
- Short and concrete: file paths, commands, numbers with units.
- Every number carries a label: **VERIFIED** (checked against an external source), **MEASURED** (our test,
  say which), or **UNVERIFIED**. No invented numbers. A number marked "do not quote" never goes on a slide.
- English only (the NASA submission must be English).
- Never delete entries. Strike outdated ones through with ~~text~~ and a date.
- No secrets (API keys, tokens, passwords).
