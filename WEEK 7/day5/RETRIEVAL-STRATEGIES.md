# Retrieval Strategies – Day 2

## Overview

In Day 2, the retrieval pipeline was enhanced to improve the quality, relevance, and diversity of the information passed to the model. The goal was to reduce noise, avoid duplication, and ensure that only the most useful context is selected.

The system now uses a hybrid retrieval approach combined with reranking, deduplication, and context engineering.

---

## 1. Hybrid Retrieval (Semantic + Keyword)

The system combines two types of search:

### Semantic Search (FAISS)

* Uses embeddings to understand the meaning of the query
* Retrieves context even if exact keywords are not present
* Example: “loan risk evaluation” can match “credit underwriting”

### Keyword Search (BM25)

* Matches exact words from the query
* Useful for IDs, policies, or specific terms

---

## 2. Result Combination

Results from FAISS and BM25 are combined into a single list:

* FAISS results (semantic)
* BM25 results (keyword)

This ensures that both meaning-based and exact matches are included.

---

## 3. Deduplication

After combining results, duplicate chunks are removed.

### Approach:

* Exact text matching is used
* Only unique chunks are retained

### Why?

* Prevents repeated information
* Reduces confusion for the model
* Improves clarity of context

---

## 4. Reranking (Cosine Similarity)

The combined results are reranked using cosine similarity.

### Process:

* Convert query and chunks into embeddings
* Normalize vectors
* Compute similarity using dot product
* Sort results based on similarity score

### Benefit:

* Ensures most relevant chunks appear first
* Improves precision of retrieval

---

## 5. Max Marginal Relevance (Conceptual Use)

Although not explicitly implemented as a formula, the system achieves similar behavior through:

* Deduplication
* Reranking

### Goal:

* Balance relevance and diversity
* Avoid redundant chunks

---

## 6. Context Engineering

Before passing data forward, the system prepares structured context.

### Steps:

1. Limit number of chunks (top_k)
2. Remove duplicates
3. Format context with metadata

### Example Format:

```
[Source: policy.pdf | Page: 2]
Credit underwriting is the process...

---
[Source: doc2 | Page: 3]
It involves risk evaluation...
```

### Benefits:

* Clean and readable structure
* Traceable sources
* Better understanding for downstream processing

---

## 7. Key Improvements Over Basic Retrieval

| Feature              | Day 1         | Day 2      |
| -------------------- | ------------- | ---------- |
| Search Type          | Semantic only | Hybrid     |
| Ranking              | Basic         | Reranked   |
| Duplication Handling | No            | Yes        |
| Context Quality      | Raw           | Structured |
| Accuracy             | Medium        | High       |

---

## Conclusion

The enhanced retrieval pipeline significantly improves the quality of retrieved information by combining multiple strategies. Hybrid search ensures better coverage, reranking improves relevance, and context engineering prepares clean and structured input.


