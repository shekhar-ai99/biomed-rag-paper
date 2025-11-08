from dataclasses import dataclass
from typing import List, Tuple, Dict
from collections import Counter

from ..utils import det_score


def _bm25_like(query_tokens: List[str], doc_tokens: List[str]) -> float:
    # Simplified overlap score
    q_counts = Counter(query_tokens)
    overlap = sum(min(q_counts[t], doc_tokens.count(t)) for t in q_counts)
    return overlap / (len(doc_tokens) + 1)


def _embed_sim(query: str, doc: str) -> float:
    # Placeholder similarity via deterministic hash-based score
    return det_score(query, doc)


@dataclass
class RetrievedDoc:
    doc_id: int
    text: str
    score: float
    bm25: float
    dense: float


class HybridRetriever:
    def __init__(self, bm25_weight: float = 0.7, dense_weight: float = 0.3):
        self.bm25_weight = bm25_weight
        self.dense_weight = dense_weight
        self._corpus: List[str] = []

    def add_documents(self, docs: List[str]):
        self._corpus.extend(docs)

    def fuse(self, bm25_s: float, dense_s: float) -> float:
        return self.bm25_weight * bm25_s + self.dense_weight * dense_s

    def retrieve(self, query: str, k: int = 5) -> List[RetrievedDoc]:
        q_tokens = query.lower().split()
        scored: List[RetrievedDoc] = []
        for i, doc in enumerate(self._corpus):
            tokens = doc.lower().split()
            bm25_s = _bm25_like(q_tokens, tokens)
            dense_s = _embed_sim(query, doc)
            fused = self.fuse(bm25_s, dense_s)
            scored.append(RetrievedDoc(i, doc, fused, bm25_s, dense_s))
        scored.sort(key=lambda r: r.score, reverse=True)
        return scored[:k]

    def precision_at_k(self, query: str, positives: List[int], k: int = 10) -> float:
        res = self.retrieve(query, k=k)
        if not res:
            return 0.0
        hits = sum(1 for r in res if r.doc_id in positives)
        return hits / min(k, len(res))
