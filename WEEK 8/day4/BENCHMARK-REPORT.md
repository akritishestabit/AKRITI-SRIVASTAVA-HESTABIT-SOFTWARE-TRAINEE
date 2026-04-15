# Benchmark Report — Day 4

## Objective

Compare inference performance of base, fine-tuned, and quantized models across different tasks.

---

## Metrics

* Tokens per second (speed)
* Latency (response time)
* Memory usage
* Accuracy (manual evaluation)

---

## Results

| Model      | Task       | Tokens/sec | Latency (s) | Memory              | Accuracy |
| ---------- | ---------- | ---------- | ----------- | ------------------- | -------- |
| Base       | QA         | 4.47       | 11.18       | ~4.1 GB (GPU VRAM)  | Good     |
| Base       | Reasoning  | 4.36       | 11.46       | ~4.1 GB (GPU VRAM)  | Good     |
| Base       | Extraction | 3.95       | 9.62        | ~4.1 GB (GPU VRAM)  | Good     |
| Fine-tuned | QA         | 4.95       | 10.10       | ~4.21 GB (GPU VRAM) | Good     |
| Fine-tuned | Reasoning  | 4.52       | 11.07       | ~4.22 GB (GPU VRAM) | Good     |
| Fine-tuned | Extraction | 3.36       | 2.08        | ~4.22 GB (GPU VRAM) | Good     |
| GGUF       | QA         | 11.82      | 2.43        | ~1.96 GB (CPU RAM)  | Good     |
| GGUF       | Reasoning  | 17.56      | 2.85        | ~1.96 GB (CPU RAM)  | Good     |
| GGUF       | Extraction | 9.80       | 1.53        | ~1.96 GB (CPU RAM)  | Good     |

---

## Observations

* Base and fine-tuned models use GPU and consume higher VRAM (~4 GB).
* GGUF runs on CPU and uses significantly lower memory (~1.96 GB).
* GGUF shows much lower latency due to lightweight quantized execution.
* Fine-tuned model slightly improves task-specific responses over base model.
* Higher tokens/sec in GGUF (especially QA) may be influenced by shorter outputs and efficient decoding.

---

## Trade-offs

| Model      | Strength                      | Limitation                       |
| ---------- | ----------------------------- | -------------------------------- |
| Base       | Stable baseline               | High latency and VRAM usage      |
| Fine-tuned | Better task performance       | Similar memory cost              |
| GGUF       | Low memory and fast inference | Possible minor quality trade-off |

---

## Conclusion

Quantized GGUF model provides the best efficiency in terms of speed and memory, making it suitable for deployment on resource-constrained systems.
Fine-tuned models improve performance on specific tasks, while the base model serves as a reliable reference.
