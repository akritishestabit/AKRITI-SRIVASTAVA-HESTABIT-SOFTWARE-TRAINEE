# Multimodal RAG (Image + Text Retrieval System)

## Overview

This project extends traditional RAG (Retrieval-Augmented Generation) by adding support for images. Instead of working with only text, the system can now process, understand, and retrieve information from images using OCR, captioning, and embeddings.

The goal is to make images searchable and usable in a retrieval pipeline just like text.

---

## What the System Does

The system processes images and extracts three types of information:

1. **OCR Text** – Extracts text written inside the image
2. **Caption** – Generates a natural language description of the image
3. **Embedding** – Converts the image into a vector representation

All of this information is stored and later used for search and retrieval.

---

## Pipeline Architecture

### 1. Image Ingestion

Each image goes through the following steps:

* OCR extracts text from the image
* BLIP generates a caption (description)
* CLIP generates an embedding (vector)

The output is stored in a structured format:

```
{
  "id": 0,
  "image": "diagram.png",
  "ocr_text": "Pressure = Force / Area",
  "caption": "A diagram showing pressure formula",
  "embedding": [ ... ]
}
```

All entries are saved in a JSON file (`image_chunks.json`).

---

### 2. Multimodal Retrieval

The system supports three types of queries:

#### Text → Image

User provides a text query.
The system converts it into an embedding and finds similar images.

#### Image → Image

User provides an image.
The system finds visually similar images using embeddings.

#### Image → Text

User provides an image.
The system retrieves similar images and combines their captions and OCR text to generate a readable answer.

---

## Core Components

### CLIP Embedder

* Converts both images and text into embeddings
* Ensures both are in the same vector space
* Enables cross-modal search (text ↔ image)

### OCR Extractor (Tesseract)

* Extracts text from images
* Uses preprocessing (resize, thresholding, noise removal)
* Includes fallback mechanism for difficult images

### Caption Generator (BLIP)

* Generates human-like descriptions of images
* Helps in understanding image context beyond raw text

### Image Ingest Pipeline

* Orchestrates OCR, captioning, and embedding
* Stores processed data in JSON format

### Image Search Engine

* Performs similarity search using cosine similarity
* Supports multiple query modes

---

## Similarity Search

The system uses **cosine similarity** to compare embeddings:

* Higher score → more similar
* Lower score → less similar

This allows meaningful matching between:

* text and image
* image and image

---

## Key Design Decisions

* Used CLIP to unify image and text into a shared embedding space
* Stored embeddings with metadata (caption + OCR text)
* Implemented fallback OCR for robustness
* Used simple JSON storage for transparency and debugging

---


## Future Improvements

* Add FAISS for faster vector search
* Integrate LLM for better answer generation
* Improve OCR with advanced engines (EasyOCR / PaddleOCR)
* Add metadata filtering and ranking strategies

---

## Summary

This system converts images into searchable knowledge by combining:

* OCR for text extraction
* Captioning for context
* Embeddings for similarity search

It enables a complete multimodal retrieval pipeline where images can be searched, compared, and understood alongside text.
