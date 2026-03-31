# Multimodal RAG (Day 3)

## Goal

The goal of Day 3 is to extend the system from text-only retrieval to multimodal retrieval.

This means the system should be able to:
- Work with images
- Understand images
- Retrieve images using queries

---

## What is Multimodal RAG?

In previous days, the system handled only text.

Text → Retrieve → Context

Now, we extend it to:

Text + Image → Retrieve → Context

---

## Core Idea

An image is converted into multiple forms so that it can be searched and understood:

- Text (using OCR)
- Description (using captioning)
- Vector (using embeddings)

---

## Pipeline

Image → OCR → Caption → Embedding → Store

---

## Components

### 1. OCR (Optical Character Recognition)

- Extracts text from images
- Useful for numbers, tables, IDs, and scanned documents

Example:
An image with "1x1 = 1" will be converted into text

---

### 2. Image Captioning

- Generates a description of the image
- Helps understand what the image represents

Example:
"A multiplication table"

---

### 3. CLIP Embeddings

- Converts both images and text into vectors
- Allows comparison between text and images

Important:
Text and image embeddings are in the same vector space

---

## Image Storage

Each image is stored with:

- Image name
- OCR text
- Caption
- Embedding (vector representation)

Example:

{
  "image": "test.jpg",
  "ocr_text": "...",
  "caption": "...",
  "embedding": [512 values]
}

---

## Query Modes

### 1. Text → Image

- User gives a text query
- Converted into embedding
- Compared with image embeddings
- Top matching images are returned

---

### 2. Image → Image

- User provides an image
- Converted into embedding
- Compared with stored image embeddings
- Similar images are returned

---

### 3. Image → Text Answer

- Input image is analyzed
- Similar images are retrieved (top_k)
- OCR text and captions are combined
- A descriptive answer is generated

---

## Similarity Calculation

Cosine similarity is used to compare embeddings.

Higher similarity score means better match.

---

## Key Understanding

- One image is represented as one embedding
- Each embedding has fixed size (e.g., 512 values)
- Retrieval happens by comparing embeddings

---

## Limitations

- OCR may not work well on noisy or colored images
- Captions may not always be accurate
- Exact matching of numbers is not guaranteed

---

## Final Outcome

The system can now:

- Search images using text
- Find similar images
- Generate text-based explanations from images

---

## Final Summary

OCR extracts text  
Captioning explains the image  
CLIP enables comparison  

