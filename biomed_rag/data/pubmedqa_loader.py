from typing import List, Dict
from pathlib import Path
import json


def load_pubmedqa(root: str, max_items: int = 100) -> List[Dict]:
    """Load or synthesize PubMedQA-style records.
    If file missing, return synthetic subset.
    """
    path = Path(root) / "data" / "samples" / "pubmedqa.json"
    if not path.exists():
        return [
            {"question": "Does aspirin reduce risk of MI?", "context": "Study shows modest reduction.", "answer": "yes"},
            {"question": "Is vitamin D linked to fractures?", "context": "Mixed RCT outcomes.", "answer": "maybe"},
        ]
    with open(path) as f:
        data = json.load(f)
    return data[:max_items]
