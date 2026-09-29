# Example rules: a menu, not a starter pack

**Kit note:** the seed offers this list at the two-week check-in. Nothing here is installed by default. Read the list together, pick the ones that name something that has already annoyed you, and put each one in your CLAUDE.md in your own words. A rule that didn't come from your own friction won't mean much to you when it fires; the first person this setup was handed to got a full rulebook at once, and it didn't survive.

Each entry is a real rule from Courtney's CLAUDE.md, shortened, with the reason it earned its place. The form to copy is **when this happens → do this**.

---

**1. Call the bail point.**
When the same fix has been tried two or three times without working, or three different approaches have all failed, stop and say so, with the options: try a different method, ask for something missing, start fresh, or set it aside.
*Why:* Claude looping on the same failing fix is the most common frustration for someone new. Without this rule it keeps grinding and you end up being the one who notices.

**2. Evidence before guesses.**
When something fails (an error, a broken page, a deploy that didn't work), ask for the actual error message or output before proposing a fix. Exception: the cause is visible (a typo, a missing import).
*Why:* a fix built on a description of an error is a guess. Pasting the error takes ten seconds.

**3. Name the quality bar.**
When there's a quick way and a right way to build something, say which one you're taking, what the right way would cost, and what the shortcut will cost later.
*Why:* without a coding background you can't see when Claude takes a shortcut (storing data in the browser instead of a database, hiding a page instead of protecting it). This makes it tell you.

**4. Anything other people can see needs a yes, every time.**
Before a push, a deploy, a message sent for you, or a comment posted anywhere: ask, for this one. A yes earlier in the session doesn't carry over.
*Why:* these are hard to take back. Pairs with the push gate in `hooks/confirm-push.py`, which enforces it for pushes and deploys.

**5. Explain the why, and check it stuck.**
Explain the reasoning behind a recommendation, not only the recommendation. Before treating a concept as understood, check: ask for it back in my words, or watch me use it.
*Why:* for someone learning as they build, a fix without the why teaches nothing, and having seen something isn't the same as understanding it.

**6. Test an unproven idea cheaply before specifying it.**
When a plan rests on something nobody has tried (a threshold, a guess about how people will use it), suggest a quick rough test first, before writing a detailed spec.
*Why:* detailed specs for untested ideas are the most expensive way to find out they were wrong.

**7. Done means done on disk.**
Never write "done," "added," or "fixed" in a status note or handoff unless it's actually true in the files right now. If work is still in progress, say so.
*Why:* a handoff that says something shipped when it didn't sends the next session off building on nothing.

**8. Adopt / skip / probe.**
When I bring in outside advice (an article, a video, a tool, this kit), sort it into what to adopt, what to skip and why, and at least one claim worth testing against my own setup in half an hour.
*Why:* advice written for someone else's setup is easy to swallow whole. The probe keeps it honest.

**9. Flag when a task deserves more thinking.**
Claude Code has effort levels (how much Claude thinks before answering). When a task would benefit from a higher one than the current setting, say so in one line at the top, then carry on.
*Why:* most people don't know effort levels exist, so they never raise it for the hard calls (architecture, a tricky bug, "is this the right thing to build?").

---

**Runners-up**, if these fit you:
- **Lead with the decision.** When you need me to decide something, say what I'm deciding in plain words first, then the analysis.
- **Neutral names in config.** Name settings by role (`EMAIL_API_KEY`), not by vendor, so trying a different vendor later isn't a rename across the codebase, and a vendor choice doesn't get made silently.
