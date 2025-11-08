from pathlib import Path

from biomed_rag.data.mimic_loader import load_mimic_samples
from biomed_rag.data.pubmedqa_loader import load_pubmedqa
from biomed_rag.data.medqa_loader import load_medqa
from biomed_rag.data.factcc_scifact import load_fact_pairs


def test_mimic_synthetic_load():
    data = load_mimic_samples(str(Path(__file__).resolve().parents[1]))
    assert isinstance(data, list)


def test_pubmedqa_synthetic_load():
    data = load_pubmedqa(str(Path(__file__).resolve().parents[1]))
    assert len(data) >= 2
    assert {"question", "context", "answer"}.issubset(data[0].keys())


def test_medqa_synthetic_load():
    data = load_medqa(str(Path(__file__).resolve().parents[1]))
    assert len(data) >= 2
    assert "question" in data[0]


def test_fact_pairs_synthetic_load():
    data = load_fact_pairs(str(Path(__file__).resolve().parents[1]))
    assert len(data) >= 2
    assert {"claim", "evidence", "label"}.issubset(data[0].keys())
