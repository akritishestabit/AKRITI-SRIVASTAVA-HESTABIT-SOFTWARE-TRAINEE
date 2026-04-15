# Quantisation Report

## Objective

The goal of this task was to reduce the memory footprint of the fine-tuned language model while preserving response quality. This was done by converting the merged FP16 model into INT8, INT4, and GGUF (q4_0) formats and comparing their size, inference speed, and output quality.

## Process Followed

### 1. Model Merge

* Loaded the base model and LoRA adapter from Day 2.
* Merged adapter weights into the base model.
* Saved the merged full-precision model.

### 2. INT8 Quantisation

* Loaded the merged model using 8-bit quantisation.
* Saved the quantised INT8 model.

### 3. INT4 Quantisation

* Loaded the merged model using 4-bit quantisation with BitsAndBytes.
* Saved the quantised INT4 model.

### 4. GGUF Conversion

* Used llama.cpp to convert the merged model to GGUF format.
* Applied q4_0 quantisation for CPU-friendly inference.
* Saved the GGUF model file.

## Quantisation Comparison

| Format    | Size   | Inference Time | Quality                  |
| --------- | ------ | -------------- | ------------------------ |
| FP16      | 2.1 GB | 1.79 sec       | Very Good                |
| INT8      | 1.2 GB | 2.69 sec       | Very Good                |
| INT4      | 774 MB | 1.14 sec       | Very Good                |
| GGUF q4_0 | 608 MB | 10.4 tok/s     | Best (Detailed Response) |

## Key Observations

* FP16, INT8, and INT4 generated accurate and meaningful responses with minimal quality difference.
* INT8 reduced model size significantly while maintaining output quality.
* INT4 provided strong compression and faster GPU inference than INT8 in this setup.
* GGUF q4_0 was the most memory-efficient format and produced the most detailed response during testing.
* GGUF took longer on first load because llama.cpp had to initialize the model.
* Overall, quantisation reduced storage and memory usage while preserving useful model performance.

## Conclusion

Quantisation was successful across all formats. The model size was reduced significantly without noticeable quality loss for standard prompts. INT4 provided the best balance between speed and size on GPU, while GGUF was the best choice for lightweight CPU deployment.
