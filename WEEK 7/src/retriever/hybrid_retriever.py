import numpy as np
from sentence_transformers import SentenceTransformer
from vectorstore.faiss_store import FAISSStore
from retriever.bm25_retriever import BM25Retriever
from retriever.reranker import Reranker
import json
from config.settings import CHUNKS_PATH


class HybridRetriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        # Embedding model
        self.model = SentenceTransformer(model_name)

        # FAISS
        self.faiss_store = FAISSStore()
        self.faiss_store.load_index()

        # BM25
        self.bm25 = BM25Retriever()

        self.reranker = Reranker()

        # Load chunks
        with open(f"{CHUNKS_PATH}/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

    
    def retrieve(self, query, top_k=5):
        # ---------------------------
        # 1. FAISS search
        # ---------------------------
        query_embedding = self.model.encode([query])
        distances, indices = self.faiss_store.search(
            np.array(query_embedding), top_k
        )

        faiss_results = [self.chunks[i] for i in indices[0]]

        # ---------------------------
        # 2. BM25 search
        # ---------------------------
        bm25_results = self.bm25.search(query, top_k)

        # ---------------------------
        # 3. Combine results
        # ---------------------------
        combined = faiss_results + bm25_results

        # ---------------------------
        # 4. Deduplicate
        # ---------------------------
        seen = set()
        unique_results = []

        for chunk in combined:
            text = chunk["text"]

            if text not in seen:
                seen.add(text)
                unique_results.append(chunk)

        # ---------------------------
        # 5. RERANK (FIXED 🔥)
        # ---------------------------
        reranked = self.reranker.rerank(query, unique_results, top_k)

        return reranked