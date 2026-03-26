# Retrieval Strategies (Day 2)

## Goal

Improve retrieval accuracy and reduce wrong results.

---

## Problem in Day 1

- FAISS uses semantic similarity only
- It fails for:
  - IDs
  - Numbers
  - Exact matches

---

## Solution: Hybrid Retrieval

We combine:

1. FAISS → semantic search (meaning)
2. BM25 → keyword search (exact words)

---

## Final Flow

Query
 ↓
BM25 (keyword search)
FAISS (semantic search)
 ↓
Combine results
 ↓
Remove duplicates
 ↓
Rerank results
 ↓
Build final context

---

## Components

### 1. BM25 Retriever
- Matches exact keywords
- Useful for IDs and structured data

### 2. FAISS Retriever
- Matches meaning
- Useful for natural language queries

### 3. Hybrid Retriever
- Combines BM25 + FAISS results

### 4. Reranker
- Reorders results based on relevance
- Best result comes first

### 5. Context Builder
- Cleans and formats final chunks
- Prepares context for LLM

---

## Key Insight

- FAISS ≠ exact match
- BM25 ≠ perfect match
- Hybrid = better results
- Best system = Hybrid + Reranking

---

## Limitations

- IDs still need exact matching logic
- Hybrid improves but does not guarantee perfection

---

## Output of Day 2

- Accurate retrieval
- Better ranking
- Clean context ready for LLM

---

## Final Understanding

Retriever finds candidates  
Reranker selects the best  
Context Builder prepares final input  

