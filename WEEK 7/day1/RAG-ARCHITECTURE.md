# RAG Architecture (Day 1)

## What is RAG?

RAG (Retrieval-Augmented Generation) is a system where:
- We first **retrieve relevant data**
- Then (later) use an LLM to generate answers

In Day 1, we only built the **retrieval part**

---

## System Flow

User Query is NOT used yet. We first prepare data:

Raw Data → Loader → Cleaner → Chunker → Embeddings → FAISS

---

## Step-by-Step

### 1. Loader
- Reads files (PDF, CSV, DOCX, TXT)
- Converts them into text documents

### 2. Cleaner
- Removes extra spaces and noise
- Saves cleaned text into `data/cleaned/`

### 3. Chunking
- Splits large text into small pieces (chunks)
- Adds metadata (source, page, type)
- Saves into `data/chunks/chunks.json`

### 4. Embeddings
- Converts text into vectors (numbers)
- Helps in similarity comparison

### 5. Vector Database (FAISS)
- Stores embeddings
- Enables fast similarity search

---

## Key Concept

- FAISS does NOT store text
- It stores only vectors
- Text is stored separately in `chunks.json`

---

## Output of Day 1

- Cleaned files
- Chunked data
- Embeddings
- FAISS index (`index.faiss`)
- Basic retrieval system

---



