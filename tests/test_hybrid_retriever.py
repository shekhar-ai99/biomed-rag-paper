from biomed_rag.retriever.hybrid_retriever import HybridRetriever


def test_hybrid_retriever_basic():
    retr = HybridRetriever()
    corpus = [
        "Aspirin reduces risk of myocardial infarction",
        "Antibiotics do not treat viral infections",
        "ECG shows ST elevation in acute MI",
        "Vitamin D effects on fracture outcomes remain mixed",
    ]
    retr.add_documents(corpus)
    res = retr.retrieve("ST elevation MI", k=3)
    assert len(res) == 3
    # ensure scores are sorted descending
    scores = [r.score for r in res]
    assert scores == sorted(scores, reverse=True)


def test_precision_at_k():
    retr = HybridRetriever()
    docs = ["alpha beta", "beta gamma", "gamma delta", "epsilon zeta"]
    retr.add_documents(docs)
    prec = retr.precision_at_k("beta", positives=[0,1], k=2)
    assert 0.0 <= prec <= 1.0
