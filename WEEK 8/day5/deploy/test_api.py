import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("--- Testing POST /generate ---")
gen_payload = {
    "prompt": "What is Python?",
    "max_tokens": 50,
    "temperature": 0.7,
    "stream": False
}

response = requests.post(f"{BASE_URL}/generate", json=gen_payload)
print(json.dumps(response.json(), indent=2))
print("\n" + "="*50 + "\n")


print("--- Testing POST /chat ---")
chat_payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful coding tutor."},
        {"role": "user", "content": "Explain what a variable is in 1 sentence."}
    ],
    "max_tokens": 50,
    "temperature": 0.7,
    "stream": False
}

response = requests.post(f"{BASE_URL}/chat", json=chat_payload)
print(json.dumps(response.json(), indent=2))
