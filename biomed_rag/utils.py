import hashlib
import json
import os
import random
from dataclasses import dataclass
from typing import Any, Dict

# Optional heavy deps (numpy, yaml) are guarded to keep tests lightweight.
try:  # pragma: no cover
    import numpy as np  # type: ignore
except Exception:  # pragma: no cover
    np = None  # type: ignore

yaml = None  # loaded lazily


@dataclass
class Config:
    data: Dict[str, Any]

    @staticmethod
    def load(path: str) -> "Config":
        global yaml
        if yaml is None:
            try:  # pragma: no cover
                import yaml as _yaml  # type: ignore
                yaml = _yaml
            except Exception as e:  # pragma: no cover
                raise ImportError("pyyaml required; install with `pip install pyyaml`.") from e
        with open(path, "r") as f:
            return Config(yaml.safe_load(f))

    def get(self, key: str, default=None):
        return self.data.get(key, default)


def set_seed(seed: int = 42):
    random.seed(seed)
    if np is not None:
        try:
            np.random.seed(seed)
        except Exception:
            pass
    try:
        import torch  # type: ignore
        torch.manual_seed(seed)
        if hasattr(torch, "cuda"):
            torch.cuda.manual_seed_all(seed)  # pragma: no cover
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
