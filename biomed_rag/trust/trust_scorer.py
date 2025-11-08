from typing import Dict


def compute_trust_score(
    exact_match: float,
    rationale_length: int,
    fact_score: float,
    weights: Dict[str, float] = None
) -> float:
    """
    Compute trust score T as per paper:
    T = w_C * C + w_Tr * Tr + w_F * F
    where C=exact match, Tr=len(R)/10, F=fact_score
    Default weights: {C: 0.4, Tr: 0.3, F: 0.3}
    """
    if weights is None:
        weights = {"C": 0.4, "Tr": 0.3, "F": 0.3}
    
    C = max(0.0, min(1.0, exact_match))
    Tr = min(1.0, rationale_length / 10.0)
    F = max(0.0, min(1.0, fact_score))
    
    T = weights["C"] * C + weights["Tr"] * Tr + weights["F"] * F
    return max(0.0, min(5.0, T * 5.0))  # scale to 1-5
