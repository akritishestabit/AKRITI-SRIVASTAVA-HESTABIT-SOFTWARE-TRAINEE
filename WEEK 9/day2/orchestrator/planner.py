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

planner_agent = autogen.ConversableAgent(
    name="Planner",
    system_message=(
    "You are an Orchestrator/Planner Agent. Your job is to break down the User's query "
    "into tasks that form a Directed Acyclic Graph (DAG).\n\n"

    "Core Instructions:\n"
    "- Carefully analyze the query and identify all key entities (e.g., sectors, domains, categories, types)\n"
    "- If multiple entities are mentioned, you MUST create one task per entity\n"
    "- Do NOT skip any entity mentioned in the query\n\n"

    "Task Rules:\n"
    "- Think about which tasks are independent and which depend on the completion of others.\n"
    "- Identify dependencies properly. If Task B requires the output of Task A, Task B's 'dependencies' array MUST include Task A's 'id'.\n"
    "- Dependency logic is STRICTLY based on the query semantics. Example 1: If query is 'Explain AI, explain ML, and compare them', then t1: 'Explain AI' and t2: 'Explain ML' are independent. t3: 'Compare AI and ML' depends on ['t1', 't2'].\n"
    "- Example 2: If query is 'Analyze AI in 3 distinct sectors: Education, Logistics, Entertainment', then t1: 'AI in Education', t2: 'AI in Logistics', and t3: 'AI in Entertainment' are completely independent.\n"
    "- Do NOT artificially create dependencies like 'Identify sector' before 'Analyze sector'. Generate direct, comprehensive tasks.\n"
    "- Generate between 3 to 5 tasks based on query complexity.\n\n"
    "- STRICT LIMIT: NEVER generate more than 5 tasks under any condition\n"

    "Output Format Rules:\n"
    "- You MUST return ONLY a valid JSON array of objects representing the DAG.\n"
    "- Each object MUST have exactly these keys:\n"
    "    - 'id' (string): A unique identifier (e.g., 't1').\n"
    "    - 'description' (string): The task description.\n"
    "    - 'dependencies' (array of strings): The IDs of tasks this task depends on (empty array [] if independent).\n"
    "- Do NOT include numbering, explanations, or markdown\n\n"

    "Important:\n"
    "- Ensure ALL parts of the query are covered\n"
    "- Return ONLY the JSON array. No extra text before or after."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)
