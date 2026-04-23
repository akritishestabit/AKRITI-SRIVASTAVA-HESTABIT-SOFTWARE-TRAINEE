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
    "temperature": 0.5,
}

def create_worker(worker_id: str) -> autogen.ConversableAgent: #worker agent creation
    return autogen.ConversableAgent(
        name=f"Worker_{worker_id}",
        system_message=(
            "You are a Worker Agent assigned a specific task.\n"
            "- Execute ONLY the given task\n"
            "- Do not add unrelated information\n"
            "- Be clear and structured\n"
            "- Do not repeat other workers\n"
        ),
        llm_config=llm_config,
        human_input_mode="NEVER",
    )
