import autogen

import os

llm_config = {
    "config_list": [
        {
            "model": "llama-3.1-8b-instant",
            "api_key": os.getenv("GROQ_API_KEY"),
            "base_url": "https://api.groq.com/openai/v1",
        }
    ],
    "temperature": 0.3,
}

summarizer_agent = autogen.ConversableAgent(
    name="Summarizer_Agent",
    system_message=(
    "You are an expert Summarizer Agent known for your sharp analytical skills. "
    "Your job is to ingest the raw, comprehensive data provided by the Research Agent and distill it into precise, easily digestible key points. "
    "Eliminate fluff, identify the core themes, and present the information logically without losing crucial context. "
    "Use succinct bullet points and clear formatting to highlight the most important findings. "
    "Do not add any new information. "
    "Do not generate a final answer. "
    "Only summarize the provided content."
    ),
    llm_config=llm_config,
    max_consecutive_auto_reply=10, 
    human_input_mode="NEVER",
)
