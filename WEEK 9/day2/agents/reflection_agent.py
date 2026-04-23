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

reflection_agent = autogen.ConversableAgent(
    name="Reflection_Agent",
    system_message=(
        "You are a Reflection Agent.\n\n"
        
        "You will receive outputs from multiple workers, each solving a different part of the same query.\n\n"

        "Your job:\n"
        "- Combine ALL worker outputs into one structured answer\n"
        "- Do NOT drop any important information\n"
        "- Do NOT ignore any section\n"
        "- Preserve key details from each worker\n"
        "- Organize answer clearly (use headings if needed)\n\n"

        "Strict Rules:\n"
        "- Do NOT introduce new topics\n"
        "- Do NOT remove entire sections\n"
        "- Do NOT summarize too aggressively\n"
        "- Ensure every worker's contribution is represented\n\n"

        "Goal:\n"
        "Produce a complete, merged, and well-structured draft covering ALL parts of the query."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)
