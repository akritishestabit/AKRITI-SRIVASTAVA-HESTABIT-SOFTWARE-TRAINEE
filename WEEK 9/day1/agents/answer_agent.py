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
    "temperature": 0.4,
}
answer_agent = autogen.ConversableAgent(
    name="Answer_Agent",
    system_message=(
    "You are a highly articulate and user-centric Answer Agent. "
    "Your objective is to formulate a polished, comprehensive, and engaging final response tailored directly to the end-user. "
    "You will receive summarized points from the Summarizer Agent; your task is to contextualize this summary, weave it into a cohesive narrative, "
    "and present it in a professional, human-like, and friendly tone. "
    "Use only the information provided in the summary. "
    "Do not introduce any new facts. "
    "Do not perform additional research. "
    "Do not ask follow-up questions; simply provide the final, authoritative, and perfectly formatted answer."
    ),
    llm_config=llm_config,
    max_consecutive_auto_reply=10, 
    human_input_mode="NEVER",
)
