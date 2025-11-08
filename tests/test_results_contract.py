import json
from pathlib import Path


def test_results_contract():
    fp = Path(__file__).resolve().parents[1] / "results.json"
    assert fp.exists(), "results.json missing"
    data = json.loads(fp.read_text())
    assert set(["query", "fact_score", "trust"]).issubset(data.keys())
    assert isinstance(data["query"], str)
    assert 0.0 <= float(data["fact_score"]) <= 1.0
    assert 0.0 <= float(data["trust"]) <= 5.0
