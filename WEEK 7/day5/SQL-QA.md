# SQL Question Answering System

## Overview

This project is a SQL Question Answering (SQL-QA) system that allows users to ask database-related questions in natural language. The system converts user questions into SQL queries, executes them safely on a database, and returns readable answers.

The goal is to make structured databases accessible to users without requiring SQL knowledge.

---

## What the System Does

The system follows a complete Text → SQL → Answer workflow:

1. Understands the user’s natural language question
2. Reads the database schema (tables and columns)
3. Generates an SQL query using an LLM
4. Validates the generated query for safety
5. Executes the query on SQLite
6. Summarizes the raw SQL results into readable output
7. Evaluates answer faithfulness and refines if needed

---

## System Architecture

### 1. Schema Loader

The schema loader reads the database structure dynamically.

It extracts:

* table names
* column names

Example schema:

```text id="s1"
Table: employees
Columns: id, name, department, salary

Table: sales
Columns: id, product, year, revenue
```

This schema is used in prompts so that the SQL generator only uses valid tables and columns.

---

### 2. SQL Generator

The SQL generator uses:

* user question
* schema information
* prompt instructions

It sends a structured prompt to an LLM (Groq / Llama 3.1) to generate SQL.

Example:

User question:

```text id="s2"
Which product had the highest revenue in 2023?
```

Generated SQL:

```sql id="s3"
SELECT product, revenue
FROM sales
WHERE year = 2023
ORDER BY revenue DESC
LIMIT 1;
```

---

### 3. Query Validation

Before execution, generated SQL is validated.

Safety checks:

* only SELECT queries allowed
* blocks dangerous queries:

  * DROP
  * DELETE
  * UPDATE
  * INSERT
  * ALTER

This prevents unsafe database operations.

---

### 4. SQL Execution

The validated query is executed on SQLite.

The system:

* connects to the database
* runs SQL
* fetches rows
* extracts column names

This provides raw structured output.

---

### 5. Result Summarization

Raw SQL rows are converted into readable output.

Example raw output:

```text id="s4"
('Laptop', 50000)
```

Summarized answer:

```text id="s5"
product: Laptop, revenue: 50000
```

This improves readability for users.

---

### 6. RAG Evaluation Layer

A semantic evaluation layer checks whether the generated answer is faithful to the SQL result context.

It uses:

* sentence embeddings
* cosine similarity

This helps detect possible hallucinations or mismatches.

Output example:

```text id="s6"
{
  "faithful": true,
  "confidence": 0.84
}
```

---

### 7. Answer Refinement

If confidence is low, the system sends:

* user question
* SQL result context
* current answer

to an LLM for refinement.

This improves:

* clarity
* completeness
* correctness

---

## Database Used

The project uses SQLite with multiple tables:

### Employees

* id
* name
* department
* salary

### Sales

* id
* product
* year
* revenue

### Customers

* id
* name
* country
* age

This setup was used to test:

* filtering
* sorting
* grouping
* aggregation

---

## Key Features

* Natural language to SQL conversion
* Dynamic schema loading
* Safe SQL execution
* Result summarization
* Semantic answer evaluation
* LLM-based answer refinement

---


## Summary

This project bridges natural language and structured databases by converting user questions into SQL queries, safely executing them, and returning clear answers.

It combines:

* schema-aware SQL generation
* validation
* execution
* semantic evaluation
* answer refinement

to create a reliable SQL Question Answering system.
