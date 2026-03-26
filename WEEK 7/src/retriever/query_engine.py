import json
import numpy as np
from sentence_transformers import SentenceTransformer
from vectorstore.faiss_store import FAISSStore
from config.settings import CHUNKS_PATH

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
    
   