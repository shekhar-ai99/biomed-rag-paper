from typing import List, Dict
from pathlib import Path
import json

SPECIALTIES = ["cardiology", "neurology", "infectious", "oncology"]


def load_medqa(root: str, max_items: int = 50) -> List[Dict]:
    path = Path(root) / "data" / "samples" / "medqa.json"
    if not path.exists():
        # synthetic examples
        return [
            {"question": "A 60-year-old with exertional angina: next test?", "options": ["ECG", "Stress echo", "MRI", "Biopsy"], "answer": 1, "specialty": "cardiology"},
            {"question": "Young patient new seizure: first-line imaging?", "options": ["CT", "MRI", "PET", "X-ray"], "answer": 1, "specialty": "neurology"},
        ]
    with open(path) as f:
        data = json.load(f)
    return data[:max_items]
