# TOOL-CHAIN.md — Day 3: Tool-Calling Agents

## Overview

Day 3 introduces **tool-using agents** — agents that can perform real-world actions
by calling Python functions directly. Unlike Day 1 (pure LLM chains) and Day 2
(orchestrated parallel workers), Day 3 agents interact with the file system,
databases, and the Python interpreter itself.

---

## Architecture

```
User Query
    ↓
Orchestrator Agent
  (routes query to relevant agents via JSON plan)
    ↓           ↓           ↓
File_Agent   DB_Agent   Code_Agent
(.txt/.csv)  (SQLite)   (Python exec)
    ↓           ↓           ↓
         Synthesizer Agent
              ↓
        Final Answer
```

---

## Agents & Their Tools

### 1. File_Agent — `tools/file_agent.py`

| Tool | Purpose |
|------|---------|
| `read_file(file_path)` | Read `.txt` or `.csv` files; CSV returns JSON rows |
| `write_file(file_path, content, mode)` | Write (`w`) or append (`a`) to `.txt`/`.csv` |
| `list_files(directory, extension_filter)` | Discover files in a directory |
| `create_sample_csv(file_path)` | Generate demo `sales.csv` for testing |

**Trigger keywords:** file, csv, txt, read, write, document, report, save

---

### 2. DB_Agent — `tools/db_agent.py`

| Tool | Purpose |
|------|---------|
| `get_schema(db_path)` | Inspect all tables and columns in a SQLite database |
| `run_sql_query(db_path, query)` | Execute any SQL (SELECT, INSERT, UPDATE, etc.) |
| `create_sample_db(db_path)` | Create a demo `sales.db` database for testing |

**Trigger keywords:** database, SQL, SQLite, table, query, records, schema

---

### 3. Code_Agent — `tools/code_executor.py`

| Tool | Purpose |
|------|---------|
| `execute_python_code(code)` | Run a Python snippet; captures stdout or raises error |

**Trigger keywords:** analyze, compute, calculate, Python, run, code, script, insights

---

## Orchestrator Routing

The `Orchestrator` agent receives the user query and returns a JSON routing plan:

```json
{
  "requires_file_agent": true,
  "requires_db_agent": false,
  "requires_code_agent": true,
  "file_task": "Read sales.csv and extract all rows",
  "db_task": "",
  "code_task": "Analyze the CSV data and compute top 5 insights",
  "reason": "Task involves a CSV file and data analysis"
}
```

Agents that are activated (`true`) run **concurrently** via `asyncio.gather`.

---

## Example Flow

### Query: *"Analyze sales.csv and generate top 5 insights"*

```
Orchestrator
  → requires_file_agent: true   (read the CSV)
  → requires_code_agent: true   (analyze the data)
  → requires_db_agent:   false  (no database involved)

File_Agent:
  → list_files(".")             # discover sales.csv
  → read_file("sales.csv")      # load all rows as JSON

Code_Agent:
  → execute_python_code(...)    # compute stats, top products, revenue

Synthesizer:
  → Merges File + Code outputs into final answer
```

---

## File Structure

```
day3/
├── main.py                  ← Entry point / orchestrator pipeline
├── config.py                ← Shared LLM configuration (Groq / llama-3.1-8b-instant)
├── tools/
│   ├── __init__.py
│   ├── file_agent.py        ← File_Agent + tools (read, write, list, sample)
│   ├── db_agent.py          ← DB_Agent + tools (schema, query, sample db)
│   └── code_executor.py     ← Code_Agent + Python execution tool
└── TOOL-CHAIN.md            ← This file
```

---

## Setup & Run

```bash
# 1. Set your API key
export GROQ_API_KEY="your_groq_api_key_here"

# 2. Install dependencies (already in venv)
pip install pyautogen python-dotenv

# 3. Run
cd day3
python main.py
```

---

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| Tools registered on agent **and** proxy | AutoGen requires dual registration for LLM-to-execution wiring |
| `asyncio.gather` for parallel agents | Mirrors Day 2's parallel worker pattern |
| Orchestrator returns JSON | Deterministic, parseable routing — no ambiguity |
| Safe fallback on JSON parse failure | Activates all agents to avoid silent failures |
| `create_sample_*` tools included | Allows zero-config demo without real files/DBs |
| Sandboxed `exec` with captured stdout | Safe code execution with full output capture |

---

## Key Concepts Practiced

- **Function / Tool calling** — agents call Python functions, not just generate text
- **System-to-tool execution** — LLM decides when and how to call a tool
- **Async parallel agent execution** — multiple agents run concurrently
- **Orchestration with routing** — a meta-agent decides the tool-chain
- **Separation of concerns** — each agent owns exactly one tool domain