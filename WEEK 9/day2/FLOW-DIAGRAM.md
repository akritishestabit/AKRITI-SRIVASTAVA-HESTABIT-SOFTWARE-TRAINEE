# FLOW DIAGRAM — DAY 2 MULTI-AGENT SYSTEM

## Overview

This system implements a DAG-based multi-agent architecture where a user query is broken into structured tasks, executed in parallel with dependency control, and then combined into a final validated response.

---

## High-Level Flow

User Query  
↓  
Planner Agent (Task Decomposition)  
↓  
DAG Task Graph (Tasks + Dependencies)  
↓  
Worker Agents (Parallel Execution)  
↓  
Reflection Agent (Merge Outputs)  
↓  
Validator Agent (Final Answer)  

---

## Step-by-Step Flow

### 1. User Input

The system begins with a user query.

Example:
"Explain Machine Learning and Deep Learning and compare them."

---

### 2. Planner Agent

The planner analyzes the query and converts it into a DAG (Directed Acyclic Graph).

Output format:
- Each task has:
  - id
  - description
  - dependencies

Example:
- t1: Explain Machine Learning (no dependencies)
- t2: Explain Deep Learning (no dependencies)
- t3: Compare ML and DL (depends on t1, t2)

---

### 3. DAG Formation

The planner output defines:
- Independent tasks → can run immediately
- Dependent tasks → must wait

This structure ensures:
- parallel execution
- correct ordering

---

### 4. Worker Execution Engine

Each task is assigned to a Worker Agent.

Execution behavior:

- All tasks are initialized together
- Tasks are added as coroutines
- asyncio.gather() starts them concurrently

---

### 5. Dependency Control (Core Logic)

Dependency handling is implemented using asyncio events.

Key mechanism:

- Each task has an event
- Dependent tasks wait:
  await events[dep].wait()

- When a task finishes:
  events[t_id].set()

This ensures:
- independent tasks run first
- dependent tasks run only after required tasks complete

---

### 6. Parallel Execution

Independent tasks:
- start immediately

Dependent tasks:
- pause at wait()
- resume only after dependencies are completed

---

### 7. Worker Output

Each worker:
- processes only its assigned task
- returns a clean response (using summary_method="last_msg")

Outputs are stored and aggregated.

---

### 8. Reflection Agent

The reflection agent:
- receives all worker outputs
- merges them into a structured draft

Responsibilities:
- preserve all information
- organize content logically
- avoid adding new information

---

### 9. Validator Agent

The validator agent:
- reviews the draft
- corrects errors
- ensures completeness
- formats the final answer

Output:
- clean
- structured
- user-ready

---

## Execution Behavior Summary

| Component | Role |
|----------|------|
| Planner | Converts query into DAG |
| Workers | Execute tasks |
| Events | Control dependencies |
| asyncio.gather | Enables parallel execution |
| Reflection | Merges outputs |
| Validator | Produces final answer |

---

## Key Technical Concepts

### 1. Coroutines
Tasks are stored as async functions and executed concurrently.

### 2. asyncio.gather
Starts all tasks together.

### 3. Event System
Controls execution order:
- wait() → block
- set() → release

### 4. DAG Execution
Ensures:
- no circular dependencies
- correct task ordering
- efficient execution

---

## Final Flow Summary

1. User provides query  
2. Planner generates DAG  
3. Workers execute tasks in parallel  
4. Dependencies enforced using events  
5. Outputs are aggregated  
6. Reflection merges outputs  
7. Validator finalizes answer  

---

## Design Benefits

- Parallel execution improves efficiency  
- Dependency handling ensures correctness  
- Modular agents improve scalability  
- Clean pipeline ensures structured output  

---

## Final Note

This system demonstrates a complete multi-agent orchestration pipeline combining:
- planning
- parallel execution
- dependency management
- synthesis
- validation