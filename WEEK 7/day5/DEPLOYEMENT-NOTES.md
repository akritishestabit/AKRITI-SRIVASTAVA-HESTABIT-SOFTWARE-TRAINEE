# Deployment Notes — GenAI System (Week 7)

## Overview

This project is an enterprise-style GenAI system that supports:

* Text-based RAG
* Image-based retrieval (multimodal RAG)
* SQL-based question answering

The system integrates memory, evaluation, and refinement to improve answer reliability and reduce hallucinations.

---

## System Architecture

User Query → Pipeline Selection → LLM → Evaluation → Refinement → Final Answer

Pipelines:

* Text RAG
* Image RAG
* SQL QA

---

## Components

### 1. Pipelines

* SQL Pipeline: Converts natural language to SQL and executes it
* Text Pipeline: Retrieves relevant document chunks
* Image Pipeline: Uses CLIP + OCR + captions

---

### 2. Memory System

* Stores last 5 interactions
* Saved in `CHAT-LOGS.json`
* Enables context-aware responses

---

### 3. Evaluation System

* Computes similarity between context and answer
* Detects hallucinations
* Generates confidence score

---

### 4. Refinement Loop

* Re-evaluates low-confidence answers
* Improves answer using LLM with context grounding

---

## LLM Configuration

* Provider: Groq
* Model: llama-3.1-8b-instant
* API Key stored as environment variable:
  GROQ_API_KEY

---

## Running the Application

### Step 1: Activate environment

```bash
source venv/bin/activate
```

### Step 2: Run the app

```bash
python -m src.deployment.app
```

---

## Available Modes

1. Text RAG
2. SQL QA
3. Image RAG

---

## Example Usage

User selects SQL mode and asks:
"Show employees with high salary"

System:

* Generates SQL using LLM
* Executes query
* Evaluates answer
* Returns final answer with confidence score

---

## Logging

* All conversations stored in:
  `CHAT-LOGS.json`

* Includes:

  * User query
  * Assistant response

---

## Safety Measures

* SQL validation (only SELECT allowed)
* Hallucination detection
* Confidence scoring
* Fallback mechanism for LLM failure

---

## Future Improvements

* Streamlit UI for better interaction
* Redis-based memory for scalability
* Advanced reranking for text retrieval
* Multi-agent architecture

---

## Conclusion

This system demonstrates a production-ready GenAI pipeline with:

* Multi-modal capabilities
* Reliable answer generation
* Self-correcting mechanisms
* Scalable architecture
