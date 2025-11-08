import pytest
from biomed_rag.eval.metrics import pearson_r, auc_roc_mock, aggregate_results


def test_pearson_r_perfect():
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [2.0, 4.0, 6.0, 8.0, 10.0]
    assert pearson_r(x, y) == pytest.approx(1.0, abs=0.01)


def test_pearson_r_zero():
    x = [1.0, 1.0, 1.0]
    y = [2.0, 3.0, 4.0]
    assert pearson_r(x, y) == 0.0


def test_auc_roc_mock_perfect():
    preds = [0.9, 0.8, 0.1, 0.2]
    labels = [1, 1, 0, 0]
    auc = auc_roc_mock(preds, labels)
    assert auc == 1.0


def test_aggregate_results():
    runs = [
        {"acc": 0.9, "f1": 0.85},
        {"acc": 0.92, "f1": 0.88},
        {"acc": 0.88, "f1": 0.84},
    ]
    agg = aggregate_results(runs)
    assert "acc_mean" in agg
    assert "f1_mean" in agg
    assert agg["acc_mean"] == pytest.approx(0.9, abs=0.01)
