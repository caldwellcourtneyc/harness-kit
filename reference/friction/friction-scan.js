#!/usr/bin/env node
// friction-scan — read the shared friction log and report what recurred.
//
// KIT NOTE (2026-09-12): copied from Courtney's live tool with four changes: the log path
// defaults to FRICTION-LOG.md in the working directory (or $FRICTION_LOG), the last group
// label says "the operator" instead of her name, with no synthesis artifact yet it scans
// the whole log instead of falling back to a date from her history, and it accepts synthesis
// filenames whose end date carries its own year as well as yearless ones. The header below is her
// original reasoning, and the legacy-vocabulary maps are the history of her log's one
// vocabulary change; a fresh log never hits them. Keep the three refusals; they are the design.
//
// WHY THIS EXISTS. The log's own header says it is "read by the weekly friction synthesis",
// and its purpose is to track "how often gates get skipped and where load lands, so we know
// what to harden". As of 2026-08-05 it holds 208 entries and exactly one synthesis artifact
// exists, covering 5/18-6/17 — every entry currently in the file postdates it. The loop did
// not fail; it stalled, because it was a human-triggered ritual with no owner. This is the
// reader half, so the synthesis has an instrument instead of a reading task.
//
// WHAT IT IS NOT. It does not synthesise, conclude, or recommend — those need a declared
// method and a human, because how you bucket 208 entries determines what you conclude. This
// only counts, groups, and says honestly what it cannot resolve.
//
// THREE THINGS IT REFUSES TO GUESS, each learned by reading the log's spec rather than
// assuming it (a throwaway version of this script got all three wrong in an hour):
//
//   1. GRAIN. The log says: "Group names are the grain the weekly synthesis should report its
//      headline at — the useful root cause usually sits at the group level, and the type tells
//      you which fix it needs." So the headline is by GROUP; type is detail.
//   2. THE VOCABULARY MIGRATION. Entries before 2026-07-28 use an older vocabulary and are
//      deliberately left as written ("a bulk retag is a separate reviewable pass, not a silent
//      edit"). The log supplies a map, but most of its rows say "read the entry" — `verification`
//      alone can land on four different current types depending on source and content. So legacy
//      entries are NOT auto-migrated here beyond the handful that are unambiguous; the rest are
//      counted and handed to the synthesis as reading work. Guessing would poison the very
//      analysis this feeds.
//   3. WHOSE FIELDS THESE ARE. `source`, `type` and `evidence` are written by the agent logging
//      its own session. They are self-reported, and the log is explicit that `source` is
//      NOT blame ("friction is system load, not agent-blame"). The output says so, every run,
//      because a count presented bare gets quoted as a measurement.
//
//   node friction-scan.js                 everything since the last synthesis artifact
//   node friction-scan.js --since=YYYY-MM-DD
//   node friction-scan.js --json
//
// Zero dependencies. Read-only: it never writes to the log.

const fs = require("fs");
const path = require("path");

const LOG = process.env.FRICTION_LOG || path.join(process.cwd(), "FRICTION-LOG.md");

// When did the last synthesis cover through? DERIVED, not declared — a hardcoded date here
// would have to be bumped by hand after every synthesis, which is a rule asking someone to
// remember, inside the tool that exists because a rule asking someone to remember failed. Left
// stale it reports the wrong window forever and throws no error: `silently-broken`, which is
// the single largest type in this very log.
//
// So it reads the synthesis artifacts themselves. They are named
// `friction-scan-<start>_to_<end>-<author>.md`, where the end date carries no year — so the
// year is inferred from the start, rolling over when the end month is earlier. Files whose
// end date carries its own year are accepted too. Falls back to
// the log's own beginning if no artifact exists yet, which is the honest answer for "nothing
// has ever been synthesised".
const FALLBACK_SINCE = "0000-00-00"; // i.e. the whole log

function lastSynthesisThrough(dir) {
  let names = [];
  try { names = fs.readdirSync(dir); } catch { return ""; }
  const ends = [];
  for (const n of names) {
    // The end date may carry its own year (an automation wrote it that way) or not (a human did).
    const m = /^friction-scan-(\d{4})-(\d{2})-(\d{2})_to_(?:(\d{4})-)?(\d{2})-(\d{2})/.exec(n);
    if (!m) continue;
    const [, y, sm, , ey, em, ed] = m;
    const year = ey ? Number(ey) : (Number(em) < Number(sm) ? Number(y) + 1 : Number(y));
    ends.push(`${year}-${em}-${ed}`);
  }
  ends.sort();
  return ends.length ? ends[ends.length - 1] : "";
}

// The thirteen current types, in their five groups. Groups are the headline grain.
const GROUPS = {
  "Acting before the gate": ["unapproved", "premature-build", "past-bail"],
  "Not checking": ["unchecked-claim", "self-accepted", "prior-work-missed"],
  "The machine": ["cant-verify", "environment", "cost"],
  "Durable state wrong": ["silently-broken", "collision"],
  "Load landed on the operator": ["manual-load", "illegible"],
};
const GROUP_OF = {};
for (const [g, types] of Object.entries(GROUPS)) for (const t of types) GROUP_OF[t] = g;

// Legacy labels the log's map resolves to exactly ONE current type. Everything else in that
// map is conditional ("read the entry"), so it stays unresolved rather than being guessed.
const LEGACY_CLEAR = {
  blessing: "unapproved",
  "verification-blocked": "cant-verify",
  "judgment-boundary": "past-bail",
  courier: "manual-load",
  sorter: "manual-load",
};

// Every label the log's migration map names, clear or not. A legacy type IN this set is
// known-but-unresolved (reading work for the synthesis); a type in NEITHER list is off-vocabulary
// and worth flagging, because it means something got logged with a label nobody defined.
const LEGACY_KNOWN = new Set([
  ...Object.keys(LEGACY_CLEAR),
  // conditional in the map — "read the entry"
  "gate", "verification", "tool-mismatch", "overproduction", "slow-start",
  "context", "durability",
  // these go to silently-broken except one named 2026-07-27 entry, so still a read
  "doc-mismatch", "trigger-gap", "guardrail-gap", "silent-gap",
  // retired with no successor; that disposition belongs in `proposed fix`, not the type
  "automation-candidate",
  // `setup` is a SOURCE value; two entries used it as a type. A mislabel, not a category.
  "setup",
]);

const arg = (n) => {
  const a = process.argv.find((x) => x.startsWith(`--${n}=`));
  return a ? a.slice(n.length + 3).trim() : "";
};
const derived = lastSynthesisThrough(path.dirname(LOG));
const since = arg("since") || derived || FALLBACK_SINCE;
const sinceWhy = arg("since") ? "--since"
  : derived ? "last synthesis artifact"
  : "no synthesis has ever run";
const asJson = process.argv.includes("--json");

let raw;
try {
  raw = fs.readFileSync(LOG, "utf8");
} catch (e) {
  console.error(`friction-scan: cannot read the log at ${LOG}\n${e.message}`);
  process.exit(2);
}

// Repair the double-encoded separator before parsing. One real entry carries "Â·" — a UTF-8
// middle dot read as Latin-1 and re-encoded on the way in, which Windows PowerShell 5.1
// can do. Without this the line silently does not parse,
// which is how a scan quietly under-reports and nobody ever knows.
const rows = [];
let unparsed = 0;
for (const rawLine of raw.split("\n")) {
  const line = rawLine.replace(/Â(?=·)/g, "").trim();
  if (!/^\d{4}-\d{2}-\d{2}/.test(line)) continue;
  const m = /^(\d{4}-\d{2}-\d{2})\s+·\s+(.*)$/.exec(line);
  if (!m) { unparsed++; continue; }
  const f = m[2].split(" · ").map((s) => s.trim());
  if (f.length < 5) { unparsed++; continue; }
  rows.push({
    date: m[1], surface: f[0], source: f[1], type: f[2], evidence: f[3],
    desc: f[4], author: f[f.length - 1],
  });
}

const win = rows.filter((r) => r.date > since);

// Three buckets: current vocabulary (clean signal), legacy resolvable, legacy needing a read.
const current = [], resolved = [], needsRead = [], offVocab = [];
for (const r of win) {
  if (GROUP_OF[r.type]) current.push(r);
  else if (LEGACY_CLEAR[r.type]) resolved.push({ ...r, mapped: LEGACY_CLEAR[r.type] });
  else if (LEGACY_KNOWN.has(r.type)) needsRead.push(r);
  else offVocab.push(r);
}

const tally = (list, key) => {
  const c = new Map();
  for (const r of list) c.set(r[key], (c.get(r[key]) || 0) + 1);
  return [...c.entries()].sort((a, b) => b[1] - a[1]);
};

const groupTally = () => {
  const c = new Map();
  for (const r of [...current, ...resolved]) {
    const t = r.mapped || r.type;
    const g = GROUP_OF[t];
    if (!c.has(g)) c.set(g, { n: 0, types: new Map() });
    const e = c.get(g);
    e.n++;
    e.types.set(t, (e.types.get(t) || 0) + 1);
  }
  return [...c.entries()].sort((a, b) => b[1].n - a[1].n);
};

if (asJson) {
  console.log(JSON.stringify({
    log: LOG, since, total: rows.length, inWindow: win.length,
    current: current.length, resolved: resolved.length,
    needsRead: needsRead.length, offVocab: offVocab.length, unparsed,
    groups: groupTally().map(([g, e]) => ({ group: g, n: e.n, types: [...e.types] })),
    bySource: tally(win, "source"), bySurface: tally(win, "surface"),
    byLegacy: tally(needsRead, "type"),
  }, null, 2));
  process.exit(0);
}

const pct = (n, d) => (d ? Math.round((100 * n) / d) : 0);
console.log(`FRICTION SCAN — ${win.length} entries since ${since} (log holds ${rows.length})`);
console.log(`Window from: ${sinceWhy}.`);
console.log(`Fields below are SELF-REPORTED by the agent that logged each session, and the log`);
console.log(`is explicit that \`source\` marks where a fix lives, not who is at fault.\n`);

const classified = current.length + resolved.length;
console.log(`HEADLINE — by group, the grain the log says to report at`);
console.log(`  ${classified} of ${win.length} entries carry a current-vocabulary type.\n`);
for (const [g, e] of groupTally()) {
  console.log(`  ${String(e.n).padStart(4)}  ${g}  (${pct(e.n, classified)}%)`);
  for (const [t, n] of [...e.types].sort((a, b) => b[1] - a[1])) {
    console.log(`        ${String(n).padStart(3)}  ${t}`);
  }
}

if (needsRead.length) {
  console.log(`\nNEEDS A READING PASS — ${needsRead.length} entries on the OLD vocabulary`);
  console.log(`  The log supplies a map, but most rows say "read the entry" — \`verification\``);
  console.log(`  alone lands on four different current types depending on source and content.`);
  console.log(`  Not guessed here. This count IS the synthesis's reading workload.`);
  for (const [t, n] of tally(needsRead, "type")) console.log(`  ${String(n).padStart(4)}  ${t}`);
}
if (offVocab.length) {
  console.log(`\nOFF-VOCABULARY — ${offVocab.length} entries whose type is in neither list`);
  for (const [t, n] of tally(offVocab, "type")) console.log(`  ${String(n).padStart(4)}  ${t}`);
}
if (unparsed) console.log(`\n${unparsed} date-leading line(s) did not parse — check the separators.`);

console.log(`\nWHERE THE FIX LIVES (source)`);
for (const [k, n] of tally(win, "source")) console.log(`  ${String(n).padStart(4)}  ${k}  (${pct(n, win.length)}%)`);
console.log(`\nWHICH SURFACE`);
for (const [k, n] of tally(win, "surface").slice(0, 10)) console.log(`  ${String(n).padStart(4)}  ${k}`);
const ev = tally(win, "evidence");
console.log(`\nEVIDENCE  ${ev.map(([k, n]) => `${n} ${k}`).join(" · ")}`);
console.log(`\nThis scan counts. It does not conclude — that needs a declared method and a human.`);
