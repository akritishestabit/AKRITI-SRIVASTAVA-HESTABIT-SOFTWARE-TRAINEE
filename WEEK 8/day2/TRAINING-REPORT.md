# TRAINING REPORT — DAY 2 (QLoRA Fine-Tuning)

## Objective

The objective of this task was to fine-tune a pre-trained Large Language Model (LLM) using Parameter-Efficient Fine-Tuning (PEFT), specifically QLoRA, on a custom dataset created in Day 1.

---

## Approach

Instead of training the entire model, which is computationally expensive, we used QLoRA to update only a small subset of parameters. This approach significantly reduces memory usage and training time while still allowing the model to adapt effectively to the dataset.

---

## Model Details

* Base Model: TinyLlama-1.1B-Chat-v1.0
* Fine-Tuning Technique: QLoRA (4-bit quantization)
* Task Type: Causal Language Modeling

---

## Training Configuration

| Parameter     | Value                |
| ------------- | -------------------- |
| LoRA Rank (r) | 16                   |
| LoRA Alpha    | 32                   |
| LoRA Dropout  | 0.05                 |
| Learning Rate | 2e-4                 |
| Batch Size    | 4                    |
| Epochs        | 3                    |
| Precision     | FP16                 |
| Quantization  | 4-bit (BitsAndBytes) |

---

## Dataset

The dataset used for training was generated in Day 1 and follows an Instruction–Input–Output format.

Preprocessing steps included:

* Removing invalid or empty samples
* Filtering out very short or low-quality outputs
* Tokenizing the data
* Adding labels for proper loss computation

---

## Training Process

The model was trained using the Hugging Face Trainer API. During training:

* Input text was tokenized
* Labels were set equal to input_ids for causal language modeling
* Loss was computed and minimized using backpropagation
* Training was performed over multiple epochs

---

## Training Results

* Final Training Loss: approximately 0.20
* Epochs Completed: 3
* Training Steps: 744

A low training loss indicates that the model has successfully learned patterns from the dataset and is able to generate relevant responses.

---

## Output Artifacts

The following files were generated after training:

```
adapters/
 ├── adapter_model.safetensors
 ├── adapter_config.json
 ├── tokenizer.json
 ├── tokenizer_config.json
 ├── chat_template.jinja
```

The adapter_model.safetensors file contains the trained LoRA weights and represents the learned knowledge from fine-tuning.

---

## Inference Test

The model was tested using a sample prompt:

Input:

```
What is a function?
```

Output:

```
A function is a reusable block of code. This concept is widely used in programming.
```

The output demonstrates that the model is able to generate correct and meaningful responses based on the training data.

---

## Key Learnings

* Parameter-efficient fine-tuning allows training large models with limited resources
* QLoRA enables memory-efficient training using quantization
* Proper dataset formatting and label assignment are essential for successful training
* Monitoring loss helps evaluate model performance

---

## Conclusion

The fine-tuning process was successfully completed. The model adapted well to the custom dataset while using minimal computational resources. QLoRA proved to be an effective and efficient approach for fine-tuning large language models.

---

## Future Improvements

* Increase dataset diversity for better generalization
* Introduce evaluation metrics such as BLEU or ROUGE
* Experiment with different LoRA hyperparameters
* Implement validation-based early stopping

---
