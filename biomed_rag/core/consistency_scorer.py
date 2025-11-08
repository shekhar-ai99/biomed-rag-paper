def rouge_fact(rouge_f: float, nli_score: float) -> float:
    """ROUGE-Fact defined as product of ROUGE-F and mean NLI score."""
    return max(0.0, min(1.0, rouge_f * nli_score))
