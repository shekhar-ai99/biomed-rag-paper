import json
from pathlib import Path

import pytest

from biomed_rag.utils import set_seed, det_score, privacy_guard, write_json, read_jsonl


def test_det_score_deterministic():
    s1 = det_score("a", "b", "c")
    s2 = det_score("a", "b", "c")
    assert 0.0 <= s1 <= 1.0
    assert s1 == pytest.approx(s2, rel=0, abs=0)


def test_set_seed_stability(tmp_path: Path):
    set_seed(42)
    # Determinism across simple operations
    import random

    vals1 = [random.randint(0, 1000) for _ in range(5)]
    set_seed(42)
    vals2 = [random.randint(0, 1000) for _ in range(5)]
    assert vals1 == vals2


def test_privacy_guard_basic():
    text = "Patient Name: John Doe"
    out = privacy_guard(text, enable=True)
    assert "Patient" not in out
    assert "Name" not in out
    assert "P." in out and "N." in out


def test_json_io_roundtrip(tmp_path: Path):
    fp = tmp_path / "data.jsonl"
    records = [{"a": 1}, {"b": 2}]
    # write as json lines
    fp.write_text("\n".join(json.dumps(r) for r in records))
    # read back
    read_back = list(read_jsonl(str(fp)))
    assert read_back == records

    # write standard json via helper
    outp = tmp_path / "dir" / "obj.json"
    write_json(str(outp), {"x": 1})
    assert outp.exists()
