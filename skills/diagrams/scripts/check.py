#!/usr/bin/env python3
"""Check Mermaid diagrams against the house rules.

Usage:
    python3 check.py <file.mmd | file.md> [more files]

A Markdown file is searched for ```mermaid blocks and each block is checked.

Every diagram is checked for:
  - a title in its header, at least three words long
  - the house header (theme: base), so it never ships in Mermaid's default look

A flowchart is also checked for:
  - arrows without a label
  - more than 9 boxes or 12 arrows

Other diagram types get the first two checks only, and the report says so.

Exit code: 0 when nothing was found, 1 when a diagram has findings,
2 when a file could not be read or holds no diagram.

The flowchart reader is a line reader, not a Mermaid parser. It knows arrows
written with --, == or -. and ending in > or nothing (-->, ---, -.->, ==>),
labels in |pipes| or between the two halves of an arrow, and `&` lists.
A line it cannot read is reported, never guessed at.
"""

import re
import sys

MAX_BOXES = 9
MAX_ARROWS = 12

FENCE = re.compile(r"^\s*```+\s*mermaid\s*$")
FENCE_END = re.compile(r"^\s*```+\s*$")
HEADER = re.compile(r"\A\s*---\s*\n(.*?)\n---\s*\n", re.S)
TITLE = re.compile(r"^title:\s*(.+?)\s*$", re.M)
SKIP = re.compile(
    r"^(end\b|direction\b|classDef\b|class\b|style\b|linkStyle\b|click\b|"
    r"accTitle\b|accDescr\b|%%)"
)
SUBGRAPH = re.compile(r"^subgraph\s+([A-Za-z0-9_][\w.-]*)?")
NODE_ID = re.compile(r"^([A-Za-z0-9_][\w.-]*)")
# A link: either two halves with text between them (-- text -->), or one arrow,
# optionally followed by a |pipe label|.
LINK = re.compile(
    r"\s*(?:"
    r"(?:--|==|-\.)\s*(?P<mid>[^\s\-=.>|&][^\->=|]*?)\s*(?:-{2,}>?|={2,}>?|\.+->?)"
    r"|<?(?:-{2,}|={2,}|-\.+-)>?"
    r")\s*(?:\|(?P<pipe>[^|]*)\|)?\s*"
)
MARK = "§"  # stands for "some text was here"


def blocks_in(path, text):
    """Return (label, first_line, source) for each diagram in the file."""
    if not path.lower().endswith((".md", ".markdown")):
        return [("diagram", 1, text)]
    found, current, start = [], None, 0
    for number, line in enumerate(text.splitlines(), 1):
        if current is None:
            if FENCE.match(line):
                current, start = [], number + 1
        elif FENCE_END.match(line):
            found.append(("block %d" % (len(found) + 1), start, "\n".join(current) + "\n"))
            current = None
        else:
            current.append(line)
    return found


def clean(line):
    """Reduce a flowchart line to ids, arrows and label marks."""
    line = re.sub(r'"([^"]*)"', lambda m: MARK if m.group(1).strip() else "", line)
    line = re.sub(r"\|([^|]*)\|", lambda m: "|%s|" % (MARK if m.group(1).strip() else ""), line)
    previous = None
    while previous != line:
        previous = line
        line = re.sub(r"\[[^\[\]]*\]|\([^()]*\)|\{[^{}]*\}", "", line)
    return line.strip()


def ids_in(group):
    """Ids in one side of an arrow: `A`, `A:::kind`, `A & B`."""
    ids = []
    for part in group.split("&"):
        match = NODE_ID.match(part.strip())
        if not match:
            return None
        ids.append(match.group(1))
    return ids


def check_flowchart(lines, first_line):
    boxes, groups, arrows, unlabeled, unread = set(), set(), 0, [], []
    for offset, raw in enumerate(lines):
        number = first_line + offset
        line = raw.strip()
        if not line or SKIP.match(line):
            continue
        sub = SUBGRAPH.match(line)
        if sub:
            if sub.group(1):
                groups.add(sub.group(1))
            continue
        line = clean(line.rstrip(";"))
        if not line:
            continue
        links = [m for m in LINK.finditer(line) if m.group(0).strip()]
        if not links:
            ids = ids_in(line)
            if ids is None:
                unread.append(number)
            else:
                boxes.update(ids)
            continue
        sides, position = [], 0
        for link in links:
            sides.append(line[position:link.start()])
            position = link.end()
        sides.append(line[position:])
        side_ids = [ids_in(side) for side in sides]
        if any(ids is None for ids in side_ids):
            unread.append(number)
            continue
        for ids in side_ids:
            boxes.update(ids)
        for index, link in enumerate(links):
            count = len(side_ids[index]) * len(side_ids[index + 1])
            arrows += count
            labelled = bool((link.group("mid") or "").strip()) or MARK in (link.group("pipe") or "")
            if not labelled:
                unlabeled.append(number)
    boxes -= groups
    return len(boxes), arrows, unlabeled, unread


def check(label, first_line, source):
    findings, notes = [], []
    header = HEADER.match(source)
    body = source[header.end():] if header else source
    body_line = first_line + (source[:header.end()].count("\n") if header else 0)
    title = TITLE.search(header.group(1)) if header else None
    title_text = title.group(1).strip().strip("\"'") if title else ""
    if not title_text:
        findings.append("no title in the header")
    elif len(title_text.split()) < 3 or "<" in title_text:
        findings.append("the title names a topic or is still the placeholder: state the finding in a sentence")
    if not header or not re.search(r"^\s*theme:\s*base\s*$", header.group(1), re.M):
        findings.append("no house header (theme: base): it would draw in Mermaid's default look")

    lines = body.splitlines()
    kind = next((l.strip().split()[0] for l in lines if l.strip() and not l.strip().startswith("%%")), "")
    if kind in ("flowchart", "graph"):
        start = next(i for i, l in enumerate(lines) if l.strip() and not l.strip().startswith("%%"))
        boxes, arrows, unlabeled, unread = check_flowchart(lines[start + 1:], body_line + start + 1)
        notes.append("%d boxes, %d arrows" % (boxes, arrows))
        for number in unlabeled:
            findings.append("line %d: an arrow has no label" % number)
        if boxes > MAX_BOXES:
            findings.append("%d boxes, more than %d: split into an overview and details" % (boxes, MAX_BOXES))
        if arrows > MAX_ARROWS:
            findings.append("%d arrows, more than %d: split into an overview and details" % (arrows, MAX_ARROWS))
        for number in unread:
            findings.append("line %d: could not be read, so it was not counted" % number)
    elif kind:
        notes.append("type %s: only the title and the header are checked" % kind)
    else:
        findings.append("empty diagram")
    return findings, notes


def main(paths):
    if not paths:
        sys.stderr.write(__doc__)
        return 2
    worst = 0
    for path in paths:
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except OSError as error:
            print("%s: cannot read (%s)" % (path, error.strerror))
            worst = max(worst, 2)
            continue
        blocks = blocks_in(path, text)
        if not blocks:
            print("%s: no mermaid block found" % path)
            worst = max(worst, 2)
            continue
        for label, first_line, source in blocks:
            findings, notes = check(label, first_line, source)
            status = "ok" if not findings else "%d to fix" % len(findings)
            print("%s, %s (line %d): %s%s" % (path, label, first_line, status, "; " + "; ".join(notes) if notes else ""))
            for finding in findings:
                print("  - " + finding)
            if findings:
                worst = max(worst, 1)
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
