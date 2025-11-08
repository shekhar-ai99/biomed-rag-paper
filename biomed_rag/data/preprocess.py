from typing import List
import re
import random

from ..utils import privacy_guard


def tokenize(text: str) -> List[str]:
    text = text.lower()
    return re.findall(r"\w+", text)


def inject_noise(text: str, noise_level: float = 0.1) -> str:
    tokens = tokenize(text)
    n = max(1, int(len(tokens) * noise_level))
    for _ in range(n):
        if tokens:
            idx = random.randrange(len(tokens))
            tokens[idx] = "<noisy>"
    return " ".join(tokens)


def dp_sanitize(text: str, epsilon: float = 1.0) -> str:
    # Placeholder: light de-id + optional perturbation
    t = privacy_guard(text, enable=True)
    if epsilon <= 1.0:
        t = inject_noise(t, noise_level=0.05)
    return t
