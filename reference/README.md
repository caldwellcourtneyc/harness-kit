# reference/: worked examples from a live harness

Real files from Courtney's working harness (snapshot 2026-09-28), with personal details, private system names, and machine paths taken out. They exist to show what mature harness pieces *look like*. The seed builds your own versions; nothing here installs as-is.

**How to read the marking:** each file that needs something only you can supply has a kit note at the top saying what to adapt, and uses placeholders like `<your journal folder>`. Where a file is her personal calibration rather than general method, the note says so. "Courtney" appears only as the credit for where a method came from.

## rules/: always-on rules, each earned by a dated incident

The thing to study is the *form*: trigger, action, scope, and the incident that produced the rule, kept at the bottom. They weren't designed in advance; they were encoded from failures, which is why they carry weight a borrowed rule can't.

- **absent-source-discipline.md:** when a lookup fails (404, empty page, timeout), the gap has to reach the output as "unverified" instead of being filled with plausible content. The most transferable file in this folder; the failure is every LLM's. The kept incident is generalized, and there's only one on purpose: a rule earns its teeth from *an* incident, and copying someone else's pile of incidents is exactly what not to do.
- **layout-measure.md**, **first-screenful.md** and **type-scale.md:** three rules for visual work that ship together (no dead space beside narrow elements; design the first screen as a priority stack; pick a small type scale once). Each uses a `paths:` line so it only loads when web files are read. If you build visual things, also keep a short avoid-list of Claude's house look (see CATALOG.md, "Always-on rules"); otherwise everything it makes starts to look alike.
- **security-build-guardrails.md:** later shelf. Build-time security rules for code: no keys in browser code, logins that fail closed, fenced file access, debug routes off.

## memory/: the recall system's two halves

- **MEMORY-index-example.md:** a real memory index, one line per fact, each with a phrase saying when to open the full file. The index loads every session; the files behind it load on demand. The format is the point; every entry is someone else's.
- **feedback-critique-not-verify-on-visual-builds.md:** one full memory file showing the anatomy (frontmatter, the incident, **Why**, **How to apply**, links). It records one of Claude's own failure modes, encoded so it can't quietly recur.

## commands/ and skills/: packaged methods

The starter tools. Reading order if you're studying the form: **reframe.md** (a whole method in a few lines, with an empty lessons table waiting for real use), **x-ray.md** (a structured checkpoint), **pickup-SKILL.md** (session re-entry), **land-SKILL.md** (a sequencer that calls other tools), then the three big ones.

- **x-ray.md**, **reframe.md:** thinking at forks. Fully general.
- **pickup-SKILL.md:** cold re-entry: reconstruct commitments, check what's actually on disk, then continue or close.
- **land-SKILL.md:** the close-out chain as one command. A portable version written for this kit; the original is wired into a live dashboard.
- **surface.md**, **capture.md**, **handoff.md**, **journal.md:** the close-out set. `capture.md` is the clearest example in the kit of "copy the shape, not the content": its method is general, and every destination in it is a placeholder for your own stores. `handoff.md` is elaborate because it grew from incidents; your first version should be one template.
- **codehealth.md:** code review aimed at Claude's own failure modes. Later shelf, shipped here.

## hooks/: mechanical enforcement, both halves shown

- **deny-destructive.sh**, **deny-credential-paths.py**, **deny-git-add-all.py:** guards that run before shell commands and block the move outright. Read each one's header: they say what they catch, what they deliberately ignore, and their known gaps.
- **reindex-journal.sh:** after a write into your journal folder, reminds Claude to update the search index. Set the folder and the message in the two variables at the top. Also shows the JSON output shape a hook needs for its message to reach Claude.
- **confirm-push.py**, **protect-append-only.py**, **gate-show-before-save.py**, **session-start.py:** later-shelf hooks: a push and deploy gate, a guard against overwriting the journal from an old copy, a mechanical show-before-save gate on memory and rules, and a session-start check that says where you left off and re-tests your guards. See `later/README.md` for each one's moment.
- **settings-hooks-example.json:** the other half of every hook install, the `settings.json` wiring. A script with no entry here never fires, silently. The later-shelf hooks sit in a separate block to move in when their moment comes.

**Every hook header has two test lines,** one input it should block and one it should allow. Run them after installing. A hook that crashes lets everything through without a word, so an untested guard is not an installed guard.

## friction/: the learning loop

The journal command logs friction at session close; this folder is the half that reads the log: a method README (start there), the watch-for prompts, a zero-dependency reader script, the weekly synthesis skill, a schedule note naming who runs it, and one real weekly synthesis (names generalized) as the output shape. The vocabulary and prompts were derived from Courtney's log; re-derive them from yours after about a hundred entries.

## later/: the "add it when you need it" shelf

Six more tools and a transcript script, each with the moment it starts paying for itself. See `later/README.md`, which also lists the later-shelf hooks, rule, checklist and backup file that live elsewhere in this folder. During setup, those moments go into your CLAUDE.md's Toolshelf section, so Claude offers each one when its moment comes.

## Setup references

- **skill-authoring.md:** how to write a skill whose trigger actually fires. The seed reads it before installing any skill; keep it for writing your own.
- **example-rules.md:** a menu of nine collaboration rules with their reasons, offered in the seed's Phase 4. Pick, never pre-install.
- **new-project-checklist.md:** later shelf. What a new project needs on day one.
- **backup/gitignore:** later shelf. A ready `.gitignore` for backing up `~/.claude` to a private repo.

## tools/

- **journal-overlap.py:** checks a new journal draft against recent entries so the journal doesn't restate itself. Called by `journal.md`.

## CLAUDE-skeleton.md: the always-loaded file

The annotated structure of a mature CLAUDE.md: each section's job, a few real lines as examples, and slots for yours, including the Toolshelf and the two-week check-in. The one file here built for direct use as a starting template.
