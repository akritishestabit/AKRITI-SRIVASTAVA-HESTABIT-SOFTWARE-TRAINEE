# Agent Memory System Architecture

This document describes the **Day 4 Memory Architecture** of the AI agent.
The system is designed to simulate **human-like memory behavior** by separating:

* Active conversational memory
* Exact historical records
* Abstract semantic knowledge

---

## System Overview

The architecture follows a **Retrieval-Augmented Generation (RAG)** pattern combined with **multi-layered memory storage**.

It ensures that the agent:

* Remembers ongoing conversations
* Stores past interactions permanently
* Retrieves relevant knowledge intelligently

---

## System Flow Diagram


flowchart TD
    A[User Query] --> B[Query Embedding]
    B --> C[FAISS Semantic Search]
    C --> D[Top-K Memory Retrieval]
    D --> E[Combine with Short-Term Memory]
    E --> F[Prompt Injection]
    F --> G[LLM Response Generation]
    G --> H[Store in Short-Term Memory]
    G --> I[Store in SQLite (Episodic)]
    G --> J[Store in FAISS (Semantic)]


---

## Step-by-Step Flow

1. **User Query** is received
2. Query is converted into a **vector embedding**
3. **FAISS index** is searched for similar past knowledge
4. Top-K relevant memories are retrieved
5. Combined with **short-term memory (current session)**
6. Injected into the **LLM prompt**
7. LLM generates a **context-aware response**
8. Output is stored in:

   * Short-Term Memory (RAM)
   * Episodic Memory (SQLite)
   * Semantic Memory (FAISS)

---

## Memory Types

### 1. Short-Term Memory (Session RAM)

**Role**
Maintains continuity within the current conversation session.

**Mechanism**

```python
[
  {"role": "user", "content": "..."},
  {"role": "assistant", "content": "..."}
]
```

**Characteristics**

* Fast in-memory access
* Stores recent interactions only
* Enables context-aware responses

**Lifecycle**

* Cleared when:

  * Session ends
  * `.clear_short_term()` is called

---

### 2. Episodic Long-Term Memory (SQLite)

**Role**
Acts as a permanent record of all interactions.

**Mechanism**

* Stored in database: `long_term.db`

**Characteristics**

* Chronological storage
* Exact transcripts
* Tracks:

  * Speaker (user/assistant)
  * Message
  * Timestamp

**Use Cases**

* Debugging
* Chat history
* Session reconstruction

---

### 3. Semantic Vector Memory (FAISS)

**Role**
Stores abstract knowledge for intelligent retrieval.

**Mechanism**

```
Text → Embedding → Vector → FAISS Index
```

**Tech Stack**

* `sentence-transformers`
* `faiss.IndexFlatL2`

**Characteristics**

* Meaning-based search
* Fast similarity matching
* Works even with rephrased queries

**Example**

```
Stored: "My favorite color is blue"

Query: "What is my favorite color?"

→ Semantic match via embeddings  
→ Correct retrieval  
→ Accurate response  
```

---

## Memory Interaction Summary

| Memory Type | Speed  | Storage | Purpose                 |
| ----------- | ------ | ------- | ----------------------- |
| Short-Term  | Fast   | RAM     | Active conversation     |
| Episodic    | Slow   | SQLite  | Exact history           |
| Semantic    | Medium | FAISS   | Meaning-based retrieval |

---

## Key Design Principles

### Separation of Concerns

* Short-Term → current context
* Episodic → exact history
* Semantic → abstract meaning

### Retrieval-Augmented Generation (RAG)

Enhances LLM by injecting:

* Past knowledge (FAISS)
* Current context (RAM)

### Efficient Storage

* RAM → speed
* SQLite → persistence
* FAISS → intelligence

---

## Final Insight

This architecture mirrors human cognition:

* Short-Term → “What is happening now?”
* Episodic → “What happened?”
* Semantic → “What does it mean?”

Result:

* Better context understanding
* Long-term recall
* Accurate and intelligent responses

---
