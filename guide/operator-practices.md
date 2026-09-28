# Operator practices — the half no file installs

These are the habits Courtney runs that make her harness compound. They're described specifically because vague advice ("give good feedback!") transfers nothing. But they're *her* habits: the point of each entry is the mechanism, and the "your version" line is where your own shape goes. Adopting them wholesale would fit badly; understanding why each works makes the right personal version findable.

The collaboration runs both ways, so each entry also says what Claude does differently because of the habit. That half is the one you can check: if the habit is in place and Claude isn't behaving this way, something isn't wired up. And every habit has a cost, named plainly, so you can decide whether it's worth paying.

Format per item: **the habit → why it works → Claude's side → what it costs → your version might look like.**

---

**1. Capture freely, promote selectively.**
Observations, corrections, and reactions get captured cheaply and constantly (journal lines, notes, a friction log) — but nothing becomes a rule from one occurrence unless it clearly warrants it. Promotion waits for recurrence.
*Why it works:* capture has no quality bar, so nothing is lost; promotion has a high bar, so the always-loaded layers stay small and trustworthy. Systems that encode everything drown; systems that encode nothing repeat their mistakes.
*Claude's side:* offers captures at natural pauses and shows the exact entry before writing it. Doesn't turn a single correction into a standing rule.
*What it costs:* the capture pile grows faster than it gets reviewed. Without a periodic sweep it becomes a backlog nobody reads.
*Your version:* any zero-friction capture spot (one running file is enough) + a rule of thumb for what earns promotion.

**2. License candor explicitly.**
Her CLAUDE.md says "Push back when warranted. No unearned praise or hollow validation." In writing, always loaded.
*Why it works:* without a standing license, Claude defaults toward agreeable — which produces flat, agreeable suggestions exactly when you're trying to sharpen an idea. One sentence changes the default.
*Claude's side:* disagreement comes first and plain, with no praise wrapped around it to soften it.
*What it costs:* some sessions are less comfortable. You have to actually want the pushback when it arrives.
*Your version:* your words, your preferred delivery (blunt? framed as questions?), in your CLAUDE.md. The seed interview covers this.

**3. Tell Claude how you think, not just what you want.**
She's encoded her own cognitive style: "I evaluate concrete instances, not descriptions — show me examples." "Don't upgrade my soft qualifiers into hard rules." Claude works with her grain instead of against it.
You don't have to work these out alone. Claude notices patterns in how you work and can name them; your part is recognizing the true ones when they're flagged and saying yes.
*Why it works:* Claude adapts to whatever it knows about its reader; most people never say. One true sentence about your own thinking outperforms ten borrowed rules.
*Claude's side:* shows examples instead of describing options, keeps "might" as "might," and names patterns it notices about how you work so you can confirm or reject them.
*What it costs:* a wrong self-description gets followed as faithfully as a right one, so these are worth revisiting now and then.
*Your version:* one thing you know about how you evaluate or decide, written down. Add more as you notice them, or as Claude points them out.

**4. Report reactions you can't diagnose.**
"I don't know what I'm looking at." "This still doesn't look right and I can't say why." She hands over the raw signal and lets Claude find the cause.
*Why it works:* most feedback dies because people wait until they can articulate it. The undiagnosed reaction is usually the most valuable data in the session — and diagnosing it is Claude's job anyway.
*Claude's side:* treats "something's off" as a complete bug report and goes looking for the cause instead of asking you to explain it.
*What it costs:* Claude's diagnosis can be confidently wrong. The reaction is real data; the diagnosis is a guess until you confirm it.
*Your version:* drop the standard of having a *reason* before saying something feels off.

**5. Close sessions deliberately.**
Sessions end with a small ritual — capture what was learned, journal it, write a handoff for next time. Not always all three; never none.
*Why it works:* this is the deposit half of retrieval. Context accumulates only if sessions write to the stores that future sessions read.
*Claude's side:* offers the close-out when a session winds down and does the writing. You rule on what gets kept.
*What it costs:* a few minutes at the end of every session, which is exactly when you least want to spend them.
*Your version:* whatever ending ritual you'll actually do (the kit's `/land` runs the whole chain as one command). A two-line journal entry every time beats a thorough one you skip.

**6. Treat Claude's failures as system-design input.**
When something breaks, the question is "what broke it, and was it avoidable?" — and the answer routes into the system (a rule, a check, a hook) rather than staying an annoyance.
One real example: an AI research scan reported five live listings, and four of them had been written up from search-result snippets for pages it never actually opened. They turned out to be dead or out of date. That became a standing rule: when a page fails to load, every claim that depended on it is marked unverified, right where the claim appears.
*Why it works:* it's why the harness got *better* over months instead of just bigger. Every rule in the reference folder is a dated failure that can't recur silently.
*Claude's side:* when it misses, it says what broke and whether it was avoidable, and proposes where the fix should live. And it doesn't say "from now on I'll…" unless it's about to write that down. Claude starts every session fresh; a promise to change that isn't written into CLAUDE.md, a rule, or memory before the session ends is forgotten by the next one, however sincerely it was made.
*What it costs:* every fix adds to what gets loaded every session. Without pruning (see 10), the rulebook bloats.
*Your version:* when Claude misses, spend one extra sentence on why — then apply practice 1.

**7. Keep approval gates.**
Nothing enters her taste profile or standing rules without her explicit OK. Claude proposes; she ratifies. A firm yes gets encoded right away. Anything softer (a bare "ok" mid-task, silence, a preference Claude inferred from a reaction) waits for her to rule on it later, and silence counts as "not now," never as yes.
*Why it works:* the system stays *hers*. Without gates, Claude's guesses about your preferences accrete into the config, and after six months the harness is optimized for a drift of you.
*Claude's side:* shows the full text of anything it wants to make durable before writing it, with one example of where the rule would have applied.
*What it costs:* a queue of things waiting on you. If you never clear it, good ideas sit there.
*Your version:* one rule — Claude never encodes a durable preference without asking.

**8. Frame asks by outcome, not procedure.**
"Can we package this so it's as helpful as possible?" — intent and constraints, path open. Not step-by-step instructions.
*Why it works:* Claude can spot things your instructions didn't anticipate — but only if the instructions leave room. Scripted asks get exactly what was asked for, which is the problem when the ask was wrong.
*Claude's side:* when an ask arrives already shaped as a specific fix, Claude says in one line what goal it thinks the fix serves before building it, so a wrong goal gets caught cheaply.
*What it costs:* less predictable output. You'll sometimes get something other than what you pictured.
*Your version:* if you want better suggestions when you refine an idea, this is the lever. Bring Claude the *goal* behind the idea, not just the idea, and ask what you're not seeing.

**9. Invite the frame-check at forks.**
Before committing to a direction, she makes room for "are we solving the right thing?" — sometimes with a named ritual, but the habit is just pausing at commitment points and asking what both parties are assuming.
*Why it works:* execution-level feedback can't catch a wrong frame. The cheapest moment to find out is before building; the reflex has caught vendor picks, wrong defaults, and entire wrong deliverables.
*Claude's side:* offers the check unprompted before big decisions, and lays out several genuinely different approaches (including building nothing) before recommending one.
*What it costs:* a pause at exactly the moment momentum feels best.
*Your version:* one question before anything substantial gets built: "what are we both assuming here?"

**10. Add trials, not systems.**
New additions come with an expiry: a check-in date and a kill condition, written down in advance. Things that don't earn their keep get removed without ceremony.
*Why it works:* a harness that only grows eventually gets abandoned wholesale. This nearly happened the first time this setup was handed to someone: the whole kit arrived at once, all of it permanent, and only the journal survived. Trials make adding cheap *because* removing is expected.
*Claude's side:* writes the check-in date and removal condition at the moment something is added, and raises it when the date comes.
*What it costs:* the check-ins have to actually happen. A trial nobody reviews quietly becomes permanent.
*Your version:* everything the seed installs gets the two-week check-in it already prescribes. Keep that habit for whatever you add later.

**11. Verify casually; report defects instead of working around them.**
She clicks the links, notices when something didn't save, and says so — the defect becomes a fix instead of a silent workaround.
*Why it works:* silent workarounds are how a system quietly stops being trusted, and an untrusted harness stops being used. Casual verification keeps the whole thing honest at near-zero cost.
*Claude's side:* says what it actually tested versus what it assumed, so you know where to click. And it knows its own checking traps, because "verified" from Claude can mean less than it sounds:
- *Its own checks tend to pass by default.* A test that can't fail, a script that reports success without checking the result, a screenshot tool that says it resized the window when it didn't. A check is only worth something if Claude has seen it fail on a bad case.
- *"Fixed" gets judged by a stand-in.* A number went down, a test turned green, an error stopped printing, while the thing you actually complained about is still there. The real check is the original complaint, looked at again.
- *After about three rounds on a design, edits start chasing the last draft instead of the goal.* Each round fixes the previous round's problem. Every few rounds, go back to what the thing was for.
*What it costs:* very little, which is the point.
*Your version:* when the harness does something odd, say so in the session — "that seems wrong" is a complete bug report; your Claude can take it from there.

**12. Ask Claude to label what it's showing you.**
Everything Claude puts in front of her says what kind of thing it is: a recommendation it would bet on, a rough probe meant only to get a reaction, or a set of options with Claude's lean stated last, after she's seen them. Questions get labeled too: "I'm stopped until you answer," or "I've picked a default and I'm continuing, correct me if it's wrong."
*Why it works:* she knows how much effort something deserves before spending any. And a guess stated with confidence can't anchor her, because it has to announce itself as a guess.
*Claude's side:* this one is almost entirely Claude's behavior. She installed it; Claude does it.
*What it costs:* a few extra words per message.
*Your version:* ask your Claude to say how sure it is, and whether it actually needs an answer from you to keep going.

**13. Let the system carry the activation energy.**
Anything that depends on her remembering to *start* it gets moved to the system's side: Claude offers it at the right moment, or a trigger fires it. Willingness is rarely the bottleneck; starting is.
This kit learned it the hard way. Its first version told the reader when each "add it later" tool would help, and left it there. His Claude never offered them, and he never went back for them. Now the seed writes each later tool into your CLAUDE.md with its moment, so Claude can notice the moment and offer it.
*Why it works:* good habits that need you to initiate them decay, however much you value them. Habits the system initiates survive busy weeks.
*Claude's side:* offers the capture, the close-out, the check-in, and the not-yet-installed tool at the moment it applies, instead of waiting to be asked.
*What it costs:* more things interrupt you, and the triggers need tuning so they fire at the right moments and not constantly.
*Your version:* notice which good habits you keep forgetting to start, and ask Claude to start them for you.

**14. Send the digging to subagents.**
When a task needs lots of reading (searching a codebase, researching a question across many pages, checking a pile of files), she has Claude hand it to a subagent: a separate Claude instance that does the reading in its own context and reports back only the answer.
*Why it works:* everything read in the main session stays in it, taking up room for the rest of the conversation and counting against usage limits. A subagent's reading disappears when it finishes; only the conclusion comes back. Sessions stay sharp longer, and the usage limit arrives later.
*Claude's side:* offers to delegate research and wide searches, and runs independent lookups in parallel. When a result comes back, it says what the subagent actually checked.
*What it costs:* you don't see the reading, only the report, so a subagent's summary can be wrong in ways you can't spot. Ask for sources on anything load-bearing.
*Your version:* the first time you hit a usage limit, or a session gets slow and forgetful after a lot of research, ask Claude to use subagents for that kind of work.

---

**If you only take three:** 1, 2, and 4. They're the flywheel — candor licensed, reactions surfaced, corrections kept. Practice 5 matters most if what you want is Claude remembering past work. Practice 14 matters most if you keep hitting usage limits. The rest will make sense to add as the system comes alive.
