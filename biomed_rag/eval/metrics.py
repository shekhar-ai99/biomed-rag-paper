from typing import List, Dict, Any
import statistics


def pearson_r(x: List[float], y: List[float]) -> float:
    """Simplified Pearson correlation coefficient."""
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denom_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    if denom_x == 0 or denom_y == 0:
        return 0.0
    
    return numerator / (denom_x * denom_y) ** 0.5


def auc_roc_mock(predictions: List[float], labels: List[int]) -> float:
    """Mock AUC-ROC for testing (not a real implementation)."""
    if not predictions or not labels:
        return 0.5
    # Placeholder: return deterministic value based on accuracy
    correct = sum(1 for p, l in zip(predictions, labels) if (p > 0.5) == l)
    return correct / len(labels)


def aggregate_results(runs: List[Dict[str, Any]]) -> Dict[str, float]:
    """Aggregate metrics across multiple runs."""
    if not runs:
        return {}
    
    metrics = {}
    for key in runs[0].keys():
        values = [r[key] for r in runs if key in r and isinstance(r[key], (int, float))]
        if values:
            metrics[f"{key}_mean"] = statistics.mean(values)
            metrics[f"{key}_std"] = statistics.stdev(values) if len(values) > 1 else 0.0
    
    return metrics
