# Dataset Analysis — Week 8 Day 1

## Overview
This dataset is created for instruction fine-tuning of a Large Language Model (LLM) in the coding domain. It includes diverse samples across QA, reasoning, and extraction tasks.

---

## Dataset Composition

### Raw Dataset
- Total Samples: 1430

### Types:
- QA: ~400
- Reasoning (Arithmetic): ~350
- Reasoning (Logic-based): ~200
- Extraction: ~200
- Complex Reasoning: ~150
- Very Long Explanations: ~120
- Noise + Low-quality Samples: ~160

---

## Data Cleaning

Cleaning steps performed:
- Removed empty instruction/output samples
- Removed low-quality responses (e.g., "ok", "yes", "done")
- Removed very short outputs (< 4 tokens)
- Removed very short inputs

### After Cleaning:
- Total Samples: 1150

---

## Token Length Analysis

Token length was computed using whitespace-based splitting.

### Statistics:
- Average Length: ~24 tokens
- Minimum Length: 19 tokens
- Maximum Length: 45 tokens

### Observations:
- Dataset shows balanced distribution
- Short/noisy samples successfully removed
- Presence of moderate-length reasoning samples

---

## Outlier Removal

- Threshold: 40 tokens
- Samples exceeding threshold were removed

### After Outlier Removal:
- Final Samples: 1100
- Removed Samples: 50

---

## Train/Validation Split

- Train: ~90% → ~990 samples
- Validation: ~10% → ~110 samples

### Final Files:
- data/train.jsonl
- data/val.jsonl

---

## Key Insights

- Dataset is diverse across multiple instruction types
- Noise injection improved cleaning validation
- Token distribution is well-balanced for fine-tuning
- Outlier filtering ensures stable training behavior

---

## Conclusion

This dataset is clean, diverse, and domain-specific. It is well-suited for efficient LLM fine-tuning using techniques like LoRA/QLoRA on limited computational resources.