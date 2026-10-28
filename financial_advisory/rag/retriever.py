"""
TF-IDF retriever.

This is real retrieval: documents are vectorized with TF-IDF, the
query is vectorized the same way, and the top-k most similar chunks
are returned by cosine similarity. It's a classical (non-neural) IR
method - no embeddings model, no vector database - but the retrieval
step is genuine, unlike a plain dict lookup.

Swap-in path to match your main project's stack: replace
TfidfVectorizer with your existing embedding service
(app/services/retrieval/embedding.py) and cosine_similarity search
with a Qdrant collection query. The retrieve() function signature
below would stay the same, so nothing downstream needs to change.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from financial_advisory.rag.documents import DOCUMENTS

_texts = [doc["text"] for doc in DOCUMENTS]

_vectorizer = TfidfVectorizer(stop_words="english")
_doc_matrix = _vectorizer.fit_transform(_texts)


def retrieve(query: str, top_k: int = 3, scheme_filter: str | None = None) -> list[dict]:
    """
    Returns the top_k most relevant document chunks for the query.

    If scheme_filter is given (e.g. "KCC"), only chunks belonging to
    that scheme are considered - this mirrors filtering by payload
    metadata in a real vector DB query.
    """
    candidates = DOCUMENTS
    candidate_matrix = _doc_matrix

    if scheme_filter:
        indices = [i for i, doc in enumerate(DOCUMENTS) if doc["scheme"] == scheme_filter]
        candidates = [DOCUMENTS[i] for i in indices]
        candidate_matrix = _doc_matrix[indices]

    query_vec = _vectorizer.transform([query])
    scores = cosine_similarity(query_vec, candidate_matrix)[0]

    ranked = sorted(zip(candidates, scores), key=lambda pair: pair[1], reverse=True)
    top = ranked[:top_k]

    return [{"id": doc["id"], "scheme": doc["scheme"], "text": doc["text"], "score": float(score)} for doc, score in top]
