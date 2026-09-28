# Retrieval: why notes don't surface on their own

The most common gap people notice once they use Claude daily: it doesn't bring in context from past discussions. You decided something last week, and this week it proposes the thing you already ruled out. The fix is not writing more down. Most people who notice this already keep notes or a journal. The difference is everything downstream of the notes.

## Storage without retrieval is a diary

A journal entry, once written, does nothing. Claude starts every session seeing only what's loaded into context. Files sitting in a folder, however good, are invisible unless one of three things happens:

1. **They're always loaded** (like CLAUDE.md). Viable only for small, stable content.
2. **An index of them is always loaded,** so Claude starts each session knowing *what exists* and can fetch the full item when relevant.
3. **A standing instruction tells Claude when to search,** and a search mechanism exists to obey it with.

The "it remembers everything" effect is the stack of all three. The first copy of this setup handed to someone else didn't include the stack, only the journal, and the journal on its own did nothing. Concretely, the source harness's retrieval machinery is:

- **`MEMORY.md`,** a one-line-per-fact index, auto-loaded every session. Claude reads a few dozen lines and knows what it can look up. Cost: negligible. Effect: the difference between "knows nothing" and "knows what it knows." Claude Code's built-in auto memory already provides this slot per project; the harness's job is to put the right facts in it and point at them.
- **Pointer lines in CLAUDE.md:** "when X, read Y." Retrieval triggers written into the always-loaded layer.
- **A journal search tool** (on Courtney's machine, an MCP server) that lets Claude search the journal by content mid-session, the moment something seems relevant. Claude Code doesn't include one.
- **A reindex hook:** every time a journal file is written, an index rebuild fires mechanically. The index can't rot, because keeping it current isn't anyone's job.

Notice what's *not* on the list: any act of will. Nobody tells Claude to check the journal; the harness does. That's the design principle: **retrieval that depends on someone remembering to retrieve will stop happening.**

## The minimum viable version

The full stack is not day-one work. The order that pays fastest:

1. **Memory first** (an afternoon): make sure auto memory is on, seed `MEMORY.md` with a few real facts in the index format, and add a CLAUDE.md line saying the index is authoritative and when to open the full files. This alone produces the "it remembered!" effect, because it covers the highest-value facts at near-zero cost.
2. **Journal pointers second:** a CLAUDE.md instruction for when to go look at the journal (picking up a project after absence; anything that sounds like it happened before), plus the journal organized so looking is cheap (dated files, predictable location).
3. **Search third, when the journal outgrows browsing:** an MCP server, or the simpler stand-in that works on day one, Claude grepping the journal folder. That needs nothing installed and covers a small journal fine. CATALOG.md's infrastructure section has both options.
4. **The deposit habit, alongside all three:** a close-out routine (`/land`) so every session actually writes to the stores the next session reads. Retrieval with nothing new going in is a museum.

## How to know it's working

The only honest test: **open a fresh session and ask something whose answer lives only in the record.** If it surfaces, the loop is closed. Run the same test again a month later. Retrieval machinery fails silently (an index that stopped updating looks exactly like an index that's current), so the check is periodic, not one-time.
