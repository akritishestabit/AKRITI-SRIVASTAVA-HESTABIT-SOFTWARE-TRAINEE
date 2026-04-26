from rank_bm25 import BM25Okapi
import json
import re
from src.config.settings import CHUNKS_PATH


class BM25Retriever:
    def __init__(self):
       
        with open(f"{CHUNKS_PATH}/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

       
        self.corpus = [self._tokenize(chunk["text"]) for chunk in self.chunks]

        
        self.bm25 = BM25Okapi(self.corpus)

    def _tokenize(self, text):
        
        text = text.lower()
        tokens = re.findall(r'\w+', text)
        return tokens

    def search(self, query, top_k=5):
        query_tokens = self._tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        results = [self.chunks[i] for i in ranked_indices[:top_k]]

        return results