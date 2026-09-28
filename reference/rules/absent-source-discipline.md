# Absent sources: never fill the gap

> **Kit note (not part of the rule):** this is a lightly-trimmed teaching copy of a live
> always-on rule from Courtney's harness. Her original carries *three* real incidents and
> links into her memory system; this keeps *one*, generalized, because the rule is what
> transfers, not the incident count. That trimming is itself the lesson — a rule earns its
> authority from *an* incident, and one is plenty. See `reference/README.md`.

**Guaranteed trigger — mechanical, not a judgment call: a retrieval failed and the work
continued anyway.** A 403, a 404, an empty body, a timeout, a redirect to an index page, a
fetch that comes back "no content was provided." That is the moment this rule certainly
fires. It is deliberately NOT "when you might be inventing something," because that state is
invisible from the inside — every instance below felt like ordinary diligence while it was
happening.

**Rule 4 is always on, independent of that trigger** (see "Known limit" below). The failed
retrieval is the one moment you cannot miss; rule 4 is the check that catches the rest.

## The five rules

1. **A failed retrieval is a fact about what you know, and it must reach the output.** Every
   claim that depended on the missing source is unverified, and says so **at the point of
   use** — inline, in the row or sentence that carries it. Not in a caveat paragraph
   elsewhere, which is how a limit gets stated and then silently dropped by whatever reads
   the table.

2. **Search-result snippets are pointers, never content.** A snippet proves a page was
   indexed once. It does not prove the page exists now, and it is not the page. Never write
   a description, quotation, price, range, date, requirement, or status as though the source
   was read when only a snippet was seen. If the snippet is all there is, the output says
   "per a search snippet, unverified against the source."

3. **Never synthesize an identifier.** URLs, job/req IDs, ticket numbers, DOIs, citations,
   file paths, line numbers, commit hashes, version strings, API endpoints, phone numbers,
   email addresses. If a field or table column wants one and you do not have it, the field
   reads ***(not captured)***. **Absence is a legal value; a plausible identifier is not** —
   because a well-formed fake gets clicked, cited, or emailed, and it fails at the worst
   possible moment, in front of someone else.

4. **The check, one question: which tool call returned this?** Before asserting any specific
   fact — a number, a name, a status, a quoted phrase — you should be able to point at the
   call in this session that produced it. If you cannot, you did not observe it, and rules
   1-3 apply.

5. **Liveness is only ever observed, never inferred.** "Currently open," "still available,"
   "in stock," "up to date," "still employed there," "the latest version" — these can come
   only from the thing itself, or from an explicit removal/updated stamp on it. A cached
   aggregator copy, a snippet, or the absence of contrary evidence is not liveness evidence.
   Where liveness is the deliverable, a source that will not render is a **negative** result,
   not a missing one.

## The incident that produced this (one is enough)

Five results were reported from a research scan. **The one source that actually rendered was
the only one that existed.**

| Result | Source retrieved? | Reality when clicked |
|---|---|---|
| A | No — 404 | Page does not exist |
| B | No — empty body | Page does not exist |
| C | No — 403 | Expired |
| D | No — 403 | No longer available |
| E | **Yes** | Real |

Four full write-ups — summaries, scores, fit notes — were composed from search snippets for
pages never opened. The dead result D was escalated to "the one to act on first," which would
have sent the user off to email someone about something that was already gone.

**Why one incident is enough:** in every slot, something needed filling, the authoritative
source was unavailable, a weaker source (or none) was at hand, and the slot got filled at
full confidence with no mark of provenance. The pressure is structural — tables want cells,
reports want findings, a scan that returns nothing feels like a failed scan. It is not a
knowledge problem and cannot be fixed by trying harder to be accurate; it needs a rule that
fires on the mechanical trigger.

## Known limit of this rule: the trigger is narrow on purpose

The trigger is *a retrieval failed*, because that is mechanically observable and therefore
fires reliably. The cost is that it does **not** catch the sibling failure where nothing was
ever fetched at all — an asserted count, a remembered version number, a "this has grown from
5 to 8" written from impression rather than from a read.

**Rule 4 is the part that generalises** — *which tool call returned this?* — and it applies to
every specific assertion, not only to ones downstream of a failed fetch. When the answer is
"none," the claim is an impression. Say so, or go count it. Counting is nearly always cheaper
than the correction.

## Label it inline, or exclude it? — the deciding question

Rule 1 says mark the unverified claim at the point of use. The corollary below says an item
that cannot clear the bar never enters the output. Both are right, for different work, and
the deciding question is: **is liveness or existence part of what is being delivered?**

- **Yes — exclude it.** A listings scan, a link check, an availability sweep, an inventory.
  Here "I could not open it" and "it is not there" are close enough to act on identically, so
  an unverifiable item goes to the reject log, not the report. Reporting it with a caveat
  still sends the reader off to act.
- **No — label it inline and keep it.** Background, history, context, a definition, anything
  where the fact is useful even if the source moved. Here dropping it loses real information,
  so it stays, marked at the point of use per rule 1.

When unsure which case you are in, exclude and say what you excluded and why. That is
recoverable in one question; the other direction sends the reader off to act on a thing that
is not there.

## Corollary for anything that reports findings

A scan, review, audit, or research pass must be able to return **empty**, and empty must be
reported as a clean result rather than padded. Where a deliverable has a per-item bar
("verify it looks currently open," "confirm the file exists"), that bar is a **gate on
entry**, not a caveat on exit: an item that cannot clear it does not enter the output at all,
it goes to the reject log with the reason. Zero findings is information. Four unverifiable
findings dressed as four verified ones is worse than zero, because it ends the search and
sends the reader off to act.
