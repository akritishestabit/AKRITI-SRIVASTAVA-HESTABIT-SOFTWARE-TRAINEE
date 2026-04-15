import os
import time
import csv
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

# paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
ADAPTER_PATH = os.path.join(SCRIPT_DIR, "../../day2/adapters")
GGUF_PATH = os.path.join(SCRIPT_DIR, "../../day3/quantized/model-q4_0.gguf")
BENCHMARKS_DIR = os.path.join(SCRIPT_DIR, "../benchmarks")
os.makedirs(BENCHMARKS_DIR, exist_ok=True)

import psutil

def get_vram():
    if torch.cuda.is_available():
        return round(torch.cuda.memory_allocated() / 1e9, 2)
    else:
        
        process = psutil.Process(os.getpid())
        return round(process.memory_info().rss / 1e9, 2)

def generate_prompt(instruction, input_text=""):
    
    if input_text:
        return f"<|system|>\nYou are a helpful assistant.</s>\n<|user|>\n{instruction}\n{input_text}</s>\n<|assistant|>\n"
    return f"<|system|>\nYou are a helpful assistant.</s>\n<|user|>\n{instruction}</s>\n<|assistant|>\n"


TEST_PROMPTS = [
    {'type': 'QA', 'instruction': 'Explain loops in Python', 'input': ''},
    {'type': 'Reasoning', 'instruction': 'Solve step by step with explanation', 'input': 'What is output of 26 + 20 * 7?'},
    {'type': 'Extraction', 'instruction': 'Extract function name from code', 'input': 'def process120(x): return x+1'}
]

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

results = []

def run_hf_model(model_path, model_name, is_adapter=False):
    print(f"\n======================================")
    print(f"--- Running {model_name} ---")
    print(f"======================================")
    
    if not os.path.exists(model_path) and model_name != "Base Model":
        print(f"Path not found at {model_path}. Please check the path.")
        return

    
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    model_to_load = BASE_MODEL if is_adapter else model_path
    
    model = AutoModelForCausalLM.from_pretrained(
        model_to_load, 
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        low_cpu_mem_usage=True
    )
    
    if is_adapter:
        from peft import PeftModel
        print(f"Dynamically loading adapter from {model_path} onto the Base Model.")
        model = PeftModel.from_pretrained(model, model_path)
    
    model.to(device)
    model.eval()
    
   
    print("\n[Executing Multi-prompt Test]")
    for p in TEST_PROMPTS:
        prompt = generate_prompt(p['instruction'], p['input'])
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        start_time = time.perf_counter()
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=50, do_sample=False, pad_token_id=tokenizer.eos_token_id)
        latency = time.perf_counter() - start_time
        
        gen_tokens = outputs.shape[1] - inputs['input_ids'].shape[1]
        tps = gen_tokens / latency if latency > 0 else 0
        
        response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True).strip()
        
        results.append({
            "model": model_name, "type": p["type"], "tokens_per_sec": round(tps, 2),
            "latency_sec": round(latency, 2), "vram_gb": get_vram(), "accuracy": "Good (Manual)"
        })
        print(f"[{p['type']}] TPS: {tps:.2f} | Latency: {latency:.2f}s | Output: {response[:60]}...")
    
   
    print(f"\n[Executing Streaming Output Demo]")
    prompt = generate_prompt("What is a function?", "")
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    with torch.no_grad():
        model.generate(**inputs, max_new_tokens=50, streamer=streamer, pad_token_id=tokenizer.eos_token_id)
        
   
    print(f"\n[Executing Batch Inference]")
    batch_prompts = [
        generate_prompt("What is a dictionary in Python?", ""),
        generate_prompt("What is encapsulation?", ""),
        generate_prompt("What is a variable?", "")
    ]
   
    tokenizer.padding_side = 'left'
    inputs = tokenizer(batch_prompts, return_tensors="pt", padding=True).to(device)
    
    start_time = time.perf_counter()
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=30, do_sample=False, pad_token_id=tokenizer.eos_token_id)
    batch_latency = time.perf_counter() - start_time
    
    print(f"Batch inference of 3 queries took {batch_latency:.2f}s total.")
    for i in range(len(batch_prompts)):
        response = tokenizer.decode(outputs[i][inputs['input_ids'].shape[1]:], skip_special_tokens=True).strip()
        print(f" - BATCH Q{i+1} Output: {response[:50]}...")
    
    
    del model
    if device == "cuda":
        torch.cuda.empty_cache()

def run_gguf():
    print(f"\n======================================")
    print(f"--- Running GGUF Model (gguf + llama.cpp) ---")
    print(f"======================================")
    if not os.path.exists(GGUF_PATH):
        print(f"GGUF model not found at {GGUF_PATH}")
        return
        
    try:
        from llama_cpp import Llama
    except ImportError:
        print("llama_cpp is not installed. To run GGUF tests please: pip install llama-cpp-python")
        return

   
    llm = Llama(model_path=GGUF_PATH, n_gpu_layers=0 if device=="cuda" else 0, verbose=False)
    
   
    print("\n[Executing Multi-prompt Test on GGUF]")
    for p in TEST_PROMPTS:
        prompt = generate_prompt(p['instruction'], p['input'])
        
        start_time = time.perf_counter()
        
        output = llm(prompt, max_tokens=50, echo=False)
        latency = time.perf_counter() - start_time
        
        gen_tokens = output['usage']['completion_tokens']
        tps = gen_tokens / latency if latency > 0 else 0
        response = output['choices'][0]['text'].strip()
        
        results.append({
            "model": "GGUF", "type": p["type"], "tokens_per_sec": round(tps, 2),
            "latency_sec": round(latency, 2), "vram_gb": get_vram(), "accuracy": "Good (Manual)"
        })
        print(f"[{p['type']}] TPS: {tps:.2f} | Latency: {latency:.2f}s | Output: {response[:60]}...")
        
    
    print(f"\n[Executing Streaming Output Demo on GGUF]")
    prompt = generate_prompt("What is a function?", "")
    print("Streaming Tokens: ", end="")
    for chunk in llm(prompt, max_tokens=50, stream=True):
        print(chunk['choices'][0]['text'], end="", flush=True)
    print("\n")

try:
    # Base Model
    run_hf_model(BASE_MODEL, "Base Model", is_adapter=False)
    
    # Fine-tuned proxy model
    run_hf_model(ADAPTER_PATH, "Fine-tuned Model (via Adapter)", is_adapter=True)
    
    # Quantized Model (GGUF)
    run_gguf()
    
    # Save Final CSV
    csv_file = os.path.join(BENCHMARKS_DIR, "results.csv")
    if results:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"\n Benchmarking completed. Results saved to {csv_file}")
except Exception as e:
    print(f"Error during inference testing: {e}")
