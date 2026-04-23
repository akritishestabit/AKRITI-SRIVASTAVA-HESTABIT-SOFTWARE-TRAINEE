# ARCHITECTURE.md — Day 1 (Agent Foundations)

## Overview

This project implements a basic multi-agent pipeline using AutoGen. The system is designed to simulate how multiple specialized AI agents collaborate to solve a task in a structured and modular way.

The pipeline consists of three agents:

- Research Agent → generates detailed raw information  
- Summarizer Agent → compresses and structures the data  
- Answer Agent → produces the final user-friendly response  

---

## System Architecture

User Input  
   ↓  
Research Agent (Raw Data Generation)  
   ↓  
Summarizer Agent (Data Compression)  
   ↓  
Answer Agent (Final Response)  

This is a sequential pipeline, where each agent processes the output of the previous one.

---

## Key Components

### 1. User Proxy Agent

Acts as the entry point of the system.

- Initiates communication with agents  
- Simulates user interaction  
- Controls execution flow  

---

### 2. Research Agent

Role: Information gathering  

- Generates detailed, factual, and structured data  
- Does not summarize  
- Does not provide final answers  

Purpose:  
To provide rich context for downstream processing  

---

### 3. Summarizer Agent

Role: Data compression  

- Converts raw data into concise bullet points  
- Preserves key concepts  
- Does not add new information  

Purpose:  
To reduce verbosity while maintaining meaning  

---

### 4. Answer Agent

Role: Final response generation  

- Converts summarized data into a coherent explanation  
- Uses a user-friendly tone  
- Does not perform new research  

Purpose:  
To generate the final output for the user  

---

## Core Concepts Implemented

### 1. Role Isolation

Each agent has a clearly defined responsibility:

- Research → Data collection  
- Summarizer → Data compression  
- Answer → Final output  

No agent overlaps with another’s role.

---

### 2. Message Passing

Agents communicate through structured messages.

- Output of one agent becomes input for the next  
- Context is passed explicitly  

---

### 3. Memory Window

A memory window of 10 messages is implemented.

- Only the last 10 interactions are passed to agents  
- Older messages are discarded  

Purpose:

- Reduce token usage  
- Improve efficiency  
- Maintain relevant context  

---

### 4. Context Formatting

Chat history is converted into a structured string format before being passed to agents.

Example:

USER: Query  
RESEARCH: Raw data  
SUMMARY: Compressed data  

This ensures compatibility with the LLM input format.

---

### 5. Controlled Execution

- max_turns = 1 ensures one response per agent  
- Prevents looping  
- Keeps flow deterministic  

---

## Design Decisions

### Why Separate Agents?

- Improves modularity  
- Easier debugging  
- Scalable architecture  

---

### Why Memory Window?

- Prevents context overload  
- Keeps only relevant information  
- Optimizes performance  

---

## Future Improvements

- Introduce agent-to-agent communication  
- Add planner/orchestrator agent  
- Integrate vector memory (FAISS)  
- Enable dynamic task delegation  

---

## Summary

This system demonstrates a foundational multi-agent architecture where:

- Each agent performs a specialized task  
- Data flows sequentially across agents  
- Context is controlled using a memory window  
- Outputs are progressively refined from raw data to final answer  

This design ensures clarity, modularity, and correctness in agent behavior.