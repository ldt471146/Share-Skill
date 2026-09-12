#!/usr/bin/env python3
"""Check skill structure and source evidence; does not judge paraphrase equivalence."""
from pathlib import Path
import argparse, json, re, hashlib, unicodedata, zipfile, html
from html.parser import HTMLParser
import yaml

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]
    def handle_data(self, data): self.parts.append(data)

def normalized(text):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text)).replace("\u00ad", "")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument("--source",type=Path,help="The original EPUB or the verified desktop PDF")
    ap.add_argument("--structure-only",action="store_true",help="Only check structure; no source verification claim")
    ap.add_argument("--corpus",type=Path,help="Optional paragraph JSON produced during the extraction audit")
    args=ap.parse_args();root=args.root.resolve();errors=[]
    entry=(root/"SKILL.md").read_text(encoding="utf-8")
    fm=re.match(r"^---\n(.*?)\n---\n",entry,re.S)
    if not fm: raise SystemExit("Invalid SKILL.md frontmatter")
    meta=yaml.safe_load(fm.group(1));body=entry[fm.end():]
    if meta.get("name")!="how-to-read-a-book":errors.append("Unexpected skill name")
    if len(fm.group(1).splitlines())>25 or len(body.splitlines())>90:errors.append("SBA entry budget exceeded")
    if not meta.get("description"):errors.append("Missing description")
    routes=yaml.safe_load((root/"routing.yaml").read_text(encoding="utf-8"))
    if routes.get("always_read")!=[]:errors.append("Unexpected startup read set")
    route_ids=[r["id"] for r in routes["task_routes"]]
    if len(route_ids)!=len(set(route_ids)):errors.append("Duplicate route ids")
    graph={};paths=list(root.rglob("*.md"))+[root/"routing.yaml"]
    for path in paths:
        rel=path.relative_to(root).as_posix();graph[rel]=set()
        text=path.read_text(encoding="utf-8")
        if re.search(r"\[TODO:|<!-- FILL:",text):errors.append(f"Unfinished content: {rel}")
        for dest in re.findall(r"\[[^\]]*\]\(([^)]+)\)",text):
            dest=dest.split("#",1)[0]
            if not dest or "://" in dest:continue
            target=(path.parent/dest).resolve()
            if not target.is_relative_to(root):errors.append(f"Outside skill link: {rel} -> {dest}");continue
            if not target.exists():errors.append(f"Missing link: {rel} -> {dest}")
            graph[rel].add(target.relative_to(root).as_posix())
    for route in routes["task_routes"]:
        dest=route["workflow"];graph["routing.yaml"].add(dest)
        if not (root/dest).is_file():errors.append(f"Missing workflow {dest}")
    for genre in routes["genres"].values():
        dest=genre["rules"];graph["routing.yaml"].add(dest)
        if not (root/dest).is_file():errors.append(f"Missing genre file {dest}")
    visited=set();pending=["SKILL.md"]
    while pending:
        current=pending.pop()
        if current in visited:continue
        visited.add(current);pending.extend(graph.get(current,[]))
    for path in list((root/"rules").rglob("*.md"))+list((root/"workflows").rglob("*.md")):
        rel=path.relative_to(root).as_posix()
        if rel not in visited:errors.append(f"Unreachable rule/workflow: {rel}")
    records=json.loads((root/"references/evidence.json").read_text(encoding="utf-8"))
    ids=[r["id"] for r in records]
    if len(ids)!=len(set(ids)):errors.append("Duplicate evidence IDs")
    headings={}
    for path in (root/"rules").rglob("*.md"):
        for rid in re.findall(r"^## ([FAGS]\d+) ",path.read_text(encoding="utf-8"),re.M):
            headings.setdefault(rid,[]).append(path.relative_to(root).as_posix())
    for record in records:
        rid=record["id"]
        if headings.get(rid)!=[record["owner"]]:errors.append(f"Rule ownership mismatch: {rid}")
        if not record["evidence"]:errors.append(f"No source evidence: {rid}")
    if set(headings)!=set(ids):errors.append("Rule headings and evidence inventory differ")
    source_meta=json.loads((root/"references/source-metadata.json").read_text(encoding="utf-8"))
    source=args.source
    evidence_status="not run: source unavailable";count=0
    corpus=None
    if args.corpus:
        corpus={p["id"]:p for p in json.loads(args.corpus.read_text(encoding="utf-8"))}
    if source is not None:
        kind=source.suffix.lower().lstrip(".")
        if kind not in ("epub","pdf"):raise SystemExit("Source must be EPUB or PDF")
        actual=hashlib.sha256(source.read_bytes()).hexdigest()
        if actual!=source_meta[kind+"_sha256"]:errors.append("Source SHA-256 differs from reviewed edition")
        cache={}
        if kind=="epub":
            with zipfile.ZipFile(source) as z:
                for rec in records:
                    for ev in rec["evidence"]:
                        name=ev["epub"]
                        if name not in cache:
                            parser=TextParser();parser.feed(z.read(name).decode("utf-8"));cache[name]=normalized("".join(parser.parts))
        else:
            import pymupdf
            doc=pymupdf.open(source)
        for rec in records:
            for ev in rec["evidence"]:
                count+=1;quote=normalized(ev["quote"])
                if kind=="epub":haystack=cache[ev["epub"]]
                else:
                    # A quoted paragraph can cross a page boundary; locator is its first page.
                    start=max(0,ev["pdf_page"]-1)
                    haystack=normalized("".join(doc[i].get_text(clip=pymupdf.Rect(0,0,420,570)) for i in range(start,min(start+4,len(doc)))))
                if not quote or quote not in haystack:errors.append(f"Source quote mismatch: {rec['id']} / {ev['paragraph_id']}")
                if corpus is not None:
                    para=corpus.get(ev["paragraph_id"])
                    if para is None or quote not in normalized(para["text"]):errors.append(f"Paragraph quote mismatch: {rec['id']}")
                    elif hashlib.sha256(para["text"].encode("utf-8")).hexdigest()!=ev["paragraph_sha256"]:errors.append(f"Paragraph digest mismatch: {rec['id']}")
        evidence_status="passed" if not errors else "see errors"
    result={"rule_count":len(records),"quote_count":count,"workflow_count":len(route_ids),"entry_body_lines":len(body.splitlines()),"source_evidence":evidence_status,"source":source.name if source else None,"semantic_equivalence":"requires recorded human/agent review; not proved by this script","errors":errors}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if errors else (2 if source is None and not args.structure_only else 0)

if __name__=="__main__":raise SystemExit(main())
