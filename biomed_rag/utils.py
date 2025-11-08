import hashlib
import json
import os
import random
from dataclasses import dataclass
from typing import Any, Dict

import numpy as np
import yaml


@dataclass
class Config:
    data: Dict[str, Any]

    @staticmethod
    def load(path: str) -> "Config":
        with open(path, "r") as f:
            return Config(yaml.safe_load(f))

    def get(self, key: str, default=None):
        return self.data.get(key, default)


def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except Exception:
        pass


def fair_doi() -> str:
    return "10.5281/zenodo.1234567"


def det_score(*args: str) -> float:
    """Deterministic pseudo-score in [0,1] based on hashing inputs."""
    h = hashlib.sha256("::".join(args).encode()).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF


def privacy_guard(text: str, enable: bool = True) -> str:
    """Very simple placeholder de-identification (for samples only)."""
    if not enable:
        return text
    return text.replace("Patient", "P.").replace("Name", "N.")


def read_jsonl(path: str):
    with open(path, "r") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_json(path: str, obj: Any):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
