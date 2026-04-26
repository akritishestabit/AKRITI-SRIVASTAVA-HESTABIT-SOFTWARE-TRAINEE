from src.utils.file_loader import load_files
from src.utils.cleaner import save_cleaned_documents
from src.utils.chunker import chunk_text
from src.embeddings.embedder import Embedder
from src.vectorstore.faiss_store import FAISSStore

def run_pipeline():
    print("Starting pipeline...")

   
    print("Loading files...")
    documents = load_files()

   
    print("Cleaning documents...")
    cleaned_docs = save_cleaned_documents(documents)

    
    print("Creating chunks...")
    chunks = chunk_text(cleaned_docs)

    
    print("Generating embeddings...")
    embedder = Embedder()
    embeddings = embedder.encode(chunks)

    print("Creating FAISS index...")
    store = FAISSStore()
    store.create_index(embeddings)
    store.save_index()

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()