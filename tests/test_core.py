import json,unittest,tempfile
from pathlib import Path
from src.qc import inspect
class TestQC(unittest.TestCase):
 def test_invalid_box_is_reported(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d); (root/"a.bin").write_bytes(b"demo"); m=root/"rows.jsonl"; m.write_text(json.dumps({"image":"a.bin","boxes":[{"bbox":[.8,.2,.2,.7]}]})+"\n",encoding="utf-8"); r=inspect(root,m); self.assertEqual(r["records"],1); self.assertTrue(r["invalid_annotations"])
