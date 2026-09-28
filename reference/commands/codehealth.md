Review code for vibecoding risks — breakage, security, and Claude's own failure modes (over-abstraction, debug artifacts, unnecessary complexity). This is the project-health review: full files (not just diffs), stack-aware via CLAUDE.md, plain-language report with saved history. Division of labor: for pre-commit correctness on a specific diff, the built-in /code-review is sharper; for everything else code-review-shaped — health checks, debt sweeps, "how's my code" — use this. Modes: quick (recent changes), deep (full audit), file (single file). Never auto-run.

---

## Invocation

- `/codehealth quick` — lightweight check on recent
  changes
- `/codehealth deep` — thorough audit after substantial
  building
- `/codehealth deep --focus [area]` — deep review
  narrowed to one area (security, architecture,
  production, debt, dependencies, data)
- `/codehealth [filepath]` — focused review of a
  single file regardless of git state

---

## Step 1: Determine Scope

### Quick mode
1. Check if inside a git repo (`git status`)
2. If yes: scope = `git diff` (staged + unstaged) +
   untracked files. Read the full content of all
   changed files, not just the diff — you need the
   surrounding context to review properly.
3. If no git repo:
   - Single-file project? Scope = that file
   - Multi-file? Scope = files with mtime in last
     7 days (use `find` or equivalent)
   - Always exclude build output directories:
     dist/, build/, .next/, node_modules/, __pycache__/
     and any files in .gitignore (if it exists)
4. If nothing changed: tell the user and stop.

### Deep mode
1. Find the divergence point:
   - `git merge-base HEAD main` (or master)
   - Or date of last deep review in
     `.claude/reviews/`
   - Use whichever is more recent
2. If `--focus [area]` provided, still read everything
   but only report on that area
3. If no git history: scope = full project

### File mode
1. Read the specified file in full
2. No git needed

---

## Step 2: Read Project Context

1. Read the project's CLAUDE.md (if it exists)
2. Extract: tech stack, deployment target, known
   issues, conventions, current priorities
3. If no CLAUDE.md found, note it in output and use
   universal checks only

---

## Step 3: Read Previous Review

1. Check for `.claude/reviews/` directory
2. If it exists, read the most recent review file
3. Extract previously flagged issues for tracking
4. If no previous review exists, skip this step

---

## Step 4: Run Checks

### Universal Checks (all modes)

**Breakage:**
- Removed imports still referenced elsewhere
- Changed function signatures without updating callers
- Altered return types or data shapes
- Missing references (deleted files/functions still
  imported)
- Renamed variables/functions without updating all
  usage

**Security:**
- Exposed secrets or API keys (especially in
  client-side code)
- Missing auth on new endpoints
- Hardcoded credentials
- Open endpoints without protection
- Sensitive data in URLs or query strings
- Missing input sanitization on user-facing inputs

**Maintainability (Claude's failure modes):**
Assume Claude wrote this code. Specifically check for:
- Functions over ~50 lines with no clear structure
- Abstractions or helpers used in only one place
- Magic numbers / hardcoded values with no comment
- Code that requires understanding 3+ other files
  to follow the logic
- Patterns that differ from the rest of the project
  without clear reason
- Over-engineering: config objects, factory patterns,
  or indirection layers that aren't needed yet
- Leftover debug artifacts (console.log, commented
  code, TODO placeholders that aren't real TODOs)
- Variable/function names that are unclear or
  misleading

**Failure modes:**
- Missing error handling on API calls, DB queries,
  file operations
- Unvalidated user inputs
- Unhandled edge cases: empty states, null/undefined
  values, network failures, timeouts
- Race conditions in async code
- Missing loading/error states in UI code

### Deep Mode Additional Checks

**Architecture health:**
- Circular dependencies
- God files (doing too many unrelated things)
- Duplicated logic that should be consolidated
- Inconsistent patterns across similar features
- Component/module boundaries that have eroded

**Production readiness:**
- Error handling at all system boundaries
- Environment config: all env vars documented and
  accounted for?
- Edge cases: auth expiry, concurrent users, stale
  data
- Missing rate limiting on public endpoints
- Missing CORS configuration (or overly permissive)

**Accumulated debt:**
- Patterns that were "fine for now" but compounded
- Quick fixes that now need real solutions
- TODOs that have been sitting across multiple
  sessions
- Workarounds that outlived their reason

**Fragility assessment:**
- What parts would break if you added the next
  feature?
- Tight coupling points
- Implicit dependencies (ordering, timing, global
  state)

**Dependency health:**
- Unused dependencies in package.json
- Known vulnerabilities (check if aware of any)
- Outdated packages that affect functionality

**Data safety:**
- Database migration risks
- Data loss scenarios
- Backup considerations
- State persistence assumptions (localStorage,
  session, DB)

**Staleness:**
- How long since this project was last actively
  developed?
- Are there dependencies or APIs that may have
  changed since last touch?
- Any deprecated patterns or APIs in use?

### Stack-Specific Checks

Read the project's CLAUDE.md to identify the stack. Apply
checks relevant to what you find — common stack-specific
risks to watch for: hook dependency arrays and SSR/client
boundaries (React/Next), RLS policies and exposed service
role keys (Supabase), edge function limits and env var
parity (Vercel), event listener cleanup and localStorage
assumptions (single-file HTML), static asset paths
(GitHub Pages).

If unfamiliar with the stack, ask the user before
proceeding rather than guessing at the right checks.

---

## Step 5: Assess Future Considerations

This is the highest-value section for vibecoding.
For every finding AND for the codebase generally,
ask: "What's fine now but will matter later?"

Examples:
- "API key is in env var but no rate limiting — fine
  for beta, needs attention before scaling"
- "localStorage handles all persistence — works for
  single device, breaks with multi-device sync"
- "No error boundary — first uncaught error will
  white-screen the whole app"
- "This file is at 400 lines — still manageable but
  nearing the point where it should split"
- "Inline styles work but will fight you when adding
  themes or dark mode"
- "No loading skeleton — fine now but will feel
  broken on slow connections"

---

## Step 6: Format Output

```
## Code Review — [Quick/Deep/File] — [Project Name]
Scope: [what was reviewed — e.g., "14 uncommitted
changes across 5 files"]
[If no CLAUDE.md: "No project CLAUDE.md found —
used universal checks only. Consider creating one."]

### FIX NOW
- [Plain language description of issue]
  → [What to do about it]

### FIX SOON
- [Plain language description of issue]
  → [What to do about it]

### WORTH KNOWING
- [Observation or pattern worth being aware of]

### FUTURE CONSIDERATIONS
- [Thing that's fine now but will matter when X]
  → [When to revisit]

### PREVIOUS FINDINGS
- [Issue from last review] — resolved / still present

Checked: [comma-separated areas checked] — no issues.
```

**Output rules:**
- Omit empty sections entirely
- "Previous Findings" only if prior review exists
- "Checked" line always present, always one line —
  confirms what was looked at even when clean
- FIX NOW is never capped: show every item, however
  many there are.
- Deep mode, other sections: in chat, show 3-5
  findings per section, then "Plus N more, all in the
  saved review." The saved file lists every finding.
- Quick mode: naturally shorter given narrower scope
- Future Considerations: always included. If truly
  nothing, say "None — current approach is solid
  for the current stage."
- Use plain text markers (FIX NOW, FIX SOON, etc.)
  not emoji — better compatibility
- Keep lines under 100 characters
- Be specific: name files, functions, line ranges.
  Don't say "some components" — say which ones.
- Every finding gets an action item (→). Don't just
  identify problems — say what to do.

---

## Step 7: Save Review

1. Create `.claude/reviews/` directory if it doesn't
   exist
2. Save the full review, every finding with no
   per-section cap, to a dated file:
   - Quick: `YYYY-MM-DD-quick.md`
   - Deep: `YYYY-MM-DD-deep.md`
   - File: `YYYY-MM-DD-file-[filename].md`
3. If a file for the same mode already exists today,
   append with a separator (`---`) rather than
   overwriting

---

## Step 8: Show Output

Display the formatted review in chat. Then:

- If FIX NOW items exist: "Want to tackle the
  critical items now?"
- If clean: "Clean review."
- Always end with the review, not with praise or
  filler.

---

## Rules

- **Never auto-run.** Only run when the user invokes
  `/codehealth` or explicitly confirms a suggestion.
- **Read the actual code.** Don't review from memory
  or diffs alone. Read the full files to understand
  context.
- **Prioritize correctly.** Security and breakage
  are always FIX NOW. Maintainability and debt are
  usually FIX SOON. Observations and patterns are
  WORTH KNOWING. Things that will matter later are
  FUTURE CONSIDERATIONS.
- **Be adversarial toward Claude's patterns.** The
  maintainability check exists because Claude
  (the tool writing the code) has known failure
  modes: over-abstraction, unnecessary complexity,
  debug artifacts, inconsistent patterns. Check
  for these explicitly.
- **Cite or suppress; scenario or downgrade.** Every
  finding quotes the specific code (file + line range)
  and names a concrete failure scenario — the inputs
  or state that make it break. Your own confidence —
  or flagging the same thing twice — is not evidence;
  the code is. If you can't confirm a finding by
  re-reading the cited code, or can't name its failure
  scenario, it stays out of FIX NOW and FIX SOON: list
  it under WORTH KNOWING marked "unconfirmed," with
  what would confirm it. If the failure scenario can't
  actually occur given the rest of the codebase, cut
  it. (Adapted from the WarmHub "Council" review spec.)
- **Scrutiny floor on sensitive paths.** Changes
  touching auth, payments, database schema/migrations,
  or anything handling secrets or user data always get
  a full read — even in quick mode, never skipped or
  skimmed. This floors how hard you look, not the
  severity you assign; grade each finding on its actual
  impact (the existing priority rules still apply).
  Concentrate depth by blast radius, not diff size.
