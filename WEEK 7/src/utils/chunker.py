import os
import json
import tiktoken
from src.config.settings import CHUNKS_PATH

CHUNK_SIZE = 400   
OVERLAP = 50       


enc = tiktoken.get_encoding("cl100k_base")

def chunk_text(documents):
    all_chunks = []

    os.makedirs(CHUNKS_PATH, exist_ok=True)

    for doc_id, doc in enumerate(documents):
        text = doc["text"]

        
        tokens = enc.encode(text)

        start = 0
        chunk_id = 0

        while start < len(tokens):
            end = start + CHUNK_SIZE

            
            chunk_tokens = tokens[start:end]

           
            chunk = enc.decode(chunk_tokens)

            if chunk.strip():
                all_chunks.append({
                    "id": f"{doc_id}_{chunk_id}",
                    "text": chunk,
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