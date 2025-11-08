from typing import List, Dict
from pathlib import Path
import json


def load_fact_pairs(root: str, max_items: int = 200) -> List[Dict]:
    path = Path(root) / "data" / "samples" / "fact_pairs.json"
    if not path.exists():
        # synthetic supportive/refuting pairs
        return [
            {"claim": "Aspirin lowers cardiovascular mortality", "evidence": "Meta-analysis of RCTs shows reduction.", "label": "SUPPORT"},
            {"claim": "Antibiotics cure viral influenza", "evidence": "Trials show no efficacy against viruses.", "label": "REFUTE"},
        ]
    with open(path) as f:
        data = json.load(f)
    return data[:max_items]
