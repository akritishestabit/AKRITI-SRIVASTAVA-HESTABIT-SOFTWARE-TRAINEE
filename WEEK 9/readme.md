# Week 9 — Multi-Agent AI Systems (NEXUS AI)

## Overview

This repository documents the complete journey of building an autonomous multi-agent AI system over five days. Each day introduces a core concept, gradually evolving from basic agents to a production-style system called **NEXUS AI**.

The final system demonstrates:

* Multi-agent orchestration
* Tool integration (code, database, file operations)
* Memory (short-term and long-term)
* Parallel execution
* Self-reflection and validation

---

## Learning Progression

### Day 1 — Agent Fundamentals

* Built basic agents:

  * Research Agent
  * Summarizer Agent
  * Answer Agent
* Learned how agents communicate and pass information

---

### Day 2 — Multi-Agent Orchestration

* Introduced:

  * Planner Agent
  * Worker Agents
  * Reflection Agent
  * Validator Agent
* Implemented:

  * Task decomposition
  * Parallel execution using asyncio
* Output pipeline:
  Planner → Workers → Reflection → Validator

---

### Day 3 — Tool-Calling Agents

* Enabled agents to interact with real tools:

  * File operations (read/write)
  * SQLite database queries
  * Python code execution
* Introduced **function calling without APIs**
* Built a tool execution layer using a proxy

---

### Day 4 — Memory System

* Implemented:

  * Short-term memory (session-based)
  * Long-term memory (vector-based using FAISS)
* Stored:

  * Conversation history (SQLite)
  * Extracted facts (semantic memory)
* Enabled:

  * Context-aware responses

---

### Day 5 — Capstone Project: NEXUS AI

A complete autonomous multi-agent system combining all previous concepts.

---

## NEXUS AI — System Overview

NEXUS AI is designed to handle complex queries through a structured pipeline:

User Input
→ Memory Recall
→ Orchestrator
→ Planner
→ Workers (Parallel Execution)
→ Critic
→ Optimizer
→ Validator
→ Reporter
→ Final Output
→ Memory Storage

---

## Key Features

### Multi-Agent Architecture

* Orchestrator: understands user intent
* Planner: breaks tasks into components
* Workers: execute tasks
* Critic / Optimizer / Validator: improve output
* Reporter: generates final structured response

---

### Parallel Execution

* Uses asyncio for concurrent task processing
* Improves performance and scalability

---

### Tool Integration

* File operations
* SQL database queries
* Python code execution

Agents can perform real-world tasks beyond text generation.

---

### Memory System

#### Short-Term Memory

* Tracks previous output
* Resolves references like “it”, “this”

#### Long-Term Memory

* Stores extracted facts using vector embeddings
* Enables semantic search using FAISS

#### Persistent Storage

* SQLite database for full interaction logs

---

### Self-Improvement Pipeline

* Critic: identifies issues
* Optimizer: refines output
* Validator: ensures correctness

---

### Dynamic Output Generation

* Code → formatted Python blocks
* SQL → query + exact results
* File → structured summaries

---

## Project Structure

```text
Week 9/
│
├── day1/
├── day2/
├── day3/
├── day4/
├── day5/
│   ├── nexus_ai/
│   │   ├── agents/
│   │   ├── tools/
│   │   ├── memory/
│   │   ├── data/
│   │   ├── main.py
│   │   └── config.py
│   ├── ARCHITECTURE.md
│   ├── FINAL-REPORT.md
│   └── README.md
│
└── Week9.pdf
```

---

## How to Run

### 1. Setup Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. Add API Key

```bash
export GROQ_API_KEY=your_api_key
```

---

### 3. Run the System

```bash
cd day5/nexus_ai
python main.py
```

---

## Example Queries

* Read and summarize a file
* Analyze a CSV dataset
* Generate and execute Python code
* Query a database using SQL
* Continue a previous conversation

---

## Design Highlights

* Hybrid system (LLM + rule-based control)
* Modular and extensible architecture
* Fault-tolerant execution
* Context-aware reasoning

---

## Challenges Solved

* Handling inconsistent LLM outputs
* Managing conversational context
* Ensuring correct task-agent mapping
* Avoiding hallucinations in structured outputs

---

## Improvements Implemented

* JSON cleaning for planner outputs
* Output sanitization layer
* Rule-based fallback routing
* Short-term memory for context resolution

---

## Limitations

* Dependent on LLM accuracy
* Limited context window
* Static routing rules for some tasks

---

## Future Scope

* Dynamic agent registry
* Full DAG execution engine
* Better memory ranking
* UI/dashboard integration
* Real-time streaming responses

---

## Conclusion

Week 9 demonstrates the transition from simple agents to a fully autonomous AI system. NEXUS AI combines reasoning, execution, memory, and self-improvement into a single pipeline, making it a strong foundation for real-world AI applications.

---

