import pytest
from biomed_rag.core.consistency_scorer import rouge_fact


def test_rouge_fact_bounds():
    assert rouge_fact(0.8, 0.9) == pytest.approx(0.72, abs=1e-9)
    assert rouge_fact(1.2, 0.9) == 1.0
    assert rouge_fact(-0.1, 0.5) == 0.0
