import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR: {BASE_DIR}")


RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "cleaned")
CHUNKS_PATH = os.path.join(BASE_DIR, "data", "chunks")


FAISS_INDEX_PATH = os.path.join(BASE_DIR, "vectorstore", "index.faiss")


CHUNK_SIZE = 500
CHUNK_OVERLAP = 100