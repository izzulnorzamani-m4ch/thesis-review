#!/usr/bin/env python3
"""List comments/annotations embedded in a PDF or Word file.

Examiners often leave feedback as sticky notes, highlights with notes, or
Word comments rather than (or as well as) a typed list. This pulls them out.

Usage:
    python extract_comments.py <file.pdf|file.docx> [--out comments.md]

Output (markdown): one numbered entry per comment with author, location
(page for PDF; nearby text for Word) and the comment text.
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_comments(path: Path):
    out = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if "word/comments.xml" not in names:
            return out
        croot = ET.fromstring(z.read("word/comments.xml"))
        comments = {}
        for c in croot.iter(f"{W}comment"):
            cid = c.get(f"{W}id")
            text = "\n".join("".join(t.text or "" for t in p.iter(f"{W}t"))
                             for p in c.iter(f"{W}p")).strip()
            comments[cid] = {"author": c.get(f"{W}author", "?"),
                             "date": (c.get(f"{W}date") or "")[:10],
                             "text": text, "anchor": ""}
        # find the text each comment is anchored to
        doc = ET.fromstring(z.read("word/document.xml"))
        open_ids, buf = set(), {}
        for el in doc.iter():
            if el.tag == f"{W}commentRangeStart":
                open_ids.add(el.get(f"{W}id"))
                buf[el.get(f"{W}id")] = []
            elif el.tag == f"{W}commentRangeEnd":
                cid = el.get(f"{W}id")
                open_ids.discard(cid)
                if cid in comments:
                    comments[cid]["anchor"] = "".join(buf.get(cid, []))
            elif el.tag == f"{W}t" and open_ids:
                for cid in open_ids:
                    buf[cid].append(el.text or "")
        for cid, c in comments.items():
            out.append({"author": c["author"], "where": c["date"],
                        "anchor": c["anchor"], "text": c["text"]})
    return out


def pdf_comments(path: Path):
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("pypdf is needed for PDF annotations: pip install pypdf")
    out = []
    reader = PdfReader(str(path))
    skip = {"/Link", "/Widget", "/Popup"}
    for i, page in enumerate(reader.pages, start=1):
        for a in page.get("/Annots") or []:
            a = a.get_object()
            sub = a.get("/Subtype")
            if sub in skip:
                continue
            text = (a.get("/Contents") or "").strip()
            if not text and sub not in ("/Highlight", "/StrikeOut", "/Underline"):
                continue
            out.append({"author": str(a.get("/T") or "?"),
                        "where": f"p. {i} ({str(sub).lstrip('/')})",
                        "anchor": "", "text": text or "(markup with no note)"})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--out")
    a = ap.parse_args()
    p = Path(a.file)
    ext = p.suffix.lower()
    if ext == ".docx":
        items = docx_comments(p)
    elif ext == ".pdf":
        items = pdf_comments(p)
    else:
        sys.exit("Supports .pdf and .docx only")

    lines = [f"# Embedded comments in {p.name}", "", f"Found: {len(items)}", ""]
    if not items:
        lines.append("No embedded comments or annotations found. "
                     "(Comments typed into the body text won't show here — read the text too.)")
    for n, it in enumerate(items, start=1):
        anchor = re.sub(r"\s+", " ", it["anchor"]).strip()
        anchor = f' — on: "{anchor[:150]}{"…" if len(anchor) > 150 else ""}"' if anchor else ""
        lines.append(f"{n}. **{it['author']}** {it['where']}{anchor}")
        lines.append(f"   {it['text']}")
    md = "\n".join(lines)
    if a.out:
        Path(a.out).write_text(md)
    print(md)


if __name__ == "__main__":
    main()
