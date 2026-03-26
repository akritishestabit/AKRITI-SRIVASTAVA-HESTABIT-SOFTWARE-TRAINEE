import os
import json
from config.settings import CHUNKS_PATH

CHUNK_SIZE = 500
OVERLAP = 100

def chunk_text(documents):
    all_chunks = []

    for doc_id, doc in enumerate(documents):
        text = doc["text"]

        start = 0
        chunk_id = 0

        while start < len(text):
            end = start + CHUNK_SIZE
            chunk_text = text[start:end]

            all_chunks.append({
                "id": f"{doc_id}_{chunk_id}",
                "text": chunk_text,
                "source": doc["source"],
                "page": doc["page"],
                "type": doc.get("type", "unknown")
            })

            start += CHUNK_SIZE - OVERLAP
            chunk_id += 1

   
    filepath = os.path.join(CHUNKS_PATH, "chunks.json")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    return all_chunks