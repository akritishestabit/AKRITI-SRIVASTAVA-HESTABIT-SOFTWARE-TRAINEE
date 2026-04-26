import json
import numpy as np
from sentence_transformers import SentenceTransformer
from src.vectorstore.faiss_store import FAISSStore
from src.config.settings import CHUNKS_PATH

class QueryEngine:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

       
        self.store = FAISSStore()
        self.store.load_index()

        
        with open(f"{CHUNKS_PATH}/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

    def query(self, question, top_k=3):
      
        query_embedding = self.model.encode([question])

       
        distances, indices = self.store.search(
            np.array(query_embedding), top_k
        )

        results = []
        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results

if __name__ == "__main__":
    engine = QueryEngine()

    while True:
        question = input("\nEnter your question (or 'exit'): ")

        if question.lower() == "exit":
            break

        results = engine.query(question)

        print("\nTop Results:\n")
        for i, r in enumerate(results):
            print(f"Result {i+1}:")
            print(f"Text: {r['text']}")
            print(f"Source: {r['source']}")
            print(f"Page: {r['page']}")
            print("-" * 50)    
        