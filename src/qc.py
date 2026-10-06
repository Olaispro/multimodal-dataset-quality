"""Dataset integrity checks. Does not infer semantic correctness."""
import argparse, hashlib, json
from pathlib import Path

def inspect(root, manifest):
    root=Path(root); files=sorted(p for p in root.rglob("*") if p.is_file()); hashes={}; duplicates=[]
    for p in files:
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if digest in hashes: duplicates.append({"file":str(p),"duplicate_of":hashes[digest]})
        else: hashes[digest]=str(p)
    records=[]; missing=[]; invalid=[]
    for line_no,line in enumerate(Path(manifest).read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: row=json.loads(line)
        except json.JSONDecodeError as e: invalid.append({"line":line_no,"reason":str(e)}); continue
        image=root/row.get("image","")
        if not image.is_file(): missing.append({"line":line_no,"image":row.get("image")}); continue
        boxes=row.get("boxes",[])
        for i,b in enumerate(boxes):
            try: x1,y1,x2,y2=map(float,b["bbox"])
            except Exception: invalid.append({"line":line_no,"box":i,"reason":"bbox must be [x1,y1,x2,y2]"}); continue
            if not (0<=x1<x2<=1 and 0<=y1<y2<=1): invalid.append({"line":line_no,"box":i,"reason":"normalized box outside [0,1] or zero-area"})
        records.append(row)
    return {"files_scanned":len(files),"records":len(records),"exact_duplicates":duplicates,"missing_images":missing,"invalid_annotations":invalid,
        "scope":"Integrity checks only; labels and semantic correctness require human review."}

def main():
    p=argparse.ArgumentParser();p.add_argument("images",type=Path);p.add_argument("manifest",type=Path);p.add_argument("--out",type=Path,default=Path("qc-report.json"));a=p.parse_args()
    report=inspect(a.images,a.manifest);a.out.write_text(json.dumps(report,indent=2),encoding="utf-8");print(json.dumps(report,indent=2))
if __name__=="__main__":main()
