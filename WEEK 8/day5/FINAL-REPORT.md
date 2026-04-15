# Final Report — Day 5

## Build & Deploy Local LLM API

---

## Objective

The objective of this capstone was to convert an optimized local LLM into a deployable microservice. The system was designed to serve a quantized GGUF model through a FastAPI-based inference server, supporting both text generation and conversational interaction.

---

## System Overview

The architecture follows a standard API-driven design:

User → FastAPI Server → Quantized LLM → Response

The system exposes endpoints that allow external clients to interact with the model in real time.

---

## Model Used

* Base Model: TinyLlama
* Fine-tuning: LoRA adapters (Day 2)
* Quantization: GGUF format (Day 3)
* Inference Engine: llama.cpp (CPU-based)

---

## Key Features

* Quantized model for efficient inference
* FastAPI-based microservice architecture
* Two endpoints: `/generate` and `/chat`
* Support for streaming responses
* Prompt templating for structured interaction
* Model caching to avoid repeated loading
* Configurable generation parameters (temperature, top-p, top-k, max_tokens)
* Request ID tracking and logging
* Ready for RAG and agent integration

---

## API Endpoints

### 1. POST /generate

Generates text from a given prompt.

**Input:**

* prompt (string)
* temperature (optional)
* top_p (optional)
* top_k (optional)
* max_tokens (optional)
* stream (optional)

**Output:**

* request_id
* generated response
* token usage statistics

---

### 2. POST /chat

Handles conversational interactions using structured message history.

**Input:**

* messages (list of role-content pairs)
* generation parameters
* stream option

**Output:**

* request_id
* assistant response
* updated conversation context

---

## Core Components

### app.py

Implements the FastAPI server, request handling, middleware logging, streaming responses, and endpoint logic.

### model_loader.py

Handles model caching using a singleton pattern and loads the GGUF model only once to optimize performance.

### config.py

Stores configurable parameters such as model path, default generation settings, and server configuration.

---

## Inference Control Parameters

* Temperature: Controls randomness of output
* Top-p: Nucleus sampling for dynamic token selection
* Top-k: Limits token candidates to top-k probabilities
* Max tokens: Defines maximum output length

These parameters allow fine control over generation quality and diversity.

---

## Streaming Support

Streaming is implemented using `StreamingResponse`, allowing token-by-token output. This reduces perceived latency and improves user experience in real-time applications.

---

## Performance Considerations

* Model caching reduces initialization overhead
* Quantization significantly reduces memory usage
* CPU-based inference enables local deployment without GPU
* Logging and request tracking improve observability

---

## Production Readiness

The system incorporates production-level practices:

* Modular architecture
* Config-driven design
* Logging and request tracing
* Efficient memory usage
* Scalable API structure

---

## Conclusion

The project successfully demonstrates how to transform a trained and optimized LLM into a deployable API service. By integrating quantization, efficient inference, and structured API design, the system is suitable for real-world applications and can be extended for RAG pipelines or agent-based systems.

---

## Key Takeaway

Transforming a model into a production-ready system requires not only optimization but also proper API design, efficient resource handling, and scalable architecture.
