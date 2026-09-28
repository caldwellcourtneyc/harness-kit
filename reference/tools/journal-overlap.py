"""Journal restating check: which lines of a journal draft repeat files this session wrote.

Usage:
  python journal-overlap.py <draft.md> [--session <id> | --transcript <path.jsonl>]

With no --session/--transcript it uses the newest transcript under ~/.claude/projects/.
Prints one banner fragment for the /journal Length Gate, then one line per overlapping
draft line. Exit 0 always.

How it decides: the files this session wrote are the file_path of every Write and Edit call in
the transcript (read from disk as they are now; scratch/temp files excluded). A draft line of
8+ words is flagged when at least half of its 4-word phrases also appear in one of those
files. That catches copy-and-trim restating. It does NOT catch paraphrase: a line that says the
same thing in new words passes. Files written only through shell commands are also missed.
Add your journal folder to SKIP so a saved entry never matches itself.

Consumer: the Length Gate in commands/journal.md. Standard library only, Python 3.8+.
"""
import glob, json, os, re, sys

HOME = os.path.expanduser("~")
MIN_WORDS = 8
THRESHOLD = 0.5
N = 4
SKIP = re.compile(r"(AppData/Local/Temp|/tmp/|/scratchpad/|/\.claude/hooks/)", re.I)


def words(s):
    return re.findall(r"[a-z0-9']+", s.lower())


def grams(ws):
    return {tuple(ws[i:i + N]) for i in range(len(ws) - N + 1)}


def find_transcript(args):
    if "--transcript" in args:
        return args[args.index("--transcript") + 1]
    pattern = os.path.join(HOME, ".claude", "projects", "*", "*.jsonl")
    if "--session" in args:
        sid = args[args.index("--session") + 1]
        hits = glob.glob(os.path.join(HOME, ".claude", "projects", "*", sid + ".jsonl"))
        return hits[0] if hits else None
    files = glob.glob(pattern)
    return max(files, key=os.path.getmtime) if files else None


def written_paths(tp):
    paths = []
    with open(tp, encoding="utf-8", errors="replace") as f:
        for line in f:
            if '"tool_use"' not in line:
                continue
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            for block in (rec.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") in ("Write", "Edit"):
                    p = ((block.get("input") or {}).get("file_path") or "").replace("\\", "/")
                    if p and p not in paths and not SKIP.search(p):
                        paths.append(p)
    return paths


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    draft_path, rest = argv[1], argv[2:]
    tp = find_transcript(rest)
    if not tp or not os.path.exists(tp):
        print("[restates: not checked, no transcript found]")
        return
    sources = {}
    for p in written_paths(tp):
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                sources[p] = grams(words(f.read()))
        except OSError:
            pass
    with open(draft_path, encoding="utf-8", errors="replace") as f:
        draft = f.read().split("\n")
    hits = []
    for i, line in enumerate(draft, 1):
        ws = words(line)
        if len(ws) < MIN_WORDS:
            continue
        g = grams(ws)
        best = max(((len(g & sg) / len(g), p) for p, sg in sources.items()), default=(0, None))
        if best[0] >= THRESHOLD:
            hits.append((i, best[0], best[1], line.strip()))
    if not hits:
        print(f"[restates: none | checked against {len(sources)} files this session wrote]")
        return
    refs = ", ".join(f"L{i} -> {os.path.basename(p)}" for i, _, p, _ in hits)
    print(f"[restates: {len(hits)} line{'' if len(hits) == 1 else 's'} ({refs}) | point to the file instead, or say why the line earns its place]")
    for i, score, p, text in hits:
        print(f"  L{i} {int(score * 100)}% of its phrasing is in {p}: {text[:90]}")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(f"[restates: check failed, {type(e).__name__}: {e}]")
