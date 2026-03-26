from sentence_transformers import SentenceTransformer
import numpy as np


class Reranker:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def rerank(self, query, chunks, top_k=5):
        # Encode query
        query_embedding = self.model.encode([query])[0]

        scored_chunks = []

        for chunk in chunks:
            chunk_embedding = self.model.encode([chunk["text"]])[0]

            # cosine similarity
            score = np.dot(query_embedding, chunk_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(chunk_embedding)
            )

            scored_chunks.append((score, chunk))

        # sort by score (descending)
        scored_chunks.sort(key=lambda x: x[0], reverse=True)

        # return only chunks
        return [chunk for score, chunk in scored_chunks[:top_k]]