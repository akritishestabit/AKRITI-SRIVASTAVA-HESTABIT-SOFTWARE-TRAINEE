# Week 7 — GenAI & Multimodal RAG System

## Overview

This project implements an end-to-end enterprise-grade GenAI system capable of handling multiple data modalities including text, images, and structured databases. The system uses Retrieval-Augmented Generation (RAG), multimodal embeddings, and SQL-based reasoning to provide accurate and reliable answers.

---

## Objectives

* Build a complete RAG pipeline for document understanding
* Implement hybrid retrieval (semantic + keyword + reranking)
* Support image-based retrieval using multimodal techniques
* Convert natural language queries into SQL and execute them
* Add conversational memory and evaluation mechanisms
* Reduce hallucination using scoring and refinement loops

---

## System Architecture

User Query → Memory → Retrieval / SQL / Image → LLM → Evaluation → Refinement → Final Answer

---

## Components

### 1. Text RAG System

* Loads and processes documents (PDF, DOCX, TXT, CSV)
* Splits text into chunks with metadata
* Generates embeddings and stores them in FAISS
* Retrieves relevant chunks based on query

---

### 2. Advanced Retrieval

* Combines semantic search (embeddings) with keyword search (BM25)
* Uses reranking to improve result relevance
* Removes duplicate or low-quality chunks

---

### 3. Image RAG (Multimodal)

* Extracts text using OCR (Tesseract)
* Generates captions using BLIP
* Creates image embeddings using CLIP
* Supports:

  * Text → Image search
  * Image → Image similarity
  * Image → Text explanation

---

### 4. SQL Question Answering

* Converts natural language queries into SQL using LLM
* Uses schema-aware prompting
* Validates queries to allow only safe SELECT operations
* Executes queries on SQLite database
* Returns structured results in readable format

---

### 5. Memory System

* Stores last 5 interactions
* Maintains conversational context
* Saves data in a local JSON file (`CHAT-LOGS.json`)

---

### 6. Evaluation System

* Computes similarity between context and answer
* Detects hallucinations
* Generates confidence score for each response

---

### 7. Refinement Loop

* Re-evaluates low-confidence answers
* Improves responses using LLM with context grounding
* Ensures higher reliability and accuracy

---

### 8. Deployment Layer

* Unified application (`app.py`) connecting all pipelines
* Supports:

  * `/ask` (Text RAG)
  * `/ask-sql` (SQL QA)
  * `/ask-image` (Image RAG)
* CLI-based interface for interaction

---

## Technologies Used

* Python
* SQLite
* FAISS (Vector Database)
* Sentence Transformers (Embeddings)
* Groq API (LLaMA 3.1 model)
* Tesseract OCR
* CLIP (Image Embeddings)
* BLIP (Image Captioning)

---

## Folder Structure

```id="m7q3hp"
src/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── chunks/
│   └── database.db
│
├── embeddings/
├── vectorstore/
├── retriever/
├── generator/
├── pipelines/
├── evaluation/
├── memory/
├── deployment/
├── utils/
├── config/
└── logs/
```

---

## How to Run

### 1. Activate environment

```id="hzf4i7"
source venv/bin/activate
```

### 2. Run the application

```id="2zn8y9"
python -m src.deployment.app
```

---

## Example Queries

* "Explain credit underwriting process"
* "Show employees with high salary"
* "List customers from India"
* "Find similar images to this diagram"

---

## Key Features

* Multi-modal RAG system (Text + Image + SQL)
* Hybrid retrieval with reranking
* Schema-aware SQL generation
* Conversational memory
* Hallucination detection and confidence scoring
* Self-refinement loop for improving answers
* Modular and scalable architecture

---

## Key Learnings

* Designing end-to-end RAG pipelines
* Integrating LLMs with structured and unstructured data
* Handling multimodal data (text + images)
* Building reliable AI systems with evaluation mechanisms
* Reducing hallucination using context-based scoring
* Creating production-ready GenAI applications

---

## Conclusion

This project demonstrates how to build a complete GenAI system capable of handling enterprise-level use cases. It combines retrieval, reasoning, multimodal processing, and evaluation techniques to deliver accurate and reliable results.

The system is modular, extensible, and suitable for real-world applications such as knowledge management, analytics, and intelligent assistants.
