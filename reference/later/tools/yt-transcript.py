# yt-transcript.py: pull a YouTube video's captions as plain text, no browser.
#
# Kit note: later shelf. The moment for it: the first time you paste a YouTube link and
# want Claude to work with what's said in it. A web fetch of a YouTube page returns an
# empty page shell, not the talk, which is a live case of the absent-source rule
# (reference/rules/absent-source-discipline.md): Claude must not summarize a video it
# never actually read. Put this in ~/.claude/tools/ and add a CLAUDE.md line:
#   "YouTube link and I want its content -> run ~/.claude/tools/yt-transcript.py, read the output file"
#
# usage: python yt-transcript.py <url-or-id> [out.txt]
# needs: pip install youtube-transcript-api
# Prints title | channel | word count | rough token count | minutes, and writes the text to
# out.txt (default: <id>.txt in the current folder). About 250 tokens per minute of talk.
# Most videos only have automatic captions: names and product terms come out mangled
# ("Claude Code" can become "Plot code"), so read accordingly.
import sys, re, json, urllib.request
from youtube_transcript_api import YouTubeTranscriptApi

arg = sys.argv[1]
m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", arg)
vid = m.group(1) if m else arg
out = sys.argv[2] if len(sys.argv) > 2 else f"{vid}.txt"
try:
    meta = json.load(urllib.request.urlopen(f"https://www.youtube.com/oembed?url=https://youtu.be/{vid}&format=json"))
    title, channel = meta["title"], meta["author_name"]
except Exception:
    title, channel = "(title not captured)", "(channel not captured)"
tl = YouTubeTranscriptApi().list(vid)
t = tl.find_transcript(["en", "en-US", "en-GB"])
data = t.fetch()
text = re.sub(r"\s+", " ", " ".join(s.text for s in data)).strip()
open(out, "w", encoding="utf-8").write(f"# {title}\n# {channel} | https://youtu.be/{vid} | captions {'auto' if t.is_generated else 'manual'}\n\n{text}\n")
words = len(text.split())
print(f"{title} | {channel} | {words} words (~{int(words*1.35)} tokens) | {(data[-1].start+data[-1].duration)/60:.0f} min | -> {out}")
