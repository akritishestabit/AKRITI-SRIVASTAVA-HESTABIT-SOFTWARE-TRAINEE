import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorMemory:
    def __init__(self, model_name='all-MiniLM-L6-v2', vector_dim=384,
                 index_path="memory/faiss.index", meta_path="memory/faiss_meta.npy"):
        self.encoder = SentenceTransformer(model_name)
        self.index_path = index_path
        self.meta_path = meta_path

        os.makedirs("memory", exist_ok=True)

        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            self.metadata = list(np.load(self.meta_path, allow_pickle=True))
        else:
            self.index = faiss.IndexFlatL2(vector_dim)
            self.metadata = []

    def _persist(self):
        faiss.write_index(self.index, self.index_path)
        np.save(self.meta_path, np.array(self.metadata, dtype=object))

    def insert_fact(self, fact: str, extra_meta: dict = None):
        if any(m.get("fact") == fact for m in self.metadata):
            return

        vec = self.encoder.encode([fact], convert_to_numpy=True)
        self.index.add(vec)

        record = {"fact": fact}
        if extra_meta:
            record.update(extra_meta)
        self.metadata.append(record)

        self._persist() 

    def search_similar(self, query: str, k: int = 3):
        if self.index.ntotal == 0:
            return []
        vec = self.encoder.encode([query], convert_to_numpy=True)
        D, I = self.index.search(vec, k)

        results = []
        for idx in I[0]:
            if 0 <= idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results