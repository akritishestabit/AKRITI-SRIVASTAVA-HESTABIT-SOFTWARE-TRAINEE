# SQL Question Answering System (Day 4)

## Overview

This project implements a SQL-based Question Answering system that converts natural language queries into SQL, executes them on a database, and returns human-readable answers.

The system follows a structured pipeline:
User Query → SQL Generation → Validation → Execution → Answer

---

## Objective

* Convert natural language questions into SQL queries
* Use database schema for accurate query generation
* Ensure safe query execution
* Return meaningful answers from database results

---

## System Components

### 1. Schema Loader (`schema_loader.py`)

* Extracts database structure (tables and columns)
* Provides schema in text format for LLM
* Helps the model understand available data

---

### 2. SQL Generator (`sql_generator.py`)

* Converts user query into SQL using LLM (Groq - LLaMA 3.1)
* Uses schema-aware prompting
* Ensures only valid SELECT queries are generated
* Includes fallback mechanism if LLM fails

---

### 3. SQL Pipeline (`sql_pipeline.py`)

Handles the complete workflow:

#### Steps:

1. Accept user query
2. Generate SQL using LLM
3. Validate SQL (only SELECT allowed)
4. Execute query on SQLite database
5. Format and return results

---

## Features

* Schema-aware SQL generation
* LLM-based dynamic query creation
* Query validation for safety
* Error handling and fallback support
* Human-readable result formatting

---

## Example

### Input:

```
Show customers from India
```

### Generated SQL:

```
SELECT * FROM customers WHERE country = 'India';
```

### Output:

```
id: 1, name: John, country: India, age: 28  
id: 3, name: Raj, country: India, age: 25
```

---

## Technologies Used

* Python
* SQLite
* Groq API (LLaMA 3.1 model)
* Prompt Engineering

---

## Key Learnings

* Converting natural language to SQL using LLMs
* Importance of schema-aware prompting
* Query validation for safe execution
* Handling LLM failures with fallback logic
* Building end-to-end data pipelines

---

## Conclusion

This system demonstrates how LLMs can be integrated with structured databases to enable intelligent query systems. It is scalable, safe, and applicable to real-world data applications.
