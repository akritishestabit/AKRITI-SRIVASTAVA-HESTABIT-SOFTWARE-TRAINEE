from rank_bm25 import BM25Okapi
import json
import re
from config.settings import CHUNKS_PATH


class BM25Retriever:
    def __init__(self):
        # Load chunks
        with open(f"{CHUNKS_PATH}/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

        # Prepare corpus (tokenized)
        self.corpus = [self._tokenize(chunk["text"]) for chunk in self.chunks]

        # Create BM25 index
        self.bm25 = BM25Okapi(self.corpus)

    def _tokenize(self, text):
        # simple tokenizer
        text = text.lower()
        tokens = re.findall(r'\w+', text)
        return tokens

    def search(self, query, top_k=5):
        query_tokens = self._tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        # sort indices based on score
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        results = [self.chunks[i] for i in ranked_indices[:top_k]]

        return results