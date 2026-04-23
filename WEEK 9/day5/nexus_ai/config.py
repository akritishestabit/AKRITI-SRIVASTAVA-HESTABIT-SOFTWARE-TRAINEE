import os

api_key = os.getenv("GROQ_API_KEY", "dummy_key")

llm_config = {
    "config_list": [
        {
            "model": "llama-3.1-8b-instant",
            "api_key": api_key,
            "base_url": "https://api.groq.com/openai/v1"
        }
    ],
    "temperature": 0.2,
    "timeout": 300,
    "max_tokens": 1000
}
