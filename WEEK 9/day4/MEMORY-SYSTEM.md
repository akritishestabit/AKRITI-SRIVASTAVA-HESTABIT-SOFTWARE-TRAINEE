# Agent Memory System Architecture

This document describes the Day 4 Memory Architecture implemented for the AI agent. The system gives the agent proper human-like memory characteristics, separating exact chronological memories from abstract core facts.

## System Flow

When a New Query arrives:
1. **Search Memory**: The query is embedded into a vector, and we query the FAISS index (Semantic Memory).
2. **Fetch Context**: FAISS mathematically retrieves the K most nearest vectors (similar facts).
3. **Inject in Prompt**: These retrieved facts, alongside active Short-Term Memory, are appended to the system instructions.
4. **Generate with Context**: The LLM creates an answer knowing the extended context.
5. **Summarize and Store**: The response is saved exactly in SQLite (Episodic) and in real-time RAM (Short-term), whilst key takeaways are sent back through the Embedding Model into FAISS (Semantic).

## Memory Types Used

### 1. Short-Term Memory (Session RAM)
- **Role**: Maintains coherence in the current active conversational session.
- **Mechanism**: A fast list (`[]`) that simply stores `{"role": "user/assistant", "content": "..."}`.
- **Lifecycle**: Cleared automatically when the script terminates or via `.clear_short_term()`.

### 2. Episodic Long-Term Memory (SQLite)
- **Role**: The permanent "black box" flight-recorder of the agent.
- **Mechanism**: Relational Database (`long_term.db`).
- **Characteristics**: Chronological, exact transcripts. It remembers the WHO exactly said WHAT and WHEN. 
- **Use-Case**: Auditing historical behavior, rebuilding past short-term RAM, or displaying chat history in a UI.

### 3. Semantic Vector Memory (FAISS)
- **Role**: Abstract core knowledge and context retrieval.
- **Mechanism**: `sentence-transformers` -> Dense Numerical Vectors -> `faiss.IndexFlatL2`.
- **Characteristics**: Fast, meaning-based associative query search instead of exact keyword match.
- **Use-Case**: If the user told the agent their favorite color was "blue" 3 months ago (which fell out of RAM long ago), questioning "What is my favorite color?" will trigger a FAISS distance calculation matching the embedding of the query cleanly with the historical fact, surfacing "Your favorite color is blue" instantaneously.
