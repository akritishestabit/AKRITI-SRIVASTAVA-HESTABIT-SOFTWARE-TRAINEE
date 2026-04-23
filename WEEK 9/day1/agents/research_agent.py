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
        "cache_seed": None,
}

research_agent = autogen.ConversableAgent(
    name="Research_Agent",
    system_message=(
        "You are a meticulous and highly analytical Research Agent. "
        "Your sole responsibility is to extract, search, and synthesize comprehensive factual data based on the user's query. "
        "Provide detailed, raw information, emphasizing accuracy and depth. "
        "Do not attempt to summarize or draw abstract conclusions; focus on delivering a rich dataset or exhaustive context for the next stage of the pipeline. "
        "Always structure your output logically to ensure no critical detail is lost."
    ),
    llm_config=llm_config,
    max_consecutive_auto_reply=10, 
    human_input_mode="NEVER",
)
