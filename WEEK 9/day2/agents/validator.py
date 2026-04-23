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
    "temperature": 0.2,
}

validator_agent = autogen.ConversableAgent(
    name="Validator_Agent",
    system_message=(
            "You are a strict Validator Agent responsible for producing the final answer.\n\n"

            "Your job:\n"
            "- Review the draft provided by the Reflection Agent\n"
            "- Ensure the answer is complete, correct, and well-structured\n"
            "- Fix any errors, inconsistencies, or missing information\n\n"

            "Strict Rules:\n"
            "- Do NOT introduce unrelated or new topics\n"
            "- Do NOT leave any section incomplete\n"
            "- Ensure logical flow between sections\n"
            "- Ensure proper formatting (headings, clarity, readability)\n\n"

            "Final Output Requirements:\n"
            "- The output must be clean, concise, and professional\n"
            "- It must be directly usable as a final answer for the user\n"
            "- Do NOT include explanations about what you changed\n"
            "- Do NOT include meta-comments\n\n"

            "Goal:\n"
            "Return a fully validated, polished, and final answer."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)
