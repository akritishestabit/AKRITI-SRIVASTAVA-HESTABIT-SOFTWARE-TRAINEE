from sentence_transformers import SentenceTransformer
import numpy as np


class Reranker:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def rerank(self, query, chunks, top_k=5):
        
        query_embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

       
        texts = [chunk["text"] for chunk in chunks]

        chunk_embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

       
        query_norm = query_embedding / np.linalg.norm(query_embedding)
        chunk_norms = chunk_embeddings / np.linalg.norm(chunk_embeddings, axis=1, keepdims=True)

        
        scores = np.dot(chunk_norms, query_norm)

        
        ranked_indices = np.argsort(scores)[::-1]

        
        return [chunks[i] for i in ranked_indices[:top_k]]