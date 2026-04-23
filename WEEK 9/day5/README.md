# NEXUS AI

An autonomous multi-agent AI system capable of planning, executing, and refining complex tasks using tools, memory, and parallel processing.

---

## Overview

NEXUS AI is designed to simulate a real-world intelligent system by combining multiple AI agents, tool execution, and memory systems.

It can:

* Understand complex queries
* Break them into tasks
* Execute tasks using tools
* Refine results automatically
* Remember past interactions

---

## Features

* Multi-agent architecture
* Parallel task execution
* Tool integration (file, database, code)
* Short-term and long-term memory
* Self-reflection pipeline
* Structured output generation

---

## Project Structure

```
nexus_ai/
│
├── agents/
│   ├── orchestrator.py
│   ├── planner.py
│   ├── workers.py
│   ├── critics.py
│
├── tools/
│   ├── file_agent.py
│   ├── db_agent.py
│   ├── code_executor.py
│
├── memory/
│   ├── session_memory.py
│   ├── vector_store.py
│
├── main.py
├── config.py
```

---

## How It Works

1. User enters a query
2. System retrieves relevant memory
3. Orchestrator refines the objective
4. Planner generates tasks
5. Workers execute tasks in parallel
6. Critic reviews output
7. Optimizer improves it
8. Validator ensures correctness
9. Reporter generates final output
10. Memory is updated

---

## Installation

1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Set environment variable:

```
export GROQ_API_KEY=your_key_here
```

---

## Run the Project

```
python main.py
for ui - streamlit run app.py
```

---

## Example Queries

* Analyze a CSV file and provide insights
* Generate Python code for a task
* Query a database using SQL
* Summarize a text file
* Continue a previous conversation

---

## Design Highlights

* Hybrid system (LLM + rule-based)
* Modular architecture
* Fault-tolerant execution
* Context-aware reasoning

---

## Limitations

* Depends on LLM accuracy
* Context window limitations
* Basic rule-based routing

---

## Future Scope

* Full DAG execution engine
* Smarter memory retrieval
* Agent registry system
* Real-time UI

---

## License

For educational and research purposes
