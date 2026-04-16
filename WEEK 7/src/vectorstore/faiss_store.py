import faiss
import numpy as np
import os
from src.config.settings import FAISS_INDEX_PATH

class FAISSStore:
    def __init__(self):
        self.index = None

    def create_index(self, embeddings):
        """
        embeddings: numpy array
        """
        dimension = embeddings.shape[1]

        
        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        return self.index

    def save_index(self):
        if self.index is not None:
            faiss.write_index(self.index, FAISS_INDEX_PATH)

    def load_index(self):
        if os.path.exists(FAISS_INDEX_PATH):
            self.index = faiss.read_index(FAISS_INDEX_PATH)
        else:
            raise ValueError("FAISS index not found!")

    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices