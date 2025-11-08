from biomed_rag.trust.trust_scorer import compute_trust_score


def test_trust_score_baseline():
    score = compute_trust_score(exact_match=0.8, rationale_length=5, fact_score=0.9)
    assert 0.0 <= score <= 5.0


def test_trust_score_perfect():
    score = compute_trust_score(exact_match=1.0, rationale_length=10, fact_score=1.0)
    assert score == 5.0


def test_trust_score_zero():
    score = compute_trust_score(exact_match=0.0, rationale_length=0, fact_score=0.0)
    assert score == 0.0


def test_trust_score_custom_weights():
    score = compute_trust_score(
        exact_match=0.5,
        rationale_length=8,
        fact_score=0.7,
        weights={"C": 0.5, "Tr": 0.25, "F": 0.25}
    )
    assert 0.0 <= score <= 5.0
