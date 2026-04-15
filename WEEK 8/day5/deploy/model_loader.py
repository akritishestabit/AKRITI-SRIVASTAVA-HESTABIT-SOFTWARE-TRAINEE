import os
from llama_cpp import Llama
from config import GGUF_MODEL_PATH

class ModelManager:
    _instance = None

    @classmethod
    def get_model(cls):
        if cls._instance is None:
            if not os.path.exists(GGUF_MODEL_PATH):
                raise FileNotFoundError(f"GGUF model not found at {GGUF_MODEL_PATH}. Make sure it is compiled correctly from Day 3!")
                
            print(f"Loading GGUF model from {GGUF_MODEL_PATH}...")
           
            cls._instance = Llama(
                model_path=GGUF_MODEL_PATH,
                n_ctx=2048,
                n_gpu_layers=0, 
                verbose=False
            )
        return cls._instance

def apply_chat_template(messages):
    """
    Takes an array of dicts: [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
    And formats it cleanly into TinyLlama's native chat format for continuous interaction.
    """
    prompt = ""
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if role == "system":
            prompt += f"<|system|>\n{content}</s>\n"
        elif role == "user":
            prompt += f"<|user|>\n{content}</s>\n"
        elif role == "assistant":
            prompt += f"<|assistant|>\n{content}</s>\n"
    
    
    if messages and messages[-1].get("role") != "assistant":
        prompt += "<|assistant|>\n"
        
    return prompt
