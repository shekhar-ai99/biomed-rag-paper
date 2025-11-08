from biomed_rag.data.preprocess import tokenize, inject_noise, dp_sanitize
from biomed_rag.utils import set_seed


def test_tokenize_basic():
    assert tokenize("Aspirin reduces MI risk.") == ["aspirin", "reduces", "mi", "risk"]


def test_inject_noise_deterministic():
    set_seed(42)
    text = "Aspirin reduces myocardial infarction risk"
    out1 = inject_noise(text, noise_level=0.3)
    set_seed(42)
    out2 = inject_noise(text, noise_level=0.3)
    assert out1 == out2
    assert "<noisy>" in out1


def test_dp_sanitize_applies_privacy():
    text = "Patient presents with Name listed"
    out = dp_sanitize(text, epsilon=1.0)
    assert "Patient" not in out and "Name" not in out
