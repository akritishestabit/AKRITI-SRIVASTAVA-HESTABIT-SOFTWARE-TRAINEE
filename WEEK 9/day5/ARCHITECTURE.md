# NEXUS AI — System Architecture

## Overview

NEXUS AI is an autonomous multi-agent system designed to process complex user queries through structured planning, parallel execution, tool integration, and self-reflection.

The system combines:

* Multi-agent orchestration
* Tool execution (code, file, database)
* Memory (short-term + long-term)
* Iterative refinement (critic → optimizer → validator)

---

## High-Level Flow Diagram

```mermaid
flowchart TD
    A[User Input] --> B[Memory Recall]
    B --> C[Orchestrator]
    C --> D[Planner (DAG)]
    D --> E[Worker Agents]

    E --> E1[Researcher]
    E --> E2[Coder]
    E --> E3[Analyst]

    E1 --> F[Tool Layer]
    E2 --> F
    E3 --> F

    F --> G[Parallel Execution Engine]

    G --> H[Critic]
    H --> I[Optimizer]
    I --> J[Validator]
    J --> K[Reporter]

    K --> L[Final Output]
    L --> M[Memory Storage]
```

---

## High-Level Flow

User Input
→ Memory Recall
→ Orchestrator
→ Planner (DAG)
→ Workers (Parallel Execution)
→ Critic
→ Optimizer
→ Validator
→ Reporter
→ Final Output
→ Memory Storage

---

## Core Components

### 1. Orchestrator Agent

* Converts raw user query into a refined objective
* Uses both short-term and long-term memory
* Ensures context-aware understanding

---

### 2. Planner Agent

* Breaks down objective into structured tasks
* Generates task distribution (researcher / coder / analyst)
* Works as a DAG-like planner (parallel-ready tasks)

---

### 3. Worker Agents

#### Researcher

* Handles file operations
* Reads, summarizes, and extracts insights

#### Coder

* Generates and executes Python code
* Returns structured outputs and explanations

#### Analyst

* Handles SQL queries
* Works with structured data (SQLite)

---

### 4. Tool Layer

Tools are executed via a controlled proxy:

* File Tools → read/write/list files
* Database Tools → SQL execution
* Code Executor → Python execution

Ensures separation between reasoning and execution.

---

### 5. Parallel Execution Engine

* Uses asyncio
* Executes multiple workers concurrently
* Improves performance and scalability

---

### 6. Reflection Layer

#### Critic

* Reviews worker output
* Identifies issues and gaps

#### Optimizer

* Improves output based on feedback

#### Validator

* Ensures correctness and completeness

---

### 7. Reporter Agent

* Generates final structured output
* Adapts formatting based on task type:

  * Code → Python blocks + explanation
  * SQL → query + exact output
  * File → strict factual summary

---

## Memory System

### Short-Term Memory

* Stores last_output
* Resolves references like "it", "this"

### Long-Term Memory (Vector Store)

* Stores extracted facts using embeddings
* Enables semantic retrieval via FAISS

### Persistent Memory (SQLite)

* Stores full conversation logs
* Used for traceability

---

## Key Design Decisions

* Hybrid architecture (LLM + rule-based routing)
* Separation of reasoning and execution
* Context-aware orchestration
* Fault-tolerant execution

---

## System Characteristics

* Modular
* Scalable
* Context-aware
* Fault-tolerant
* Production-ready foundation

---
