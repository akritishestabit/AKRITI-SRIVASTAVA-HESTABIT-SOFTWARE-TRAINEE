import numpy as np
from sentence_transformers import SentenceTransformer
from src.vectorstore.faiss_store import FAISSStore
from src.retriever.bm25_retriever import BM25Retriever
from src.retriever.reranker import Reranker
import json
from src.config.settings import CHUNKS_PATH


class HybridRetriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

        self.faiss_store = FAISSStore()
        self.faiss_store.load_index()

        self.bm25 = BM25Retriever()
        self.reranker = Reranker()

        with open(f"{CHUNKS_PATH}/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

    
    def mmr(self, query_embedding, chunk_embeddings, chunks, top_k=5, lambda_param=0.7):
        selected = []
        selected_indices = []

        similarities = np.dot(chunk_embeddings, query_embedding)

        while len(selected) < min(top_k, len(chunks)):
            mmr_scores = []

            for i in range(len(chunks)):
                if i in selected_indices:
                    continue

                relevance = similarities[i]

                diversity = 0
                if selected_indices:
                    diversity = max(
                        np.dot(chunk_embeddings[i], chunk_embeddings[j])
                        for j in selected_indices
                    )

                score = lambda_param * relevance - (1 - lambda_param) * diversity
                mmr_scores.append((score, i))

            _, best_idx = max(mmr_scores)
            selected.append(chunks[best_idx])
            selected_indices.append(best_idx)

        return selected

    def retrieve(self, query, top_k=5):
        query_embedding = self.model.encode([query])

        distances, indices = self.faiss_store.search(
            np.array(query_embedding), top_k
        )
        faiss_results = [self.chunks[i] for i in indices[0]]

        bm25_results = self.bm25.search(query, top_k)

        combined = faiss_results + bm25_results

        
        seen = set()
        unique_results = []

        for chunk in combined:
            text = chunk["text"]
            if text not in seen:
                seen.add(text)
                unique_results.append(chunk)

        
        texts = [chunk["text"] for chunk in unique_results]
        chunk_embeddings = self.model.encode(texts)

        query_emb = query_embedding[0]  

        mmr_results = self.mmr(query_emb, chunk_embeddings, unique_results, top_k)

        
        reranked = self.reranker.rerank(query, mmr_results, top_k)

        return reranked