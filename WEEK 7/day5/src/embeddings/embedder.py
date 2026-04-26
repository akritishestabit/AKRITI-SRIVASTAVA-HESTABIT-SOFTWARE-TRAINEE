from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, chunks):
        """
        chunks: list of dicts (from chunker)
        returns: numpy array of embeddings
        """
        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return np.array(embeddings)