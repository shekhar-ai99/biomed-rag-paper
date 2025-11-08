from typing import List, Dict, Any
from pathlib import Path

from ..utils import read_jsonl, privacy_guard


def load_mimic_samples(root: str) -> List[Dict[str, Any]]:
    """Load sample de-identified EHRs (JSONL) with minimal FHIR-like fields."""
    fp = Path(root) / "data" / "samples" / "mimic_samples.jsonl"
    if not fp.exists():
        return []
    out = []
    for rec in read_jsonl(str(fp)):
        note = privacy_guard(rec.get("note", ""), enable=True)
        out.append({
            "patient_id": rec.get("patient_id", "P0"),
            "note": note,
            "fhir": rec.get("fhir", {}),
        })
    return out
